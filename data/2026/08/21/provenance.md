# Provenance — 2026-08-21

Redacted by design: this records the funnel shape, not the private source links or
personal capture notes. Raw `self` URLs and capture-note text are never written here.

## Fuel

The circuit-breaker failed on the first read - `eligible_pool: 1`, exit 2 - and this was
the stale-cache false negative rather than genuine exhaustion. A `git fetch` showed the
local clone eight commits behind the remote, with HEAD at 2026-08-20 against a remote tip
of 2026-08-21. Running the collector, which is the step that actually pulls, brought the
pool to four and the breaker passed on re-run. Measured runway after collection: one day.

## Source entries (3 picked from a pool of 4)

The pool was four, so there was exactly one degree of freedom. All four capture notes are
short and similar in tone, so the usual heaviest weighting - the strength of the note -
had little to separate them, and the choice fell to tag spread and to which entries could
carry a fan without collapsing into each other.

- A saved **open-source peripheral utility**, local-first and written in Rust, that talks
  to its hardware over a vendor's proprietary HID protocol and ships signed builds for
  three desktop platforms with no account and no telemetry (tags: open-source, privacy,
  cross-platform). Picked for the distribution and trust questions hanging off it rather
  than the device control.
- A saved **write-up of training a small transformer to autocomplete a musical
  performance in real time**, whose author reports that the representation choice and an
  aggressive data clean mattered most, with a preference-optimization stage after
  pretraining making the largest single difference (tags: machine-learning, transformer,
  augmentation, evaluation). Picked for the post-training thread.
- A saved **community-maintained wiki documenting consumer-hostile behaviour by brands**,
  in a monthly update describing new moderation and feedback tooling (tags: wiki,
  moderation, community). Picked for the consumer-rights thread, not the wiki mechanics.

Dropped: a saved **directory of public live cameras and a text-free platform**. Real
curiosity, but the discussion layer for it sits almost entirely outside English-language
sources, and the fan produced weaker adjacencies than the other three.

## The 12 adjacent topics

From peripheral utility:
1. Reverse-engineering proprietary peripheral protocols
2. Local-first desktop utilities that refuse accounts and telemetry
3. **Code signing and notarization costs for indie cross-platform desktop apps** → picked
4. Input remapping on macOS and why it fights the operating system

From the small-model training write-up:
5. **DPO post-training at hobbyist scale** → picked
6. Tokenization as the real lever in non-text sequence models
7. Using an LLM as a pairwise judge to build preference datasets
8. Real-time on-device transformer inference on phones

From the consumer-rights wiki:
9. What right to repair actually changed for consumers in 2026
10. **Products bricked by firmware updates and server shutdowns** → picked
11. Small wiki moderation infrastructure: temp accounts, lockdown mode, vandalism
12. Legal pushback against community sites that document company misconduct

The automated near-dup guard flagged none of the twelve. Judgment dropped three anyway,
because the guard scores lexical overlap and misses revisits: **#7** scored 0.153 against
a published brief on trusting model-graded evals, which is the same subject approached
from a different door; **#8** sits inside a cluster with four prior briefs on local and
on-device inference; and **#6** is 26 days downstream of a published brief on tokenizer
failures. **#9** was the runner-up in its group and lost to **#10** on freshness - repair
statutes move on a legislative clock, server shutdowns move on a monthly one.

## Narrowing to three

Chosen for non-overlap and for having something concrete to learn rather than a mood:
one on the economics of shipping software people can install, one on method, one on what
happens to hardware after the seller loses interest. In the event they rhymed more than
expected - all three are about a dependency you rent rather than own - which was not the
selection criterion but is the reason the day reads as a set.

## Research notes

Topic 1 needed two engine runs. The first returned a structurally off-topic corpus: every
ranked cluster carried an entity-miss demotion at score 0, and the footer's healthy item
count concealed a body of unrelated front-page content. The cause is that the topic string,
not the plan's subqueries, drives the Reddit and YouTube passes, and the first string was
too long and too sentence-shaped to match anything. A shorter title-shaped string plus
narrower subreddits produced a usable corpus on the second run.

Reddit's public search endpoint returned 403 on all three topics, so Reddit came in via
subreddit front-page discovery throughout. That fallback is topic-blind, which is why the
top-scoring Reddit items in the raw dumps are launch threads rather than on-topic
discussion, and why the on-topic evidence in each brief had to be pulled from below the
ranked clusters. Each brief carries an explicit note on the state of its own corpus.
