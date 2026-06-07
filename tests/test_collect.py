"""U2 tests: parsing, eligibility, dedup exclusion, special-file skip, sync failure."""

import types
from pathlib import Path

import pytest

import collect
from collect import CollectError, collect as collect_entries, is_eligible, parse_entry

NOTE_ENTRY = """+++
id = 99
kind = "note"
title = "a private thought"
+++

just a note, no url
"""


def test_parses_url_entry(self_repo):
    entry = parse_entry(self_repo / "2026-w17" / "2026-04-21-000013-key-laws-and-principles.md")
    assert entry["id"] == 13
    assert entry["kind"] == "url"
    assert entry["url"].startswith("https://")
    assert "aphorism" in entry["why"]
    assert "software-engineering" in entry["tags"]


def test_skips_malformed_frontmatter(self_repo, tmp_path):
    bad = self_repo / "2026-w17" / "2026-04-23-000040-broken.md"
    bad.write_text("no frontmatter here\njust text\n")
    assert parse_entry(bad) is None


def test_excludes_kind_outside_allowlist(self_repo):
    note = self_repo / "2026-w17" / "2026-04-23-000099-note.md"
    note.write_text(NOTE_ENTRY)
    entry = parse_entry(note)
    assert is_eligible(entry) is False


def test_collect_skips_reflection_echo_and_returns_eligible(self_repo):
    entries = collect_entries(self_repo)
    ids = {e["id"] for e in entries}
    assert ids == {13, 27}  # the two url entries; reflection/echo excluded


def test_excludes_retired_id(self_repo):
    # Covers AE1: a retired source id is not eligible for selection.
    entries = collect_entries(self_repo, retired_ids={13})
    ids = {e["id"] for e in entries}
    assert ids == {27}


def test_empty_pool_when_all_retired(self_repo):
    entries = collect_entries(self_repo, retired_ids={13, 27})
    assert entries == []


def test_sync_failure_aborts(monkeypatch, tmp_path):
    monkeypatch.setattr(
        collect, "_git",
        lambda *a, **k: types.SimpleNamespace(returncode=1, stderr="auth denied", stdout=""),
    )
    with pytest.raises(CollectError):
        collect.sync_self("git@example.com:nope/self.git", tmp_path / "cache")


def test_measure_reports_pool(self_repo):
    stats = collect.measure(collect_entries(self_repo))
    assert stats["eligible_pool"] == 2
    assert stats["capture_rate_per_day"] > 0


def test_tags_non_list_does_not_crash(self_repo):
    bad = self_repo / "2026-w17" / "2026-04-23-000050-badtags.md"
    bad.write_text('+++\nid = 50\nkind = "url"\nurl = "https://x.example"\ntitle = "t"\ntags = 42\n+++\n\nbody\n')
    assert parse_entry(bad)["tags"] == []   # coerced, not a TypeError
    collect_entries(self_repo)              # collecting over the dir must not raise


def test_tags_string_not_char_split(self_repo):
    bad = self_repo / "2026-w17" / "2026-04-23-000051-strtags.md"
    bad.write_text('+++\nid = 51\nkind = "url"\nurl = "https://y.example"\ntitle = "t"\ntags = "rust"\n+++\n\nbody\n')
    assert parse_entry(bad)["tags"] == []   # a bare string is dropped, never split into ['r','u',...]
