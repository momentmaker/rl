"""Generate the static site from all dated entries under ``data/``.

Renders a reverse-chronological index plus one page per day showing each
topic's brief, its "connects to [past topic]" links, and the redacted
provenance. Output goes to ``site/`` (gitignored); the same renderer runs in
CI (U8) and locally to feed the self-review gate (U7).

Each day dir may contain a machine-readable ``meta.json`` (written by the
orchestration skill) describing topics + connections; absent that, the
renderer falls back to listing the brief files it finds.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import markdown as md
from jinja2 import Environment, FileSystemLoader, select_autoescape

SOCIAL_FILES = {"tweet.md", "telegram.md"}
PROVENANCE_FILE = "provenance.md"
META_FILE = "meta.json"

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_TEMPLATES = SCRIPT_DIR.parent / "templates"


def _render_md(path: Path) -> str:
    return md.markdown(path.read_text(encoding="utf-8"), extensions=["extra", "sane_lists"])


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


def build_day(day: Path, data_dir: Path, base_url: str) -> dict:
    rel = day.relative_to(data_dir).as_posix()  # e.g. 2026/06/07
    meta_path = day / META_FILE
    topics = []
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        for t in meta.get("topics", []):
            brief = day / t.get("brief_file", "")
            topics.append({
                "title": t.get("title", brief.stem),
                "html": _render_md(brief) if brief.exists() else "",
                "connections": [
                    {"title": c.get("title", ""),
                     "href": f"{base_url}/{c['date']}/" if c.get("date") else "#"}
                    for c in t.get("connections", [])
                ],
            })
    else:
        for brief in _brief_files(day):
            topics.append({"title": brief.stem.replace("-", " "),
                           "html": _render_md(brief), "connections": []})

    provenance = day / PROVENANCE_FILE
    return {
        "date": rel,
        "href": f"{base_url}/{rel}/",
        "topics": topics,
        "provenance_html": _render_md(provenance) if provenance.exists() else "",
    }


def render_site(data_dir, out_dir, templates_dir=None, base_url: str = "") -> dict:
    data_dir = Path(data_dir)
    out_dir = Path(out_dir)
    base_url = base_url.rstrip("/")
    env = Environment(
        loader=FileSystemLoader(str(templates_dir or DEFAULT_TEMPLATES)),
        autoescape=select_autoescape(["html"]),
    )
    days = [build_day(d, data_dir, base_url) for d in _day_dirs(data_dir)]

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(days=days, base_url=base_url)
    )
    for day in days:
        page_dir = out_dir / day["date"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(
            env.get_template("day.html").render(day=day, base_url=base_url)
        )
    return {"days": len(days)}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Build the static site from data/.")
    p.add_argument("--data-dir", default="data")
    p.add_argument("--out-dir", default="site")
    p.add_argument("--templates-dir", default=None)
    p.add_argument("--base-url", default="", help="site root prefix, e.g. /rl")
    args = p.parse_args(argv)
    result = render_site(args.data_dir, args.out_dir, args.templates_dir, args.base_url)
    print(f"built {result['days']} day page(s) into {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
