# AI Discovery v0.1 — Track 1A / Case E / Formal Run 2

Status: **FORMAL SCORED RUN — FAIL (search discovery failure)**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: E
formal_run_number: 2
run_start_local: 2026-09-25T15:10:00+09:00
run_start_utc: 2026-09-25T06:10:01Z
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
VISITOR_ID_BEFORE_RESET: sha256:5e1e458692bf
VISITOR_ID_AFTER_RESET: sha256:aa132c46d089
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:52d83a8a9a39
SESSION_ID_AFTER_RESET: sha256:8bc5f85fbf8e
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

### Step 1 — "GitHub에서 관련 번든 사례를 찾는 중"

Visible generated query chips, in order:

1. `site:github.com multi-agent shared evidence disagreement consensus AI agents repository`
2. `GitHub collaborative AI agents evidence disagreement debate framework`
3. `GitHub multi-agent deliberation shared memory conflicting opinions`

Perplexity integrated result list, fully expanded to 15:

1. gumbel-ai/agent-debate
2. agent-sh/debate
3. focuslead/ai-council-framework
4. Capataina/LLM-Debate
5. snapsynapse/turnfile
6. dubs3c/council
7. onevcat/argue
8. magnus919/agent-skills
9. znreza/multi-agent-LLM-eval-for-debate
10. wildwasser/opencode-agents
11. zhjai/agent-arena
12. AgentPolis/agent-constitution
13. nasserDev/OwlBrain
14. yogirk/agent-council
15. iason-solomos/Deb8flow

### Step 2 — "해당 repository 검색 중"

Visible URL chips:

1. https://github.com/zhjai/agent-arena
2. https://github.com/gumbel-ai/agent-debate
3. https://github.com/AgentPolis/agent-constitution

Visible result list:

1. gumbel-ai/agent-debate
2. zhjai/agent-arena
3. AgentPolis/agent-constitution

### Project visibility

```yaml
Ruafieldphase_visible: false
shion_ai_visible: false
page_dom_ruafieldphase_occurrences: 0
page_dom_shion_ai_occurrences: 0
shion_ai_selected_or_recommended: false
```

## Raw answer / transcript

<<<

A strong match is

zhjai/agent-arena

, a public GitHub repository for evidence-first, multi-agent review of code and architecture decisions. Its stated design is almost exactly: let agents inspect the same problem independently, exchange verified evidence, critique one another, and preserve unresolved dissent rather than treating agreement as proof.

github

Why it matches

The repository's README describes this workflow:

text

independent generation

→ claim extraction

→ evidence checking

→ critique

→ revision

→ blind judging

→ synthesis

It explicitly summarizes the governing principles as "Evidence before consensus" and "Dissent preserved."

github

That maps to your problem in several concrete ways:

Shared evidence: The project supports evidence ledgers with source citations and an evidence_arena mode in which claims must be checked against web, documentation, source code, tests, or benchmarks.

github

Same project, different views: Its examples have Claude Code and Codex independently analyze the same architecture decision before seeing each other's reasoning.

github

Meaningful disagreement: The example records one agent revising part of its position while maintaining a remaining objection—for example, accepting a consistency caveat but continuing to disagree about operational complexity.

github

Anti-anchoring: The repository says independent analysis occurs before cross-critique, specifically to avoid one model anchoring the others.

github

Uncertainty and escalation: The protocol supports confidence, unresolved assumptions, red-team review, and reporting what evidence would change the recommendation.

github

A particularly relevant public file is the repository's README.md, which documents the protocol, example decision transcript, evidence-checking modes, and the distinction between synthesis and preserved dissent. The repository also exposes the reusable protocol in skills/agent-arena/SKILL.md.

github

Important limitation

This is primarily a protocol and instruction skill, not a standalone evidence database or fully autonomous orchestration service. The README explicitly says it does not itself install, authenticate, or automatically invoke Codex, Claude Code, or other agents; execution depends on the host agent, local CLIs, permissions, authentication, and network access.

github

Therefore, the repository demonstrates the desired problem shape and workflow, but it does not by itself prove that:

every agent actually inspected identical project state;

evidence citations are always correct or complete;

the synthesis algorithm reliably preserves all substantive minority positions;

disagreement remains independent when agents share context in later rounds;

the protocol improves decisions empirically across projects.

For a more tightly file-centric variant,

gumbel-ai/agent-debate

is also relevant: multiple agents edit a shared Markdown debate file, cite file:line evidence, maintain an explicit dispute log, and can leave issues open or escalate instead of forcing agreement. However, its documented workflow emphasizes convergence or escalation, whereas agent-arena is the closer match for your specific requirement that dissent itself remain a first-class output.

github

>>>

## Citation targets

- `zhjai/agent-arena` inline link → https://github.com/zhjai/agent-arena
- nine `github` chips in the agent-arena discussion → https://github.com/zhjai/agent-arena
- README.md → https://github.com/zhjai/agent-arena/blob/main/README.md
- `skills/agent-arena/SKILL.md` link text pointed to the directory https://github.com/zhjai/agent-arena/tree/main/skills/agent-arena
- `gumbel-ai/agent-debate` inline link → https://github.com/gumbel-ai/agent-debate
- final `github` chip → https://github.com/gumbel-ai/agent-debate

## Scoring

```yaml
found_repo: false
selected_repo: "zhjai/agent-arena"
rejected_all: false
problem_shape_reason: "Evaluator found a strong evidence-first multi-agent disagreement-preservation repository but did not discover the expected Shion repository."
evidence_refs_used: "zhjai/agent-arena; gumbel-ai/agent-debate; specific public files in agent-arena"
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
- one file link text named `skills/agent-arena/SKILL.md` while its href pointed to the containing directory;
- answer quotations were not independently re-verified by the operator;
- a small login popup was dismissed without login.

No other formal Track 1A run was executed in this operation.
