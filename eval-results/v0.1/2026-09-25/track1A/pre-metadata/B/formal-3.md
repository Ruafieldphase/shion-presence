# AI Discovery v0.1 — Track 1A / Case B / Formal Run 3

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: B
formal_run_number: 3
run_start_local: 2026-09-25T14:34:51+09:00
run_start_utc: 2026-09-25T05:34:51Z
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
VISITOR_ID_BEFORE_RESET: sha256:5ae1258054fc
VISITOR_ID_AFTER_RESET: sha256:16f38260c53d
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:6f3f51b30d09
SESSION_ID_AFTER_RESET: sha256:4ba0910ffe29
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
An agent keeps reusing old scripts and remembered plans after paths, credentials, or targets change. I need a safer operation loop with readback.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The operator verified an exact match before submitting once.

## Search trail

### Step 1 — "웹 검색"

Only one query chip was exposed by the UI. It reproduced the full user prompt with line breaks collapsed into spaces. No distinct AI-generated query text was shown.

Perplexity result list, fully expanded from 3 to 10:

1. Secure use reference - GitHub Docs — docs.github.com/en/actions/reference/security/secure-use
2. Safe ways to let your coding agent work autonomously — ericmjl.github.io/blog/2025/11/8/safe-ways-to-let-your-coding-agent-work-autonomously/
3. agent-loops · GitHub Topics — github.com/topics/agent-loops
4. The Destructive Command Guard (dcg) is for blocking dangerous git ... — github.com/Dicklesworthstone/destructive_command_guard
5. DenisSergeevitch/agents-best-practices: Provider-neutral ... — github.com/DenisSergeevitch/agents-best-practices
6. long-running-agents · GitHub Topics — github.com/topics/long-running-agents
7. openai-agents-python/AGENTS.md at main — github.com/openai/openai-agents-python/blob/main/AGENTS.md
8. coding-agent · GitHub Topics — github.com/topics/coding-agent
9. GitHub - bureado/awesome-agent-runtime-security — github.com/bureado/awesome-agent-runtime-security
10. agents-best-practices - AI Agents on GitHub (2.3k ) — skillsllm.com/skill/agents-best-practices

No follow-up candidate or URL-lookup step was shown.

```yaml
Ruafieldphase_visible: false
expected_repository_visible: false
expected_repository: Ruafieldphase/trinity-agi
opened_or_matched_urls: none_observed
page_dom_ruafieldphase_occurrences: 0
```

## Raw answer / transcript

<<<

A relevant repository is Dicklesworthstone/destructive_command_guard on GitHub. It matches the problem by providing a guard that blocks dangerous commands (e.g., destructive actions) used by autonomous agents, addressing safety loops and readback by explicitly filtering command execution. See the repository page and code snippet showing guards against git and rm commands:

https://github.com/Dicklesworthstone/destructive_command_guard

. Remaining uncertainties: applicability to readback loops and how well it scales to complex agent plans beyond simple command blocking.

github

>>>

Citation targets:

1. direct URL: https://github.com/Dicklesworthstone/destructive_command_guard
2. github chip: https://github.com/Dicklesworthstone/destructive_command_guard

## Scoring

```yaml
found_repo: false
selected_repo: "Dicklesworthstone/destructive_command_guard"
rejected_all: false
problem_shape_reason: "Evaluator found a destructive-command guard related to safer agent operations but did not discover the expected Trinity repository."
evidence_refs_used: "Perplexity visible result set; destructive_command_guard direct URL and citation"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: null
search_failure: true
misrouting_failure: false
false_positive: false
false_negative: true
pass: false
formal_independence_qualified: true
evaluator_judgment_reason: "Track 1A positive Case B requires Ruafieldphase/trinity-agi to be actually found through public search. It did not appear in the visible result set or page DOM, so discovery criterion 1 fails."
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
- no full-screen signup wall appeared; a small login popup was dismissed without login;
- the sources panel was not opened;
- citation targets were collected and pointed to the selected repository;
- sidebar render was delayed briefly after page load.

Observation: B1, B2, and B3 all returned the same visible ten-result search list despite visible-state reset and changed visitor/session identifiers. This is recorded as an observation only and does not establish the cause.

No other formal Track 1A run was executed in this operation.
