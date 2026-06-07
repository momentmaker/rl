"""U11 tests: low-fuel circuit-breaker."""

import fuel
from fuel import LOW_FUEL_EXIT, runway


def test_ample_pool_runs(self_repo):
    assert fuel.main(["--self-dir", str(self_repo), "--min-pool", "2"]) == 0


def test_low_pool_short_circuits(self_repo):
    assert fuel.main(["--self-dir", str(self_repo), "--min-pool", "5"]) == LOW_FUEL_EXIT


def test_runway_reports_days(self_repo):
    stats = runway(self_repo, per_day=3)
    assert stats["eligible_pool"] == 2
    assert stats["days_runway"] == 0  # 2 // 3
