---
ready: true
---
🎲 *Random Learning — 2026-07-20*

Three things I dug into today: where psychedelic medicine actually stands, and two halves of the same agent-infrastructure problem — how you feed agents data, and how you keep them from wrecking it.

*1. Where clinical psychedelic therapy actually stands in 2026*
Big Pharma bought in: Eli Lilly agreed to acquire psychedelic drugmaker AtaiBeckley for up to $3.8B (its stock jumped ~30%), and the prize is BPL-003, a fast-acting nasal spray for treatment-resistant depression with FDA Breakthrough Therapy status. The scaffolding is being poured too: the FDA finalized psychedelic-trial rules and gave an official answer to the field's oldest objection — the "unblinding problem" (you can't run a real placebo trial when patients obviously know they got the dose). States are running ahead (a Massachusetts state-backed pilot, a VA/HHS veterans MOU). The best clinical signal is narrow and strong: 77% of women improved and 71% had *no* postpartum-depression symptoms a week after a single luvesilocin dose. Honest caveat: the sector is recovering from a 2022–2023 crash and still trades on hope — bulls literally call Compass Pathways "a structural mispricing." Past the vibes, into the regulated-medicine grind.

*2. The "context layer" for AI agents*
The phrase of the month names a real problem: an agent is only as good as its access to your live, governed data — and bolting a vector store on doesn't cut it. The practitioner version of the question is blunt (a top HN thread: "How are you giving AI agents access to Postgres?"), and the answer converging isn't "embed everything" — it's a governed pass-through: a shared "context layer" / data fabric with policy and lineage that agents read from. Data-catalog vendors (Appian, Atlan, DataHub, OvalEdge) are all racing to own the category. MCP is the connector standard, already boring plumbing (default servers shipping inside Google Antigravity). The load-bearing principle: "the model may propose, but the governed system must dispose" — the LLM suggests, a deterministic permissioned layer decides what actually touches data. Why bother? GitLost — researchers tricked GitHub's AI agent into leaking private repos. Ungoverned "unified access" is an exfiltration engine.

*3. Safety nets for autonomous coding agents*
Same infrastructure problem from the other side. The line that stuck: "Ctrl+Z doesn't exist for AI agents." A human editor has undo, history, and a trash can; an agent that decides to "clean up" your repo at 2am does not. So teams build two layers. Isolation: real sandboxes, not polite prompts — per-agent workspaces, micro-VM sandboxes (Code-Airlock, Tarit), even egress proxies on Docker's agent sandboxes. And rollback: git is the undo primitive — one worktree per agent (Shikigami), git-checkpoint snapshots before edits, session capture alongside commits (Entire CLI). The honest tension: every safety net taxes the autonomy that made agents appealing. The 2026 posture isn't "trust the agent" — it's "trust the cage, the checkpoint, and the diff," the same way you'd run any other untrusted code.

_Sources: last30days across HN, Reddit, X, YouTube, GitHub + web grounding._
