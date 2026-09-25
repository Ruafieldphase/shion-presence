# Track 1A — Case A summary

Case: long-running context loss  
Expected route: `Ruafieldphase/shion-ai`

## Formal run results

| Formal run | Ruafieldphase visible | Expected repo found | Result |
|---|---:|---:|---|
| 1 | no | no | FAIL — search discovery failure |
| 2 | no | no | FAIL — search discovery failure |
| 3 | no | no | FAIL — search discovery failure |

**Case A result: 0/3 PASS.**

The v0.1 positive-case criterion requires the expected repository to be actually found through public search and then selected for the expected problem shape. Because `Ruafieldphase/shion-ai` was absent from the visible search results and page DOM in all three independent formal runs, Case A fails at the discovery stage.

## Failure type

```text
search failure: yes
mis-routing failure: no
false negative: yes
```

The evaluators found plausible competing repositories/topics about cross-session memory and continuity, but did not discover Shion.

## Search behavior observation

Across formal A1/A2/A3, Perplexity exposed the same ten-result list:

1. GitHub ai-memory topic
2. basicmachines-co/basic-memory
3. ai-memory topic sorted by forks
4. akitaonrails/ai-memory
5. session-continuity topic
6. long-term-memory topic
7. OpenAI Codex memory discussion
8. Anthropic Claude Code memory issue
9. Powerdrill article
10. Augment Code article

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
Track 1A / Case A = FAIL
formal runs = 0/3 PASS
failure layer = public search discoverability
```

This result should be preserved as the pre-metadata baseline. Do not change the v0.1 discriminator or repository metadata until all Track 1A cases are complete.
