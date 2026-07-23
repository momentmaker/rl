🌐 last30days v3.3.2 · synced 2026-07-23

What I learned:

**The two Chinese open-weight heavyweights are being used for different jobs, not ranked head-to-head** - This month's evidence splits cleanly: Qwen 3.6 is the model people trust as their local workhorse, and DeepSeek V4 is the cheap-and-capable engine people wrap in a pipeline. The blunt community verdict on Qwen came from [@AstraiaAI](https://x.com/AstraiaAI/status/2080148616442675428) (386 likes): "Qwen 3.6 27B is by far, and beyond any doubt, STILL the best open model under 200B parameters right now. Nothing I have tested even comes close, except for its own finetunes." That "STILL" is the tell - it has held the local crown for a while.

**Nobody trusts DeepSeek V4 end-to-end; they orchestrate it** - The most useful thread was ["Deepseek V4 Pro is AMAZING"](https://www.reddit.com/r/DeepSeek/comments/1v2dwel/deepseek_v4_pro_is_amazing/) (403 upvotes, 79 comments), where the praise is immediately qualified: "I find it very cheap however the output sometimes is not so great... I have to rely a lot on skills in order to polish the way I really want." The pattern people actually run is a tiered pipeline, best captured by [u/enterme2](https://www.reddit.com/r/DeepSeek/comments/1v2dwel/deepseek_v4_pro_is_amazing/): "Plan it with v4-pro high, then have the plan reviewed by a stronger model like gpt-5.6 or kimi k3, then use v4-flash max to execute the plan. Saves you a ton while having higher quality output." DeepSeek's value is being the cheap tier in a multi-model workflow, not the single brain.

**Qwen wins the local-on-Apple-Silicon race because the tooling targets it** - The highest-scored item on the Qwen side was [youssofal/MTPLX](https://github.com/youssofal/MTPLX) (1.1K stars): "3x decode TPS increase on Qwen 3.6 27B... Native MTP Speculative Decoding on Apple Silicon with no external drafter," under the banner "run local LLMs on Apple Silicon, around twice as fast." There's even a 16GB-friendly path - [Luke's Dev Lab](https://www.youtube.com/watch?v=DBEd5dpxaNQ) benchmarks a Qwen 3.6 14B A3B variant pruned down from 35B via REAP for smaller Macs. DeepSeek V4's dense/Pro tiers simply ask for more machine.

**The practical gotcha with Qwen is the chat template, not the weights** - A grounded ["I ran Qwen 3.6 locally for 45 days"](https://www.reddit.com/r/LocalLLM/comments/1uyukbe/i_ran_qwen_36_locally_for_45_days_here_are_the/) writeup (297 upvotes, 118 comments) surfaced the real-world snag: "the worse tool calling is because of a few bugs in the standard chat template. On huggingface froggeric has some patched templates. I use those." The comments hammer that your quant version matters as much as the model. And a meta-note from [@jukan05](https://x.com/jukan05/status/2080250710638334372) (258 likes): the flood of Chinese open weights actually reinforces NVIDIA's dominance, since they're trained and shipped optimized for NVIDIA hardware. Open weights are closing the gap on frontier coding models - [@antirez](https://x.com/antirez/status/2080243186497179725) notes even a small specialist like Laguna S2.1 beats DeepSeek V4 Flash on some coding tasks - but the frontier keeps moving.

KEY PATTERNS from the research:
1. Qwen 3.6 27B is the community's "best open model under 200B" - the local default, per [@AstraiaAI](https://x.com/AstraiaAI/status/2080148616442675428)
2. DeepSeek V4 is used as the cheap tier in a plan / review / execute pipeline, not trusted solo, per [r/DeepSeek](https://www.reddit.com/r/DeepSeek/comments/1v2dwel/deepseek_v4_pro_is_amazing/)
3. Qwen wins on Apple Silicon because the speedup tooling (MTP speculative decoding) targets it, per [youssofal/MTPLX](https://github.com/youssofal/MTPLX)
4. Qwen's real-world snag is chat-template tool-calling bugs - use patched templates and mind your quant, per [r/LocalLLM](https://www.reddit.com/r/LocalLLM/comments/1uyukbe/i_ran_qwen_36_locally_for_45_days_here_are_the/)
5. Open weights keep closing in on frontier coding, but specialist models can already beat DeepSeek V4 Flash on narrow tasks, per [@antirez](https://x.com/antirez/status/2080243186497179725)

## Head-to-Head

| Dimension | DeepSeek V4 | Qwen 3.6 |
|---|---|---|
| What it is | Chinese open model, Pro/Flash tiers | Alibaba open model (Apache-2.0), 14B-35B + A3B |
| Community verdict | Cheap and capable but inconsistent | "Best open model under 200B," local favorite |
| Local on a Mac | Heavier; asks for more machine | MTP speculative decoding ~3x on Apple Silicon |
| Coding use | Draft with V4-Pro, execute with V4-Flash | Solid; pruned variants fit 16GB Macs |
| Main gotcha | Output needs skills/prompting to polish | Chat-template tool-calling bugs (patch them) |
| How people run it | Multi-model plan / review / execute pipeline | Quantized locally; the quant version matters |
| Best for | Cheap high-volume with a review step | Strongest single model you can self-host |

Bottom line: choose Qwen 3.6 if you want the strongest self-hostable open model and you run on Apple Silicon - the ecosystem is built around making it fast and small. Choose DeepSeek V4 if you want cheap, capable tokens and you're willing to wrap it in a plan/review/execute pipeline. The emerging stack isn't either/or - people orchestrate DeepSeek as the cheap draft-and-execute tier, hand review to a stronger model, and keep Qwen as the local workhorse.

---
✅ All agents reported back!
├─ 🟠 Reddit: 8 threads │ 2,372 upvotes │ 609 comments
├─ 🔵 X: 9 posts │ 539 likes │ 25 reposts
├─ 🔴 YouTube: 4 videos │ 110,694 views │ 0/4 with transcripts
├─ 🟡 HN: 8 storys │ 85 points │ 36 comments
├─ 🐙 GitHub: 9 items │ 200 reactions │ 114 comments
├─ 🌐 Web: 4 pages - deepseek.com, deepinfra.com, build.nvidia.com, reddit.com
├─ 🗣️ Top voices: @antirez, @jukan05, @Standard_Wealth │ r/DeepSeek, r/SillyTavernAI, r/opencode
└─ 📎 Raw results saved to /private/tmp/rl-raw.o3yHPR/deepseek-v4-raw-dsq.md
---
