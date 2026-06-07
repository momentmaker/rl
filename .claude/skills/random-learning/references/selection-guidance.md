# Selection guidance

This is a **personal** learning ritual. Optimize every choice for *your own*
curiosity first; "others would find it interesting too" is a tiebreaker, not the
target.

## Pick 3 entries (from the collected `self` entries)

Weight, in order:

1. **The `why?` note — heaviest.** It's your own stated reason for saving the
   link. An entry whose `why?` shows genuine pull ("i keep getting confused
   by…", "i like these kinds of things…") beats a link saved on a whim.
2. **Tags + topical variety.** Don't pick 3 entries from the same tag cluster on
   the same day. Spread across domains so the day feels like a range, not a rut.
3. **Freshness of interest.** A recently captured entry usually reflects a live
   curiosity; very old untouched entries are fine too, but prefer signal over
   age alone.

Avoid picking three near-identical entries — the funnel below needs room to
diverge.

## Fan to exactly 12 adjacent topics

From the 3 entries, generate 12 topics that are *adjacent* — related or one hop
away — not restatements of the source links. Good adjacency:

- A neighboring concept ("Conway's Law" → "team topologies", "inverse Conway
  maneuver").
- A practical angle ("async in Rust" → "structured concurrency", "what people
  get wrong about `Pin`").
- A cross-domain echo ("aphorisms for complex ideas" → "mental models people
  actually use", "the map vs the territory").

Run each through the near-dup guard and drop anything already published (or, on
a tiny index, anything your judgment says is a repeat). The 12 should feel like
a genuinely interesting menu — things *you'd* want to read about.

## Narrow to the top 3

Choose for: **curiosity** (do you actually want to learn this today?),
**freshness** (is there live discussion in the last 30 days?), and
**learnability** (can a `last30days` brief teach you something concrete, not
just vibes?). Prefer 3 that don't overlap.

## Write 3 seed sentences (the `last30days` queries)

Each seed is one sentence framing the topic the way **people discuss it**, not
the way a tutorial titles it. `last30days` searches social + web; keyword-trap
phrasing returns noise.

- Bad (keyword trap): "how to use Docker", "what is RAG", "best practices for X".
- Good (discussion-shaped): "Docker production setups people actually run in
  2026", "where RAG falls short and what people switched to", "what teams say
  about X after living with it".

Name the entity and the angle. A good seed reads like something a knowledgeable
person would post, which is exactly the corpus `last30days` mines.
