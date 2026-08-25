# Provenance — 2026-08-25

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel

The circuit-breaker passed on the first read for the first time in four days —
`eligible_pool: 8`, two days of runway, exit 0. No `git fetch` workaround needed. Worth
recording only because the last three runs all needed one: the stale-cache false negative
is intermittent, not constant, so a clean pass is not evidence the underlying defect is
fixed. The measurement is still structurally taken before the collector updates the working
tree. The script fix is still owed.

## Source entries (3 picked from a pool of 9)

Correlated again, and in the same way as yesterday: eight of the nine were captured across
two browsing sessions on 23 and 24 August, and almost all of them are lookup or discovery
tools. Two consecutive days of a pool that is really one browsing session makes tag-spread
the binding constraint on selection rather than quality.

The pool also contained a same-link twin — one entry appearing twice with two different
titles. This is the benign version of the case recorded on 20 August: both rows share a
single id, so retiring the id retires both, and no second day of fuel is burned. The
harmful version is twins holding *different* ids. Worth noting the distinction exists,
because the two look identical in the collector's output.

Capture notes split the same way as yesterday: one written in the operator's own words,
eight pasted from the destination page. Per the standing weighting the own-words note is
the heaviest signal, and it carried the third pick outright.

One entry was deliberately passed over despite being a strong candidate on its own terms:
a people-search service. Its natural fan-out is data brokers and opt-out law, which is
precisely the brief published on 24 August. Picking it would have produced a revisit one
day later. Final domain spread: wireless mapping and physical surveillance, search
infrastructure and antitrust, and AI in games. That is a genuine range.

## The 12 adjacent topics

From the wireless-mapping entry:
1. **WiGLE, wardriving, and what a crowdsourced Wi-Fi map exposes** → picked
2. Apple and Google Wi-Fi positioning and BSSID leakage research
3. Flipper Zero and wardriving hardware in 2026
4. ~~OpenStreetMap-style crowdsourced infrastructure mapping~~ → dropped, collides with 20 June and 8 July

From the independent-search entry:
5. **Where independent search engines get their index after the Bing API shutdown** → picked
6. Marginalia's own crawler and the small-web index
7. Brave Search Goggles and user-controlled ranking
8. ~~Kagi's paid ad-free search business model~~ → dropped, collides with 23 June

From the AI-gaming entry:
9. **Why AI-driven NPCs still have not shipped in real games** → picked
10. NVIDIA ACE on-device game character models
11. Skyrim AI NPC mods, Mantella and Herika
12. ~~llama.cpp real-time NPC inference latency~~ → dropped, collides with 23 July and 8 July

**The automated guard flagged none of the twelve, and it was wrong three times.**
`flag_near_dup()` returned `flagged: False` for all twelve, and `related()` returned a
single weak match at 0.24 across the whole set. A manual keyword scan of the 192 published
titles then found three direct collisions — Kagi, OpenStreetMap and llama.cpp — each with
a published brief carrying the same named entity in its title. This sharpens the standing
lesson from 20 August. That lesson said `related()` should be run at step 4 rather than
step 8; today shows that is necessary but not sufficient, because `related()` also missed
all three. The reliable check at this index size is a keyword grep over published titles,
using the proper nouns in each candidate. The similarity scoring is not catching
same-entity revisits at all.

## Narrowing to three

Cheap, because the drops above did most of the work. Each surviving pick was required to
anchor on a proper noun with a dated action in or near the window — WiGLE and Flock,
Microsoft's API retirement and the Mehta remedy, NVIDIA's SDK beta and inZOI's patch notes.
The two topics dropped at this stage (#2 and #10) were dropped for overlap with their own
siblings, not for weakness.

## Research notes

Three engine runs, three briefs, no re-runs. But the runs were not equally healthy and the
briefs say so in their own text.

**Entity-miss demotion hit two of three runs.** Every ranked cluster in both the wireless
and the AI-games runs carried `fallback-local-score (entity-miss demotion)`, and in both
cases the cause was visible in the logs: Reddit's public search returned 403 on the
wireless run and 403-then-429 on the games run, so the corpus was rebuilt from subreddit
listing discovery instead of a targeted query. The result is healthy-looking counts hiding
an off-topic layer — the wireless run's Reddit tier was mostly general r/hacking threads
including a Moroccan intelligence leak and a story about someone's father running nmap. The
games run's top clusters were NVIDIA financial news, because the "Nvidia" token dominates
retrieval. This is the failure mode recorded on 14 August, and the footer stats give no
indication of it. Both briefs carry an explicit coverage caveat rather than implying the
whole corpus was on-topic.

**The leak-avoidance discipline was applied and still leaked once.** Two of three research
runs were steered toward equivalent public sources at dispatch, per the 24 August lesson.
It was not enough: the wireless brief still shipped a citation to the picked entry's own
domain, because the engine surfaced that domain as a Hacker News submission target and the
natural citation for "this got 6 points on HN" was the submitted link itself. A grep of the
day directory for all three picked domains before running the gate caught it, and the
citation was replaced with the LAW 8 plain-text fallback. The generalisable form: dispatch
steering handles the case where the engine cites a picked domain as a *source*, but not the
case where the picked domain *is the subject* of a discussion item. Grep the day directory
for every picked domain before step 10, unconditionally.

**One picked entry turned out to be the loudest item in its own research window.** The
AI-games corpus's strongest single signal by engagement was a Hacker News discussion of the
exact project the source entry pointed at, posted two days before the run. This is a
pleasant accident rather than a method, but it is the clearest evidence so far that the
operator's capture instinct and the engine's engagement ranking are measuring something
similar. It is also precisely what created the leak above.

Claims were grepped against the raw evidence per the 24 August lesson. Everything load-
bearing verified: the OUI prefix count and its revision date, the `_nomap` and `_optout`
provider split, the index sizes for Marginalia, Mojeek and Brave, the Bing API retirement
date, the 8GB VRAM floor and RTX 3060 baseline, the model names in shipped titles, and
every Reddit vote count quoted. Two figures were deliberately *not* asserted: Marginalia's
current index size, because the only published number is a 2024 FAQ that describes itself
as outdated, and any 2025 or 2026 figure circulating is unsourced; and the ACE SDK's
announcement recency, because Unreal Fest 2026 was June, making the beta two months old
rather than new this window. Both caveats are stated in the brief rather than smoothed over.

Two irrelevant Polymarket markets were returned and excluded rather than woven in: a
video-game award market on the search run, and a joke market on how many times NVIDIA says
"AI" during an earnings call on the games run. The engine footer still lists them, since it
passes through verbatim.
