🌐 last30days v3.3.2 · synced 2026-06-14

What I learned:

**The front page is a coin flip you load the dice for, not a lottery you win** - Builders who have done it keep repeating the same uncomfortable stat: Show HN posts reach the front page less than 2% of the time, per [Amplify Partners](https://www.amplifypartners.com/blog-posts/what-gets-to-the-front-page-of-hacker-news). The people who beat those odds say it is not luck - it is craft applied to the title, the demo, and the first 90 minutes after posting, per [Indie Hackers](https://www.indiehackers.com/post/my-show-hn-reached-hacker-news-front-page-here-is-how-you-can-do-it-44c73fbdc6).

**Intellectual curiosity is the actual ranking signal, and it favors weird specificity over polish** - The two best-performing map/dataviz posts in the window are not slick dashboards, they are oddly specific obsessions. "Show HN: I am building a map of people who lived in the Roman Empire" pulled 183 points and 43 comments at [new.roman-names.com](https://news.ycombinator.com/), and "Show HN: I made an emergency page for my family" got 105 comments off just 84 points - a comment-to-point ratio that screams "this made people feel something," per [HN](https://news.ycombinator.com/). The HN crowd rewards the thing that gratifies curiosity, not the thing that looks expensive.

**The viral hit is the visualization that hands the audience an argument** - On Reddit, the runaway dataviz of the month was "[OC] Trump's Iran Deal Has Been Imminent for 11 Weeks" at 7,477 upvotes and 198 comments on [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/1u2zbip/oc_trumps_iran_deal_has_been_imminent_for_11_weeks/). The top comment isn't praise - it's "You should do this on how many times Musk said self driving taxis were around the corner" ([u/Jackmc1047](https://www.reddit.com/r/dataisbeautiful/comments/1u2zbip/oc_trumps_iran_deal_has_been_imminent_for_11_weeks/), 986 upvotes). The spread came from people wanting the next chart, not just upvoting this one. A viz that starts a fight in the comments outranks a viz that ends the conversation.

**A surprising number with a clean comparison beats a beautiful map** - The other Reddit monster was "Bots now account for more than half of web traffic, up from 30% nine months ago" - 6,737 upvotes on [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/1u28uap/bots_now_account_for_more_than_half_of_web/), where the top comment is just raw disbelief at the delta: "From 30% to over 50% in less than a year is truly crazy" ([u/JellyBeanWizard2](https://www.reddit.com/r/dataisbeautiful/comments/1u28uap/bots_now_account_for_more_than_half_of_web/), 2,442 upvotes). The shareable unit is the before/after jump, not the chart type.

**Speed is non-negotiable because virality is a traffic weapon aimed at your own server** - The thing builders learn the hard way is that the front page sends a wall of traffic in minutes, and a slow or crashing demo dies before the discussion starts. The web context behind the advice is brutal: 53% of mobile visitors abandon a site that takes over 3 seconds to load, per [Crystallize](https://crystallize.com/blog/frontend-performance-checklist). If your interactive map needs a heavy WebGL warm-up or a 180MB payload, you will lose the wave - the [Hacker News Data Map [180MB]](https://news.ycombinator.com/item?id=42035981) thread is full of people who never got it to render. The masters of the genre, like the [Veritasium](https://www.youtube.com/watch?v=kS-CGkiPetQ) breakdown of why Google Maps is "unreasonably fast" (5.6M views), are implicitly teaching the same lesson: the magic is making something computationally huge feel instant.

KEY PATTERNS from the research:
1. Title factually, never with marketing language - the "<Name> - <what it does>" or "I built X to do Y" format wins, marketing speak is an instant downvote, per [Indie Hackers](https://www.indiehackers.com/post/my-show-hn-reached-hacker-news-front-page-here-is-how-you-can-do-it-44c73fbdc6)
2. Ship a try-it-now live link, not a screenshot or a signup gate - the front page rewards work people can immediately play with, per [Amplify Partners](https://www.amplifypartners.com/blog-posts/what-gets-to-the-front-page-of-hacker-news)
3. Pick a strangely specific obsession over a general dashboard - the Roman Empire map and the family emergency page beat generic "sales dashboard" content cold, per [HN](https://news.ycombinator.com/)
4. Make the chart pick a fight - the top dataviz this month all hand the audience an argument or a shocking delta to react to, per [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/1u2zbip/oc_trumps_iran_deal_has_been_imminent_for_11_weeks/)
5. Optimize for instant load and survive the traffic wave - a slow or 180MB interactive dies before the comments form, per [Crystallize](https://crystallize.com/blog/frontend-performance-checklist)
6. Credit your data and tools and label [OC] - on r/dataisbeautiful it is a hard rule, and on HN the "I did the work" signal is what earns the upvote, per [r/dataisbeautiful](https://en.wikipedia.org/wiki/R/dataisbeautiful)

---
✅ All agents reported back!
├─ 🟠 Reddit: 15 threads │ 21,885 upvotes │ 1,620 comments
├─ 🔵 X: 3 posts │ 145 likes │ 40 reposts
├─ 🔴 YouTube: 1 video │ 5,683,762 views │ 1/1 with transcripts
├─ 🟡 HN: 21 storys │ 862 points │ 351 comments
├─ 🐙 GitHub: 2 items │ 7 comments
├─ 🌐 Web: 6 pages - news.ycombinator.com, safegraph.com, apps.nationalmap.gov, mapsplatform.google.com, thoughtspot.com, anychart.com
├─ 🗣️ Top voices: @marcel_glaeser, @gudanglifehack, @noir_myspecial1 │ r/dataisbeautiful, r/datascience, r/webdev
└─ 📎 Raw results saved to /private/tmp/rl_raw.fdNW7L/what-actually-makes-a-data-visualization-or-interactive-map-project-go-viral-and-reach-the-hacker-news-front-page-according-to-the-people-who-build-and-discuss-them-in-2026-raw-v3.md
---
