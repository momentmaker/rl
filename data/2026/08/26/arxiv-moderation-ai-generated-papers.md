---
title: "What arXiv's AI moderation rules catch, and what still gets through"
date: 2026/08/26
tags: [arxiv, moderation, ai-generated, peer-review, academia, preprints, research-integrity]
---

🌐 last30days v3.3.2 · synced 2026-08-26

What I learned:

**The policy is settled and the argument has moved to enforcement** - the rules themselves stopped being news. arXiv no longer accepts computer-science review articles and position papers that have not been vetted by a journal or conference, per the [arXiv entry on Wikipedia](https://en.wikipedia.org/wiki/ArXiv), and separately runs a one-year submission ban for manuscripts containing unchecked AI-generated content - hallucinated citations, leftover chatbot instructions - described in the [Issues in Science and Technology](https://issues.org/artificial-intelligence-ai-scientific-discovery-aiken-batalis-tananbaum-forum/) forum on AI slop as "a strict one-year ban for authors of manuscripts containing unchecked AI-generated content." What researchers are actually arguing about in this window is whether any of it can be enforced. [Inside Higher Ed](https://www.insidehighered.com/news/faculty/books-publishing/2026/05/22/ban-authors-who-submit-ai-content-welcome-unenforceable) put the academic verdict in its headline: welcome but unenforceable.

**The measured leak rate is the number that undercuts the whole scheme** - a large-scale citation study on arXiv itself ([arXiv:2605.07723](https://arxiv.org/pdf/2605.07723)) estimates that 78.8% of non-existent citations pass moderation and appear on the platform anyway. Screened manuscripts do disproportionately contain hallucinated citations, so the filter is catching something real - but the majority of hallucinated content still enters the scholarly record. That is the gap between a policy that reads as decisive and a pipeline that is still mostly porous.

**The clearest picture of who gets caught is a git commit, not a press release** - the sharpest artifact in the whole 30-day corpus is a pull request titled ["Update publication plan after arXiv decline; prep Zenodo deposit"](https://github.com/mavaali/agentic-trust-protocol/pull/5), which states plainly: "arXiv declined the paper on 2026-08-18 (moderation, MOD-100537), with an account-level restriction requiring a journal reference/DOI for future submissions." That is the mechanism working end to end on a named date with a ticket number - and the consequence is not just a rejected paper but an account-level gate, with the author rerouting to Zenodo. It is the only first-person record of the penalty landing that surfaced anywhere in the window, and it lives in a repo, not a forum.

**Researchers are angrier about detection than about the ban** - the loudest academic thread of the month is not about arXiv at all. On [r/academia](https://www.reddit.com/r/academia/comments/1vl2vew/i_am_done_with_pangram_and_every_other_ai/), "I am DONE with Pangram and every other 'AI detector' - I'm just a good writer, and that's apparently a crime now" pulled 209 upvotes and 59 comments. The complaint is false positives on human writing, which is precisely the failure mode arXiv's own design tries to avoid - the [arXiv moderation appeals process](https://info.arxiv.org/help/moderation/appeals.html) routes through a moderator flagging, a section chair confirming, and an appeal being available, rather than through a classifier score. The community fear and the actual policy are pointed in different directions.

**AI showing up on the reviewer's side of the desk is the complaint with no policy attached** - [r/academia](https://www.reddit.com/r/academia/comments/1vo0kum/an_ai_reviewed_my_paper_the_editor_told_me_to/) ran "An AI 'reviewed' my paper. The editor told me to suck it up. Should I retaliate?" at 69 upvotes and 33 comments, and [r/MachineLearning](https://www.reddit.com/r/MachineLearning/comments/1v90r9r/neurips_2026_reviewer_aigenerated_rebuttals_and/) ran "NeurIPS 2026 Reviewer: AI-Generated Rebuttals (and Paper)" at 119 upvotes and 56 comments. arXiv can ban a submitter; nobody in this window has a lever for a reviewer or an editor. The corpus also surfaces the escalation already in flight: ["Hidden Prompts in Manuscripts Exploit AI-Assisted Peer Review"](https://arxiv.org/abs/2507.06185), authors embedding instructions aimed at the LLM reading their paper.

**The hardest line came from a mathematician, not from arXiv** - [@rperezmarco](https://x.com/rperezmarco/status/2088374500005998679) drew the most engagement of any X post in the window with a maximalist position: "no one should sign a paper that he hasn't written himself and understood... @arxiv should ban computer generated papers. Do the work, understand the math, write your paper, disclose the AI contribution and then you earn your credit for authorship. If you don't do it, you are just a button pusher that only deserves credit for pushing a button." That is a much broader rule than arXiv's - arXiv bans *unchecked* output, not generated output - and the gap between the two is the actual live disagreement.

**Mathematics is where the abolitionist case is being written, and it is not the case anyone is reading** - [Max Weinreich's "The crisis of AI-generated mathematics"](https://arxiv.org/abs/2608.02859) reached Hacker News on 22 August arguing for total opposition to AI use in mathematics, with proposals for departments, journals and institutions to act together. It drew 10 points and 2 comments. Three days earlier [Terence Tao's "Mathematics in the age of AI"](https://arxiv.org/abs/2608.16753) drew 210 points and 269 comments - the single biggest discussion in the corpus, and twenty times the abolitionist essay's reception. Neither is an arXiv policy document; both are being hosted by arXiv while it decides how much of this it wants to carry.

**arXiv is not the only preprint server tightening, and it is not the strictest** - per [Editage's 2026 preprint guide](https://www.editage.com/blog/what-is-a-preprint/), the generalist preprint service hosted by OSF stopped accepting new submissions entirely in August 2025 citing quality of incoming work, and PsyArXiv switched from moderating after posting to moderating before posting. Meanwhile the [QIP 2027 call for submissions](https://qipconference.org/2027/call/) now explicitly builds in a "moderation-delay case," warning authors that they are responsible for allowing enough time for a preprint to become publicly available - conference deadlines are now being written around arXiv's queue, which [arXiv itself](https://arxiv.org/localtime) says runs one to four days and sometimes longer.

KEY PATTERNS from the research:
1. The rules are no longer contested; enforceability is - per [Inside Higher Ed](https://www.insidehighered.com/news/faculty/books-publishing/2026/05/22/ban-authors-who-submit-ai-content-welcome-unenforceable)
2. 78.8% of non-existent citations still pass moderation, so screening is a filter and not a gate - per [arXiv:2605.07723](https://arxiv.org/pdf/2605.07723)
3. The only first-person evidence of a penalty landing is a GitHub PR with a moderation ticket number and an account-level restriction - per [mavaali/agentic-trust-protocol](https://github.com/mavaali/agentic-trust-protocol/pull/5)
4. Researcher anger is aimed at AI detectors and false positives, not at arXiv's human-in-the-loop process - per [r/academia](https://www.reddit.com/r/academia/comments/1vl2vew/i_am_done_with_pangram_and_every_other_ai/)
5. AI on the reviewer side has no policy attached anywhere in the window, and prompt-injection into peer review is already documented - per [r/MachineLearning](https://www.reddit.com/r/MachineLearning/comments/1v90r9r/neurips_2026_reviewer_aigenerated_rebuttals_and/)
6. The loudest voices want a broader ban than arXiv wrote - generated versus merely unchecked - per [@rperezmarco](https://x.com/rperezmarco/status/2088374500005998679)
7. The abolitionist position is being published but not read: 10 points for Weinreich against 210 for Tao's measured essay three days earlier
8. Conference organisers are now writing arXiv's moderation delay into their submission rules - per [QIP 2027](https://qipconference.org/2027/call/)

---
✅ All agents reported back!
├─ 🟠 Reddit: 7 threads │ 2,570 upvotes │ 233 comments
├─ 🔵 X: 5 posts │ 55 likes │ 5 reposts
├─ 🔴 YouTube: 6 videos │ 9,291,463 views │ 3/6 with transcripts
├─ 🟡 HN: 13 storys │ 694 points │ 620 comments
├─ 🐙 GitHub: 19 items │ 12 reactions │ 236 comments
├─ 🌐 Web: 13 pages - en.wikipedia.org, issues.org, qipconference.org, arxiv.org, casrai.org, editage.com, stingrai.io
├─ 🗣️ Top voices: @weweweai, @rperezmarco, @newcryptospace │ r/academia, r/MachineLearning, r/PhD
└─ 📎 Raw results saved to (raw evidence, not committed)
---
