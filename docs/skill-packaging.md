# Skill packages

Each skill directory is its installation unit. The skills CLI copies the selected directory and its contents.

1. **Source intake:** source capture, component-record hashing and part-index parsing; Python standard library.
2. **Drawing inspection:** DXF inspection, component-record hashing and part-index parsing; pinned native-reader dependencies.
3. **CAD OCS Engineering:** the complete OCS and component workflows, original OCS references and agent metadata, shared modeling and inspection helpers, `cadtools` geometry/runtime/save-reopen code, OCS transport and coordinate-contract checker; pinned native-reader dependencies and a running OpenCADStudio session.

The [installation examples](../README.md#installing) select an agent and project/global scope, assign `SKILL_ROOT` to the installed directory, create a Python 3.12 environment and execute the package checker. The skills CLI requires Node.js >=22.20 and npm/npx. Resolve bundled helpers from `SKILL_ROOT/scripts`. Supply source files, project roots, job records, output locations and the OCS session as caller inputs. [Installation](../README.md#installing).

## Maintain the packages

1. Edit reusable implementations under `scripts/`; edit each skill's instructions and references in its skill directory. New Python helpers automatically belong to CAD OCS Engineering. Source intake and drawing inspection receive their entry points' transitive local imports, including package initializers. The builder's `HOST_ONLY` declaration assigns build-only scripts to repository tooling. An import of build-only code or an unregistered script inside a distributed package fails validation.
2. Run `python3 scripts/build_skill_packages.py --finalize` after adding, changing or deleting reusable helpers or package dependencies/instructions. Supply the existing skills CLI and pinned Python dependency directories through `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT`, or `--cli-root` and `--reader-root`. The operation regenerates package copies, dependencies, licenses and source/hash manifests, then requires lifecycle and isolated installation checks. Missing prerequisites and failed checks return a nonzero exit status.
3. Run `python3 scripts/build_skill_packages.py --verify` for final validation. This checks synchronisation and executes the same mandatory tests without regeneration; a final sync check catches sources changed during the tests. Ordinary unittest discovery includes [the package sync and lifecycle gate](../tests/test_skill_package_build.py), which fails if regeneration was skipped. Record the PASS result before completing the reusable tooling improvement.
4. The [isolated package checks](../tests/test_skill_packages.py) copy dependencies into a temporary Python environment, install skills individually into temporary projects, check local references/imports/commands and exercise source-intake and DXF fixtures. Telemetry is disabled. Set a caller-selected `OCS_DESCRIPTOR` for the additional read-only OCS state check. Completion always requires the isolated package checks; live state access is conditional on that descriptor.
5. Commit canonical changes and generated copies/manifests in the same authorized batch, preserving unrelated work. `--check` remains a lightweight synchronisation check. For a historical comparison, `--committed --check` reads both the script inventory and bytes from local Git HEAD. Completion modes validate current sources and reject `--committed`.

### Required catalogue and source registration

1. Add a readable helper entry to [docs/tools.md](tools.md), and index each procedure referenced by the CAD skill in [skills/README.md](../skills/README.md).
2. Record original source locators, titles, summaries, dates, evidence status, hashes and referring documents in an attributed JSON file under `research/sources/`. Merge that file into both combined source indexes using `python3 research/tools/build_workflow_register.py --date YYYY-MM-DD --source-record research/sources/RECORD.json`. The merge preserves existing source IDs and observations; repeated merges are idempotent. Pass the actual client date explicitly.
3. The combined register retains the input-document list. Future full register builds replay those documents. `--finalize` and `--verify` check helper catalogue coverage, procedure-index coverage, source coverage and whether both combined source indexes include the latest observations from those documents. Register omissions fail completion.

## Runtime ownership

Generic `cadtools` runtime, geometry and persistence functions are maintained here. The existing component-project copies remain intact for current callers. Component recipes, dimensions, model files, source originals and job results retain their owning project. [Runtime provenance](../scripts/cadtools/NOTICE.md). [Migration update](../research/repository-split-preparation/script-changes.md#independent-skill-packaging).

Package and dependency checks establish software execution and retained bytes. Component geometry and saved-file checks are recorded by their own modeling job.

## Skill name migration

1. `drawing-inspection` is now `cad-drawing-inspection`; `source-intake` is now `cad-source-intake`. Installation commands use the CAD-prefixed names.
2. An existing old-name installation remains its own local copy. Install the new skill by its current name; review and remove an old local copy separately when migrating that environment.
3. Historical source locators retain their original values. Added current locators and the [rename record](../execution/skill-renaming-2026-11-13.md) identify the moved packages.

## Complete OCS engineering merge

1. `cad-ocs-engineering` combines the full original OCS engineering skill and this repository’s component workflow. Both workflows are merged directly into its main `SKILL.md`.
2. The package retains the component procedures, generic helpers, tests and source checks developed here. It also includes the original OCS control, computational-engineering and capability references and adapted agent metadata.
3. The former `component-cad` package is now `cad-ocs-engineering`. [Merge inventory and verification](../execution/cad-ocs-engineering-merge-2026-11-13.md).

The dated merge comparison can be rechecked with `VERIFY_OCS_MERGE_SNAPSHOT=1 python -m unittest discover -s tests -p test_ocs_skill_merge.py`. It validates the retained snapshot; ordinary component improvements keep their own current checks and evidence.
