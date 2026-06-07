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

## Scheduling (Mac Mini)

The pipeline runs daily as a **Local Desktop scheduled task** (a Claude Code
routine, Local variant) on an always-on Mac Mini:

- Create it in Claude Code Desktop → Routines → New routine → **Local**, pointing
  at the `random-learning` skill, on a daily schedule.
- Grant the task the tools it needs (Bash / Write / Read / Edit + skill
  invocation) via the task's permission set.
- Provide env: `BRAVE_API_KEY`, `FROM_BROWSER=chrome`. Grant the one-time
  macOS Keychain "always allow" for Chrome cookie access (fallback:
  `AUTH_TOKEN` / `CT0` env vars).
- Git push uses `gh`-authenticated HTTPS (`gh auth login` once).

**Before trusting the schedule (spike):** run the `random-learning` skill once
by hand and confirm it can (a) invoke the user-level `last30days` sub-skill,
(b) write the day's files, and (c) `git push` via `gh`. A forced gate failure
must commit nothing.

A scheduled GitHub Action (`heartbeat.yml`) alerts if `data/` goes stale, so a
silent failure on the Mac Mini surfaces independently.

## Plan & origin

- Requirements: `docs/brainstorms/2026-06-07-random-learning-requirements.md`
- Plan: `docs/plans/2026-06-07-001-feat-random-learning-pipeline-plan.md`
