# Provenance — 2026-08-03

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

The eligible pool was **exactly 3**, so there was no selection step today — all three
eligible entries were picked, and the pool is now empty. See the fuel note at the bottom.

- A saved **frontier model release discussion** covering a general-availability model
  rollout: gradual staging to keep service stable, an outsized internal win where the
  vendor's own coding agent analysed weeks of production traffic and wrote custom
  partitioning heuristics for a 20%+ token-generation speedup, and a comment layer arguing
  over a very high quoted hallucination rate set against a competitor's much lower one
  (tags: ai-models, benchmarks, coding, efficiency), captured 23 April. Pull: the only
  entry in today's pool carrying a stated reason, and that note points at the competitive
  dynamic rather than at any one model — which is why the fan went to the *measurement*
  layer rather than to the release.
- A saved **discussion of a real-time multimodal interaction model** — one transformer
  trained jointly on text, image and audio in both directions, with input and output
  treated as continuous token streams and processing interleaved in 200ms micro-turns
  (tags: multimodal, transformer, interaction-model, real-time, ai), captured 11 May. No
  note attached; selected on domain grounds. **Caveat:** this is a same-link duplicate of
  an entry retired on 2026-08-02 — retirement is by entry id, not by URL, so the twin
  stayed eligible. Yesterday's fan from it went to the *representation* layer (audio
  codecs and tokenizers); today's went to the *interaction* layer (turn-taking, barge-in,
  endpointing), which is a different subject and cleared the near-dup guard. Flagged so
  the repeat is on the record rather than silent.
- A saved **self-hosted project-management platform** built so AI agents and humans sit in
  the same Scrum team as equal members — agents assigned to sprints, appearing on the
  board alongside people, picking tasks off the backlog and updating status, with a
  protocol server exposing projects, tasks and sprints to any compatible agent (tags:
  project-management, ai-collaboration, self-hosted, scrum, open-source), captured
  13 June. No note attached; selected on domain grounds.

Domain spread: **evaluation methodology · real-time voice interaction · engineering
workflow**. Three different layers, no shared tag cluster.

## The 12 adjacent candidates

From the frontier model release:
1. **Hallucination benchmarks: what the divergent rates actually measure** ← picked
2. Coding agents writing their own performance optimizations in production
3. Model version churn: deprecation and pinning in production LLM apps
4. What actually determines tokens-per-second when you serve an LLM

From the real-time multimodal model:
5. **Full-duplex voice agents: barge-in and turn-taking** ← picked
6. Speech-to-speech models replacing the ASR-LLM-TTS pipeline
7. Latency budgets for real-time voice AI
8. Interleaved streaming architectures for multimodal models

From the agent-teammate project tool:
9. **AI agents assigned issues in the tracker: what teams report** ← picked
10. MCP servers for project management and workspace tools
11. Gherkin and BDD specs as the contract for AI agents
12. Story points and sprint estimation when agents do the work

All 12 cleared the mechanical near-dup guard against the 168-topic index. Three were
dropped on judgment rather than by the guard: **6** and **8** sit close to the 2026-08-02
day on how speech-native models represent audio (same source entry, adjacent layer), and
**11** overlaps the 2026-07-31 day on spec-driven development with coding agents. Of the
survivors, the three picked were the ones with live in-window evidence rather than
evergreen explainer material.

## Notes on the research runs

- The **voice-agent** run's Reddit layer is unusable: search returned 403 for every
  subquery and the engine fell back to subreddit listing discovery, so the footer's 18
  threads and 10,412 upvotes are unrelated front-page posts. The brief states this in its
  first paragraph and the footer line is annotated; the finding rests on the GitHub issue
  tracker, HN and web layers instead. Recorded because a healthy-looking footer is exactly
  the failure this note exists to catch.
- The **ticket-assignment** run surfaced two pieces of retrieved content carrying
  directive text: a public gist publishing another team's agent configuration, and an
  automated comment telling the reader to close their own issue as a duplicate. Both were
  treated as data describing how other teams configure agents. Neither was acted on.

## Fuel

The pool is now **empty**: 3 eligible entries, all 3 picked and retired, 1 day of runway
at the pre-run check. The next cycle has nothing to draw on unless the `self` library
gains new entries before it runs.
