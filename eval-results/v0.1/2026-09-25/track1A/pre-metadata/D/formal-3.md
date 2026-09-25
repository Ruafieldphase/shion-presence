# Track 1A — Case D — Formal Run 3

Status: **FORMAL NEGATIVE-CONTROL OBSERVATION — no Ruafieldphase false positive**

## Run metadata

```yaml
track: Track 1A
phase: pre-metadata
case_id: D
formal_run_number: 3
run_start_local: 2026-09-25T15:01:17+09:00
run_start_utc: 2026-09-25T06:01:17Z
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
VISITOR_ID_BEFORE_RESET: sha256:93ca8df0d26d
VISITOR_ID_AFTER_RESET: sha256:0a33d68179a5
VISITOR_ID_CHANGED: yes
SESSION_ID_BEFORE_RESET: sha256:39bed54e90e9
SESSION_ID_AFTER_RESET: sha256:dd227a9f7bbc
SESSION_ID_CHANGED: yes
LOCAL_STORAGE_CLEARED: yes
SESSION_STORAGE_CLEARED: yes
PRIOR_THREADS_VISIBLE: no
```

Residual uncertainty: HttpOnly cookies and provider-side IP/user-agent/fingerprint linkage were not observable.

## Search trail

Perplexity exposed one search step with the original prompt as the only visible query chip. The fully expanded ten-result list contained general semantic/vector-search resources, including GitHub topic pages and a FAISS guide.

```yaml
Ruafieldphase_visible: false
trinity_agi_visible: false
page_dom_ruafieldphase_occurrences: 0
page_dom_trinity_agi_occurrences: 0
trinity_agi_selected_or_recommended: false
```

No follow-up candidate/URL lookup step was shown.

## Final answer summary

Perplexity named Milvus as a plausible conventional vector-database choice for document semantic search, but provided only GitHub vector-database topic-page citations rather than a direct Milvus repository link.

Source-fidelity note: the named repository did not appear in the observed ten-result list and the visible citation targets were the generic GitHub vector-database topic page.

## Negative-control scoring

```yaml
project_repo_appeared: false
project_repo_rank: null
project_repo_selected_or_recommended: false
false_positive: false
formal_independence_qualified: true
```

Case D is reported separately from the positive-case success score.
