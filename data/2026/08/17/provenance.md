# Provenance — 2026-08-17

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked from a pool of 6)

Today's pool held six eligible entries across very different domains. Three were picked,
weighting each entry's own capture note heaviest and then spreading across fields — and,
this run, deliberately breaking a long AI/coding-agent streak in the recent index by
capping the day at a single AI topic.

- A saved **science Q&A on mushroom-induced hallucinations** — altered perception and the
  vivid imagery people report under psilocybin (tags: mushroom, hallucinations, psychedelic,
  biology, science), captured 16 August. Pull: a genuine curiosity note about *why*
  hallucinated experience feels like a structured world rather than random noise, which is
  what sent the fan toward the neuroscience of hallucination *form* rather than toward
  mushrooms as a subject.
- A saved **self-hostable HTTP push-notification service** for sending alerts to phone or
  desktop from any script, with open-source mobile apps (tags: push-notifications, http,
  open-source, self-hosting, mobile-app), captured 16 August. Practical-tool note; the fan
  went to the *stack* people build around it, not the single tool.
- A saved **free tool that rewrites AI-flavored text into plain prose** and documents how
  AI text watermarking works (tags: ai, text-rewriting, plagiarism, watermarking, tool),
  captured 16 August. Enthusiast note about detecting and removing AI tells; the fan went
  to the detection/humanizer/watermark arms race the tool sits inside.

Domain spread: **hallucination neuroscience · self-hosted infrastructure · AI-text
forensics**. Three different fields; only one touches AI, on purpose.

## The 12 adjacent candidates

From the mushroom-hallucination Q&A:
1. **Form constants: why hallucinations converge on the same geometric patterns** ← picked
2. Lilliputian hallucinations: seeing tiny people across drugs, fever and Charles Bonnet
3. Charles Bonnet syndrome: vivid hallucinations as vision fails
4. Shared and collective hallucinations: can two people see the same thing?

From the self-hosted push service:
5. **Self-hosted alerting stacks people actually run in their homelab** ← picked
6. UnifiedPush: routing phone notifications around Google and Apple
7. How mobile push actually works: APNs, FCM, Web Push and VAPID
8. Notification fatigue: how self-hosters tune alerts so they still get read

From the AI-text rewriting tool:
9. **AI humanizer tools and whether AI-text detectors are reliable** ← picked
10. AI text watermarking like SynthID and whether paraphrasers strip it
11. Why AI text detectors keep false-flagging human writing
12. The tells of AI slop prose: the words and rhythms that give it away

Near-dup guard: **0 of 12 flagged** against a 174-topic index. The highest near-scores
were all in the low 0.1s (nearest neighbours in the self-hosting and AI-text clusters),
well under threshold.

## Narrowing to 3

One topic per source entry, three different fields:

- **#1 over #2/#3/#4** — form constants is the candidate that actually *answers* the source's
  pull (why hallucination feels like a shared, structured world) with a concrete mechanism
  rather than a catalogue of cases, so it beat the Lilliputian, Charles-Bonnet and
  collective-hallucination angles on learnability.
- **#5 over #6/#7/#8** — the homelab alerting stack carries the broadest live discussion and
  the most concrete tool comparisons; the pure-protocol (#7) and fatigue (#8) angles are
  narrower, and UnifiedPush (#6) folds into #5 as one section.
- **#9 folds in #10/#11/#12** — detector reliability, humanizers and watermarking are the
  same 2026 arms race; running them as one topic avoids three near-identical AI briefs and
  keeps the day to a single AI entry.

## Research-quality notes (worth recording)

- **Reddit's public search returned 403 on the neuroscience and self-hosting runs**, so the
  Reddit counts in those two footers are listing-discovery noise, not on-topic threads —
  visible in the off-topic top-communities lines (e.g. r/SubspacePhysics, r/HomeServer).
  The substantive evidence came from documentation, published models and one or two
  high-signal threads per topic.
- **The form-constants topic had essentially no live 30-day layer** — the only on-topic
  explainers sat at 10–21 views and the X/Hacker News "form" matches were unrelated
  (soft-body form controls, an SEC Form D, a calculus operator). The brief leans on
  evergreen neuroscience plus a February 2026 preprint and says so in its own body rather
  than dressing the thin layer up as consensus.
- **Privacy substitution:** where the engine's top public source for a topic happened to
  coincide with a privately saved link, the brief was pointed at an equivalent public
  source instead, so no saved URL appears in any committed artifact.

## Supply note

The pool read **empty at the start of the run**: the fuel check measured the local `self`
clone before the sync step pulled it, and the clone was several commits behind, so the
circuit-breaker saw zero eligible entries. Fetching brought the pool to six; the re-run
passed. This is the known stale-cache ordering issue — the breaker reads the cache without
syncing it first. After retiring today's three source ids, **three entries remain (~1 day of
runway)** until new links are captured.
