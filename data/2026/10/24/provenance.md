# Provenance — 2026-10-24

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel — the first shipped run since 23 September

The morning before this one, the library clone was **5 commits behind** `origin/master`, so the
pre-pull fuel reading (`eligible_pool: 2`, exit 2) was treated as carrying no information. The
filename diff showed one genuine dated capture (from 17 October) alongside a weekly digest and
two housekeeping files. After the pull, `fuel.py` returned `eligible_pool: 3`, exit 0,
`span_days: 28`, `capture_rate_per_day: 0.11` — exactly at the `--min-pool 3` floor.

Two different things kept this routine silent for a month. From 24 September to 17 October the
pool sat at one or two eligible entries against a floor of three, and each morning skipped
cleanly at step 1. From 18 to 23 October the scheduled runs never reached step 1 at all: each
died at startup on an expired authentication session. The capture that cleared the floor
landed on 17 October, so the first morning that could have shipped was the 18th, and the
outage cost six days of it. Retiring three entries today empties the pool to zero.

## Source entries — pool of exactly 3, so step 3 had no choice to make

Three distinct ids, no same-link twins, all three picked. The selection guidance's variety
rule was satisfied by accident rather than design: the entries span game AI, generative music
in the browser, and consumer health testing. Ranked by capture note: a short note expressing
interest in a frontier model playing a real-time strategy game; a note about reusing a
browser-music idea inside one of the operator's own projects; and a note framing consumer lab
testing plus AI as where preventive care is heading.

## The 12 adjacent topics

From entry A (a benchmark of frontier models playing a classic RTS):

1. SSCAIT and the StarCraft bot ladder, and what scripted bots still do that LLMs can't — **picked** (researched as the Brood War bot scene)
2. Claude Plays Pokémon and what game-playing LLM streams actually show
3. Factorio Learning Environment and LLM agents in real-time games
4. BALROG and the case for game benchmarks of agent reasoning

From entry B (a browser page that generates ambient music live with Web Audio):

5. Strudel live coding and making music in the browser — **picked**
6. Tone.js and procedural music with the Web Audio API
7. Endel and functional music for focus, what the evidence says
8. The Pomodoro Technique and what people keep after trying it

From entry C (a consumer blood-testing membership):

9. Direct-to-consumer blood-testing memberships and what doctors say about overtesting — **picked**
10. Prenuvo whole-body MRI and the incidental-findings problem — **dropped, revisit**
11. Continuous glucose monitors for people without diabetes
12. ApoB testing and why preventive cardiology people want it

All twelve came back `flagged: false` from the near-dup guard with empty `related()` lists.
The keyword grep over published titles and brief bodies — the control that actually works at
this index size — caught one collision the guards missed: candidate 10 is the subject of
*Full-body AI health scanners and longevity screening* (2026/06/22), whose brief names Prenuvo
ten times. It was dropped, and the blood-testing research was explicitly scoped away from
imaging. That earlier brief is linked as a connection instead.

## Narrowing

One topic per entry, for range. Each carries a proper noun for the engine to match on
(StarCraft, Strudel, Function Health), and each engine topic string was kept title-shaped
and free of ` vs ` and slashes. Candidate 1 was preferred over the Pokémon and Factorio
options because "Pokémon" would have pulled fandom content and because the bot scene is the
yardstick the source benchmark measures against. Strudel was preferred over Tone.js because
it has a live community and because the embedding question is directly what the capture note
was about. The blood-testing topic was preferred over ApoB because it stays closest to what
the entry actually was — a membership model with an AI interpretation layer.

## Research notes

- **Brood War:** one engine run. Thin and lopsided: 12 of 14 Hacker News stories matched on
  "LLM" generically, and a single X post carries 1,684 of 1,953 likes. The tournament result,
  the benchmark tiers and the download incident came from X, the Show HN item, and appended
  web supplements. The source entry's own report URL was kept out of the brief by instruction
  at dispatch.
- **Strudel:** one engine run. Twelve of sixteen Reddit threads were the r/synthesizers
  front page; the four on-topic threads hold all 47 upvotes. The project FAQ, the REPL manual,
  npm download counts and an NPR piece, all appended to the raw file, carried most of the brief.
- **Blood testing:** two engine runs (the one permitted re-query, because the first pass's
  Reddit layer was blocked by a 403). Hacker News was entirely name collisions on "function"
  and "superpower". The footer shown is the second run's, because the first run's web line
  listed the source entry's own domain. Two figures rest on search summaries rather than
  fetched pages and are marked as weaker in the raw file.
- Every number and quote in the three briefs was grepped case-insensitively against its raw
  file. Pronouns for two first-person reviewers were neutralised because the evidence did not
  state them.

## Safety

Nothing in any of the three corpora attempted to redirect the routine. One X item in the
blood-testing corpus is a long chatbot instruction template that a member wrote for their own
health questions; it was read as evidence of members exporting results to general chatbots,
and not acted on.

No leak remains: the day directory was grepped for all three picked domains and for every
capture note's distinctive phrasing before the gate ran.
