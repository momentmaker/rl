🌐 last30days v3.3.2 · synced 2026-07-22

What I learned:

**"Advertise in ChatGPT" went live and it is the single loudest AI story of the week** - OpenAI's self-serve Ads Manager landed a launch-day [Hacker News](https://news.ycombinator.com/item?id=46652024) thread of 861 points and 671 comments, and an [r/singularity](https://www.reddit.com/r/singularity/comments/1v2s6iz/openai_launches_chatgpt_ads/) post at 175 upvotes. OpenAI's own pitch is that "in ChatGPT, people share richer context, enabling advertising that is more relevant, personalized, and useful" - which is exactly the framing critics seized on. The pilot targets logged-in Free and Go users in the US plus Brazil, UK, Japan, South Korea and Mexico; Pro/Business/Enterprise/Education stay ad-free.

**The "Sam Altman lied to your face" reversal is the emotional core of the conversation** - Marketer [@neilpatel](https://x.com/neilpatel/status/2077815694775771573) framed it as "one of the most important tells in tech right now": two years ago Altman called ads in AI "uniquely unsettling" and "a last resort," and now OpenAI is testing them. His read is measured though - "OpenAI did not suddenly become an ad company. It became a company that needs ad money." The [Hacker News](https://news.ycombinator.com/item?id=46652024) title captured the mood in one line: "ChatGPT is getting ads. Sam Altman once called them a 'last resort.'" Outlets like [PC Gamer](https://www.pcgamer.com/software/ai/here-we-go-openai-ceo-sam-altman-once-called-it-a-last-resort-but-chatgpt-is-about-to-get-stuffed-with-ads/) and [The Ken](https://the-ken.com/podcasts/daybreak/the-worlds-most-popular-ai-assistant-is-getting-a-sales-gig/) leaned into the same "welcome to last resort" arc.

**The privacy angle is what actually enrages users - it is your conversations being sold, not a banner** - [@TheAhmadOsman](https://x.com/TheAhmadOsman/status/2079619615756337274) got 196 likes on "OpenAI sent me an email to start advertising to ChatGPT users. The data they are collecting from your conversations will be used to serve ads to you. Yet another reason that Local and Opensource AI must win." That local/open-source flight instinct showed up in the corpus too - [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) was among the top Reddit communities in the pull. Earlier reporting captured the same nerve when users on Reddit called mid-conversation "app suggestions" a sign of ["enshitification"](https://www.tomsguide.com/ai/openai-tipped-to-launch-ads-on-chatgpt-and-theres-already-a-huge-backlash).

**Performance marketers are genuinely excited - the pitch is intent, not eyeballs** - [@Traderibo123](https://x.com/Traderibo123/status/2077096188739018769) nailed the bull case: "The interesting part isn't the 1B users, it's the intent. People open ChatGPT to solve problems, not to scroll." Tooling is already wiring in - [@Fraank9991](https://x.com/Fraank9991/status/2077098487808937991) hyped "AI Media Buyer now connects directly to OpenAI Ads," pitching a single dashboard for OpenAI, Meta, Google and TikTok campaigns. On the infra side, [PostHog](https://github.com/PostHog/posthog/pull/72649) already merged a PR implementing an `openai_ads` import source into its data warehouse - a concrete signal that analytics vendors are treating this as a real ad channel.

**The "is spend actually shifting from Google?" question has a surprisingly deflationary answer** - Per [eMarketer](https://www.emarketer.com/content/how-search-shifting-5-charts), more than 80% of 2026 US "AI ad spending" runs through paid search next to Google's AI Overviews, not chatbot conversations - the pie got bigger and AI took the new slice rather than shrinking Google. Demand signals are real ([DesignRush](https://news.designrush.com/chatgpt-ads-google-search-budgets-implications) cites ~80% of SMBs interested and ChatGPT-referred users converting ~1.5x higher; G2 says 51% of B2B buyers now start research with an AI chatbot), but analysts are brutal on OpenAI's own math: [24/7 Wall St.](https://247wallst.com/investing/2026/07/21/openai-is-on-pace-to-miss-its-own-ad-revenue-forecast-by-90-heres-what-it-means-for-the-ai-trade/) reports eMarketer sees OpenAI missing its own five-year ad forecast (the $2.5B-in-2026-to-$100B-by-2030 ramp per [The Tech Portal](https://thetechportal.com/2026/04/09/openai-projects-100bn-in-ad-revenue-by-2030-around-2-5bn-in-2026-report)) by roughly 90%.

KEY PATTERNS from the research:
1. The launch is the story, the reversal is the hook - "last resort" is the phrase every source keeps quoting, per [@neilpatel](https://x.com/neilpatel/status/2077815694775771573)
2. Backlash is aimed at conversation-data targeting, not ads-as-a-concept, and it drives a local/open-source flight instinct, per [@TheAhmadOsman](https://x.com/TheAhmadOsman/status/2079619615756337274)
3. Marketers frame the moat as intent capture (problem-solving mindset) sitting closer to paid search than to social feeds, per [@Traderibo123](https://x.com/Traderibo123/status/2077096188739018769)
4. Ad-tech is already integrating - unified dashboards on X, an `openai_ads` warehouse source merged on [GitHub](https://github.com/PostHog/posthog/pull/72649)
5. The spend-shift is additive, not zero-sum yet - >80% of AI ad dollars still flow through Google-adjacent paid search, and analysts think OpenAI's revenue projection is ~90% too optimistic, per [eMarketer via 24/7 Wall St.](https://247wallst.com/investing/2026/07/21/openai-is-on-pace-to-miss-its-own-ad-revenue-forecast-by-90-heres-what-it-means-for-the-ai-trade/)

---
✅ All agents reported back!
├─ 🟠 Reddit: 29 threads │ 16,370 upvotes │ 3,438 comments
├─ 🔵 X: 24 posts │ 843 likes │ 81 reposts
├─ 🔴 YouTube: 4 videos │ 175,362 views │ 0/4 with transcripts
├─ 🟡 HN: 28 storys │ 1,513 points │ 989 comments
├─ 🐙 GitHub: 12 items │ 1 reactions │ 11 comments
├─ 🌐 Web: 11 pages - windsor.ai, Forbes, Business Insider, OpenAI, supermetrics.com, stubgroup.com, miamiherald.com, marketingdive.com
├─ 🗣️ Top voices: @denohawari, @TheAhmadOsman, @Fraank9991 │ r/LocalLLaMA, r/ChatGPT, r/singularity
└─ 📎 Raw results saved to /private/var/folders/nv/zl70w7t90d3d9b6myqydky9c0000gn/T/tmp.mzqOWZte2w/ads-coming-to-chatgpt-and-openai-building-an-ads-business-raw-v3clean.md
---
