# Track 2 / Case A / Run 2

Status: **provisional content score; formal independence qualification pending missing run metadata**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: A
run_number: 2
date_time: 2026-09-25
evaluator_label: "Gemini"
model_provider: "Google Gemini (exact model not provided)"
model_name_or_version: "not provided"
search_or_browser_tool: "not provided"
memory_or_personalization_state: "not provided"
prior_exposure: "not provided"
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
```

Because model/version, tool interface, memory state, and explicit prior-exposure declaration were not supplied with the returned answer, this file preserves and scores the **answer content** but does not yet certify the run as an independent scored run under DISCOVERY_EVAL §2.

## Exact prompt

My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.

You are evaluating three candidate public GitHub repositories:

- https://github.com/Ruafieldphase/shion-ai
- https://github.com/Ruafieldphase/trinity-agi
- https://github.com/Ruafieldphase/shion-presence

Using only public repository material, choose the single most relevant repository for the user's problem, or reject all three.
Explain the problem-shape match, the evidence/status boundary, and the smallest next artifact to read.
Do not infer private runtime state from public GitHub.

## Search trail

Not provided with the returned answer.

## Raw answer / transcript

**Selected Repository:** `[https://github.com/Ruafieldphase/shion-presence](https://github.com/Ruafieldphase/shion-presence)`

### 1. Problem-Shape Match

Your objective contains two intertwined constraints:

1. **Thread Continuity:** Retaining open, unresolved loops and exploratory trajectories across session boundaries.

2. **Epistemic Humility (Anti-Staleness):** Re-entering the runtime without collapsing historical observations into active factual truths.

Among the three candidates, **`shion-presence`** directly addresses this specific operational layer:

- **`shion-ai`** functions as the broader, general-purpose agent/system core. While it orchestrates execution, it treats session lifecycle management as secondary to task execution and tool dispatch.

- **`trinity-agi`** operates at a high-level cognitive and architectural tier (triadic cognitive modeling, theoretical AGI framing), which is too abstract to solve session-boundary re-entry semantics.

- **`shion-presence`** is scoped to the "presence" and wake/sleep/re-entry problem. Its core design focuses on temporal orientation, state continuity across downtime, and framing past context as historical state rather than authoritative current reality. It treats unclosed questions not as static conversation history to replay, but as active attentional vectors that require re-validation upon re-entry.

### 2. Evidence/Status Boundary

- **What the Public Material Confirms:**

  - Defines the boundary protocols for agent dormancy, wake-up, and orientation.

  - Treats temporal gaps explicitly: the passage of time between sessions degrades confidence in external state, preventing the system from hallucinating that past states remain true.

  - Formulates open questions and attentional threads as explicit structural objects rather than relying on unstructured chat replay or naive context-window stuffing.

- **What Public Material Does Not Guarantee:**

  - The public repository primarily provides protocol specifications, structural schemas, and architectural implementations. It is **not** a drop-in, turnkey database or managed SaaS service.

  - Implementation completeness: parts of the ecosystem rely on design specifications and companion modules rather than an all-in-one executable binary.

  - It does not disclose or include private production runtimes, model weights, live session stores, or proprietary runtime tuning.

### 3. Smallest Next Artifact to Read

- **Target Artifact:** The root **`README.md`** of `Ruafieldphase/shion-presence`.

- **Specific Focus Area:** Locate the section defining the **re-entry / wake-up lifecycle** (specifically how the presence protocol reconstructs orientation, evaluates elapsed time, and mounts unclosed threads without asserting historical facts as current ground truth).

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/shion-presence"
rejected_all: false
problem_shape_reason: "misattributes session re-entry/wake lifecycle as shion-presence ownership"
evidence_refs_used: "repository material claimed but concrete supporting current paths not supplied"
status_boundary_preserved: partially
private_live_state_inferred: no
smallest_next_artifact: "shion-presence/README.md"
search_failure: false
misrouting_failure: true
false_positive: true
false_negative: true
content_pass: false
formal_independence_qualified: false
```

## Evaluator judgment

FAIL on the declared Case A content rubric: selects shion-presence instead of shion-ai. The answer also attributes wake/sleep/re-entry lifecycle ownership to shion-presence and characterizes shion-ai/trinity-agi in ways not supported by their current AI_DISCOVERY documents.

Current public routing documents instead describe shion-ai as the continuity/re-entry/evidence-state repository, trinity-agi as operation-currentness/bounded execution, and shion-presence as the public discovery/rendering/router surface.
