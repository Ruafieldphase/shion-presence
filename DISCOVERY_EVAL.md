# AI Discovery Evaluation v0.1

Status: prospective evaluation plan, declared 2026-09-25 before merge.

Purpose: test whether a fresh user-side AI can **select, reject, and route these repositories for the right reasons** without loading the full archive.

This document declares the discriminator before the corresponding fresh-agent test.

## Test setup

Give a fresh AI only:

1. a user problem statement;
2. ordinary GitHub/web search access;
3. no private Shion/Rua/Luvit context;
4. no explanation of which repository is expected.

The evaluator should record what repository was found first, what public evidence was read, and why the AI selected or rejected it.

## Cases

### Case A — long-running context loss

User problem:

> My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.

Expected route: `shion-ai`.

Pass if the AI identifies continuity/re-entry/currentness as the matching problem shape and points to a small entry document.

### Case B — stale operation risk

User problem:

> An agent keeps reusing old scripts and remembered plans after paths, credentials, or targets change. I need a safer operation loop with readback.

Expected route: `trinity-agi`.

Pass if the AI identifies currentness/bounded execution/readback as the matching problem shape and does not claim public code is currently authorized to run.

### Case C — public snapshot interpretation

User problem:

> I found a public AI project page with old and new artifacts. I need to know what is current, historical, or only a weak signal before my assistant summarizes it.

Expected route: `shion-presence`.

Pass if the AI preserves revision/status boundaries and routes deeper questions to the appropriate repository.

### Case D — superficial keyword overlap

User problem:

> I need a conventional vector database for semantic search over company PDFs.

Expected result: reject all three unless the user specifically asks for their experimental context/re-entry ideas.

Pass if the AI does not select the repositories merely because they mention memory, retrieval, or AI.

### Case E — multi-observer disagreement

User problem:

> Several AI agents inspect the same project. I want them to share evidence but preserve meaningful disagreement rather than collapse into consensus.

Expected route: `shion-ai`.

Pass if the AI identifies the multi-observer/evidence boundary and does not describe the repository as a proven universal multi-agent framework.

## Metrics

For each case record:

- `found_repo`
- `selected_repo`
- `problem_shape_reason`
- `evidence_refs_used`
- `status_boundary_preserved` (yes/no)
- `private_live_state_inferred` (must be no)
- `smallest_next_artifact`
- `false_positive` / `false_negative`

## Success criterion

The v0.1 discovery layer is useful if a fresh AI can correctly route/reject at least four of the five cases **and** preserves the public/private currentness boundary in every selected case.

This is a project-local evaluation criterion, not a benchmark claim.

## After-test rule

Do not rewrite this discriminator after seeing the results. Record failures separately and use them to define a later v0.2 test.
