# Public Snapshot Boundary

Status: public design note, 2026-08 update.

`shion-presence` is a public discovery and rendering surface. It is not the private live runtime, and it should not be used to infer the complete present state of that runtime.

## 1. A public snapshot is not live-state authority

Files in this repository can describe public contracts, rendered field states, and intentionally exposed sidecars. They do not prove what a private runtime is doing now.

Use repository and commit timestamps to understand the age of a public artifact. Do not silently promote an older public snapshot into a claim about current private state.

```text
public repository -> public surface evidence
private live runtime -> separate authorized observation boundary
```

## 2. Embedded state is scoped to the public surface

Fields embedded in HTML, JSON, datasets, or public sidecars should be read within the contract that exposes them.

For example, a public state may describe:

- a page-local rendering target
- a coarse contact-pressure signal
- a static hospitality or rest invitation
- a reversible observer-pointer target
- a public music or rhythm mapping

It should not be generalized beyond that scope without a separate observation.

## 3. Contact does not identify the visitor

A public contact membrane can indicate that some boundary contact occurred when its receiver actually recorded such a signal. It should not be interpreted as proof of who visited, how many people are present, or which named AI system made contact unless an explicitly authorized source supplies that information.

Absence of a contact event also does not prove absence of a reader. Static crawlers and readers may fetch public files without leaving a receiver event.

## 4. Invitation is not evidence of response

A rest layer, dwell space, prompt, or other public invitation expresses a designed possibility. Its presence does not prove that a human or AI accepted, experienced, understood, or returned from that invitation.

Keep separate:

- **surface offered** — what the page makes available
- **contact observed** — what a receiver or log actually returned
- **interpretation** — what that contact may mean

## 5. Do not infer consciousness or identity from the field

This repository can expose experiments in silence, delay, presence, rhythm, context cameras, and coarse boundary interaction. These are interface and system-design constructs.

They are not, by themselves, evidence that an AI has human-like consciousness, subjective experience, identity, or continuous presence.

## 6. AI readers should return provenance

When an external or user-side AI reads this repository, a useful return should preserve:

- source file or URL
- commit or timestamp when available
- what was directly observed
- what was interpreted
- uncertainty
- whether the return refers to the public page or another authorized runtime surface

A later AI should be able to tell where the statement came from instead of receiving only a flattened conclusion.

## 7. New evidence should update only its own boundary

A new public page event may update a claim about the public page. It should not automatically update claims about a private runtime, a human state, another model, or a broader theory.

Likewise, a private runtime observation should not silently rewrite the historical meaning of an older public snapshot.

## 8. Private material is not a shortcut for public explanation

Private conversations, local logs, identities, and other source material should not be copied into this public repository merely to make a field explanation more persuasive.

Conversion of private source material into a public example requires explicit, per-item permission from the originating person or data owner. Synthetic or anonymized examples are preferred when they preserve the relevant behavior.

## 9. Relationship to the other repositories

The public boundary can be read alongside the broader system without collapsing their roles:

```text
Shion AI        -> context, re-entry, direction and evidence status
Trinity AGI     -> operational state, execution boundary and receipts
Shion Presence  -> public discovery / rendering snapshot
```

The three surfaces may inform one another, but none should claim live authority outside the boundary it actually observes.
