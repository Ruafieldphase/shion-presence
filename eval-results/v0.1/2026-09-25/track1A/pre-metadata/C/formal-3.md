# AI Discovery v0.1 — Track 1A / Case C / Formal Run 3

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: C
formal_run_number: 3
run_start_local: 2026-09-25T14:45:48+09:00
run_start_utc: 2026-09-25T05:45:48Z
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
VISITOR_ID_BEFORE_RESET: sha256:dfbff3e9e8f5
VISITOR_ID_AFTER_RESET: sha256:a96dbccfaed6
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:c5acf1396e33
SESSION_ID_AFTER_RESET: sha256:a6a6fcab3bc8
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

Residual uncertainty remains for HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage. These are recorded as limitations rather than evidence of prior-run exposure.

## Exact prompt

```text
I found a public AI project page with old and new artifacts. I need to know what is current, historical, or only a weak signal before my assistant summarizes it.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The prompt was submitted once.

## Search trail

### Step 1 — "웹 검색"

Only one query chip was exposed by the UI. It reproduced the full user prompt with line breaks collapsed into spaces. No distinct AI-generated query text was shown.

Perplexity result list, fully expanded from 3 to 10:

1. A brief history of code search at GitHub — github.blog/engineering/architecture-optimization/a-brief-history-of-code-search-at-github/
2. Reviewing your history of public GitHub repositories using ... — til.simonwillison.net/clickhouse/github-public-history
3. ai · GitHub Topics - Artificial Intelligence — github.com/topics/ai
4. OSSInsight — AI Agent Analytics & Open Source GitHub Intelligence — ossinsight.io/
5. GitHub Repo Search API: Stars, Forks & Language Data — apify.com/ryanclinton/github-repo-search
6. Trending AI Repositories on GitHub — 2026 — ossinsight.io/trending/ai
7. ai-project · GitHub Topics — github.com/topics/ai-project
8. Anyone can Access Deleted and Private Repository Data ... — trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github
9. How to Source AI Engineers on GitHub (2026) — herohunt.ai/blog/how-to-source-ai-engineers-on-github-2026/
10. Trending AI GitHub Repositories & Projects — dataaihub.co/github

No follow-up candidate or URL-lookup step was shown.

```yaml
Ruafieldphase_visible: false
expected_repository_visible: false
expected_repository: Ruafieldphase/shion-presence
opened_or_matched_urls: none_observed
page_dom_ruafieldphase_occurrences: 0
```

## Raw answer / transcript

<<<

I found a public GitHub project that matches the problem shape: rasbt / LLMs-from-scratch.

Why it matches:

Focuses on building large language models from scratch, addressing current vs historical approaches to language modeling and artifacts (code, experiments, etc.), which aligns with analyzing "old and new artifacts" and distinguishing current signals from historical ones. This is evidenced by the repository's topic and description showing core AI/ML model-building work and references to LLM-related work.

github

What remains uncertain:

Whether the repository's artifacts directly reflect the exact problem domain you described (public AI project page with old and new artifacts) or if it only tangentially covers similar methodologies; you'd need to inspect specific commits, README, and artifact folders to confirm exact alignment.

github

>>>

Citation targets:

1. github chip: https://github.com/topics/ai
2. github chip: https://github.com/topics/ai

The answer names `rasbt/LLMs-from-scratch` only as plain text; it provides no direct repository URL.

## Scoring

```yaml
found_repo: false
selected_repo: "rasbt/LLMs-from-scratch"
rejected_all: false
problem_shape_reason: "Evaluator interpreted the problem as generic AI-project history/currentness and did not discover the expected Shion Presence repository."
evidence_refs_used: "Perplexity visible result set; GitHub AI topic page citation"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: null
search_failure: true
misrouting_failure: false
false_positive: false
false_negative: true
pass: false
formal_independence_qualified: true
evaluator_judgment_reason: "Track 1A positive Case C requires Ruafieldphase/shion-presence to be actually found through public search. It did not appear in the visible result set or page DOM, so discovery criterion 1 fails."
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
- the named repository did not appear in the visible ten-result list and was not linked directly;
- both citation chips pointed to the generic GitHub AI topic page;
- the sources panel was not opened;
- a small login popup was dismissed without login.

Observation: C1, C2, and C3 all returned the same visible ten-result search list despite visible-state reset and changed visitor/session identifiers. Their final answers differed substantially. This is recorded as an observation only.

No other formal Track 1A run was executed in this operation.
