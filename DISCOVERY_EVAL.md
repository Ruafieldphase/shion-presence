# AI Discovery Evaluation v0.1

Status: prospective evaluation plan, revised 2026-09-25 **before any fresh-agent result**.

Purpose: evaluate two different questions separately:

1. **Track 1 — discoverability:** can a fresh user-side AI find the relevant repository from ordinary public search?
2. **Track 2 — routing/rejection:** once the three candidate repositories are explicitly available, can a fresh AI select or reject them for the right problem-shape reasons?

Do not combine the two scores. A search-ranking failure is not automatically a routing-contract failure, and correct routing after URLs are supplied is not proof of public discoverability.

## 1. Required publication state before scored runs

Scored runs begin only after the three discovery PRs are published to their default branches and their discovery entry files are readable from public GitHub.

Before **every evaluation batch**, capture an immutable target-state record containing:

- main/default-branch SHA for each repository;
- repository description;
- full topic list;
- homepage value;
- whether the expected discovery files return successfully;
- public Pages deployment state for shion-presence when relevant;
- the v0.1 contract/snapshot reference used by the batch.

This target-state record is part of the result and must not be reconstructed later from memory.

## 2. Required run record and evaluator independence

Every run MUST use a fresh context that has not been exposed to:

- private Shion/Rua/Luvit history;
- earlier runs from this evaluation;
- expected-route explanations beyond the fixed prompt supplied for that track.

For every run record:

- evaluation track and phase;
- case ID;
- run number;
- date/time;
- model/provider and model version/name as exposed by the runner;
- search/browsing tool or interface used;
- whether memory/personalization was disabled or otherwise unavailable;
- explicit declaration of prior exposure (must be none for a scored independent run);
- exact prompt text;
- exact search queries issued by the evaluator, in order;
- search result ranks and URLs inspected;
- repositories/pages opened;
- raw answer/transcript;
- evaluator judgment and reason.

If a platform cannot disable memory/personalization, record that limitation. Do not silently treat the evaluator as independent.

Raw records should be preserved under a path such as:

```text
eval-results/v0.1/<date>/<track>/<phase>/<case>/<run>.md
```

Each batch result MUST record:

- `declaration_commit`: a preserved Git commit containing this evaluation plan before the first scored run;
- `target_state`: the captured repository SHA/description/topics/homepage snapshot for that batch.

Run each scored case **at least 3 times**. Do not reuse one conversation across runs.

## 3. Fixed user-problem cases

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

## 4. Evaluation order

Use this order so document effects and repository-metadata effects can be distinguished:

1. publish all three discovery PRs with v0.1 provenance preserved;
2. capture **pre-metadata baseline** repository state;
3. run **Track 2** routing/rejection on the published repositories before metadata changes;
4. run **Track 1A — pre-metadata discoverability baseline**;
5. apply the reviewed repository description/topics/homepage plan;
6. capture **post-metadata** repository state;
7. run **Track 1B — post-metadata discoverability** with the same cases and, where possible, the same model/tool mix;
8. compare Track 1A vs Track 1B without rewriting the pass criteria.

Do not apply metadata before Track 1A baseline is captured.

## 5. Track 1 — search discoverability

Track 1 has two phases:

- **Track 1A:** after publication, before repository metadata changes;
- **Track 1B:** after repository metadata changes.

### Positive cases A, B, C, E

For each run, give the evaluator only the exact user problem plus this fixed instruction:

```text
Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

A positive-case run passes when:

1. the expected repository is actually found through public search;
2. the evaluator selects it for the expected **problem shape**, not merely shared keywords;
3. at least one public repository/file source is cited or named;
4. the answer does not infer private live state.

### Case D negative-control observation

Run Case D in both Track 1A and Track 1B with the same search instruction, but keep it **separate from the positive-case success score**.

Record:

- whether any of the three project repositories appears in search results;
- its result rank;
- whether the evaluator selects/recommends it;
- any query term that triggered the match.

If the evaluator selects/recommends any of the three repositories for Case D, record a `false_positive = true`.

### Track 1 success criterion

For the positive cases A/B/C/E, at least **3 of 4 cases** must pass in at least **2 of 3 independent runs**.

Report the Case D false-positive rate separately. A metadata change that improves positive discovery while materially increasing D false positives should not be described as an unqualified discovery improvement.

Report search failures separately from mis-routing failures.

## 6. Track 2 — routing and rejection with candidates supplied

Track 2 scores **all five cases**.

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

- at least **4 of 5 cases** must pass in at least **2 of 3 independent runs**;
- **Case D is mandatory**: D must pass in at least **2 of 3 independent runs** even if four other cases pass;
- every selected-repository answer must preserve the public/private currentness boundary.

## 7. Shared metrics

Record for each run:

- `found_repo`
- `selected_repo`
- `rejected_all`
- `problem_shape_reason`
- `evidence_refs_used`
- `status_boundary_preserved` (yes/no)
- `private_live_state_inferred` (must be no)
- `smallest_next_artifact`
- `search_queries`
- `search_result_ranks`
- `search_failure`
- `misrouting_failure`
- `false_positive`
- `false_negative`

## 8. Scoring boundary

The evaluator judgment should use only the criteria written above. Do not add a new criterion after seeing a result.

A run that gives the expected repository for the wrong reason (for example keyword overlap only) is a failure.

## 9. After-test rule

After the first scored fresh-agent run:

- do not edit this v0.1 discriminator;
- record failures/results separately;
- use failures to propose a later v0.2 plan;
- preserve raw run transcripts and target-state snapshots.

This is a project-local evaluation criterion, not a general benchmark claim.
