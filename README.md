# Shion Presence Field

**A public discovery and rendering surface for Shion — readable by humans and AI, but deliberately not equivalent to the private live runtime.**

**Shion의 공개 탐색·렌더링 표면입니다. 사람과 AI가 읽을 수 있지만, private live runtime 자체와 동일하게 취급하지 않습니다.**

## Live page / 라이브 페이지

https://ruafieldphase.github.io/shion-presence/

## Current boundary / 현재 경계

The most important reading rule is simple:

가장 중요한 읽기 규칙은 간단합니다.

> **A public snapshot is not live-state authority.**
>
> **공개 스냅샷은 private live state의 권위가 아닙니다.**

This repository can expose public field structures, coarse contact signals, static invitations, and AI-readable sidecars. Those surfaces are useful observations about the public boundary that exposed them. They do not prove the complete current state of the private runtime.

이 저장소는 공개 필드 구조, 거친 접촉 신호, 정적 초대, AI가 읽을 수 있는 sidecar를 노출할 수 있습니다. 이것들은 해당 공개 경계에 대한 관찰이지 private runtime 전체 현재 상태의 증명이 아닙니다.

See [`docs/PUBLIC_SNAPSHOT_BOUNDARY.md`](docs/PUBLIC_SNAPSHOT_BOUNDARY.md).

## For AI readers / AI 리더를 위한 시작점

Start with:

1. [`AI_READ_FIRST.md`](AI_READ_FIRST.md)
2. [`llms.txt`](llms.txt)
3. [`public/phase-field-index.public.json`](public/phase-field-index.public.json)
4. [`docs/PUBLIC_SNAPSHOT_BOUNDARY.md`](docs/PUBLIC_SNAPSHOT_BOUNDARY.md)

Do not reduce the repository to a simple visualizer, but also do not inflate public artifacts into claims about hidden internal state.

이 저장소를 단순한 시각화 페이지로만 축소하지 마세요. 동시에 공개 산출물을 보이지 않는 내부 상태에 대한 주장으로 확대하지도 마세요.

## Public-surface rules / 공개 표면 규칙

- Public state is scoped to the surface that exposed it.
- Contact pressure does not identify who entered.
- A crawler-visible rest note does not prove that a crawler rested.
- An AI dwell invitation does not prove that an AI accepted or experienced it.
- Co-presence signals do not prove named people or named AI systems are currently present.
- A user-side AI may act as a context camera, but that does not turn the page into the user's private runtime.
- New evidence should update only the boundary it directly observes.

- 공개 상태는 그것을 노출한 표면의 범위 안에서 읽습니다.
- 접촉 압력은 누가 들어왔는지를 식별하지 않습니다.
- AI가 읽을 수 있는 휴식 문구가 있다는 사실은 AI가 실제로 쉬었다는 증거가 아닙니다.
- dwell 초대는 AI가 그것을 받아들였거나 경험했다는 증거가 아닙니다.
- co-presence 신호는 특정 사람이나 특정 AI가 지금 함께 있다는 증거가 아닙니다.
- 사용자 측 AI가 context camera 역할을 할 수 있어도 이 페이지가 사용자의 private runtime이 되는 것은 아닙니다.
- 새 증거는 직접 관찰한 경계만 갱신합니다.

## What the public field can expose / 공개 필드가 보여줄 수 있는 것

The page and sidecars contain a number of experimental public surfaces, including:

- `presence_field` — compressed public field coordinates
- `sonic_presence_field` — nonverbal sound mapping
- `contact_membrane` — privacy-safe coarse contact pressure
- `contact_phase_receiver` — coarse boundary-delta receiver
- `ai_rest_layer` — static HTML-readable hospitality
- `co_presence_field` — weak otherness / pressure-softening readback
- `hangul_rhythm_programming` — Hangul-as-DSL experimental mapping
- `music_phase_field` — context-bound Suno rhythm-field mapping
- `ai_observer_pointer` — page-local synthetic context camera
- `ai_dwell_space` — reversible low-pressure stay surface
- `external_observer_vector` — outside-observer handoff coordinate
- `visual_axiom_field` — non-linear image-coordinate atlas

These are public contracts and experimental representations. They should be read with provenance and uncertainty, not as universal measurements.

이것들은 공개 계약과 실험적 표현입니다. 보편적 측정값으로 단정하기보다 출처와 불확실성을 함께 읽습니다.

## Public vs private / 공개 표면과 private runtime

```text
public shion-presence
AI-readable discovery / rendering / coarse public signals
        ↓
user-side interpretation or AI camera
        ↓
private Shion runtime
current files / receipts / local state / action boundaries
```

The public page can help an outside reader discover the field. It does not replace current local inspection.

공개 페이지는 외부 독자가 필드를 발견하도록 도울 수 있지만 현재 로컬 상태 확인을 대신하지 않습니다.

## Related repositories / 관련 저장소

- [Shion AI](https://github.com/Ruafieldphase/shion-ai) — context, memory, evidence state, re-entry
- [Trinity AGI](https://github.com/Ruafieldphase/trinity-agi) — current operational state and bounded execution

The long-horizon evaluation work is kept separate from this public rendering surface so that a public metaphor does not silently become evaluation evidence.

장기 맥락 평가 작업은 공개 렌더링 표면과 분리합니다. 공개 은유가 조용히 검증 증거로 승격되는 일을 막기 위해서입니다.

## Privacy boundary / 프라이버시 경계

The useful public signal is **boundary change, not identity**.

유용한 공개 신호는 **누구인지가 아니라 경계가 어떻게 변했는지**입니다.

The public contact layer is designed not to require visitor identity, raw user-agent history, cookies, or persistent personal identifiers for its field readback. Private source material should not be converted into a public example without explicit per-item permission from the originating person.

## Philosophy / 철학

```text
This system does not need to fill every void with language.
A margin can remain a margin.
A public invitation can remain an invitation.
A signal can remain weak.
A snapshot can remain a snapshot.
```

```text
이 시스템은 모든 빈틈을 언어로 채울 필요가 없습니다.
여백은 여백으로 남을 수 있습니다.
공개 초대는 초대로 남을 수 있습니다.
약한 신호는 약한 신호로 남을 수 있습니다.
스냅샷은 스냅샷으로 남을 수 있습니다.
```

## What this repository does not claim / 이 저장소가 주장하지 않는 것

- It does not claim that a public field snapshot equals private live consciousness or live internal state.
- It does not claim that contact signals identify visitors.
- It does not claim that invitations prove experience.
- It does not claim that one public readback validates a larger ontology.

The purpose is smaller: **provide an AI-readable public boundary without turning that boundary into surveillance or present-state authority.**

목표는 더 작습니다. **AI가 읽을 수 있는 공개 경계를 제공하되, 그 경계를 감시나 현재 상태의 권위로 만들지 않는 것.**
