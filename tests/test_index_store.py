"""U3 tests: dedup, near-duplicate guard (incl. small-index + cluster), connections."""

import json

import pytest

from index_store import IndexStore, IndexStoreError, DEDUP_THRESHOLD, RELATED_THRESHOLD


def _seed_cluster(store):
    for t in ["memory", "planning", "tools", "evaluation", "routing"]:
        store.record_topic(f"AI agent {t}", tags=["ai", "agent", t], slug=t)


def test_bootstrap_and_persist(index_path):
    store = IndexStore(index_path)
    assert store.topic_count == 0
    store.record_topic("Understanding async in Rust", tags=["rust", "async"], slug="async-rust")
    # A fresh instance on the same path sees the persisted topic.
    assert IndexStore(index_path).topic_count == 1


def test_retire_roundtrip(index_path):
    store = IndexStore(index_path)
    assert not store.is_retired(13)
    store.retire([13, 27])
    assert store.is_retired(13) and store.is_retired(27)
    assert IndexStore(index_path).is_retired(27)


def test_near_identical_scores_high(index_path):
    store = IndexStore(index_path)
    store.record_topic("Key Laws and Principles of Software Engineering",
                       tags=["software-engineering", "principles"], slug="laws")
    cands = store.near_dup_candidates("Key Laws and Principles of Software Engineering",
                                      tags=["software-engineering", "principles"])
    assert cands[0]["score"] >= DEDUP_THRESHOLD


def test_unrelated_scores_low(index_path):
    store = IndexStore(index_path)
    store.record_topic("Understanding async in Rust", tags=["rust", "async"], slug="async")
    cands = store.near_dup_candidates("Sourdough bread fermentation", tags=["baking", "bread"])
    assert cands[0]["score"] < DEDUP_THRESHOLD


def test_related_ranking_and_self_exclusion(index_path):
    store = IndexStore(index_path)
    store.record_topic("Understanding async in Rust", tags=["rust", "async", "concurrency"], slug="async")
    store.record_topic("Baking sourdough bread", tags=["baking", "bread"], slug="bread")
    related = store.related("Async patterns in Rust", tags=["rust", "async"])
    titles = [r["topic"] for r in related]
    assert "Understanding async in Rust" in titles
    assert "Baking sourdough bread" not in titles
    assert all(r["score"] >= RELATED_THRESHOLD for r in related)


def test_tiny_index_defers_to_judgment(index_path):
    store = IndexStore(index_path)
    store.record_topic("AI agent memory", tags=["ai", "agent", "memory"], slug="mem")
    decision = store.flag_near_dup("AI agent memory", tags=["ai", "agent", "memory"])
    assert decision["defer_to_judgment"] is True
    assert decision["flagged"] is False  # never auto-flag on a tiny index


def test_cluster_does_not_overblock(index_path):
    store = IndexStore(index_path)
    _seed_cluster(store)  # 5 topics sharing the "ai"/"agent" core
    assert not store.is_small()
    decision = store.flag_near_dup("AI agent pricing tiers", tags=["ai", "agent", "pricing"])
    assert decision["flagged"] is False  # IDF down-weights the shared core


def test_large_index_flags_real_duplicate(index_path):
    store = IndexStore(index_path)
    _seed_cluster(store)
    decision = store.flag_near_dup("AI agent memory", tags=["ai", "agent", "memory"])
    assert decision["defer_to_judgment"] is False
    assert decision["flagged"] is True


def test_atomic_write_leaves_no_temp(index_path):
    store = IndexStore(index_path)
    store.record_topic("X", tags=["x"], slug="x")
    assert index_path.exists()
    json.loads(index_path.read_text())  # valid JSON
    leftovers = list(index_path.parent.glob("*.tmp"))
    assert leftovers == []


def test_corrupt_index_raises(index_path):
    index_path.write_text("{not valid json")
    with pytest.raises(IndexStoreError):
        IndexStore(index_path)


def test_missing_keys_tolerated(index_path):
    index_path.write_text('{"version": 1}')
    store = IndexStore(index_path)  # setdefault backfills retired_ids/topics
    assert store.topic_count == 0
    assert not store.is_retired(1)
