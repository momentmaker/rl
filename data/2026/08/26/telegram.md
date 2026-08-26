---
ready: true
---
🎲 *Random Learning — 2026-08-26*

Three confident remedies. In all three, the measurement is missing or says the opposite.

*1. What Windows debloat tools actually remove*
Two PowerShell scripts carry *117,530* GitHub reactions between them — Chris Titus Tech's *winutil* (61K stars) and *Win11Debloat* (56K). Then somebody measured. A four-tool test found a fresh Windows 11 install sits at *1.9–2.1GB* of RAM at boot and the tools don't materially move it; biggest gain, *100–200MB*. PCMag on 22 August: "Debloat tools claim to make Windows 11 more efficient by... freeing up RAM. In practice, that's not the case." That post got *2 likes*. The loudest post in the window is the opposite claim, at *426 likes*.

What breaks is narrower than a bricked machine: an open issue titled "After running Win11Debloat, my friend can't sign into their Microsoft account or Xbox." The unrecoverable removals are the *Microsoft Store* and *XboxSpeechToTextOverlay*.

And the bloat returns *by design* — image-provisioned packages reappear after feature updates. The category has conceded it: the hook shifted from "removes bloat" to "*blocks reinstalls*," and the tools that survive work upstream of the OS. Microsoft's supported version is *Enterprise and Education only*. Meanwhile the top HN thread of the window — *671 points* — is Windows 11's Weather app eating *over 1GB* of RAM. A 1.2GB complaint and a 200MB remedy is the category in two numbers.

*2. What arXiv's AI moderation catches*
arXiv refuses CS review articles not already vetted by a journal, and runs a *one-year submission ban* for unchecked AI-generated content. The rules are settled; the fight moved to enforcement. Inside Higher Ed's verdict: welcome but *unenforceable*.

The number that undercuts it is hosted on arXiv itself: a citation study estimates *78.8% of non-existent citations pass moderation* anyway. Screened manuscripts really do contain disproportionately many hallucinated citations — so it catches something — but it's a filter, not a gate.

The best evidence of a penalty landing is a git commit, not a press release. A pull request records it exactly: "arXiv declined the paper on 2026-08-18 (moderation, *MOD-100537*), with an account-level restriction requiring a journal reference/DOI for future submissions." Not one rejected paper — a gate on the account. The author rerouted to Zenodo.

Two mismatches worth keeping. Researchers are angrier about *detectors* than the ban ("I'm just a good writer, and that's apparently a crime now"), while arXiv's process actually routes through a human moderator, a section chair and an appeal — not a classifier score. And arXiv can ban a submitter but nobody has a lever for a *reviewer*: "An AI 'reviewed' my paper. The editor told me to suck it up."

*3. What UK identity verification has actually changed*
Mandatory Companies House ID verification went live *18 Nov 2025*, transition to *17 Nov 2026* — so this is the last quarter of a grace period. As of end-June, *55% of directors* and *50% of LLP members* were verified, against *6–7 million* people in scope. Half the register, three months out — and it won't resolve on one day, because the catch mechanism is the *confirmation statement*, unwinding across rolling filing anniversaries.

The trap isn't verification, it's the *11-character personal code* you must supply at your next filing. Anyone who verified before *8 July 2026* was never emailed it — and losing the code is identical to not verifying.

Did it remove fake directors? *Nobody has published that number.* Every official statistic measures uptake, not register cleanliness. And in March 2026 a Companies House flaw let any logged-in user open the private dashboard of any of ~*five million* companies, for five months.

A footnote on reading research honestly: that brief's footer shows *9,608* Reddit upvotes. Almost all of it is one off-topic thread about a neighbour setting their house on fire — it matched on "house." The on-topic threads scored *11* and *5*.

_Sources: last30days across Reddit, HN, X, GitHub, YouTube + web._
