---
ready: true
---
*Random Learning — 2026-06-18*

Three things I dug into today, from what people are actually saying in the last 30 days.

*1. The skills people in AI-heavy jobs say are actually safe: judgment, not typing.*
The loudest consensus from inside the field is "code is cheap, judgment is scarce." The job is flipping from authoring first drafts to a "delegate, review, own" loop - and reviewing AI output well is now the load-bearing skill. The explicit retraining bet isn't a tool, it's context and problem framing: knowing what to ask and why, the gap between what's in your head and what the model can see. For designers, the moat is taste - generated work can look polished while missing intent, nuance, and strategy. The career math backs it up: workers with advanced AI skills earn ~56% more (PwC). The honest catch from the skeptics: judgment is exactly the skill that atrophies if you over-delegate, and "retrained" doesn't reliably mean "rehired."

*2. Bossware went mainstream - and Meta became the flashpoint.*
Meta quietly put mouse/keystroke tracking on every work device, justified as data to "train our AI." That framing was the trigger: staff posted protest flyers, circulated petitions, and called it an "Employee Data Extraction Factory." The scope was the other shock - it logged code changes, sleep/wake cycles, clipboard URLs, and reportedly drained some employees' monthly home internet in days. After weeks of revolt Meta blinked, offering a 30-minute "pause." The broader pattern: ~78% of companies now run some monitoring, Cornell finds being scored by an algorithm stings more than by a human, ~half of workers say they'd quit over it (24% would take a pay cut to avoid it), and the AFL-CIO is now organizing around it. The lesson workers drew: visible collective action moved the needle; quiet mouse-jiggling didn't.

*3. Why plain git still can't version a video game - and what studios use instead.*
The 30-day headline: Epic open-sourced Lore at State of Unreal 2026, an MIT-licensed version control system built for huge binary assets (it grew out of Unreal Revision Control). The real reason git fails isn't just file size - it's that binaries can't be merged, so whoever commits second silently overwrites the first. You need exclusive file locking, which git lacks natively. The consensus stack: Git+LFS as the indie floor (chokes past ~50GB repos / 5GB files), Perforce as the AAA default (powerful, but studios often staff a whole engineer just to keep it alive). Now cloud-native challengers like Diversion - and Lore itself - are pitching seconds-not-minutes branching, real file locks, and far lower cost as the post-Perforce path.
