# Provenance — 2026-07-23

*Redacted by design: source rationale is summarized at the topic level; no raw
saved-link URLs or private capture notes appear here.*

## Seed entries (from the private library)

Three saved entries seeded today's funnel, plus one adjacent entry that
reinforced the model comparison:

- **A** — a Chinese open-weight model release and the question of whether it is
  self-hostable on a modest Apple machine.
- **B** — a visual walkthrough of how large language models work under the hood.
- **C** — a browser-native tool that saves a slide deck as one self-contained
  HTML file.
- *(supporting)* — a hands-on review of a local, open-source coding model in the
  Qwen family.

## Fan-out: 12 adjacent candidates

Each was checked against the near-duplicate guard; none collided with a
previously published topic. Pursued topics marked ✅.

From the local/open-model thread (A + supporting):
1. ✅ MLX vs llama.cpp for local LLM inference on Apple Silicon
2. Quantization tradeoffs in local LLMs people actually notice
3. ✅ DeepSeek V4 vs Qwen 3.6 for local coding models
4. Why mixture-of-experts makes big open models runnable on consumer hardware

From the "how LLMs work" thread (B):
5. Karpathy's nanochat and learning to build an LLM from scratch
6. How tokenization quietly causes LLM bugs
7. Mechanistic interpretability in 2026 — can we read what's inside a model?

From the self-contained-HTML thread (C):
8. Local-first sync engines (ElectricSQL / Zero / PowerSync)
9. Single-file self-contained HTML apps as a durable document format
10. ✅ Astro vs Next.js in 2026
11. The revival of "view source" — HTML artifacts vs SaaS lock-in
12. Generating slide decks with AI as editable HTML instead of PDF

## Why these three

Narrowed on curiosity, freshness, and learnability — with one extra, hard
constraint: which topics the live-discussion engine could actually resolve.
The conceptual seeds (tokenization internals, abstract "single-file HTML,"
local-first, nanochat) hit entity-miss demotion and returned off-topic noise,
so they were re-anchored on named entities with active 30-day communities. The
three that cleared are all clean comparisons:

- **MLX vs llama.cpp** — the local-inference *runtime* decision, resolved as a
  portability-vs-peak-Apple-speed split. Connects to the earlier day on Apple
  Silicon as a local-LLM box.
- **DeepSeek V4 vs Qwen 3.6** — the *model* decision one layer up: which open
  weights people actually self-host, and how they orchestrate the cheaper one.
- **Astro vs Next.js** — a deliberate change of domain from AI to web
  frameworks, carrying the same "durable, ship-less" thread from seed C.

The day's shape: a "what can I run on my own hardware" throughline (topics 1–2)
plus a web-framework palate-cleanser (topic 3).
