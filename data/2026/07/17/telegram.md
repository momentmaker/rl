---
ready: true
---
🎲 *Random Learning — 2026-07-17*

Three things I dug into today, from a coding hack to a plain-text notes revolt to a 1,400-year-old company.

*1. Running Claude Code on cheaper (and local) models — does BYO-model actually work?*
The trick is dull and universal: coding CLIs speak the Anthropic API, so you point `ANTHROPIC_BASE_URL` at a compatible endpoint (DeepSeek, Qwen, MiniMax, a local Ollama model) and the same agent loop drives a different brain. The pitch is always "as good as Sonnet" and the numbers are the draw — "99% cheaper," free daily run quotas, $100/mo workflows for ~$0. Reality check: it's a lateral move for routine work, local inference is slow on consumer hardware, and cheap models wobble most on agentic tool-use. The honest community wisdom: "in about a week there's a better setup." The next frontier is per-subagent routing — spend premium tokens only where they earn it.

*2. "Files over apps": the plain-markdown notes revival*
Karpathy posted a bare folder structure and pulled 16M views — because a folder of `.md` files is something you can grep, diff, back up, and still open in 30 years. The escape ladder is Notion → Obsidian → plain markdown, each step shedding lock-in. The 2026 accelerant is AI: a markdown folder is the most agent-legible store there is, so people now wire agents at their vaults as a read/write "brain," and new tools launch "AI-first" against plain files. The trade is real — you lose graph view, backlinks, mobile polish; you gain grep, git history, and a format no company can deprecate.

*3. Kongo Gumi and the world's oldest companies*
A temple-building firm founded in 578 AD (to build Osaka's Shitennō-ji) ran ~1,400 years — ending not in collapse but in a 2006 acquisition. The real surprise: Japan holds most of the planet's centuries-old firms, called *shinise* and treated as national treasures, against a <20-year global company lifespan. The playbook is anti-growth: one durable craft, conservative finance, continuity over expansion, and deliberate succession via adult adoption (*mukoyoshi*) so the house outlives any heir. The shadow: Kongo Gumi fell after straying into bubble-era real-estate debt — the mirror image of the three-generation rule that kills most family businesses.

_Sources: last30days across HN, Reddit, X, YouTube + web grounding._
