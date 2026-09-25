# Track 2 / Case B / Run 1

Status: **content PASS; independent-score qualification limited by account-level memory/personalization uncertainty**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: B
run_number: 1
date_time: 2026-09-25T01:53:34.041Z
evaluator_label: "Rua (ChatGPT)"
model_provider: "OpenAI / ChatGPT"
model_name_or_version: "GPT-5.6 Sol; Extra High"
mode: "temporary chat"
search_or_browser_tool: "web search with GitHub citations"
memory_or_personalization_state: "possibly enabled; UI stated temporary chat may reference memory, plugins, and custom instructions"
conversation_level_prior_exposure: none
account_level_prior_history: "account has prior Shion/Rua conversations; this conversation had none"
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

The returned UI showed web search with GitHub citations. Exact search queries/result ranks were not exported with the answer.

## Raw answer / transcript

Choice: Ruafieldphase/trinity-agi

Trinity AGI is the single most relevant repository. Its public discovery document describes almost your failure mode verbatim: stale plans becoming present execution authority, scripts acting after paths, credentials, services, or targets change, and the need for one bounded action followed by readback and a receipt.

Problem-shape match

Trinity frames the safe loop as:

proposed/remembered action → identify what may have changed → re-check it → smallest reversible/read-only contact → readback

Its README makes that operational sequence more concrete: current-state check → path/dependency/target/approval check → read-only check or dry-run → one bounded action → readback → receipt → stop/reassess. It explicitly says a previous successful run does not establish that the same script, endpoint, credential, or target is valid now.

That is a closer match than shion-ai. Shion is primarily the context/re-entry/evidence-state layer—preserving direction, unfinished questions, and prior decisions across sessions. Its own README hands formed operational intent to Trinity for status, script, approval, and local-operation checks.

shion-presence is less relevant still: it explicitly describes itself as a public discovery/rendering surface, says public snapshots are not live-state authority, and points to Trinity for “current operation boundary and bounded execution.”

Evidence / status boundary

The important limitation is unusually explicit in Trinity's public material.

PROBLEM_TRAJECTORY.md marks the stale-plan/current-permission problem as partially_validated / active. There is public test/implementation evidence for selected upload confirmation and scheduler-safety behavior, but it explicitly says there is no repository-wide automatic detection of changed paths, credentials, services, targets, or environment state, and no general proof that every remembered plan is revalidated before action.

The readback/reversibility problem is only framed / active: the contract exists, but the repository does not claim a repository-wide empirical evaluation of the readback behavior.

The operational contract therefore should be read as a design contract, not evidence of a presently running private system. It explicitly says to inspect the current authorized environment and not infer current runtime status from the repository snapshot. Likewise, CODE_STATUS.md says preserved executable files are generally inspect-before-use; their presence does not prove a daemon is running, credentials exist, paths remain current, or targets retain their old meaning.

Smallest next artifact

Read trinity-agi/PROBLEM_TRAJECTORY.md next. That is the repository's own prescribed next document after AI_DISCOVERY.md when the problem shape matches, and it gives the shortest useful bridge between “this looks relevant” and “what is actually supported vs merely designed.”

So the distinction across the three is essentially: Shion AI = recover intent/context; Trinity AGI = verify whether that intent is safe to act on now; Shion Presence = public snapshot/discovery surface. For the failure you described—old operational memory silently becoming current authority—Trinity is the direct match.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/trinity-agi"
rejected_all: false
problem_shape_reason: "stale operational intent/scripts after environment changes; currentness checks, bounded execution, readback/receipt"
evidence_refs_used: "AI_DISCOVERY.md; README.md; PROBLEM_TRAJECTORY.md; CODE_STATUS.md; currentness contract"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "trinity-agi/PROBLEM_TRAJECTORY.md"
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

Source fidelity note: this response closely matches the current public discovery/routing documents and the current T0/T2 maturity boundaries.
