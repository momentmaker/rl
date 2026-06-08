#!/usr/bin/env python3
"""Hermes preprocessor for the Random Learning daily poster.

Runs as the `--script` of a Hermes cron job. It does all the deterministic work
(find today's entry, check it's gate-approved, extract the post bodies, enforce
post-once) and prints a small contract that the Hermes agent acts on:

  STATUS: POST      -> agent calls post_tweet(TWEET) and delivers TELEGRAM to TG
  STATUS: NO_ENTRY  -> agent delivers the ALERT line to TG (daily heartbeat)
  STATUS: SILENT    -> already handled today; agent replies [SILENT] (no delivery)

State is local (~/.local/state/rl-poster/posted-<date>), written optimistically
when a payload is handed off so the job never double-posts on a re-run. A failed
post is surfaced by the agent's TG message; to retry, delete the marker and
`hermes cron run`.

Install: symlinked into ~/.hermes/scripts/ (Hermes requires --script there); the
canonical copy lives here in the repo. Test overrides: RL_POST_DATE=YYYY/MM/DD,
RL_POST_DRY_RUN=1 (skip the marker write), RL_REPO=<path>.
"""

from __future__ import annotations

import os
import re
from datetime import date
from pathlib import Path

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def _repo() -> Path:
    if os.environ.get("RL_REPO"):
        return Path(os.environ["RL_REPO"])
    return Path(__file__).resolve().parents[1]  # ops/ -> repo root (resolves symlink)


def _state_dir() -> Path:
    return Path(os.environ.get("RL_POST_STATE")
                or (Path.home() / ".local" / "state" / "rl-poster"))


def _today() -> str:
    return os.environ.get("RL_POST_DATE") or date.today().strftime("%Y/%m/%d")


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


def _emit(*lines: str) -> None:
    print("\n".join(lines))


def main() -> int:
    tp = _today()                      # 2026/06/07
    iso = tp.replace("/", "-")         # 2026-06-07
    day = _repo() / "data" / tp
    tweet_f, tg_f = day / "tweet.md", day / "telegram.md"
    marker = _state_dir() / f"posted-{iso}"
    dry = os.environ.get("RL_POST_DRY_RUN") == "1"

    if marker.exists():
        _emit("RL-POST v1", "STATUS: SILENT")
        return 0

    if not (tweet_f.exists() and tg_f.exists()):
        _emit("RL-POST v1", "STATUS: NO_ENTRY", f"DATE: {iso}",
              f"ALERT: [rl] No entry to post for {iso} - the daily run produced "
              f"nothing (low fuel, gate fail, or it hasn't finished). No "
              f"tweet/telegram under data/{tp}.")
        return 0  # no marker on no-entry, so a late entry can still be posted

    tweet_fm, tweet_body = _split_frontmatter(tweet_f.read_text(encoding="utf-8"))
    tg_fm, tg_body = _split_frontmatter(tg_f.read_text(encoding="utf-8"))
    if tweet_fm.get("ready") != "true" or tg_fm.get("ready") != "true":
        _emit("RL-POST v1", "STATUS: NO_ENTRY", f"DATE: {iso}",
              f"ALERT: [rl] Entry for {iso} exists but is not marked ready - not posting.")
        return 0

    if not dry:
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(date.today().isoformat() + "\n", encoding="utf-8")

    _emit("RL-POST v1", "STATUS: POST", f"DATE: {iso}",
          "--- TWEET ---", tweet_body,
          "--- TELEGRAM ---", tg_body,
          "--- END ---")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
