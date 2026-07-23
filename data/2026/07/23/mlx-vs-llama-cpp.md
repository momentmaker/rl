🌐 last30days v3.3.2 · synced 2026-07-23

What I learned:

**The 30-day story is MLX pulling ahead on the Mac while llama.cpp stays the "runs everywhere" default** - The engine resolved this as a clean two-way split. [llama.cpp](https://github.com/ggml-org/llama.cpp) is the incumbent by a mile - 121K stars, 1,914 open issues, and a stated goal of "LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware." MLX is the Apple-Silicon-native challenger, and the sharpest framing came from an [r/MacStudio thread on MLX-Serve](https://www.reddit.com/r/MacStudio/comments/1uy2id9/new_updates_to_mlxserve_its_really_fast_now_with/) (93 upvotes, 26 comments) where a commenter nails the tradeoff: "llama.cpp is simply optimized for Cuda/Nvidia, and not much you can do about it - llama.cpp is about compatibility across architectures, OS's, GPU's." That's the whole comparison in one line: portability vs peak-Apple speed.

**MLX's momentum this month is the ecosystem, not just the core** - The activity clustering around MLX is people building fast Apple-Silicon tools on top of it. [@ivanfioravanti](https://x.com/ivanfioravanti/status/2080263269512585272) shipped a Mage-Flow PR for mflux (image gen "Powered by Apple MLX") clocking 1024x1024 generation at ~1.6s on an M5 Max and ~2.7s on an M3 Ultra, using ~18-20GB. The recurring theme is "twice as fast on Apple Silicon" - the same pitch behind MTP speculative-decoding projects in the MLX orbit. MLX's rough edge is model coverage: an [LM Studio mlx-engine bug](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/2102) shows a new MoE-vision model type failing to load, the kind of gap you rarely hit with llama.cpp's broad format support.

**llama.cpp's edge is quantization tooling and the fact that it runs on the hardware you don't own yet** - The freshest llama.cpp-adjacent project is [TheTom/llama-cpp-turboquant](https://github.com/TheTom/llama-cpp-turboquant) (2.2K stars), pitching "production-grade KV-cache and weight quantization for llama.cpp, with cross-backend kernel support for Apple Silicon, NVIDIA CUDA, AMD ROCm, and Vulkan." That cross-backend reach is exactly why people keep it around even when MLX is faster on their Mac - the same engine covers the CUDA box, the ROCm rig, and prebuilt setups like [ai-dock/llama.cpp-cuda](https://github.com/ai-dock/llama.cpp-cuda).

**A wildcard is appearing: third-party runtimes claiming to beat both** - A small HN post, ["6.4x faster than llama.cpp, 3.9x faster than MLX"](https://www.basecompute.co/getbasert), is the early signal that the two-horse race may not stay a two-horse race - purpose-built inference runtimes are starting to benchmark against both incumbents at once. It's low-engagement so far (4 points), so treat it as a straw in the wind, not a verdict.

KEY PATTERNS from the research:
1. Portability vs peak-Apple is the real axis - llama.cpp runs on "architectures, OS's, GPU's," MLX squeezes the Mac, per [r/MacStudio](https://www.reddit.com/r/MacStudio/comments/1uy2id9/new_updates_to_mlxserve_its_really_fast_now_with/)
2. MLX's momentum is the tool ecosystem (mflux, MLX-Serve, MTP decoding) more than the core framework, per [@ivanfioravanti](https://x.com/ivanfioravanti/status/2080263269512585272)
3. llama.cpp's staying power is quantization + cross-backend reach, per [TheTom/llama-cpp-turboquant](https://github.com/TheTom/llama-cpp-turboquant)
4. MLX still trails on model coverage - new model types can fail to load, per the [LM Studio mlx-engine bug](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/2102)
5. Watch for third-party runtimes benchmarking against both at once, per [basert on HN](https://www.basecompute.co/getbasert)

## Head-to-Head

| Dimension | MLX | llama.cpp |
|---|---|---|
| What it is | Apple-Silicon-native array + serving stack | C/C++ inference engine, runs almost anywhere |
| GitHub footprint | Ecosystem repos (mflux, MLX-Serve, MTP) | 121K stars, 1,914 open issues on ggml-org |
| Philosophy | Peak performance on Apple GPU/ANE | Compatibility across arch, OS, and GPU |
| Hardware | Apple Silicon only | CUDA, ROCm, Vulkan, Metal, CPU |
| Speed on Mac | Fastest local path; ~2x claims common | Runs well, but tuned for CUDA not peak Apple |
| Quantization | Growing MLX quants | TurboQuant+ KV-cache/weight, cross-backend |
| Rough edges | New model types can fail to load | Broad but 1,900+ open issues |
| Best for | Mac-only users chasing tokens/sec | One engine spanning Mac + NVIDIA + more |

Bottom line: choose MLX if you live entirely on Apple Silicon and want the fastest local tokens with a growing tool ecosystem around it. Choose llama.cpp if you need a single engine that also targets NVIDIA/AMD and values format breadth over peak-Mac speed. The emerging stack is both at once - llama.cpp as the portable baseline, MLX-based serving on the Mac for speed - while newcomers like basert start benchmarking against both.

---
✅ All agents reported back!
├─ 🟠 Reddit: 2 threads │ 190 upvotes │ 41 comments
├─ 🔵 X: 14 posts │ 70 likes │ 3 reposts
├─ 🔴 YouTube: 9 videos │ 34,647,426 views │ 6/9 with transcripts
├─ 🟡 HN: 6 storys │ 22 points │ 2 comments
├─ 🐙 GitHub: 1 item │ 8 reactions │ 3 comments
├─ 🌐 Web: 5 pages - GitHub, huggingface.co, f22labs.com, XDA
├─ 🗣️ Top voices: @ivanfioravanti, @satanworker, @Nekt_0 │ r/MacStudio, r/oMLX
└─ 📎 Raw results saved to /private/tmp/rl-raw.o3yHPR/mlx-raw-mlx.md
---
