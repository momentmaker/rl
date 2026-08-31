# Provenance — 2026-08-31

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel — the stale-cache defect finally fired

`fuel.py` before the pull: `eligible_pool: 2`, **exit 2**. After `collect.py` pulled:
`eligible_pool: 3`, exit 0.

This is the fourth day running that the circuit breaker has measured a stale working tree,
and the first time it has actually returned a **non-zero exit** — a live low-fuel abort
signal against a library that had enough fuel. On 27 August the failure was latent: the
number was wrong but still landed on the threshold. Today the routine would have skipped
the day outright had it been followed literally.

The 27 August note already diagnosed this correctly and the fix is still owed: `git fetch`
updates remote refs, `fuel.py` reads the working tree, so fetching first tells you the
clone is behind without changing the number the breaker acts on. The only reason today
produced three briefs is that the operator overrode a red gate on the strength of the
`[behind 4]` from the fetch. That is not a workaround, it is a human patching a broken
sensor, and it will not survive the routine running unattended at 07:17. **`fuel.py` must
pull, or read the fetched ref, before it counts.**

## Source entries — the pool number was inflated, exactly as predicted

The pool reported three rows and contained **two distinct ids**. One id exists twice on
disk as a same-link twin, and `collect.py` emits one record per file while the breaker
counts records. This is the precise scenario written down on 28 August as a hypothetical:
a pool of twins passing `--min-pool 3` and stranding step 3 with fewer usable sources than
the gate promised. It is no longer hypothetical. Dedupe by id before judging whether a
pool is real.

So today's three topics were fanned from **two** sources, not three. Retiring the two ids
clears all three rows, so no fuel is lost to the twin.

Capture notes split one-and-one: one written in the operator's own words, one pasted
verbatim from the destination page. Per the standing weighting, the own-words entry
carried its pick outright and was given two of the three slots.

**The people-search entry was picked after three consecutive days of being passed over.**
The 27 August note recommended either picking it with a deliberately different fan-out or
retiring it outright, on the grounds that three declines had stopped being a daily
judgment call and become a standing state. It was picked, and the fan-out was deliberately
steered off its natural target: the obvious adjacency is data brokers and deletion law,
which is the 24 August brief, so the entry was fanned to the **engineering layer**
underneath instead — how probabilistic record linkage actually decides two rows are the
same person. Same source, different layer, on the record.

That choice also protected the day from a rut. The index already carries six
privacy-and-data-governance briefs in the preceding two weeks; a seventh would have been
the least interesting available use of the slot.

## The 12 adjacent topics

From the people-search entry:
1. **Record linkage with Splink and how identities get matched across messy databases** → picked
2. Credit header data and how it feeds free people-search sites
3. State address confidentiality programmes and what they actually shield
4. Voter file data as the public feedstock for people lookups
5. Skip tracing and how process servers actually locate people
6. Reverse phone lookup accuracy and the CNAM database behind it

From the video-editor entry:
7. **Kdenlive and what editors say after finishing real projects on it** → picked
8. **FFmpeg hardware AV1 encoding on NVENC and what it costs in quality** → picked
9. Proxy workflows and why open-source video editors stall on long timelines
10. DaVinci Resolve on Linux and the codec licensing wall
11. SVT-AV1 encoding and whether anyone actually ships AV1 exports
12. Qt6 migration and what it broke in long-lived desktop apps

`flag_near_dup()` returned clean on all twelve; the highest score anywhere in the fan was
**0.14**, on the 24 August data-broker brief against the people-search cluster — low
enough to confirm the layer-shift worked. `related()` returned an empty list for all three
final titles. That is the **fourth consecutive day** of zero matches across 201 published
topics, which continues to read as a scoring function that does not work at this index
size rather than as evidence of genuine novelty.

## Narrowing, and two failures designed out before they could happen

Each pick had to carry a **proper noun** — the entity-miss constraint is now the fourth
narrowing criterion alongside curiosity, freshness and learnability. Candidates 9 and 11
were dropped for being concept-shaped despite being interesting.

**Leak pre-empted at step 5, again.** Both picked URLs were handed to each researcher as
explicit exclusions before any engine call. The video topics were the live risk, because
threads comparing free editors routinely link the picked repository; the researcher was
told it could name the product but not cite the URL. It did exactly that — the product
appears once, inside a quotation, with no link. Neither picked domain appears anywhere in
the day's artifacts.

**A new failure mode found by reading the gate rather than by tripping it.** The video
entry's capture note is a six-word phrase whose middle five words are an entirely natural
thing to write about open-source video software. The gate's `_shingle_leak` tokenizes the
note with `[a-z0-9]+`, which drops hyphens, but normalizes the artifact text without
dropping them — so the note's shingle only matches a brief that writes the phrase
**unhyphenated**. A brief writing it the ordinary way would have failed the privacy check
on a phrase carrying no private information whatsoever. Both video briefs were grepped for
the unhyphenated form before the gate ran. Clean, but by luck rather than design.

This is worth generalising: the privacy check treats a capture note as a secret, but a
note pasted from a destination page — or a note made of generic words — is not one. The
check cannot tell the difference, so short generic notes are a standing false-positive
risk that grows with how well the brief matches its own subject.

## Research notes

Three engine runs, three briefs, one re-query. All three carry the badge and a full stats
footer, and all three wrote raw evidence to disk.

**Entity-miss demotion on all three runs — 3 for 3.** This is no longer an occasional
artifact; it is the default outcome. Every ranked cluster on every run carried
`fallback-local-score (entity-miss demotion)`, including runs whose topic strings were
short, title-shaped and anchored on a strong proper noun, which is exactly what the
standing guidance says to do. The guidance is necessary and evidently not sufficient. On
the record-linkage run, 24 Reddit threads carrying 1,426 upvotes contained **zero**
on-topic items; the video run pulled a football thread about a team called Reading into
its corpus.

**Salvage carried all three briefs.** In every case the engine's ranked layer was junk and
the usable evidence was underneath it: the repository discussion tab in one case, the web
and X layer plus a direct `.rss` fetch in another after Reddit's public search returned
403 and 429. Only one run spent its single permitted re-query, anchoring on a named
release, which recovered a Reddit layer. Salvage beat re-querying two times out of three.

**The verification pass was the most valuable step of the day and it should be standing
practice.** The record-linkage brief's numbers were all traceable, but none of its
quotations were: the researcher had read the threads live and never persisted them, so
34 quoted spans had nothing greppable behind them. Sending it back to persist the bodies
and re-check found **six real defects** — a typo silently corrected inside quotation
marks, an altered capital mid-quote, a changed word, two separate bullets spliced into one
continuous quotation, and a punctuation substitution. The sixth is the one that matters:
a licensing claim was presented as settled fact when the only reply on the issue disputes
it outright. The brief now carries the dissent and the takeaway no longer asserts the
contested reading. **A quote that cannot be grepped is a quote that has not been checked.**

**One arithmetic contradiction caught in review.** The encoding brief's body and its ninth
takeaway gave different gaps for the same release rebase, three days against eleven; the
body was right, the takeaway had silently measured to a different upstream release.
Corrected. Twelve other unsourced claims were cut by the researchers before drafting.

**One footer is not fully representative of its brief.** The video-editor brief reports
the second run's footer, while several cited X handles come from the first run's corpus.
The footer is real engine output and nothing in it is invented, but its top-voices line
does not name everyone the brief quotes. Noted here rather than silently passed through.

Nothing in any of the three corpora attempted to redirect the routine. One repository
issue in an earlier run was written as a task handoff addressed to an automated assistant;
today's corpora contained no equivalent. All research content was read as data.

No leak remains: the day directory was grepped for both picked URLs, for the capture-note
shingles in both hyphenated and unhyphenated form, and for the injection patterns, before
the gate ran.
