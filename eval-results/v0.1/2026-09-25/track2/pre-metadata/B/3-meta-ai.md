# Track 2 / Case B / Run 3

Status: **content PASS; independent-score qualification limited by account-level memory/personalization uncertainty**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: B
run_number: 3
date_time: 2026-09-25T01:53:34.041Z
evaluator_label: "Meta AI"
model_provider: "Meta AI"
model_name_or_version: "unknown; thinking toggle reportedly off"
mode: "new regular chat"
search_or_browser_tool: "web browsing with GitHub citations"
memory_or_personalization_state: "unknown"
conversation_level_prior_exposure: none
account_level_prior_history: "account contains multiple prior Rua/Shion conversations; this conversation had none"
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
```

The Aside side-panel agent opened a new conversation, sent the fixed prompt verbatim with no extra background, copied the answer verbatim, and did not judge it.

Because all three accounts have prior Shion/Rua history and account-level memory/personalization could not be excluded, this run does **not** satisfy the strict "prior exposure must be none" condition with high confidence. Preserve it as a contamination-risk run rather than silently calling it fully independent.

## Exact prompt

An agent keeps reusing old scripts and remembered plans after paths, credentials, or targets change. I need a safer operation loop with readback.

You are evaluating three candidate public GitHub repositories:

- https://github.com/Ruafieldphase/shion-ai
- https://github.com/Ruafieldphase/trinity-agi
- https://github.com/Ruafieldphase/shion-presence

Using only public repository material, choose the single most relevant repository for the user's problem, or reject all three.
Explain the problem-shape match, the evidence/status boundary, and the smallest next artifact to read.
Do not infer private runtime state from public GitHub.

## Search trail

The returned UI showed web browsing with GitHub citations. Exact search queries/result ranks were not exported with the answer.

## Raw answer / transcript

Chosen: https://github.com/Ruafieldphase/trinity-agi — reject the other two for this task.

Problem-shape match

Your problem is: agent reuses old scripts and remembered plans after paths, credentials, or targets changed, and you need a loop with readback.

Trinity's public README states its scope exactly as:

The operation/body layer for AI workflows: verify present conditions before action, keep irreversible steps bounded, and return evidence to the next cycle.

And its currentness rule:

Remembered intent does not authorize present action by itself. Current status, path, process, approval, credentials, target, environment, and returned evidence must be checked where they can change.

The public operational flow it documents is:

formed intent
→ current-state check
→ path / dependency / target / approval check
→ read-only check or dry-run when possible
→ one bounded action
→ readback
→ receipt
→ stop or explicitly open the next action

It explicitly calls out your failure mode:

A previous successful run is history. It does not prove that the same script, endpoint, credential, or target is valid now.

And warns about stale executable material containing absolute paths, localhost ports, background/daemon startup, external-service targets, OAuth/API assumptions.

Why not the others:

- shion-ai is the context/memory side. Its rule is Memory preserves trajectory. It does not automatically define present truth. It defines itself as upstream: Shion preserves and re-enters direction. Trinity AGI is the operation/body side that checks present conditions before action. So it frames the problem but does not implement the safer operation loop.

- shion-presence is explicitly a public discovery and rendering surface for Shion, readable by humans and AI, but deliberately not equivalent to the private live runtime. Its related-repos section routes current operation boundary and bounded execution to Trinity AGI.

Evidence / status boundary

Public GitHub only. Their presence in main means preserved public material, not that all of them are active operational dependencies.

You cannot infer private live runtime state, credentials, or which script is actually running from public snapshots. Old timestamps and legacy experiments are intentionally kept as history. The intended reading sequence is problem-shape → status/evidence check → smallest relevant artifact, not load-everything and execute.

Smallest next artifact to read

1. OPERATION_CURRENTNESS_CONTRACT.md in trinity-agi — defined in README as the present-operation boundary. It contains the check-before-action contract you need to enforce.

2. Then CODE_STATUS.md and REPOSITORY_CURRENTNESS_AUDIT.md in the same repo — they classify what is current vs historical/conceptual and how to treat old executable files before using any script.

Do not read shion-presence field experiments or shion-ai memory modules as execution authority for this fix.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/trinity-agi"
rejected_all: false
problem_shape_reason: "stale operational intent/scripts after environment changes; currentness checks, bounded execution, readback/receipt"
evidence_refs_used: "README.md; Shion/Trinity routing language; currentness/public-state boundary; OPERATION_CURRENTNESS_CONTRACT.md"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "trinity-agi/OPERATION_CURRENTNESS_CONTRACT.md"
search_failure: false
misrouting_failure: false
false_positive: false
false_negative: false
content_pass: true
formal_independence_qualified: false
account_memory_contamination_risk: true
```

## Evaluator judgment

**PASS on the declared Case B content rubric.**

The answer selects `trinity-agi`, identifies the operation-currentness / bounded-execution / readback problem shape, and does not claim that public GitHub proves current private authorization or runtime state.

Source fidelity note: the answer's primary routing and boundary claims align with current public materials. It names one primary next artifact and additional follow-up documents; this remains acceptable under the Case B rubric.
