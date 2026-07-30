# Provenance — 2026-07-30

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **Metal-powered command-line video upscaler for macOS** (tags: video, upscaling,
  metal, macos, ffmpeg), captured yesterday. Pull: the only entry in the eligible pool
  whose note records undirected delight rather than an intention or a justification — a
  tool stumbled into while reading someone's blog. It is also the newest entry available
  and the only non-AI-industry domain in the pool, which made it the anchor for the day.
- A saved **local-first, open-source alternative to a hosted AI design tool** (tags:
  open-source, design, local-first, llm, agent-cli, prototyping), captured in May. Pull:
  the note states a concrete future use rather than curiosity, which is a stronger signal
  than interest. Selected for its local-first axis rather than its design axis, because the
  design axis was already spent (see the fan-out notes).
- A saved **discussion thread on lessons and debates in agentic coding** (tags: ai, coding,
  software-engineering, tech-debt, automation), captured in May. Pull: the note is about a
  change in what the job is, not about a tool, which is the kind of entry that fans out to
  process questions rather than product questions.

Chosen for domain spread (GPU media tooling · distributed systems · engineering process).
The eligible pool is 15 entries and 13 of them are AI-industry entries, so the media-tools
pick is the only genuine domain escape available and it was taken first. Four entries sit
in the jobs-and-industry cluster already published on 2026-07-28 and were passed over for
that reason. Fuel check at start of run: 14 eligible, span 96 days, capture rate 0.15/day,
roughly **4 days of runway** at 3 per day — the tightest this log has recorded, and worth
flagging to the operator.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the video-upscaler entry:
1. Metal compute shaders vs CUDA for local media work on Apple silicon
2. Where ffmpeg filter chains lose to native GPU video pipelines
3. AI video upscaling models people actually run locally ✅ picked
4. Video codec choices for archiving: ProRes vs HEVC vs AV1
5. Why >4K H.264 and HEVC playback breaks: hardware decoder limits

From the local-first design-tool entry:
6. Local-first software: what CRDT sync actually costs to run ✅ picked
7. Design tokens as the handoff format between agents and design tools
8. Where AI design-to-code tools break for production UI
9. Canvas and SVG editor architecture: what makes a design tool feel fast

From the agentic-coding entry:
10. Tech debt in codebases where most code is agent-written
11. Code ownership and blame when an agent wrote the commit ✅ picked
12. Test suites as the only durable spec in agent-written code

Near-dup guard: none of the 12 were flagged (threshold 0.6) and none triggered the
small-index defer — the index holds 156 topics. But the highest score in the batch is the
interesting one: **#7 scored 0.5726** against the 2026-07-24 design-tokens day, a hair
under the threshold and substantively the same topic; **#8 scored 0.2951** against the same
day and 0.1956 against the 2026-06-21 generative-UI day. The design fan was effectively
burned on 07-24, which is why the local-first entry was mined for its infrastructure
adjacency instead of its design adjacency. Next-highest was #8, then **#3 at 0.2339**
against the 2026-07-12 local-image-generation day and 0.228 against the 2026-07-08
local-LLM-hardware day — both "local inference" collisions on the word rather than the
subject, which is the guard doing what it should and stopping short of a verdict. The
cleanest candidates in the batch were #5 (0.0399) and #4 (0.045).

## Narrowing to the top 3

- **#3 AI video upscaling** — picked over #1, #2 and #5, which are all real questions with
  thin 30-day discussion; a codec or decoder-limit brief would have returned vendor pages,
  not conversation. #4 was the runner-up and lost on the same freshness test. #3 also has
  the useful property of interrogating the source entry rather than restating it: the saved
  tool is a *non-generative* Metal scaler, so asking what the AI option costs puts the two
  in tension, which is where the brief ended up.
- **#6 Local-first CRDT costs** — picked as the day's only non-AI-agent engineering topic
  and the lowest-scoring candidate in its group at 0.1037. Preferred over #9, which is
  genuinely interesting but is a craft question with no 30-day news hook, and over #7 and
  #8 for the dedup reason above. Seeded toward the operational bill rather than the merge
  algorithm, which is what kept it clear of a CRDT explainer.
- **#11 Code ownership** — picked over #10 and #12, which both score against the 2026-07-27
  stop-conditions day and the 2026-07-29 ensemble-review day and would have re-run last
  week's material from a new angle. #11 is the only one of the three that moves off code
  *quality* onto attribution, policy and liability, none of which the index has covered.
  Seeded toward blame, sign-off and the commit record rather than toward review practice,
  specifically to stay clear of 07-29.

Final three picked titles scored 0.1495, 0.0913 and 0.1228 against the index. No past topic
cleared the 0.2 connection threshold for any of the three, so `meta.json` records no
connections — a genuinely unconnected day, verified by spot-checking the helper against two
titles that do connect.

## Evidence quality notes

Engine asserted before the run: `--diagnose` reported v3.3.2 with 7 sources active,
`bird_authenticated: true`, `local_mode: true`, and Brave as the web backend. All three
topics are concept phrases with no single named entity, so the cluster ranker demoted every
cluster with "entity-miss" on all three runs and none of the ranked cluster scores carry
information — each brief was read off the raw items directly. YouTube captured 0 usable
transcripts on two of three runs. Beyond those shared caveats:

- **Video upscaling** — this topic was run **twice**. The first attempt used a topic string
  containing the phrase "local AI", which turned out to be a keyword trap: the corpus came
  back dominated by local-LLM Show HN posts (a local-first agent router, a local AI file
  scanner, a GPU bandwidth benchmark) with almost nothing about upscaling, and Reddit
  returned only generation threads. The run was discarded and re-run with the phrase
  removed, which lifted the corpus from 51 to 62 items and turned up the actual on-topic
  material. Even after the re-run the engine layer was thin: the load-bearing numbers in
  the brief — the SeedVR2-1.4B VRAM figures, the 9.7-vs-9.8 blind-test result, and the
  temporal-flicker mechanism — all came from post-engine supplements. The engine's real
  contributions were the r/StableDiffusion distillation announcement, the live GitHub star
  counts, and one X post that supplied the brief's sharpest quote.
- **Local-first sync** — 76 items across 6 sources, Polymarket at zero. The engine layer
  was strong on GitHub (live star counts for Electric, Yjs, Automerge and TanStack DB) and
  weak everywhere else; the Reddit total of 15,680 upvotes is almost entirely r/webdev
  front-page noise, and the single most useful engine observation was negative — that
  Hacker News' "local-first" items this month are overwhelmingly desktop AI tools rather
  than sync projects, which became a finding in its own right. All three cost numbers in
  the brief came from supplements.
- **Code ownership** — richest corpus of the three at 126 items across 6 sources, and the
  only run where the engine layer was genuinely load-bearing: the r/ExperiencedDevs thread
  about inheriting a 99%-AI-generated project, the attribution tooling (agent-trace,
  TracesHub, atomic), the copyright case, the xAI-vs-user suit, and the Emacs force-push
  post all came from the engine. Supplements added the LLVM policy text, the Co-Authored-By
  dispute, and the Bot Sponsorship framing. One accuracy note: the Emacs force-push claim
  rests on a single X post and is attributed as such in the brief rather than stated as
  fact; the general pattern (history rewrites to strip AI trailers) is independently
  corroborated.

Nine post-engine web supplements across the three topics, three per brief, all appended to
the non-committed raw evidence files under the run's temporary memory directory.
