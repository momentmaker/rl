🌐 last30days v3.3.2 · synced 2026-06-15

What I learned:

**The two attacks people are defending against are mechanically different, and that matters for what works** - A relay attack uses a pair of signal-boosting devices, one held near the key fob (often through a house wall) and one near the car, to relay the fob's signal and trick the vehicle into unlocking and starting in under 30 seconds with no network hacking at all, per [PlaxidityX](https://plaxidityx.com/blog/blog-post/keyless-car-theft-north-america/). CAN injection is a different beast: thieves pry open a headlight or reach a wiring junction, splice a small device onto the car's CAN bus, and inject fake "valid key" and "start engine" messages that bypass the fob and the immobilizer entirely. The practical upshot owners keep arriving at is that a Faraday pouch only addresses the first attack - it does nothing against a thief who is physically cutting into your wiring loom.

**The scale is what's driving the panic, and it's a North American story now** - PlaxidityX puts US vehicle thefts above 850,000 in 2024, roughly one every 37 seconds, and attributes about 60% of them to keyless techniques like CAN injection and key-fob relaying, per [PlaxidityX](https://plaxidityx.com/blog/blog-post/keyless-car-theft-north-america/). Canada is being hit hard too, with about 361.5 million dollars in theft-related insurance claims in the first half of 2025 and an estimated 900 million dollars in total annual insurer losses. Against a backdrop where 92% of US households own at least one car and roughly 285 million vehicles are registered, per [AutoInsurance.com](https://www.autoinsurance.com/research/car-ownership-statistics/), the keyless attack surface is enormous and the financial incentive for thieves is obvious.

**The Faraday pouch is the cheap default people reach for, and the consensus is "necessary but not sufficient"** - The most-watched practical guidance in the pull is a long-running explainer from [Revive My Ride](https://www.youtube.com/watch?v=pNtXb6G53mg) (452K views) that frames the problem bluntly: keyless go is convenient, but "it also opens the door for the modern day sophisticated car thief," with the channel citing roughly 50,000 keyless thefts a year in the UK and around 900,000 stolen vehicles a year in the US. The signal-blocking pouch stops the fob's signal from reaching a relay device while it sits by your front door, which is exactly why owners treat it as step one. But because it does nothing against CAN injection and fails the moment you forget to use it, the recurring advice is to layer it with a physical deterrent rather than rely on it alone.

**The defenses owners actually trust are the visible, physical ones - steering locks and OBD port locks** - The throughline in the hands-on guidance is that thieves optimize for speed and low risk, so a deterrent they can see before they commit is worth more than a clever electronic countermeasure. A steering-wheel lock turns a sub-30-second relay grab into a noisy, multi-minute job, and an OBD port lock or hidden port relocation specifically frustrates the diagnostic-port flavor of injection attack, which is why the [Revive My Ride](https://www.youtube.com/watch?v=pNtXb6G53mg) walkthrough leans on "three car anti-theft methods that will stop your car from being stolen plus proof that they work" rather than a single silver bullet. The pattern owners report: the goal is not to be unhackable, it is to be the harder car on the street.

**The deeper fix lives in the car itself, and right-to-repair tension complicates it** - OEMs are moving toward motion-sensor fobs that sleep when still, PIN-to-drive codes, and embedded CAN-bus intrusion detection like PlaxidityX's vDome that watches for forged messages in real time, per [PlaxidityX](https://plaxidityx.com/blog/blog-post/keyless-car-theft-north-america/). But the same locked-down vehicle networks that block injection attacks also lock out independent mechanics, and that friction surfaced on Hacker News around [Ford CEO Jim Farley's right-to-repair comments](https://www.thedrive.com/news/ford-ceo-jim-farleys-right-to-repair-comment-should-make-every-car-owner-uncomfortable), which owners flagged as a sign that "fixing" security by sealing the car can quietly transfer control away from the people who own it.

KEY PATTERNS from the research:
1. Relay attacks and CAN injection are different attacks, and no single device counters both - the Faraday pouch only stops the relay variant - per [PlaxidityX](https://plaxidityx.com/blog/blog-post/keyless-car-theft-north-america/)
2. Keyless techniques now account for roughly 60% of US vehicle thefts, making this a mainstream owner problem, not a niche one - per [PlaxidityX](https://plaxidityx.com/blog/blog-post/keyless-car-theft-north-america/)
3. The Faraday pouch is treated as step one but "necessary not sufficient" because it fails against wiring attacks and human forgetfulness - per [Revive My Ride](https://www.youtube.com/watch?v=pNtXb6G53mg)
4. Visible physical deterrents - steering locks and OBD port locks - win because thieves optimize for a fast, quiet grab - per [Revive My Ride](https://www.youtube.com/watch?v=pNtXb6G53mg)
5. The car-level fixes are motion-sensor fobs, PIN-to-drive, and embedded CAN intrusion detection that flags forged messages - per [PlaxidityX](https://plaxidityx.com/blog/blog-post/keyless-car-theft-north-america/)
6. Locking down vehicle networks for security collides with right-to-repair, raising who-controls-the-car concerns for owners - per [The Drive](https://www.thedrive.com/news/ford-ceo-jim-farleys-right-to-repair-comment-should-make-every-car-owner-uncomfortable)

---
✅ All agents reported back!
├─ 🔵 X: 4 posts │ 56 likes │ 15 reposts
├─ 🔴 YouTube: 1 video │ 451,970 views │ 1/1 with transcripts
├─ 🟡 HN: 12 storys │ 1,122 points │ 802 comments
├─ 🐙 GitHub: 4 items │ 46,185 reactions │ 377 comments
├─ 🌐 Web: 4 pages - autoinsurance.com, leftlanenews.com, caranddriver.com, plaxidityx.com
├─ 🗣️ Top voices: @AFkokogems, @Andy_T_, @June_12_1776
└─ 📎 Raw results saved to /private/tmp/rl_raw_20260615/how-car-owners-in-2026-are-actually-stopping-keyless-relay-attack-and-can-injection-thefts-and-which-defenses-like-faraday-pouches-obd-locks-and-steering-locks-people-say-really-work-raw-v3.md
---
