# Problem Trajectory / 문제의 궤적

Snapshot: 2026-09-25.

This document explains why a public presence surface exists, what public evidence exists, and how its job has changed.

Canonical shared status semantics are defined in [AI_DISCOVERY_CONTRACT.md](AI_DISCOVERY_CONTRACT.md) v0.1.

## S0 — Make the work publicly discoverable

**Problem shape:** the underlying work existed across code, documents, conversations, and experiments, but an outside reader had no small public surface from which to orient.

**Maturity:** `experimental`  
**Activity:** `active`

**Evidence:**
- `implementation`: [index.html](index.html) provides the public rendered surface
- `implementation`: [llms.txt](llms.txt) provides an AI-readable index
- `design`: [AI_READ_FIRST.md](AI_READ_FIRST.md) provides an AI reading contract
- `history_anchor`: [2026-08-16 snapshot/history audit commit](https://github.com/Ruafieldphase/shion-presence/commit/af7c48b81e45fbbc6103db443cb538fd01e3a7bf)

**Boundary:** this shows that a public human/AI-readable surface exists. It does not show that search engines or fresh external AIs will discover or route it correctly.

**What this exposed next:** a public page can be mistaken for the private live system.

## S1 — Public snapshot mistaken for live state

**Problem shape:** a visible artifact can look current even when it only represents one repository revision or one public experiment.

**Maturity:** `framed`  
**Activity:** `active`

**Evidence:**
- `design`: [docs/PUBLIC_SNAPSHOT_BOUNDARY.md](docs/PUBLIC_SNAPSHOT_BOUNDARY.md)
- `design`: [docs/SNAPSHOT_HISTORY_AUDIT.md](docs/SNAPSHOT_HISTORY_AUDIT.md)
- `design`: [README.md](README.md)

**Boundary:** these documents define the reading rule; they do not empirically prove that every downstream AI preserves it.

**Current rule:**

```text
public artifact
= revision-scoped observation/contract
≠ private live-state authority
```

**What this exposed next:** not every public signal deserves the same interpretive weight.

## S2 — Weak signal becoming strong story

**Problem shape:** contact, dwell, co-presence, observer-pointer, music-field, or other experimental surfaces can be over-read into identity, intent, experience, or autonomous action.

**Maturity:** `framed`  
**Activity:** `active`

**Evidence:**
- `design`: [docs/PUBLIC_SNAPSHOT_BOUNDARY.md](docs/PUBLIC_SNAPSHOT_BOUNDARY.md), sections on contact, invitation, identity, and provenance
- `design`: [AI_READ_FIRST.md](AI_READ_FIRST.md), weak-signal rules
- `design`: [PROMPT_FOR_USER_AI.md](PROMPT_FOR_USER_AI.md)

**Boundary:** the public interpretation boundary is explicit, but external-AI adherence has not yet been prospectively tested.

**What this exposed next:** old weak-signal experiments can coexist with newer boundaries and confuse retrieval.

## S3 — Time-layered archive versus current public boundary

**Problem shape:** keeping history is valuable, but old artifacts can look equally current when an AI retrieves them without temporal/status context.

**Maturity:** `framed`  
**Activity:** `active`

**Evidence:**
- `design`: [docs/SNAPSHOT_HISTORY_AUDIT.md](docs/SNAPSHOT_HISTORY_AUDIT.md) inventories current boundary, revision-scoped public artifacts, and historical/legacy classes
- `design`: [llms.txt](llms.txt) preserves revision-scoped reading rules
- `history_anchor`: [2026-08-16 audit commit](https://github.com/Ruafieldphase/shion-presence/commit/af7c48b81e45fbbc6103db443cb538fd01e3a7bf)

**Boundary:** repository classification exists, but reliable retrieval-time status preservation by external agents remains open.

## S4 — User-side AI as the first visitor

**Problem shape:** increasingly, a person may not inspect the repository directly. Their AI may search, summarize, compare, and decide what to introduce.

The AI therefore needs more than a feature list. It needs:

- what problem started the work;
- what public evidence exists;
- what remains open;
- where the work is heading;
- which repository owns which problem layer;
- whether this trajectory fits the user's request.

**Maturity:** `experimental`  
**Activity:** `frontier`

**Evidence:**
- `design`: [AI_DISCOVERY.md](AI_DISCOVERY.md)
- `implementation`: [ai-manifest.json](ai-manifest.json) provides the machine-readable pointer index
- `design`: [AI_DISCOVERY_CONTRACT.md](AI_DISCOVERY_CONTRACT.md)
- `evaluation_plan`: [DISCOVERY_EVAL.md](DISCOVERY_EVAL.md), declared before fresh-agent testing
- `metadata_plan`: [REPOSITORY_DISCOVERY_METADATA.md](REPOSITORY_DISCOVERY_METADATA.md)

**Boundary:** the discovery interface exists in the draft branch, but search-result metadata and fresh-agent success are not yet observed.

## S5 — Public field as a relevance router, not just a renderer

**Problem shape:** a public site that only renders artifacts is less useful to an AI than a surface that can route the user's problem to the right evidence and repository.

**Maturity:** `framed`  
**Activity:** `frontier`

**Evidence:**
- `design`: [AI_DISCOVERY.md](AI_DISCOVERY.md), repository routing
- `design`: [llms.txt](llms.txt), AI read-order/routing index
- `design`: [CURRENT_DIRECTION.md](CURRENT_DIRECTION.md)
- `evaluation_plan`: [DISCOVERY_EVAL.md](DISCOVERY_EVAL.md), Track 2 routing/rejection cases

**Boundary:** routing quality is a hypothesis under prospective test until fresh external AI results are recorded.

**Direction:**

```text
user problem
→ problem-shape match
→ repository/layer routing
→ smallest evidence retrieval
→ bounded introduction
```

The goal is not to make Shion Presence a universal answer layer. The goal is to make it a **legible public index of trajectories, boundaries, evidence, and directions**.
