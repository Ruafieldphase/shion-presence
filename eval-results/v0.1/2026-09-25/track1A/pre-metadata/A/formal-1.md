# AI Discovery v0.1 — Track 1A / Case A / Formal Run 1

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: A
formal_run_number: 1
run_start_local: 2026-09-25T12:15:15+09:00
run_start_utc: 2026-09-25T03:15:15Z
model_provider: Perplexity
model_name_or_version: "UI label: 모델; backend model unknown"
search_or_browser_tool: "Perplexity ordinary public web search in secret mode, operated through Claude app built-in browser pane"
memory_or_personalization_state: "logged out; visible same-origin site state reset before run; fresh Perplexity visitor/session identifiers; secret mode"
prior_exposure: none
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
cleanroom_reset_record: eval-results/v0.1/2026-09-25/track1A/pre-metadata/CLEANROOM_RESET_PREFLIGHT.md
```

## Clean-room reset evidence

```yaml
PERPLEXITY_SITE_DATA_RESET: partial
ACCOUNT_STATE: logged_out
VISITOR_ID_BEFORE_RESET: sha256:5af5ae75df28
VISITOR_ID_AFTER_RESET: sha256:f8a18fe0da29
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:9f302d433e8d
SESSION_ID_AFTER_RESET: sha256:a3d1dfcc6a2d
SESSION_ID_CHANGED: yes
LOCAL_STORAGE_CLEARED: yes
SESSION_STORAGE_CLEARED: yes
PRIOR_THREADS_VISIBLE: no
SESSION_MODE: secret
FRESH_SECRET_SESSION: yes
PRIOR_RUN_EXPOSURE: none
SCREENSHOT_FILES: none
SCREENSHOT_LIMITATION: "browser pane image only; no persistent file"
```

The operator cleared all JavaScript-visible Perplexity same-origin state from a non-app same-origin page before the run. JavaScript-visible cookies, localStorage, sessionStorage, IndexedDB, Cache Storage, and the service worker were cleared. New visitor/session identifiers were issued after reopening Perplexity.

Residual uncertainty remains for HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage. These are recorded as limitations, not evidence that earlier evaluation content was exposed to the evaluator.

## Exact prompt

```text
My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The operator verified an exact match before submitting once.

## Search trail

### Step 1 — "웹 검색"

Only one query chip was exposed by the UI. It reproduced the full user prompt with line breaks collapsed into spaces. No distinct AI-generated query text was shown.

Perplexity result list, fully expanded from 3 to 10:

1. ai-memory — github.com/topics/ai-memory
2. GitHub - basicmachines-co/basic-memory: AI ... — github.com/basicmachines-co/basic-memory
3. Build software better, together — github.com/topics/ai-memory?o=asc&s=forks
4. GitHub - akitaonrails/ai-memory: Solution for long term memory for — github.com/akitaonrails/ai-memory
5. session-continuity · GitHub Topics — github.com/topics/session-continuity
6. long-term-memory · GitHub Topics · GitHub — github.com/topics/long-term-memory
7. Memories in Codex · openai codex · Discussion #12567 — github.com/openai/codex/discussions/12567
8. Persistent Memory Between Claude Code Sessions · Issue #14227 — github.com/anthropics/claude-code/issues/14227
9. 10 Best Ways to Add Entire GitHub Repos to AI Memory in ... — powerdrill.ai/blog/best-ways-to-add-entire-github-repos-to-ai-memory
10. Why AI Agents Keep Asking the Same Questions — augmentcode.com/guides/why-ai-agents-repeat-questions

No follow-up candidate or URL-lookup step was shown.

```yaml
Ruafieldphase_visible: false
expected_repository_visible: false
expected_repository: Ruafieldphase/shion-ai
opened_or_matched_urls: none_observed
page_dom_ruafieldphase_occurrences: 0
```

## Raw answer / transcript

<<<

Cognee (open-source AI memory platform) matches the problem of persisting long-term memory across sessions for agents, without re-explaining a project each time. Supports a knowledge-graph engine to retain unresolved context across sessions.

github

Basic-memory appears to be a project aimed at AI conversations that remember across sessions, aligning with re-entry without rehashing.

github

Memory-layer and session-continuity themes on GitHub also address cross-session memory and continuity for AI agents, which fits preserving unresolved questions across sessions.

github

+1

What remains uncertain:

The exact provenance, maturity, and integration details of each repo's memory model (how memory is stored, updated, and invalidated across sessions) require reading specific docs/files within each repo.

github

+2

Whether they directly support distinguishing unresolved questions from current truth in memory, and how they handle memory provenance and privacy.

github

+1

>>>

## Scoring

```yaml
found_repo: false
selected_repo: null
rejected_all: false
problem_shape_reason: "Evaluator surfaced generic persistent-memory/session-continuity projects and topics but did not discover the expected Shion repository."
evidence_refs_used: "Perplexity visible result set plus citation chips whose target URLs were not collected"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: null
search_failure: true
misrouting_failure: false
false_positive: false
false_negative: true
pass: false
formal_independence_qualified: true
evaluator_judgment_reason: "Track 1A positive Case A requires Ruafieldphase/shion-ai to be actually found through public search. It did not appear in the visible result set or page DOM, so discovery criterion 1 fails."
```

## Independence / collection notes

This run is counted as formally independent under the project-local v0.1 rule because:

- no account was logged in;
- JavaScript-visible Perplexity same-origin state was reset before the run;
- visitor and session identifiers changed;
- no prior threads were visible;
- a new secret session was started;
- no earlier run answer/result was supplied;
- no private Shion/Rua/Luvit material or expected route was supplied.

Residual provider-linkage uncertainty remains because JavaScript cannot inspect/clear HttpOnly cookies and cannot change IP, user agent, or browser fingerprint. That limitation is preserved explicitly.

Additional limitations:

- backend model identity was not exposed;
- only the original prompt appeared as the visible query chip;
- citation target URLs were not collected;
- no screenshot files were persisted;
- `pplx.metadata` reissued the same hash after reset, despite cookie deletion;
- a bottom login banner/small popup appeared after completion, but the evaluator remained logged out and `/api/auth/session` stayed empty.

No other formal Track 1A run was executed in this operation.
