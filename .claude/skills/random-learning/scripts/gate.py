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
from index_store import DEDUP_THRESHOLD, IndexStore, IndexStoreError, normalize_tokens

SOCIAL_LIMITS = {"tweet.md": 280, "telegram.md": 4096}
NON_BRIEF = {"tweet.md", "telegram.md", "provenance.md", "meta.json"}
BADGE_MARK = "last30days"
FOOTER_MARK = "all agents reported back"
ERROR_MARKERS = ("## pre-research status",)
INJECTION_PATTERNS = (
    r"ignore (all |the |your )?(previous|prior)",
    r"disregard (all |the |your )?(previous|prior)",
    r"forget (everything|all)\b",
    r"new instructions?:",
    r"\bsystem\s*:",
    r"system prompt",
    r"ready:\s*true",
)
MIN_BRIEFS = 3
_ZERO_WIDTH = dict.fromkeys(map(ord, "​‌‍﻿"), None)
_WORD_RE = re.compile(r"[a-z0-9]+")


def _normalize(text: str) -> str:
    """Lowercase, drop zero-width chars, collapse whitespace — defeats trivial evasion."""
    return re.sub(r"\s+", " ", text.translate(_ZERO_WIDTH).lower())


def _canonical_url(url: str) -> str:
    """Scheme/www/query/trailing-slash-insensitive host+path form for leak matching."""
    u = url.strip().lower().split("?", 1)[0].split("#", 1)[0]
    u = re.sub(r"^[a-z]+://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.rstrip("/")


def _shingle_leak(needle_norm: str, haystack_norm: str, n: int = 5) -> bool:
    """True if any n-word run of the note appears verbatim — catches light paraphrase/reflow."""
    words = _WORD_RE.findall(needle_norm)
    if len(words) < n:
        return needle_norm in haystack_norm
    return any(" ".join(words[i:i + n]) in haystack_norm for i in range(len(words) - n + 1))


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

    # injection scan across briefs + social files + provenance (all reach the public site)
    scan = briefs + [day / s for s in (set(SOCIAL_LIMITS) | {"provenance.md"}) if (day / s).exists()]
    for f in scan:
        norm = _normalize(f.read_text(encoding="utf-8"))
        for pat in INJECTION_PATTERNS:
            if re.search(pat, norm):
                reasons.append(f"{f.name}: injection-shaped content matched /{pat}/")

    # privacy: no raw self URL or why-note in any committed artifact (canonicalized)
    artifacts = briefs + [day / x for x in NON_BRIEF if (day / x).exists()]
    blob_norm = _normalize("\n".join(f.read_text(encoding="utf-8") for f in artifacts))
    for url in source_urls:
        canon = _canonical_url(url or "")
        if canon and canon in blob_norm:
            reasons.append(f"privacy: raw self URL leaked into committed artifacts ({url})")
    for why in source_whys:
        w = _normalize(why or "")
        if w and (w in blob_norm or _shingle_leak(w, blob_norm)):
            reasons.append("privacy: raw self `why?` note leaked into committed artifacts")

    # dedup + connections from meta.json
    meta_path = day / "meta.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            meta = None
            reasons.append(f"meta.json: invalid JSON ({e})")
        if meta is not None:
            topics = meta.get("topics", [])
            # near-duplicate of a previously published topic — IDF-Jaccard score, not exact
            # equality, so a one-word variant can't slip through. Hard threshold (no small-index
            # defer): the gate is the mechanical backstop, not the selection-time judgment call.
            store = None
            if index_path and Path(index_path).exists():
                try:
                    store = IndexStore(index_path)
                except IndexStoreError as e:
                    reasons.append(f"index.json unreadable: {e}")
            if store is not None:
                for t in topics:
                    cands = store.near_dup_candidates(t.get("title", ""), t.get("tags"), top=1)
                    if cands and cands[0]["score"] >= DEDUP_THRESHOLD:
                        reasons.append(f"dedup: topic '{t.get('title')}' duplicates a prior published topic")
            # intra-run duplicates (two near-identical topics in the same day)
            for i, a in enumerate(topics):
                ta = normalize_tokens(a.get("title", ""), a.get("tags"))
                for b in topics[i + 1:]:
                    if _same_topic(ta, normalize_tokens(b.get("title", ""), b.get("tags"))):
                        reasons.append(
                            f"dedup: '{a.get('title')}' and '{b.get('title')}' duplicate within today's run"
                        )
            # connection links resolve to an existing day
            data_root = day.parents[2] if len(day.parents) >= 3 else day.parent
            for t in topics:
                for c in t.get("connections", []):
                    cdate = c.get("date")
                    if cdate and not (data_root / cdate).exists():
                        reasons.append(f"connection: dangling link to {cdate}")

    return GateResult(ok=not reasons, reasons=reasons)


_FRONTMATTER_SPLIT = re.compile(r"^(---\s*\n.*?\n---\s*\n)(.*)$", re.DOTALL)


def set_ready(day_dir) -> None:
    """Set `ready: true` in the leading YAML frontmatter only — never body prose (gate authority)."""
    for fname in SOCIAL_LIMITS:
        f = Path(day_dir) / fname
        if not f.exists():
            continue
        m = _FRONTMATTER_SPLIT.match(f.read_text(encoding="utf-8"))
        if not m:
            continue
        fm = re.sub(r"ready:\s*false", "ready: true", m.group(1), count=1)
        f.write_text(fm + m.group(2), encoding="utf-8")


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
