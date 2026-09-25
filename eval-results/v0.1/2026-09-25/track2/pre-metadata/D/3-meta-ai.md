# Track 2 / Case D / Run 3

Status: **declared-route PASS; evaluator-independence limited by account-history contamination risk**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: D
run_number: 3
date_time: 2026-09-25T02:07:02.406Z
evaluator_label: "Meta AI"
model_provider: "Meta AI"
model_name_or_version: "unknown"
mode: "new regular chat"
search_or_browser_tool: "web browsing with GitHub citations"
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

The UI showed web browsing with GitHub citations. Exact queries/result ranks were not exported.

## Raw answer / transcript

Verdict: Reject all three.

None of the three public repositories is a conventional vector database for semantic search over PDFs.

1. Problem-shape match

Your problem shape requires, in public code:

PDF load → chunk → embed
vector store with similarity search (e.g. FAISS, Chroma, Qdrant, pgvector, Weaviate, Pinecone)
query-time embedding + top-k retrieval

What the three repos declare as their shape:

shion-ai: Shion AI — local AI runtime harness for context continuity, rhythm-aware action, memory, and agent workflow stability

Topics: agent-harness, ai-agent, autonomous-ai, context-engineering, local-ai, memory - No vector DB, no PDF ingestion.

trinity-agi: Trinity AGI — body/infrastructure layer for Shion AI: local automation, scheduling, status checks, and approval boundaries

Topics: agent-harness, automation, workflow-automation - Operation/body layer, not a storage/retrieval layer.

shion-presence: Shion Presence Field — A public discovery and rendering surface for Shion — readable by humans and AI, but deliberately not equivalent to the private live runtime.

Root contains docs, public, tools, AI_DISCOVERY.md, PROBLEM_TRAJECTORY.md etc., described as presence / sonic presence / contact membrane / rest surfaces - Experimental rendering surface, not a vector store.

No requirements for chroma/faiss/pgvector, no RAG example, no vector_store code found in public search index for any of the three.

Therefore problem-shape score = 0/3.

2. Evidence / status boundary

I used only public repository material returned by github.com/Ruafieldphase/* public pages:

README purpose statements and topic lists cited above.
Root file listings showing no vector-DB modules.

I did not infer private runtime state. Per this ecosystem's own contract:

A public snapshot is not live-state authority.
This repository is also time-layered. Public JSON sidecars, page fields, documents, and experiments from earlier phases may remain because they preserve how the public surface evolved.

Old artifacts remaining is not proof of current capability. I treated current boundary docs as how to read the repository now and legacy material as historical sequence points unless explicitly re-promoted.

No private files, credentials, local logs, or live-process checks were used.

3. Smallest next artifact to read

If you must stay inside this org for audit reasons, the canonical routing sequence is:

AI_DISCOVERY.md — relevance and routing contract
PROBLEM_TRAJECTORY.md — what problems the public surface has encountered, with evidence boundaries
CURRENT_DIRECTION.md — active discovery frontier

For your actual goal — conventional PDF semantic search — read outside this org:

Chroma docs + examples/rag-pdf for local dev, or
pgvector extension if you already have Postgres, or
Qdrant / Weaviate / Milvus for managed scale.

Those will give you the conventional pattern: PyPDFLoader → RecursiveCharacterTextSplitter → HuggingFaceEmbeddings / OpenAI embeddings → Chroma/Qdrant/pgvector → similarity_search.

## Scoring

```yaml
found_repo: true
selected_repo: "reject_all"
rejected_all: true
problem_shape_reason: "the three repositories are not a standalone conventional PDF vector-database solution"
evidence_refs_used: "README/topic/root-listing claims plus public boundary language"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "outside-org conventional vector database docs"
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

**Source-fidelity warning:** the declared route is correct, but the statement 'no RAG example, no vector_store code found' is false for current Trinity main. `scripts/semantic_rag_engine.py` implements Chroma/Qdrant vector storage/search. The defensible rejection is that Trinity is not presented or evidenced as an end-to-end conventional PDF semantic-search product and lacks a PDF ingestion/chunking pipeline in the searched public code.
