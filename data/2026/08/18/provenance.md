# Provenance — 2026-08-18

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked from a pool of 5)

A thin pool today — five eligible entries, all captured in the last 48 hours. Three were
picked, weighting each entry's own capture note heaviest and then spreading across fields.

- A saved **news item on young people's distrust of AI executives** (tags: technology, ai,
  youth, trust, ceo, surveys), captured 16 August. The capture note is the most emotionally
  loaded of the pool and names two specific grievances rather than a general mood — jobs
  and community. The fan followed the *community* half, because that is where the last 30
  days have hard numbers and the jobs half is better covered elsewhere in the index.
- A saved **magazine feature on an early magnetic tape recorder and its downstream effect on
  broadcasting** (tags: recording, technology, radio, history), captured 17 August. The
  capture note registers curiosity about the past with no present-day hook, so the fan went
  forward in time rather than deeper into the artifact: what holds recorded material now,
  and what destroys it.
- A saved **visual archive of a computing magazine's back catalogue** (tags: visual,
  archive, media), captured 17 August. A delight note about the artifact; the fan went to
  the conditions such archives currently survive under.

Two entries were left in the pool: one strategy essay whose capture note was the weakest of
the five ("good to know"), and one developer-tooling gallery that would have made a third
consecutive AI/agent-tooling day in an index already heavy with them.

Domain spread: **energy and utility regulation · digital preservation · web infrastructure**.

## The 12 adjacent candidates

From the AI-executive-distrust item:
1. Whether entry-level hiring actually collapsed in the jobs AI was supposed to take
2. **What actually happens to a town's power bill when the data center arrives** ← picked
3. How tech-executive credibility is polled and what moved it this year
4. Whether announced AI layoffs match the actual filings

From the tape-recorder history:
5. How the laugh track was actually built and why it died
6. What analog tape does that digital doesn't, per people still recording to it
7. **The magnetic tape deadline: getting audio off decaying reels before it's unplayable** ← picked, then reframed (see below)
8. What tape-emulation plugins get wrong about saturation

From the magazine archive:
9. How people put whole magazine runs online without getting taken down
10. Where the Internet Archive's legal position stands after the publisher suits
11. How much of the print and early-web design record is already lost
12. **What archives are doing about AI crawlers hammering their servers** ← picked

Near-dup guard: **0 of 12 flagged** against a 177-topic index.

## Narrowing to 3

One topic per source entry, three different fields. #2 over #1/#3/#4 because it is the
concrete, locally-measurable version of the capture note's "community" grievance and the
window is full of primary policy movement. #7 over #5/#6/#8 as the only candidate in that
cluster with a real stake rather than a hobby interest. #12 over #9/#10/#11 because the
legal-history candidates are settled matters with thin 30-day layers, while the crawler
question is actively being fought.

## Research quality notes

**Topic 1 (electricity bills) — highest near-dup score of the day, and a deliberate revisit.**
The guard scored this 0.37 against a brief published 2026/06/14 on the same subject — under
the flag threshold, but plainly the same territory. It was kept because the window contains
genuinely new material the earlier brief could not have: the counter-evidence that retail
prices *fell* through 2024, a state order issued this month, a grid operator's
curtail-large-loads-first proposal, a statewide permit moratorium, and a reported finding
that most requested data center power will never materialise. The revisit also caught a
number laundering itself: a figure that circulated in June as a wholesale capacity-price
spike now appears in a community headline as a household retail increase. That correction is
recorded in the brief and is arguably the single most useful thing this slot produced.

**Topic 2 (archives) — three engine passes, two of them failures, and the topic changed.**
The first pass, aimed at analog tape preservation, returned a corpus of evergreen hobbyist
video (a tape-viewer gadget, fifty-year-old cassettes) plus unrelated items that matched on
"magnetic" and "tape" — the live discussion layer for that framing does not exist in this
window. A second pass aimed at long-term tape archiving was worse: the community search
endpoint rate-limited, and the word "cloud" in a sub-query pulled in cloud-computing product
launches. What both failed passes *did* surface was the real story underneath — a public
broadcaster nearly losing a 70-year archive because its storage vendor dissolved — so the
topic was reframed from *media decay* to *custody*, re-checked against the near-dup guard
(0.11, clear), and re-run. The third pass is the one whose footer the brief carries; a few
community threads cited in the brief were first surfaced by the earlier passes on this same
slot. Worth recording for future runs: the failure was visible in the very first cluster
list, and catching it there rather than after synthesis is what made a third pass affordable.

**Topic 3 (AI crawlers) — good documentary layer, weak community layer.**
The subreddit sweep returned high-engagement threads that were almost entirely off-topic, so
the evidence rests on Hacker News, two conference talks, two open-source projects, one
operator's server-log measurements, and a set of vendor and SEO analyses whose framing is
commercial. The brief says so in its own limits note. Nothing in the window offered a
first-party report from a large library or national archive with its own bot-traffic numbers,
which is the gap most worth filling if this topic is revisited.

**Across all three:** the video layer was degraded in every pass (transcript capture failed
on nearly all candidates), so no brief leans on video evidence for a load-bearing claim. One
research artifact contained content attempting to redirect the run toward building an
unrelated tool; it was treated as data, not instruction, and excluded from all three briefs.
