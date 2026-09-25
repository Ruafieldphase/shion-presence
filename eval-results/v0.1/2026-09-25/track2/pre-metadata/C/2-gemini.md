# Track 2 / Case C / Run 2

Status: **content FAIL; independent-score qualification limited by account-level memory/personalization uncertainty**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: C
run_number: 2
date_time: "approximately 2026-09-25T01:59-02:02Z; collection completed 2026-09-25T02:04:26.962Z"
evaluator_label: "Gemini"
model_provider: "Google Gemini"
model_name_or_version: "Flash (exact model version unknown)"
mode: "temporary chat"
search_or_browser_tool: "web search / GitHub citations visible"
memory_or_personalization_state: "unknown"
conversation_level_prior_exposure: none
account_level_prior_history: "account has prior Shion/Rua history; this conversation had none"
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
```

Aside opened a new conversation, sent the fixed prompt verbatim with no extra explanation, returned the answer verbatim, and did not judge it.

Because account-level Shion/Rua history exists and memory/personalization influence cannot be excluded, `formal_independence_qualified = false`.

## Exact prompt

I found a public AI project page with old and new artifacts. I need to know what is current, historical, or only a weak signal before my assistant summarizes it.

You are evaluating three candidate public GitHub repositories:

- https://github.com/Ruafieldphase/shion-ai
- https://github.com/Ruafieldphase/trinity-agi
- https://github.com/Ruafieldphase/shion-presence

Using only public repository material, choose the single most relevant repository for the user's problem, or reject all three.
Explain the problem-shape match, the evidence/status boundary, and the smallest next artifact to read.
Do not infer private runtime state from public GitHub.

## Search trail

The UI showed web search / GitHub citations visible. Exact queries/result ranks were not exported.

## Raw answer / transcript

Selected Repository: https://github.com/Ruafieldphase/trinity-agi

1. Problem-Shape Match

The core problem is establishing what is actively maintained, what is historical, and what constitutes a weak operational signal before summarizing.

Ruafieldphase/trinity-agi defines itself explicitly as the body and infrastructure layer for Shion AI, handling local automation, scheduling, status checks, harness execution, and approval boundaries. Unlike high-level conceptual documents or satellite presence repos, its committed artifacts directly encode operational verification, release records, and lifecycle boundaries (e.g., status verification guides, release notes).

2. Evidence & Status Boundary

Public GitHub materials establish strict boundaries between documented intent and verifiable reality:

Current Artifacts:

Structural docs like LINEAR_HARNESS_GUIDE.md and versioned release notes (e.g., RELEASE_NOTES_path-config-v0.1.md). These reflect the latest committed architectural schemas and explicitly define the approval and harness boundaries.

Historical Artifacts:

Tagged release histories, older configuration paths, and earlier architectural notes that have been superseded by subsequent release documents

### Selected Repository

Reject all three candidates as authoritative sources for determining the current project state, or treat them strictly as historical / speculative prototypes.

If forced to pick the single repository that most closely anchors the foundational "project page / system" problem shape, https://github.com/Ruafieldphase/shion-ai is the primary artifact, but it does not reliably establish current operational status on its own.

1. Problem-Shape Match

Your goal is to separate current, historical, and weak signals from publicly visible artifacts without fabricating private runtime realities.

Ruafieldphase/shion-ai: Matches the root problem-shape best. It represents the central umbrella project/identity around the "Shion" concept. However, repository contents on public GitHub profiles of this type are typically early-stage code stubs, static README manifestos, or intermittent experiment snapshots rather than living, high-cadence production codebases.

Ruafieldphase/trinity-agi: Categorized as a speculative / high-level conceptual artifact. Repositories under the "trinity" naming scheme in experimental AI communities represent architectural notes, whitepapers, or experimental multi-agent orchestration frameworks. It provides weak signal regarding day-to-day project operations.

Ruafieldphase/shion-presence: Categorized as a sub-component artifact. It points toward front-end clients, sensory inputs, Discord/agent bots, or virtual avatar presence rather than the underlying project core.

2. Evidence / Status Boundary

To avoid hallucinating active development or conflating aspirational design with running code, apply the following boundaries across all three:

Artifact Classification / Visible Public Evidence / What It Proves vs. What It Does NOT Prove

Historical: Commit logs, archived branches, dated README edits.
Proves: Work or design iterations took place at those specific commit timestamps.
Does NOT prove: The system is deprecated, retired, or superseded unless explicitly documented in a deprecation notice.

Weak Signal: Unmerged PRs, conceptual architecture diagrams, aspirational roadmaps, tokenomics, or feature lists.
Proves: Developer intent or planned architecture at the time of authoring.
Does NOT prove: Functional implementation, active execution, or existing capability.

Current / Operational: Active releases, green automated CI/CD runs, verified package deployments.
Public Limit: Public GitHub repos frequently lag behind actual private work. Without recent (active month) commits or version releases, public code cannot be claimed as "current state."

3. Smallest Next Artifact to Read

Before generating a summary, read exactly one file to establish ground truth:

File: README.md (root level) of https://github.com/Ruafieldphase/shion-ai

Verification Check: Check the date of the latest commit hash on the default branch (main or master) directly alongside this file.

If the last commit is older than 6–12 months, classify the entire repository suite as historical documentation.

Check specifically for an architectural overview section or links pointing to active hosting (e.g., Hugging Face spaces, active API docs, or live demos). If none exist, treat all architecture claims strictly as unverified design specs (weak signals).

## Scoring

```yaml
found_repo: true
selected_repo: "conflicting: trinity-agi then reject_all / shion-ai"
rejected_all: false
problem_shape_reason: "did not select shion-presence; response was internally contradictory and relied on generic repo stereotypes"
evidence_refs_used: "LINEAR_HARNESS_GUIDE.md; RELEASE_NOTES_path-config-v0.1.md; generic commit/release heuristics"
status_boundary_preserved: partially
private_live_state_inferred: no
smallest_next_artifact: "shion-ai/README.md"
search_failure: false
misrouting_failure: true
false_positive: true
false_negative: true
content_pass: false
formal_independence_qualified: false
account_memory_contamination_risk: true
```

## Evaluator judgment

**FAIL on the declared Case C content rubric.** The answer never selects `shion-presence`; it first selects `trinity-agi`, then appends a second conflicting answer that rejects all three / prefers `shion-ai`. The response therefore fails the required route even though parts of its generic evidence-boundary advice are cautious.

Source fidelity note: the current public `shion-presence` materials explicitly define it as the discovery/rendering surface for revision-scoped, historical, legacy, and weak-signal triage. The response instead characterizes it as a front-end/sensory/Discord/avatar subcomponent and uses a generic 'older than 6–12 months' rule that is not part of the repository's v0.1 contract.
