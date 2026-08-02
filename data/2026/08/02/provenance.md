# Provenance — 2026-08-02

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **collection of agent-harness examples** across Node, CI, a serverless edge
  platform and a hosted container provider — CLI-triggered runs with no HTTP endpoint, the
  agent never seeing the repository token, the working directory mounted into the sandbox,
  and object storage plus embedded SQLite standing in as the agent's filesystem (tags:
  agent-framework, node, sandbox, github-actions, cloudflare), captured 2 May. Pull: the
  note records active enthusiasm for building one's own harness and flags the space as very
  new — the strongest signal in the pool.
- A saved **frontier model release announcement** covering a general-availability model and
  a science-focused sibling: months of engineering compressed into days, autonomous protein
  design and bioinformatics matching or beating skilled human operators, over a week of
  largely autonomous genomics work, and a new classifier layer for detecting misuse (tags:
  ai, software-engineering, cybersecurity, biology, safeguards, model-release), captured
  9 June. Pull: the note marks the release as the thing worth registering.
- A saved **discussion of a real-time multimodal interaction model** — one transformer
  trained jointly on text, image and audio in both directions, with input and output
  treated as continuous token streams and processing interleaved in 200ms micro-turns
  (tags: multimodal, transformer, interaction-model, real-time, ai), captured 11 May. Pull:
  no note attached; selected on domain grounds.

Chosen for domain spread (**agent runtime infrastructure · computational biology ·
speech/audio representation**). The eligible pool is 6 entries and two of those are exact
duplicates of the same link, so the real menu was 5. Two entries were passed over: a
frontier-model-release entry from April sits in the same tag cluster as the June one and
would have made two picks from one lane, and a self-hosted project-management tool whose
angle (agents as teammates inside a team process) overlaps the 2026-07-30 day on code
ownership when an agent wrote the commit.

## The 12 adjacent candidates

From the agent-harness examples:
1. **Sandboxing coding agents: isolation setups teams actually run** ← picked
2. Keeping credentials out of the agent's context window
3. Ephemeral dev containers for agents: managed providers vs microVMs
4. Object storage as an agent filesystem

From the frontier model release:
5. Autonomous AI in the lab: what got independently reproduced
6. Jailbreak classifiers as a deployed safety layer
7. **AI protein design in practice: what gets reported from the bench** ← picked
8. Long-horizon agent runs: what breaks after hour one

From the real-time multimodal model:
9. Micro-turn streaming architectures for interleaved multimodal IO
10. **Audio tokenizers and codecs behind speech-native models** ← picked
11. Real-time video understanding: models that watch a stream, not a clip
12. Evaluating interaction models: benchmarks for realtime, not turn-based

All 12 cleared the near-dup guard (highest score 0.161). Four further candidates were
generated and **dropped by judgment rather than by score**, which is worth recording
because the guard passed all of them: three voice-agent framings (full-duplex turn-taking,
latency budgets, speech-to-speech vs cascade) sit on top of the 2026-07-18 day in
substance despite scoring 0.14–0.24, and "verifying frontier model capability claims"
repeats the verified-versus-claimed spine of yesterday's vulnerability brief. Candidate 1
was narrowed away from the already-covered checkpoint-and-rollback angle (2026-07-20) and
toward the runtime substrate itself — providers, meters, session caps, escape mechanics.
Candidate 10 was deliberately scoped *below* the 2026-07-18 voice-agent day: the
representation layer, not product engineering.

## Notes on this run

**The three briefs share an unplanned finding: none of these topics has a community
layer.** Reddit's public search endpoint returned 403 on every attempt in all three runs,
so every Reddit tally is listing-discovery noise rather than query matches. Per topic:

- *Agent sandbox runtimes* — 12 Reddit threads across seven relevant subs with zero
  mentioning a provider, the entire Hacker News layer at 132 points across 19 stories, 3 X
  posts totalling 22 likes, and zero YouTube results across five query shapes. A category
  with heavy venture funding and effectively no public argument. One data-quality miss is
  recorded in the brief itself: the engine's repo canonicalizer resolved a sandbox SDK to a
  similarly-named unrelated repository, so that star count is a resolution artifact and is
  labelled as such rather than quietly used.
- *AI-designed proteins* — 1 off-topic Reddit thread, 25 Hacker News stories of pure
  keyword collision with zero about protein design, nothing from YouTube, Polymarket or
  GitHub project mode, and an X layer made of paper-summarizer bot accounts rather than
  bench scientists. Only 19 of 51 items fall inside the last 7 days. Every load-bearing
  claim came from the web layer plus five targeted supplements, and the brief says outright
  that it reports what the literature shows, not what practitioners are saying. One
  circulating pooled success-rate figure could not be corroborated and is marked unverified
  in the body.
- *Audio tokenizers* — 1 Reddit thread (off-topic), 5 X posts totalling 54 likes, one of
  which matches only because a codec name is an ordinary Swahili word. The engine's own
  Hacker News pass keyed on the wrong term and surfaced nothing on-topic; the real
  in-window traffic was recovered with a targeted second pass and cited explicitly. Two of
  the strongest sources sit just outside the 30-day window and are flagged as such in the
  brief rather than presented as current.

**One engine behaviour worth remembering.** A seed sentence containing " vs " routed the
engine into comparison mode and fanned out per-entity runs. The affected topic was re-run
with the phrasing corrected. Future seeds should avoid " vs " unless a comparison run is
actually wanted.

**Connections are empty today by computation, not by omission.** The read-only relatedness
pass returned no links above threshold for any of the three topics — expected, since two of
them open domains the index has not covered before. The nearest prior neighbours are
recorded here instead: the sandbox brief sits one hop from 2026-07-20 (safety nets for
autonomous coding agents) at 0.123, and the audio brief sits below 2026-07-18 (real-time
voice agents) at the product layer.

**Fuel is now the binding constraint.** The check at start of run: **6 eligible, span 51
days, capture rate 0.12/day, roughly 2 days of runway** at 3 per day. Retiring today's
three picks leaves the pool at 3, which is exactly the `--min-pool 3` circuit-breaker
threshold. Unless entries are captured before the next run, the routine will skip rather
than spend. Capture is running at roughly a third of burn and has now shrunk on four
consecutive days.
