🌐 last30days v3.3.2 · synced 2026-06-20

What I learned:

**The quality gap with ElevenLabs is basically closed - the production gap isn't** - That framing comes straight from [@RealSoohyunBae](https://x.com/RealSoohyunBae/status/2067625852662423919) announcing Zyphra's ZONOS2 (8B params, Apache 2.0, MoE): "The quality gap is closing. The production gap isn't." That is the consensus of the month - on raw naturalness the open models have caught up, but the cloud advantage is now infrastructure (uptime, scaling, support), not voice quality.

**Kokoro is the model people actually run when they just want it to work** - At 82M params it's the efficiency champion: under 2GB VRAM, runs on an RTX 3060 or even CPU, around 210x realtime (roughly 40x faster than ElevenLabs), and it hit #1 on TTS Arena, per [TextToLab](https://texttolab.com/blog/kokoro-tts-review). The catch everyone repeats: no voice cloning, just ~54 fixed voicepacks. It's the most-deployed self-hosted option - there's an [OpenAI-compatible Docker image](https://github.com/hwdsl2/docker-kokoro/) (50+ voices, 9 languages, streaming, offline) and it carries 7.6K stars on [hexgrad/kokoro](https://github.com/hexgrad/kokoro).

**Chatterbox is the one that made people stop saying "ElevenLabs is unbeatable"** - Resemble AI's Chatterbox wins blind A/B tests against ElevenLabs Turbo 63.75%-65.3% of the time on identical samples, per [FindSkill.ai](https://findskill.ai/blog/best-open-source-tts-2026/). Chatterbox-Turbo hits sub-150ms (around 75ms) time-to-first-sound versus ElevenLabs' ~2.38s average, clones from ~5 seconds of audio, is MIT-licensed, and does zero-shot cloning across 23 languages, per [GenMediaLab](https://www.genmedialab.com/comparisons/elevenlabs-vs-chatterbox-tts/). On r/LocalLLaMA it's now treated as a serious top-3 contender alongside CosyVoice2.

**Fish Speech is the cloning/multilingual pick that actually tops the blind leaderboard** - Fish Audio S1 holds #1 on TTS-Arena2 ahead of ElevenLabs on naturalness, and the hosted API runs ~$15 per 1M characters vs ElevenLabs' ~$165, per [Ringly](https://www.ringly.io/blog/elevenlabs-alternatives). The open-weights Fish Speech (1.6 / S2) is self-hostable for free if you have a GPU, with 80+ language coverage - it's the go-to when you need cloning plus breadth rather than Kokoro's fixed voices.

**Orpheus and Qwen3-TTS are the "build your stack on it" foundations** - Orpheus (Canopy Labs, LLaMA-3B based, 6.2K stars on [canopyai/Orpheus-TTS](https://github.com/canopyai/Orpheus-TTS)) ships in multiple sizes (3B down to 150M) for org-wide deployment, and Alibaba's [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) is the highest-star repo of the bunch at 12K, cited for highest-fidelity cloning. A handy field guide from [CrispASR](https://github.com/CrispStrobe/CrispASR) sums up the role split the community uses: "Kokoro (smallest), Qwen3-TTS (highest fidelity, voice cloning), VibeVoice (lowest-latency streaming), Orpheus (3B Llama + SNAC), Chatterbox (flow-matching + HiFT vocoder)."

**"Vibes" still beat benchmarks, and long-form is where local breaks** - [@kwindla](https://x.com/kwindla/status/2067265653250097617) captured the eval problem: metrics like time-to-first-audio and missing words matter, "but more than any other technology I've ever worked with, people make voice decisions based on 'vibes' that are hard (maybe impossible) to quantify" (he flags Vapi's new "Humanness Index"). Meanwhile r/speechtech's ["Local TTS for long-form audio"](https://www.reddit.com/r/speechtech/comments/1u4jifr/local_tts_for_longform_audio_voice_quality_is_not/) thread is a reminder that voice quality isn't the only hard part - chunking, prosody drift, and pacing over long passages are the real local-deployment pain.

KEY PATTERNS from the research:
1. Pick by job, not by "best": Kokoro for speed/cheap with fixed voices, Chatterbox for low-latency cloning on a gaming GPU, Fish Speech for multilingual cloning quality - per [CrispASR](https://github.com/CrispStrobe/CrispASR)
2. On head-to-head blind tests, open models now win: Chatterbox 63-65% over ElevenLabs Turbo, Fish Audio S1 #1 on TTS-Arena2 - per [FindSkill.ai](https://findskill.ai/blog/best-open-source-tts-2026/)
3. Latency favors local: Chatterbox ~75-150ms first-sound vs ElevenLabs ~2.38s - per [GenMediaLab](https://www.genmedialab.com/comparisons/elevenlabs-vs-chatterbox-tts/)
4. The remaining ElevenLabs moat is production infra and reliability, not naturalness - per [@RealSoohyunBae](https://x.com/RealSoohyunBae/status/2067625852662423919)
5. Cost is the loud indie-builder driver: "Stop paying $0.01+ per second for ElevenLabs," self-host XTTS-v2/Coqui and clone in 6s - per [@boshigao2016](https://x.com/boshigao2016/status/2059996211252482428)
6. Long-form local TTS still struggles past raw voice quality (pacing, chunking, prosody) - per [r/speechtech](https://www.reddit.com/r/speechtech/comments/1u4jifr/local_tts_for_longform_audio_voice_quality_is_not/)

---
✅ All agents reported back!
├─ 🟠 Reddit: 13 threads │ 5,081 upvotes │ 893 comments
├─ 🔵 X: 6 posts │ 79 likes │ 11 reposts
├─ 🐙 GitHub: 3 items │ 25,803 reactions │ 365 comments
├─ 🌐 Web: 16 pages - GitHub, ringly.io, ai-box.eu, aitoolanalysis.com, elevenlabs.io, reddit.com, codesota.com, assemblyai.com
├─ 🗣️ Top voices: @RealSoohyunBae, @kwindla, @boshigao2016 │ r/LocalLLaMA, r/speechtech, r/MachineLearning
└─ 📎 Raw results saved to (raw evidence, not committed)
---
