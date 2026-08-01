# Provenance — 2026-08-01

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **vendor cookbook of agentic AI workflow recipes** — async multi-agent patterns
  with a shared message hub, three tiers of deployment maturity, a vulnerability-discovery
  agent that threat-models a C target, and a grade-and-revise loop whose stateless grader
  re-fetches every URL and checks every quote against a rubric (tags: claude, agents,
  tool-usage, r&d, integrations), captured 24 July — the freshest entry in the pool. Pull:
  the note marks it as a reference to come back to for practical use, the strongest signal
  currently in the pool.
- A saved **essay on how AI is reshaping the software industry and its labour market** —
  named layoffs, falling entry barriers, the thesis that the middle of the product market
  disappears, and value migrating toward services and expert judgment (tags: software, ai,
  job-market, product-management, services), captured 27 June. Pull: the note is a plain
  endorsement of the piece's account of the field's trajectory.
- A saved **discussion thread of user reactions to an AI assistant's creative-software
  integrations** — Blender, Fusion, Affinity and Adobe Creative Cloud, including 3D models
  emitted via CadQuery, one flat "can't replace taste or imagination," and the observation
  that agent-written scripts can be saved, re-run and given their own UI (tags: ai,
  creative-tools, blender, user-feedback, automation), captured 29 April. Pull: no note
  attached. Selected on domain grounds, as explained below.

Chosen for domain spread (**agent engineering · software business economics · CAD and
making**). The eligible pool is 9 entries and 8 sit somewhere in the AI cluster, so the
creative-software thread was the only real domain escape available and was taken despite
carrying no note — the guidance weights the note heaviest, but it also warns against three
picks from one cluster on one day, and that constraint bound harder here.

Two entries with usable notes were deliberately passed over. An agent-harness entry sits
directly on the 2026-07-28 harness-vs-model day. A frontier-model-release entry is a
factual bookmark rather than a stated curiosity, and its topic is the most-mined ground in
the whole index.

## The 12 adjacent candidates

From the agent cookbook:
1. Agent-to-agent peer messaging: what multi-agent hubs look like in practice
2. Running coding agents in production: Docker vs Modal vs Kubernetes
3. Citation verification: making an LLM check every quote and URL it cites
4. **Agents that find vulnerabilities in C code: what actually gets found** ← picked

From the software-industry essay:
5. Services-as-software: the agency model investors are chasing now
6. Whether the mid-market SaaS product is actually dying
7. **Outcome-based pricing for AI products: what people charge for now** ← picked
8. Building software solo when code stops being the bottleneck

From the creative-software thread:
9. **Text-to-CAD: whether LLMs can actually produce parametric models** ← picked
10. MCP servers for creative apps: Blender, Figma, Fusion, DaVinci
11. Agent-authored scripts that become saved tools with their own UI
12. Where AI actually lands in the 3D pipeline: modeling, retopo, rigging, texturing

All 12 cleared the near-dup guard (highest score 0.129, well under threshold). The three
were chosen for non-overlap and for having something concrete to learn rather than a mood
to sample; 5 and 6 were dropped as the two most likely to return vibes, and 12 was dropped
because it shares a domain with 9.

## Notes on this run

**Topic 1 was retitled after research.** As first framed — what the agents found *and* how
maintainers feel about the reports — it scored 0.213 against 2026-07-08's slop-flood day.
Under the guard's threshold, but close enough to be a repeat in substance. The brief's real
centre of gravity is the verification gap (a vendor's 250+ claimed CVEs against an
independent tracker's five verified records; an audit finding the 432-CVE kernel batch is a
CVE-process artifact rather than an agent flood), so the topic was retitled to lead with
that. The 07-08 adjacency is recorded as a connection rather than hidden.

**Source-quality caveats, per topic.** Each brief states its own; summarised here because
two of the three are load-bearing.

- *AI-found vulnerabilities* — 88 items, carried by web and Hacker News plus two large
  r/cybersecurity threads. YouTube returned nothing, X returned 9 low-engagement posts with
  no maintainer voices, and much of the r/C_Programming layer is ordinary beginner traffic.
  Only 39 of 88 dated items fall inside the last 7 days. One circulating "1,596 disclosed,
  97 fixed" statistic was checked and left in as explicitly uncorroborated.
- *AI product pricing* — the community layer did not show up at all. Public Reddit search
  returned 403s, the RSS tier returned zero, and the 7 threads that came back are
  listing-discovery noise rather than pricing discussion. Both YouTube results are
  unrelated (a gaming stream and a state-senate hearing). The analyst and web layer carried
  this brief entirely, and the X layer is mostly vendor marketing at 1–2 likes.
- *Text-to-CAD* — the absence **is** the finding, so the thin community layer is reported
  rather than worked around: 22 threads and 54,264 upvotes across eight CAD and printing
  subreddits, none about AI-generated CAD, and one 6-point HN submission with no comments.
  Every strong claim in that brief traces to a vendor blog, a benchmark paper or a README,
  and the brief says so in its own body.

**Fuel is the thing to act on.** The check at start of run: **9 eligible, span 92 days,
capture rate 0.10/day, roughly 3 days of runway** at 3 per day. That is down from 12
eligible and 4 days yesterday, and it is the third consecutive day the log has recorded a
shrinking pool. Capture is running at a third of burn. At this rate the routine hits the
`--min-pool 3` circuit-breaker within about three days and will start skipping runs.
