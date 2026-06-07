"""Self-review gate: validate a day's artifacts before commit. Fail closed.

Mechanical checks (a thin Claude qualitative pass runs on top in the skill):
  - 3 briefs exist, non-empty, carry the last30days badge + footer (engine ran),
    and contain no error markers;
  - tweet.md <= 280, telegram.md <= 4096 (via lengthcheck);
  - no injection-shaped strings / frontmatter overrides in briefs or social files;
  - no raw `self` URL or `why?` note leaks into committed artifacts (privacy);
  - today's topics are not prior duplicates in the index (dedup);
  - every "connects to" link resolves to an existing day.

`ready` is set by this gate (never the model), only after all checks pass.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from lengthcheck import check as length_check
from index_store import IndexStore, normalize_tokens

SOCIAL_LIMITS = {"tweet.md": 280, "telegram.md": 4096}
NON_BRIEF = {"tweet.md", "telegram.md", "provenance.md", "meta.json"}
BADGE_MARK = "last30days"
FOOTER_MARK = "all agents reported back"
ERROR_MARKERS = ("## pre-research status",)
INJECTION_PATTERNS = (
    r"ignore (all )?previous",
    r"disregard (all )?previous",
    r"\bsystem:\s",
    r"ready:\s*true",
)
MIN_BRIEFS = 3


@dataclass
class GateResult:
    ok: bool
    reasons: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps({"ok": self.ok, "reasons": self.reasons}, indent=2)


def brief_files(day: Path) -> list[Path]:
    return sorted(p for p in day.glob("*.md") if p.name not in NON_BRIEF)


def _same_topic(tokens_a, tokens_b) -> bool:
    return set(tokens_a) == set(tokens_b)


def run(day_dir, *, index_path=None, source_urls=(), source_whys=(), min_briefs=MIN_BRIEFS) -> GateResult:
    day = Path(day_dir)
    reasons: list[str] = []

    briefs = brief_files(day)
    if len(briefs) < min_briefs:
        reasons.append(f"expected >= {min_briefs} briefs, found {len(briefs)}")
    for b in briefs:
        text = b.read_text(encoding="utf-8")
        low = text.lower()
        if not text.strip():
            reasons.append(f"{b.name}: empty brief")
            continue
        if BADGE_MARK not in low or FOOTER_MARK not in low:
            reasons.append(f"{b.name}: missing last30days badge/footer (engine may not have run)")
        for marker in ERROR_MARKERS:
            if marker in low:
                reasons.append(f"{b.name}: contains error marker '{marker}'")

    # social length gates
    for fname, limit in SOCIAL_LIMITS.items():
        f = day / fname
        if not f.exists():
            reasons.append(f"{fname}: missing")
            continue
        ok, count, why = length_check(f.read_text(encoding="utf-8"), limit)
        if not ok:
            reasons.append(f"{fname}: {why}")

    # injection scan across briefs + social files
    scan = briefs + [day / s for s in SOCIAL_LIMITS if (day / s).exists()]
    for f in scan:
        low = f.read_text(encoding="utf-8").lower()
        for pat in INJECTION_PATTERNS:
            if re.search(pat, low):
                reasons.append(f"{f.name}: injection-shaped content matched /{pat}/")

    # privacy: no raw self URL or why-note in any committed artifact
    artifacts = briefs + [day / x for x in NON_BRIEF if (day / x).exists()]
    blob = "\n".join(f.read_text(encoding="utf-8") for f in artifacts)
    for url in source_urls:
        if url and url in blob:
            reasons.append(f"privacy: raw self URL leaked into committed artifacts ({url})")
    for why in source_whys:
        w = (why or "").strip()
        if w and w in blob:
            reasons.append("privacy: raw self `why?` note leaked into committed artifacts")

    # dedup + connections from meta.json
    meta_path = day / "meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        today = meta.get("date")
        topics = meta.get("topics", [])
        if index_path and Path(index_path).exists():
            store = IndexStore(index_path)
            for t in topics:
                cand = normalize_tokens(t.get("title", ""), t.get("tags"))
                for stored in store.data["topics"]:
                    if stored.get("date") != today and _same_topic(cand, stored["tokens"]):
                        reasons.append(f"dedup: topic '{t.get('title')}' already published {stored.get('date')}")
                        break
        data_root = day.parents[2] if len(day.parents) >= 3 else day.parent
        for t in topics:
            for c in t.get("connections", []):
                cdate = c.get("date")
                if cdate and not (data_root / cdate).exists():
                    reasons.append(f"connection: dangling link to {cdate}")

    return GateResult(ok=not reasons, reasons=reasons)


def set_ready(day_dir) -> None:
    """Flip `ready: false` -> `ready: true` in social frontmatter (gate authority)."""
    for fname in SOCIAL_LIMITS:
        f = Path(day_dir) / fname
        if f.exists():
            text = re.sub(r"ready:\s*false", "ready: true", f.read_text(encoding="utf-8"))
            f.write_text(text, encoding="utf-8")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Self-review gate for a day's artifacts.")
    p.add_argument("day_dir")
    p.add_argument("--index")
    p.add_argument("--source-file", help="non-committed JSON {urls:[],whys:[]} for leak checks")
    args = p.parse_args(argv)

    urls, whys = (), ()
    if args.source_file and Path(args.source_file).exists():
        src = json.loads(Path(args.source_file).read_text())
        urls, whys = src.get("urls", []), src.get("whys", [])

    result = run(args.day_dir, index_path=args.index, source_urls=urls, source_whys=whys)
    print(result.to_json())
    if result.ok:
        set_ready(args.day_dir)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
