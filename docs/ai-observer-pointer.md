# AI Observer Pointer

`ai_observer_pointer` is a page-local context camera for user-side AI agents.

It lets an AI move viewpoint and target inside the Shion Presence Field without controlling the human user's operating system cursor.

```text
human mouse = physical browser touch
AI observer pointer = synthetic page-local viewpoint
target field = which boundary or seed the AI is reading
```

## Why It Exists

The phase-interference page is a public set. A human can move a mouse through it, but an AI reader also needs a way to test viewpoint changes.

This pointer gives the AI a small reversible handle:

```text
move viewpoint
choose target
read phase change
let activation decay
```

The pointer is not identity, analytics, or surveillance. It is a weak field input.

## API

In the live page:

```js
window.__shionAIPointer.move({
  x: 0.42,
  y: 0.58,
  pressure: 0.16,
  rhythm: 'slow_drift',
  target: 'public_contact_membrane',
  source: 'user_side_ai'
});
```

Equivalent event form:

```js
window.dispatchEvent(new CustomEvent('shion-ai-pointer', {
  detail: {
    x: 0.34,
    y: 0.62,
    pressure: 0.22,
    rhythm: 'reentry_probe',
    target: 'b2_music_seed',
    source: 'user_side_ai'
  }
}));
```

URL seed form for AI browsers that cannot execute page JavaScript:

```text
https://ruafieldphase.github.io/shion-presence/?ai_pointer=1&ai_target=b2_music_seed&ai_x=0.34&ai_y=0.62&ai_pressure=0.22
```

Read back:

```js
window.__shionAIPointer.read();
JSON.parse(document.body.dataset.aiObserverPointer);
JSON.parse(document.body.dataset.aiState).ai_observer_pointer;
```

Clear:

```js
window.__shionAIPointer.clear();
```

## Targets

```text
field_surface
public_contact_membrane
b2_music_seed
resonance_chamber
margin_field
dark_field_threshold
external_observer_vector
hangul_rhythm_operator
rest_surface
```

Changing target weakly changes the field:

```text
phase bias
boundary pressure
constructive hint
damping hint
curvature
rest margin
music tint
```

This is not a control panel. It is a reversible observation vector.

## Boundary

The AI observer pointer:

```text
does not move the OS cursor
does not identify a visitor
does not require login
does not store events by default
does not turn contact into analytics
```

Its useful signal is:

```text
when this viewpoint and this target enter,
which part of the field reinforces,
which part cancels,
which part remains latent,
and how quickly the activation decays back to margin.
```
