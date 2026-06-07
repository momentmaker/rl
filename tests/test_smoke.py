"""U1 smoke test: dependencies resolve and the project skeleton exists."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_dependencies_import():
    import jinja2  # noqa: F401
    import markdown  # noqa: F401
    import tomllib  # noqa: F401  (stdlib, 3.11+)


def test_skeleton_exists():
    skill = ROOT / ".claude" / "skills" / "random-learning"
    assert (skill / "scripts").is_dir()
    assert (skill / "templates").is_dir()
    assert (skill / "references").is_dir()
    assert (ROOT / "data").is_dir()


def test_fixtures_available(self_repo, index_path):
    assert (self_repo / "2026-w17").is_dir()
    assert not index_path.exists()
