# Provenance — 2026-07-28

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **discussion thread about an open-source agent taking the top spot on a terminal
  benchmark** (tags: oss, terminalbench, agent, harness, benchmark, gemini), captured in
  late April. Pull: flagged for hands-on follow-up once this machine was set up, and the
  thread's own punchline — that benchmark numbers are mostly a function of the scaffolding
  around a rentable model — is the seed the fan-out grew from.
- A saved **consumer-brand analysis site** (tags: brands, marketing, consumer, analysis,
  strategy), captured yesterday, the freshest entry in the eligible pool. Pull: a
  practical shopping question about which names are still worth the money.
- A saved **discussion thread on software engineering careers under agentic coding**
  (tags: software-engineering, ai, careers, automation, skills, workforce), captured in
  May with the most conviction-carrying note of the three. Pull: agreement that the job
  description itself is being rewritten rather than merely augmented.

Chosen for domain spread (agent engineering · consumer economics · labour market) and
specifically to get one non-AI-framed topic onto a day where the eligible pool remains
heavily AI-weighted. The pool holds two further entries in the same careers cluster and
three more in the agent-tooling cluster, which is a dedup risk for coming days.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the benchmark entry:
1. Harness vs model: how much of an agent benchmark score is the scaffolding ✅ picked
2. Agent benchmark integrity and leaderboard-compliant runs
3. Context compaction strategies inside long-running agent harnesses
4. Sub-agent orchestration versus a single agent loop

From the consumer-brand entry:
5. Shrinkflation and tracking product quality degradation over time
6. Buy-it-for-life: how people decide what is actually durable now ✅ picked
7. Store brands versus name brands and whether the quality gap closed
8. Repairability scores and right-to-repair as a purchase signal

From the careers entry:
9. Whether the junior developer entry path still exists ✅ picked
10. What an agent-wrangler role actually looks like day to day
11. How technical interviews were rebuilt for the AI era
12. Solo and small-team software businesses as a career hedge

Near-dup guard: none of the 12 were flagged, and none triggered the small-index defer.
Highest score in the batch was 0.180 for #5 against the 2026-07-06 private-equity brands
day, with #7 at 0.153 against the same day and #8 at 0.152 against 2026-07-06's 3D-printer
lockdown day. In the agent cluster, #10 scored 0.138 against yesterday's stop-conditions
day and 0.135 against 2026-07-26's agent-memory day; #3 scored 0.107 against the 2026-06-21
context-rot day. The three picked candidates were the *least* entangled in their groups —
0.104, 0.099 and 0.090 respectively — which was a deliberate tiebreak, not a coincidence.

## Narrowing to the top 3

- **#1 Harness vs model** — the most learnable of the agent four, and the only one whose
  answer is numeric rather than architectural: the window contains controlled experiments,
  not just opinions. Picked over #3 and #4, which sit close to the 2026-06-21 context-rot
  and 2026-07-27 stop-conditions days respectively, and over #2, which is a subset of the
  disclosure argument that #1 ended up covering anyway.
- **#6 Buy-it-for-life** — deliberately the non-tech slot, and chosen over #5 and #7
  specifically because those two lean into the ownership-and-decay story already published
  on 2026-07-06. Framing it as a decision procedure rather than a decline narrative was the
  differentiator, and the brief holds that line: the spine is the verification problem, not
  who bought whom.
- **#9 Junior developer entry path** — picked over #10, which would have made the day
  three-for-three AI *and* scored highest in the whole batch against two of the last three
  published days. Chosen over #11 and #12 on live-discussion volume. Framed to force
  concreteness (what teams are actually doing) rather than inviting a doom essay.

Final three span three distinct domains and do not overlap. Two of the three landed on a
genuine in-window reversal rather than the expected consensus.

## Evidence quality notes

All three briefs carry an explicit italic evidence note, per the engine's honesty
convention. All three are concept topics with no single named entity, so the engine's
cluster ranker demoted every cluster with "entity-miss" on every run and none of the
ranked scores carry information — each brief was read off the raw items directly. Beyond
that shared caveat, recall failed differently in each case:

- **Harness vs model** — the first engine run had to be discarded: the topic string
  contained " vs ", which tripped the comparison-mode detector and split the query into
  two entities, the second of which ("model: what actually moves...") was not an entity at
  all and returned five unrelated repositories. Re-run under a non-comparison title. Reddit
  403'd into keyless listing discovery, so the footer's 14,451 upvotes are largely
  off-topic front-page threads, and YouTube captured 0 of 3 transcripts. The load-bearing
  evidence is the arXiv and web layer plus a Hacker News front page that carried four
  separate harness artifacts inside four days.
- **Buy-it-for-life** — the weakest corpus of the three. Reddit 403'd and then rate-limited,
  leaving 3 threads out of roughly 460 discovered cards; GitHub was pulled in by keyword and
  returned 38 items of pure noise (unrelated repository issues), and the single Polymarket
  market was an esports match. The top-ranked cluster was a sand-digging video with 2.1M
  views. Both junk lines are called out in the brief's own note so the footer is not read as
  evidence. Salvaged from the raw file, where the web layer and two on-topic Reddit threads
  were intact.
- **Junior developer path** — GitHub and Polymarket were excluded from this run after the
  previous one, which cleaned up the footer. Reddit returned 21 threads and 54,188 upvotes,
  but the high-engagement ones are general r/recruitinghell venting rather than
  junior-specific, so they are used in the brief for register rather than for claims.
  YouTube returned 0 items in range. The load-bearing evidence is the web layer plus Hacker
  News, and the two strongest items (a payroll-data analysis and an economics preprint) both
  came from post-engine supplements rather than the engine itself.

Nine post-engine web supplements across the three topics, three per brief, all appended to
the non-committed raw evidence files.
