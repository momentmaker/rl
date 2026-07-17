🌐 last30days v3.3.2 · synced 2026-07-17

What I learned:

**The "files over apps" idea — keep your notes as plain markdown in a folder you own, not trapped in an app's database — has gone from niche principle to viral aesthetic.** The clearest signal is a post about how [Karpathy Posted a Folder Structure and Got 16 Million Views](https://x.com/neil_xbt/status/2069968385182486703): a stripped-down directory of plain files, no app, presented as a whole knowledge system, pulling enormous engagement. The appeal is exactly its boringness — a folder of `.md` files is something you can grep, diff, back up, sync with anything, and still open in thirty years. The movement's whole thesis is that the file, not the app, is the durable unit, and everything fancier is a renderer you should be able to walk away from.

**Obsidian was the original "own your files" darling — and now it's the incumbent people are leaving for something even simpler.** [XDA's widely-shared piece](https://www.xda-developers.com/favorite-alternative-to-notion-isnt-obsidian-anymore-something-simpler-and-efficient/) captures the arc in its title: "My favorite alternative to Notion isn't Obsidian anymore, it's something simpler and more efficient." The pattern is a ladder of escape — people flee Notion's cloud lock-in for Obsidian's local vault, then flee Obsidian's plugin sprawl and proprietary flavor of markdown for a plain folder plus a text editor. Each step trades features for fewer moving parts and more certainty that the data outlives the tool.

**The 2026 accelerant is AI: a folder of markdown is the most agent-legible knowledge store there is, so notes are being reframed as an agent's memory rather than a human's filing cabinet.** People are wiring coding agents directly at their vaults — one widely-liked example is a [`/goal` to "build a mature, source-backed Obsidian vault brain"](https://x.com/nickvasiles/status/2068828549000413510), a local vault an agent can read and extend on its own. And new tools are being built AI-first from the start: the [Show HN for OpenKnowledge](https://github.com/inkeep/open-knowledge) (381 points) pitches itself explicitly as an "open source AI-first alternative to Obsidian/Notion." Plain text wins here for the same reason it wins for humans — no proprietary schema an LLM has to reverse-engineer, just files it can read and write.

**What you actually give up is real, which is why this is a genuine trade rather than a free upgrade.** Leaving Obsidian/Notion means losing the graph view, first-class backlinks, polished mobile apps, rich embeds, and the plugin ecosystem. What you get back is grep, git history, provider-agnostic sync, zero lock-in, and a format no company can deprecate out from under you. The people making the switch are explicitly optimizing for ownership and longevity over features — betting that "I can always read this" matters more than "it does everything," especially once an AI can supply the search and linking the app used to.

**Underneath the tool churn, the constant is a preference for the lowest-tech format that still does the job.** Plain markdown keeps winning not because it's powerful but because it's inert: it doesn't rot, doesn't phone home, doesn't need a subscription, and doesn't care which editor or model touches it next. The recurring lesson across every thread is that the exciting layer (apps, AI, sync) should be disposable and swappable, while the notes themselves stay dumb, plain, and yours.

KEY PATTERNS from the research:
1. "Files over apps" went mainstream — a plain folder-of-files knowledge setup pulled 16M views, per [@neil_xbt](https://x.com/neil_xbt/status/2069968385182486703)
2. The escape ladder is Notion → Obsidian → plain markdown, each step shedding lock-in, per [XDA](https://www.xda-developers.com/favorite-alternative-to-notion-isnt-obsidian-anymore-something-simpler-and-efficient/)
3. AI is reframing notes as agent memory — vaults as "brains" agents read and extend, per [@nickvasiles](https://x.com/nickvasiles/status/2068828549000413510)
4. New tools are being built AI-first against markdown, e.g. [OpenKnowledge](https://github.com/inkeep/open-knowledge)
5. The real trade is features (graph, backlinks, mobile) for ownership (grep, git, no lock-in) — plain text wins on durability

---
✅ All agents reported back!
├─ 🔵 X: 20 posts │ 540 likes │ 54 reposts
├─ 🟡 HN: 9 storys │ 423 points │ 178 comments
├─ 🐙 GitHub: 1 item │ 1 comments
├─ 🌐 Web: 3 pages - XDA, lindy.ai, Medium
└─ 🗣️ Top voices: @JulianGoldieSEO, @typakon4, @k2sbhai
---

I'm now an expert on the files-over-apps notes movement. Some things I can help with:
- Design a plain-markdown notes setup (folder structure, git, sync) that stays readable for decades and survives any app going away
- Wire an AI agent at a markdown vault as a read/write "brain" — and where that actually helps vs. adds noise
- Weigh the honest trade-offs of leaving Obsidian or Notion (what you lose: graph, backlinks, mobile; what you gain: grep, ownership, portability)
