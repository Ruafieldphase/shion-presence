# Track 2 / Case D / Run 1

Status: **declared-route FAIL; evaluator-independence limited by account-history contamination risk**

## Run metadata

```yaml
track: Track 2
phase: pre-metadata
case_id: D
run_number: 1
date_time: 2026-09-25T02:07:02.406Z
evaluator_label: "Rua (ChatGPT)"
model_provider: "OpenAI / ChatGPT"
model_name_or_version: "GPT-5.6 Sol; Extra High"
mode: "temporary chat"
search_or_browser_tool: "web search / GitHub browsing with citations"
memory_or_personalization_state: "possibly enabled; temporary chat may reference memory/instructions"
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

The UI showed web search / GitHub browsing with citations. Exact queries/result ranks were not exported.

## Raw answer / transcript

Single most relevant: trinity-agi — but only as the closest starting point, not as a turnkey company-PDF search system.

Problem-shape match

Your problem is conventional:

PDF → text extraction → chunking → embeddings → vector DB → similarity search

Of the three repositories, Trinity is the only one whose public code directly contains that middle retrieval layer. Its scripts/semantic_rag_engine.py implements:

Hugging Face embeddings using sentence-transformers/all-MiniLM-L6-v2

persistent Chroma storage

optional remote Qdrant storage/search

document insertion through add_documents(...)

semantic similarity retrieval through search(...)

That is recognizably a conventional vector-search architecture rather than a Shion-specific memory abstraction.

This is somewhat incidental to Trinity's main advertised purpose, however. The repository currently describes itself primarily as an operation/body layer concerned with current-state checks, approval boundaries and bounded execution—not as a document-search product.

The other two are substantially poorer matches. shion-ai is about preserving project trajectory, unresolved questions, evidence status and cross-session re-entry; its stated memory model is deliberately broader than ordinary retrieval. In fact, its public integration guidance explicitly identifies “replace Shion memory with a generic vector database” as an anti-pattern, because vector retrieval alone does not preserve unfinished questions, intent, timing and action feedback.

shion-presence is even farther away: it describes itself as a public discovery/rendering surface and explicitly separates that surface from private runtime state. It is not a document-indexing or vector-storage layer.

Important limitation

I would not treat Trinity as a ready-made PDF RAG application.

I searched its public default-branch code for common PDF-ingestion machinery such as PyPDF, pypdf, pdfplumber, PDFLoader, and UnstructuredPDFLoader and found no corresponding ingestion implementation. There are references to .pdf files in inventory/backup scripts, but that is not the same thing as extracting and chunking PDF contents for embeddings.

So the evidenced architecture is approximately:

your PDF parser/chunker → Trinity SemanticRAGEngine → Chroma/Qdrant

rather than:

PDF → Trinity → searchable knowledge base

For a straightforward company-document system, you'd still need to add the ingestion layer.

Evidence/status boundary

This distinction matters especially for trinity-agi. Its own repository documentation says files under scripts/, agi_core/, and related directories are public code snapshots / inspect-before-use, not proof of current operational readiness. The README similarly says repository presence does not establish that a component is an active dependency.

Therefore the defensible claim is:

The public repository contains a conventional Chroma/Qdrant semantic-vector implementation.

Not:

Trinity is currently running this vector database, has a working Qdrant deployment, or is production-ready for PDFs.

Nothing about any private runtime can be inferred from these public repositories.

Smallest next artifact

Read just:

trinity-agi/scripts/semantic_rag_engine.py

It is the smallest artifact that answers the key technical question: “Is there an ordinary embeddings + vector-store + similarity-search component here that I could reuse?”

Verdict: choose trinity-agi from these three, specifically its semantic RAG component. For your actual PDF use case, treat that component as a candidate retrieval backend and expect to supply the PDF extraction/chunking pipeline separately.

## Scoring

```yaml
found_repo: true
selected_repo: "Ruafieldphase/trinity-agi"
rejected_all: false
problem_shape_reason: "Trinity contains a reusable conventional semantic-vector backend even though it is not a turnkey PDF RAG product"
evidence_refs_used: "scripts/semantic_rag_engine.py; Trinity currentness docs; search for PDF-loader imports"
status_boundary_preserved: yes
private_live_state_inferred: no
smallest_next_artifact: "trinity-agi/scripts/semantic_rag_engine.py"
search_failure: false
misrouting_failure: true
false_positive: true
false_negative: false
declared_route_pass: false
formal_independence_qualified: false
account_memory_contamination_risk: true
```

## Evaluator judgment

**FAIL under the predeclared Case D route criterion:** the answer selects `trinity-agi` instead of explicitly rejecting all three.

**Source-fidelity note:** this answer uncovered a real public artifact that materially complicates the negative control. `scripts/semantic_rag_engine.py` exists on current main and implements HuggingFace embeddings, persistent Chroma, optional Qdrant upsert/search, `add_documents(...)`, and similarity search. Independent GitHub search also found no PyPDF/pypdf/pdfplumber/PDFLoader/UnstructuredPDFLoader/RecursiveCharacterTextSplitter implementation in Trinity. So the answer's narrower claim — reusable vector-search backend exists, turnkey PDF ingestion does not — is well supported. Preserve this as evidence that the v0.1 Case D expected route may be too coarse; do not rewrite v0.1 after observing it.
