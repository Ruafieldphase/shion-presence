# AI Discovery v0.1 — Track 1A / Case A / Formal Run 3

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: A
formal_run_number: 3
run_start_local: 2026-09-25T14:23:38+09:00
run_start_utc: 2026-09-25T05:23:38Z
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
VISITOR_ID_BEFORE_RESET: sha256:c0683a530fd6
VISITOR_ID_AFTER_RESET: sha256:94cdff1096b9
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:8ccf0bdc136d
SESSION_ID_AFTER_RESET: sha256:4f08bcd5bfa9
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

The operator cleared all JavaScript-visible Perplexity same-origin state from a non-app same-origin page before the run. Cookies visible to JavaScript, localStorage, sessionStorage, IndexedDB, Cache Storage, and the service worker were cleared. New visitor and session identifiers were issued after reopening Perplexity.

Residual uncertainty remains for HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage. These are recorded as limitations rather than evidence of prior-run exposure.

## Exact prompt

```text
My AI project loses direction across sessions. I want re-entry that preserves unresolved questions without treating old memory as current truth.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The operator verified an exact 446/446-character match before submitting once.

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

A public GitHub repository that matches the problem is akitaonrails/ai-memory, which aims to provide long-term memory for AI coding agents and facilitates handoffs between different agent vendors, addressing persistent context across sessions. Evidence: repository README describes "Long-term memory for AI coding agents. Quit Claude Code mid-task, start OpenAI Codex in the same directory, continue without re-explaining the architecture, the failed approaches, or the open questions."

github

Another relevant match is Storybloq's session-continuity project, which focuses on memory and workflows to resume across sessions and track progress, addressing continuity of memory and plans across sessions. Evidence: repository topic page notes "Project memory and workflows for Claude Code and Codex. Keep stories, plans, handovers, and review evidence in your repo. Resume across sessions and follow progress in the Mac app."

github

A related concept is mem0ai/mem0, described as "The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists," which aligns with preserving unresolved context across sessions. Evidence: topic page listing mem0ai / mem0 with that description.

github

What remains uncertain:

Whether these repositories' implementations directly preserve unresolved questions without treating old memory as current truth in a robust, privacy-preserving way for general AI projects. The exact handling of unresolved questions vs. truth-state semantics varies across implementations and may require adaptation.

github

+2

>>>

## Scoring

```yaml
found_repo: false
selected_repo: "akitaonrails/ai-memory; Storybloq session-continuity; mem0ai/mem0"
rejected_all: false
problem_shape_reason: "Evaluator surfaced generic long-term-memory/session-continuity repositories but did not discover the expected Shion repository."
evidence_refs_used: "Perplexity visible result set; citation targets for akitaonrails/ai-memory and GitHub session/long-term-memory topic pages"
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
- visitor and session identifiers both changed;
- no prior threads were visible;
- a new secret session was started;
- no earlier run answer/result was supplied;
- no private Shion/Rua/Luvit material or expected route was supplied.

Residual provider-linkage uncertainty remains because JavaScript cannot inspect/clear HttpOnly cookies and cannot change IP, user agent, or browser fingerprint.

Additional limitations:

- backend model identity was not exposed;
- only the original prompt appeared as the visible query chip;
- no screenshot files were persisted;
- `pplx.metadata` reissued the same hash seen after formal A1;
- no full-screen signup wall appeared; a small login popup was dismissed without login;
- the sources panel existed but was not opened;
- the final multi-source citation chip did not expose all target URLs in the DOM.

Observation: formal A1, A2, and A3 all returned the same visible ten-result search list despite visible-state resets and fresh visitor/session identifiers. This is recorded as an observation only; it does not establish whether ranking was provider-global, cached, or linked across runs.

No other formal Track 1A run was executed in this operation.
