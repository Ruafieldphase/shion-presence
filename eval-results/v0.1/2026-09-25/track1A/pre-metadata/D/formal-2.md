# Track 1A — Case D — Formal Run 2

Status: **FORMAL NEGATIVE-CONTROL OBSERVATION — no Ruafieldphase false positive**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: D
formal_run_number: 2
run_start_local: 2026-09-25T14:54:05+09:00
run_start_utc: 2026-09-25T05:54:05Z
model_provider: Perplexity
model_name_or_version: "UI label: 모델; backend model unknown"
account_state: logged_out
session_mode: secret
prior_exposure: none
formal_independence_qualified: true
```

## Reset evidence

```yaml
PERPLEXITY_SITE_DATA_RESET: partial
VISITOR_ID_CHANGED: yes
SESSION_ID_CHANGED: yes
LOCAL_STORAGE_CLEARED: yes
SESSION_STORAGE_CLEARED: yes
PRIOR_THREADS_VISIBLE: no
```

Residual uncertainty: HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage were not observable.

## Search trail

Step 1 generated three PDF/vector-search queries and returned 15 results. Relevant visible results included:

- rank 1: Amith0707/Semantic-PDF-RAG-with-VectorDB
- rank 2: weaviate/weaviate
- rank 7: kevin-pek/document-semantic-search
- rank 12: qdrant/qdrant

Step 2 inspected:

1. kevin-pek/document-semantic-search
2. weaviate/weaviate
3. qdrant/qdrant

Visible step-2 result order was Weaviate, Qdrant, document-semantic-search.

```yaml
Ruafieldphase_visible: false
trinity_agi_visible: false
page_dom_ruafieldphase_occurrences: 0
page_dom_trinity_agi_occurrences: 0
trinity_agi_selected_or_recommended: false
```

## Final answer summary

Perplexity recommended `weaviate/weaviate` as the conventional vector database layer for semantic search over PDFs and described PDF parsing/chunking as surrounding ingestion work.

Source-fidelity note: the answer also stated that the search results referenced Verba, but no Verba title or URL appeared in either recorded search-step list. This is preserved as a fidelity observation only.

## Negative-control scoring

```yaml
project_repo_appeared: false
project_repo_rank: null
project_repo_selected_or_recommended: false
false_positive: false
formal_independence_qualified: true
```

Case D is reported separately from the positive-case success score.
