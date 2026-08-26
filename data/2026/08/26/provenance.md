# Provenance — 2026-08-26

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel

`eligible_pool: 6`, two days of runway, exit 0 — but only after a manual `git fetch` on the
self clone, which came back one commit behind. This is the stale-cache defect recorded on
21 August, appearing again. The fetch is what distinguishes a genuinely thin pool from a
clone that has not seen the last capture session; without it the runway number is measured
against yesterday's library. Third occurrence in the log. The script fix is still owed, and
running `git fetch` before step 1 should now be treated as part of the procedure rather
than a workaround.

## Source entries (3 picked from a pool of 6)

The pool was small and correlated — all six captured across two sessions on 23 and 24
August — and it contained a same-link twin sharing a single id, which is the benign variant
noted on 25 August: retiring the id retires both rows, so no second day of fuel is lost.

Capture notes split one-to-five: a single note in the operator's own words, five pasted
verbatim from the destination page. Per the standing weighting the own-words note carried
its pick outright, and it was the shortest note in the pool.

One entry was deliberately passed over despite being a reasonable candidate: a people-search
service. Its natural fan-out is data brokers and deletion law, which is the brief published
on 24 August. Same reasoning as the 25 August pass-over, and it is now the second
consecutive day this particular entry has been declined for the same collision. It will keep
surfacing until it is picked with a deliberately different fan-out or retired. A second
entry — an AI tool directory — was passed over on domain-spread grounds, since the last
week of briefs is already AI-heavy.

Final domain spread: consumer OS tooling, scientific publishing integrity, and UK corporate
registry law. That is a genuine range.

## The 12 adjacent topics

From the open-source-replacements entry:
1. **Windows 11 debloat tools — what they remove and what returns** → picked
2. Immutable Linux desktops as the debloat endpoint
3. Telemetry on by default in developer tooling
4. De-Googling Android with GrapheneOS in 2026

From the academic-graph entry:
5. **arXiv moderation and AI-generated paper submissions** → picked
6. OpenAlex as open citation infrastructure after Microsoft Academic Graph
7. Retraction Watch and papermill detection at scale
8. Semantic Scholar API limits and downstream tool breakage

From the legal-entity-data entry:
9. **Companies House identity verification** → picked
10. EU beneficial ownership registers after the CJEU ruling
11. Legal Entity Identifier adoption and GLEIF
12. Shell company detection and sanctions screening data quality

**Both automated guards returned clean on all twelve, and the keyword grep caught a real
collision they missed.** `flag_near_dup()` returned `flagged: False` for all 12 and
`related()` returned an empty list for every one of them — not a weak match, *zero* matches
across 195 published titles. The manual keyword scan adopted as standing practice on
25 August then found a direct hit: **"AI-generated papers and fabricated citations in peer
review"** (2026/06/19). This is now the second consecutive day the similarity scoring has
missed a same-subject prior and the keyword grep has caught it. Treat `related()` as
non-functional for revisit detection at this index size; the grep is the actual control.

**The collision was assessed and the topic was kept.** The June brief is about the ban being
*announced* — arXiv's May "one-strike" rule, the academic backlash, "then academics lost
their minds." Today's centre of gravity is what the policy measurably *did* in the two
months since: the 78.8% leak rate from a citation study that did not exist in June, the
first first-person receipt of enforcement landing (a moderation ticket number plus an
account-level restriction), the migration of researcher anger from the ban to AI detectors,
and the reviewer-side gap where no policy exists at all. That is a follow-up with new
evidence, not a restatement.

One honest deduction against it: both briefs lean on the same Inside Higher Ed "welcome but
unenforceable" line, and in today's brief it does framing work in the opening section. The
repeated citation is real. It survives because the load-bearing fact today is the 78.8%
figure, which is new, measured, and points the opposite way from the policy's confidence.
The connection is recorded in `meta.json` rather than left implicit.

## Narrowing to three

Each surviving pick had to anchor on a proper noun with a dated action in or near the window
— two named GitHub projects with releases dated this month, an arXiv moderation ticket dated
18 August, and a UK statutory deadline with published quarterly compliance statistics. The
nine dropped topics were dropped for sibling overlap and domain spread, not for weakness;
the registry cluster in particular had three viable candidates and lost two to the one-per-
entry rule.

## Research notes

Three engine runs, three briefs, no re-runs. All three carried the badge and a full stats
footer, and all three wrote raw evidence to disk (43–64KB each), which is the check that the
engine actually ran rather than being improvised.

**Entity-miss demotion appeared again, on the academic run.** Every ranked cluster in the
arXiv corpus carried `fallback-local-score (entity-miss demotion)`, and the visible symptom
is an X tier populated by an unrelated IPFS chat-log project that ranked into the top voices.
The brief does not cite any of it. This is the 14 August failure mode and the footer gives no
indication of it.

**The footer-stats trap fired hard on the registry run, and the brief says so in its own
text.** The Companies House footer reads `Reddit: 3 threads │ 9,608 upvotes`, which looks
like a healthy community layer. It is one off-topic r/LegalAdviceUK thread about a neighbour
setting their house on fire, at 9,592 points, matched on the token "house." The two genuinely
on-topic threads scored 11 and 5. The engine footer passes through verbatim so the number
stays, but the brief names the artifact explicitly and the telegram post carries it as a
closing note, because "half of six million directors are affected and Reddit produced two
threads scoring 16 points between them" is a more interesting finding than the fake 9,608.

**One unsourced claim was caught and removed at the verification pass.** The registry brief
as returned asserted that "over 10,000 accountants, solicitors and formation agents have
registered as Authorised Corporate Service Providers." A grep of the raw evidence for that
figure returned nothing — the corpus contains an ACSP directory, one named firm announcing
its registration on 20 August, the GOV.UK fit-and-proper criteria, and the AccountingWEB
practitioner discussion, but no count anywhere. The sentence was rewritten to assert only
what the evidence carries. This is the 24 August lesson working exactly as intended: a
confident, well-formatted, entirely plausible number with zero backing.

One near-miss on method worth recording: the first verification pass flagged "unenforceable"
as unsourced in the arXiv brief. That was a false alarm caused by a case-sensitive grep — the
raw file carries it capitalised inside a headline. Grep case-insensitively, or the check
manufactures its own false positives.

**Two claims were checked for inversion and held.** The arXiv brief's chronology — an
abolitionist mathematics essay reaching Hacker News on 22 August at 10 points, three days
after a measured essay drew 210 points and 269 comments — was verified against the raw dates
and scores in both directions before being stated, because the reception asymmetry is the
whole point of the sentence and an inverted date would reverse its meaning. The Windows
brief's star counts, release version strings and issue number all verified directly.

No leak was found: the day directory was grepped for all three picked domains before the
gate, per the standing 25 August rule, and none of the three appears in any brief, the
tweet, the telegram post, or this file.
