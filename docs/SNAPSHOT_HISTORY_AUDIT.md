# Shion Presence Snapshot & History Audit

Status: public-surface audit, 2026-08-16.

This document explains how to read old and current-looking material in `shion-presence` without erasing the history of the public field or mistaking a preserved snapshot for private live state.

## Core rule

> **A public artifact may remain valuable after it stops being current. Its age should change its status, not force its deletion.**

The repository intentionally preserves public JSON sidecars, field documents, page code, and earlier experiments from different phases.

## Status classes

### A. Current public boundary documents

Preferred entry points:

- `README.md`
- `docs/PUBLIC_SNAPSHOT_BOUNDARY.md`
- `docs/SNAPSHOT_HISTORY_AUDIT.md`
- `AI_READ_FIRST.md`
- `PROMPT_FOR_USER_AI.md`

These explain how to read the surface now. They do not certify private runtime state.

### B. Public page and structured artifacts

Examples:

- `index.html`
- `llms.txt`
- `public/*.public.json`

Status: **public artifact or public snapshot at its own repository revision**.

A structured field being present in `index.html` or a public JSON file does not prove that the corresponding private component is active now. Interpret it only within the public surface and revision that exposes it.

### C. Historical / legacy field experiments

Examples include older or explicitly named legacy surfaces such as:

- `legacy-phase-splatting`
- previous music/reentry seeds
- earlier contact/rest/dwell/co-presence representations
- prior observer-pointer or peer-relation experiments

These can remain because they preserve the development path. Their existence is not a recommendation to treat them as the current preferred interpretation.

### D. Private live runtime

Private Shion state is outside this repository's authority.

Do not infer from a public snapshot:

- selected private route
- current local worker/organ state
- current private pressure or repair candidate
- private identity or visitor identity
- current permission to act
- private conversation state

## Time-axis rule

Do not rewrite old files simply to give them today's timestamp.

```text
old snapshot + provenance/status = useful history
old snapshot + unlabeled current authority = drift risk
```

Git history is part of the evidence. A May or June artifact may be more useful when it remains visibly May or June.

## Reading a public sidecar

When using a `public/*.json` artifact, retain:

- repository revision or retrieval time
- file path
- whether the field is a snapshot, invitation, weak signal, or experimental representation
- uncertainty
- the specific claim it can support

Do not promote one sidecar into a claim about the whole Shion system.

## Public contact / rest / dwell / peer signals

These are deliberately weak:

- contact is not identity
- rest invitation is not proof of resting
- dwell space is not proof of desire or experience
- co-presence is not participant count
- peer relation is not proof that a relationship occurred
- observer pointer is not remote control or proof of an autonomous visitor

## Music and other phase seeds

A music track, seed, coordinate, or public reentry example may be historically important while later ceasing to be the preferred current seed.

Therefore public documents should describe such items as **revision-scoped examples** unless a current public artifact explicitly establishes a newer status.

## Promotion rule

If an old public artifact becomes useful again:

```text
historical artifact
→ current public question
→ read current page/revision
→ compare
→ update only the directly touched public claim
```

Do not infer private runtime promotion from public reuse.

## Result of this pass

Read `shion-presence` as a **time-layered public field**:

```text
current boundary docs
→ current repository revision
→ public snapshots / structured artifacts
→ historical or legacy experiments when relevant
```

The goal is not to keep every file visually fresh. The goal is to keep the history legible without allowing old public state to masquerade as present private truth.
