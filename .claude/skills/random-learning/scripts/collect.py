"""Collect eligible entries from the private `self` link library.

Syncs `self` (clone-or-pull), walks its ``YYYY-wNN/`` week dirs, parses each
entry's TOML frontmatter (``+++ ... +++``) + body + personal ``why?`` note,
classifies eligibility, and emits a normalized JSON list to stdout. Retired
ids and reflection/echo files are excluded.

Sync-failure policy: if the clone/pull fails, abort with a clear reason rather
than silently running on a stale cache.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

DEFAULT_ALLOWLIST = ("url",)
_FRONTMATTER_RE = re.compile(r"^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n?(.*)$", re.DOTALL)
_WHY_RE = re.compile(r"#\s*why\??\s*\n", re.IGNORECASE)
_ISO_TS_RE = re.compile(r"^\s*\d{4}-\d{2}-\d{2}T[\d:]+Z?\s*$")


class CollectError(RuntimeError):
    """Raised when the `self` sync fails (fail-closed, never run on stale cache)."""


def is_special_file(path: Path) -> bool:
    """Per-day reflection/echo files are not entries."""
    name = path.name.lower()
    return name.endswith("-reflection.md") or name.endswith("-echo.md")


def _extract_why(body: str) -> str:
    parts = _WHY_RE.split(body, maxsplit=1)
    if len(parts) < 2:
        return ""
    tail_lines = [ln for ln in parts[1].strip().splitlines()]
    note_lines = [ln for ln in tail_lines if not _ISO_TS_RE.match(ln)]
    return "\n".join(note_lines).strip()


def _extract_description(body: str) -> str:
    before_why = _WHY_RE.split(body, maxsplit=1)[0]
    lines = [
        ln.strip()
        for ln in before_why.strip().splitlines()
        if ln.strip() and not ln.strip().startswith("http")
    ]
    return " ".join(lines).strip()


def parse_entry(path: Path) -> dict | None:
    """Parse one entry file into a normalized record, or None if it isn't an entry."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        meta = tomllib.loads(m.group(1))
    except tomllib.TOMLDecodeError:
        return None
    body = m.group(2)
    return {
        "id": meta.get("id"),
        "title": meta.get("title", ""),
        "url": meta.get("url", ""),
        "tags": list(meta.get("tags", [])),
        "kind": meta.get("kind", ""),
        "captured_at": meta.get("captured_at"),
        "iso_week": meta.get("iso_week"),
        "local_date": meta.get("local_date"),
        "why": _extract_why(body),
        "description": _extract_description(body),
        "path": str(path),
    }


def is_eligible(entry: dict, allowlist=DEFAULT_ALLOWLIST) -> bool:
    return bool(entry.get("url")) and entry.get("kind") in set(allowlist)


def collect(self_dir, retired_ids=(), allowlist=DEFAULT_ALLOWLIST) -> list[dict]:
    """Walk `self`, return eligible, non-retired entries as normalized records."""
    retired = set(retired_ids)
    out = []
    for path in sorted(Path(self_dir).rglob("*.md")):
        if is_special_file(path):
            continue
        entry = parse_entry(path)
        if entry is None or not is_eligible(entry, allowlist):
            continue
        if entry.get("id") in retired:
            continue
        out.append(entry)
    return out


# ---- git sync ----------------------------------------------------------------

def _git(args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def sync_self(remote: str, cache_dir) -> Path:
    cache = Path(cache_dir)
    if (cache / ".git").exists():
        r = _git(["-C", str(cache), "pull", "--ff-only"])
    else:
        cache.parent.mkdir(parents=True, exist_ok=True)
        r = _git(["clone", "--depth", "50", remote, str(cache)])
    if r.returncode != 0:
        raise CollectError(f"self sync failed: {(r.stderr or r.stdout).strip()}")
    return cache


# ---- supply measurement ------------------------------------------------------

def measure(entries: list[dict]) -> dict:
    """Eligible-pool size + a rough recent capture rate (entries/day over the span)."""
    dates = sorted(e["local_date"] for e in entries if e.get("local_date"))
    span_days = 1
    if len(dates) >= 2:
        from datetime import date
        try:
            d0 = date.fromisoformat(dates[0])
            d1 = date.fromisoformat(dates[-1])
            span_days = max(1, (d1 - d0).days)
        except ValueError:
            span_days = 1
    return {
        "eligible_pool": len(entries),
        "span_days": span_days,
        "capture_rate_per_day": round(len(entries) / span_days, 2),
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Collect eligible entries from the self library.")
    p.add_argument("--self-dir", required=True, help="Local self cache directory")
    p.add_argument("--remote", help="self git remote (for clone/pull)")
    p.add_argument("--index", help="index.json path (to read retired ids)")
    p.add_argument("--allowlist", default=",".join(DEFAULT_ALLOWLIST),
                   help="comma-separated eligible kinds")
    p.add_argument("--no-sync", action="store_true", help="skip git sync (use existing cache)")
    p.add_argument("--measure", action="store_true", help="emit pool stats instead of entries")
    args = p.parse_args(argv)

    if args.remote and not args.no_sync:
        sync_self(args.remote, args.self_dir)

    retired = ()
    if args.index:
        from index_store import IndexStore
        retired = IndexStore(args.index).data["retired_ids"]

    allowlist = tuple(k.strip() for k in args.allowlist.split(",") if k.strip())
    entries = collect(args.self_dir, retired, allowlist)
    print(json.dumps(measure(entries) if args.measure else entries, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
