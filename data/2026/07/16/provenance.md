# Provenance — 2026-07-16

Redacted by design: source `self` URLs and private `why?` notes are never
committed. This file records the topic-level rationale and the candidate funnel.

## Source signal (3 entries mined from the private `self` library)

The pool skews heavily toward AI tooling, models, and coding agents. To keep the
day genuinely wide, the funnel was steered toward three saved entries with strong
personal pull that span three unrelated domains — culture/linguistics, philosophy
of mind, and hands-on dev/infra:

1. A saved article on the **digital revival of Sanskrit**, annotated with interest
   in the return-to-ancient-tradition trend. Seeded the language / NLP track.
2. A saved **theories-of-consciousness reference site**, flagged as an intriguing
   reference worth exploring. Seeded the philosophy-of-mind track.
3. A saved **Telegram serverless-bot backend** doc, annotated with a note that
   Telegram is heading in this direction. Seeded the dev / infra track.

## Fan-out: 12 adjacent candidates (all passed the near-dup guard)

From the Sanskrit / language seed:
- AI reviving endangered and ancient languages
- Speech synthesis for tonal liturgical chanting
- Digitizing oral traditions with machine learning
- Is Sanskrit uniquely suited to computing and NLP

From the consciousness seed:
- IIT vs Global Workspace Theory of consciousness
- The modern revival of panpsychism
- Could large language models be conscious
- The hard problem of consciousness in 2026

From the Telegram / serverless seed:
- Building Telegram bots on serverless edge platforms
- Telegram Mini Apps and the TON ecosystem
- Webhook vs long-polling for chat bot backends
- Telegram Stars and the in-app bot economy

## Narrowed to 3 (curiosity, freshness, learnability, non-overlap)

1. **Is Sanskrit really the ideal language for AI?** — the language pick. Chosen
   over the broader "reviving ancient languages" candidate because it carries a
   sharp, testable claim: the viral "NASA said Sanskrit is best for AI" myth vs
   what linguists and NLP practitioners actually find (Briggs' real 1985 paper,
   sandhi breaking tokenizers, Panini's grammar as the defensible core, and
   India's 2026 native Sanskrit-LLM push).
2. **Could today's LLMs actually be conscious?** — the philosophy pick, narrowed
   from the general consciousness-theories seed to the most live, most learnable
   angle. Anchored by Anthropic's July 2026 "J-space" finding, the model-welfare
   program and Claude's own 15-20% self-estimate, the introspection studies, and
   the fracturing "stochastic parrot" camp.
3. **Building Telegram bots on serverless and edge platforms** — the dev/infra
   pick, honoring the source doc directly. The webhooks-only constraint, cold
   starts, Durable-Objects-vs-KV state, the webhook race-condition footgun, and
   the grammY-plus-Nitro write-once multi-target pattern.

## A note on domain spread

The three picks were chosen to avoid the AI-model rut that dominates the pool:
culture/linguistics, philosophy of mind, and dev/infra. Two touch AI only
tangentially (Sanskrit-for-NLP is a myth-busting linguistics story; the Telegram
pick is pure edge-infra), and the consciousness pick approaches AI from the
philosophy-of-mind side rather than the capability race.

## Connections

None of the three final topics scored above the connection threshold against the
prior index. The near-dup guard cleared all twelve fan-out candidates, and the
read-only `store.related` check returned zero related prior topics for each of
the three — the IDF-weighted score down-weights common tokens like "ai" and
"llm", so the distinctive terms (sanskrit, consciousness, telegram, serverless)
map to genuinely new territory. All three are new ground.
