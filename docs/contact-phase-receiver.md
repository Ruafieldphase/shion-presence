# Contact Phase Receiver

The contact phase receiver is the local ear for the phase-interference page.

It answers this:

```text
what touched the boundary, and what changed?
```

It does not answer this:

```text
who entered?
```

## Why This Exists

The public page can expose a contract, but GitHub Pages cannot give the local system a live event stream. A crawler may read HTML, Markdown, or JSON without executing browser JavaScript. A human browser may execute JavaScript but still should not be tracked as an identity.

So the receiver records only coarse field deltas:

- a public file was requested
- the rendered page sent a coarse contact beacon
- a music input was posted as a wave event
- a prompt input was posted as a context-camera event

## Local Receiver

Run:

```powershell
python tools\phase_contact_receiver.py --host 127.0.0.1 --port 58231
```

Then open:

```text
http://127.0.0.1:58231/
```

The receiver writes:

```text
C:\workspace\agi\outputs\sena\contact_phase_receiver_events.jsonl
C:\workspace\agi\outputs\sena\contact_phase_receiver_latest.json
```

It also exposes:

```text
http://127.0.0.1:58231/phase-contact/latest
```

## Public Receiver

The public page can also send coarse contact beacons to a Cloudflare Worker:

```text
https://twilight-union-3b86shion-phase-contact.kuirvana.workers.dev/phase-contact
```

The public readback endpoint is:

```text
https://twilight-union-3b86shion-phase-contact.kuirvana.workers.dev/phase-contact/latest
```

This public receiver uses the `PHASE_EVENTS` binding attached to the
`shion-phase-events` KV namespace. It keeps the same boundary rule as the local
receiver: receive field deltas, not identity.

## Event Model

Each event is a boundary particle:

```text
event_kind
contact_source
contact_class
path
referrer_class
viewport_class
boundary_pressure
phase_effect
field_delta
```

`contact_class` is coarse:

- `browser_contact_candidate`
- `ai_crawler_candidate`
- `unknown_contact`

`phase_effect` is coarse:

- `soft_contact`
- `boundary_damping`
- `reinforcement_pressure`
- `music_wave_delta`

## Privacy Boundary

The receiver intentionally does not store:

- IP address
- raw user-agent string
- full referrer URL
- cookies
- localStorage identifiers
- fingerprint identifiers

The useful signal is not identity. The useful signal is boundary change.

## Music And Prompt Inputs

Music, prompts, bots, and people can all be read as incoming scalar fields.

The receiver can accept explicit POSTs:

```text
POST /phase-contact
POST /phase-event
POST /phase-music
```

For public posts, use:

```text
POST https://twilight-union-3b86shion-phase-contact.kuirvana.workers.dev/phase-contact
POST https://twilight-union-3b86shion-phase-contact.kuirvana.workers.dev/phase-event
POST https://twilight-union-3b86shion-phase-contact.kuirvana.workers.dev/phase-music
```

For the current music field, the important public seed is:

```text
B2 / open_reentry_body_anchor
```

When this seed appears in `field_delta.music_phase_seed`, AI readers should compare it with recent contact events instead of interpreting it as a universal emotion score.
