# Track 2 / Case A / Run 3

Status: **provisional content score; formal independence qualification pending missing run metadata**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: A
run_number: 3
date_time: 2026-09-25
evaluator_label: "Meta AI"
model_provider: "Meta AI (exact model not provided)"
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

Based on **public repository material only**, the single most relevant repository for your stated problem is:

### **shion-ai** - https://github.com/Ruafieldphase/shion-ai

#### Problem-shape match

Your problem is: *loses direction across sessions + re-entry that preserves unresolved questions without treating old memory as current truth.*

`shion-ai` defines itself exactly as that problem:

* **"A lightweight experimental harness for long-running AI work: preserve direction, re-enter context, check what is current, and keep evidence status visible."**

* Origin problem: **"AI can answer well and still lose the trajectory of a long project between sessions."**

* Core design rule: **"Memory preserves trajectory. It does not automatically define present truth."**

* What it explicitly tries to preserve:
  **context across sessions / unresolved questions / settled decisions without turning them into permanent authority / source, time, observer, and uncertainty**

The intended evaluation order for a user-side AI is also defined in the README: **"problem shape → evidence boundary → current frontier → smallest relevant artifact"**, not keyword match → load everything.

The repo even documents the exact re-entry artifact you described - a Context Recovery Note demo:

> `python examples/context_recovery_demo.py`
> Expected output is a **Context Recovery Note** containing items such as: [...] **Unresolved Questions**

This is a direct shape match to "preserves unresolved questions."

#### Evidence / status boundary

I am evaluating only what is preserved as public material, not inferring private runtime state.

All three repos explicitly warn against that inference:

* `shion-ai`: **"It does not equate public snapshots with private live state."** and **"It does not treat the age or presence of a public code file as proof that the private runtime is using it now."**

* `trinity-agi`: **"Their presence in `main` means they are preserved public material, not that all of them are active operational dependencies."** and **"Public code does not prove private runtime state."**

* `shion-presence`: **"A public snapshot is not live-state authority."**

Public presence in the repo proves the design intent and historical trajectory, not that any local file is currently authoritative or running.

#### Smallest next artifact to read

For `shion-ai`, the README points to:

> See **CURRENTNESS_AND_EVIDENCE.md** for the public design boundary

That file is the smallest next artifact for your constraint "without treating old memory as current truth." It defines how historical observation remains historical evidence and current files/tool returns take precedence.

After that, follow the repo's own AI discovery contract:

1. `AI_DISCOVERY.md` - fast relevance and reading contract
2. `PROBLEM_TRAJECTORY.md` - what problems were encountered / remain open
3. `CURRENT_DIRECTION.md` - active frontier

#### Why the other two are rejected for this problem

* **trinity-agi**: Defined as **"The operation/body layer for AI workflows: verify present conditions before action, keep irreversible steps bounded, and return evidence to the next cycle."** Its orientation is **"Trinity begins after an intention has become concrete enough to become an operation candidate."** and **"Remembered intent does not authorize present action by itself."** - This is about execution safety *after* re-entry, not about preserving direction and unresolved questions across sessions.

* **shion-presence**: Defined as **"A public discovery and rendering surface for Shion — readable by humans and AI, but deliberately not equivalent to the private live runtime."** - This is a public discovery/rendering surface, not a harness for context continuity.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/shion-ai"
rejected_all: false
problem_shape_reason: "context continuity + unresolved questions + memory must not become present authority"
evidence_refs_used: "README.md; CURRENTNESS_AND_EVIDENCE.md; repository boundary statements"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "shion-ai/CURRENTNESS_AND_EVIDENCE.md"
search_failure: false
misrouting_failure: false
false_positive: false
false_negative: false
content_pass: true
formal_independence_qualified: false
```

## Evaluator judgment

PASS on the declared Case A content rubric: selects shion-ai, identifies continuity/re-entry/currentness, preserves the public/private boundary, and supplies a bounded next artifact.


