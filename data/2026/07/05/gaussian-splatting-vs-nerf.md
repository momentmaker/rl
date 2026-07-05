🌐 last30days v3.3.2 · synced 2026-07-05

What I learned:

**The 30-day signal is not a debate anymore - it is a division of labor.** Across the last month the loud, high-engagement material on both X and Reddit is almost entirely Gaussian splatting, and almost none of it argues with NeRF at all. [@gracia_vr](https://x.com/gracia_vr/status/2072292904869978229) is pushing 4D Gaussian Splatting as a creative-production tool (multi-camera volumetric capture of a dancer under strobing lights, then free viewpoint chosen in post), and drone-mapping people in [r/UAVmapping](https://www.reddit.com/r/UAVmapping/comments/1ukqf37/gaussian_splatting_based_rooftop_edges_distortion/) are shipping splat-based orthomosaics of rooftops. The tell: when practitioners want a photoreal result on a screen, fast, they reach for splats by default and do not mention NeRF as a rival. NeRF has stopped being the thing you compare against and become the thing underneath - one resolved-entity note in the raw dump put it bluntly, that splatting is the destination-is-a-screen technology while NeRF in 2026 is 'mostly' infrastructure and research substrate.

**Where NeRF still actually wins is the stuff splats are structurally bad at: physically-correct light and tiny files.** The consistent finding from verification is that splats bake view-dependent appearance into the scene - lighting is captured, not modeled - so you cannot cleanly relight a splat, reshape it, or hand it to a modeller, and complex reflections off glass and mirrors break because there is no real geometry behind the virtual image. NeRF's implicit MLP representation is the friendlier starting point for inverse rendering, material decomposition, and relighting, which is exactly why the freshest arXiv work surfacing in the [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) feed (AugSplat, StereoGS, and a run of 'Reflective / deferred-shading' Gaussian papers) is essentially splatting trying to borrow NeRF's abilities back. The other durable NeRF edge is size: NeRF scenes compress to roughly 10-50MB while a raw splat scene runs 500MB-1.5GB, which matters the moment you leave a demo GPU and try to stream to phones or the web. NeRF also degrades more gracefully in textureless or sparse-view captures where splats' structure-from-motion dependency starves.

**What splatting still cannot do, even in its 2026 hot streak, is be an editable model.** A splat is millions of view-dependent blobs, not a mesh with materials, so relighting, animation, physically-based reflection, transparent/thin-geometry capture, and clean handoff to a DCC modeller are all still open problems that the community is patching paper-by-paper (4D splatting for motion, deformable and scaffold variants for storage, deferred-reflection variants for glossy surfaces) rather than solving natively. The honest 2026 read is that splatting won real-time viewing and NeRF-family methods still own the physics; the fact that nobody on X is arguing about it is itself the story.

KEY PATTERNS

- **Splatting owns the output, NeRF owns the substrate** - the month's engagement is all splat production work (4DGS video, drone orthomosaics), with NeRF invisible precisely because it moved under the hood.
- **The contrarian tell is silence** - practitioners no longer benchmark splats against NeRF; they benchmark splats against photogrammetry and LiDAR, which is what 'replaced' really looks like.
- **NeRF's moat is light and bytes** - relighting, complex reflections, inverse rendering, and 10-50MB vs 500MB-1.5GB file size are the axes where NeRF-style implicit models still beat splats.
- **Splatting's ceiling is editability** - view-dependent baked lighting means no easy relight, no reshape, weak glass/mirror/thin-geometry capture, and no clean modeller handoff.
- **The research delta is convergence, not competition** - new arXiv splatting papers (Reflective GS, deferred-shading GS, deformable/scaffold GS, 4DGS) are splats absorbing NeRF's relighting and compactness, blurring the line the seed question assumes.

---
✅ All agents reported back!
├─ 🟠 Reddit: 6 threads │ 683 upvotes │ 171 comments
├─ 🔵 X: 16 posts │ 512 likes │ 71 reposts
├─ 🔴 YouTube: 12 videos │ 26,324,797 views │ 5/12 with transcripts
├─ 🐙 GitHub: 4 items │ 11 reactions │ 11 comments
├─ 🌐 Web: 5 pages - news.ycombinator.com, en.wikipedia.org, arxiv.org, cnet.com, GitHub
├─ 🗣️ Top voices: @gracia_vr, @ai_hakase_, @rsasaki0109 │ r/GaussianSplatting, r/UAVmapping
└─ 📎 Raw results saved to /private/tmp/rl_raw.YRqhEk/gaussian-splatting-raw-gsplat.md
---

If you want, I can go one level deeper on any single thread here - the 4D-splatting-for-video pipeline, the relightable-Gaussian research race, or the file-size/streaming tradeoff that keeps NeRF alive on the web.
