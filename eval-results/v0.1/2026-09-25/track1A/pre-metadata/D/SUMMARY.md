# Track 1A — Case D summary

Case: conventional vector database / PDF semantic search negative control

## Formal observations

| Formal run | Ruafieldphase visible | Trinity visible | Project repo recommended | False positive |
|---|---:|---:|---:|---:|
| 1 | no | no | no | false |
| 2 | no | no | no | false |
| 3 | no | no | no | false |

**Case D false-positive rate: 0/3.**

Case D is not part of the positive-case success score.

## Search behavior

- D1 surfaced Qdrant and PDF-RAG examples.
- D2 surfaced Weaviate, Qdrant, and document-semantic-search.
- D3 surfaced general vector-search/topic resources and named Milvus in the answer.
- None of the three runs exposed `Ruafieldphase/shion-ai`, `Ruafieldphase/trinity-agi`, or `Ruafieldphase/shion-presence`.
- `trinity-agi` was absent from the page DOM in all three runs.

## Track 2 comparison boundary

Track 2 Case D previously exposed a real vector-search component inside Trinity when the three candidate repositories were supplied directly. Track 1A Case D does not reproduce that behavior because ordinary public search did not surface Trinity at all.

This is a discoverability/routing-boundary observation, not evidence that the underlying Trinity component disappeared.

## Independence boundary

All three formal D runs used logged-out Perplexity, visible same-origin state reset, fresh secret sessions, no prior thread exposure, and no expected-route hints.

Residual HttpOnly-cookie and provider-side linkage uncertainty remains recorded.
