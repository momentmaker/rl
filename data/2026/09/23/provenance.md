# Provenance — 2026-09-23

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel — the first shipped run since 7 September, and the pull was what unblocked it

No pre-pull fuel number was taken. Per the standing rule, a count measured against an
unpulled clone carries no information whatever its value, so the sequence was reordered:
fetch, inspect the filename diff, `collect.py` (which pulls), *then* `fuel.py`.

The fetch showed the clone **6 commits behind** `origin/master`. The filename diff — the
cheap pre-pull tell — showed **two genuine captures** alongside an echo file and a sparks
update. That is the "ordinary dated capture filename" case rather than the all-`-echo.md`
case, and it predicted correctly.

Post-pull: `eligible_pool: 4`, exit 0, `span_days: 9`, `capture_rate_per_day: 0.44`. This
ends a long run of non-shipping mornings whose causes were split between a stranded pool
(two eligible entries against a `--min-pool 3` floor, unchanged for three days) and, before
that, an authentication outage that killed five launchd runs before they reached step 1.
Both captures landed on 22 September, which took the pool from 2 to 4 and cleared the floor
for the first time in a fortnight. Retiring three today leaves one entry behind.

Worth recording plainly because two earlier forecasts about capture timing were wrong in
the optimistic direction: this is one observation, not a trend. The trailing-window rates
are still low and nothing here licenses a prediction about the next capture.

## Source entries — pool of 4, so step 3 made a real choice for the first time in weeks

Four distinct ids, no same-link twins. `references/selection-guidance.md` weights the
capture note heaviest, then topical variety. Three of the four notes carried usable signal
and one was a bare description, so the note ranking was: a long, invested note about a
writer's engagement with a classical text; a short note naming a specific worry about
hidden marking in generated media; a brief note about a list of origin stories across
cultures; and, last, a one-line reaction to a model benchmark.

The benchmark entry was dropped rather than picked, for two reasons. Its note was the
thinnest of the four, and picking it would have put three of three picks inside the AI
orbit — the other two entries both touch machine-generated content — which is exactly the
rut the guidance warns against. It stays eligible for a later day, which also matters when
the pool is this tight. The three picks span mythology/culture, privacy/forensics and
philosophy/translation.

## The 12 adjacent topics

From entry A (a cross-cultural collection of origin stories):

1. Aarne-Thompson-Uther and how folklorists index a story
2. Joseph Campbell's monomyth and what scholars actually say about it — **picked**
3. Phylogenetic analysis of folktales and how old a story can be
4. The Database of Religious History and quantifying belief

From entry B (hidden identifying marks embedded in media):

5. Google SynthID and whether AI watermarks survive editing — **dropped, revisit**
6. C2PA Content Credentials and what actually strips them — **dropped, revisit**
7. Zero-width Unicode in LLM output and AI text detection tells — **dropped, revisit**
8. Machine Identification Code printer dots and what still prints them — **picked**

From entry C (a musician's aphoristic book about making things):

9. Brian Eno's Oblique Strategies and constraint cards in practice
10. Tao Te Ching translations and which one people recommend — **picked**
11. Wu wei and the flow-state claim in creative work
12. *The Creative Act* and what practitioners took from it

Replacements drawn after the three drops, all guard-clean: *Cinavia and forensic
watermarking in streaming video*, *AirTag stalking alerts and the unwanted-tracking
standard*, and *The EURion constellation and banknote detection in software*. None took a
slot; the printer-dots candidate was the strongest of the non-AI marking angles on both
liveness and learnability.

## Three revisits in one fan-out, none caught by the guard

`flag_near_dup` returned `flagged: false` on all twelve candidates and on all three
replacements. Three of the twelve were repeats anyway, and all three were caught only by
the manual grep of `data/` for candidate proper nouns:

- **SynthID** appears in three prior briefs (2026/08/17, 2026/07/11, 2026/06/30).
- **C2PA** appears in five files across four days, including two prior briefs.
- The **08/17 AI-detectors brief** turns out to cover the whole cluster in depth — text
  watermark removability, a clean-scan result meaning "no vendor watermark" rather than
  "human," and the removal-kit economy. A SynthID or C2PA brief today would have been a
  second pass over settled ground.

This is now the fourth recorded occasion of the guard clearing a same-subject repeat, and
the second where it cleared more than one in a single fan-out. The grep is the control; the
similarity score is not. Note the useful negative result too: *Aarne* appeared once in
`data/`, but in a **candidate list** from 2026/06/07 rather than a published brief, so it
was correctly treated as eligible. Distinguishing a prior candidate from a prior brief
matters — a naive grep hit count would have dropped it.

## Research — three runs, three differently broken corpora

Engine resolved at the nested plugin path (`cache/last30days-skill/last30days/3.3.2/…`),
`--diagnose` confirming v3.3.2 with seven sources, X authenticated and Brave as the web
backend. All three runs used a hand-written `--plan` with 4 subqueries and Step 0.55
resolution (handles, subreddits, hashtags, and one GitHub repo). Topic strings were kept
short and title-shaped; the discussion-shaped seeds were used for the `ranking_query`
fields only. Every cluster in every run carried the `entity-miss` demotion tag.

The footers are unreliable in three distinct ways, each documented in its own brief's
evidence note:

- **Campbell**: all 16 Reddit items are subreddit front pages with no Campbell content, so
  the 2,696 upvotes are someone else's conversation. X returned 3 posts totalling 7 likes.
  Both GitHub items are unrelated AI-agent repositories supplying all 515 comments.
- **Printer dots**: a single r/technology thread about licence-plate-camera employees
  supplies **43,871 of the 45,839** Reddit upvotes. All 13 Hacker News stories are keyword
  traps on "machine" and "printer" — zero on topic. The 22M YouTube views are dominated by
  a printer-ink pricing video at 10.6M and an unrelated hardware teardown at 3.9M.
- **Tao Te Ching**: all 12 Hacker News stories are about the mathematician **Terence Tao**.
  A pure name collision, and the cleanest single example of the keyword trap in any run to
  date. The engine itself warned that "top evidence is highly concentrated in one source."

Because all three corpora were thin, eight sources were fetched or searched directly to
fill gaps. These are cited inline in the briefs and are the origin of several of the
strongest claims — the named folklorist critiques and the Irish narrative forms, the
retirement status of the printer list and the decoder's commit history and open issues, and
the manuscript history plus the translator background. The briefs are therefore engine
corpus **plus** targeted supplementation, not engine output alone.

One factual check is worth recording: the printer-decoder's activity figures (last push
2024-09-15, five open issues, and their titles and dates) were taken from the GitHub API
directly rather than from the engine's project card, which reported only a star count and
an issue count.

`reddit.com` fetches were not attempted. The r/taoism edition-identification thread, the
r/Screenwriting structure-guru thread and the r/mythology belief thread are cited only from
their titles and engagement counts as captured in the raw evidence. No claim is made about
the contents of any Reddit post body.

## Safety

Nothing in any of the three corpora attempted to redirect the routine. One X item in the
printer-dots corpus is a memecoin promotion that matched on the word "printer," and several
others in the same slot are unrelated or offensive posts that matched on "yellow dots";
all were read as evidence about corpus quality, quoted only where relevant to that point,
and not acted on.

No leak remains: the day directory was grepped for all three picked URLs and for the
capture-note text in both hyphenated and unhyphenated form before the gate ran.
