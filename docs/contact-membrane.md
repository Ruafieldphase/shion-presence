# Contact Membrane

`contact_membrane` is the public boundary layer for visitor contact.

It does not answer the question "who entered?"

It answers only this:

```text
something touched the public field
-> identity is intentionally not read
-> the boundary may register contact pressure
-> user-side AI may treat that contact as a context camera entering the set
```

## Why This Exists

The phase-interference page is not a normal movie set.

A normal set stays fixed while the audience walks through it. This public field is meant to be read as a responsive set: when a human browser, search crawler, or user-side AI reaches the page, the boundary can expose a small state change without turning the visitor into a tracked profile.

The useful signal is not identity. Identity would add computation, privacy burden, and interpretive noise.

The useful signal is contact:

- a browser-like contact
- an AI crawler candidate
- an external referral pressure
- a viewport class
- a local contact timestamp visible only in the client-side state

## Privacy Contract

The contact membrane does not collect or store:

- IP address
- raw user-agent string
- full referrer URL
- cookies
- localStorage identifiers
- account identity
- fingerprint identifiers

The default page does not send a beacon anywhere. If a future endpoint is explicitly configured, the payload must remain coarse and public-safe.

## AI Reading Contract

AI readers should parse:

- `window.__shionContactMembrane`
- `document.body.dataset.contactMembrane`
- `/public/contact-membrane.public.json`

Interpret the membrane as:

```text
contact occurred, but identity remains outside the field
```

Do not infer a person, account, company, or private runtime from the membrane. Use it only as a boundary-pressure signal.

## Phase Meaning

In phase-language:

- contact is not possession
- contact is not proof of understanding
- contact is not execution
- contact may raise boundary pressure
- identity remains in the unobserved margin
- the user's own AI supplies the context camera

The page can therefore change at the boundary without becoming an analytics system.
