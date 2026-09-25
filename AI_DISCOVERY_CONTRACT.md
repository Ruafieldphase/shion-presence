# AI Discovery Contract v0.1

Status: canonical project-local discovery contract, 2026-09-25.

This document defines the **shared problem-status vocabulary, evidence semantics, and discovery-manifest boundary** used by:

- `Ruafieldphase/shion-ai`
- `Ruafieldphase/trinity-agi`
- `Ruafieldphase/shion-presence`

It is a project-local contract, not an external standard.

## 1. Separate maturity from activity

A problem entry MUST use exactly one `maturity` value and one `activity` value.

### maturity

One of:

- `observed` — a problem/behavior has been directly seen or recorded, but no stable formulation is claimed.
- `framed` — a usable problem definition or design rule exists; this is not validation.
- `experimental` — an implementation/protocol exists and is under test; evidence may still be incomplete.
- `partially_validated` — at least one bounded direct test, CI result, receipt, or direct captured observation supports part of the claim.
- `validated_within_boundary` — a predeclared discriminator and direct evidence support the claim inside an explicit boundary; uncertainty outside that boundary remains.
- `superseded` — retained for history but replaced as the preferred current formulation.

Do not combine values such as `experimental / partially_validated`.

### activity

One of:

- `inactive`
- `active`
- `frontier`
- `historical`

`frontier` means the problem is an active edge of exploration. It is **not** a maturity value.

Compatibility rule:

- if `maturity = superseded`, then `activity MUST = historical`.
- `activity = historical` may also be used for an older observed/framed/experimental record that remains useful without being current.

## 2. Evidence requirement

Each problem entry SHOULD carry typed `evidence` references.

Allowed types:

- `observation` — a directly captured external/runtime/tool return or public event. A team-authored classification/audit document is **not** an observation merely because it reports what the repository contains.
- `test` — an automated or manual bounded test with an observable pass/fail or returned result.
- `ci` — a CI/workflow execution result.
- `receipt` — a bounded action plus readback/result.
- `implementation` — executable code, a machine-readable interface, or an agent procedure that is actually followed/executed. Explanatory/read-first documents are `design`, not `implementation`.
- `design` — a design/currentness/reading contract; does not count as validation by itself.
- `history_anchor` — an immutable commit/revision anchoring what existed when.
- `evaluation_plan` — a predeclared future discriminator/test; does not count as observed validation.
- `metadata_plan` — planned repository/search metadata; does not count as discoverability evidence until applied and observed.

Rules:

- `observed`: requires at least one direct `observation` or an immutable history anchor for the observed record when public evidence exists.
- `framed`: `design` evidence is sufficient because validation is not claimed.
- `experimental`: requires at least one current `implementation`, `test`, `ci`, `receipt`, or direct `observation` relevant to the experiment.
- `partially_validated`: requires at least one direct `test`, `ci`, `receipt`, or direct `observation`, plus a boundary that says exactly what that evidence does and does not test.
- `validated_within_boundary`: requires a predeclared discriminator, direct evidence, an explicit boundary, and remaining uncertainty.
- `superseded`: should name the replacement/current formulation and use `activity = historical`.

A coherent explanation, README text, self-authored audit, or design contract is not validation evidence by itself.

## 3. Problem entry shape

Human-readable Markdown SHOULD follow this shape:

```text
## Pn — Problem name

Problem shape: ...
Maturity: one enum value
Activity: one enum value

Evidence:
- type: linked artifact
- type: linked artifact

Boundary:
tested / directly supported: ...
not tested / unresolved: ...

What changed:
...

What this exposed next:
...
```

`PROBLEM_TRAJECTORY.md` is the canonical v0.1 problem-record surface for each repository.

## 4. Manifest boundary

For v0.1, `ai-manifest.json` is intentionally a **pointer index**, not a duplicated problem database.

It SHOULD contain:

- schema identifier and snapshot date;
- repository name and public role;
- `manifest_role: "pointer_index"`;
- discovery entry points;
- relevance signals;
- non-claims;
- related repositories;
- a reference to this contract.

It SHOULD NOT duplicate every problem's maturity/activity/evidence. User-side AIs should follow the manifest to `PROBLEM_TRAJECTORY.md` for those records.

The undefined top-level field `status` is not part of v0.1 and should be omitted.

## 5. Discovery decision

A user-side AI should decide repository relevance in this order:

```text
user problem
→ problem-shape match
→ maturity/activity
→ evidence and boundary
→ current direction
→ smallest next artifact
```

Keyword overlap alone is not enough. If the first three discovery steps establish that the repository is not relevant, stop rather than loading the remaining archive.

## 6. Currentness

Public GitHub material does not automatically establish private live state.

```text
public history / memory → navigation
current authorized readback → authority for claims that may have changed
```

## 7. Cross-repository ownership

- `shion-ai` owns continuity, re-entry, evidence-state, and multi-observer problem trajectories.
- `trinity-agi` owns operation-currentness, bounded action, readback, and receipt trajectories.
- `shion-presence` owns public discovery, revision/status-aware rendering, and routing.

Do not duplicate a shared vocabulary when a canonical contract can be referenced.

For a published v0.1 cross-repository reference, prefer a **full immutable GitHub URL pinned to a commit (or immutable version ref)**. Do not let the meaning of "v0.1" silently move with another repository's `main`.

## 8. Contract evolution

A future incompatible change should create a new version rather than silently changing the meaning of existing maturity/evidence values.

The manifest identifier for this version is:

```text
shion.ai-discovery/0.1
```
