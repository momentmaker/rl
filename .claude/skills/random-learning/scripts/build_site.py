"""Generate the static site from all dated entries under ``data/``.

Renders an editorial, reverse-chronological journal: a homepage (latest entry
featured + compounding stats + tag cloud + month-grouped archive), one page per
day (each topic's brief, styled last30days badge + source footer, tag chips,
"connects to" links, redacted provenance), and browse-by-tag pages. Also emits
an Atom feed, sitemap, robots.txt, JSON-LD, and copies brand assets. Output goes
to ``site/`` (gitignored); the same renderer runs in CI (U8) and locally to feed
the self-review gate (U7).

Each day dir may carry a machine-readable ``meta.json`` (topics + tags +
connections); absent that, the renderer falls back to the brief files it finds.

Untrusted brief/provenance HTML is sanitized with ``nh3`` so the public site can
never become an XSS sink, and model-supplied filenames are confined to the day
dir (no traversal).
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import markdown as md
import nh3
from jinja2 import Environment, FileSystemLoader, select_autoescape

SOCIAL_FILES = {"tweet.md", "telegram.md"}
PROVENANCE_FILE = "provenance.md"
META_FILE = "meta.json"

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_TEMPLATES = SCRIPT_DIR.parent / "templates"
STATIC_DIRNAME = "static"

DEFAULT_SITE_URL = "https://rl.fz.ax"
SITE_TITLE = "Random Learning"
SITE_TAGLINE = "What I learned, one day at a time."
SITE_DESCRIPTION = (
    "A daily learning ritual: three researched topics a day, drawn from a private "
    "library of saved links, each grounded in what people said this month, and "
    "wired to past entries so the learning compounds. Never the same topic twice."
)

WORDS_PER_MINUTE = 220
_MD_EXT = ["extra", "sane_lists"]
_WORD_RE = re.compile(r"[A-Za-z0-9']+")


# ---- markdown / sanitize ----------------------------------------------------

def _clean(html: str) -> str:
    # Briefs/provenance derive from untrusted web/social research and are rendered
    # |safe; strip embedded HTML/scripts so the public site can't be an XSS sink.
    return nh3.clean(html)


def _render_md_text(text: str) -> str:
    return _clean(md.markdown(text, extensions=_MD_EXT))


def _render_md(path: Path) -> str:
    return _render_md_text(path.read_text(encoding="utf-8"))


def _reading_minutes(text: str) -> int:
    words = len(_WORD_RE.findall(text))
    return max(1, round(words / WORDS_PER_MINUTE))


# ---- brief structure (badge / body / source footer / invitation) ------------

_HR_RE = re.compile(r"^\s*-{3,}\s*$")


def split_brief(text: str) -> dict:
    """Pull the last30days badge, body, source-footer tree, and invitation apart.

    The engine emits: a `🌐 last30days …` badge line, the synthesis body, a
    footer block fenced by `---` that starts with `✅ All agents reported back!`,
    then a short invitation. Briefs without that shape (e.g. plain test fixtures)
    fall through as body-only so rendering never depends on the engine format.
    """
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    badge = None
    if i < len(lines) and lines[i].lstrip().startswith("🌐"):
        badge = lines[i].strip()
        i += 1

    # Find a `---` fence whose next non-empty line begins the engine footer.
    foot_start = foot_end = None
    for j in range(i, len(lines)):
        if _HR_RE.match(lines[j]):
            k = j + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines) and lines[k].lstrip().startswith("✅"):
                foot_start = j
                for m in range(k + 1, len(lines)):
                    if _HR_RE.match(lines[m]):
                        foot_end = m
                        break
                break

    if foot_start is None:
        body = "\n".join(lines[i:]).strip()
        return {"badge": badge, "body": body, "footer": None, "invitation": ""}

    body = "\n".join(lines[i:foot_start]).strip()
    footer_lines = [ln for ln in lines[foot_start + 1:foot_end] if ln.strip()]
    invitation = "\n".join(lines[(foot_end + 1):]).strip() if foot_end else ""
    return {"badge": badge, "body": body, "footer": footer_lines, "invitation": invitation}


def _render_badge(badge: str | None) -> str:
    if not badge:
        return ""
    # "🌐 last30days v3.3.2 · synced 2026-06-07" -> engine + version + synced date.
    # Returned as plain text; the template autoescapes it via Jinja ({{ }}).
    return badge.lstrip("🌐").strip()


def _render_footer(footer_lines: list[str] | None) -> dict | None:
    """Turn the emoji-tree footer into structured plain-text data for the template.

    Values are plain strings; the template autoescapes them (no `| safe`), so any
    HTML in the engine output is neutralized without nh3 double-escaping spaces.
    """
    if not footer_lines:
        return None
    headline = footer_lines[0].strip()
    sources = []
    for ln in footer_lines[1:]:
        s = ln.strip().lstrip("├└─ ").strip()
        if not s or s.startswith("📎"):  # drop the raw-results bookkeeping line
            continue
        sources.append(s)
    return {"headline": headline, "sources": sources}


# ---- path / slug helpers ----------------------------------------------------

def _safe_child(day: Path, name: str) -> Path | None:
    """Resolve a model-supplied filename, confined to the day dir (no traversal)."""
    if not name or "/" in name or "\\" in name or ".." in name:
        return None
    candidate = day / name
    try:
        candidate.resolve().relative_to(day.resolve())
    except ValueError:
        return None
    return candidate


def slugify(value: str) -> str:
    out = re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")
    return out or "tag"


def _day_dirs(data_dir: Path) -> list[Path]:
    return sorted(
        (p for p in data_dir.glob("[0-9]*/[0-9]*/[0-9]*") if p.is_dir()),
        reverse=True,
    )


def _brief_files(day: Path) -> list[Path]:
    return sorted(
        p for p in day.glob("*.md")
        if p.name not in SOCIAL_FILES and p.name != PROVENANCE_FILE
    )


def _display_date(rel: str) -> str:
    try:
        return datetime.strptime(rel, "%Y/%m/%d").strftime("%B %-d, %Y")
    except ValueError:
        return rel


def _month_key(rel: str) -> tuple[str, str]:
    try:
        d = datetime.strptime(rel, "%Y/%m/%d")
        return d.strftime("%Y/%m"), d.strftime("%B %Y")
    except ValueError:
        return rel, rel


# ---- model building ---------------------------------------------------------

def _build_topic(day: Path, t: dict) -> dict:
    brief = _safe_child(day, t.get("brief_file", ""))
    raw = brief.read_text(encoding="utf-8") if (brief and brief.exists()) else ""
    parts = split_brief(raw)
    slug = (brief.stem if brief else slugify(t.get("title", "topic")))
    return {
        "title": t.get("title", brief.stem if brief else ""),
        "slug": slug,
        "anchor": slugify(t.get("title", slug)),
        "tags": [str(x) for x in (t.get("tags") or [])],
        "badge": _render_badge(parts["badge"]),
        "html": _render_md_text(parts["body"]) if parts["body"] else "",
        "footer": _render_footer(parts["footer"]),
        "invitation": _render_md_text(parts["invitation"]) if parts["invitation"] else "",
        "reading_minutes": _reading_minutes(parts["body"] or raw),
        "connections": [
            {"title": c.get("title", ""),
             "href": None, "date": c.get("date")}
            for c in (t.get("connections") or [])
        ],
    }


def build_day(day: Path, data_dir: Path, base_url: str) -> dict:
    rel = day.relative_to(data_dir).as_posix()  # e.g. 2026/06/07
    meta_path = day / META_FILE
    topics: list[dict] = []
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            meta = {"topics": []}
        for t in meta.get("topics", []):
            topics.append(_build_topic(day, t))
    else:
        for brief in _brief_files(day):
            parts = split_brief(brief.read_text(encoding="utf-8"))
            topics.append({
                "title": brief.stem.replace("-", " "), "slug": brief.stem,
                "anchor": slugify(brief.stem), "tags": [],
                "badge": _render_badge(parts["badge"]),
                "html": _render_md_text(parts["body"]) if parts["body"] else "",
                "footer": _render_footer(parts["footer"]),
                "invitation": _render_md_text(parts["invitation"]) if parts["invitation"] else "",
                "reading_minutes": _reading_minutes(parts["body"]),
                "connections": [],
            })

    # resolve connection hrefs now that base_url is known
    for t in topics:
        for c in t["connections"]:
            c["href"] = f"{base_url}/{c['date']}/" if c.get("date") else "#"

    provenance = day / PROVENANCE_FILE
    mkey, mlabel = _month_key(rel)
    tagset: list[str] = []
    for t in topics:
        for tag in t["tags"]:
            if tag not in tagset:
                tagset.append(tag)
    return {
        "date": rel,
        "date_display": _display_date(rel),
        "href": f"{base_url}/{rel}/",
        "month_key": mkey,
        "month_label": mlabel,
        "topics": topics,
        "tags": tagset,
        "description": " · ".join(t["title"] for t in topics) or SITE_TAGLINE,
        "provenance_html": _render_md(provenance) if provenance.exists() else "",
    }


# ---- aggregates -------------------------------------------------------------

def _aggregate(days: list[dict], base_url: str) -> dict:
    tag_map: dict[str, dict] = {}
    for day in days:
        for t in day["topics"]:
            for tag in t["tags"]:
                slug = slugify(tag)
                entry = tag_map.setdefault(slug, {"slug": slug, "label": tag.replace("-", " "),
                                                  "name": tag, "entries": []})
                entry["entries"].append({"title": t["title"], "day": day["date"],
                                         "day_display": day["date_display"],
                                         "href": f"{day['href']}#{t['anchor']}"})
    tags = sorted(tag_map.values(), key=lambda e: (-len(e["entries"]), e["label"]))
    total_topics = sum(len(d["topics"]) for d in days)
    months = {d["month_key"] for d in days}
    return {
        "tags": tags,
        "stats": {
            "entries": len(days),
            "topics": total_topics,
            "tags": len(tags),
            "months": len(months),
        },
    }


def _group_by_month(days: list[dict]) -> list[dict]:
    groups: list[dict] = []
    for day in days:
        if not groups or groups[-1]["key"] != day["month_key"]:
            groups.append({"key": day["month_key"], "label": day["month_label"], "days": []})
        groups[-1]["days"].append(day)
    return groups


# ---- feeds / sitemap / robots ----------------------------------------------

def _abs(site_url: str, base_url: str, path: str) -> str:
    return f"{site_url}{base_url}{path}"


def _write_feed(out_dir: Path, days: list[dict], site_url: str, base_url: str) -> None:
    home = _abs(site_url, base_url, "/")
    updated = (datetime.strptime(days[0]["date"], "%Y/%m/%d").replace(tzinfo=timezone.utc)
               .isoformat() if days else datetime(2026, 1, 1, tzinfo=timezone.utc).isoformat())
    esc = _xml_escape
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        f"<title>{esc(SITE_TITLE)}</title>",
        f"<subtitle>{esc(SITE_TAGLINE)}</subtitle>",
        f'<link href="{esc(home)}"/>',
        f'<link rel="self" href="{esc(_abs(site_url, base_url, "/feed.xml"))}"/>',
        f"<id>{esc(home)}</id>",
        f"<updated>{esc(updated)}</updated>",
    ]
    for day in days[:50]:
        url = _abs(site_url, base_url, f"/{day['date']}/")
        dt = datetime.strptime(day["date"], "%Y/%m/%d").replace(tzinfo=timezone.utc).isoformat()
        parts += [
            "<entry>",
            f"<title>{esc(day['date_display'])} — {esc(day['description'])}</title>",
            f'<link href="{esc(url)}"/>',
            f"<id>{esc(url)}</id>",
            f"<updated>{esc(dt)}</updated>",
            f"<summary>{esc(day['description'])}</summary>",
            "</entry>",
        ]
    parts.append("</feed>")
    (out_dir / "feed.xml").write_text("\n".join(parts), encoding="utf-8")


def _write_sitemap(out_dir: Path, urls: list[str], site_url: str, base_url: str) -> None:
    esc = _xml_escape
    body = ["<?xml version=\"1.0\" encoding=\"utf-8\"?>",
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        body.append(f"<url><loc>{esc(_abs(site_url, base_url, u))}</loc></url>")
    body.append("</urlset>")
    (out_dir / "sitemap.xml").write_text("\n".join(body), encoding="utf-8")


def _write_robots(out_dir: Path, site_url: str, base_url: str) -> None:
    txt = "User-agent: *\nAllow: /\nSitemap: " + _abs(site_url, base_url, "/sitemap.xml") + "\n"
    (out_dir / "robots.txt").write_text(txt, encoding="utf-8")


def _xml_escape(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def _copy_static(templates_dir: Path, out_dir: Path) -> None:
    static = templates_dir / STATIC_DIRNAME
    if static.is_dir():
        shutil.copytree(static, out_dir, dirs_exist_ok=True)


# ---- render -----------------------------------------------------------------

def render_site(data_dir, out_dir, templates_dir=None, base_url: str = "",
                site_url: str = DEFAULT_SITE_URL) -> dict:
    data_dir = Path(data_dir)
    out_dir = Path(out_dir)
    templates_dir = Path(templates_dir or DEFAULT_TEMPLATES)
    base_url = base_url.rstrip("/")
    site_url = site_url.rstrip("/")

    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.filters["slugify"] = slugify

    days = [build_day(d, data_dir, base_url) for d in _day_dirs(data_dir)]
    agg = _aggregate(days, base_url)
    site = {
        "title": SITE_TITLE, "tagline": SITE_TAGLINE, "description": SITE_DESCRIPTION,
        "base_url": base_url, "site_url": site_url,
        "url": f"{site_url}{base_url}/", "og_image": f"{site_url}{base_url}/og-image.png",
        "feed_url": f"{base_url}/feed.xml",
        "tags": agg["tags"], "stats": agg["stats"],
        "year": (days[0]["date"][:4] if days else "2026"),
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    _copy_static(templates_dir, out_dir)

    def render(template, path, **ctx):
        page = ctx.pop("page")
        html = env.get_template(template).render(site=site, page=page, **ctx)
        dest = out_dir / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")

    # home
    render("index.html", "index.html",
           page={"title": SITE_TITLE, "description": SITE_DESCRIPTION,
                 "canonical": f"{site_url}{base_url}/", "og_image": site["og_image"],
                 "og_type": "website"},
           days=days, months=_group_by_month(days), latest=(days[0] if days else None))

    # day pages
    sitemap_urls = ["/"]
    for day in days:
        sitemap_urls.append(f"/{day['date']}/")
        render("day.html", f"{day['date']}/index.html",
               page={"title": f"{day['date_display']} · {SITE_TITLE}",
                     "description": day["description"],
                     "canonical": f"{site_url}{base_url}/{day['date']}/",
                     "og_image": site["og_image"], "og_type": "article"},
               day=day)

    # tag index + per-tag pages
    if agg["tags"]:
        sitemap_urls.append("/tags/")
        render("tags.html", "tags/index.html",
               page={"title": f"Topics · {SITE_TITLE}",
                     "description": f"Browse {site['stats']['topics']} topics across "
                                    f"{len(agg['tags'])} themes.",
                     "canonical": f"{site_url}{base_url}/tags/",
                     "og_image": site["og_image"], "og_type": "website"},
               tags=agg["tags"])
        for tag in agg["tags"]:
            sitemap_urls.append(f"/tags/{tag['slug']}/")
            render("tag.html", f"tags/{tag['slug']}/index.html",
                   page={"title": f"{tag['label']} · {SITE_TITLE}",
                         "description": f"{len(tag['entries'])} entries on {tag['label']}.",
                         "canonical": f"{site_url}{base_url}/tags/{tag['slug']}/",
                         "og_image": site["og_image"], "og_type": "website"},
                   tag=tag)

    _write_feed(out_dir, days, site_url, base_url)
    _write_sitemap(out_dir, sitemap_urls, site_url, base_url)
    _write_robots(out_dir, site_url, base_url)

    return {"days": len(days), "tags": len(agg["tags"]), "topics": agg["stats"]["topics"]}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Build the static site from data/.")
    p.add_argument("--data-dir", default="data")
    p.add_argument("--out-dir", default="site")
    p.add_argument("--templates-dir", default=None)
    p.add_argument("--base-url", default="", help="site root path prefix, e.g. /rl")
    p.add_argument("--site-url", default=DEFAULT_SITE_URL, help="absolute origin for canonical/OG/feed")
    args = p.parse_args(argv)
    result = render_site(args.data_dir, args.out_dir, args.templates_dir, args.base_url, args.site_url)
    print(f"built {result['days']} day page(s), {result['tags']} tag page(s) into {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
