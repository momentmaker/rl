"""U6 tests: index ordering, connection links (AE5), provenance, empty state, privacy."""

import json
from pathlib import Path

from build_site import render_site, split_brief

TEMPLATES = Path(__file__).resolve().parent.parent / ".claude" / "skills" / "random-learning" / "templates"


def _make_day(data_dir, date_path, slug, title, brief_text, connections=None, provenance=None, tags=None):
    day = data_dir / date_path
    day.mkdir(parents=True)
    (day / f"{slug}.md").write_text(f"# {title}\n\n{brief_text}\n")
    meta = {"date": date_path, "topics": [
        {"title": title, "brief_file": f"{slug}.md", "connections": connections or [],
         "tags": tags or []}
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


# ---- new: head meta, assets, tags, feed/sitemap/robots, badge/source card ----

SITE_URL = "https://rl.fz.ax"


def test_head_meta_and_static_assets(tmp_path):
    data = tmp_path / "data"
    _make_day(data, "2026/06/07", "x", "A topic", "Body.", tags=["alpha", "beta"])
    out = tmp_path / "site"
    render_site(data, out, templates_dir=TEMPLATES, site_url=SITE_URL)
    index = (out / "index.html").read_text()
    assert '<link rel="canonical" href="https://rl.fz.ax/">' in index
    assert 'property="og:image" content="https://rl.fz.ax/og-image.png"' in index
    assert 'name="twitter:card" content="summary_large_image"' in index
    assert '<meta name="description"' in index
    # static brand assets are copied into the output root
    for asset in ("favicon.svg", "favicon-32.png", "apple-touch-icon.png",
                  "og-image.png", "manifest.webmanifest"):
        assert (out / asset).exists(), f"missing {asset}"


def test_tag_pages_and_cloud(tmp_path):
    # distinctive titles that are not substrings of the inlined CSS (e.g. "Iowan Old Style")
    data = tmp_path / "data"
    _make_day(data, "2026/03/15", "a", "Zebra topic", "Body.", tags=["shared"])
    _make_day(data, "2026/06/07", "b", "Quasar topic", "Body.", tags=["shared", "unique"])
    out = tmp_path / "site"
    result = render_site(data, out, templates_dir=TEMPLATES, site_url=SITE_URL)
    assert result["tags"] == 2
    assert (out / "tags" / "index.html").exists()
    shared = (out / "tags" / "shared" / "index.html").read_text()
    assert "Zebra topic" in shared and "Quasar topic" in shared  # both under the shared tag
    uniq = (out / "tags" / "unique" / "index.html").read_text()
    assert "Quasar topic" in uniq and "Zebra topic" not in uniq


def test_feed_sitemap_robots(tmp_path):
    data = tmp_path / "data"
    _make_day(data, "2026/06/07", "x", "A topic", "Body.", tags=["alpha"])
    out = tmp_path / "site"
    render_site(data, out, templates_dir=TEMPLATES, site_url=SITE_URL)
    feed = (out / "feed.xml").read_text()
    assert "<feed" in feed and "https://rl.fz.ax/2026/06/07/" in feed
    sitemap = (out / "sitemap.xml").read_text()
    assert "https://rl.fz.ax/" in sitemap and "https://rl.fz.ax/tags/alpha/" in sitemap
    robots = (out / "robots.txt").read_text()
    assert "Sitemap: https://rl.fz.ax/sitemap.xml" in robots


def test_engine_badge_and_source_card_render(tmp_path):
    brief = (
        "🌐 last30days v3.3.2 · synced 2026-06-07\n\n"
        "What I learned:\n\nThe body paragraph.\n\n"
        "---\n"
        "✅ All agents reported back!\n"
        "├─ 🟠 Reddit: 14 threads\n"
        "└─ 📎 Raw results saved to (raw evidence, not committed)\n"
        "---\n\n"
        "Closing invitation line.\n"
    )
    # real briefs start with the badge (no markdown H1), so write the file directly
    data = tmp_path / "data"
    day = data / "2026/06/07"
    day.mkdir(parents=True)
    (day / "x.md").write_text(brief)
    (day / "meta.json").write_text(json.dumps({"date": "2026/06/07", "topics": [
        {"title": "Topic", "brief_file": "x.md", "connections": [], "tags": ["alpha"]}]}))
    out = tmp_path / "site"
    render_site(data, out, templates_dir=TEMPLATES)
    page = (out / "2026/06/07" / "index.html").read_text()
    assert "last30days v3.3.2 · synced 2026-06-07" in page  # styled badge text
    assert "&#32;" not in page                              # no over-escaped spaces
    assert "✅ All agents reported back!" in page            # source-card headline
    assert "Reddit: 14 threads" in page                     # source chip
    assert "Raw results saved" not in page                  # 📎 bookkeeping line dropped
    assert 'class="badge"' in page and 'class="sources"' in page


def test_split_brief_separates_parts():
    parts = split_brief(
        "🌐 last30days v1 · synced 2026-01-01\n\nbody here\n\n"
        "---\n✅ All agents reported back!\n├─ Reddit: 1\n---\n\ninvite\n"
    )
    assert parts["badge"].startswith("🌐")
    assert parts["body"] == "body here"
    assert parts["footer"][0].startswith("✅")
    assert parts["invitation"] == "invite"


def test_split_brief_without_engine_format_is_body_only():
    parts = split_brief("Just a plain brief.\n\nSecond paragraph.")
    assert parts["badge"] is None
    assert parts["footer"] is None
    assert "Second paragraph." in parts["body"]
