"""Shared pytest fixtures and import path setup for the random-learning scripts."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / ".claude" / "skills" / "random-learning" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

SAMPLE_ENTRY = """+++
id = 13
kind = "url"
source = "article"
captured_at = "2026-04-21T23:59:34Z"
local_date = "2026-04-21"
iso_week = "2026-W17"
week_idx = 2101
url = "https://lawsofsoftwareengineering.com/"
telegram_msg_id = 53
title = "Key Laws and Principles of Software Engineering"
tags = [ "software-engineering", "principles", "management", "development", "optimization", ]
+++

Conway's Law: Organizations design systems that mirror their own communication structure.

A comprehensive collection of foundational laws and principles guiding software engineering.

https://lawsofsoftwareengineering.com/

# why?

2026-04-22T00:00:08Z

i like these kind of things - kind of like aphorism or shortcut to explain some complex terms
"""

SAMPLE_ENTRY_2 = """+++
id = 27
kind = "url"
source = "article"
captured_at = "2026-04-22T10:00:00Z"
local_date = "2026-04-22"
iso_week = "2026-W17"
week_idx = 2102
url = "https://example.com/rust-async"
telegram_msg_id = 61
title = "Understanding async in Rust"
tags = [ "rust", "async", "concurrency" ]
+++

A deep dive into how async/await works in Rust.

https://example.com/rust-async

# why?

2026-04-22T10:01:00Z

i keep getting confused by pinning and futures
"""

SAMPLE_REFLECTION = "# reflection\n\nToday I thought about systems thinking.\n"
SAMPLE_ECHO = "# echo\n\nA quiet day.\n"


@pytest.fixture
def self_repo(tmp_path):
    """A fake `self` library: one week dir with two url entries + a reflection + an echo."""
    week = tmp_path / "self" / "2026-w17"
    week.mkdir(parents=True)
    (week / "2026-04-21-000013-key-laws-and-principles.md").write_text(SAMPLE_ENTRY)
    (week / "2026-04-22-000027-understanding-async-in-rust.md").write_text(SAMPLE_ENTRY_2)
    (week / "2026-04-21-reflection.md").write_text(SAMPLE_REFLECTION)
    (week / "2026-04-22-echo.md").write_text(SAMPLE_ECHO)
    return tmp_path / "self"


@pytest.fixture
def index_path(tmp_path):
    """A fresh (non-existent) index.json path for store tests to bootstrap."""
    return tmp_path / "index.json"
