"""Hard length gate for social-post files.

Counts the post *body* (the text after any leading YAML frontmatter) and fails
when it is empty or exceeds the platform limit. The skill calls this right after
drafting each file; the self-review gate (U7) calls it too rather than
reimplementing the check.

  lengthcheck.py tweet.md --max 280
  lengthcheck.py telegram.md --max 4096
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n?(.*)$", re.DOTALL)


def body_of(text: str) -> str:
    """Return the post body, stripping a leading YAML frontmatter block if present."""
    m = _FRONTMATTER_RE.match(text)
    return (m.group(1) if m else text).strip()


def check(text: str, max_len: int) -> tuple[bool, int, str]:
    """Return (ok, char_count, reason)."""
    count = len(body_of(text))
    if count == 0:
        return False, 0, "empty body (nothing to post)"
    if count > max_len:
        return False, count, f"body is {count} chars, over the {max_len} limit"
    return True, count, "ok"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Validate a social-post file's body length.")
    p.add_argument("file", help="path to the post file")
    p.add_argument("--max", type=int, required=True, help="max body characters")
    args = p.parse_args(argv)

    ok, count, reason = check(Path(args.file).read_text(encoding="utf-8"), args.max)
    if ok:
        print(f"{args.file}: {count} chars OK")
        return 0
    print(f"{args.file}: FAIL - {reason}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
