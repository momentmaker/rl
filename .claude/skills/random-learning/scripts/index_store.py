"""Dedup index, near-duplicate guard, and connections store for Random Learning.

The index is a single JSON file recording, across all runs:
  - retired source-entry ids (so a `self` entry is never mined twice),
  - every published topic with a normalized token signature,
  - (derived on demand) the most-related past topics, for "connects to" links.

Near-duplicate scoring is an IDF-weighted Jaccard over each topic's
title+tag token set. IDF down-weights generic cluster vocabulary (e.g.
"ai", "agent") so a whole interest area isn't over-blocked. While the index
is smaller than ``SMALL_INDEX_K`` topics the threshold is unreliable, so the
guard defers the keep/drop decision to Claude's judgment instead.

Importable module: ``from index_store import IndexStore``. A thin ``__main__``
debug entry is provided, but the only real caller is the skill's Python.
"""

from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path

SMALL_INDEX_K = 5
DEDUP_THRESHOLD = 0.6
RELATED_THRESHOLD = 0.2

_STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "to", "in", "for", "on", "with",
    "is", "are", "how", "what", "why", "your", "you", "it", "this", "that",
    "as", "at", "by", "be", "from", "into", "about",
}

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def normalize_tokens(title: str, tags: list[str] | None = None) -> list[str]:
    """Lowercase, split title+tags into a deduped token set (sorted for stability)."""
    text = title or ""
    if tags:
        text = text + " " + " ".join(tags)
    tokens = {
        tok
        for tok in _TOKEN_RE.findall(text.lower())
        if len(tok) >= 2 and tok not in _STOPWORDS
    }
    return sorted(tokens)


class IndexStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.data = self._load()

    # ---- persistence -------------------------------------------------------

    def _load(self) -> dict:
        if self.path.exists():
            return json.loads(self.path.read_text())
        return self.bootstrap()

    @staticmethod
    def bootstrap() -> dict:
        return {"version": 1, "retired_ids": [], "topics": []}

    def save(self) -> None:
        """Atomic write: serialize to a temp file then os.replace into place."""
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(self.data, indent=2, ensure_ascii=False))
        os.replace(tmp, self.path)

    # ---- retired source ids ------------------------------------------------

    def is_retired(self, entry_id) -> bool:
        return entry_id in set(self.data["retired_ids"])

    def retire(self, ids) -> None:
        retired = set(self.data["retired_ids"])
        retired.update(ids)
        self.data["retired_ids"] = sorted(retired, key=lambda x: (str(type(x)), str(x)))
        self.save()

    # ---- topics ------------------------------------------------------------

    def record_topic(self, title: str, *, tags=None, date=None, slug=None, path=None) -> dict:
        topic = {
            "title": title,
            "tokens": normalize_tokens(title, tags),
            "tags": list(tags or []),
            "date": date,
            "slug": slug,
            "path": path,
        }
        self.data["topics"].append(topic)
        self.save()
        return topic

    @property
    def topic_count(self) -> int:
        return len(self.data["topics"])

    def is_small(self) -> bool:
        """True while the index is too small for the Jaccard threshold to be trusted."""
        return self.topic_count < SMALL_INDEX_K

    # ---- similarity --------------------------------------------------------

    def _idf(self) -> dict[str, float]:
        topics = self.data["topics"]
        n = len(topics)
        df: dict[str, int] = {}
        for t in topics:
            for tok in set(t["tokens"]):
                df[tok] = df.get(tok, 0) + 1
        return {tok: math.log((n + 1) / (d + 1)) + 1.0 for tok, d in df.items()}

    def _idf_of(self, token: str, idf: dict[str, float]) -> float:
        # Tokens unseen in the corpus are maximally distinctive.
        n = len(self.data["topics"])
        return idf.get(token, math.log((n + 1) / 1) + 1.0)

    def _score(self, cand_tokens: set[str], stored_tokens: set[str], idf: dict[str, float]) -> float:
        union = cand_tokens | stored_tokens
        if not union:
            return 0.0
        inter = cand_tokens & stored_tokens
        inter_w = sum(self._idf_of(tok, idf) for tok in inter)
        union_w = sum(self._idf_of(tok, idf) for tok in union)
        return inter_w / union_w if union_w else 0.0

    def near_dup_candidates(self, title: str, tags=None, top: int = 5) -> list[dict]:
        """All stored topics scored against the candidate, highest first."""
        cand = set(normalize_tokens(title, tags))
        idf = self._idf()
        scored = [
            {"topic": t["title"], "slug": t.get("slug"), "date": t.get("date"),
             "score": round(self._score(cand, set(t["tokens"]), idf), 4)}
            for t in self.data["topics"]
        ]
        scored.sort(key=lambda s: s["score"], reverse=True)
        return scored[:top]

    def flag_near_dup(self, title: str, tags=None) -> dict:
        """Guard decision. While the index is small, defer to Claude's judgment."""
        candidates = self.near_dup_candidates(title, tags)
        top = candidates[0]["score"] if candidates else 0.0
        if self.is_small():
            return {"flagged": False, "defer_to_judgment": True, "top_score": top,
                    "candidates": candidates}
        return {"flagged": top >= DEDUP_THRESHOLD, "defer_to_judgment": False,
                "top_score": top, "candidates": candidates}

    def related(self, title: str, tags=None, k: int = 3) -> list[dict]:
        """Past topics above the (lower) connection threshold, excluding the exact self."""
        cand = set(normalize_tokens(title, tags))
        idf = self._idf()
        out = []
        for t in self.data["topics"]:
            stored = set(t["tokens"])
            if stored == cand and t["title"].strip().lower() == (title or "").strip().lower():
                continue  # exact self
            score = self._score(cand, stored, idf)
            if score >= RELATED_THRESHOLD:
                out.append({"topic": t["title"], "slug": t.get("slug"),
                            "date": t.get("date"), "score": round(score, 4)})
        out.sort(key=lambda s: s["score"], reverse=True)
        return out[:k]


if __name__ == "__main__":  # minimal debug entry
    import sys
    store = IndexStore(sys.argv[1] if len(sys.argv) > 1 else "index.json")
    print(json.dumps({"topics": store.topic_count, "retired": len(store.data["retired_ids"])}))
