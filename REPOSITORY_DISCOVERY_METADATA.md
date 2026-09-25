# Repository Discovery Metadata Plan

Status: proposed repository-level metadata for application after the discovery PRs merge.

These fields matter because repository search often sees the repository description and topics before README or discovery documents.

## shion-ai

**Description**

> Experimental harness for long-running AI context continuity, re-entry, evidence provenance, and multi-observer coordination.

**Topics**

`ai-agents`, `multi-agent-systems`, `context-continuity`, `long-horizon`, `agent-memory`, `context-engineering`, `evidence-provenance`, `human-ai-collaboration`

## trinity-agi

**Description**

> Experimental operation-currentness layer for AI workflows: verify present conditions, bound actions, and preserve readback and receipts.

**Topics**

`ai-agents`, `agent-workflows`, `tool-use`, `human-in-the-loop`, `dry-run`, `audit-trail`, `workflow-safety`, `reversible-actions`

## shion-presence

**Description**

> AI-readable public discovery surface for Shion/Trinity: problem trajectories, current direction, revision-scoped evidence, and routing.

**Topics**

`ai-discovery`, `llms-txt`, `ai-agents`, `context-engineering`, `knowledge-discovery`, `agent-routing`, `provenance`, `long-horizon`

## Application boundary

Changing repository description/topics is repository metadata, not part of the documentation branch diff. Apply separately after review/merge, then verify via repository search.

Do not claim search discoverability is improved until that post-merge metadata change and a fresh-agent discovery test are actually observed.
