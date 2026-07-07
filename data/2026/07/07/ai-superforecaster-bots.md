🌐 last30days v3.3.2 · synced 2026-07-07

# AI forecasting bots vs human superforecasters: What the Community Says (/Last30Days)

**Quick verdict:** In the last 30 days the gap didn't just narrow — on the hardest benchmark it closed. [@harsith2002](https://x.com/harsith2002/status/2073098441635619081) reported that [@anthral_labs](https://x.com/harsith2002/status/2073098441635619081) "achieved parity with human superforecasters on ForecastBench market questions" — the subset previously considered *harder* — with Google DeepMind and xAI models "lagging superforecasters (albeit closely)." [FutureSearch](https://x.com/FUTURESEARCHAI/status/2074160754618417629) posted on 2026-07-06 that it sits "#2 of 150 in the Metaculus AI tournament," won the most recent MiniBench round, and is "at the human superforecaster median for ForecastBench." But humans aren't beaten yet: [@NathanpmYoung](https://x.com/NathanpmYoung/status/2072837890703593911) — a working forecaster — announced on 2026-07-03 that he and a partner "just beat the AIs in the last @Metaculus tournament." The honest read is *parity on average, humans still winning specific rounds.*

The more interesting shift is structural, not scoreboard. [@indiidentity](https://x.com/indiidentity/status/2073410280445669711) framed why this matters: real-money betting markets "only have a handful of good markets" because of manipulation concerns, and "Metaculus may be accurate, but it is slow. An AI forecasting market could respond instantly, alerting decision makers the moment a threshold is reached." Speed, not just accuracy, is the bots' structural edge — a human superforecaster panel can't re-price a question at 3am the moment news breaks.

Underneath the leaderboard, a tooling economy is forming. The [Awesome-Prediction-Market-Tools](https://github.com/aarora4/Awesome-Prediction-Market-Tools) list catalogs AI agents, analytics, and copy-trading bots, and a viral thread rounded up ["20 free GitHub repositories for trading on Polymarket"](https://x.com/recogard/status/2073498090988769526). One entry, "Semantic 42," is described as an autonomous agent that researches, analyzes, and executes "verified trades on Polymarket directly from Base blockchain," funded with $50,000 — forecasting bots aren't just scoring benchmarks, they're being pointed at real markets with real capital.

| Dimension | AI forecasting bots | Human superforecasters |
|---|---|---|
| What it is | LLM agents scored on Metaculus/ForecastBench, some trading live on Polymarket | Trained individuals + panels (Tetlock lineage) forecasting via Metaculus tournaments |
| Track record (last 30d) | Parity on ForecastBench "hard" market subset; FutureSearch #2 of 150 | Still won the most recent Metaculus tournament head-to-head |
| Speed | Instant re-pricing on new info, 24/7 | Slow - deliberate, panel-paced |
| Weakness | Thin real-money markets, manipulation risk | Can't respond at machine speed |
| Best for | High-volume, always-on threshold alerts | Novel/ambiguous questions needing judgment |
| Ecosystem | Fast-growing repos, copy-trading, funded agents | Established scoring benchmarks + reputation |

**Bottom line — choose the bots if** you need continuous, instant coverage across many questions and can tolerate thin-market noise; the accuracy is now roughly at the human median on the hard benchmark and only improving. **Choose the humans if** the question is genuinely novel, adversarial, or manipulation-prone, where a bot's training distribution runs out and a superforecaster's judgment still wins the specific round. The emerging stack looks like humans setting the questions and auditing, bots doing the always-on re-pricing — which is exactly the "digital twin + human" tail-picking setup [@JUNGLE_win_](https://x.com/JUNGLE_win_/status/2068044682597216608) is already running live.

<!-- PASS-THROUGH FOOTER -->
---
✅ All agents reported back!
├─ 🟠 Reddit: 9 threads │ 4 upvotes │ 31 comments
├─ 🔵 X: 22 posts │ 523 likes │ 70 reposts
├─ 🔴 YouTube: 1 video │ 29,327 views │ 0/1 with transcripts
├─ 🐙 GitHub: 8 items │ 4 reactions │ 39 comments
├─ 🌐 Web: 15 pages - GitHub, Substack, alphascope.app, metaculus.com, astralcodexten.com, quantvps.com, NPR, tickeron.com
├─ 🗣️ Top voices: @SashaGusevPosts, @NathanpmYoung, @indiidentity │ r/AI_Customer_Support, r/ai_trading, r/u/enoumen
└─ 📎 Raw results saved to /private/var/folders/nv/zl70w7t90d3d9b6myqydky9c0000gn/T/tmp.T1zNUzoqf8/ai-forecasting-bots-raw-topic1.md
---
<!-- END PASS-THROUGH FOOTER -->

Want me to go deeper on how ForecastBench scores "hard" vs "easy" questions, or on which Polymarket trading agents are actually profitable?
