# Provenance — 2026-07-27

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and `why?` text are never written here.

## Source entries (3 picked, topic-level only)

- A saved **essay on loops as the emerging unit of software engineering work** (tags: ai,
  coding-agents, software-development, automation, loops), captured in late June with one
  of the most conviction-carrying notes in the eligible pool. Pull: the sense that agents
  running in loops is where the practice is heading, and an unresolved discomfort about
  what judgment survives it.
- A saved **multimodal command-line tool built for agents to use** (tags: cli, multimodal,
  llm, python, rust), captured in early July. Pull: interest in the tool as something to
  hand an agent, which under the surface is a question about what an agent can and cannot
  perceive.
- A saved **open-source React component set for document-heavy interfaces** (tags:
  open-source, ui-components, document-processing, react, tailwind), captured in June.
  Pull: appreciation for the UX of document-shaped web apps, which the fan-out followed
  down into how those components get distributed at all.

Chosen for domain spread (agent engineering practice · agent perception and tooling ·
frontend architecture) and specifically to get one non-AI-framed topic onto a day where
the eligible pool was heavily AI-weighted. The last five published days ran AI-adjacent on
nearly every slot.

## Fan-out — 12 adjacent candidates (all cleared the near-dup guard)

From the loops entry:
1. Stop conditions for agent loops: how people decide the agent is actually done ✅ picked
2. What breaks in long-running autonomous coding agents after hour three
3. Ratchets and guardrails that keep quality from degrading across agent iterations
4. Agent-written code review loops versus human checkpoints

From the multimodal-CLI entry:
5. Giving coding agents access to PDFs, images, audio and video ✅ picked
6. sqlite-vec and embedded vector search as the local default
7. Rust core plus Python API as the shipping pattern for dev tools
8. Unix-philosophy composability for LLM command-line tools

From the document-components entry:
9. Rendering PDFs in the browser after pdf.js
10. Citation and source-highlighting UX in AI document apps
11. Headless component libraries versus copy-in shadcn-style components ✅ picked
12. Virtualized rendering and scroll performance for very long documents

Near-dup guard: none of the 12 were flagged. Highest score was 0.196 for candidate #1
against the 2026-07-26 agent-memory day, followed by 0.155 for #3 (same day) and 0.135 for
#11 against the 2026-07-24 design-tokens day. #2 and #4 sat at 0.121 and 0.131 against
2026-07-20's autonomous-agent safety-nets day, which is the closest existing neighbour in
that cluster. All comfortably clear of the threshold, and the picked three were checked by
eye against those neighbours as well as by score.

## Narrowing to the top 3

- **#1 Stop conditions** — the most learnable of the loop-adjacent four, because the
  question has concrete answers this month rather than opinions: a shipped command
  surface, an explicit evaluator design, a named failure class with a paper behind it.
  Picked over #3, which turned out to be a component of the same answer and got folded in,
  and over #4, which borders the LLM-as-a-judge day published 2026-07-25.
- **#5 Agents reading binary formats** — chosen over #6, #7 and #8, which are each one
  layer of the same tool rather than the question the tool exists to answer. The angle
  survived contact badly in an instructive way: the premise turned out to be out of date,
  which became the brief's opening finding.
- **#11 Copy-in versus headless components** — deliberately the non-AI slot, and it landed
  on a dated in-window event (shadcn/ui defaulting to Base UI in July). Picked over #10,
  which would have made the day three-for-three AI, and over #9 and #12, which overlap the
  PDF material already covered by #5.

Final three span three distinct domains and do not overlap. Two of the three ended up
correcting the question they were asked, which is the better outcome available.

## Evidence quality notes

All three briefs carry an explicit italic evidence note, per the engine's honesty
convention. Recall was uneven on each, in three different ways:

- The stop-conditions brief is a concept topic with no named entity, so the engine's
  cluster ranker demoted every cluster with "entity-miss" and its scores are not
  meaningful; the read comes from the raw items directly. Reddit's search 403'd into
  listing discovery, so the footer's 16,926 upvotes are two unrelated viral threads, and
  YouTube returned 4 videos with 0 usable transcripts. The load-bearing evidence is the
  web layer plus a few X posts with real engagement.
- The binary-formats brief hit a genuine keyword trap: Hacker News tags submissions with a
  literal `[pdf]` suffix, so its HN slot filled with every PDF-linked story of the month
  (Terence Tao's ICM slides, a BIS bulletin, a 1939 essay), none of them on topic. One
  GitHub project with live star data, first-party Google model docs and three web
  supplements carried it.
- The components brief had the strongest corpus of the three (a 282-point HN thread, the
  shadcn changelog, live GitHub star counts) but almost nothing on X - 4 posts, 24 likes
  total. The word "copy" also matched a floppy-disk preservation guide and a story about
  MG cars, which is the engine catching the wrong sense of the word.
