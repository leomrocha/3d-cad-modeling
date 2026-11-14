# Check existing 3D files before starting a component

1. Run this check before every component start. It reads the external input manifest, work index, model paths, input-sheet links and files. It runs no CAD operations. Existing model paths, recorded scope and checks supply reuse evidence.

```sh
python3 ${SKILL_ROOT}/scripts/model_inventory.py \
  --index ${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json \
  --work-index ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/component-work.json \
  --cad-root ${FERME_ROOT}/engineering/module-development/cad \
  --project-root ${FERME_ROOT} \
  --root FERME_ROOT="${FERME_ROOT}" \
  --id C001
```

2. **SKIP_EXISTING_MODEL:** a matching nonempty 3D file is present through an attributed manifest, work or sheet link. Mark the current build-list entry DONE, retain its actual path and use its existing checks. Move to a component requiring a new model. `model`, `output` and `native_model` are all observed work-record path fields.
3. **LOCATE_COMPLETED_MODEL:** the work record says DONE and the attributed path was not found. Locate its completed artifact using the available file inventory and existing records. Preserve completed status during that search.
4. **REVIEW_EXISTING_CANDIDATES:** the filesystem contains a model matching a component code without an attributed link. Review its actual identity and representation against the input sheet. Record a confirmed match and reuse it; identify a different-component reference explicitly. Direct dependency models remain separately listed. A component-specific reviewed-candidate record can dismiss one exact filename-derived candidate after the review is documented as described below.
5. **NEW_MODEL_REQUIRED:** the completed-file lookup found no attributed model or unresolved filename candidate for this component. A valid exact reviewed-candidate decision removes only that reviewed file from the unresolved candidate set. Continue its existing source-readiness and construction procedure. Keep the filesystem result beside that particular start so it establishes which files were checked.
6. `2d_schemas` files are recorded as 2D references. Byte-identical retained copies keep that role through SHA-256 association with the original; the inventory records their role basis and source paths. A distinct model's different bytes retain its existing classification. The current FERME list contains these interface references for the Blickle casters and SPP trailer coupling.
7. The initial reconciliation found existing 3D models for the ME0907 motor, both Sumitomo PRO gearmotors, BMW/Leaf/Victron batteries, SKF bearing, Sumitomo driver, Lynx BMS, Fibox enclosure, Victron 24/12 converter and both frame members. Their geometry and prior checks are reused. Reconciliation record (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/audit.json`).
8. Stored `${ROOT_NAME}` locators require an explicit `--root ROOT_NAME=ABSOLUTE_PATH` for every referenced root. Python callers pass `root_map` to `audit` or `start_check`. An unresolved root raises an error before a new-model decision. Relative manifest and job model paths use `cad_root`; relative input-sheet links use the sheet directory. Absolute runtime paths remain supported. The returned inventory contains runtime paths; normalize them to named-root locators before storing the result.
9. The file inventory includes `.igs` and `.iges` source models. An attributed matching IGES file takes the reuse route; an unattributed filename match requires component-identity review. Source/native representation and actual topology are recorded during import: the extension alone does not distinguish a surface model from a solid model.
10. For a component with separately modeled configurations, pass both `--id PART_ID` and `--configuration EXACT_NAME`. The corresponding work record declares a `configurations` list; each entry has a unique exact `name` and may carry its own `model`, `output`, `native_model`, and `state`. Only that configuration's attributed model paths can produce `SKIP_EXISTING_MODEL`. An existing model attributed to another declared configuration is returned under `other_configuration_models` and does not suppress the selected configuration. The selected entry's `state: DONE` with no existing attributed file produces `LOCATE_COMPLETED_MODEL`; a pending selected entry can return `NEW_MODEL_REQUIRED` even when the component-level record says `DONE`.
11. When the selected configuration has an attributed existing model, reuse it with `SKIP_EXISTING_MODEL`; other candidates stay reported. When its attributed model is absent, any unscoped model link or unscoped matching filename candidate produces `REVIEW_EXISTING_CANDIDATES` before new construction. The selector never ignores an existing candidate merely because it lacks a configuration label. Linked 2D drawings remain in `references_2d`; they do not satisfy a 3D model path. Configuration checks require a nonempty declarations list, unique nonempty exact names, and a name matching the requested selector. The CLI requires `--id` when `--configuration` is supplied; other parts in the same audit use the ordinary component-level check.
12. To record that one matching filename candidate belongs to a different component, add a `candidate_reviews` list to that component's work-job record. Each entry has exactly these fields: `candidate_path` (portable named-root path to the candidate), `sha256` (the candidate's current 64-character lowercase SHA-256), `decision` (`different_component`), `reason` (a concrete explanation), and `evidence_locator` (a portable named-root path to an existing evidence file or an HTTPS source URL). For example:

```json
{
  "candidate_reviews": [
    {
      "candidate_path": "${FERME_ROOT}/engineering/module-development/cad/parts/example-model.step",
      "sha256": "<current 64-character lowercase SHA-256>",
      "decision": "different_component",
      "reason": "The reviewed model has different source dimensions and represents the named adjacent size.",
      "evidence_locator": "${FERME_ROOT}/engineering/module-development/cad/work/example/review.md"
    }
  ]
}
```

   `model_inventory.py` validates all record fields before applying any review. It dismisses a filename candidate only when both its resolved path and current inventory SHA-256 exactly match the record. The dismissed row, including its inventory evidence, decision, reason and evidence locator, remains in `reviewed_candidates`. Stale-hash and unmatched records appear in `unmatched_candidate_reviews`; a stale, unknown or newly discovered candidate remains in `candidates` and continues to block a new build. A review never removes an attributed existing model or an unscoped model link; linked models retain their existing reuse/review action. Keep the review on the owning component work record so another component cannot inherit the decision.
