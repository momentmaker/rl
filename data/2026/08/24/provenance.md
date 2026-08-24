# Provenance — 2026-08-24

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel

The circuit-breaker failed on the first read — `eligible_pool: 0`, exit 2 — and this was
the stale-cache false negative for the third consecutive day. A `git fetch` showed the
local clone *25 commits* behind the remote, which is the largest gap yet and made the
diagnosis unambiguous: a genuinely exhausted pool and a badly stale clone produce the same
zero. Pulling brought the pool to 11 and the breaker passed on re-run, with three days of
runway. This has now recurred often enough to stop being an anomaly. The breaker reads the
working tree at step 1, and the collector that updates that working tree is step 2, so the
measurement is structurally taken before the update. The fix belongs in the script — either
have `fuel.py` pull first, or have it fail distinctly when the clone is behind its remote —
rather than in a daily manual workaround.

## Source entries (3 picked from a pool of 11)

An unusually healthy pool, and an unusually correlated one. All 11 entries were captured in
a single browsing session on 2026-08-23, and nearly all of them were public-records and
discovery tools. That correlation, not scarcity, was the selection problem today.

The capture notes split cleanly into two kinds: three written in the operator's own words,
and eight that were text pasted from the destination page. Per the standing weighting —
the note is the heaviest signal because it is the only part the operator actually wrote —
the own-words group carried the pick. Two of the final three came directly from it: one
trade-data tool and one weather-visualisation tool.

The third own-words entry was deliberately passed over. Its natural fan-out — open-source
replacements, de-bloating, self-hosting — collides with three already-published briefs from
17, 19 and 21 August. It was replaced with an entry from the dominant cluster, whose
adjacency is unexplored. Final domain spread: international trade, atmospheric science, and
internet exposure. That is a genuine range rather than a rut, which was the goal.

## The 12 adjacent topics

From the trade-data entry:
1. **US customs bill-of-lading data and supplier discovery** → picked
2. What 2026 tariffs did to small-scale importers' sourcing decisions
3. The end of de minimis and what it changed for small ecommerce sellers
4. How importers screen suppliers under forced-labour enforcement

From the weather-visualisation entry:
5. Which weather model forecasters actually trust
6. How sailors and pilots use weather visualisation in practice
7. **AI weather models in operational forecasting** → picked
8. What personal weather stations contribute and where the data goes wrong

From the internet-exposure entry:
9. What internet-wide scanning finds exposed in 2026
10. The legality and ethics of mass port scanning
11. **People-search data brokers and the deletion laws aimed at them** → picked
12. Wardriving databases and the privacy of Wi-Fi based location

The automated near-dup guard flagged none of the twelve, and — per the standing lesson that
the guard misses subject revisits — `related()` was also run at this step rather than at
provenance time. It returned nothing for any of the twelve. That empty result is itself
informative: with 189 published topics, this index has no coverage at all of trade,
meteorology, or privacy law. The pool's correlation pointed somewhere genuinely new.

## Narrowing to three

Curiosity and freshness pointed the same way for once, so the narrowing was cheap. The
deciding criterion was the one added to this list two days ago: prefer a topic anchored on
a named organisation over a topic that is a concept. Each of the three picks resolves to an
institution with a dated action in the window — a customs authority and a specific
regulation, a forecasting centre and its model, a state privacy regulator and a compliance
deadline that fell inside the last 30 days.

Overlap was checked in both directions. #5 was dropped because it overlaps #7, and #9 was
dropped in favour of #11 because #11 had a hard date inside the window.

## Research notes

Three engine runs for three briefs, all landing on the first attempt. That is worth
recording against the nine runs needed for three briefs on 22 August. The difference was
entirely step-5 discipline: every topic string was title-shaped and anchored on a proper
noun, and every seed avoided the phrasings known to trigger the engine's comparison mode.
The lesson from two days ago transferred cleanly and cost nothing to apply.

Two process notes worth carrying forward.

**Leak avoidance moved upstream.** Two of the three picked entries are well-known enough
that the engine would plausibly cite their own domains, which trips the gate's privacy
check at step 10 and forces a post-hoc citation swap. Rather than wait for that, each
research run was instructed at dispatch to cite equivalent public sources instead. No brief
cites a picked domain, and the privacy check passed with no rework. Preventing this at
step 6 is materially cheaper than repairing it at step 10.

**One brief carried an unsourced claim, and the grep caught it.** The weather brief
asserted a five-day cyclone track-error comparison — three specific distances and a named
competing model. Grepping the raw evidence found zero support for any of it: the competing
model's name appears nowhere in the corpus, and neither do the figures. Every other number
in the same bullet verified. The claim was cut and replaced with what the evidence actually
supports. This is the second time a confident, well-formatted, entirely unbacked claim has
appeared in an otherwise sound brief, which suggests it is a standing property of the
synthesis step rather than bad luck. The number-by-number grep against the raw file should
be treated as mandatory, not optional.

Everything else verified against the raw evidence: the confidentiality-request mechanics
and its exact-match weakness, the removal-service study's participant and instance counts,
both enforcement fines, the enrolment and broker-registration figures, the ensemble scoring
gains and their stated regressions, and the compute-reduction figure. One internal
inconsistency was corrected, where settlement dates had been conflated with announcement
dates in a summary line while the body had both right.

Corpus honesty: the trade brief has effectively no live 30-day discussion layer, and says
so in its own text rather than dressing up an evergreen topic as a current one.
