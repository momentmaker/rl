"""U5 tests: hard length gates at the platform boundaries (Covers AE3)."""

from lengthcheck import body_of, check

FM = "---\nplatform: x\nchar_count: 0\nready: false\n---\n"


def test_tweet_boundary():
    assert check("a" * 280, 280)[0] is True
    assert check("a" * 281, 280)[0] is False


def test_telegram_boundary():
    assert check("a" * 4096, 4096)[0] is True
    assert check("a" * 4097, 4096)[0] is False


def test_empty_body_fails():
    ok, count, _ = check("", 280)
    assert ok is False and count == 0
    assert check(FM, 280)[0] is False  # frontmatter only, no body


def test_frontmatter_not_counted():
    text = FM + ("a" * 280)
    assert body_of(text) == "a" * 280
    assert check(text, 280)[0] is True


def test_valid_reports_count():
    ok, count, reason = check("hello world", 280)
    assert ok is True and count == 11 and reason == "ok"
