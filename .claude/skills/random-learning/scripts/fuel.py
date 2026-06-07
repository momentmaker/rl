"""Supply-liveness check (R24): is there enough eligible fuel to run today?

The pipeline is a net consumer of a finite `self` pool (entries are retired
forever). Before spending tokens on research, the skill calls this as a
circuit-breaker: a non-zero exit means "low fuel — skip the run and raise an
out-of-band alert" rather than burning a research cycle on an empty pool.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from collect import DEFAULT_ALLOWLIST, collect, measure

LOW_FUEL_EXIT = 2
ABORT_EXIT = 3


def runway(self_dir, retired_ids=(), allowlist=DEFAULT_ALLOWLIST, per_day: int = 3) -> dict:
    stats = measure(collect(self_dir, retired_ids, allowlist))
    stats["per_day"] = per_day
    stats["days_runway"] = stats["eligible_pool"] // per_day
    return stats


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Low-fuel circuit-breaker for the daily run.")
    p.add_argument("--self-dir", required=True)
    p.add_argument("--index")
    p.add_argument("--min-pool", type=int, default=3, help="skip the run below this eligible-pool size")
    p.add_argument("--per-day", type=int, default=3)
    args = p.parse_args(argv)

    retired = ()
    if args.index and Path(args.index).exists():
        from index_store import IndexStore, IndexStoreError
        try:
            retired = IndexStore(args.index).data["retired_ids"]
        except IndexStoreError as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            return ABORT_EXIT

    stats = runway(args.self_dir, retired, per_day=args.per_day)
    print(json.dumps(stats))
    return 0 if stats["eligible_pool"] >= args.min_pool else LOW_FUEL_EXIT


if __name__ == "__main__":
    sys.exit(main())
