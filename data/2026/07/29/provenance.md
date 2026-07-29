# Provenance — 2026-07-29

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **multi-agent pull-request review plugin for a coding-agent CLI** (tags:
  pr-review, multi-agent, claude-code, ai, plugin), captured in May. Pull: the strongest
  note in the eligible pool, because it is the only one that records an existing habit
  rather than an intention — the tool is compared against another review tool already in
  regular use. Live usage beats curiosity as a signal.
- A saved **write-up of running local language models on an M4 laptop** (tags:
  local-models, llm, macbook, open-source, configuration, coding), captured in May. Pull:
  a calibration question rather than a shopping question — what this class of hardware can
  actually do, stated as wanting a gauge.
- A saved **collection of AI-native React components** (tags: react, ui-components,
  opensource, ai-native, npm), captured in June. Pull: lightest of the three notes, and
  chosen anyway as the domain outlier — it is the only entry in the eligible pool whose
  adjacency reaches the web platform rather than the model layer.

Chosen for domain spread (agent evaluation · local inference · web platform). The
eligible pool is 17 entries and every one of them is tech, so today is a tech day by
supply, not by choice; the third pick is where the spread had to be manufactured. Two
further entries sit in the jobs-and-industry cluster already published on 2026-07-28, and
two more sit in the design-tooling cluster already published on 2026-07-24, which is the
dedup pressure to watch for coming days. Fuel check at start of run: 16 eligible, roughly
5 days of runway at 3 per day.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the PR-review entry:
1. Ensemble code review: a second model over the same diff ✅ picked
2. The false-positive tax in AI code review
3. Resumable agent runs and persisting state between stages
4. Who reviews the code now that agents write most of it

From the local-models entry:
5. How much unified memory a useful local model actually needs
6. Quantization quality cliffs: where q4 stops being good enough ✅ picked
7. The 128K context claim versus what local models retain
8. Chat template surgery: turning on thinking and tool use locally

From the components entry:
9. Why server-sent events came back in the LLM era ✅ picked
10. Deliberate dark patterns as design critique
11. Streaming UI patterns for token-by-token interfaces
12. The npm micro-package supply chain in 2026

Near-dup guard: none of the 12 were flagged (threshold 0.6) and none triggered the
small-index defer — the index holds 153 topics. Highest score in the batch was 0.243 for
#10 against the 2026-06-12 aesthetic-usability day, then 0.234 for #5 against the
2026-06-25 Apple-silicon-inference-box day, and 0.174 for #11 against the same 06-12 day
with 0.160 against the 2026-06-21 generative-UI day. Two candidates were dropped from
contention by judgment despite passing numerically: #5 is substantively the same sizing
question as the 06-25 day, and #7 is context rot under a different name (0.098 against the
2026-06-21 context-rot day, a score that badly understates the overlap). That is the guard
working as a floor, not as the decision.

## Narrowing to the top 3

- **#1 Ensemble code review** — picked over #2 because the ensemble framing subsumes the
  false-positive question as a sub-theme and the seed could be written to pull both, which
  it did. Picked over #3, the highest scorer in its group at 0.149 against the 2026-07-26
  agent-memory day, and over #4, which invites an opinion essay rather than a measurable
  answer. Seeded to ask what people *find* after a second pass, not whether they like it.
- **#6 Quantization cliffs** — the cleanest score in the whole batch at 0.067, and the only
  one of the local-models four that escapes an already-published axis: 2026-07-23 covered
  MLX versus llama.cpp (runtimes) and DeepSeek versus Qwen (model choice), 2026-07-24
  covered local-as-orchestrator, and 2026-06-25 covered the hardware box. Quant *quality*
  was the remaining gap. #8 was the runner-up and is narrower than it looks in terms of
  live discussion volume.
- **#9 Server-sent events** — picked over #11, which is the same streaming subject seen
  from the UI side and scores more than twice as high against past days, and over #12,
  which is security-flavoured and adjacent to the 2026-06-17 malware-via-repo day. #10 was
  the most entertaining candidate and the weakest evidence bet: satire does not leave a
  30-day trail. Seeded toward the transport decision rather than the API tutorial.

Final three picked titles scored 0.111, 0.093 and 0.072 against the index. No past topic
cleared the 0.2 connection threshold for any of the three, so `meta.json` records no
connections — this is a genuinely unconnected day rather than an omission.

## Evidence quality notes

Engine asserted before the run: `--diagnose` reported v3.3.2 with 7 sources active,
`bird_authenticated: true`, and Brave as the web backend. All three topics are concept
phrases with no single named entity, so the engine's cluster ranker demoted every cluster
with "entity-miss" on all three runs and none of the ranked cluster scores carry
information — each brief was read off the raw items directly. Reddit 403'd on the public
search endpoint on every run and fell back to keyless listing discovery, which is why all
three footers show large upvote totals attached to general front-page threads rather than
on-topic ones. YouTube captured 0 transcripts across all three runs, consistent with the
engine's own stale-yt-dlp diagnostic. Beyond those shared caveats:

- **Ensemble code review** — richest corpus of the three at 98 items across 7 sources. The
  Polymarket line is pure keyword collision: "second pass" pulled seven "second-best AI
  lab" markets, which carry no information about the topic and are ignored in the brief.
  Load-bearing evidence is the Hacker News layer, which was genuinely on-topic (a
  PR-size-inflation post, a review-is-not-viable argument, an Ask HN on reviewing AI code,
  and the formal-verification Show HN), plus the web layer and three post-engine
  supplements. The single most important number in the brief — 93.4% of flagged locations
  found by exactly one of four tools — came from a supplement, not from the engine.
- **Quantization cliffs** — thinnest corpus of the three at 46 items across 6 sources, with
  Polymarket at zero and Hacker News at only 5 items. The Reddit total is the least
  representative of the three: the top-scoring thread is a robot dying mid-presentation at
  5,210 points, which is front-page noise. The one on-topic HN item (four identically
  labelled quants measuring different bits per weight) was the seed for the brief's lead,
  and the two other load-bearing findings — the tool-calls-degrade-before-chat ordering and
  the QAT-below-4-bit split — both came from supplements. X contributed two useful items on
  the quant ladder and on who actually maintains the k-quant code.
- **Server-sent events** — 68 items across 5 sources, YouTube and Polymarket both zero. Of
  the three runs this had the best X layer and the worst Reddit and HN layers: the top
  Reddit thread is career-advice fluff at 4,340 points and the top HN item is a shell
  scripting post at 400 points, while X supplied the four-way real-time-primitive
  breakdown, the POST-based SSE implementation, and the best single anecdote in the day's
  research (an ISP silently blocking persistent streaming connections, so deploys timed out
  on transactions that had actually succeeded). The entire MCP transport-deprecation
  timeline, which is the brief's contrarian spine, came from supplements rather than the
  engine.

Nine post-engine web supplements across the three topics, three per brief, all appended to
the non-committed raw evidence files under the run's temporary memory directory.
