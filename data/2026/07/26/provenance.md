# Provenance — 2026-07-26

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **visual explainer of how large language models work** (tags: llms, training,
  parameters, text-data, vocabulary), captured in April and carrying the strongest
  appreciation note in the whole eligible pool. Pull: genuine enthusiasm for a
  well-illustrated mechanical explanation, which makes "what does the model actually get
  handed" the load-bearing question.
- A saved **persistent-intelligence add-on for a coding agent** (tags: software,
  automation, productivity, nodejs, ai-assistant). Pull: interest in the efficiency angle,
  which under the hood is a memory-and-context design problem rather than a compression
  trick.
- A saved **component-block install log for a landing page** (tags: web-development, ui,
  pricing, react, landing-page), where the capture note points somewhere quite different
  from the title: the interesting part was the artifact of the terminal session itself.
  That mismatch is what the fan-out followed.

Chosen for domain spread (model internals · agent infrastructure · developer craft) and to
step out of the local-model and agentic-coding cluster that has dominated recent days.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the LLM explainer entry:
1. Mechanistic interpretability for practitioners
2. Tokenizers as the hidden source of model failures ✅ picked (reframed toward byte-level)
3. Why next-token-prediction explanations mislead people
4. Learning ML by re-implementing models from scratch

From the persistent-intelligence entry:
5. Context engineering over prompt engineering — *dropped on judgment*
6. Agent memory that persists between sessions ✅ picked
7. Prompt caching economics for agent token bills
8. Subagent context isolation as the real token lever

From the component-block entry:
9. Terminal demo recording craft with VHS and asciinema ✅ picked (merged with #11)
10. Agent demo artifacts as pull request evidence
11. Screenshot-driven visual verification loops for agents
12. Pricing page design in the component-registry era

Near-dup guard: none of the 12 were flagged. Highest score was 0.193 for candidate #5
against the previously published Context-rot day, which is why #5 was dropped by judgment
rather than by threshold — it is the same neighbourhood as an entry already on the site.
Next highest were 0.134 (#7 vs the AI-native-video-editors day) and 0.111 (#6 vs the
design-tokens day), both comfortably clear.

## Narrowing to the top 3

- **#2 Tokenization failures**, reframed to include whether byte-level models fix them —
  highest curiosity of the four explainer-adjacent candidates and by far the most
  learnable: there are measured numbers (rewrite-sensitivity rates, patch sizes, FLOP
  savings) instead of intuitions. Picked over #3, which is the same argument without the
  mechanism, and #1, which had no concrete 30-day corpus.
- **#6 Agent memory between sessions** — the actual mechanism behind the source entry's
  efficiency claim, and the liveliest of the four: a real practitioner argument, a dense
  run of launches, and a benchmark correction worth keeping. Picked over #7 and #8, which
  are the cost consequence rather than the design question.
- **#9 Terminal demos**, merged with the verification half of #11 — the craft question the
  third entry's capture note actually pointed at, with concrete tooling and a live
  culture-of-credibility thread. Picked over #10 (narrower) and #12 (a design topic, and
  the closest neighbour to an already-published generative-UI day).

Final three span three distinct domains and do not overlap.

## Evidence quality notes

All three briefs carry an explicit italic evidence note, per the engine's honesty
convention, because recall was uneven on every one of them:

- The tokenization brief ran into a thin social window (Reddit search returned 403 and
  degraded to a keyless fallback, YouTube returned zero, and most X "byte"/"token" hits
  were unrelated), so it rests on two live July artifacts, one unusually clear X post, and
  the 2026 paper crop from the web supplements.
- The agent-memory brief had two unrelated Chinese web-drama videos score into its YouTube
  slot on a "memory system" collision, and its X side is heavily promotional; the read
  leans on the threads that did surface, the Show HN run, and the benchmark literature.
- The terminal-demo brief hit the worst collision of the three: "VHS" on X in this window
  is almost entirely videotape nostalgia, so the footer's 24 X posts are largely
  off-topic. The brief says so up front and rebuilds the read from tooling docs, repo
  evidence, and one r/commandline satire thread at 1,981 upvotes.
