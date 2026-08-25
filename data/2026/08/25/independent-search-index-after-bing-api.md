---
title: "Where independent search engines get their index after the Bing API shutdown"
date: 2026/08/25
tags: [search-engine, index, bing-api, marginalia, brave, mojeek, antitrust]
---

🌐 last30days v3.3.2 · synced 2026-08-25

What I learned:

**The set of search engines that actually own an index is far smaller than the set that markets itself as an alternative** - the corpus keeps making the same distinction and most alternative-search roundups blur it. [SearchEngines.Net](https://www.searchengines.net/guides/search-engines-other-than-google/) draws the line explicitly: use Brave or Mojeek when you specifically want an independent index, choose DuckDuckGo, Startpage, Ecosia or Qwant when privacy or mission matters more than crawler independence, and SearXNG "doesn't crawl the web itself" at all - it queries 100+ other engines and merges. Kagi is openly hybrid: Google, Bing, Mojeek, Brave, Marginalia, plus its own indexing component. Marginalia's index is a *supplier* to a commercial search product, which is a more interesting fact about it than anything on its own homepage.

**Marginalia is the best-documented independent crawler and one of the smallest** - it runs its own crawler identified as `search.marginalia.nu` in both user-agent and robots.txt token, from a published static IP range, on an eight-to-ten-week refresh cycle, with no Google or Bing feed anywhere in the pipeline. The size is where you have to be careful: the project FAQ says roughly 300 million documents occupying about a terabyte as of 2024 and describes itself as outdated, and the current about-page says only "hundreds of millions." No dated 2025 or 2026 figure has been published, so any precise current number circulating is unsourced. For scale, [Mojeek](https://www.searchengines.net/mojeek/) hit 9 billion pages in 2025 and Brave reports 30 billion with 100M+ daily updates. Marginalia is roughly two orders of magnitude below the small commercial independents, and that is the point rather than a failing.

**The clearest statement of what Marginalia is for came from a competitor's README** - [mwmbl](https://github.com/mwmbl/mwmbl), an open-source non-profit search engine, positions itself by contrast: "Marginalia Search is fantastic, but our goals are different: we aim to be a replacement for commercial search engines whereas Marginalia aims to provide a different type of search." The same README dismisses YaCy's peer-to-peer index as spiritually closest but too slow to fetch results. Those two sentences map the whole non-commercial index space better than any listicle in the window.

**The economics of owning an index inverted in the last year, and the Bing shutdown is why** - Microsoft retired the Bing Search APIs on 11 August 2025, which removed the cheap tier that let anyone put a search box on a product without crawling. The [2026 replacement guides](https://cloro.dev/blog/bing-search-api-key/) rank the survivors and almost all of them are resellers or SERP scrapers - SerpAPI for Bing SERP parsing, DataForSEO at $0.60 per thousand - with Brave the one entry described as "an independent 30B-page index outside the Google/Microsoft duopoly." Then the agent market arrived with real money behind it: Brave launched an LLM Context API built for agent consumption, and Parallel raised $100M to build out its own web-scale index. Crawling the web yourself went from a hobbyist's principled loss to venture-backed infrastructure in about twelve months. A [new entrant on Reddit](https://www.reddit.com/r/Blopus/comments/1vss1bl/blopusai_web_search_api_for_llms_agents/) pitches itself on exactly that axis: "built on our own independent, continuously crawled index - not a Google or Bing reseller, and not a scraper hitting sites on demand."

**The legal route to an index is real, ordered, and still delivering nothing** - Judge Mehta's September 2025 remedy requires Google to share its web search index and click-and-query data with Qualified Competitors and to offer capped syndication licences. But Google is appealing, the DOJ cross-appealed by a 3 February 2026 deadline seeking the divestitures Mehta refused, and appellate argument is projected for late 2026 or early 2027. The [Economic Liberties amicus](https://www.economicliberties.us/our-work/amicus-brief-united-states-of-america-v-google-search-rem/) calls the ruling "the barest data-sharing and syndication remedies in its arsenal," noting it left the default payments intact while Google grounds its GenAI products in the same search index. [SerpAPI filed its own brief](https://serpapi.com/blog/amicus-brief-in-u-s-v-google/). Nobody has received index access.

**What people actually reach for these engines to do is find the old web, not replace Google** - the one high-engagement video in the window, at 128,920 views, frames it as recovering what ranking buried: "Somewhere out there is a website some guy built in 2004 about the history of lighthouse lenses, and it is genuinely wonderful, and you will never ever find it on Google," and on Marginalia specifically, "search something on Marginalia and you don't get 10 companies trying to sell you the answer." [@cyb_detective](https://x.com/cyb_detective/status/2084199066326512107) lists the working set the same way - Marginalia, Wiby, Million Short, Search My Site, Mwmbl, Mojeek - under "6 search engines that find the internet that Google forgot." Meanwhile the ambient Google complaints on [Hacker News](https://news.ycombinator.com/item?id=49142458) are about the product decaying rather than about alternatives: the time filter breaking, the classic Search button disappearing from an AI-first homepage, CAPTCHAs on search.

KEY PATTERNS from the research:
1. Owning a crawler and owning a brand are different things, and only Brave, Mojeek, Marginalia, Mwmbl and a handful of others clear the first bar, per [SearchEngines.Net](https://www.searchengines.net/guides/search-engines-other-than-google/)
2. Index scale spans two orders of magnitude among "independents" - roughly 300M documents for Marginalia against 9B for Mojeek and 30B for Brave
3. The Bing API retirement on 11 August 2025 is the event that made independent crawling commercially rational, by deleting the cheap alternative
4. Agent demand, not consumer search, is what is funding new indexes now - Parallel at $100M and Brave's LLM Context API
5. The court-ordered path to Google's index is stuck in appeals until late 2026 at the earliest, so it is not a 2026 option for anyone building today
6. Marginalia explicitly is not trying to replace Google, per [mwmbl's own README](https://github.com/mwmbl/mwmbl) drawing the distinction

---
✅ All agents reported back!
├─ 🟠 Reddit: 28 threads │ 56,196 upvotes │ 3,909 comments
├─ 🔵 X: 17 posts │ 730 likes │ 187 reposts
├─ 🔴 YouTube: 1 video │ 128,920 views │ 1/1 with transcripts
├─ 🟡 HN: 22 storys │ 259 points │ 77 comments
├─ 🌐 Web: 19 pages - searchengines.net, GitHub, cloro.dev, itechguides.com, economicliberties.us, alternativeto.net, serpapi.com, grigio.org
├─ 🗣️ Top voices: @Adelizzle_, @Gunflame345, @cyb_detective │ r/degoogle, r/selfhosted, r/privacy
└─ 📎 Raw results saved to (raw evidence, not committed)
---
