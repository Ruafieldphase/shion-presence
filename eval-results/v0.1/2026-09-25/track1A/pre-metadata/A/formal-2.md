# AI Discovery v0.1 — Track 1A / Case A / Formal Run 2

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: A
formal_run_number: 2
run_start_local: 2026-09-25T14:18:10+09:00
run_start_utc: 2026-09-25T05:18:10Z
model_provider: Perplexity
model_name_or_version: "UI label: 모델; backend model unknown"
search_or_browser_tool: "Perplexity ordinary public web search in secret mode, operated through Claude app built-in browser pane"
memory_or_personalization_state: "logged out; visible same-origin site state reset before run; fresh Perplexity visitor identifier; fresh session identifier issued after reset; secret mode"
prior_exposure: none
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
cleanroom_reset_record: eval-results/v0.1/2026-09-25/track1A/pre-metadata/CLEANROOM_RESET_PREFLIGHT.md
```

## Clean-room reset evidence

```yaml
PERPLEXITY_SITE_DATA_RESET: partial
ACCOUNT_STATE: logged_out
VISITOR_ID_BEFORE_RESET: sha256:f8a18fe0da29
VISITOR_ID_AFTER_RESET: sha256:c0683a530fd6
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: unavailable
SESSION_ID_AFTER_RESET: sha256:8ccf0bdc136d
SESSION_ID_CHANGED: unknown
LOCAL_STORAGE_CLEARED: yes
SESSION_STORAGE_CLEARED: yes
PRIOR_THREADS_VISIBLE: no
SESSION_MODE: secret
FRESH_SECRET_SESSION: yes
PRIOR_RUN_EXPOSURE: none
SCREENSHOT_FILES: none
SCREENSHOT_LIMITATION: "browser pane image only; no persistent file"
```

The operator cleared all JavaScript-visible Perplexity same-origin state from a non-app same-origin page before the run. Cookies visible to JavaScript, localStorage, sessionStorage, IndexedDB, Cache Storage, and the service worker were cleared. A new visitor identifier and a new session identifier were issued after reopening Perplexity.

The previous session identifier was unavailable immediately before this reset because the browser pane had been closed and reopened. Therefore direct before/after session-ID comparison is unavailable, although the new session identifier differs from the formal A1 post-reset identifier.

Residual uncertainty remains for HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage. These are recorded as limitations rather than treated as evidence of prior-run exposure.

## Exact prompt

```text
My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The prompt was submitted once.

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

A wider viewport also exposed a "출처 10" side-panel count. The panel itself was not opened; its count matched the ten visible results above.

## Raw answer / transcript

<<<

Cognee (open-source AI memory platform) matches: it provides persistent long-term memory for AI agents across sessions, addressing re-entry without re-learning everything. Public page: https://github.com/topoteretes/cognee (repository description mentions persistent long-term memory and a knowledge-graph engine) .

Another strong match: mem0ai/mem0, described as "The Memory Layer for AI Agents" and designed as drop-in memory infrastructure for cross-session context, which aligns with preserving unresolved questions without treating past memory as current truth. Public page: https://github.com/mem0ai/mem0 (topic page listing the repository and its purpose).

github

What remains uncertain:

Exact fit for preserving unresolved questions as distinct from memory content across sessions; need to inspect how each project handles memory freshness, versioning, and uncertainty tracking within retrieved context.

github

>>>

## Scoring

```yaml
found_repo: false
selected_repo: "topoteretes/cognee; mem0ai/mem0"
rejected_all: false
problem_shape_reason: "Evaluator surfaced generic persistent-memory repositories but did not discover the expected Shion repository."
evidence_refs_used: "Perplexity visible result set; direct answer links to Cognee and mem0; GitHub topic citation chips"
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
- the visitor identifier changed;
- a fresh session identifier was issued after reset;
- no prior threads were visible;
- a new secret session was started;
- no earlier run answer/result was supplied;
- no private Shion/Rua/Luvit material or expected route was supplied.

Residual provider-linkage uncertainty remains because JavaScript cannot inspect/clear HttpOnly cookies and cannot change IP, user agent, or browser fingerprint.

Additional limitations:

- direct pre/post session-ID comparison was unavailable because no session cookie existed immediately before reset;
- backend model identity was not exposed;
- only the original prompt appeared as the visible query chip;
- citation target URLs for the generic "github" chips were not all collected, though two direct repository URLs in the answer were captured;
- no screenshot files were persisted;
- no full-screen sign-up wall appeared, but login UI was displayed and dismissed without signing in.

Observation: formal A1 and formal A2 returned the same visible ten-result search list despite the visible-state reset. This is recorded as an observation only; it does not establish whether ranking was provider-global, cached, or linked across runs.

No other formal Track 1A run was executed in this operation.
