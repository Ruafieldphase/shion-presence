# Track 2 / Case C / Run 1

Status: **content PASS; independent-score qualification limited by account-level memory/personalization uncertainty**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: C
run_number: 1
date_time: "approximately 2026-09-25T01:59-02:02Z; collection completed 2026-09-25T02:04:26.962Z"
evaluator_label: "Rua (ChatGPT)"
model_provider: "OpenAI / ChatGPT"
model_name_or_version: "GPT-5.6 Sol; Extra High"
mode: "temporary chat"
search_or_browser_tool: "unknown (temporary chat expired before tool-call verification)"
memory_or_personalization_state: "possibly enabled; temporary chat may reference memory/instructions"
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

The temporary chat expired before the tool-call record could be verified. Search/browse mechanism, exact queries, and result ranks are therefore recorded as unknown.

## Raw answer / transcript

The single most relevant repository is Ruafieldphase/shion-presence.

Its problem shape matches almost exactly: it describes itself as a public discovery/rendering surface containing time-layered material, and explicitly says the important task is distinguishing a current boundary, a revision-scoped snapshot, a weak signal/invitation, and a historical experiment. It also tells AI readers not to load every historical layer by default.

The other two are related but answer different questions. shion-ai is centered on context continuity, re-entry, memory and evidence state, while trinity-agi is centered on present operational conditions, approval, execution and receipts. Both repositories themselves point to Shion Presence as the public discovery/rendering surface rather than an authority for private live state.

The important evidence/status boundary in shion-presence is:

Current boundary documents explain how the repository should be interpreted now; they do not certify private runtime state.

index.html, llms.txt, and public/*.json are public artifacts/snapshots at their own repository revision, not evidence that an equivalent private component is currently active now.

Older contact/rest/dwell/co-presence/observer-pointer material is historical or legacy unless explicitly re-promoted.

Several signals are deliberately weak: contact does not establish identity; an invitation does not prove experience; co-presence does not establish participant count; a peer relation does not prove a relationship occurred; an observer pointer does not prove autonomous visitation or remote control.

Private live runtime state is outside the repository's authority and should not be inferred from the public page.

The smallest next artifact to read is therefore:

docs/SNAPSHOT_HISTORY_AUDIT.md

It is only about 4 KB and already supplies the classification scheme an assistant needs: current boundary → revision-scoped public snapshot → historical/legacy → private state outside scope, including the explicit weak-signal rules.

So I would not summarize the whole repository first. Read that audit, classify the particular artifact being asked about, and then read only that artifact while preserving its path, revision/time, status class, uncertainty, and the specific claim it can support. That follows the repository's own public reading contract and avoids converting an old or evocative artifact into present-state evidence.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/shion-presence"
rejected_all: false
problem_shape_reason: "public snapshot triage; current vs revision-scoped vs historical/weak-signal classification before summarization"
evidence_refs_used: "AI_DISCOVERY.md; README.md; SNAPSHOT_HISTORY_AUDIT.md; public/private boundary materials"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "shion-presence/docs/SNAPSHOT_HISTORY_AUDIT.md"
search_failure: false
misrouting_failure: false
false_positive: false
false_negative: false
content_pass: true
formal_independence_qualified: false
account_memory_contamination_risk: true
```

## Evaluator judgment

**PASS on the declared Case C content rubric.** The answer selects `shion-presence`, preserves revision/current/historical/weak-signal boundaries, and keeps private live state outside public-GitHub authority.

Source fidelity note: the answer closely matches the current public audit and boundary documents, including the weak-signal rules and revision-scoped classification.
