🌐 last30days v3.3.2 · synced 2026-06-18

What I learned:

**Epic just blew the category open by open-sourcing Lore** - The single biggest 30-day story is Epic Games open-sourcing Lore at State of Unreal 2026, a next-generation version control system built specifically around huge binary assets. It started life as Unreal Revision Control, already ships inside Unreal Editor for Fortnite, and is now MIT-licensed - a deliberately permissive license meant to pull studios off Perforce. Per [The Register](https://www.theregister.com/devops/2026/06/17/git-good-with-epic-games-new-open-source-vcs-lore/5257978), it is a centralized, content-addressed VCS designed from the ground up for large files and easy enough for 3D artists, not just engineers, and the [EpicGames/lore](https://github.com/EpicGames/lore) repo went public alongside UE5.8 and a UE6 roadmap.

**The core reason plain git fails is merging, not just file size** - The community keeps correcting the "git is just bad with big files" framing. The real wall is that binary assets - textures, meshes, audio, cutscenes - cannot be merged. Whoever commits second silently overwrites whoever committed first, so you need exclusive file locking, which git does not support natively. As [@kidtsang](https://x.com/kidtsang/status/2067531847026823317) put it on X, "it's not just about file size; the way we version control assets needs a rethink... collaboration on large binaries requires smarter tools." The [Bugnet Blog](https://bugnet.io/blog/version-control-strategies-for-game-assets) makes the same point: with no automated merge for binaries, file locking and clear ownership are the whole game.

**Git LFS is the indie floor, Perforce is the AAA default, and both have sharp edges** - The consensus stack is unchanged at the extremes: Git+LFS for small-to-mid indie teams, Perforce (Helix Core / P4) for large studios with massive libraries, per [Anchorpoint](https://www.anchorpoint.app/blog/version-control-for-game-development). But LFS reportedly chokes past roughly 50GB repos and 5GB files with limited locking, while Perforce "works when it works" but is gnarly enough that teams often staff a dedicated tools engineer just to keep the server alive, per the same gamedev discussions surfaced on [r/unrealengine](https://www.reddit.com/r/unrealengine/comments/1u8excv/epic_announces_a_new_open_source_version_control/).

**Cloud-native challengers are smelling blood** - Diversion is positioning as the modern Perforce replacement, and its founder showed up in the [r/unrealengine](https://www.reddit.com/r/unrealengine/comments/1u8excv/epic_announces_a_new_open_source_version_control/) Lore thread predicting "more game devs / studios will leave Perforce/Git for either Lore or Diversion." Per [Diversion](https://www.diversion.dev/knowledge-center/perforce-alternatives), it offers exclusive file locks, branch creation in seconds versus minutes on big Perforce streams, sync that scales to 400,000+ files per minute, and up to 70% lower total cost of ownership - and it claims to be officially recommended by Epic with the top-rated VCS plugin on FAB.

KEY PATTERNS from the research:
1. The headline event is Epic open-sourcing Lore, an MIT-licensed VCS purpose-built for large game binaries - per [The Register](https://www.theregister.com/devops/2026/06/17/git-good-with-epic-games-new-open-source-vcs-lore/5257978)
2. Plain git fails on binaries because they can't be merged and git has no native file locking, not merely because files are big - per [Bugnet Blog](https://bugnet.io/blog/version-control-strategies-for-game-assets)
3. The practical split stays Git+LFS for indies, Perforce for AAA, with LFS hitting limits around 50GB repos / 5GB files - per [Anchorpoint](https://www.anchorpoint.app/blog/version-control-for-game-development)
4. Perforce's hidden cost is operational: studios often need a dedicated tools engineer to keep it running - per [r/unrealengine](https://www.reddit.com/r/unrealengine/comments/1u8excv/epic_announces_a_new_open_source_version_control/)
5. Cloud-native challengers like Diversion are pitching seconds-not-minutes branching, file locks, and up to 70% lower TCO as the post-Perforce path - per [Diversion](https://www.diversion.dev/knowledge-center/perforce-alternatives)

---
✅ All agents reported back!
├─ 🟠 Reddit: 4 threads │ 1,936 upvotes │ 181 comments
├─ 🔵 X: 14 posts │ 744 likes │ 110 reposts
├─ 🐙 GitHub: 6 items │ 28 reactions │ 40 comments
├─ 🌐 Web: 10 pages - reddit.com, diversion.dev, bugnet.io, news.slashdot.org, resetera.com, atlassian.com
├─ 🗣️ Top voices: @kidtsang, @kalin_t, @parzerp │ r/godot, r/unrealengine, r/gamedevscreens
└─ 📎 Raw results saved to /private/var/folders/nv/zl70w7t90d3d9b6myqydky9c0000gn/T/tmp.AGCDib33UK/what-game-studios-actually-use-to-version-huge-binary-assets-in-2026-and-why-plain-git-still-doesn-t-cut-it-raw-v3.md
---
