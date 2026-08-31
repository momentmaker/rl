---
ready: true
---
🎲 *Random Learning — 2026-08-31*

Three subjects where the headline number and the load-bearing number are not the same number — and in all three, the gap is the finding.

*1. Record linkage: matching identities across messy databases*
The problem is deciding whether two rows are the same person. The open-source shelf for it looks well stocked and is mostly abandoned: dedupe at *4,510 stars*, no push since July 2025; recordlinkage *1,062*, none since February 2024.

Three things worth carrying out:

• *The threshold is a cost decision, not a hyperparameter.* One practitioner matching NHTSA filings: "a missed link inflates a non-match rate that I report openly. A false link *fabricates a discrepancy* between two unrelated events and attaches it to a named company." Not fastidiousness — false links *bias downstream estimates*, worst exactly where match rates are low and identifiers are dirty.

• *Blocking sets a recall ceiling almost nobody scores.* You can't compare every pair, so you block — and anything blocking never generated cannot be found. Splink can score those as false negatives, but the flag is wired into *one of four* evaluation methods, and not the one most clerical review produces.

• *The hard failure isn't typos, it's error that correlates with a real record.* Called "PII bleed": two people with radically different names sharing email, phone, address and date of birth. That breaks the *independence assumption* the model rests on. The best reply refuses to call it an error — "I could legally change my first and last name and still retain all my other information."

Most transferable idea of the day: expanding "St." → "Street" beats compressing, because *directionality is a choice about which collisions to create*. Compression is many-to-one — it silently swallows "Saint" too.

The whole conversation lives in one repo's discussion tab. Of 24 Reddit threads pulled, *zero* on topic; HN, zero; the two YouTube videos, *63 views between them*.

*2. Kdenlive, after real projects*
KDE Gear 26.08 shipped 20 August. The project's own wording: "lots of *quality of life* improvements and polishing."

The number worth the brief: the engine pulled *2,061 upvotes* across 16 threads, which reads healthy until you split it. *1,856* sit in r/kde on threads about Dolphin and KDE Connect. *142* are general r/editors craft questions. That leaves *63 upvotes* across every r/kdenlive thread in the window.

Two more tells. Both crash reports in 30 days are against *26.11.70, an unreleased build* — nothing against the version people run. And there is exactly *one* first-person account of finishing real work: 20 hours per video down to 3–4 after moving off Blender's sequencer. Nothing anywhere about how a long timeline behaved after a month.

Mostly it circulates as a row in a paid-to-free swap table. The month's biggest such list routes Premiere users to DaVinci Resolve and never names it.

*3. FFmpeg hardware AV1 on NVENC*
FFmpeg *9.0* shipped in-window. Its changelog's only NVENC line is a *removal*; the AV1 work appears solely in the maintainer's blog. The release's HN thread ran *466 points, 97 comments*, with zero mentions of AV1, hardware encoding, x264, x265, SVT or VMAF.

Meanwhile one person measured it, on an RTX 5070 Ti, same source, same CQ 27:
• NVENC H.265 — *339 MB*, VMAF 91.90, ~3 min
• NVENC AV1 — *638 MB*, VMAF 93.46, ~2 min
• SVT-AV1 (CPU, preset 2) — *263 MB*, VMAF 92.32, *55 min*

The GPU's newer codec produced nearly *double* the file. The best objection is that CQ isn't comparable across codecs — and the table supports it, since the biggest file also scored highest. Nobody resolved it.

His follow-up two weeks later is the honest version: AV1 wins on *10/12-bit, HDR, very high bitrate* sources, by about *5%*. HEVC wins everything else by *20–30%*.

And the documented way to close the gap deletes the reason you used the GPU: NVIDIA's UHQ mode buys *22.79% BD-Rate* at *over 400% more latency* and up to *40% more board power*.

_Sources: last30days across Reddit, HN, X, GitHub, YouTube + web._
