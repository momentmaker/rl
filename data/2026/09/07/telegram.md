---
ready: true
---
🎲 *Random Learning — 2026-09-07*

Three subjects where the thing existed the whole time and something else was missing — an index, a routing decision, an intention.

*1. Meshtastic, and what actually limits an off-grid mesh*
The live argument isn't range. It's routing, and it has produced a second firmware people are flashing.

Meshtastic *floods*: every node rebroadcasts every packet it hears, up to *7 hops*. That's the entire pitch — "there's nothing to configure." It's also the ceiling: as a flood network grows, "channel utilization climbs, latency increases, and eventually the mesh becomes *a source of interference with itself*."

• *The scope verdict, from a search-and-rescue write-up rather than the forums.* "Meshtastic is the right platform for a single incident with a defined team. It's the wrong platform for a statewide network, and *no firmware update changes that math*."

• *A city mesh stopped asking and shipped the fix as a default.* Philly Mesh baked reduced position, telemetry and NodeInfo reporting into the firmware — "without these packets clogging the mesh, there is more room for messages to reliably flow." You buy hops by *deleting the traffic the network generates about itself*. Almost none of a struggling mesh's air time is people talking.

• *Ignore any range number that doesn't name an antenna.* Same node, same day: *702 feet* on the BLE antenna, *11.5 miles* on LoRa with an upgraded whip.

Hardware, node maps and apps all went protocol-agnostic this month. Plan for two firmwares.

*2. FamilySearch's AI handwriting search*
From r/Genealogy: "I found a marriage record using the full text that I couldn't find for *15 years*. It is a perfectly fine record too, from 1849. The handwriting is a little messy, but very legible."

It was scanned, legible and on the site the whole time. What was missing was an index — and a name search returns nothing whether a record is absent or merely unindexed. The AI didn't read anything a person couldn't; it read what nobody had gotten around to.

What changed is *which pile opened*: microfilm scanned but never indexed — *deeds, probate files, land grants*. Indexed genealogy has always been births, marriages and deaths, because those carry a name in a predictable field and are cheap to index by hand. The skipped records are where a life actually leaves a trail.

• *The failure mode is coverage, not accuracy.* Six separate collections, "no real way to determine the degree of redundancy," any search reaching "an unknown number of documents." So "most users… do an unsuccessful name search and conclude that FamilySearch does not have the documents." *A negative result carries no information.*

• *You can't fix a bad transcript, and the reason is legal.* Editing is off so edits can't "impede our ability to follow privacy laws and respond to requests from the organizations that own the records" — possibly permanently. *Correctability was traded for retractability.*

*3. Read-it-later apps, a year after Pocket*
The sharpest line came from the note-taking crowd: "you can't tell which saves were things you genuinely meant to read and which were just there to round out the collection. *A vault full of unread material isn't a second brain. It's a storage unit.*"

The mechanism makes it stick: things you intend to use get routed within seconds — restaurant to Google Maps, article to a group chat. The queue is defined by *exclusion*: it's where things go when you decide not to decide, so backlog size isn't a tooling problem.

• *The vendor says the capture is lossy, in its own docs.* Readwise: "we'll never be able to parse 100% of the internet, 100% perfectly."

• *Portability had an expiry date.* Four apps accept Pocket's export format — "yes, *if you exported it before access ended*." The only durable version is the copy already on your disk.

• *The most-upvoted fix changes the device, not the app* — RSS piped to a 4.3-inch backlight-free e-reader, 228 points on HN. Its author never claims he now reads more.

_Sources: last30days across Reddit, HN, X, GitHub + web._
