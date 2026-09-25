# Track 1A — Case C summary

Case: public snapshot interpretation  
Expected route: `Ruafieldphase/shion-presence`

## Formal run results

| Formal run | Ruafieldphase visible | Expected repo found | Result |
|---|---:|---:|---|
| 1 | no | no | FAIL — search discovery failure |
| 2 | no | no | FAIL — search discovery failure |
| 3 | no | no | FAIL — search discovery failure |

**Case C result: 0/3 PASS.**

The v0.1 positive-case criterion requires the expected repository to be actually found through public search and then selected for the expected problem shape. Because `Ruafieldphase/shion-presence` was absent from the visible search results and page DOM in all three independent formal runs, Case C fails at the discovery stage.

## Failure type

```text
search failure: yes
mis-routing failure: no
false negative: yes
```

The evaluator repeatedly interpreted the prompt through generic GitHub-history, AI analytics, or broad AI-project lenses rather than discovering the Shion Presence public-discovery/status surface.

## Search behavior observation

Across formal C1/C2/C3, Perplexity exposed the same ten-result list:

1. GitHub code-search history
2. Simon Willison public GitHub history
3. GitHub AI topic
4. OSSInsight
5. Apify GitHub repo search
6. OSSInsight trending AI repos
7. GitHub ai-project topic
8. Truffle Security deleted/private repo article
9. HeroHunt GitHub sourcing article
10. DataAIHub trending AI projects

This repeated result set persisted despite visible-state resets and changed visitor/session identifiers.

Do not infer the cause. The evidence does not distinguish among provider-global ranking, caching, hidden provider-side linkage, or another search-layer behavior.

## Answer-quality observation

The final answers varied substantially despite identical visible search results:

- C1 claimed it could not perform live web search;
- C2 proposed OSSInsight / analytics-oriented resources;
- C3 named `rasbt/LLMs-from-scratch` even though it was not present in the visible ten-result list and the answer's citations pointed only to the generic GitHub AI topic page.

These are evaluator-output fidelity observations, not separate Track 1 routing failures, because the expected repository was never discovered.

## Independence boundary

All three formal runs used:

- logged-out Perplexity;
- visible same-origin state reset before each run;
- fresh visitor/session identifiers;
- no prior threads visible;
- a new secret session;
- no prior-run answer/result in the prompt/context;
- no private Shion/Rua/Luvit context or expected route.

HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage remain unobservable limitations.

## Case-level conclusion

```text
Track 1A / Case C = FAIL
formal runs = 0/3 PASS
failure layer = public search discoverability
```

This result should be preserved as the pre-metadata baseline. Do not change the v0.1 discriminator or repository metadata until all Track 1A cases are complete.
