🌐 last30days v3.3.2 · synced 2026-06-22

What I learned:

**The numbers are worse than the vibes, and 2026 made them concrete** - The headline figure people keep circulating is from [Pew Research Center](https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/): 38% of pages that existed in 2013 are already gone, and a quarter of everything that existed between 2013 and 2023 no longer resolves. When you check old links, you find rot is not a tail risk - it is the default. [Ahrefs](https://ahrefs.com/blog/link-rot-study/) put the harder ceiling on it: 66.5% of links to sites sampled since January 2013 have rotted. The decay is exponential with age - scholarly web citations drop from ~87% reachable at 0-5 years to 38% past 10 years, per the 2026 LIS-literature study in [Emerald's AJIM](https://www.emerald.com/ajim/article/doi/10.1108/AJIM-05-2025-0286/1335399/Link-rot-in-LIS-literature-a-20-year-study-of-web).

**Citations are the scariest failure surface, and the courts prove it** - This is where "digital dark age" stops being a slogan. Roughly half of the URLs in U.S. Supreme Court opinions no longer reach what they cited, and 70%+ of the URLs in Harvard Law Review have rotted, per [Vice](https://www.vice.com/en/article/the-supreme-court-has-a-serious-problem-with-link-rot/) and the [ABA Journal](https://www.abajournal.com/magazine/article/link_rot_is_degrading_legal_research_and_case_cites). The chilling framing from Harvard's Perma.cc work: without a fix, the information in a judicial citation "will be known solely from those citations" - the source itself is gone. The average webpage lifespan people keep quoting is 44-75 days.

**The Internet Archive moved from "save it yourself" to "fix it automatically" in February 2026** - The biggest 2026 development is the [Automattic + Internet Archive Link Fixer](https://tech.slashdot.org/story/26/02/05/1729259/automattic-and-the-internet-archive-team-up-to-fight-link-rot), a free open-source WordPress plugin that detects broken outbound links and silently redirects readers to the Wayback Machine copy, requesting a fresh snapshot when none exists. On Wikipedia the [WP:IABOT](https://en.wikipedia.org/wiki/Wikipedia:Link_rot) bot already does this at scale - continuously scanning articles, archiving live links pre-emptively, and swapping dead ones for archived versions. The pattern is the same: stop relying on humans to remember to archive.

**Archivists' actual anxiety right now is cost, not apathy** - The most-engaged community thread in the window was [r/DataHoarder](https://www.reddit.com/r/DataHoarder/comments/1tmwbzk/the_prices_are_killing_data_hoarding/) - "The prices are killing data hoarding" - at 1,454 upvotes and 353 comments. The people who would actually preserve the web are getting priced out of the drives to do it. Meanwhile a [r/internetarchive](https://www.reddit.com/r/internetarchive/comments/1tvleg9/journalist_looking_for_explanation_regarding/) thread shows journalists now treating Wayback Machine captures as primary evidence, which raises the stakes when X and other platforms actively block archiving.

**What people actually do about it: self-host and own the bytes** - The recurring practitioner answer is [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) - open-source, self-hosted, saves redundant HTML/PDF/PNG/WARC/SQLite snapshots from your bookmarks, browser history, RSS, and social feeds, and runs on anything from a Raspberry Pi to a laptop with data staying 100% local. The throughline from the data-hoarder crowd is distrust of any single point of failure (including the Internet Archive itself), so the move is personal redundancy plus Perma.cc-style permalinks for anything that has to survive a citation.

KEY PATTERNS from the research:
1. Rot is exponential with age, not linear - reachability collapses past the 10-year mark, per [Emerald AJIM](https://www.emerald.com/ajim/article/doi/10.1108/AJIM-05-2025-0286/1335399/Link-rot-in-LIS-literature-a-20-year-study-of-web)
2. Citations are the highest-stakes casualty - ~50% of Supreme Court URLs and 70%+ of Harvard Law Review URLs are dead, per [ABA Journal](https://www.abajournal.com/magazine/article/link_rot_is_degrading_legal_research_and_case_cites)
3. The 2026 fix is automated redirect-to-archive, not manual saving - per the [Automattic + Internet Archive Link Fixer](https://tech.slashdot.org/story/26/02/05/1729259/automattic-and-the-internet-archive-team-up-to-fight-link-rot)
4. Wikipedia already operationalized pre-emptive archiving via [WP:IABOT](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
5. Storage cost is the real bottleneck for grassroots preservation, per [r/DataHoarder](https://www.reddit.com/r/DataHoarder/comments/1tmwbzk/the_prices_are_killing_data_hoarding/)
6. Self-hosting with [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) plus Perma.cc permalinks is the practitioner answer to single-point-of-failure risk

---
✅ All agents reported back!
├─ 🟠 Reddit: 7 threads │ 1,681 upvotes │ 393 comments
├─ 🔵 X: 14 posts │ 4,301 likes │ 1,062 reposts
├─ 🐙 GitHub: 7 items │ 5 reactions │ 706 comments
├─ 🌐 Web: pages - pewresearch.org, ahrefs.com, emerald.com, abajournal.com, tech.slashdot.org, en.wikipedia.org
├─ 🗣️ Top voices: @Liz_Wheeler, @hydroterpz421a, @simonvhardy │ r/internetarchive, r/DataHoarder, r/internetarchive
└─ 📎 Raw results saved to (raw evidence, not committed)
