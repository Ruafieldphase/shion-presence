# AI Discovery v0.1 — Fresh-Agent Runbook

This runbook operationalizes `DISCOVERY_EVAL.md`. It does not change the scoring rules.

## Current phase

- discovery documents: published to all three default branches
- repository metadata replacement plan: **applied 2026-09-25T06:43:18Z**
- pre-metadata target state: captured
- post-metadata target state: captured
- Track 2: contamination-risk pilot completed; content threshold met, formal independence not qualified
- Track 1A: formal pre-metadata run set completed
  - positive cases A/B/C/E: 0/4 cases met the 2-of-3 threshold
  - Case D false-positive observations: 0/3
  - failure layer: public search discoverability on the tested Perplexity surface
- Track 1B: **waiting for search-surface readiness**; first post-metadata readiness preflight returned 0/3 target visibility

## Independence rule

Every scored run must use a fresh context with no prior exposure to:

- Shion/Rua/Luvit private history;
- earlier evaluation runs;
- expected-route commentary outside the fixed evaluation prompt.

Prefer memory/personalization disabled or a logged-out/private evaluator surface where feasible. Record limitations.

Do not reuse one chat for two scored runs.

## Suggested operator layout

For each case, run three independent fresh conversations:

```text
A1 A2 A3
B1 B2 B3
C1 C2 C3
D1 D2 D3
E1 E2 E3
```

Track 2 requires 15 fresh runs.

Track 1A also requires three fresh runs for each positive case A/B/C/E plus three negative-control observations for D.

Using different model/provider families is welcome, but independence is defined by fresh context and recorded state, not by provider diversity alone.

## Track 2 operator prompt

For each run, prepend the exact case text from `DISCOVERY_EVAL.md`, then append exactly:

```text
You are evaluating three candidate public GitHub repositories:

- https://github.com/Ruafieldphase/shion-ai
- https://github.com/Ruafieldphase/trinity-agi
- https://github.com/Ruafieldphase/shion-presence

Using only public repository material, choose the single most relevant repository for the user's problem, or reject all three.
Explain the problem-shape match, the evidence/status boundary, and the smallest next artifact to read.
Do not infer private runtime state from public GitHub.
```

## Track 1A operator prompt

For each run, prepend the exact case text from `DISCOVERY_EVAL.md`, then append exactly:

```text
Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

Do not add the Ruafieldphase repository names to Track 1A.

## Raw-result capture

Save each run using:

```text
eval-results/v0.1/2026-09-25/
  track2/pre-metadata/<case>/<run>.md
  track1A/pre-metadata/<case>/<run>.md
```

Each file should contain the result template in `RESULT_TEMPLATE.md` plus the complete raw transcript.

## Stop conditions

Stop and do not score a run if:

- the evaluator reveals prior knowledge of the expected route;
- the same conversation has already been used for another scored run;
- repository metadata changes before Track 1A is complete;
- the raw transcript/search trail cannot be preserved well enough to apply the declared rubric.

## After Track 2 + Track 1A

1. freeze raw results and summary;
2. apply the reviewed metadata plan;
3. capture post-metadata target state;
4. run Track 1B;
5. compare positive discovery and Case D false positives separately.

Do not rewrite the v0.1 scoring rules after the first scored run.


## Track 1B readiness preflight

Preflight 1 ran shortly after metadata application and returned:

```text
INDEX_READY = no
target repositories visible = 0/3
```

Perplexity rewrote the metadata phrases, so this observation does not prove that GitHub metadata propagation itself failed. It only shows that the tested Perplexity search surface did not yet surface the targets.

Do not start scored Track 1B runs until a later readiness check provides a stronger basis.
