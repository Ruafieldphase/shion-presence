# AI Discovery v0.1 — Pre-Metadata Target State

Capture date: 2026-09-25 (KST)
Evaluation phase: pre-metadata publication baseline
Purpose: immutable target-state record for Track 2 and Track 1A before repository discovery metadata is changed.

## Declaration / version anchors

- contract: `e5005b38b7a452c73602c634ead71484a7a2e609`
- evaluation plan: `8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54`
- metadata plan: `4bb48282739831e0a9eb82555ae4d0a9d1759550`
- preserved v0.1 snapshot branch: `ai-discovery-v0.1-snapshot`
- preserved snapshot branch head after final pre-publish wording fixes: `5317de0f9fd19d4fb5f432928a8d155d2a216acc`

## Public default-branch state

### Ruafieldphase/shion-ai

- main SHA: `6485ad4238d54a9b8e58f30aae494638e366bf62`
- discovery publication: merged via merge commit
- `AI_DISCOVERY.md`: present on main
- `PROBLEM_TRAJECTORY.md`: present on main
- `ai-manifest.json`: present on main
- description:
  `Shion AI — local AI runtime harness for context continuity, rhythm-aware action, memory, and agent workflow stability`
- topics:
  - `agent-harness`
  - `ai`
  - `ai-agent`
  - `autonomous-ai`
  - `context-engineering`
  - `local-ai`
  - `memory`
  - `python`
- homepage: none
- latest pre-merge branch Public safety check: success
- latest current-head pre-merge Public safety run: `36081936993` — success

### Ruafieldphase/trinity-agi

- main SHA: `0dceff683dcdc86a847e6352e8c186df37e6c811`
- discovery publication: merged via merge commit
- `AI_DISCOVERY.md`: present on main
- `PROBLEM_TRAJECTORY.md`: present on main
- `ai-manifest.json`: present on main
- description:
  `Trinity AGI — body/infrastructure layer for Shion AI: local automation, scheduling, status checks, and approval boundaries`
- topics:
  - `agent-harness`
  - `agi`
  - `ai`
  - `ai-agent`
  - `automation`
  - `human-ai-collaboration`
  - `local-ai`
  - `python`
  - `typescript`
  - `workflow-automation`
- homepage:
  `https://www.youtube.com/channel/UC-o_jxk0ls6NUEk6VmuM3JA`
- latest current-head pre-merge Public safety run: `36081941917` — success

### Ruafieldphase/shion-presence

- main SHA: `3694316212929b21ebb762c28a78ecceaf18682d`
- discovery publication: merged via merge commit
- `AI_DISCOVERY.md`: present on main
- `PROBLEM_TRAJECTORY.md`: present on main
- `ai-manifest.json`: present on main
- `AI_DISCOVERY_CONTRACT.md`: present on main
- `DISCOVERY_EVAL.md`: present on main
- `REPOSITORY_DISCOVERY_METADATA.md`: present on main
- description: none
- topics: none
- homepage: none
- GitHub Pages enabled: yes
- Pages deployment/readback: not independently verified from the current execution environment at capture time; repository main contains the published source files.
- CI: no repository CI workflow was claimed for this publication.

## Metadata contamination boundary

Repository description/topics/homepage remain at their **pre-metadata** values above.

The reviewed metadata plan has **not** been applied.

Therefore this target state is suitable as the Track 1A / Track 2 pre-metadata publication baseline.

## Evaluation constraints

- Track 2 should use fresh independent contexts with the three candidate repository URLs supplied.
- Track 1A should use ordinary public search without project names supplied.
- Track 1A negative-control Case D should be observed separately for false positives.
- Metadata must not be applied before Track 1A target state and runs are preserved.
- If Pages availability is required by a specific run, record the actual Pages readback in that run rather than assuming it from `has_pages=true`.
