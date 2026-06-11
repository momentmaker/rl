# Random Learning (rl)

A daily, set-and-forget learning ritual. Each day it mines a private link
library ([`self`](https://github.com/momentmaker/self)), lets Claude pick 3
entries, fan them into 12 adjacent topics, and narrow to the top 3; researches
each topic with the [`last30days`](https://github.com/mvanhorn/last30days-skill)
skill; and commits dated briefs, a regenerated static site, and ready-to-post
social files to this repo — never repeating a topic, gated by a self-review
pass.

Posting to X / Telegram is handled by a separate downstream bot that consumes
the committed `tweet.md` / `telegram.md` files. This project only produces and
commits artifacts.

## How a day flows

1. Sync `self`, collect eligible entries (skipping retired ids and
   reflection/echo files).
2. Claude picks 3 entries → fans to 12 adjacent topics → narrows to 3.
3. Each topic is researched via `last30days` (agent mode); briefs land in
   `data/YYYY/MM/DD/`.
4. `tweet.md` (≤280) and `telegram.md` (≤4096) are drafted and length-checked.
5. The dedup index, connections, and redacted provenance are updated.
6. A self-review gate validates everything; on pass it commits and pushes.

## Layout

```
.claude/skills/random-learning/   # the orchestration skill + helper scripts
data/YYYY/MM/DD/                   # dated briefs, social files, provenance
index.json                        # dedup + topics + near-dup signatures + connections
tests/                            # pytest suite for the helper scripts
.github/workflows/                # site publish + liveness heartbeat
```

## Develop

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Helper scripts target Python 3.12+ (TOML frontmatter parsed with stdlib
`tomllib`). Run one cycle by hand before relying on the schedule.

## Deploy on the Mac Mini

When you pull this onto the Mac Mini there's no prior context — this section is
the whole runbook.

### 1. One-time setup

```bash
git clone git@github.com:momentmaker/rl.git && cd rl
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q                # proves the deterministic scripts

gh auth login            # git push uses gh-authenticated HTTPS
```

Operator config lives **outside the repo** (so secrets are never committed),
sourced by the runner from `~/.config/rl/env`:

```bash
mkdir -p ~/.config/rl
cat > ~/.config/rl/env <<'EOF'
export BRAVE_API_KEY=...            # last30days web backend
export SELF_DIR=$HOME/.cache/rl-self
export AUTH_TOKEN=...  CT0=...      # X session cookies (auth_token, ct0)
export FROM_BROWSER=off            # use the tokens above; do NOT read Chrome cookies
export TELEGRAM_BOT_TOKEN=...       # [rl] alerting bot (same-day failure pings)
export TELEGRAM_CHAT_ID=...
EOF
```

`last30days` must be installed for the user the routine runs as — either as a
user skill (`~/.claude/skills/last30days`) or as a Claude Code plugin
(`~/.claude/plugins/cache/last30days-skill/<version>/skills/last30days`), with
its first-run setup complete. Verify with a `--diagnose` check against the
resolved engine (`bird_authenticated: true` means X auth is live).

**X auth + the Keychain prompt.** Authenticate X via the `AUTH_TOKEN`/`CT0`
cookies (from a logged-in x.com session) rather than `FROM_BROWSER=chrome`.
`FROM_BROWSER=chrome` makes last30days decrypt Chrome's cookie store every run,
which raises a recurring macOS **"Chrome Safe Storage"** Keychain prompt that
"Always Allow" often fails to silence (the requesting `python` binary isn't
stably code-signed). `FROM_BROWSER=off` skips the cookie read entirely; the env
tokens still authenticate X. Refresh the tokens when they expire (logging out of
x.com invalidates `auth_token`).

### 2. Test before scheduling (the spike)

Work up from cheap to full. There is no conversation context on the Mac Mini, so
each step is self-contained:

```bash
S=.claude/skills/random-learning/scripts

# a) deterministic scripts — no Claude, no network
pytest -q

# b) real self data — no Claude — confirms parsing + supply
python $S/collect.py --self-dir "$SELF_DIR" --remote git@github.com:momentmaker/self.git --measure
python $S/fuel.py    --self-dir "$SELF_DIR" --index index.json
python $S/build_site.py                       # renders an empty-state site/ locally

# c) ONE full cycle, DRY RUN — Claude does collect -> pick -> last30days ->
#    write -> gate, but commits/pushes NOTHING. Inspect data/<today>/ after.
ops/run_daily.sh --dry-run

# d) ONE real cycle — commits + pushes; the publish Action then deploys the site
ops/run_daily.sh
```

Step (c) is the spike: it proves Claude finds the project skill, invokes the
user-level `last30days` sub-skill, the briefs carry the engine badge/footer, the
social files are within limits, and the fail-closed gate passes on good data
(and commits nothing on a forced failure). Logs land in `~/.local/state/rl/`.

### 3. Schedule the daily routine

Pick one.

**A. Claude Code Desktop routine (Local)** — simplest if the Desktop app runs on
the Mac Mini. Desktop app → **Routines → New routine → Local**, prompt
`/random-learning`, daily schedule, and grant Bash / Read / Write / Edit + skill
invocation in the task's permission set. Local routines are durable (survive
restarts, no 7-day expiry) and spawn their own session per run.

**B. launchd LaunchAgent** — OS-level, no Desktop app needed. A LaunchAgent (not
a Daemon) runs in your logged-in GUI session, so it keeps Chrome/Keychain and
`gh` access:

```bash
# edit the checkout path inside the plist first if your Mac Mini differs
cp ops/com.momentmaker.rl.daily.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.momentmaker.rl.daily.plist
launchctl start com.momentmaker.rl.daily      # fire once now to verify
```

It runs `ops/run_daily.sh` daily (07:17 by default). The one thing to confirm
for your `claude` version is the headless invocation inside `run_daily.sh`
(permission mode + tool/dir access) — step 2c is where you verify it.

### Alerting

Failures surface to Telegram with an `[rl]` prefix from two complementary places:

- **`run_daily.sh` (Mac Mini, same-day):** `[rl] no entry committed today …` when a
  real run errors or ships nothing (gate fail / low fuel). Deterministic — it
  inspects git, not model behavior. Needs `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`
  in `~/.config/rl/env`.
- **`heartbeat.yml` (cloud, catch-all):** `[rl] pipeline stale …` when `data/` goes
  stale for more than 2 days — fires even if the Mac Mini or the routine dies.
  Needs the same two values as **GitHub repo secrets** (Settings → Secrets and
  variables → Actions): `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`. It also opens a
  deduped GitHub issue as a durable record.

Both degrade gracefully (skip the ping) if the creds aren't set, so the pipeline
runs fine before you wire alerting.

## Posting to X + Telegram (Hermes)

The daily run only *produces* `tweet.md` / `telegram.md` (with `ready: true` set
by the gate). A separate **Hermes** scheduled job posts them, decoupled from the
rl run so it no-ops cleanly on days rl skips.

- **`ops/hermes-rl-post.py`** — a deterministic poster, run by Hermes in
  **`--no-agent`** mode (no LLM). It finds `data/<today>/`, checks `ready: true`,
  extracts the frontmatter-stripped bodies, posts the tweet by driving the
  logged-in Chrome over CDP (port 9222, the same path the x-poster plugin uses),
  writes a post-once marker on success, and prints the Telegram body to stdout —
  which Hermes delivers verbatim (empty stdout = silent run). Hermes requires
  `--script` files un-symlinked under `~/.hermes/scripts/`, so install a thin
  real-file shim there that sets `RL_REPO` (and, for the backup, `RL_POST_MODE=
  backup`) and `runpy`s this canonical copy. It runs under the Hermes venv python
  (`sys.executable`), which has playwright.
- **No LLM on purpose.** The agent path failed twice in production — a model-API
  broken pipe, and the model improvising a stale-token `xurl` call instead of the
  posting tool. The post is mechanical (fixed text → one CDP call), so `--no-agent`
  removes that whole class of failure and makes the post-once marker deterministic
  (the script writes `~/.local/state/rl-poster/posted-<date>` only after the post
  succeeds; a failed run leaves no marker and is retried by the backup).
- **Two cron jobs** — primary + a backup that auto-recovers a failed primary
  (backup mode retries if no marker yet, else prints nothing → silent; stays
  silent on no-entry so it can't double-alert):
  ```bash
  hermes cron create "30 8 * * *" --name rl-daily-post \
    --script rl-post.py --no-agent --deliver telegram --workdir <repo>
  hermes cron create "30 9 * * *" --name rl-daily-post-backup \
    --script rl-post-backup.py --no-agent --deliver telegram --workdir <repo>
  # pause/resume: hermes cron pause|resume rl-daily-post
  # force a retry now: rm ~/.local/state/rl-poster/posted-<date> && hermes cron run rl-daily-post
  # test the path safely (today already posted -> silent): hermes cron run rl-daily-post-backup
  ```
- **Debug Chrome must stay up + logged in.** The CDP post drives an
  already-running Chrome on port 9222 (`~/.config/hermes-chrome` profile, **logged
  into x.com**). `ops/hermes-chrome-keeper.sh` + `ops/ai.hermes.chrome-debug.plist`
  are a LaunchAgent watchdog (RunAtLoad + 60s interval) that relaunches it after
  reboots/crashes; the dedicated profile keeps x.com/gmail logins persistent. The
  keeper keeps the *process* up but can't re-login — if the x.com session expires,
  log into x.com once in that Chrome. Install:
  ```bash
  cp ops/ai.hermes.chrome-debug.plist ~/Library/LaunchAgents/
  launchctl load ~/Library/LaunchAgents/ai.hermes.chrome-debug.plist
  ```

## Custom domain (rl.fz.ax)

The site is served at the **root** of `rl.fz.ax`, so the Pages base path is empty
— `publish-site.yml` derives it automatically via `actions/configure-pages` and
writes a `CNAME` on every deploy. One-time setup:

1. **DNS** at the `fz.ax` zone — `rl` is a subdomain, so add a CNAME record:
   `rl  CNAME  momentmaker.github.io.`
2. **GitHub → Settings → Pages**: Source = **GitHub Actions**; Custom domain =
   `rl.fz.ax` (GitHub verifies DNS, then issues a cert); after the cert lands,
   tick **Enforce HTTPS**.
3. Enable Pages (step 2's Source) **before** the workflow runs —
   `actions/configure-pages` errors otherwise. Trigger a first deploy with
   **Actions → Publish site → Run workflow** to verify the domain + HTTPS on the
   empty-state page, before any daily entry exists.

## Plan & origin

- Requirements: `docs/brainstorms/2026-06-07-random-learning-requirements.md`
- Plan: `docs/plans/2026-06-07-001-feat-random-learning-pipeline-plan.md`
