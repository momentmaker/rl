#!/usr/bin/env python3
"""Deterministic poster for the Random Learning daily entry (Hermes --no-agent).

Runs as a Hermes cron `--script` in **--no-agent** mode: there is no LLM. This
script finds today's gate-approved entry, posts the tweet by driving the
already-logged-in Chrome over CDP (port 9222, the same path the x-poster plugin
uses), writes a post-once marker only on a confirmed success, and prints the
Telegram body to stdout — which Hermes delivers to Telegram verbatim. Empty
stdout is a silent run (no message).

Why no agent: the LLM path failed twice in production — a model-API broken pipe
(2026-06-10) and the model improvising a stale-token `xurl` call instead of the
post_tweet tool (2026-06-11). The post is mechanical (fixed text in, one tool
call), so removing the model removes that whole class of failure and makes
marker-on-success deterministic.

stdout contract (Hermes --no-agent: non-empty stdout -> delivered, empty ->
silent, non-zero exit -> error alert):
  - already posted today (marker)      -> print nothing            (silent)
  - posted just now                    -> print the Telegram body  (delivered)
  - post failed                        -> print "[rl] tweet FAILED ..."
  - no entry / not ready, primary mode -> print the heartbeat ALERT
  - no entry / not ready, backup mode  -> print nothing            (silent)

Modes (env RL_POST_MODE): primary (default) alerts on no-entry; backup retries a
failed primary and stays silent on no-entry so it can't double-alert.

Runs under the Hermes venv python (has playwright). Test overrides:
RL_POST_DATE=YYYY/MM/DD, RL_POST_STATE=<dir>, RL_REPO=<path>,
RL_POST_DRY_RUN=1 (skip the real post + marker; print what would go out).
"""

from __future__ import annotations

import os
import re
import sys
from datetime import date
from pathlib import Path

CDP_URL = "http://localhost:9222"
TWEET_MAX = 280
_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def _repo() -> Path:
    if os.environ.get("RL_REPO"):
        return Path(os.environ["RL_REPO"])
    return Path(__file__).resolve().parents[1]


def _state_dir() -> Path:
    return Path(os.environ.get("RL_POST_STATE")
                or (Path.home() / ".local" / "state" / "rl-poster"))


def _today() -> str:
    return os.environ.get("RL_POST_DATE") or date.today().strftime("%Y/%m/%d")


def _is_backup() -> bool:
    return os.environ.get("RL_POST_MODE", "").lower() == "backup"


def _split_frontmatter(text: str) -> tuple[dict, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}, text.strip()
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2).strip()


def post_tweet_via_cdp(text: str) -> tuple[bool, str]:
    """Post one tweet by driving the logged-in Chrome on the CDP debug port.

    Mirrors the x-poster plugin: attach to the EXISTING Chrome, open a new page
    on the compose URL, fill, click tweet, then close only our page (never the
    browser). Returns (ok, detail).
    """
    import asyncio

    async def _run() -> tuple[bool, str]:
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            browser = await p.chromium.connect_over_cdp(CDP_URL)
            context = browser.contexts[0] if browser.contexts else await browser.new_context()
            page = await context.new_page()
            try:
                await page.goto("https://x.com/compose/post", wait_until="domcontentloaded")
                box = page.get_by_role("textbox").first
                await box.click()
                await box.fill(text)
                try:
                    await page.get_by_test_id("tweetButton").click(timeout=5000)
                except Exception:
                    await page.get_by_test_id("tweetButtonInline").click(timeout=5000)
                await page.wait_for_timeout(2500)
                return True, "posted"
            finally:
                await page.close()

    try:
        return asyncio.run(_run())
    except Exception as e:
        return False, (f"{type(e).__name__}: {e}. Is Chrome on :9222 running and "
                       f"logged into x.com?")


def main() -> int:
    tp = _today()                      # 2026/06/11
    iso = tp.replace("/", "-")
    day = _repo() / "data" / tp
    tweet_f, tg_f = day / "tweet.md", day / "telegram.md"
    marker = _state_dir() / f"posted-{iso}"
    dry = os.environ.get("RL_POST_DRY_RUN") == "1"

    if marker.exists():
        return 0  # already posted today -> silent (no stdout)

    if not (tweet_f.exists() and tg_f.exists()):
        if not _is_backup():
            print(f"[rl] No entry to post for {iso} - the daily run produced "
                  f"nothing (low fuel, gate fail, or it hasn't finished).")
        return 0  # backup: silent (primary already alerted)

    tweet_fm, tweet_body = _split_frontmatter(tweet_f.read_text(encoding="utf-8"))
    tg_fm, tg_body = _split_frontmatter(tg_f.read_text(encoding="utf-8"))
    if tweet_fm.get("ready") != "true" or tg_fm.get("ready") != "true":
        if not _is_backup():
            print(f"[rl] Entry for {iso} exists but is not marked ready - not posting.")
        return 0

    if len(tweet_body) > TWEET_MAX:
        print(f"[rl] tweet FAILED: body is {len(tweet_body)} chars, over the "
              f"{TWEET_MAX} limit; not posting {iso}.")
        return 0

    if dry:
        print(f"[DRY] would post tweet ({len(tweet_body)} chars) for {iso}, then "
              f"deliver:\n\n{tg_body}")
        return 0

    ok, detail = post_tweet_via_cdp(tweet_body)
    if not ok:
        # No marker on failure -> the backup run (or a manual re-fire) retries.
        print(f"[rl] tweet FAILED for {iso}: {detail}")
        return 0

    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(date.today().isoformat() + "\n", encoding="utf-8")
    print(tg_body)  # delivered to Telegram
    return 0


if __name__ == "__main__":
    sys.exit(main())
