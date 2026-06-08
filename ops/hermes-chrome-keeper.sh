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

if curl -s --max-time 4 "http://localhost:${PORT}/json/version" >/dev/null 2>&1; then
  exit 0  # already up — nothing to do
fi

echo "$(date '+%Y-%m-%dT%H:%M:%S') chrome-keeper: :${PORT} unreachable, launching Chrome"
open -na "Google Chrome" --args \
  --remote-debugging-port="${PORT}" \
  --user-data-dir="${PROFILE}" \
  --no-first-run \
  --no-default-browser-check
