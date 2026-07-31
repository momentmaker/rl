# Provenance — 2026-07-31

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **essay on making coding agents follow senior-engineering workflow** — specs,
  tests, reviews, scope discipline, with every step terminating in concrete evidence
  (tags: ai-coding, software-engineering, agent-skills, workflow, verification), captured
  in May. Pull: the note pairs a judgment of usefulness with an observation about the
  repo's traction, which is the shape of an entry saved to come back to rather than one
  saved in passing.
- A saved **discussion thread on what software abstractions cost once AI compresses the
  work** (tags: software, abstraction, ai, job-market, productivity, industry), captured in
  May. Pull: the note frames it as one more instance of a genre the operator keeps
  returning to, and a recurring-interest signal outranks a one-off in the guidance.
- A saved **open-source starter kit and component library for building AI-driven design
  apps** — canvas, toolbar, layers, timeline and keyframes, pitched as giving an agent an
  application architecture rather than components (tags: ai, design, open-source,
  ui-library, creative-tools), captured three days ago. Pull: the weakest note of the
  three, recording plain attraction with no stated use. Selected anyway on domain grounds,
  as explained below.

Chosen for domain spread (engineering process · hiring and industry · creative-tool
engineering). The eligible pool is 12 entries and 11 sit somewhere in the AI-industry
cluster, so the design-tooling entry was the only genuine domain escape available and was
taken despite the thin note — the guidance weights the note heaviest, but it also warns
against three picks from one cluster on one day, and that constraint bound harder here.

Two entries with stronger notes were deliberately passed over. An agent-harness entry
whose note records real enthusiasm sits directly on the 2026-07-28 harness-vs-model day.
An entry on where software engineering is heading sits in the same jobs-and-industry
cluster as the abstraction entry and as 2026-07-28's junior-developer day; mining both
would have produced two versions of one topic.

Fuel check at start of run: **12 eligible, span 96 days, capture rate 0.12/day, roughly 4
days of runway** at 3 per day. Capture is running below burn and this is the second
consecutive day the log has recorded a 4-day runway — worth flagging to the operator.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the agent-workflow entry:
1. Spec-driven development with coding agents ✅ picked
2. What verification evidence agents must produce before claiming done
3. Bounding scope creep in agent-written pull requests
4. Writing agent skills that survive a real repo

From the abstraction-costs entry:
5. AI-generated resumes and the collapse of hiring signal ✅ picked
6. Small teams as the new default engineering org size
7. Leaky abstractions when nobody knows the layer below
8. Technical interviews redesigned for the AI era

From the design-tooling entry:
9. Canvas and timeline UI engineering for creative tools ✅ picked
10. Visual regression testing for AI-generated interfaces
11. Undo, redo and history models in creative apps
12. Giving agents an application architecture instead of components

Near-dup guard: none of the 12 were flagged and none triggered the small-index defer — the
index holds 159 topics. The fan was shaped defensively, because the last five published
days are unusually concentrated: 07-26 agent memory, 07-27 stop conditions, 07-28 harness
and junior developers, 07-29 ensemble code review, 07-30 code ownership. Candidates 2 and 3
are the clearest casualties of that concentration — #2 restates 07-27's stop-conditions
question in different words, and #3 walks into 07-29's finding that AI makes pull requests
3.5x bigger. Both were dropped at the narrowing step rather than by the guard, which is the
judgment call the guard is not meant to make.

## Narrowing to the top 3

- **#1 Spec-driven development** — picked over #4, which was the stronger candidate on live
  discussion volume but is a component of the harness question published on 07-28. #1 is
  the actual thesis of the source entry (specs, tests, reviews, scope discipline) and it
  carries a real contested camp rather than a how-to, which is what the guidance means by a
  discussion-shaped seed. Seeded toward what teams report and where it becomes waterfall
  theater, specifically to invite the counter-argument rather than the pitch.
- **#5 AI-generated resumes** — picked over #6, #7 and #8. #8 is nearly the same topic and
  was folded into #5's seed as the screening angle rather than run separately. #7 is the
  most literal reading of the source entry and was rejected as evergreen with no 30-day
  hook. The seed was deliberately aimed at the **screening** side — what hiring teams
  changed — to stay clear of 07-28's junior-developer-supply day, which covered the same
  industry from the candidate-pipeline direction.
- **#9 Canvas and timeline UIs** — picked over #10 and #12, both of which drift back into
  AI-agent territory and would have made this a three-agent-topic day. #11 was folded into
  #9's brief as the undo-model section rather than spent as its own slot. #9 is the only
  candidate in the batch that is pure engineering craft, and the nearest thing to it in the
  index is 07-24's AI-native video editors day at 0.0863 — same word "timeline", different
  subject, which is the guard behaving correctly.

Final three titles scored **0.1172, 0.0581 and 0.0863** against the index, all far under
the 0.6 threshold. No past topic cleared the connection threshold for any of the three, so
`meta.json` records no connections — the second consecutive unconnected day.

## Evidence quality notes

Engine asserted before the run: `--diagnose` reported v3.3.2 with 7 sources active,
`bird_authenticated: true`, `local_mode: true`, Brave as the web backend. Resolved at the
plugin cache path; the marketplace clone was explicitly avoided as a known stale copy.
YouTube was degraded on all three runs — 1 video and 0 usable transcripts each, with the
engine itself flagging a stale `yt-dlp`. Polymarket returned nothing on all three, as
expected for these topics. Beyond those shared caveats:

- **Spec-driven development** — 73 items across 6 sources. Reddit's 18 threads are
  r/ClaudeAI and r/ExperiencedDevs general-AI noise after the public search endpoint
  returned 403 and the engine fell back to listing discovery, so the footer's 30,219
  upvotes are real but not topically load-bearing. The brief is carried by GitHub live API
  numbers, X, HN and web. The three headline star counts were re-verified against the
  GitHub API during review and matched within two stars of drift. Two attractive figures
  circulating in search summaries were dropped after the pages they were attributed to
  turned out not to contain them.
- **Hiring screening** — the seed phrase was a partial keyword trap: Reddit returned 21
  threads led by r/BestofRedditorUpdates and r/relationship_advice, because "screening
  candidates" collides with relationship-drama vocabulary. HN's 35 items were generic AI
  noise. The engine's ranked clusters were unusable and the brief was sourced from targeted
  web verification instead; the footer overstates on-topic depth accordingly. The largest
  dataset in the window (38.5% of 19,368 interviews) is vendor-published with no
  false-positive rate disclosed, and is carried in the brief with that caveat attached
  rather than quoted clean. Two widely circulated detector statistics were dropped for
  having no primary source behind the aggregator summaries.
- **Canvas and timeline UIs** — 94 items across 5 core sources and the cleanest Reddit
  targeting of the day (r/webdev, r/gamedev, r/programming), though the ranked clusters
  still skewed to front-page noise because the topic is a concept phrase with no single
  named entity. The load-bearing material came from the HN and web sections plus targeted
  fetches. All seven library star counts were pulled from the GitHub API rather than
  trusted from blog posts.

Ten post-engine web supplements across the three topics, all appended to the non-committed
raw evidence files under the run's temporary memory directory.
