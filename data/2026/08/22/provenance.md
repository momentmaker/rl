# Provenance — 2026-08-22

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel

The circuit-breaker failed on the first read - `eligible_pool: 1`, exit 2 - and this was
again the stale-cache false negative rather than genuine exhaustion. A `git fetch` showed
the local clone one commit behind the remote, with HEAD at the 2026-08-20 echo against a
remote tip of 2026-08-21. Pulling brought the pool to three and the breaker passed on
re-run. Measured runway after collection: one day. Worth noting the breaker has now
produced the same false negative on consecutive days; it reads the working tree before the
collector is the step that updates it.

## Source entries (3 picked from a pool of 3)

The pool was exactly three, so the pick had no degrees of freedom - all three were used.
Domain spread was good by luck rather than selection: one on public live cameras and a
text-free platform, one on the destruction of physical books for model training, one on an
essay arguing that measured intelligence does not translate into wellbeing. Capture notes
were short across all three, so the usual heaviest weighting had nothing to separate.

## The 12 adjacent topics

From the live-camera directory:
1. What it costs to keep a camera streaming continuously
2. Ambient and slow-TV streams as background company
3. Text-free and image-only social platforms
4. **Japan's visitor numbers and the rules arriving to manage them** → picked

From the book-destruction piece:
5. **Destructive scanning and the race to digitise physical books** → picked
6. The AI book copyright settlement and what it set as precedent
7. Shadow libraries and their legal standing
8. Orphan works and books that exist in a single copy

From the intelligence essay:
9. Wisdom against intelligence on poorly defined problems
10. Why AI benchmarks fail on open-ended tasks
11. Population test-score trends and what replicates
12. **What a category measures when its criteria keep widening** → picked

The automated near-dup guard flagged none of the twelve; top score across the set was
0.12, and the nearest matches were lexical collisions rather than subject revisits.
Judgment dropped **#10** anyway - it overlaps a published brief on what actually moves a
coding agent's benchmark score. Per the standing lesson that the guard misses revisits,
`related()` was run at this step rather than at provenance time; it returned nothing above
threshold for any candidate.

## Narrowing to three, and re-picking twice

This is the part worth recording, because the first narrowing was wrong.

The initial three were #5, #1 and a poorly-defined-problems topic from group three. Only
#5 survived contact with the research. #1 failed across three engine runs and its
group-two substitute failed on a fourth: the corpus for continuous camera streaming was
evergreen tutorials from 2019-2024 plus a Reddit layer of general Twitch-streamer
questions, and the ambient-streams attempt returned a top cluster score of 1 with music-
news noise. The intelligence topic failed for a different and more instructive reason -
the saved essay dates from 2022, so there was no 30-day discussion layer to find at all.

The pattern across all six failed runs was identical: every ranked cluster carried an
entity-miss demotion, and the topics that failed were concepts while the one that worked
named an organisation. The two replacement topics were therefore chosen to be anchored on
named entities with live coverage, and both landed on the first run. That is the
transferable lesson from today - the ranker needs a proper noun, and "is this a concept or
an entity?" belongs in the step-5 narrowing criteria alongside curiosity and freshness.

Both replacements were re-checked against the near-dup guard before use (0.088 and 0.045)
and both were clear.

## Research notes

Nine engine runs for three briefs. Two failure modes are worth carrying forward.

First, a topic string containing `24/7` was parsed as a comparison between "24" and "7"
and fanned out into a two-entity run, returning cartoon episodes and unrelated surveillance
news. This is the same class as the known problem with the word "versus" in a topic string;
the slash triggers it too. Strip slashes from step-5 seeds.

Second, healthy footer counts again concealed an off-topic Reddit layer - one run reported
33 threads and 52,877 upvotes while the actual threads were about stream viewer counts and
anonymity. Reddit's public search endpoint returned 403 throughout, so Reddit came in via
subreddit front-page discovery, which is topic-blind. Choosing the right community matters
more than the count: retargeting from a streaming subreddit to self-hosting subreddits
changed the corpus completely while leaving the totals similar.

All three briefs carry an explicit note on the state of their own corpus. The Japan brief
in particular rests on news reporting and published government targets rather than on any
discussion layer, and says so. The books brief flags that its Polymarket line is six tennis
markets matched on a first name and nothing else.

Hard numbers in every brief were verified against a primary or near-primary source - a
registry study's own university release and its PubMed record, a national newspaper of
record for visitor statistics, a wire report for the regulatory letter - rather than taken
from the engine's ranking, which was doing little useful work on any of the three.
