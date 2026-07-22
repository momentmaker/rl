🌐 last30days v3.3.2 · synced 2026-07-22

Note on evidence: the engine's live Reddit search was rate-blocked (403) this run, so the on-topic STT threads did not surface directly - the Reddit items that came through are broader r/LocalLLaMA "why we need local models" discussion, not model-specific. The highest-signal evidence here is GitHub project-mode data (live star counts) plus the WebSearch benchmark supplements. Treat the model-vs-model specifics below as sourced from those, not from a rich social debate.

What I learned:

**The 2026 consensus is "pick by job," not "one winner"** - Across every benchmark roundup people converge on the same split: Parakeet for English accuracy and speed, Moonshine for the smallest edge footprint and lowest latency, Whisper only when you need multilingual. [Northflank](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks) puts Parakeet TDT 0.6B v3 at 6.32% average WER, edging Whisper large-v3's 7.44% on the Open ASR Leaderboard - but with the caveat that Parakeet covers only ~25 European languages, so Mandarin/Japanese/Hindi/Arabic still send you back to Whisper per [onResonant](https://www.onresonant.com/resources/local-stt-models-2026).

**Moonshine's pitch is latency, and the numbers are the selling point** - Moonshine's own repo is now at 10K stars with only 8 open issues, described as "very low latency speech to text, intent recognition, and text to speech, for building voice agents." The load-bearing stat people cite: Moonshine Medium hits ~107ms vs Whisper Large V3's ~11,286ms on a MacBook Pro - roughly 100x faster - at 245M params (6x smaller than Whisper) while beating it on English WER, per [modelslab](https://modelslab.com/blog/audio-generation/moonshine-vs-whisper-asr-real-time-speech-2026). The [Moonshine v2 paper](https://arxiv.org/abs/2602.12241) explains the trick: an "ergodic streaming encoder" that processes exactly the audio you give it (no zero-padding), so a 3-second phrase only runs 3 seconds of compute. [Pete Warden](https://petewarden.com/2026/02/13/announcing-moonshine-voice/) frames the whole point as CPU-only on-device - no NPU/GPU dependency, prebuilt for iOS/Android/macOS/Windows/Linux and Raspberry Pi.

**Parakeet has quietly become the default local Mac dictation engine** - The story people tell in 2026 is that three engines now dominate Mac dictation - Whisper, NVIDIA Parakeet, and Apple's own SpeechAnalyzer, per [Spokenly](https://spokenly.app/blog/speech-to-text-mac). Parakeet's edge is running at ~80ms latency locally via FluidAudio CoreML on the Apple Neural Engine, per [Dictato](https://dicta.to/blog/whisper-vs-parakeet-vs-apple-speech-engine/). That's spawned free open-source apps built around it - [MacParakeet](https://macparakeet.com/) (GPL-3.0, system-wide dictation + meeting recording, optional local WhisperKit fallback) is the clearest example of practitioners choosing Parakeet "from day one" over Whisper.

**The apps are converging on a "local by default, cloud optional" shape** - The most-starred repo the engine surfaced in this space is [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) at 4.7K stars (though carrying 209 open issues) - explicitly "voice-to-text dictation app with local (Nvidia Parakeet/Whisper) and cloud models (BYOK), privacy-first, cross-platform." The pattern people want is a dictation app that ships Parakeet/Whisper locally and only reaches for a cloud key if you opt in, echoed by [gabrimatic/local-whisper](https://github.com/gabrimatic/local-whisper) ("offline-first voice dictation... for macOS, iOS, and Android").

**The louder social energy is the privacy/anti-cloud argument, not the model bake-off** - Where r/LocalLLaMA actually lit up this window was the case for local models at all. The top thread, ["This is why we need local models and opensource harnesses"](https://www.reddit.com/r/LocalLLaMA/comments/1uvlwz0/this_is_why_we_need_local_models_and_opensource/) (3,383 upvotes, 409 comments), is a reaction to a server-side flag nobody could disable - [u/Comfortable-Rock-498](https://www.reddit.com/r/LocalLLaMA/comments/1uvlwz0/this_is_why_we_need_local_models_and_opensource/): "What is particularly nasty is the server side flag. You literally can't control it locally." That's the emotional undercurrent driving people to on-device STT in the first place - the same instinct behind [WAIC 2026: "Bringing AI Home Without Giving Up Data Privacy"](https://x.com/ZimaSpace/status/2079883349368381738) per [@ZimaSpace](https://x.com/ZimaSpace).

KEY PATTERNS from the research:
1. No single winner - Parakeet for English accuracy/speed, Moonshine for edge footprint, Whisper for multilingual - per [Northflank](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks)
2. Latency is the headline metric, not just WER - Moonshine's ~107ms vs Whisper's ~11,000ms is the stat that keeps getting quoted, per [modelslab](https://modelslab.com/blog/audio-generation/moonshine-vs-whisper-asr-real-time-speech-2026)
3. Parakeet-on-Apple-Neural-Engine (~80ms via CoreML) is the emerging default for local Mac dictation, per [Dictato](https://dicta.to/blog/whisper-vs-parakeet-vs-apple-speech-engine/)
4. Apps are settling on "local by default, cloud BYOK optional" - see [OpenWhispr](https://github.com/OpenWhispr/openwhispr) (4.7K stars)
5. The demand is privacy-driven - the anti-server-side-flag sentiment on [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1uvlwz0/this_is_why_we_need_local_models_and_opensource/) is the real fuel behind going on-device

---
✅ All agents reported back!
├─ 🟠 Reddit: 13 threads │ 15,900 upvotes │ 2,437 comments
├─ 🔵 X: 14 posts │ 41 likes │ 10 reposts
├─ 🟡 HN: 13 storys │ 1,017 points │ 307 comments
├─ 🐙 GitHub: 2 items │ 15,008 reactions │ 217 comments
├─ 🌐 Web: 17 pages - GitHub, ai-market-watch.com, hyper.ai, explainx.ai, hackster.io, localai.io, getvoibe.com, sourceforge.net
├─ 🗣️ Top voices: @sanchitmonga22, @ZimaSpace, @_Morax__ │ r/LocalLLaMA, r/LocalLLM, r/selfhosted
└─ 📎 Raw results saved to /private/var/folders/nv/zl70w7t90d3d9b6myqydky9c0000gn/T/tmp.mzqOWZte2w/what-people-running-local-on-device-speech-to-text-in-2026-say-about-moonshine-parakeet-and-other-real-time-whisper-alternatives-for-transcription-and-voice-control-raw-v3.md
---
