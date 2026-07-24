---
ready: true
---
🎲 *Random Learning — 2026-07-24*

Three rabbit holes today, one loose theme: where the "AI agent" actually plugs into an existing craft — your model stack, your design system, your video timeline — and where the seams still show.

*1. Local model as orchestrator, frontier model on call*
The framing quietly shifted this month from "local vs cloud" to *routing*: assume you run both, then argue over how to split the work. New Show HN projects like Wayfinder Router pitch deterministic local↔hosted routing, with the honest catch that a small model deciding what counts as "hard" is itself the unreliable part. The pattern people actually ship keeps the frontier model *inside the harness* — the top demo (250K views) runs local quant models on a 5090 but drives them through Claude Code, where the planning and tool calls live. Frameworks make the swap a one-liner (LangGraph checkpointing behaves the same for Ollama or an API). The payoff is bounded: local wins the long-context, repetitive, privacy-sensitive turns; the breakpoints are hardware cost (a four-figure Mac to plan well), fragile throughput (one config change = 10x), and the router misjudging its own context window.

*2. Design tokens as the AI design-to-code contract*
As Figma buys the AI coding layer (Bud) and Claude ships a design→handoff bundle, the design tool and the code-gen tool are collapsing into one pipeline — which makes tokens a shared schema, not an optional spec. The recurring failure: an AI-generated design looks right but carries 25pt spacing into an 8pt codebase, and it ships anyway. "Bring your own tokens" has become the line separating real design-system tools from slop generators; the workable architecture is a 3-tier token taxonomy synced from Figma variables to code over MCP/Code Connect. Necessary but not sufficient — teams still keep a human reviewer, amid loud AI-code backlash (Godot banning AI contributions, a shop charging $10k/week to delete AI code).

*3. AI-native video editors go agent-first*
A burst of new editors redefine "AI-native" as *agent-controllable architecture* — a JSON timeline plus MCP/REST APIs an agent can drive — not a chat box bolted onto a legacy editor. What creators actually trust is the self-verifying grunt work: on-device transcription, captions, semantic shot-finding, rough cuts that "check their own work." The contrarian consensus: stop at the prompt and you get fake-looking output that drags you back to the timeline. Tellingly, the manual timeline is being preserved on purpose — as an explicit edit stage, and as the pro-editor trajectory data these agents train on. Full automation works but is DIY (Claude Code plus open toolkits), and exposing your whole timeline to an agent is also an attack surface.

_Sources: last30days across HN, Reddit, X, YouTube, GitHub + web grounding._
