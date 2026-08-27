# Provenance — 2026-08-27

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel

`eligible_pool: 3`, exit 0 — sitting exactly on the `--min-pool 3` floor. It was wrong, and
this is the first time the stale-cache defect has been shown to be capable of causing a false
skip rather than merely a misleading runway figure.

The sequence is worth writing down precisely. A `git fetch` on the self clone was run before
step 1, per the standing rule adopted on 21 August, and it reported the clone four commits
behind `origin/master`. Step 1 then measured `eligible_pool: 3`. Step 2 pulled, and the same
command re-run afterwards returns `eligible_pool: 5`. The pool was under-reported by two, and
it landed on the exact value of the circuit-breaker threshold.

**The workaround adopted on 21 August does not actually work.** `git fetch` updates remote
refs; `fuel.py` reads the working tree. So the fetch correctly tells you the clone is behind —
which is the diagnosis the note claimed — but it does not change the number the circuit
breaker then acts on. Had the pool been two commits thinner, the run would have aborted for
low fuel against a library that had five eligible entries in it. Fourth consecutive
occurrence, and the first with teeth. The fix owed is a real one: `fuel.py` must pull, or read
the fetched ref, before it counts. Running `git fetch` first is not a substitute.

## Source entries (3 picked from a pool of 4 distinct ids)

Five rows, four ids: the pool again contained a same-link twin sharing a single id, the benign
variant noted on 25 August, so retiring the id retires both rows and no second day of fuel is
lost.

Capture notes split two-and-two: two written in the operator's own words, two pasted verbatim
from the destination page. Per the standing weighting the two own-words notes carried their
picks outright, and both are short — one of them four words. Note length is still a bad proxy
for signal; authorship is the signal.

The people-search entry was passed over for the **third consecutive day**, for the same reason
each time: its natural fan-out is data brokers and deletion law, which is the brief published
on 24 August. Three declines is no longer a judgment call being re-made daily, it is a
standing state the funnel has no way to express. It will keep consuming a slot in every
selection pass until it is either picked with a deliberately different fan-out or retired
outright. Recommend the latter at the next opportunity.

That left four ids for three slots, so only one further pass-over was needed, and domain
spread decided it. Final spread: platform access and open-source front-ends, self-hosted
network infrastructure, and web analytics and publishing economics.

## The 12 adjacent topics

From the anonymous-platform-viewer entry:
1. **What actually still works for reading X without an account** → picked
2. How API pricing and login walls killed third-party front-ends
3. Which alternative front-ends survived: Invidious, Redlib, Piped

From the userspace-networking entry:
4. **Headscale and what breaks when you self-host the control plane** → picked
5. Running your own DERP relay and what it buys you
6. Userspace WireGuard against the kernel module in practice
7. What people replaced ngrok with after the pricing changes
8. Mesh VPNs compared after living with them: NetBird, Nebula, ZeroTier

From the AI-tool-discovery entry:
9. **What ChatGPT referral traffic is actually worth to small sites** → picked
10. Whether AI tool directories still send anyone anywhere
11. Whether Product Hunt still matters for an AI launch
12. What an AI tool review is worth once every listing is paid

Both automated guards returned clean on all twelve: `flag_near_dup()` returned
`flagged: False` for every one, and `related()` returned an empty list — not a weak match,
*zero* matches across 198 published titles, and it stayed empty for the three final titles
too. That is now the third consecutive day `related()` has returned nothing at all, which
continues to read as a scoring function that is not functional at this index size rather than
as evidence of genuine novelty. The manual keyword scan adopted on 25 August was run against
all twelve and found no same-subject prior. The highest similarity score anywhere in the fan
was 0.16, on a self-hosting cluster overlap rather than a subject collision.

## Narrowing to three, and a leak designed out rather than caught

Each pick had to anchor on a proper noun with a dated action inside the window: two named
projects taken offline on 24–25 August, a client release and a numbered issue on a named
control-plane project, and a named analytics platform's July 2026 channel-group change.

**Two of the three topics were deliberately steered away from their most natural framing,
because that framing would have made the engine cite a picked source's own URL.** This is the
leak recorded on 25 August, and today it was pre-empted at step 5 rather than caught at
step 10.

The AI-tool-discovery entry's obvious topic is candidate 10, whether those directories still
send anyone anywhere. Researching that would almost certainly have surfaced the picked
directory itself as a citation, failing the gate and aborting the whole run. Reframing to the
referral-traffic side of the same question keeps the thing worth learning — do these
intermediaries still deliver anything — while moving the evidence base to analytics studies
and publisher numbers. It is also the better brief: it comes back with measurements instead of
a directory listing.

The networking entry sits in the same GitHub organisation as several of its natural fan-out
targets, so the pick was anchored on the independent downstream project rather than the vendor,
and the researcher was given the picked repository as an explicit exclusion. It did not appear
in the evidence, so no substitution was needed.

**Designing the leak out is cheaper than catching it.** A gate failure at step 10 discards
three completed engine runs. Choosing the adjacent framing at step 5 costs nothing and, in
this case, improved the topic. Worth making standing practice: before writing a seed, ask
whether the obvious version of the query would cite the source that produced it.

## Research notes

Three engine runs, three briefs, no re-runs. All three carried the badge and a full stats
footer, and all three wrote raw evidence to disk, which is the check that the engine actually
ran rather than being improvised.

**The leak fired on the third run and was handled inside the research step.** The engine
surfaced the picked anonymous-viewer domain as a 494-point Hacker News thread — exactly the
predicted failure mode, a popular pick getting independently cited. It does not appear in the
brief; equivalent public evidence was substituted, and the finding it supported survived
intact. The other two picked domains did not appear in their corpora at all.

**Entity-miss demotion appeared again, and in its sharpest form yet, on the networking run.**
Every ranked cluster carried `fallback-local-score (entity-miss demotion)`. The footer reads
`Reddit: 32 threads │ 4,585 upvotes`, and almost all of it is off-topic — split-tunnelling
questions and self-hosting threads about Docker Compose, AI aesthetics and AppFlowy. Exactly
one Reddit item was used. The single YouTube video is about subnet routers, not the subject,
and was not cited. Hacker News returned nothing in thirty days. The brief's real evidence came
from the project's own issue tracker via direct API calls, which is itself one of its findings:
for a project of this size the tracker is the discussion venue, and the social layer has
nothing to say.

**Reddit was degraded on the analytics run** — 403 and 429 responses on public search, falling
back to listing discovery, returning 8 threads of which roughly 3 are on topic. The GitHub
layer there, 29 items, is entirely keyword pollution: bot comments embed `utm_medium=referral`
in their links, so unrelated pull requests matched. Nothing from GitHub was cited. Part of the
Hacker News layer matched on the bare word "track" and pulled in license-plate-camera stories
from an unrelated subject.

**Polymarket contributed a clean example of the same artifact**: four markets returned on the
front-ends run, all of them football fixtures for a team called Reading. Left out of the body,
still visible in the pass-through footer.

**Four unsourced claims were caught and removed across two briefs.** On the front-ends run,
the Hacker News API returns `points: null` for comments, so three superlatives that depended
on comment scores — "most-upvoted comment", "most popular consolation", "most-cited use case" —
were cut and replaced with countable phrasings. A first-pass summarizer had separately invented
comment point counts by attributing the story's 1,174 points to a single comment; that was
caught before it reached the draft. On the analytics run, a claim that a tracker indexed
eleven named assistants was cut when the evidence enumerated ten. The 24 August lesson
continues to earn its place: the dangerous claim is the confident, well-formatted, entirely
plausible number with nothing behind it.

Verification was pushed down into the research step rather than left to the end, which is why
these were caught individually rather than as a batch. On the front-ends run the full comment
corpus for both source threads was persisted to the raw directory specifically so every quote
would be greppable, and a 38-item automated check was run against it. That is the right shape
for this: make the evidence checkable, then check it.

One item in the analytics corpus was a repository issue written as a task handoff addressed to
an automated assistant. It was read as data, not acted on, and excluded from the brief. Nothing
else in any of the three corpora attempted anything similar.

No leak remains: the day directory was grepped for all three picked domains before the gate,
and none appears in any brief, the tweet, the telegram post, or this file.
