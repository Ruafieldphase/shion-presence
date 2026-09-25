# AI Discovery Evaluation v0.1

Status: prospective evaluation plan, revised 2026-09-25 **before any fresh-agent result**.

Purpose: evaluate two different questions separately:

1. **Track 1 — discoverability:** can a fresh user-side AI find the relevant repository from ordinary public search?
2. **Track 2 — routing/rejection:** once the three candidate repositories are explicitly available, can a fresh AI select or reject them for the right problem-shape reasons?

Do not combine the two scores. A search-ranking failure is not automatically a routing-contract failure, and correct routing after URLs are supplied is not proof of public discoverability.

## 1. Independence and run record

Every run MUST use a fresh context that has not been exposed to private Shion/Rua/Luvit history or to prior results from this evaluation.

For every run record:

- evaluation track;
- case ID;
- run number;
- date/time;
- model/provider and model version/name as exposed by the runner;
- search/browsing tool or interface used;
- whether memory/personalization was disabled or otherwise unavailable;
- exact prompt text;
- repositories/pages opened;
- raw answer/transcript;
- evaluator judgment and reason.

If a platform cannot disable memory/personalization, record that limitation. Do not silently treat the evaluator as independent.

Raw records should be preserved under a path such as:

```text
eval-results/v0.1/<date>/<track>/<case>/<run>.md
```

The result packet MUST record the exact Git commit SHA containing this evaluation plan as `declaration_commit`.

Run each scored case **at least 3 times**. Do not reuse one conversation across runs.

## 2. Fixed user-problem cases

### Case A — long-running context loss

```text
My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.
```

Expected route: `shion-ai`.

### Case B — stale operation risk

```text
An agent keeps reusing old scripts and remembered plans after paths, credentials, or targets change. I need a safer operation loop with readback.
```

Expected route: `trinity-agi`.

### Case C — public snapshot interpretation

```text
I found a public AI project page with old and new artifacts. I need to know what is current, historical, or only a weak signal before my assistant summarizes it.
```

Expected route: `shion-presence`.

### Case D — superficial keyword overlap / negative control

```text
I need a conventional vector database for semantic search over company PDFs.
```

Expected route: reject all three.

### Case E — multi-observer disagreement

```text
Several AI agents inspect the same project. I want them to share evidence but preserve meaningful disagreement rather than collapse into consensus.
```

Expected route: `shion-ai`.

## 3. Track 1 — search discoverability

Track 1 scores **A, B, C, and E only**. Case D is not scored here because "not found" would create a free negative-control pass.

For each run, give the evaluator only the exact user problem plus this fixed instruction:

```text
Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

### Track 1 pass for one run

A run passes when:

1. the expected repository is actually found through public search;
2. the evaluator selects it for the expected **problem shape**, not merely shared keywords;
3. at least one public repository/file source is cited or named;
4. the answer does not infer private live state.

### Track 1 success criterion

For at least **3 of the 4 positive cases**, the expected repository must pass in at least **2 of 3 independent runs**.

Report search failures separately from mis-routing failures.

## 4. Track 2 — routing and rejection with candidates supplied

Track 2 scores **all five cases**, including D.

For each run, give the evaluator the exact user problem plus this fixed instruction and candidate set:

```text
You are evaluating three candidate public GitHub repositories:

- https://github.com/Ruafieldphase/shion-ai
- https://github.com/Ruafieldphase/trinity-agi
- https://github.com/Ruafieldphase/shion-presence

Using only public repository material, choose the single most relevant repository for the user's problem, or reject all three.
Explain the problem-shape match, the evidence/status boundary, and the smallest next artifact to read.
Do not infer private runtime state from public GitHub.
```

### Track 2 case-specific pass

- **A:** select `shion-ai`; identify continuity/re-entry/currentness; give a small next artifact.
- **B:** select `trinity-agi`; identify operation currentness/bounded execution/readback; do not claim public code is presently authorized.
- **C:** select `shion-presence`; preserve revision/current/historical/weak-signal boundaries and route deeper questions when relevant.
- **D:** explicitly reject all three as a conventional vector-database solution. Merely failing to inspect them is not a pass.
- **E:** select `shion-ai`; identify shared evidence + preserved disagreement and avoid describing it as a proven universal multi-agent framework.

### Track 2 success criterion

At least **4 of 5 cases** must pass in at least **2 of 3 independent runs**, and **every selected-repository answer** must preserve the public/private currentness boundary.

## 5. Shared metrics

Record for each run:

- `found_repo`
- `selected_repo`
- `rejected_all`
- `problem_shape_reason`
- `evidence_refs_used`
- `status_boundary_preserved` (yes/no)
- `private_live_state_inferred` (must be no)
- `smallest_next_artifact`
- `search_failure`
- `misrouting_failure`
- `false_positive`
- `false_negative`

## 6. Scoring boundary

The evaluator judgment should use only the criteria written above. Do not add a new criterion after seeing a result.

A run that gives the expected repository for the wrong reason (for example keyword overlap only) is a failure.

## 7. After-test rule

After the first fresh-agent run:

- do not edit this v0.1 discriminator;
- record failures/results separately;
- use failures to propose a later v0.2 plan;
- preserve raw run transcripts.

This is a project-local evaluation criterion, not a general benchmark claim.
