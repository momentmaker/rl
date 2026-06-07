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

notify() {  # [rl]-prefixed Telegram alert; no-op unless creds are in the env file
  [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ] || return 0
  curl -fsS -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=[rl] $1" >/dev/null 2>&1 || true
}

# Same-day alert from the Mac Mini side (the cloud heartbeat is the slower catch-all).
# Deterministic: inspects git, not model behavior.
if [ "${1:-}" != "--dry-run" ]; then
  today="data/$(date +%Y/%m/%d)"
  if [ "$status" -ne 0 ]; then
    notify "daily run errored (exit $status); see $LOG"
  elif ! git ls-files --error-unmatch "$today" >/dev/null 2>&1; then
    notify "no entry committed for $(date +%Y-%m-%d) — gate failed or low fuel; see $LOG"
  fi
fi

exit "$status"
