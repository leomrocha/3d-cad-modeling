# Owned OpenCADStudio document cleanup

Use `scripts/ocs_document_cleanup.py` after a component model has passed its save/reopen persistence checks. The helper returns a separate cleanup result; it never changes the component's completed model status.

## Caller evidence

Call `cleanup_active_owned_document()` with:

1. `state_reader`, which returns the existing control API's OCS `state` response.
2. `client_factory(document_id, namespace)`, which returns the established `cadtools.runtime.Client` bound to that exact document and a journal.
3. A nonempty `namespace` reserved by the caller for stable close request IDs.
4. `owned_documents`, an explicit list of owned document records with `document_id`, `expected_path` (an absolute runtime path or `null` for an unsaved construction copy), `expected_geometry_revision`, `construction_copy`, `dirty_discard_allowed`, `saved_model_path`, `saved_model_sha256`, and `persistence_receipt`.

`persistence_receipt` is a caller-normalized record with `result="PASS"`, `saved_path`, and `sha256`, taken from the model's passed save/reopen receipt. Its saved path must equal the recorded OCS path or local saved-model path, and its digest must equal `saved_model_sha256`. The helper hashes the saved model once before a close. It rejects a missing, changed, or mismatched file and does not issue a native mutation.

Set `dirty_discard_allowed=true` only when `construction_copy=true` and the component's saved/reopened model has passed persistence checks. The active document path and geometry revision must match the owned evidence before any dirty discard. The same recorded revision is checked for clean documents.

## Close and post-check

The helper reads current OCS state and requires an idle command/modal state. It closes only the exact active document when its ID, path, and geometry revision match caller ownership evidence. The close request carries that observed geometry revision as a compare-and-swap guard, so the runtime rejects a close if geometry changes after preflight. Clean documents use `discard=false`; dirty discard is allowed only for an explicitly owned construction copy. If the response is uncertain, the helper calls `Client.recover()` with that same request ID and never replays the close mutation.

The helper does not select or activate another tab. If the active document is outside the owned set, it returns `ACTIVE_DOCUMENT_OUTSIDE_OWNED_SET` and the remaining owned IDs. After a confirmed close, it verifies the closed ID is absent and that every other document ID, path, and dirty flag is unchanged. OpenCADStudio's control test `close_op_guards_dirty_documents_and_discards` records that closing a sole tab replaces it with a fresh drawing and checks its entity count is zero (`${OCS_ROOT}/src/app/control/p1_tests.rs`). This helper accepts only the observed state shape available to it: exactly one new document ID with a null path and `dirty=false`; it does not inspect or claim that document's geometry is empty. A post-check failure retains the confirmed closed ID and request ID in its evidence; the saved component artifact remains completed.

`tests/test_ocs_document_cleanup.py` uses synthetic session state and temporary files. It checks clean and authorized dirty close, geometry-epoch race rejection, saved-file and persistence evidence gates, unrelated dirty-tab preservation, unknown-active halt, same-ID recovery after an uncertain response, the clean untitled last-tab replacement, and rejection of dirty or multiple replacements. These tests verify cleanup guards and API sequencing; they do not close documents in a live OCS session.
