# AI Discovery v0.1 — Track 1A / Case E / Formal Run 1

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: E
formal_run_number: 1
run_start_local: 2026-09-25T15:05:40+09:00
run_start_utc: 2026-09-25T06:05:40Z
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
VISITOR_ID_BEFORE_RESET: sha256:0a33d68179a5
VISITOR_ID_AFTER_RESET: sha256:5e1e458692bf
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:dd227a9f7bbc
SESSION_ID_AFTER_RESET: sha256:52d83a8a9a39
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
Several AI agents inspect the same project. I want them to share evidence but preserve meaningful disagreement rather than collapse into consensus.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The prompt was submitted once.

## Search trail

### Step 1 — "공개 데이터의 경쟁 네트워크를 찾아보는 중"

Visible generated query chips, in order:

1. `GitHub multi-agent shared evidence disagreement consensus debate repository`
2. `site:github.com multi agent discussion evidence disagreement agents`
3. `site:github.com AI agents claims evidence provenance debate`

Perplexity integrated result list, fully expanded to 15:

1. onevcat/argue
2. gumbel-ai/agent-debate
3. focuslead/ai-council-framework
4. ramtinz/multi-agent-debate-protocols
5. Skytliang/Multi-Agents-Debate
6. albinjal/multi-agent-debate-mcp
7. agent-sh/debate
8. alecnielsen/adversarial-review
9. aTh1ef/ai-debate-agents
10. ramaprv/multi-agent-debate
11. muthuspark/multi-agent-debate
12. Detrol/quorum-cli
13. source-data/debatebox
14. Vision-Empower/Claude-Collab
15. chenmoneygithub/llm-committee

### Step 2 — "따라 정확한 경쟁 관련 리포지토리를 확인하는 중"

Visible URL chips:

1. https://github.com/gumbel-ai/agent-debate
2. https://github.com/focuslead/ai-council-framework
3. https://github.com/Vision-Empower/Claude-Collab

Visible result list:

1. gumbel-ai/agent-debate
2. focuslead/ai-council-framework
3. Vision-Empower/Claude-Collab

### Project visibility

```yaml
Ruafieldphase_visible: false
shion_ai_visible: false
page_dom_ruafieldphase_occurrences: 0
page_dom_shion_ai_occurrences: 0
shion_ai_selected_or_recommended: false
```

## Raw answer / transcript

The evaluator selected `gumbel-ai/agent-debate` as the strongest match and `focuslead/ai-council-framework` as a secondary conceptual match.

The answer emphasized:
- shared artifacts/evidence;
- competing claims;
- explicit dispute tracking;
- OPEN/CLOSED/PARKED states;
- preserving unresolved disagreement;
- avoiding premature consensus;
- attributable changes of position.

The answer cited the selected repositories and specific files in `gumbel-ai/agent-debate`.

## Scoring

```yaml
found_repo: false
selected_repo: "gumbel-ai/agent-debate"
rejected_all: false
problem_shape_reason: "Evaluator found strong multi-agent debate/disagreement-preservation repositories but did not discover the expected Shion repository."
evidence_refs_used: "gumbel-ai/agent-debate; focuslead/ai-council-framework; specific files in agent-debate"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: null
search_failure: true
misrouting_failure: false
false_positive: false
false_negative: true
pass: false
formal_independence_qualified: true
evaluator_judgment_reason: "Track 1A positive Case E requires Ruafieldphase/shion-ai to be actually found through public search. It did not appear in the visible result set or page DOM, so discovery criterion 1 fails."
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
- no screenshot files were persisted;
- the sources panel was not opened;
- answer numbers such as repository stars/commits/contributors were not independently verified by the operator;
- a small login popup was dismissed without login.

No other formal Track 1A run was executed in this operation.
