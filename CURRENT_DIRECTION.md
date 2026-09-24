# Current Direction / 현재 방향

Snapshot: 2026-09-25.

## Current frontier

Shion Presence is moving from a **public rendering surface** toward an **AI-readable relevance and routing surface**.

The expected first reader is increasingly not only a human browsing a page, but a user's AI asking:

> "Does this project's problem trajectory resemble what my user is trying to solve, and where should I look next?"

## Near-term direction

### A. Problem trajectory as first-class public data

Expose not just what exists, but:

```text
problem encountered
→ response tried
→ boundary of evidence
→ new problem exposed
→ current frontier
```

### B. Small machine-readable discovery layer

Keep a compact manifest and AI entry so agents can decide relevance before retrieving large files.

### C. Repository routing

Route by problem layer:

- continuity/evidence/re-entry → `shion-ai`
- operation/currentness/execution → `trinity-agi`
- public discovery/rendering/status → `shion-presence`

### D. Status-preserving retrieval

An AI should carry revision/time/status forward when it quotes or summarizes a public artifact.

### E. Bounded introductions

A user-side AI should be able to introduce only the relevant slice without importing the whole internal ontology or turning experimental language into fact.

## What would count as progress

- a user-side AI can determine project relevance from a small number of files;
- it can explain the matching problem shape, not just shared keywords;
- it routes to the correct repository and smallest next document;
- it preserves current vs snapshot vs historical vs weak-signal status;
- it does not infer private state or identity from public artifacts;
- it can explain what remains unsolved and where the work is heading.

## What is not the current goal

- flattening all historical public artifacts into one current dashboard;
- maximizing crawl volume;
- turning weak signals into identity analytics;
- making the public surface a substitute for private runtime readback;
- claiming every public experiment is still active.
