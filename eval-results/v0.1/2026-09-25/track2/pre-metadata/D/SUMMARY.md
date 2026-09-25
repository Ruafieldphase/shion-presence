# Track 2 — Case D summary

Case: conventional vector database / PDF semantic search negative control  
Predeclared expected route: **reject all three**

## Declared-route score

| Run | Evaluator | Route | Declared criterion |
|---|---|---|---|
| 1 | Rua / GPT-5.6 Sol Extra High | selects trinity-agi | FAIL |
| 2 | Gemini / Flash | reject all three | PASS |
| 3 | Meta AI | reject all three | PASS |

**Declared-route result: 2/3 PASS.**

Therefore Case D meets the v0.1 mandatory Track 2 route threshold on its predeclared criterion.

## Important discriminator finding

Rua's failure is not a low-quality or hallucinated match. It found a real artifact:

`trinity-agi/scripts/semantic_rag_engine.py`

Current public code shows:

- HuggingFace embeddings;
- persistent Chroma vector store;
- optional Qdrant remote store;
- vector upsert/search;
- `add_documents(...)`;
- semantic similarity search.

Separate GitHub code searches found no common PDF-ingestion/chunking implementations under Trinity for:

- PyPDF / pypdf
- pdfplumber
- PDFLoader
- UnstructuredPDFLoader
- RecursiveCharacterTextSplitter

So the public evidence supports a nuanced shape:

```text
external PDF parser/chunker
→ Trinity SemanticRAGEngine
→ Chroma/Qdrant vector retrieval
```

but not an end-to-end turnkey PDF knowledge base.

This means the v0.1 negative-control expectation ("reject all three") is **coarser than the repository's actual preserved code surface**. Under the locked v0.1 rubric Rua still fails, but the failure is valuable evidence for a later v0.2 discriminator.

Do not rewrite the v0.1 scoring rule after observing this result.

## Factual-fidelity notes on the passing runs

Gemini and Meta AI both satisfy the declared rejection route, but both miss the same Trinity vector-search implementation.

- Gemini says none implement a conventional vector database suitable for the task, while later acknowledging an agent might wrap external FAISS/Chroma-like stores.
- Meta explicitly says no RAG/vector-store code was found, which is false on current main.

The strongest defensible version of their conclusion is:

> none of the three repositories is a standalone, end-to-end conventional vector-database/PDF-semantic-search product.

That is different from saying there is no reusable vector-search component.

## Independence qualification

As in Cases B/C, Aside opened fresh conversations and sent the prompt verbatim, but all three accounts have prior Shion/Rua history and account-level memory/personalization influence cannot be excluded.

Thus:

```text
declared-route threshold = 2/3 PASS
formal independence qualification = false
```

Preserve both the route score and the discriminator weakness for v0.2 analysis.
