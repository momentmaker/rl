# Provenance — 2026-07-09

Redacted by design: source `self` URLs and private `why?` notes are never
committed. This file records the topic-level rationale and the candidate funnel.

## Source signal (3 entries mined from the private `self` library)

Three saved entries seeded today's fan-out, chosen for genuine personal pull and
domain spread (weighting the private `why?` note heaviest). The index skews
heavily AI/coding, so the funnel was steered for range — one creative
data-viz/transit thread, one AI-in-production thread, and one self-hosted
infrastructure thread:

1. A saved link on a **3D transit-map visualization** (a browser-based train
   tracker built with a WebGL data-viz library), annotated with a concrete
   personal project idea. Seeded the transit / data-viz / creative-coding track —
   which naturally reaches an adjacent Japanese-railway sound topic.
2. A saved link on an **AI agent causing a destructive database action**,
   annotated with a strong opinion that anything touching production needs guards.
   Seeded the AI-agents-in-production / guardrails track.
3. A saved link on a **self-hosted team-chat server from a solo developer**
   (a Slack/Discord-style alternative). Seeded the self-hosting / owned-infra track.

## Fan-out: 12 adjacent candidates (all passed the near-dup guard)

From the transit/data-viz seed:
- deck.gl vs kepler.gl vs Mapbox GL for large geospatial datasets
- Real-time transit maps from GTFS-Realtime feeds
- Japanese train-station departure melodies (eki melodies) and who composes them
- WebGPU for browser big-data rendering

From the AI-in-production seed:
- AI agents deleting production databases and the guardrails teams add
- Human-in-the-loop approval gates for autonomous agents
- Least-privilege sandboxing and permission models for AI agents
- Blameless postmortems when an AI causes the outage

From the self-hosting seed:
- Self-hosted Slack and Discord alternatives people run (Matrix, Zulip, Mattermost)
- The solo-dev indie infrastructure movement
- Matrix protocol and federated chat in 2026
- Data sovereignty and the self-hosting revival

## Narrowed to 3 (curiosity, freshness, learnability, non-overlap)

1. **Japanese train station departure melodies** — the deliberately non-AI pick,
   a delightful and concrete topic with a clear cast (Mukaiya of Casiopea, Ide of
   Switch), an engineered 7-second design constraint, and a named fan culture
   (ototetsu). Keeps the day a range rather than an AI-tooling rut.
2. **AI agents deleting production databases** — the AI pick with the sharpest
   30-day arc (the PocketOS "9-second" Railway wipe, echoing the 2025 Replit
   case) and a clean, learnable thesis: the failure is access control, not model
   malice; the fix is least-privilege, task-scoped credentials plus human gates.
3. **Self-hosted Slack/Discord alternatives** — the owned-infra pick, tied to the
   solo-dev seed, with concrete comparables (Mattermost vs Zulip vs Matrix vs
   Rocket.Chat), a live homeserver-migration story (Synapse → Conduit), and clear
   VPS-vs-per-seat economics.

## Connections

None of today's three topics scored above the connection threshold against the
prior index. The transit-culture, AI-production-safety, and self-hosted-chat
tracks are all new territory for the index; their only overlaps with past topics
are generic tags the relatedness check (correctly) does not treat as real
connections.
