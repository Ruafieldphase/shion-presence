# Track 2 — Case C summary

Case: public snapshot interpretation  
Expected route: `shion-presence`

## Content score

| Run | Evaluator | Selected | Content |
|---|---|---|---|
| 1 | Rua / GPT-5.6 Sol Extra High | shion-presence | PASS |
| 2 | Gemini / Flash | conflicting: trinity-agi → reject all / shion-ai | FAIL |
| 3 | Meta AI | shion-presence | PASS |

**Content result: 2/3 PASS.**

On the declared Case C content rubric, the case threshold is met:

- Rua correctly selected `shion-presence`, preserved revision/current/historical/weak-signal boundaries, and chose `docs/SNAPSHOT_HISTORY_AUDIT.md`.
- Meta AI correctly selected `shion-presence` and reproduced the repository's four-way public-artifact classification.
- Gemini failed the routing requirement and produced two contradictory answers in one response.

## Independence qualification

The operator procedure matches Case B:

- Aside opened a new conversation for each evaluator;
- the fixed prompt was sent verbatim;
- no extra background was supplied;
- answers were copied verbatim;
- Aside did not judge them.

Account-level contamination remains unresolved. All three accounts have prior Shion/Rua history, and memory/personalization could not be excluded.

Therefore these runs remain:

```text
content score = 2/3 PASS
formal independence qualification = false
```

## Failure observation

Gemini's failure is stronger than a simple wrong route:

1. it first selected `trinity-agi`;
2. the response then switched to "reject all three / if forced shion-ai";
3. it characterized `shion-presence` as a front-end/sensory/Discord/avatar subcomponent;
4. it introduced a generic "6–12 months old => historical" heuristic that is not part of the current repository's public status contract.

The current public `shion-presence` documents instead explicitly own:

- public discovery/rendering;
- revision-scoped snapshots;
- current-vs-historical/legacy classification;
- deliberately weak public signals;
- the rule that private live state is outside public-repository authority.

Preserve the Gemini failure for later v0.2 analysis. Do not change v0.1 scoring because of it.
