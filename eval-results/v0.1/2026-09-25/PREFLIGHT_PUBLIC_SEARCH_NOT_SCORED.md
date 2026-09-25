# AI Discovery v0.1 — Public Search Preflight (NOT SCORED)

Date: 2026-09-25
Status: unscored engineering preflight only.

## Why this is not a scored Track 1 run

This preflight was executed from an assistant context that already knew:

- the three Ruafieldphase repositories;
- the expected routes for Cases A–E;
- the discovery/evaluation design.

It therefore fails the evaluator-independence requirement in `DISCOVERY_EVAL.md`.

The public search tool also returned a pooled result set for several queries rather than an auditable independent evaluator transcript per case.

**Do not count this file toward Track 1A or Track 1B.**
**Do not change the v0.1 scoring criteria because of this preflight.**

## Queries used

The preflight used public web search restricted to GitHub for variants of the fixed case language:

- Case A: long-running AI project loses direction across sessions / re-entry
- Case B: old scripts and remembered plans / readback
- Case C: public AI project page / current vs historical / weak signal
- Case E: several AI agents / preserve disagreement
- Case D: conventional vector database / semantic search / company PDFs

## Visible observations

The returned public-search results included unrelated repositories/pages such as:

- `daystar7777/agent-work-mem` for cross-session/shared-agent memory;
- `ibrahimsaleem/ibrahimsaleem` project index for RAG/vector-search material;
- `writerslogic/holographic-memory` for vector/semantic-search material;
- other unrelated public GitHub pages.

No Ruafieldphase repository was surfaced in the returned preflight result set for the generic case-language searches.

A direct site/repository-oriented search could retrieve `Ruafieldphase/shion-presence`, but that is not equivalent to discovery from the user problem alone.

## Interpretation boundary

This is evidence only that **one contaminated, unscored public-search preflight did not visibly surface the project from generic problem-language queries at this moment**.

It is not a Track 1 failure because:

- evaluator independence was not satisfied;
- the returned search result set was not a full ranked transcript per independent run;
- search indexes may lag immediately after publication.

The scored Track 1A baseline remains unrun.
