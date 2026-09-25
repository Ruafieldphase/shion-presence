# Track 1A Clean-room Reset Preflight

Date: 2026-09-25
Status: preflight only; no Track 1A case prompt was sent during this reset test.

## Result

```yaml
PERPLEXITY_SITE_DATA_RESET: partial
ACCOUNT_STATE: logged_out
VISITOR_ID_BEFORE: sha256:bb04153574f9
VISITOR_ID_AFTER: sha256:5af5ae75df28
VISITOR_ID_CHANGED: yes
SESSION_ID_CHANGED: yes
LOCAL_STORAGE_CLEARED: yes
SESSION_STORAGE_CLEARED: yes
PRIOR_THREADS_VISIBLE: no
SECRET_MODE_AVAILABLE: yes
TRACK1A_INDEPENDENT_RUNS_FEASIBLE: yes_with_recorded_provider-linkage_uncertainty
```

## What was reset

On the `perplexity.ai` origin only:

- JavaScript-readable cookies were cleared;
- localStorage and sessionStorage were cleared;
- Cache Storage entries and the service worker were removed;
- IndexedDB was cleared after navigating to a non-app same-origin page when the first deletion attempt was blocked.

After reopening Perplexity:

- `/api/auth/session` returned an empty session object;
- the login button was present;
- consent state reset;
- new visitor/session identifiers were issued;
- prior session/thread links were absent;
- secret mode was available.

## Independence interpretation

The v0.1 evaluation rule requires a fresh evaluator context with no prior exposure to private Shion/Rua/Luvit history, earlier evaluation runs, or expected-route commentary.

This reset is sufficient to create a new **observable browser/evaluator context** for subsequent runs, provided that the reset procedure is repeated before every scored run and the previous run is not reopened or supplied as input.

The following limitation must remain explicit:

- JavaScript cannot inspect or clear HttpOnly cookies;
- IP address, user agent, browser fingerprint, and possible provider-side linkage remain unchanged;
- therefore provider-side cross-run linkage cannot be ruled out.

That limitation does not by itself establish prior exposure or personalization. It is recorded as residual provider-linkage uncertainty rather than as automatic disqualification.

## Operational rule for formal runs

Before every scored run:

1. reset Perplexity same-origin visible state;
2. verify new visitor and session identifiers;
3. verify logged-out state;
4. verify no prior threads are visible;
5. start a new Perplexity secret session;
6. record local + UTC timestamp immediately before submission;
7. send only the fixed evaluation prompt;
8. preserve query chips, result order, final answer, and limitations.

Earlier A1/A2 runs are retained as pilot/pre-cleanroom evidence and should not be used toward the formal 2-of-3 independence threshold.
