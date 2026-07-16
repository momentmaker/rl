🌐 last30days v3.3.2 · synced 2026-07-16

What I learned:

**Webhooks are the only real serverless option - long-polling is architecturally impossible on Vercel and Cloudflare Workers, and that single constraint drives every other decision.** Long-polling needs a persistent process endlessly asking Telegram "any new messages?" via `getUpdates`, which serverless platforms cannot provide because they terminate after each request, per [grammY's deployment-types guide](https://grammy.dev/guide/deployment-types) and [GramIO](https://gramio.dev/updates/webhook). Webhooks flip the model: you register an HTTPS URL, Telegram POSTs updates to you, and the function runs only when an update arrives - a natural fit for scale-to-zero. As [PandaStack's 2026 hosting roundup](https://pandastack.io/blog/best-telegram-bot-hosting-2026) puts it, "for webhook bots specifically, serverless is a great fit," while long-polling wants an always-on host like Render or Fly.io. The community consensus is clean: if you want serverless, you want webhooks, full stop.

**Cold starts are a real but mostly-tolerable tax, and Cloudflare Workers' near-zero cold-start is its headline advantage over Vercel's Lambda-backed functions.** On free-tier serverless, scale-to-zero means the bot idles at zero cost then cold-starts when a message arrives - [PandaStack](https://pandastack.io/blog/best-telegram-bot-hosting-2026) calls this "acceptable for low-traffic bots" but recommends a warm tier for instant responses, describing the wake as "like a lazy cat waking up from a nap." Cloudflare Workers largely sidesteps this: in [codeSTACKr's Workers walkthrough](https://www.youtube.com/watch?v=xRt9PwphmY8) the pitch is "runs your code within milliseconds of your users worldwide, and no more cold starts, zero milliseconds worldwide," because Workers run in V8 isolates rather than spinning up a container. Vercel's own constraint is a timing ceiling, not a cold-start one: you get roughly 25 seconds on the default grammY `webhookCallback` adapter against Telegram's 60-second retry window, per [grammY's Vercel hosting docs](https://grammy.dev/hosting/vercel).

**State is the hard part, and Cloudflare's Durable Objects have emerged as the go-to primitive for per-user Telegram bot state on the edge.** The most-engaged artifact in the window was [flashblaze's "Telegram Bot with Cloudflare Workers, Durable Objects and grammY"](https://flashblaze.xyz/posts/cloudflare-workers-durable-objects-telegram-bot/), which hit Hacker News as "[Telegram Serverless](https://news.ycombinator.com/item?id=46851922)" with 195 points and 99 comments - the pattern is one Durable Object per user, giving strongly-consistent SQL-backed state. [Cloudflare's storage-options docs](https://developers.cloudflare.com/workers/platform/storage-options/) draw the split developers actually use: Durable Objects for strongly-consistent per-user state, Workers KV for high-read/low-write session and config data (bounded by ~1 write/sec per key). [@HugoValters](https://x.com/HugoValters/status/2077656984535364002) captured the appeal in one line: "Deploy stateful Workers with Durable Objects... strongly consistent state across requests via a single global coordinator with SQLite-based persistence."

**The sneakiest serverless-webhook footgun is concurrency: because responding to a webhook makes Telegram immediately send the next update, sessions can silently corrupt.** [grammY's Cloudflare Workers docs](https://grammy.dev/hosting/cloudflare-workers-nodejs) warn that when the old update is still processing, "two updates which were previously processed sequentially are suddenly processed in parallel, leading to race conditions," and that "the session plugin will inevitably break due to WAR hazards, causing data loss." The fix the docs prescribe is discipline plus offloading: keep middleware fast and push slow work to a queue rather than doing it inside the small webhook window. This is the concrete tradeoff versus a traditional always-on server, where sequential long-polling naturally serializes updates and this class of bug does not exist.

**Multi-platform starter templates have consolidated the "build once, deploy anywhere serverless" pattern, with grammY as the dominant framework glue.** The [sxzz/telegram-bot-starter](https://github.com/sxzz/telegram-bot-starter) (84 stars, TypeScript) advertises itself as "a starter template for Telegram bots on Serverless, with Vercel, Netlify, Cloudflare, and more support," using Nitro to abstract the deploy target - so the same bot code ships to whichever serverless host you pick. grammY itself is the connective tissue across nearly every tutorial in the window because it works in browsers/isolates (`import { Bot } from "grammy/web"`) and ships `webhookCallback` adapters for both Cloudflare and Vercel, per [its GitHub repo](https://github.com/grammyjs/grammY). The remaining friction is small but real: Telegram's webhook API rejects Cloudflare's default `*.workers.dev` domain, so a custom domain is required, per the [Cloudflare Workers hosting guide](https://grammy.dev/hosting/cloudflare-workers-nodejs).

KEY PATTERNS from the research:
1. Webhooks or bust on serverless - long-polling can't run on scale-to-zero platforms, per [grammY](https://grammy.dev/guide/deployment-types)
2. DO-vs-KV storage split - Durable Objects for consistent per-user state, KV for read-heavy config, per [Cloudflare docs](https://developers.cloudflare.com/workers/platform/storage-options/)
3. Cold start as a tier decision - free scale-to-zero accepts cold starts, warm tiers buy instant response, per [PandaStack](https://pandastack.io/blog/best-telegram-bot-hosting-2026)
4. Fast-middleware-or-queue - avoid webhook race conditions that corrupt sessions by offloading slow work, per [grammY](https://grammy.dev/hosting/cloudflare-workers-nodejs)
5. Write-once multi-target templates - Nitro-based starters deploy the same bot to Vercel/Netlify/Cloudflare, per [sxzz/telegram-bot-starter](https://github.com/sxzz/telegram-bot-starter)

---
✅ All agents reported back!
├─ 🟠 Reddit: 5 threads │ 423 upvotes │ 97 comments
├─ 🔵 X: 5 posts │ 75 likes │ 4 reposts
├─ 🔴 YouTube: 8 videos │ 1,411,274 views │ 4/8 with transcripts
├─ 🟡 HN: 12 storys │ 935 points │ 578 comments
├─ 🐙 GitHub: 1 item │ 84 reactions │ 2 comments
├─ 🌐 Web: 14 pages - developers.cloudflare.com, pandastack.io, grammy.dev, kuberns.com, GitHub, vercel.com, teleclaw.bot
├─ 🗣️ Top voices: @minimalistneko, @miantiao_me, @auth0 │ r/CloudFlare, r/Telegram, r/nextjs
└─ 📎 Raw results saved to (local, non-committed)
---

I'm now an expert on building Telegram bots on serverless. Some things I can help with:
- Scaffolding a grammY webhook bot for Cloudflare Workers with a Durable Object per user for state, plus the custom-domain and `setWebhook` setup
- Designing the storage layer - deciding between Durable Objects, Workers KV, D1, or an external DB - and adding a queue so slow work never blocks the webhook window
- Porting an existing long-polling bot to a serverless webhook deploy on Vercel or Cloudflare, including handling cold starts, the 25s/60s timing limits, and the session race-condition footgun
