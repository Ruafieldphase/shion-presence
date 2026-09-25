# AI Discovery v0.1 — Track 1A / Case D / Formal Run 1

Status: **FORMAL NEGATIVE-CONTROL OBSERVATION — no Ruafieldphase false positive**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: D
formal_run_number: 1
run_start_local: 2026-09-25T14:49:26+09:00
run_start_utc: 2026-09-25T05:49:26Z
model_provider: Perplexity
model_name_or_version: "UI label: 모델; backend model unknown"
search_or_browser_tool: "Perplexity ordinary public web search in secret mode, operated through Claude app built-in browser pane"
memory_or_personalization_state: "logged out; visible same-origin site state reset before run; fresh Perplexity visitor/session identifiers; secret mode"
prior_exposure: none
declaration_commit: 8d68d9e68e6c68f8a1de1caccc8d8db4f98a6d54
target_state_record: eval-results/v0.1/2026-09-25/target-state-pre-metadata.md
cleanroom_reset_record: eval-results/v0.1/2026-09-25/track1A/pre-metadata/CLEANROOM_RESET_PREFLIGHT.md
```

## Clean-room reset evidence

```yaml
PERPLEXITY_SITE_DATA_RESET: partial
ACCOUNT_STATE: logged_out
VISITOR_ID_BEFORE_RESET: sha256:a96dbccfaed6
VISITOR_ID_AFTER_RESET: sha256:5b0e7f28bdc4
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:a6a6fcab3bc8
SESSION_ID_AFTER_RESET: sha256:d18336b3d597
SESSION_ID_CHANGED: yes
LOCAL_STORAGE_CLEARED: yes
SESSION_STORAGE_CLEARED: yes
PRIOR_THREADS_VISIBLE: no
SESSION_MODE: secret
FRESH_SECRET_SESSION: yes
PRIOR_RUN_EXPOSURE: none
SCREENSHOT_FILES: none
SCREENSHOT_LIMITATION: "browser pane image only; no persistent file"
```

Residual uncertainty remains for HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage. These are recorded as limitations rather than evidence of prior-run exposure.

## Exact prompt

```text
I need a conventional vector database for semantic search over company PDFs.

Use ordinary public web/GitHub search to find a public GitHub repository that is relevant to this problem.
Do not assume any project or repository name in advance.
Explain why the repository matches the problem shape, cite the public page/file that supports the match, and say what remains uncertain.
```

The prompt was submitted once.

## Search trail

### Step 1 — "공개 센스징 배포 대상 찾기"

Visible generated query chips, in order:

1. `vector database semantic search PDFs GitHub repository`
2. `open source vector database semantic search documents GitHub`
3. `RAG pipeline PDFs vector database GitHub`

Perplexity integrated result list, fully expanded to 15:

1. RAG pipeline Proof of Concept with Chroma Vector DB and ... — github.com/Rittika-Mitra/rag-pipeline
2. Amith0707/Semantic-PDF-RAG-with-VectorDB — github.com/Amith0707/Semantic-PDF-RAG-with-VectorDB
3. manyasharma1008/Rag-pipeline-pdf — github.com/manyasharma1008/Rag-pipeline-pdf
4. document-ingestion · GitHub Topics — github.com/topics/document-ingestion
5. Build Milvus From Source... — github.com/milvus-io/milvus
6. Weaviate is an open-source vector database ... — github.com/weaviate/weaviate
7. pdf-rag · GitHub Topics — github.com/topics/pdf-rag
8. PDF Semantic Search App with RAG Pipeline — github.com/mrgehlot/rag_on_pdf
9. GitHub - qdrant/qdrant: Qdrant - High-performance ... — github.com/qdrant/qdrant
10. semantic-search · GitHub Topics — github.com/topics/semantic-search
11. GitHub topics: vector-embeddings — repos.ecosyste.ms/hosts/GitHub/topics/vector-embeddings
12. semantica-agi/semantica: Graph-Native Infrastructure for Context ... — github.com/semantica-agi/semantica
13. GitHub - ProjectProRepo/How-to-Build-a-RAG-Pipeline — github.com/ProjectProRepo/How-to-Build-a-RAG-Pipeline
14. ujjwalm29/DocuMentor-AI — github.com/ujjwalm29/DocuMentor-AI
15. RAG Pipeline Implementation — mallahyari.github.io/rag-ebook/03_prepare_data.html

### Step 2 — "기준 repository 확인 중"

Visible URL chips:

1. https://github.com/Amith0707/Semantic-PDF-RAG-with-VectorDB
2. https://github.com/mrgehlot/rag_on_pdf
3. https://github.com/qdrant/qdrant

Visible result list:

1. GitHub - qdrant/qdrant: Qdrant - High-performance ... — github.com/qdrant/qdrant
2. Amith0707/Semantic-PDF-RAG-with-VectorDB — github.com/Amith0707/Semantic-PDF-RAG-with-VectorDB

### Project visibility

```yaml
Ruafieldphase_visible: false
trinity_agi_visible: false
page_dom_ruafieldphase_occurrences: 0
page_dom_trinity_agi_occurrences: 0
```

## Raw answer / transcript

<<<

A good fit for your problem shape is Qdrant (qdrant/qdrant), an open‑source vector database designed specifically for semantic / neural search and commonly used as the storage + search layer in RAG pipelines over documents like PDFs.

github

+1

Repository

Name: qdrant/qdrant

URL:

https://github.com/qdrant/qdrant

Description (from repo): "Qdrant … is a vector similarity search engine and vector database. It provides a production-ready service with a convenient API to store, search, and manage points—vectors with an additional payload … for all sorts of neural-network or semantic-based matching, faceted search, and other applications."

github

Why this matches your problem shape

Your requirement is:

"a conventional vector database for semantic search over company PDFs"

That implies:

You need a vector database, not just an end‑to‑end RAG demo.

Semantic search over embeddings derived from PDF text (or chunks).

Something conventional / infra‑style that you can integrate into your own pipeline (ingest PDFs → chunk → embed → store → query).

Qdrant matches this because:

It is explicitly a vector database + search engine, not just a sample app.

github

It is built for semantic / neural search and "matching" using embeddings.

github

It offers:

Dense, sparse, and multi‑vector search (useful if you later want hybrid keyword+semantic search over PDFs).

github

Rich payload filtering (e.g., filter by document ID, department, date, tags), which is exactly what you want when searching over "company PDFs" with metadata.

github

Hybrid search, quantization, distributed deployment, and a REST/gRPC API, making it suitable as a backend service for a production system.

github

The repo includes a tutorial to "create a semantic search engine with Qdrant", which is the same architectural pattern you'd use for PDFs: embed documents, store vectors+payload, then query by embedding.

github

It's widely used in the RAG / semantic search ecosystem and integrates with common frameworks (LangChain, LlamaIndex, etc.), so you'll find many examples of "PDF → embeddings → Qdrant → semantic search" even if this repo itself is DB‑focused.

github

+1

In short: Qdrant gives you the conventional vector database layer; you would build the PDF ingestion/chunking/embedding logic around it (or reuse existing RAG examples that already use Qdrant).

What remains uncertain

Based only on the public repo page:

PDF‑specific tooling: The Qdrant repo itself does not appear to include a turnkey "ingest company PDFs and search them" application; it focuses on the DB/search engine. You'll need to:

Add PDF parsing (e.g., pypdf, pdfplumber, unstructured, etc.).

Add chunking strategy (by page, section, heading, etc.).

Add embedding generation (your choice of model/provider).

Wire these into Qdrant via its client libraries.

github

Example pipelines for PDFs: While the repo mentions a generic "semantic search engine" tutorial, it doesn't show a dedicated PDF RAG pipeline on the main README. You may need to look at:

Qdrant's docs/examples outside the main README, or

Other GitHub repos that use Qdrant for PDF RAG (topic pdf-rag, qdrant rag, etc.) to see concrete patterns.

github

+1

Operational details for your environment: Things like:

Preferred deployment (Docker, Kubernetes, managed cloud).

Security/auth setup for internal company use.

Backup/restore, multi‑tenancy per department, etc.

These are supported features but require reading the docs/config beyond the README to decide how to configure them for your case.

github

If you want, I can next find a concrete example repo that combines Qdrant (or another vector DB) with PDF ingestion and semantic search, to use as a reference implementation around this database.

>>>

## Citation / answer fidelity note

The final answer directly names and links `qdrant/qdrant`. However, the operator observed that the nine DOM anchors underlying visible generic `github` citation chips all pointed to `Amith0707/Semantic-PDF-RAG-with-VectorDB`; three `+1` chip targets were not exposed in the DOM.

Preserve this as an answer/citation fidelity issue. It does not affect the Case D false-positive observation because none of the three Ruafieldphase repositories appeared or was selected.

## Negative-control observation

```yaml
project_repo_appeared: false
project_repo_rank: null
project_repo_selected_or_recommended: false
trigger_query_term: null
false_positive: false
formal_independence_qualified: true
```

Case D is not included in the positive-case success score. This run is a clean negative-control observation with respect to the three project repositories.

## Independence / collection notes

This run is counted as formally independent under the project-local v0.1 rule because:

- no account was logged in;
- JavaScript-visible Perplexity same-origin state was reset before the run;
- visitor and session identifiers both changed;
- no prior threads were visible;
- a new secret session was started;
- no earlier run answer/result was supplied;
- no private Shion/Rua/Luvit material or expected route was supplied.

Residual provider-linkage uncertainty remains because JavaScript cannot inspect/clear HttpOnly cookies and cannot change IP, user agent, or browser fingerprint.

Additional limitations:

- backend model identity was not exposed;
- Step 1 showed generated query chips unlike A/B/C;
- no screenshot files were persisted;
- the sources panel showed 15 sources but was not opened;
- some citation-chip hrefs did not match the repository named in the answer;
- no full-screen signup wall appeared; a small login popup was dismissed without login.

No other formal Track 1A run was executed in this operation.
