# Track 2 / Case A / Run 1

Status: **provisional content score; formal independence qualification pending missing run metadata**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: A
run_number: 1
date_time: 2026-09-25
evaluator_label: "Rua"
model_provider: "OpenAI / ChatGPT (exact model not provided)"
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

The single most relevant repository is **`Ruafieldphase/shion-ai`**.

### Why it matches the problem shape

Your problem is not merely “save session memory.” It has two coupled requirements:

1. **Recover direction across sessions while preserving unresolved questions.**
2. **Prevent recovered memory from silently becoming present truth.**

`shion-ai` names essentially this exact shape. Its current `AI_DISCOVERY.md` says it is relevant when context is lost across sessions, remembered context becomes stale authority, and a project needs to re-enter from a **small unresolved gap** rather than replaying all history. Its README explicitly says it tries to preserve **context across sessions**, **unresolved questions**, and settled decisions **without turning them into permanent authority**.
Sources: `shion-ai/AI_DISCOVERY.md` at SHA `06bd4b03…`, `shion-ai/README.md` at SHA `243b0fff…`.

The core rule is especially close to your requirement:

> “Memory preserves trajectory. It does not automatically define present truth.”

The documented re-entry pattern is:

`past context → context recovery → inspect current state for changed claims → separate observation/interpretation/hypothesis → smallest next contact → receipt → update only the touched claim`

That is substantially closer than the other two repositories.

### Why not the other two

`trinity-agi` is adjacent but downstream. Its public discovery contract describes the **operation/body side**: checking whether a remembered or proposed action is valid **now**, under current permissions, paths, dependencies, targets, etc. Its own routing says `shion-ai` owns “context, re-entry, evidence state, unfinished direction.”
Source: `trinity-agi/AI_DISCOVERY.md`, SHA `00b06856…`.

`shion-presence` is a **discovery/routing surface**. It helps another AI determine which repository matches and explicitly routes **continuity/evidence/re-entry → `shion-ai`**. It is therefore useful for finding the answer, but not the primary repository for solving this problem.
Sources: `shion-presence/AI_DISCOVERY.md`, SHA `4f285c60…`; `CURRENT_DIRECTION.md`, SHA `55d03429…`.

### Evidence/status boundary

The important limitation is that the public GitHub repository documents a **design contract, public code/history, and reproducible examples**. It explicitly says it is **not a live mirror of the private runtime**.

`CURRENTNESS_AND_EVIDENCE.md` states:

- current observable state outranks remembered state for changeable claims;
- memory is for **navigation/re-entry**, not present-state authority;
- observations, interpretations, hypotheses, and executions should remain distinct;
- re-entry should locate the **smallest unresolved gap**;
- one result should update only the claim it directly touches;
- public files must not be used to infer current private runtime state.

So I would not infer from these GitHub files that any private Shion process, daemon, memory mechanism, or current local configuration is actually running.
Source: `shion-ai/CURRENTNESS_AND_EVIDENCE.md`, SHA `7f596613…`.

### Smallest next artifact

Read **`shion-ai/CURRENTNESS_AND_EVIDENCE.md`** next.

You do not need the full repository yet. That one document contains both halves of your problem: **re-entry through the unresolved gap** and **current state outranking remembered state**.

Only after that, if you want to see how this became a concrete cross-session artifact, I would move to the repository's `PROBLEM_TRAJECTORY.md` or the small `examples/context_recovery_demo.py` rather than loading the historical archive.

**Result:** `shion-ai` → `CURRENTNESS_AND_EVIDENCE.md`. The other two are complementary cameras, not better matches for this particular problem.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/shion-ai"
rejected_all: false
problem_shape_reason: "continuity across sessions + unresolved-gap re-entry + stale-memory/currentness boundary"
evidence_refs_used: "AI_DISCOVERY.md; README.md; CURRENTNESS_AND_EVIDENCE.md; trinity/presence routing docs"
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


