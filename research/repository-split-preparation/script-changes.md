# Planned script and test changes

Status: proposal; existing Python files and commands retain current behavior in this preparation.

1. **part_index.py, component_records.py, source_intake.py, model_inventory.py, dxf_inspect.py:** retain shared implementations. Continue explicit index/job/project/output inputs. Test relocated external records and preserve original-file protection. A source-intake tooling self-test can retain its own evidence here; component intake outputs go to FERME.
2. **rounded_tube.py and axial_motor.py:** retain parameterized construction/check functions. They import `cadtools.geometry`; rounded_tube's CLI accepts `--cad-modules` and imports FERME `cadtools.runtime` and `cadtools.verification`. Document the existing external runtime and make other callers supply the same explicit runtime path. Inventory FERME callers before changing imports. Preserve native session, journal and save/reopen behavior.
3. **native_acis.py, step_placements.py, assembly_repair.py, feature_checks.py:** retain geometry/placement functions. Keep native representation limits and transformation options explicit. Component expectations and raw native records remain external inputs.
4. **pillow_block.py, battery_module.py, driver_checks.py:** retain supported family checks whose dimensions and metadata are supplied by the job. Extract any embedded component choices discovered during implementation into FERME job records. Battery checks cover shell/terminal patterns and named tabbed-case solids with repeated planar recesses, using source-bound expected features.
5. **pixhawk.py:** the inspected recipe requires C052, Pixhawk 6C, millimetres and M2 references. Propose moving the component recipe to FERME's component_recipes with its component procedure and tests. Keep any extracted general feature operations here only when their contract and tests support reuse. Preserve envelope and nominal-thread representation labels.
6. **small_bms.py:** inspected functions compare SAT/SAB points, body topology and assembly placements. Retain shared behavior; propose a geometry/persistence-oriented module name and a temporary import alias for existing callers during migration. Put C054 case paths and measured expectations in FERME. Resolve the final name after reviewing all current imports.
7. **test_native_acis.py, test_scaled_assembly.py, test_tabbed_battery.py:** retain synthetic tests here. Move FERME component integration cases to its test tree and provide explicit FERME_ROOT and shared script path. Replace implicit sibling-directory lookup in migrated tests; preserve actual numerical expectations and source links.
8. **test_small_bms.py:** current test reads C054 SAT/SAB under this repository's execution directory and inserts `${NATIVE_READER_ROOT}` into sys.path. Move the real component case to FERME; configure dependency location explicitly and retain shared function tests here.
9. **test_pixhawk.py:** separate generic fixtures for extracted shared functions from C052-specific recipe tests in FERME. Verify imports from the proposed recipe directory and current shared code before removing old paths.
10. **research/tools/build_workflow_register.py:** currently scans local round-* source files and regenerates source/idea/workflow outputs. Extend source discovery to registered batch records and cross-repository references while preserving stable source IDs, original URLs and observation scope. Avoid regenerating unrelated workflow documents during migration. Existing preparation records are indexed directly from research/README.md.
11. **research/tools/build_workflow_details.py:** retain generic workflow rendering. Check moved source locators and component examples without rewriting historical evidence.
12. **Other FERME callers:** search its skills, construction scripts, work scripts and documentation for exact moved filenames and absolute paths. Record each replacement in the migration manifest. Validate read-only CLI help, synthetic tests and actual retained integration fixtures before switching a live caller.

## Required checks before path transition

1. Generic unit suite runs with pinned reader dependencies and no FERME fixture data.
2. FERME integration suite receives explicit project root, shared tools path and cadtools path; reports results for the exact retained fixture hashes.
3. Existing-model inventory identifies the same completed component files. Original CAD/source hashes are preserved.
4. Each current caller resolves its imports and outputs after transition. The executing agent adopts changes at an affected component checkpoint.

## Independent skill packaging

Implementation scope authorized 13 November 2026: distribute each skill with the reusable code and instructions needed by its installation. The existing component-project runtime remains intact for concurrent callers.

1. **Generic code ownership:** maintain the required `cadtools.runtime`, `cadtools.geometry` and generic `cadtools.verification` functions under `scripts/cadtools/`. Keep the wheel-specific verification and catalogue code in the component project. Preserve source hashes and attribution in the [packaging source record](../sources/skill-packaging-2026-11-13.json).
2. **OCS transport:** maintain the copied generic control and coordinate-contract helpers under `scripts/`. Component skill instructions carry their own session, model-contract, journal, recovery and persistence instructions.
3. **Distribution:** generate skill-local script copies, licenses, dependency files, notices and hash manifests using `scripts/build_skill_packages.py`. Source intake and drawing inspection receive their dependency closures; component CAD receives the shared helper set. Canonical source remains in one location.
4. **Import transition:** the envelope and tube runners default to bundled control/runtime locations. The envelope runner's named project roots resolve job data and metadata; they supply no Python imports. Legacy explicit arguments remain accepted for existing callers. Installed instructions execute the skill-local defaults.
5. **Handoff:** leave existing FERME callers and runtime files intact. Each continuing component job can adopt an exact committed shared-tool revision at its checkpoint. Historical models, recipes, source files and evidence retain the migration plan's separate scope.
6. **Verification:** check each copied skill with an isolated interpreter, its declared dependencies and caller-supplied fixtures. Use the cached skills CLI for local discovery and individual temporary copy installation. Read the selected running OCS state through the bundled helper; retain package checks separately from component modeling results.

## Complete OCS skill ownership

1. `skills/cad-ocs-engineering/` combines the original OCS skill and repository component workflow, with both instruction sets merged directly in its main entrypoint. Original control helpers are reused from canonical `scripts/`; original references and adapted agent metadata are included in the package.
2. All component helpers and added procedures retain their supported source-bound behavior. Component recipes, dimensions, models, sources and evidence retain their owning-project routing. Existing external skill installations remain unchanged.
3. [Merge plan and coverage](../cad-ocs-engineering-merge-plan.md) record the checkpoint, source provenance, destination inventory and verification.
