# Modeling and inspection scripts

1. Purpose: shared code for source records, part-index access, existing-model lookup, DXF inspection, native geometry checks and parameterized construction.
2. Maintain shared functions here. Save component models, recipes and inspection results in the modeling job's configured output directory.
3. Dependencies: [requirements-native.txt](../requirements-native.txt) pins native-reader packages. OCS construction imports the local `scripts/cadtools` modules and uses `scripts/ocs_control.py`. Installed skills carry generated copies and their own `requirements.txt`. [Package maintenance](../docs/skill-packaging.md).
4. Use the [parts catalogue configured at setup or refresh](../skills/cad-ocs-engineering/references/modeling-operation-selection.md#set-up-and-refresh-the-local-operation-catalogue) to find existing components. Supply the job record, work index, CAD root and selected source paths required by the operation. The [tools catalogue](../docs/tools.md) lists each Python helper and its purpose.
5. `part_index.py --index PATH --id ID` searches an index; `component_records.py JOB.json` reports source readiness. Both print JSON.
6. `model_inventory.py --index PATH --work-index PATH --cad-root PATH --project-root PATH [--id ID] [--configuration EXACT_NAME]` prints model lookup JSON and reads existing files. Configuration selection requires `--id`; [selection and retained-drawing rules](../skills/cad-ocs-engineering/references/existing-model-start-check.md).
7. `source_intake.py --input SPEC.json --output NEW_DIRECTORY` writes a protected source revision. [Input contract](../skills/cad-source-intake/SKILL.md).
8. `dxf_inspect.py SOURCE.dxf --output NEW.json [--space Model] [--layer NAME]` writes a bounded source inventory. [Drawing contract](../skills/cad-drawing-inspection/SKILL.md).
9. Construction requires an authorized source-bound job, current CAD session, explicit destinations and existing-model check. [Component procedure](../skills/cad-ocs-engineering/SKILL.md).
10. `retained_artifacts.py MANIFEST.json [--job JOB_JSON] [--project-root DIRECTORY] [--output SAVED_MODEL]` verifies manifest paths, file hashes and saved JSON/JSONL syntax. [Retained-file contract](../skills/cad-ocs-engineering/references/retained-artifact-checks.md).
11. `envelope_job_runner.py --help` lists the job record, receipt directory, selected output and OCS session inputs. Its default is read-only preflight; `--allow-write` enables the guarded native route for an authorized job. [Runner contract](../skills/cad-ocs-engineering/references/envelope-job-runner.md).
12. `ocs_document_cleanup.py` exports `cleanup_active_owned_document()` for the existing CAD runner. Its inputs include caller ownership records, saved-file hashes and persistence receipts. [Cleanup contract](../skills/cad-ocs-engineering/references/document-cleanup.md).
13. Python bytecode, virtual environments and test caches are excluded by the repository [ignore rules](../.gitignore).

## Source-bound reference geometry

1. [annular_reference.py](annular_reference.py) is an imported construction and inspection module. `build_annulus(client, job)` creates a plain ring; `inspect(client, handle, job)` reads native geometry and stored source metadata. The external job supplies dimensions in millimetres, source bindings and local placement. [Input and check contract](../skills/cad-ocs-engineering/references/annular-reference.md).
2. [hexagonal_reference.py](hexagonal_reference.py) exports `build_hexagonal_reference(client, job)` and the source-defined polygon utility `regular_hexagon_points`. Supply across-flats dimension, height, frame and any bore diameter through the external job. [Input and check contract](../skills/cad-ocs-engineering/references/hexagonal-reference.md).
3. [toroidal_reference.py](toroidal_reference.py) constructs and inspects source-bound circular-section rings. See [ring geometry](../docs/tools.md#circular-section-ring-geometry).

## Package maintenance

1. `python3 scripts/build_skill_packages.py --finalize` registers new helpers, regenerates skill copies and source/hash manifests, and requires lifecycle and isolated installation checks. Supply `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT` as existing software inputs. Use `--verify` for read-only final validation. `--check` detects source/distribution differences; the ordinary test suite also enforces synchronisation. [Completion procedure](../skills/cad-ocs-engineering/references/package-completion.md).
2. `package_check.py` runs from an installed skill and checks its own files, imports and dependency versions. Component CAD accepts `--session` or `--descriptor` for a read-only OCS state check.
3. `ocs_control.py`, `check_contract.py` and `cadtools/` hold the generic control, coordinate checks, geometry and persistence code. [Runtime provenance](cadtools/NOTICE.md).
