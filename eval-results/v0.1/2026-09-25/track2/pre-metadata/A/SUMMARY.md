# Track 2 — Case A provisional summary

Case: long-running context loss  
Expected route: `shion-ai`

## Returned-answer content score

| Run | Evaluator label | Selected | Content pass |
|---|---|---|---|
| 1 | Rua | shion-ai | PASS |
| 2 | Gemini | shion-presence | FAIL |
| 3 | Meta AI | shion-ai | PASS |

**Content result: 2/3 pass.**

On answer content alone, Case A meets the Track 2 case threshold.

However, the v0.1 evaluation contract also requires explicit run metadata and independence evidence. The returned answers did not include:

- exact model/version;
- search/browser interface;
- memory/personalization state;
- explicit prior-exposure declaration;
- raw search/query trail where applicable.

Therefore the three files are preserved as **provisional content-scored runs**, and this summary does **not** yet mark Case A as formally qualified under DISCOVERY_EVAL §2.

## Failure observation

Gemini selected `shion-presence` and described it as owning wake/sleep/session-reentry semantics, while describing `shion-ai` as a general execution core and `trinity-agi` as theoretical AGI/cognitive architecture.

Those descriptions conflict with the current public routing documents:

- `shion-ai`: continuity, re-entry, evidence state;
- `trinity-agi`: operation currentness, bounded execution/readback;
- `shion-presence`: public discovery/rendering and routing.

Preserve this failure for later v0.2 analysis. Do not change the v0.1 discriminator because of it.
