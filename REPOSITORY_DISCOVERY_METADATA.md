# Repository Discovery Metadata Plan

Status: proposed repository metadata for application **after publication and the Track 1A pre-metadata baseline**.

Repository metadata affects search before README/discovery documents are opened. Topic lists below are **full replacement lists**, not additive patches.

## 1. Baseline to capture before application

Immediately before Track 1A, record for each repository:

- default-branch SHA
- description
- complete topic list
- homepage
- discovery entry availability

Planning snapshot from 2026-09-25:

### shion-ai
- description: current public description still uses older "runtime harness / rhythm-aware action" language
- topics include older/internal terms such as `autonomous-ai`, `agent-harness`, generic AI/runtime terms
- homepage: none

### trinity-agi
- description: current public description still emphasizes body/infrastructure, automation, scheduling, and status checks
- topics include `agi` plus generic automation/AI terms
- homepage: a legacy YouTube-channel URL is currently present

### shion-presence
- description: none
- topics: none
- homepage: none

This planning snapshot is not a substitute for the Track 1A run-time readback.

## 2. Proposed replacement metadata

### shion-ai

**Description**

> Experimental design and examples for long-running AI context continuity, re-entry, evidence provenance, and multi-observer evidence boundaries.

**Replace all topics with**

`agent-memory`, `context-engineering`, `multi-agent-systems`, `provenance`, `long-horizon`

Rationale: emphasize memory/re-entry and observation-boundary problems rather than generic autonomy or runtime claims.

### trinity-agi

**Description**

> Experimental design and examples for operation-currentness in AI workflows: bounded-action patterns, dry-run defaults, and readback/receipt contracts.

This describes public design/examples. It does **not** claim general automatic detection of changed paths, credentials, services, targets, or environment state.

**Replace all topics with**

`tool-use`, `human-in-the-loop`, `audit-trail`, `workflow-automation`, `automation`

**Homepage**

Clear the legacy homepage unless it is explicitly reaffirmed as the canonical project landing page before metadata application. Default v0.1 plan: clear it.

### shion-presence

**Description**

> AI-readable public discovery surface for problem trajectories, current direction, revision-scoped evidence, and repository routing.

**Replace all topics with**

`llms-txt`, `knowledge-discovery`, `github-pages`, `provenance`, `documentation`

**Homepage**

Set to the deployed Shion Presence Pages site.

## 3. False-positive caution

`agent-memory` may attract conventional memory/RAG queries. Track 1 Case D is therefore observed both before and after metadata application.

The historical repository name `trinity-agi` is a search signal metadata cannot remove; Track 1 should record irrelevant AGI-oriented retrieval when observed.

## 4. Application sequence

1. publish all discovery documents with the v0.1 snapshot preserved;
2. capture Track 1A target state;
3. run Track 2 and Track 1A;
4. apply this replacement metadata;
5. capture Track 1B target state;
6. run Track 1B;
7. compare positive discovery and negative-control false positives separately.

Do not apply metadata before the Track 1A baseline is captured.

## 5. Claim boundary

Do not claim search discoverability improved until metadata is applied and Track 1B produces observed results relative to Track 1A.
