# Provenance — 2026-07-10

Redacted by design: source `self` URLs and private `why?` notes are never
committed. This file records the topic-level rationale and the candidate funnel.

## Source signal (3 entries mined from the private `self` library)

Three saved entries seeded today's fan-out, chosen for genuine personal pull and
domain spread (weighting the private `why?` note heaviest). The index skews
heavily AI/coding, so the funnel was deliberately steered for range — one
homelab/hardware thread, one security-tooling thread, and one creative/archival
thread:

1. A saved link on **remotely powering on / reaching a Mac at home**, annotated
   with a personal note about eventually setting one up. Seeded the
   homelab / always-on / remote-access track.
2. A saved link on a **file-and-URL sandbox scanning service**, annotated with
   interest in checking whether something is safe before opening it. Seeded the
   security / malware-triage track.
3. A saved link on a **public-domain image archive**, annotated as an
   interesting collection. Seeded the creative / copyright-free / archival track.

## Fan-out: 12 adjacent candidates (all passed the near-dup guard)

From the homelab / remote-Mac seed:
- Headless Mac mini home-server setups people run in 2026
- Wake-on-LAN and remote power for always-on home labs
- Remote-access stacks for a home Mac (Tailscale, SSH, screen sharing)
- Always-on home server energy, noise, and idle-power economics

From the security / scanning seed:
- Online malware sandboxes for checking files and URLs (VirusTotal, ANY.RUN, Hybrid Analysis)
- How people vet a suspicious link before clicking it
- Browser isolation and disposable VMs for sketchy attachments
- QR-code and URL phishing (quishing) and how people defend against it

From the public-domain / archival seed:
- Where people find trustworthy public-domain images in 2026
- The public domain class of 2026 — what entered and why it matters
- AI image generation vs archival scans — training on public-domain art
- Museum and library open-access programs digitizing old illustrations

## Narrowed to 3 (curiosity, freshness, learnability, non-overlap)

1. **Mac mini as an always-on headless home server** — the homelab pick, tied to
   the remote-Mac seed. Fresh 30-day hook (an Apple silicon exec calling the
   mini/Studio the "machines of choice" for AI agents) plus concrete, learnable
   mechanics: Tailscale/SSH remote access, the headless-display gotcha, and the
   split between classic home-server duties and unattended AI workers.
2. **Online malware-analysis sandboxes and their traps** — the security-tooling
   pick, tied to the scanning seed. A clean, learnable thesis with live 30-day
   discussion: treat VirusTotal/Hybrid Analysis/ANY.RUN as triage not verdicts
   ("0 detections ≠ safe"), the shift to CLI/agent-driven triage, and the
   false-positive mirror problem.
3. **QR-code phishing (quishing)** — the third slot pivoted within the security
   cluster. The public-domain/archival candidates were dropped at the research
   stage (evergreen reference topics with thin last-30-days discussion — the
   engine surfaced mostly generic stock-image and AI-slop noise, not fresh
   signal). Quishing, an adjacent candidate off the same scanning seed, had a
   sharp fresh arc instead: a June 2026 advisory on AITM quishing that defeats
   MFA, an AI-driven surge, and cheap commodity kits.

## Connections

None of today's three topics scored above the connection threshold against the
prior index. The homelab/remote-Mac, malware-triage, and quishing tracks are new
territory for the index; their only overlaps with past topics are generic tags
the relatedness check (correctly) does not treat as real connections.
