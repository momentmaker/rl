# Provenance — 2026-07-24

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved note on **reducing agent cost by escalating from a cheap tier to a stronger
  frontier model** (tags: llm, agent, cost-optimization). Genuine personal pull: it maps
  onto a standing plan to run a local model that plans/orchestrates and calls out to
  smarter hosted models for the hard parts.
- A saved **AI design-language CLI tool** (tags: ai, design, cli, frontend). Pull: a
  concrete tool for generating design from AI, framed as a step up from earlier
  design-generation tooling.
- A saved **macOS AI video editor** (tags: video-editor, macos, ai-integration,
  open-source, swift) — the freshest capture in the pool. Pull: enthusiasm for
  AI-powered video editing.

Chosen for domain spread (LLM infra · design systems · creative video) so the funnel had
room to diverge.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the LLM-infra entry:
1. LLM model routing and cascades: cheap model triages, strong model executes
2. Local model as the orchestrator calling out to cloud frontier models ✅ picked
3. Semantic search over CI and build logs to cut debugging time
4. Token and cost-optimization tactics teams use for agent runs

From the design entry:
5. AI tools that generate whole design systems, not just components
6. Design tokens as the contract between AI design tools and code ✅ picked
7. CLI-first design tooling: generating UI from the terminal
8. How AI-generated UIs escape the generic "AI slop" look

From the video entry:
9. AI-native video editors: prompt- and agent-driven timeline editing ✅ picked
10. On-device AI video editing and generation on Apple Silicon
11. Auto-editing: AI that cuts long footage into short-form clips
12. Native macOS Swift AI apps vs Electron for creative tools

Near-dup guard: all 12 scored below the dedup threshold against the published index
(highest ≈ 0.21, "generate whole design systems" vs the prior Generative-UI day). None
flagged.

## Narrowing to the top 3

- **#2 Local orchestrator → frontier models** — strongest curiosity (ties to the standing
  plan), live 30-day discussion around deterministic local/hosted routing, and concretely
  learnable (real projects, hardware thresholds, failure modes).
- **#6 Design tokens as the AI design-to-code contract** — most concrete and teachable of
  the design candidates; #5/#7 skewed closest to the already-published Generative-UI day,
  so tokens (the mechanism, not the vibe) won.
- **#9 AI-native video editors** — closest to the freshest source entry, with a live burst
  of agent-native editor launches to learn from; picked over #10 (overlaps recent
  Apple-Silicon coverage) and #11 (narrower).

Final three span three distinct domains and do not overlap.
