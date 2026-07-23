---
ready: true
---
🎲 *Random Learning — 2026-07-23*

Three things I dug into today, all from the "what can I actually run on my own hardware" rabbit hole: the two engines for local LLMs on a Mac, the two Chinese open models everyone self-hosts, and the framework fight underneath every site you build.

*1. MLX vs llama.cpp — the local-inference split*
The community frames it as one clean tradeoff: portability vs peak-Apple speed. `llama.cpp` is the incumbent (121K stars) whose whole point is "compatibility across architectures, OS's, GPU's" — it runs on your Mac, your NVIDIA box, and hardware you don't own yet. MLX is Apple-Silicon-native and increasingly the *fast* path on a Mac, with a booming tool ecosystem around it (mflux image gen, MLX-Serve, MTP speculative decoding all clocking "~2x faster on Apple Silicon"). MLX's rough edge is model coverage — new model types can still fail to load — while llama.cpp's edge is quantization tooling (TurboQuant+) and cross-backend reach. Emerging move: keep llama.cpp as the portable baseline, switch to MLX-based serving on the Mac for speed. Watch for third-party runtimes (e.g. "basert") starting to benchmark against *both* at once.

*2. DeepSeek V4 vs Qwen 3.6 — different jobs, not a ranking*
Qwen 3.6 27B is the crowd's "best open model under 200B parameters, and nothing comes close" — the local workhorse. It wins on Apple Silicon because the speedup tooling targets it (MTPLX gets ~3x decode on a 27B), and there are pruned 14B variants that fit a 16GB Mac. Its real-world snag isn't the weights, it's the chat template — tool-calling breaks until you swap in patched templates, and your quant version matters as much as the model. DeepSeek V4, by contrast, nobody trusts end-to-end: it's "very cheap but the output sometimes isn't great," so people run it as the cheap tier in a pipeline — *plan with V4-Pro, have a stronger model review, execute with V4-Flash*. Open weights keep closing in on frontier coding (a small specialist, Laguna S2.1, already beats DeepSeek V4 Flash on some coding tasks), though one sharp take notes the flood of Chinese open models actually *reinforces* NVIDIA's dominance, since they're trained and shipped optimized for NVIDIA.

*3. Astro vs Next.js — and the "Next.js without Vercel" opening*
Next.js is still the gravitational center (141K stars, now v16 LTS), but the freshest energy is about escaping its orbit. The standout release this month was Cloudflare's `vinext` — "a Vite plugin that reimplements the Next.js API surface" so you can run Next.js on Workers and "deploy anywhere," announced as "how we rebuilt Next.js with AI in one week." The recurring knock even fans admit: version churn ("they rename half the features, break the other half"). Astro 7.0 also shipped, holding its HTML-first, ship-minimal-JS lane — the natural pick when a full React app is more than you need. The 2026 consensus isn't one winner: Astro for content/docs/marketing, Next.js for the app-shaped, data-heavy surface, with vinext opening a path off the Vercel rails.

_Sources: last30days across HN, Reddit, X, YouTube, GitHub + web grounding._
