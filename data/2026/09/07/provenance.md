# Provenance — 2026-09-07

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel — the rule was followed, and the staleness carried real fuel this time

No pre-pull fuel number was taken. Per the standing rule, a count measured against an
unpulled clone carries no information whatever its value, so the sequence was reordered:
fetch, inspect, `collect.py` (which pulls), *then* `fuel.py`.

The fetch showed the clone **4 commits behind** `origin/master`. The filename diff — the
cheap pre-pull tell for whether staleness is fuel or noise — showed one genuine capture
alongside a weekly digest, a sparks file and a backup blob. Unlike 2 September, where every
new path was an `-echo.md` and the skip was real, today's gap contained an actual entry.

Post-pull: `eligible_pool: 3`, exit 0, `span_days: 4`, `days_runway: 1`. Landing exactly on
the `--min-pool 3` floor is the same razor-thin margin as 27 August. Two commits thinner and
this would have aborted against a library that had enough.

The durable fix is still owed and is now overdue by several weeks: `fuel.py` should take
`--remote` and call `sync_self()`, or the skill should put collect before the breaker.
Every run since has depended on an operator or an agent knowing to ignore the sensor.

## Source entries — pool of 3, three distinct ids, so step 3 made no choice

The three rows resolved to **three distinct ids** — no same-link twins today, so the
inflated-pool defect did not fire. But with exactly three eligible entries and a quota of
three, selection was arithmetic rather than judgment. `references/selection-guidance.md`
weights the capture note heaviest and asks for topical variety across picks; neither lever
had anything to move. Worth noting for the record that on a floor-margin day the selection
guidance is inert, and all of the day's real curation happens at steps 4 and 5.

The capture notes themselves were unusually thin — three short reactions to tools and
projects rather than the "i keep getting confused by…" shape the guidance says should carry
a pick outright. With no strong signal in the notes, the fan-out was steered by domain
variety and learnability instead: one hardware/radio topic, one archives/history topic, one
software/attention topic, deliberately spread so the day reads as a range.

## The 12 adjacent topics

From entry A (a communications art project):

1. Meshtastic off-grid mesh networks at large events — **picked**
2. Futel free payphone network
3. Asterisk and FreePBX self-hosted phone systems
4. Starlink at remote festivals and desert events
5. SIP trunking providers for hobbyist VoIP

From entry B (a population-scale data toy):

6. Our World in Data historical population estimates
7. HYDE gridded historical population dataset
8. Observable Plot for interactive data stories
9. FamilySearch mass digitization of historical records — **picked**

From entry C (a document-to-audio tool):

10. Kokoro TTS open-weight speech models — **dropped, revisit**
11. Marker and MinerU PDF-to-markdown extraction for papers — **dropped, revisit**
12. Audiobookshelf self-hosted audiobook server

Replacements drawn after the two drops, both guard-clean: *FamilySearch mass digitization*
(which then took the slot) and *Readwise Reader and read-it-later apps after Pocket*, the
third pick.

## The near-dup guard missed two revisits in one fan-out

`flag_near_dup` returned `flagged: false` on all twelve. Two of them were repeats anyway,
and both were caught only by the manual `related()`-plus-grep pass at step 4 rather than by
the guard:

- **Kokoro TTS** scored **0.186** against `open-source-tts-2026` (2026/06/20) — the highest
  similarity in the whole fan-out, still under threshold. A grep of `data/` for TTS terms
  found not one prior brief but four: 06/20 (open-source TTS), 07/18 (real-time voice
  agents), 08/02 (audio tokenizers and speech models), 08/03 (full-duplex voice agents).
  The speech cluster is saturated; the guard reported it as clean.
- **Marker and MinerU** scored **0.0865** against `agents-reading-binary-files` (2026/07/27).
  Reading that brief settled it — it already covers ParseBench, LlamaParse, pdf-mcp,
  MarkItDown and per-page routing. A document-parsing brief today would have been a second
  pass over the same ground.

This is the third recorded instance of the guard clearing a same-subject repeat, and the
first where it cleared **two in one day**. The lesson holds and should be treated as
procedure rather than diligence: at step 4, grep `data/` for the candidate's proper nouns.
The score is not the check.

## Research — three runs, all thin, all with misleading footers

Engine resolved at the nested plugin path (`cache/last30days-skill/last30days/3.3.2/…`),
`--diagnose` confirming v3.3.2 with seven sources and X authenticated. All three runs used
agent mode with a hand-written `--plan` and Step 0.55 resolution (handles, subreddits,
repos). Topic strings were kept short and title-shaped; the discussion-shaped seeds were
used only for framing and for the `ranking_query` fields.

Reddit's public search returned **403 on every query across all three runs**, so all Reddit
evidence came from listing discovery, and every cluster in every run carried the
`entity-miss` demotion tag. The footers are correspondingly unreliable, in three different
ways, each documented in its own brief's evidence note:

- **Meshtastic**: nine of fifteen Reddit items are the r/preppers front page — a Costco
  run, flashlights, water storage, bunkers — carrying most of the 1,977 upvotes.
- **FamilySearch**: **7,022 of 7,162** Reddit upvotes come from a single
  r/BestofRedditorUpdates thread about a doctor's appointment. The Hacker News slot is two
  keyword traps stacked, "text" pulling an AI-watermarking cluster and "archive" pulling
  Anna's Archive and Archive.org.
- **Read-it-later**: the web slot is near-entirely vendor-authored listicles, one of which
  ranks its own product first.

Because all three corpora were thin, six sources were fetched directly to fill gaps, plus
one supplementary web search on FamilySearch's limitations. These are cited inline in the
briefs and are the origin of several of the strongest claims — notably the coverage
critique, the transcript-editing rationale, the wildcard rules, and the e-ink build's
details. The briefs are therefore engine corpus **plus** targeted supplementation, not
engine output alone.

`reddit.com` fetches were refused, so the r/meshtastic solar-deployment retrospective, the
r/Genealogy full-text thread and the r/ObsidianMD thread are cited only from their titles,
engagement counts and the snippets the engine itself captured. No claim is made about the
contents of any Reddit post body beyond what appears in the raw evidence file.

## Safety

Nothing in any of the three corpora attempted to redirect the routine. One X item describes
a red-team hardware tool commanded over radio; it was read as evidence about the topic, the
same as everything else, and is quoted as a fact about the field rather than acted on.

No leak remains: the day directory was grepped for all three picked URLs and for the
capture-note text in both hyphenated and unhyphenated form before the gate ran.
