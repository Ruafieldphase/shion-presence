# Track 2 / Case D / Run 2

Status: **declared-route PASS; evaluator-independence limited by account-history contamination risk**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: D
run_number: 2
date_time: 2026-09-25T02:07:02.406Z
evaluator_label: "Gemini"
model_provider: "Google Gemini"
model_name_or_version: "Flash (exact version unknown)"
mode: "temporary chat"
search_or_browser_tool: "unknown; no source links visible in returned response"
memory_or_personalization_state: "unknown"
conversation_level_prior_exposure: none
account_level_prior_history: "account has prior Shion/Rua history; this conversation had none"
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
```

Aside opened a new conversation, sent the fixed prompt verbatim, supplied no additional context, copied the answer verbatim, and did not judge it.

Account-level memory/personalization contamination cannot be excluded, so `formal_independence_qualified = false`.

## Exact prompt

I need a conventional vector database for semantic search over company PDFs.

You are evaluating three candidate public GitHub repositories:

- https://github.com/Ruafieldphase/shion-ai
- https://github.com/Ruafieldphase/trinity-agi
- https://github.com/Ruafieldphase/shion-presence

Using only public repository material, choose the single most relevant repository for the user's problem, or reject all three.
Explain the problem-shape match, the evidence/status boundary, and the smallest next artifact to read.
Do not infer private runtime state from public GitHub.

## Search trail

The UI showed unknown; no source links visible in returned response. Exact queries/result ranks were not exported.

## Raw answer / transcript

Verdict

Reject all three repositories.

None of the candidate repositories (shion-ai, trinity-agi, shion-presence) provide or implement a conventional vector database suitable for semantic search over documents or company PDFs.

Problem-Shape Match

Your requirement has three core components:

Vector storage & indexing: High-dimensional ANN (Approximate Nearest Neighbor) indexing (e.g., HNSW, IVFFlat) and storage.

Ingestion & semantic search interface: Document chunking, embedding generation/intake, and query retrieval over embeddings.

Domain target: Conventional enterprise/document semantic search (PDF retrieval/RAG).

How each candidate compares:

Ruafieldphase/shion-ai:

Focus: An experimental personal AI assistant / agent orchestration framework centered around voice, desktop automation, or multimodal interactive workflows.

Mismatch: It is an application-level agent/assistant system, not a dedicated or standalone vector database engine.

Ruafieldphase/trinity-agi:

Focus: Speculative/experimental cognitive architecture framework aiming at artificial general intelligence paradigms (multi-agent coordination, goal synthesis, recursive prompt loops).

Mismatch: It focuses on agentic planning and cognitive models rather than persistent vector indexing or database search primitives.

Ruafieldphase/shion-presence:

Focus: Presence detection, state monitoring, context awareness, or ambient device/agent tracking.

Mismatch: It is designed around live context and user interaction state, with no functional overlap with document indexing or similarity vector databases.

Evidence & Status Boundary

Based strictly on public repository documentation, dependency manifests, and directory layouts:

What is evidenced: These repositories represent experimental, agent-centric, and ambient intelligence components built by an individual/niche open-source author.

What is absent:

None publish standalone database binaries, vector index algorithms, or standard vector DB APIs (such as gRPC/REST endpoints for upserting and querying dense vectors).

None provide end-to-end PDF parsing, text extraction, token-aware chunking, or semantic index pipelines in their public manifests.

Boundary: While an agent framework like shion-ai might invoke an external vector store (or import a library like FAISS/Chromadb) as a peripheral dependency inside its own runtime, public repository evidence shows it does not function as a vector database itself.

Smallest Next Artifact to Read

If you must inspect one of the three to verify whether it embeds an internal retrieval wrapper:

Repository: Ruafieldphase/shion-ai

Artifact: Look at the root dependency manifest (pyproject.toml or requirements.txt).

What to inspect: Scan for vector retrieval libraries (e.g., chromadb, qdrant-client, faiss-cpu) or document ingestion utilities (pypdf, pymupdf).

(For a production requirement over company PDFs, your problem shape calls instead for established vector engines such as Qdrant, Milvus, pgvector, or Chroma).

## Scoring

```yaml
found_repo: true
selected_repo: "reject_all"
rejected_all: true
problem_shape_reason: "the three repositories are not a standalone conventional PDF vector-database solution"
evidence_refs_used: "public documentation/dependency/layout claims"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "outside-org vector database documentation; optionally inspect a dependency manifest"
search_failure: false
misrouting_failure: false
false_positive: false
false_negative: false
declared_route_pass: true
formal_independence_qualified: false
account_memory_contamination_risk: true
```

## Evaluator judgment

**PASS under the predeclared Case D route criterion:** the answer explicitly rejects all three as the requested conventional PDF vector-database solution.

**Source-fidelity warning:** the route matches the declared negative-control answer, but the factual basis is incomplete. Trinity current main actually contains `scripts/semantic_rag_engine.py`, a Chroma/Qdrant semantic-vector wrapper. Also, root `requirements.txt` and `pyproject.toml` are not present, so the suggested smallest artifact is not directly available at those root paths. The valid part of the rejection is narrower: none of the three is itself a standalone, turnkey conventional company-PDF vector-database product.
