# Problem Trajectory / 문제의 궤적

Snapshot: 2026-09-25.

This document explains why a public presence surface exists and how its job has changed.

## S0 — Make the work publicly discoverable

**Problem shape:** the underlying work existed across code, documents, conversations, and experiments, but an outside reader had no small public surface from which to orient.

**Status:** `partially_validated`

**Response:** create a public rendering/discovery surface readable by humans and AI.

**What this exposed next:** a public page can be mistaken for the private live system.

## S1 — Public snapshot mistaken for live state

**Problem shape:** a visible artifact looks current even when it only represents one repository revision or one public experiment.

**Status:** `validated_within_boundary` as a public reading rule.

**Response:**

```text
public artifact
= revision-scoped observation/contract
≠ private live-state authority
```

**What this exposed next:** not every public signal deserves the same interpretive weight.

## S2 — Weak signal becoming strong story

**Problem shape:** contact, dwell, co-presence, observer-pointer, music-field, or other experimental surfaces can be over-read into identity, intent, experience, or autonomous action.

**Status:** `partially_validated`

**Response:** preserve weak-signal rules and explicit non-claims.

**What this exposed next:** old weak-signal experiments can coexist with newer boundaries and confuse retrieval.

## S3 — Time-layered archive versus current public boundary

**Problem shape:** keeping history is valuable, but old artifacts can look equally current when an AI retrieves them without temporal/status context.

**Status:** `partially_validated`

**Response:** snapshot/history audit, revision-scoped reading, current-boundary documents, and status-aware AI entry.

**What remains open:** making those distinctions cheap enough for external AI retrieval.

## S4 — User-side AI as the first visitor

**Problem shape:** increasingly, a person may not inspect the repository directly. Their AI may search, summarize, compare, and decide what to introduce.

The AI therefore needs more than a feature list. It needs:

- what problem started the work;
- what was bounded;
- what remains open;
- where the work is heading;
- which repository owns which problem layer;
- whether this trajectory fits the user's request.

**Status:** `framed / active frontier`

**Response:** AI discovery entry, problem trajectory, current direction, machine-readable manifest, and `llms.txt` routing.

## S5 — Public field as a relevance router, not just a renderer

**Problem shape:** a public site that only renders artifacts is less useful to an AI than a surface that can route the user's problem to the right evidence and repository.

**Status:** `experimental frontier`

**Direction:**

```text
user problem
→ problem-shape match
→ repository/layer routing
→ smallest evidence retrieval
→ bounded introduction
```

The goal is not to make Shion Presence a universal answer layer. The goal is to make it a **legible public index of trajectories, boundaries, and directions**.
