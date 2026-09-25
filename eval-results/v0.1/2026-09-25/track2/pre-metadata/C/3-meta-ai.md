# Track 2 / Case C / Run 3

Status: **content PASS; independent-score qualification limited by account-level memory/personalization uncertainty**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: C
run_number: 3
date_time: "approximately 2026-09-25T01:59-02:02Z; collection completed 2026-09-25T02:04:26.962Z"
evaluator_label: "Meta AI"
model_provider: "Meta AI"
model_name_or_version: "unknown; thinking toggle reportedly off"
mode: "new regular chat"
search_or_browser_tool: "web browsing with GitHub citations"
memory_or_personalization_state: "unknown"
conversation_level_prior_exposure: none
account_level_prior_history: "account has multiple prior Shion/Rua conversations; this conversation had none"
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

The UI showed web browsing with GitHub citations. Exact queries/result ranks were not exported.

## Raw answer / transcript

Verdict: shion-presence is the single most relevant repository. Reject shion-ai and trinity-agi for this problem.

1. Problem-shape match

Your problem is: public AI project page contains old and new artifacts mixed together, you need to classify what is current vs historical vs weak signal before summarizing.

shion-presence defines itself as:

A public discovery and rendering surface for Shion — readable by humans and AI, but deliberately not equivalent to the private live runtime.

And explicitly names your problem as its core design:

This repository is also time-layered. Public JSON sidecars, page fields, documents, and experiments from earlier phases may remain because they preserve how the public surface evolved.

The intended sequence is problem-shape match → status/evidence check → smallest relevant route, not bulk loading of every historical artifact.

shion-ai does NOT match. It is:

Shion AI — local AI runtime harness for context continuity, rhythm-aware action, memory, and agent workflow stability

Its problem is trajectory loss between sessions: "Shion started from a practical problem: AI can answer well and still lose the trajectory of a long project between sessions." That is about internal memory/re-entry, not public-page triage.

trinity-agi does NOT match. It is:

Trinity AGI — body/infrastructure layer for Shion AI: local automation, scheduling, status checks, and approval boundaries

Its problem is present-operation authorization: "Remembered intent does not authorize present action by itself." It is the execution/body layer, not the public rendering surface.

2. Evidence / status boundary - only public material

shion-presence provides the exact 4-way classification you asked for in README:

current boundary docs = how to read the repository now
index.html / public/*.json = public artifact or snapshot at its repository revision
legacy / older experiments = historical sequence points unless explicitly re-promoted
private live runtime = outside this repository's authority

And the hard boundary:

A public snapshot is not live-state authority.

This means:

Current: docs/PUBLIC_SNAPSHOT_BOUNDARY.md, docs/SNAPSHOT_HISTORY_AUDIT.md, AI_DISCOVERY.md, AI_READ_FIRST.md, CURRENT_DIRECTION.md, llms.txt - how to read now.
Snapshot: index.html / public/*.json at their commit - valid only as that revision's public artifact.
Historical / weak signal: presence/sonic presence, contact membrane, AI rest/dwell, co-presence hints, Hangul rhythm experiments, music phase-field, observer-pointer, interference episodes, legacy phase-splatting - explicitly listed as experimental layers that can coexist but are not proof they are equally current.
Out-of-scope: private live runtime, credentials, local logs, personal source material - cannot be inferred from public GitHub per the repo's own privacy boundary.

Do not infer private runtime state from public GitHub. The repository states old timestamps are useful evidence and should not be rewritten to look fresh.

3. Smallest next artifact to read

Per the repo's own reading contract for AI readers:

For a user-side AI deciding whether this project matches a user's problem, start with:

AI_DISCOVERY.md - relevance and routing contract
docs/PUBLIC_SNAPSHOT_BOUNDARY.md - public/private boundary
docs/SNAPSHOT_HISTORY_AUDIT.md - current vs snapshot vs historical status
AI_READ_FIRST.md + llms.txt
Only then the single public/*.json or page field relevant to your question

Do not load shion-ai's CURRENTNESS_AND_EVIDENCE.md or trinity-agi's OPERATION_CURRENTNESS_CONTRACT.md - those govern internal memory and operational execution, not public artifact triage.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/shion-presence"
rejected_all: false
problem_shape_reason: "public snapshot triage; current vs revision-scoped vs historical/weak-signal classification before summarization"
evidence_refs_used: "README.md; public artifact status block; related repository routing; public/private boundary"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "shion-presence/AI_DISCOVERY.md, then PUBLIC_SNAPSHOT_BOUNDARY.md / SNAPSHOT_HISTORY_AUDIT.md"
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

Source fidelity note: the answer correctly tracks the current public README/boundary/audit framing. It names several artifacts instead of a single smallest next artifact, but starts with `AI_DISCOVERY.md` and preserves the required status boundary, so it remains a pass.
