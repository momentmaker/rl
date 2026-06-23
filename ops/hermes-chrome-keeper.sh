#!/usr/bin/env bash
# Keep a debug-port Chrome alive for Hermes (x-poster on X, plus a persistent
# logged-in profile for gmail/x.com).
#
# Watchdog pattern: a LaunchAgent runs this every minute (StartInterval) and at
# login (RunAtLoad). It relaunches Chrome ONLY when the CDP port is unreachable,
# so it survives reboots and crashes without the respawn loop you'd get from
# pointing launchd's KeepAlive directly at Chrome (Chrome daemonizes and the
# launcher returns immediately). Chrome is started detached via `open` on a
# DEDICATED profile, so logins persist and it never touches your main browser.
set -uo pipefail

PORT=9222
PROFILE="$HOME/.config/hermes-chrome"

# Check if Chrome with the right profile is already running
CHROME_PID=$(pgrep -f "remote-debugging-port=${PORT}.*hermes-chrome" 2>/dev/null || true)

if [ -n "$CHROME_PID" ]; then
  # Chrome process exists — verify the port is actually responding
  if curl -s --max-time 4 "http://localhost:${PORT}/json/version" >/dev/null 2>&1; then
    exit 0  # all good
  fi
  # Port is down but Chrome process exists — it might be hung. Kill and restart.
  echo "$(date '+%Y-%m-%dT%H:%M:%S') chrome-keeper: Chrome running (PID $CHROME_PID) but port ${PORT} down — killing"
  kill "$CHROME_PID" 2>/dev/null || true
  sleep 2
fi

# Also check if ANY Chrome is on port 9222 (e.g. launched without the right profile)
ANY_CHROME_ON_PORT=$(pgrep -f "remote-debugging-port=${PORT}" 2>/dev/null || true)
if [ -n "$ANY_CHROME_ON_PORT" ]; then
  echo "$(date '+%Y-%m-%dT%H:%M:%S') chrome-keeper: Stale Chrome on port ${PORT} — killing"
  kill "$ANY_CHROME_ON_PORT" 2>/dev/null || true
  sleep 2
fi

echo "$(date '+%Y-%m-%dT%H:%M:%S') chrome-keeper: :${PORT} unreachable, launching Chrome"
open -na "Google Chrome" --args \
  --remote-debugging-port="${PORT}" \
  --user-data-dir="${PROFILE}" \
  --no-first-run \
  --no-default-browser-check
