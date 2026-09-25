# AI Discovery Contract v0.1

Status: canonical project-local discovery contract, 2026-09-25.

This document defines the **shared machine-readable status vocabulary and evidence rules** used by:

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
- `partially_validated` — at least one bounded direct test, CI result, public receipt, or equivalent observation supports part of the claim.
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

## 2. Evidence requirement

Each problem entry SHOULD carry `evidence` references. Evidence references must be typed.

Allowed types:

- `observation` — direct public observation or captured return
- `test` — automated or manual bounded test
- `ci` — CI/workflow execution
- `receipt` — bounded action + readback result
- `implementation` — code/protocol that makes the experiment executable
- `design` — design/currentness contract; does not count as validation by itself
- `history_anchor` — immutable commit/revision anchoring what existed when
- `evaluation_plan` — predeclared future discriminator/test; does not count as observed validation
- `metadata_plan` — planned repository/search metadata; does not count as discoverability evidence until applied and observed

Rules:

- `observed`: requires at least one observation or history anchor when public evidence exists.
- `framed`: design evidence is sufficient because validation is not claimed.
- `experimental`: requires at least one implementation or experiment reference.
- `partially_validated`: requires at least one direct `test`, `ci`, `receipt`, or equivalent observation plus a stated boundary.
- `validated_within_boundary`: requires a predeclared discriminator, direct evidence, an explicit boundary, and remaining uncertainty.
- `superseded`: should name the replacement/current formulation.

A coherent explanation, README text, or design contract is not validation evidence by itself.

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
...

What changed:
...

What this exposed next:
...
```

Machine-readable forms SHOULD preserve the same separation.

## 4. Discovery decision

A user-side AI should decide repository relevance in this order:

```text
user problem
→ problem-shape match
→ maturity/activity
→ evidence and boundary
→ current direction
→ smallest next artifact
```

Keyword overlap alone is not enough.

## 5. Currentness

Public GitHub material does not automatically establish private live state.

```text
public history / memory → navigation
current authorized readback → authority for claims that may have changed
```

## 6. Cross-repository ownership

- `shion-ai` owns continuity, re-entry, evidence-state, and multi-observer problem trajectories.
- `trinity-agi` owns operation-currentness, bounded action, readback, and receipt trajectories.
- `shion-presence` owns public discovery, revision/status-aware rendering, and routing.

Do not duplicate a shared vocabulary when a canonical contract can be referenced.

## 7. Contract evolution

A future incompatible change should create a new version rather than silently changing the meaning of existing maturity values.

The manifest identifier for this version is:

```text
shion.ai-discovery/0.1
```
