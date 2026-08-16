🌐 last30days v3.3.2 · synced 2026-08-16

What I learned:

**The shade math is the part that already got validated, which is the opposite of what the framing assumes** - [NREL](https://research-hub.nrel.gov/en/publications/validating-the-accuracy-of-helioscopeaposs-automated-shade-report/) tested HelioScope's remote solar access values against Solmetric SunEye readings taken in the field at 43 roof locations across four Los Angeles houses, 38 across four Denver houses and four across two Camden buildings. Two one-sided statistical tests found the remote and field readings statistically equivalent, with HelioScope's error running -7.0% to +4.3%, in line with other validated tools at within ±7%. The industry did not just assert this. It ran 85 measured roof points and published.

**Which is why the shade report is now a regulatory instrument, not a sales aid** - remote shade analysis is accepted in lieu of on-site measurement by rebate authorities in California, Texas, New Jersey, Oregon, New York and Rhode Island, per [HelioScope's own documentation](https://help-center.helioscope.com/hc/en-us/articles/8198878093971-Shade-Reports). The question stopped being "is the software good enough" some years ago and became "good enough for what."

**The accuracy number is not one number, it is a tier that depends on whether LiDAR covers your address** - with LiDAR coverage the tools land at roughly ±2-3%, and where only satellite imagery exists that widens to ±5-8%, per [Energyscape Renewables](https://energyscaperenewables.com/post/lidar-solar-design-accuracy-for-us-solar-installers/). Nothing in the report tells the customer which tier their own roof fell into. A ±3% design and a ±8% design print the same document.

**What the site visit actually catches is everything that is not shade** - the on-site list from [EagleView](https://www.eagleview.com/blog/solar-design-process/) and the survey checklists is roof age and wear, electrical panel labels, interior wiring paths, attic access, structural framing, unusual roof materials, and anything that changed since the last imagery pass. On layout specifically, the panel area must be verified free of vents, pipes, skylights and setbacks - a forgotten vent forces a design change or costs a panel on install day. The remote model is good at sun angles and bad at plumbing.

**The one shading thing remote analysis genuinely cannot do is look forward** - the checklists call for recording nearby trees, chimneys, dormers and future growth risk. A satellite pass is a photograph of a tree on a date. A twenty-five year production model is a claim about that tree in 2051, and nothing in the imagery pipeline models growth.

**The stated engineering rule is a threshold, and it is specific** - field verification is advised when the roof is complex or the system exceeds 25 kW, with the framing that remote data speeds up sales while field data protects engineering. That sentence is the whole tension in one line: the two datasets serve two different departments, and the site visit is a cost to the department that does not benefit from it.

**The reason any of this is contested is that the shade report is a liability document** - production guarantees typically run 10-25 years with a payout trigger at 85-95% of estimate, and [Sunrun's terms](https://solarcancellationcompanies.com/guide/solar-production-guarantee/) exclude refunds for underproduction from anything other than a system defect or "shading conditions present at the commencement of installation." Shade is simultaneously the thing the model measures and the thing the contract carves out. The document that sold the system is the document that limits the remedy.

**And the failure mode people actually litigate is the model being run on the wrong picture** - one documented dispute had the production estimate built on unshaded satellite data that ignored visible roof obstructions, with a lawyer finding satellite images showing no shade while street-level photos from the same week showed trees plainly. That is not a modelling error. That is stale or mis-selected imagery under a validated model, which the ±7% figure says nothing about.

**Blaming a tree is the industry's reflex, and it is checkable** - in a [BBB complaint](https://www.bbb.org/us/ut/farmington/profile/solar-energy-contractors/1solar-1126-90012700/complaints) an 18-panel system produced about 6.8 kWh/day for two and a half months. The company suggested a nearby tree; the homeowner pointed out the tree had no leaves. A technician eventually found roughly two thirds of the panels were not producing because the system had been installed incorrectly. Against a reported pattern of production landing about 12% under model, "it's the shading" is the cheapest available explanation and it is wrong often enough to be worth testing.

**The evidence layer for this topic is almost entirely vendor-published, and the engine run makes that visible** - the corpus pulled 13 Reddit threads totalling 6 upvotes, 13 X posts about British farmland leases and German generation records, and 13 HN stories whose top entries were solar overtaking fossil fuels in Germany, whether to wash your panels, and an eclipse map. Reddit's search endpoint returned 403. The only on-topic item the engine surfaced on its own is [pvlib-python](https://github.com/pvlib/pvlib-python) at 1.6K stars and 242 open issues, the open-source PV modelling library that every commercial tool is implicitly benchmarked against and that nobody in the sales conversation ever mentions.

KEY PATTERNS from the research:
1. Remote shade reports were validated against field instruments at 85 roof points across three metros, statistically equivalent, error -7.0% to +4.3%, per [NREL](https://research-hub.nrel.gov/en/publications/validating-the-accuracy-of-helioscopeaposs-automated-shade-report/)
2. Six states' rebate authorities accept remote shade analysis instead of on-site measurement, per [HelioScope](https://help-center.helioscope.com/hc/en-us/articles/8198878093971-Shade-Reports)
3. Accuracy is a tier, not a number - roughly ±2-3% with LiDAR coverage against ±5-8% satellite-only, and the report does not say which you got, per [Energyscape](https://energyscaperenewables.com/post/lidar-solar-design-accuracy-for-us-solar-installers/)
4. What the site visit catches is non-shade: vents, pipes, skylights, roof age, panel labels, wiring paths, attic access, structural framing, per [EagleView](https://www.eagleview.com/blog/solar-design-process/)
5. Future tree growth is the one shading factor no imagery pipeline models, against a 25-year production claim
6. The stated rule is field-verify when the roof is complex or the system exceeds 25 kW - remote speeds sales, field protects engineering
7. Shading is the named exclusion in production guarantees, so the shade report caps the remedy it helped sell, per [Sunrun's terms](https://solarcancellationcompanies.com/guide/solar-production-guarantee/)
8. The litigated failure is stale or wrong imagery under a valid model, not the model - satellite showing no shade while street photos the same week showed trees
9. "It's the shading" is the default explanation for the reported ~12% under-model pattern and is frequently wrong - one 18-panel system ran at 6.8 kWh/day for 2.5 months because two thirds of the panels were miswired, per [BBB](https://www.bbb.org/us/ut/farmington/profile/solar-energy-contractors/1solar-1126-90012700/complaints)

---
✅ All agents reported back!
├─ 🟠 Reddit: 13 threads │ 6 upvotes │ 9 comments
├─ 🔵 X: 13 posts │ 455 likes │ 191 reposts
├─ 🔴 YouTube: 3 videos │ 13,610 views │ 2/3 with transcripts
├─ 🟡 HN: 13 storys │ 1,400 points │ 1,271 comments
├─ 🐙 GitHub: 1 item │ 1,638 reactions │ 242 comments
├─ 🌐 Web: 4 pages - energyscaperenewables.com, heavendesigns.in, heavengreenenergy.com
├─ 🗣️ Top voices: @TheMinuend, @Localizefoodapp, @Steve09812 │ r/solar, r/IndicKnowledgeSystems, r/theydidthemath
└─ 📎 Raw results saved to the run's non-committed evidence directory
---
