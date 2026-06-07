#!/usr/bin/env bash
# Run one Random Learning cycle on the Mac Mini.
#
#   ops/run_daily.sh             # real run: produces artifacts, then commits + pushes
#   ops/run_daily.sh --dry-run   # produces + gates artifacts, but commits/pushes NOTHING
#
# Used both for manual testing (the spike) and by the launchd LaunchAgent.
set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

# Operator config lives OUTSIDE the repo so secrets never get committed.
# Expected: BRAVE_API_KEY, FROM_BROWSER=chrome, SELF_DIR (optional AUTH_TOKEN/CT0).
ENV_FILE="${RL_ENV_FILE:-$HOME/.config/rl/env}"
if [ -f "$ENV_FILE" ]; then set -a; . "$ENV_FILE"; set +a; fi
SELF_DIR="${SELF_DIR:-$HOME/.cache/rl-self}"

PROMPT="/random-learning run today's cycle"
if [ "${1:-}" = "--dry-run" ]; then
  PROMPT="/random-learning dry run — do everything except commit and push"
fi

LOG_DIR="${HOME}/.local/state/rl"; mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/run-$(date +%Y%m%dT%H%M%S).log"

# Unattended: this is your own repo on your own machine, and the gate is
# fail-closed. Confirm the exact flags once against `claude --help` during the
# spike (step 2c in the README) — permission mode + tool/dir access vary by
# claude version. --add-dir grants access to the self cache outside the repo.
claude -p "$PROMPT" \
  --permission-mode bypassPermissions \
  --add-dir "$SELF_DIR" \
  >"$LOG" 2>&1
status=$?

echo "random-learning: exit=$status log=$LOG"
exit "$status"
