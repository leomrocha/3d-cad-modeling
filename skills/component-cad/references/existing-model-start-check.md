# Check existing 3D files before starting a component

1. Run this check before every component start. It reads the external input manifest, work index, model paths, input-sheet links and files. It runs no CAD operations. Existing model paths, recorded scope and checks supply reuse evidence.

```sh
python3 ${MODELING_ROOT}/scripts/model_inventory.py \
  --index ${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json \
  --work-index ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/component-work.json \
  --cad-root ${FERME_ROOT}/engineering/module-development/cad \
  --project-root ${FERME_ROOT} \
  --id C001
```

2. **SKIP_EXISTING_MODEL:** a matching nonempty 3D file is present through an attributed manifest, work or sheet link. Mark the current build-list entry DONE, retain its actual path and use its existing checks. Move to a component requiring a new model. `model`, `output` and `native_model` are all observed work-record path fields.
3. **LOCATE_COMPLETED_MODEL:** the work record says DONE and the attributed path was not found. Locate its completed artifact using the available file inventory and existing records. Preserve completed status during that search.
4. **REVIEW_EXISTING_CANDIDATES:** the filesystem contains a model matching a component code without an attributed link. Review its actual identity and representation against the input sheet. Record a confirmed match and reuse it; identify a different-component reference explicitly. Direct dependency models remain separately listed.
5. **NEW_MODEL_REQUIRED:** the completed-file lookup found no attributed model or unresolved filename candidate for this component. Continue its existing source-readiness and construction procedure. Keep the filesystem result beside that particular start so it establishes which files were checked.
6. `2d_schemas` files are recorded as 2D references. Their existing model-link field does not classify them as 3D components. The current FERME list contains these interface references for the Blickle casters and SPP trailer coupling.
7. The initial reconciliation found existing 3D models for the ME0907 motor, both Sumitomo PRO gearmotors, BMW/Leaf/Victron batteries, SKF bearing, Sumitomo driver, Lynx BMS, Fibox enclosure, Victron 24/12 converter and both frame members. Their geometry and prior checks are reused. Reconciliation record (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/audit.json`).
