---
ready: true
---
🎲 *Random Learning — 2026-08-27*

Three ways of routing around a platform. In all three, the dependency nobody counted is the one that decided the outcome.

*1. Reading X without an account*
Nitter and XCancel both went dark in about *24 hours* — to a letter, not a court order. Deadline *5 p.m. EST the next day*, claims under the Texas Harmful Access by Computer Act and the Lanham Act. A C&D isn't binding. Both complied anyway.

The interesting document is the five demands, specifically number four: "*Delete all X account credentials and session tokens*." That isn't a takedown request, it's a description of how Nitter works. Nitter read X by logging into X.

So the standing consolation — "they can't stop instances in other countries" — was already wrong. Instances were rate-limited to death *before* the letter, and X appears to have revoked the credentials outright. That doesn't need jurisdiction. And the top self-hosting guide's prerequisite is "*a burner/temporary Twitter account without 2FA enabled*": the recommended way to read X without an account is to make an X account.

The loss people actually name isn't the interface — it's the *RSS endpoint*, in 22 separate comments. Twitter had feeds once; Nitter had been synthesising them ever since.

The asymmetry is the punchline. HN: *1,174 points*. r/privacy: 1,208 upvotes. On X itself — the platform whose login wall is the story — a 30-day search returns *12 posts and 170 likes*, only three on topic.

*2. Headscale, and what breaks when you self-host the control plane*
You can replace Tailscale's coordination server. You're still running *their client*, and that's where it broke: Tailscale *1.102.2* emptied the exit-node list on macOS and iOS against a stock Headscale 0.29.3.

The good part is what happened next. Tailscale's support desk blamed Headscale's MapResponse status bits; a user disproved it on the wire and found the real gap — the hosted control plane emits a `suggest-exit-node` attribute Headscale never emits. Fix: *two lines of `nodeAttrs`* in your own ACL, confirmed by five other people.

Costs worth knowing first:
• Version drift is a *one-way door* on Apple — no downgrade on iOS, none via the App Store.
• The floor moves: client *v1.80.0* min in 0.29.3, *v1.82.0* in unreleased 0.30.0.
• ACL policy loads from file *exactly once*, then lives in the DB — later edits silently do nothing.
• `tailscale ping` succeeds through a blocking ACL, so misconfiguration reads as "server down."
• Funnel: `not_planned` since *2022*, now cited by name as blocking a migration.

The measurable win is DERP — one operator went *500ms+* on public relays to about *30ms* self-hosted, at 38 yuan/month. And the clearest statement of the point came from a red-team toolkit, not the homelab crowd: run Headscale as control plane *and* DERP relay and "*Tailscale Inc knows nothing about your tailnet*."

*3. What ChatGPT referral traffic is worth*
Volume is settled: *about one percent*. Conductor 1.08%; Orbit Media, best-instrumented, *0.5%* across 28.9M sessions; Elmo 0.2%. Hundreds-of-percent growth on a base that rounds to nothing — and *82–87%* is ChatGPT, so an AI referral strategy is a ChatGPT strategy.

Conversion is not settled, and that's the tell. Same channel, twelve months: *1.3%* … 4.7% … 14.2% … *16.8%*. Elmo's 1.3% is AI traffic converting *worse than email*.

Why nobody agrees: ~*70%* of AI visits arrive with no referrer and land in GA4 as *Direct*. GA4 only began auto-classifying an "AI Assistant" channel in *July 2026* — so every multiple published before this summer ran on about a third of the data.

The two biggest corporate receipts contradict each other. Shopify: AI traffic and orders *tripled*. Booking Holdings: under *1% of room nights*, nearly four years in.

The ledger is lopsided: loss measured, gain anecdotal. Axios has small publishers down *60%* of search referrals over two years; the month's best-documented AI revenue receipt is one brand's *$22,700*.

_Sources: last30days across Reddit, HN, X, GitHub, YouTube + web._
