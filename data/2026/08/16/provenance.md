# Provenance — 2026-08-16

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

The eligible pool was **exactly 3**, so there was no selection step today — all three
eligible entries were picked, and the pool is now empty. See the supply note at the bottom.

- A saved **open-source astrophotography planning app** that scores a night from 1 to 10
  by folding together weather, moonlight, hours of darkness and light pollution, models
  how much the moon brightens the sky at a given target, and finds nearby dark-sky sites
  with drive time and road distance (tags: astrophotography, weather-forecast, dark-sky,
  open-source, moon-phases, planning), captured 9 August. Pull: the only entry in today's
  pool carrying a substantive reason, and that note points at reusing the idea inside an
  existing personal project rather than at astronomy as a subject — which is why the fan
  went to the *data quality* layer underneath the app rather than to the app itself.
- A saved **write-up of one person's multi-agent working setup**: six agents on a single
  small cloud server, one of which reads the prior day's conversations and sends a morning
  report on what was accomplished and what needs attention, reached over chat and an open
  messaging protocol, and closing with an admission that standing it up took roughly 10x
  longer than simply doing the tasks by hand (tags: ai-agents, automation, productivity),
  captured 12 August. Brief, non-specific note; selected on domain grounds.
- A saved **browser tool that simulates sun shadows anywhere on Earth**, casting 3D
  shadows from buildings, trees and terrain for any date and time and generating shadow
  accumulation maps (tags: shadow, sun, simulation, solar-analysis, 3d, online-tool),
  captured 12 August. Brief, non-specific note; selected on domain grounds.

Domain spread: **satellite/night-sky data quality · agent operations · solar engineering
practice**. Three different fields, no shared tag cluster.

## The 12 adjacent candidates

From the astrophotography planning app:
1. **How light pollution actually gets measured and how stale the maps are** ← picked
2. Which weather models amateur astronomers trust for seeing and cloud forecasts
3. What happens when an app compresses everything into one 1-10 score
4. How dark-sky places get certified and whether the designation holds

From the multi-agent working setup:
5. **What people report after running a personal staff of agents on their own VPS** ← picked
6. Agent-to-agent messaging over open protocols instead of vendor SDKs
7. Why daily digest agents get ignored after week two
8. What it actually costs to keep long-running agents on a cheap VPS

From the sun-shadow simulator:
9. **What rooftop solar shading tools get wrong compared to an on-site survey** ← picked
10. Where the 3D building and terrain data in browser maps actually comes from
11. How solar access and right-to-light rules get enforced in planning disputes
12. Solar position algorithms and how much precision anyone actually needs

Near-dup guard: **0 of 12 flagged** against a 171-topic index. The two highest scores were
#8 at 0.152 (nearest: agent memory between sessions, 2026/07/26) and #10 at 0.147
(nearest: OpenStreetMap and Google Maps, 2026/06/20) — both well under threshold.

## Narrowing to 3

One topic per source entry, and three genuinely different fields. Two candidates were
dropped by judgment rather than by the guard:

- **#8** was cut as an unflagged overlap: the 2026/08/02 brief already worked the
  per-vCPU-hour pricing of agent runtimes in detail, and 2026/08/01 covered inference as
  cost of goods sold. #5 keeps the ops-and-breakage angle without re-running the price
  comparison.
- **#10** was cut because it shares a shape with #1 — both are "where does this geodata
  come from and how old is it." Keeping both would have made two of three briefs the same
  argument in different fields.

#11 and #12 lost on freshness and learnability respectively: planning law moves too slowly
for a 30-day window, and solar position math is settled to a precision nobody disputes.

## Research-quality notes (worth recording)

- **Topic 1 was re-run.** The first engine pass used a long, sentence-shaped topic string;
  the token "sky" pulled in streaming-TV adverts and unrelated video content, and the
  engine tagged every returned cluster with its own entity-miss demotion. A second pass on
  a tighter, title-shaped string returned a genuinely on-topic transcript layer. The
  discarded pass is in the run's evidence directory alongside the kept one.
- **All three topics had a thin or absent discussion layer**, and each brief says so in its
  own body rather than burying it. Reddit's public search endpoint returned 403 on every
  one of the three runs, so the Reddit counts in all three footers are listing-discovery
  noise rather than on-topic threads — visible in the top-communities lines, which include
  subreddits with no relation to any of the three subjects. The substantive evidence came
  from transcripts, documentation, published validation studies and incident write-ups.

## Supply note

The pool was **empty at the start of the run** and the circuit-breaker tripped: the local
`self` cache had not been pulled since 29 July, so the fuel check measured a stale clone
and reported zero eligible entries. Fetching showed the remote was 9 commits ahead. The
sync step, which runs *after* the fuel check in the current sequence, brought the pool to
exactly 3 and the check passed on a re-run.

Worth fixing: the circuit-breaker reads the cache without syncing it, so a stale clone
reads as low fuel and would have silently skipped the day. Runway after today is **0 days**
until new entries are captured.
