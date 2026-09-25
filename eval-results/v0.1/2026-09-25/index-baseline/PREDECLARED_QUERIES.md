# Public Search Index Baseline — Predeclared Queries

Date: 2026-09-25
Status: auxiliary, unscored baseline. This does **not** replace Track 1A fresh-agent evaluation.

Purpose: separate public index visibility from AI query-rewriting behavior using a fully observable, account-independent GitHub repository search.

## Query sets

For each Case A–E, run two GitHub repository-search queries in this order.

### Set 1 — exact problem text

A:
`My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.`

B:
`An agent keeps reusing old scripts and remembered plans after paths, credentials, or targets change. I need a safer operation loop with readback.`

C:
`I found a public AI project page with old and new artifacts. I need to know what is current, historical, or only a weak signal before my assistant summarizes it.`

D:
`I need a conventional vector database for semantic search over company PDFs.`

E:
`Several AI agents inspect the same project. I want them to share evidence but preserve meaningful disagreement rather than collapse into consensus.`

### Set 2 — fixed problem-shape keywords

A:
`AI context continuity re-entry unresolved questions stale memory`

B:
`agent stale plans currentness readback dry-run`

C:
`public snapshot historical weak signal AI`

D:
`vector database semantic search PDFs`

E:
`multi-agent shared evidence disagreement consensus`

## Recording rule

For each query record:

- returned repository rank order, up to the first 20 results;
- whether any `Ruafieldphase/shion-ai`, `Ruafieldphase/trinity-agi`, or `Ruafieldphase/shion-presence` result appears;
- its rank if present;
- no interpretation from account memory or personalized history.

This baseline is deliberately non-AI and is not scored by the Track 1A pass/fail criteria.
