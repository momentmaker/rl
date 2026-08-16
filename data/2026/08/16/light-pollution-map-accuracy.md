🌐 last30days v3.3.2 · synced 2026-08-16

What I learned:

**The map and the Bortle number are measuring two different things, and the atlas author says so himself** - [djlorenz's Light Pollution Atlas](https://djlorenz.github.io/astronomy/lp/bortle.html), the model behind most of the maps people plan around, states the mismatch plainly: the maps simulate artificial brightness *at zenith*, straight up, while the Bortle scale is a subjective visual metric covering the entire sky horizon-to-zenith. His conclusion is that zenith brightness and Bortle "are too different to equate" and map data should be reported as zenith brightness, not as a Bortle class. Every colored patch anyone drives toward is a zenith simulation wearing a Bortle label it was never entitled to.

**The practical consequence is that the number ignores the thing that actually ruins the shot** - [Astroimagery](https://www.youtube.com/watch?v=bdbuKYufLvo) puts it in one line: the map "doesn't show the massive dome of light pollution on the horizon from a city 50 miles away." The framing across the on-topic video layer is the same - "you found that perfect blue or green patch on the map," drove hours, and the photos came back washed out. [sterngucker](https://www.sterngucker.de/en/light-pollution/) gives the absurd case: a site on the edge of a conurbation next to a motorway and an alpine location at 1,600 m can both read "Bortle 4" on the map. Same label, completely different night.

**Somebody actually ran the head-to-head with a meter instead of arguing about it** - [Cosmic Curiosity](https://www.youtube.com/watch?v=yday2RTkVj8) tested lightpollutionmap.info against other data sources at four locations using a physical SQM: "in order to determine the actual light pollution levels, what we're going to be doing is we're going to be using this... the lens that sits here on the top measures the actual light pollution." The instrument's own limitation is the tell - "it only measures in a 20° cone above it," so even the ground-truth device is a zenith measurement. The 6,597-view test is the only measured comparison in the corpus; the rest is assertion.

**The staleness is real but smaller than the modelling gap** - [lightpollutionmap.app](https://lightpollutionmap.app/about-data/) is explicit that the latest *completed* annual satellite layer is 2025, and anything labelled 2026 is a provisional model estimate revised as monthly inputs arrive, not a finished layer. djlorenz likewise recalculated Cinzano's original World Atlas against 2025 VIIRS composites from the Earth Observation Group. So the data is roughly a year behind, not a decade - the bigger error is structural, not chronological.

**The structural error has a measured size, and it is about six-fold** - [Globe at Night](https://www.science.org/doi/10.1126/science.abq7781)'s 51,000+ naked-eye citizen observations put sky brightening at 9.6% per year globally (6.5% in Europe, 10.4% in North America), against satellite-observed growth in light emissions of 2.2% per year for 2012-2016. [Sky & Telescope](https://skyandtelescope.org/astronomy-news/light-pollution-is-increasing-even-faster-than-we-realized/) names the two mechanisms: VIIRS is blind to the blue wavelengths that LED fixtures emit, and it is most sensitive to *upward*-directed light while horizontally emitted light is what actually builds skyglow. The satellite is under-counting exactly the lighting that has been replacing everything since 2012.

**The field's own advice has already moved off Bortle, quietly** - sterngucker's recommendation is to go by the SQM value in mag/arcsec² rather than the plotted Bortle classes, "those are only rough conversions." [Adventures in Astronomy](https://www.youtube.com/watch?v=M7o0BNOZI00) makes the same move affordable: a dedicated SQM meter runs about £150-200, and a phone app tracks it to within "0.1, 0.2" of the real instrument. [Tsula's Big Adventures](https://www.youtube.com/watch?v=8gVIgUUOIrU) supplies the conversion anyway for people who want it - Bortle 1 corresponds to SQM 21.76-22.0, Bortle 5 to SQM 20.3-21.3 - which is itself the demonstration, since a whole Bortle class spans a full magnitude of sky brightness.

**The topic has no live discussion layer at all, and that is the honest finding** - the engine pulled 24 Reddit threads, 13 X posts and 9 HN stories in the window and essentially none of them are about this. The Reddit layer surfaced r/PhasmophobiaGame in its top communities, the X layer returned IPTV adverts matching on "Sky," and the top HN story was an all-sky map of supermassive black holes. Reddit's public search endpoint returned 403 on both attempts. Every genuinely on-topic item in the corpus is a YouTube video or a documentation page, and all five videos are dated outside the 30-day window - the newest is 2026-05-31. This is a settled evergreen question that practitioners re-explain to each other on video, not an argument anyone is currently having.

KEY PATTERNS from the research:
1. Maps model zenith brightness; Bortle is a horizon-to-zenith visual judgment - the atlas author says they should not be equated, per [djlorenz](https://djlorenz.github.io/astronomy/lp/bortle.html)
2. The map cannot see the light dome from a city 50 miles off, which is what actually degrades the frame, per [Astroimagery](https://www.youtube.com/watch?v=bdbuKYufLvo)
3. Two sites with identical "Bortle 4" labels can be a motorway edge and a 1,600 m alpine location, per [sterngucker](https://www.sterngucker.de/en/light-pollution/)
4. Latest completed satellite layer is 2025; 2026 values are provisional estimates, not a finished annual layer, per [lightpollutionmap.app](https://lightpollutionmap.app/about-data/)
5. Ground observers measure 9.6%/yr brightening against 2.2%/yr from satellites - roughly 6x, per [Globe at Night](https://www.science.org/doi/10.1126/science.abq7781)
6. VIIRS is blind to LED blue and weights upward light, while horizontal light drives skyglow, per [Sky & Telescope](https://skyandtelescope.org/astronomy-news/light-pollution-is-increasing-even-faster-than-we-realized/)
7. The recommended substitute is the SQM value in mag/arcsec², with a phone app tracking a £150-200 meter to within 0.1-0.2, per [Adventures in Astronomy](https://www.youtube.com/watch?v=M7o0BNOZI00)
8. One Bortle class spans a full magnitude of SQM (Bortle 5 = 20.3-21.3), which is why the label loses the information, per [Tsula's Big Adventures](https://www.youtube.com/watch?v=8gVIgUUOIrU)

---
✅ All agents reported back!
├─ 🟠 Reddit: 24 threads
├─ 🔵 X: 13 posts │ 254 likes │ 189 reposts
├─ 🔴 YouTube: 5 videos │ 36,056 views │ 5/5 with transcripts
├─ 🟡 HN: 9 storys │ 284 points │ 127 comments
├─ 🐙 GitHub: 5 items │ 1 comments
├─ 🌐 Web: 10 pages - sterngucker.de, lightpollutionmap.app, opticalmechanics.com, en.wikipedia.org, spaceinformer.com, tembrica.com
├─ 🗣️ Top voices: @twicktwit, @wthgngg, @Ayan_smith_ │ r/telescopes, r/Stargazing, r/PhasmophobiaGame
└─ 📎 Raw results saved to the run's non-committed evidence directory
---
