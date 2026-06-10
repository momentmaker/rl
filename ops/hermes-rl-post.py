#!/usr/bin/env python3
"""Hermes preprocessor for the Random Learning daily poster.

Runs as the `--script` of a Hermes cron job. It does all the deterministic work
(find today's entry, check it's gate-approved, extract the post bodies, decide
whether today is already done) and prints a small contract the agent acts on:

  STATUS: POST      -> agent calls post_tweet(TWEET), delivers TELEGRAM to TG, and
                       ONLY on a successful post writes the MARKER file (post-once).
  STATUS: NO_ENTRY  -> agent delivers the ALERT line to TG (daily heartbeat).
  STATUS: SILENT    -> already posted today (marker exists); agent replies [SILENT]
                       which Hermes treats as a delivery-suppression sentinel.

Idempotency is **mark-on-success**: the marker (~/.local/state/rl-poster/posted-
<date>) is written by the agent AFTER post_tweet succeeds, not optimistically
here. So a run that fails before/at posting leaves no marker and is safely
retryable — which is what makes the backup run work.

Modes (env RL_POST_MODE):
  primary (default) -> alerts on NO_ENTRY (the daily heartbeat).
  backup            -> a later same-day safety run: POST if not yet done, else
                       SILENT. Stays SILENT on NO_ENTRY so it can't double-alert
                       (the primary already did).

Install: a thin real-file shim under ~/.hermes/scripts/ sets RL_REPO (and, for
the backup job, RL_POST_MODE=backup) and runpy's this canonical copy. Hermes
rejects a symlinked --script as traversal, and a plain copy breaks repo
auto-detection, hence the shim. Test overrides: RL_POST_DATE=YYYY/MM/DD,
RL_POST_STATE=<dir>, RL_REPO=<path>.
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
    return Path(__file__).resolve().parents[1]  # ops/ -> repo root


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


def _emit(*lines: str) -> None:
    print("\n".join(lines))


def _no_entry(iso: str, reason: str) -> int:
    # Backup run stays silent so the primary's heartbeat alert isn't duplicated.
    if _is_backup():
        _emit("RL-POST v1", "STATUS: SILENT")
    else:
        _emit("RL-POST v1", "STATUS: NO_ENTRY", f"DATE: {iso}", f"ALERT: {reason}")
    return 0


def main() -> int:
    tp = _today()                      # 2026/06/10
    iso = tp.replace("/", "-")         # 2026-06-10
    day = _repo() / "data" / tp
    tweet_f, tg_f = day / "tweet.md", day / "telegram.md"
    marker = _state_dir() / f"posted-{iso}"

    if marker.exists():                # already posted today -> nothing to do
        _emit("RL-POST v1", "STATUS: SILENT")
        return 0

    if not (tweet_f.exists() and tg_f.exists()):
        return _no_entry(iso, f"[rl] No entry to post for {iso} - the daily run "
                              f"produced nothing (low fuel, gate fail, or it hasn't "
                              f"finished). No tweet/telegram under data/{tp}.")

    tweet_fm, tweet_body = _split_frontmatter(tweet_f.read_text(encoding="utf-8"))
    tg_fm, tg_body = _split_frontmatter(tg_f.read_text(encoding="utf-8"))
    if tweet_fm.get("ready") != "true" or tg_fm.get("ready") != "true":
        return _no_entry(iso, f"[rl] Entry for {iso} exists but is not marked "
                              f"ready - not posting.")

    # Mark-on-success: the agent writes MARKER only after post_tweet succeeds, so a
    # failed run leaves no marker and the backup run can retry it.
    _emit("RL-POST v1", "STATUS: POST", f"DATE: {iso}", f"MARKER: {marker}",
          "--- TWEET ---", tweet_body,
          "--- TELEGRAM ---", tg_body,
          "--- END ---")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
