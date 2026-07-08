# Provenance — 2026-07-08

Redacted by design: source `self` URLs and private `why?` notes are never
committed. This file records the topic-level rationale and the candidate funnel.

## Source signal (3 entries mined from the private `self` library)

Three saved entries seeded today's fan-out, chosen for genuine personal pull and
domain spread (weighting the private `why?` note heaviest). The index skews
heavily AI/coding, so the funnel was steered toward range — one security/OSS
thread, one local-AI thread, and one deliberately non-AI privacy/mapping thread:

1. A saved link on an **open-source scheduling tool**, annotated with a hunch that
   open projects are retreating from openness under AI-accelerated vulnerability
   pressure. Seeded the security / open-source-economics track.
2. A saved link on a **local AI model built by a well-known systems programmer**
   (the Redis creator's from-scratch local-inference work). Seeded the
   local-LLM-on-your-own-hardware track.
3. A saved link on a **privacy-first offline maps app**. Seeded the
   privacy / OpenStreetMap navigation track — the day's non-AI pick.

## Fan-out: 12 adjacent candidates (all passed the near-dup guard)

From the open-source-security seed:
- AI bug-hunting: real CVEs found by agents vs AI slop reports flooding maintainers
- Open-source projects going source-available or closed under AI pressure
- AI-generated vulnerability-report spam drowning maintainers (curl, OSS bounties)
- Source-available license backlash (BSL, FSL, Elastic)
- AI coding agents used for offensive security and pentest automation

From the local-AI seed:
- Local LLM inference on consumer hardware in 2026 — what is actually usable
- Veteran systems programmers moving into local AI and ML infrastructure
- The llama.cpp / MLX / Ollama local-inference tooling ecosystem

From the privacy-maps seed:
- Organic Maps vs CoMaps fork and the OSM app governance split
- Privacy-first offline alternatives to Google Maps
- OpenStreetMap data quality and community in 2026
- The offline-first app design revival

## Narrowed to 3 (curiosity, freshness, learnability, non-overlap)

1. **AI bug-hunting vs the slop flood** — the security/OSS pick, with a sharp
   30-day arc (curl's bounty shutdown-and-pause, Big Sleep / AISLE / XBOW real
   finds, the OpenSSF slop working group) and a clean "discovery got cheap,
   verification didn't" thesis.
2. **Local LLMs people actually run in 2026** — the local-AI pick, tied to the
   systems-programmer seed, with concrete, learnable specifics (Qwen3-Coder MoE,
   MLX vs llama.cpp throughput, Mac mini RAM tiers, antirez's DS4 experiment).
3. **Organic Maps vs CoMaps** — the deliberately non-AI pick, a live governance
   split (April 2025 open letter, the not-for-profit fork, CalyxOS/iodéOS default
   swaps) that keeps the day a range rather than an AI-tooling rut.

## Connections

One prior published topic scored above the connection threshold: the local-LLM
brief links to the earlier **Apple-silicon Mac mini / Studio as the local-LLM
inference box** entry (2026-06-25) — the same hardware question, revisited a
window later through what people actually run and where the frontier gap sits.
The security and maps tracks are new territory for the index; their only overlaps
are generic tags the relatedness check (correctly) does not treat as real
connections.
