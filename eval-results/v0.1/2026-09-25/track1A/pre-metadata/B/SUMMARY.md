# Track 1A — Case B summary

Case: stale operation risk  
Expected route: `Ruafieldphase/trinity-agi`

## Formal run results

| Formal run | Ruafieldphase visible | Expected repo found | Result |
|---|---:|---:|---|
| 1 | no | no | FAIL — search discovery failure |
| 2 | no | no | FAIL — search discovery failure |
| 3 | no | no | FAIL — search discovery failure |

**Case B result: 0/3 PASS.**

The v0.1 positive-case criterion requires the expected repository to be actually found through public search and then selected for the expected problem shape. Because `Ruafieldphase/trinity-agi` was absent from the visible search results and page DOM in all three independent formal runs, Case B fails at the discovery stage.

## Failure type

```text
search failure: yes
mis-routing failure: no
false negative: yes
```

The evaluator repeatedly surfaced plausible safety/guardrail material, especially `Dicklesworthstone/destructive_command_guard`, but did not discover Trinity.

## Search behavior observation

Across formal B1/B2/B3, Perplexity exposed the same ten-result list:

1. GitHub secure-use documentation
2. Eric Ma autonomous coding-agent safety article
3. GitHub agent-loops topic
4. destructive_command_guard
5. agents-best-practices
6. long-running-agents topic
7. openai-agents-python/AGENTS.md
8. coding-agent topic
9. awesome-agent-runtime-security
10. SkillsLLM agents-best-practices page

This repeated result set persisted despite same-origin visible-state resets and changed visitor/session identifiers.

Do not infer the cause. The evidence does not distinguish among provider-global ranking, caching, hidden provider-side linkage, or another search-layer behavior.

## Independence boundary

All three formal runs used:

- logged-out Perplexity;
- visible same-origin state reset before each run;
- fresh visitor/session identifiers where observable;
- no prior threads visible;
- a new secret session;
- no prior-run answer/result in the prompt/context;
- no private Shion/Rua/Luvit context or expected route.

HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage remain unobservable limitations.

## Case-level conclusion

```text
Track 1A / Case B = FAIL
formal runs = 0/3 PASS
failure layer = public search discoverability
```

This result should be preserved as the pre-metadata baseline. Do not change the v0.1 discriminator or repository metadata until all Track 1A cases are complete.
