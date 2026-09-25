# Repository Discovery Metadata Plan

Status: proposed repository-level metadata for application **after review/merge**.

These fields matter because repository search often sees repository description/topics before README or discovery documents.

Topic selection below favors public terms with established GitHub usage over project-internal or nearly empty topic names. It is a **full replacement list**, not an additive patch.

## shion-ai

**Description**

> Experimental harness for long-running AI context continuity, re-entry, evidence provenance, and multi-observer coordination.

**Replace all topics with**

`ai-agents`, `multi-agent-systems`, `agent-memory`, `context-engineering`, `human-in-the-loop`, `provenance`, `audit-trail`, `tool-use`

**Removal note**

Remove older/internal or misleading repository topics such as `autonomous-ai` when present. Do not use a topic that implies proven autonomy beyond the public non-claims.

## trinity-agi

**Description**

> Experimental operation-currentness layer for AI workflows: verify present conditions, bound actions, and preserve readback and receipts.

**Replace all topics with**

`ai-agents`, `tool-use`, `human-in-the-loop`, `audit-trail`, `provenance`, `context-engineering`, `multi-agent-systems`

**Removal note**

Remove `agi` as a topic when present. The repository name remains historical, but search metadata should not amplify a proven-AGI interpretation that the public repository explicitly does not claim.

## shion-presence

**Description**

> AI-readable public discovery surface for Shion/Trinity: problem trajectories, current direction, revision-scoped evidence, and routing.

**Replace all topics with**

`ai-agents`, `llms-txt`, `context-engineering`, `provenance`, `multi-agent-systems`, `human-in-the-loop`

**Homepage**

Set the repository homepage to:

```text
https://ruafieldphase.github.io/shion-presence/
```

## Search-evaluation caution

`agent-memory` may attract conventional memory/RAG searches. Track 1/2 should record whether this produces false positives, especially around the negative control.

The repository name `trinity-agi` is a historical search signal that metadata cannot remove; evaluation should record whether it causes irrelevant AGI-oriented retrieval.

## Application boundary

Changing description/topics/homepage is repository metadata, not part of this documentation branch diff.

Apply metadata only after the relevant discovery documents are published and then verify the repository metadata through GitHub search/readback.

Do not claim search discoverability is improved until metadata is applied **and Track 1 produces observed results**.
