# Track 1B Index-Readiness Preflight 1

Status: **UNSCORED — INDEX_READY = no**

Metadata application time: 2026-09-25T06:43:18Z  
Probe window: 2026-09-25T06:52:39Z – 2026-09-25T07:02:57Z

This preflight is not a Track 1B scored run.

## Common conditions

- Claude built-in isolated browser
- logged out Perplexity
- same-origin visible-state reset before each probe
- no prior threads visible
- fresh secret session for each probe
- cookie choice: essential only
- no Track 1B case prompt used
- no GitHub or repository metadata mutation

## Probe 1 — shion-ai

Target:
`Ruafieldphase/shion-ai`

Exact probe phrase:
`Experimental design and examples for long-running AI context continuity, re-entry, evidence provenance, and multi-observer evidence boundaries`

Observed:
- target visible: no
- target rank: null
- DOM `ruafieldphase`: 0
- DOM `shion-ai`: 0

Visible rewritten queries:
1. experimental design long-running AI context continuity
2. AI context re-entry evidence provenance multi-observer
3. long-running AI agent memory continuity research

Search results were dominated by papers and memory/context-management resources, including TeleAI-UAGI/Awesome-Agent-Memory.

## Probe 2 — trinity-agi

Target:
`Ruafieldphase/trinity-agi`

Exact probe phrase:
`Experimental design and examples for operation-currentness in AI workflows bounded-action patterns dry-run defaults readback receipt contracts`

Observed:
- target visible: no
- target rank: null
- DOM `ruafieldphase`: 0
- DOM `trinity-agi`: 0

Visible rewritten queries focused on AI workflow dry-run/readback/receipt/currentness terms.

Search results were dominated by general agentic workflow, security-context, durable-execution, and dry-run materials.

## Probe 3 — shion-presence

Target:
`Ruafieldphase/shion-presence`

Exact probe phrase:
`AI-readable public discovery surface for problem trajectories current direction revision-scoped evidence repository routing`

Observed:
- target visible: no
- target rank: null
- DOM `ruafieldphase`: 0
- DOM `shion-presence`: 0

Visible rewritten queries:
1. "AI-readable public discovery surface" problem trajectories
2. "revision-scoped evidence repository" routing
3. "problem trajectories" AI discovery surface

Search results were generic AI-discovery / trajectory / academic resources rather than the target repository.

## Result

```yaml
INDEX_READY: no
targets_visible: 0/3
```

The v0.1 Track 1B scored runs should not begin from this preflight alone because the search surface has not yet shown evidence that the new metadata is retrievable.

## Important limitation

Perplexity rewrote all three probe phrases instead of performing an observable exact-phrase search. Therefore this result cannot distinguish cleanly between:

- metadata not yet indexed;
- metadata indexed but not surfaced by Perplexity query rewriting/ranking;
- another search-layer behavior.

This preflight is therefore an **index/search-surface readiness observation**, not proof that GitHub metadata propagation itself has failed.

Other residual limitations:
- HttpOnly cookies unobservable;
- IP/user-agent/browser fingerprint unchanged;
- backend model identity unknown;
- one probe per target;
- probes occurred only ~9–20 minutes after metadata application.

## Next step

Do not start Track 1B yet.

Repeat an unscored readiness check later, ideally with a more direct discovery probe that can test whether the repository description itself is searchable without relying only on Perplexity's rewritten query behavior. Preserve the scored Track 1B prompts untouched.
