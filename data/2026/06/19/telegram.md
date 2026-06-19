---
ready: true
---
*Random Learning — 2026-06-19*

Three things I dug into today, from what people are actually saying in the last 30 days.

*1. AI-fabricated citations broke peer review - and now there are numbers.*
A Columbia/Lancet audit of 2.5M biomedical papers found 4,046 fake citations, with the rate up 12x since 2023 - roughly 1 in 277 papers in early 2026. The framing that stuck: this is a patient-safety problem, not academic hygiene, because a clinician "has no way of knowing the evidence they rely on does not exist" - and 98.4% of flagged papers got no publisher action. The proof everyone cites that human review can't catch this: ~53 papers at NeurIPS 2025 carried hallucinated citations that survived 3-5 expert reviewers each. The flashpoint response is arXiv's new one-strike rule (a year-long ban for hallucinated cites or leftover chatbot prompts) - which academics revolted against, and integrity experts call "welcome but unenforceable." Publishers are now fighting AI with AI (Springer Nature's reviewer-detection tool) while banning reviewers from uploading manuscripts to public LLMs.

*2. OpenCV 5 landed - and the story isn't "AI won," it's "classical vision is the layer underneath."*
First major release since 2018, dropped at CVPR. The upgrades: a rewritten DNN engine, ONNX coverage from ~22% to 80%+, built-in LLM/VLM support. But the developer takeaway is consolidation, not reinvention - the classic detectors stay right alongside the neural ones. Where classical still wins: geometry problems (SLAM, structure-from-motion, image stitching, 3D reconstruction), edge/embedded compute where hand-designed detectors match deep learning at a fraction of the cost, and interpretability - which in 2026 became a procurement requirement, not just a research nicety. In practice OpenCV does the resize, crop, calibration, and tracking before YOLO/SAM/a VLM ever runs. Migration pain is real in C++ (legacy C API gone, C++17 required) and a near non-event in Python.

*3. Why those little "live cursor" websites feel magical.*
Neal Agarwal's Cursor Camp drops you onto a campsite as a bare mouse pointer among strangers - no chat, no usernames, no profiles - and people are genuinely moved. The magic word everyone reaches for is "vibe," not "feature": just seeing other live cursors gives you the sense that "behind the glass, there are real people." Stripping away the social-media machinery is the point - reviewers call it a "wholesome no-chat hangout." The warmth comes from wordless collaboration: strangers build a fire and make stew together with zero communication. People read it as an antidote to the loneliness internet - "technology should create intimacy, not just scale." And it's now a DIY genre: one script tag via partykit/cursor-party, or managed infra via Liveblocks.
