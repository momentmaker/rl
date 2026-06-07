"""U6 tests: index ordering, connection links (AE5), provenance, empty state, privacy."""

import json
from pathlib import Path

from build_site import render_site

TEMPLATES = Path(__file__).resolve().parent.parent / ".claude" / "skills" / "random-learning" / "templates"


def _make_day(data_dir, date_path, slug, title, brief_text, connections=None, provenance=None):
    day = data_dir / date_path
    day.mkdir(parents=True)
    (day / f"{slug}.md").write_text(f"# {title}\n\n{brief_text}\n")
    meta = {"date": date_path, "topics": [
        {"title": title, "brief_file": f"{slug}.md", "connections": connections or []}
    ]}
    (day / "meta.json").write_text(json.dumps(meta))
    if provenance:
        (day / "provenance.md").write_text(provenance)
    return day


def test_site_renders_with_ordering_connections_and_provenance(tmp_path):
    data = tmp_path / "data"
    _make_day(data, "2026/03/15", "async-rust", "Async in Rust", "Futures and pinning.")
    _make_day(
        data, "2026/06/07", "ai-agents", "AI agent memory", "How agents remember.",
        connections=[{"title": "Async in Rust", "date": "2026/03/15"}],
        provenance="Picked because I keep circling back to systems topics.",
    )
    out = tmp_path / "site"
    result = render_site(data, out, templates_dir=TEMPLATES)
    assert result["days"] == 2

    index = (out / "index.html").read_text()
    assert "2026/06/07" in index and "2026/03/15" in index
    assert index.find("2026/06/07") < index.find("2026/03/15")  # reverse-chronological

    newer = (out / "2026/06/07" / "index.html").read_text()
    assert "How agents remember." in newer
    assert "2026/03/15" in newer  # Covers AE5: connects-to link to the older topic
    assert "circling back" in newer  # provenance rendered

    older = (out / "2026/03/15" / "index.html").read_text()
    assert "Futures and pinning." in older


def test_empty_data_renders_empty_state(tmp_path):
    data = tmp_path / "data"
    data.mkdir()
    out = tmp_path / "site"
    result = render_site(data, out, templates_dir=TEMPLATES)
    assert result["days"] == 0
    assert "No entries yet" in (out / "index.html").read_text()


def test_no_private_self_url_leaks_when_provenance_redacted(tmp_path):
    data = tmp_path / "data"
    _make_day(
        data, "2026/06/07", "laws", "Laws of software", "Conway's law and friends.",
        provenance="Topic-level rationale only (redacted).",
    )
    out = tmp_path / "site"
    render_site(data, out, templates_dir=TEMPLATES)
    page = (out / "2026/06/07" / "index.html").read_text()
    assert "lawsofsoftwareengineering.com" not in page  # raw self URL never injected


def test_brief_html_is_sanitized(tmp_path):
    data = tmp_path / "data"
    _make_day(data, "2026/06/07", "x", "Topic", "Safe text <script>alert(1)</script> more")
    out = tmp_path / "site"
    render_site(data, out, templates_dir=TEMPLATES)
    page = (out / "2026/06/07" / "index.html").read_text()
    assert "<script>" not in page  # untrusted HTML stripped (XSS guard)
    assert "Safe text" in page


def test_brief_file_traversal_is_blocked(tmp_path):
    secret = tmp_path / "secret.txt"
    secret.write_text("TOPSECRET")
    data = tmp_path / "data"
    day = data / "2026/06/07"
    day.mkdir(parents=True)
    (day / "ok.md").write_text("# T\n\nbody\n")
    meta = {"date": "2026/06/07",
            "topics": [{"title": "T", "brief_file": "../../../../secret.txt", "connections": []}]}
    (day / "meta.json").write_text(json.dumps(meta))
    out = tmp_path / "site"
    render_site(data, out, templates_dir=TEMPLATES)  # must not read outside the day dir or crash
    page = (out / "2026/06/07" / "index.html").read_text()
    assert "TOPSECRET" not in page
