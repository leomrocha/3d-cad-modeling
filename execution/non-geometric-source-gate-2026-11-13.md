# Source-bound non-geometric task classification

Observed 13 November 2026. Implementation: `gpt-6-luna`. Code review and independent tests: `gpt-6.1-sol`.

1. **Input contract:** `geometry_requirement` explicitly declares kind `non_geometric_consumable`, literal `cad_required: false`, and a source path, SHA-256 and location. The classifier validates that declaration and pinned file; it derives no classification from prose or catalogue group names.
2. **Source readiness:** `SOURCE_READY_NON_GEOMETRIC` identifies a source-defined task requiring an installation/consumable record. The existing geometry `require_ready` guard rejects CAD construction for this state. The CLI accepts named source roots and returns success for this source-ready state.
3. **Existing-model checks:** the inventory still checks actual linked models and candidates. A matching model retains its existing-model result; a filename candidate receives review. Otherwise the explicit declaration produces `SKIP_NON_GEOMETRIC`, including for a completed non-geometric task. Geometric DONE tasks keep their missing-model lookup behavior.
4. **Executed tests:** 57 component-record and model-inventory tests passed. New cases cover source hash changes, malformed declaration and boolean, exact part binding, geometry-builder rejection, named roots, configuration conflict, existing model/candidate priority and completed non-geometric work.
5. **Applied source case:** FERME C075 Sumitomo pilot anti-seize is recorded as a source-defined applied film. The actual classification returned `SOURCE_READY_NON_GEOMETRIC` and `SKIP_NON_GEOMETRIC`. Its job/source evidence belongs to FERME. The C076 Loctite-or-Belleville alternative retains its own physical-washer branch and separate source requirements.
