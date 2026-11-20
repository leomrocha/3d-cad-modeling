# Skill packages

Each skill directory is its installation unit. The skills CLI copies the selected directory and its contents.

1. **Source intake:** source capture, component-record hashing and part-index parsing; Python standard library.
2. **Drawing inspection:** DXF inspection, component-record hashing and part-index parsing; pinned native-reader dependencies.
3. **CAD OCS Engineering:** the complete OCS and component workflows, original OCS references and agent metadata, shared modeling and inspection helpers, `cadtools` geometry/runtime/save-reopen code, OCS transport and coordinate-contract checker; pinned native-reader dependencies and a running OpenCADStudio session.

4. **CAD MCP translator:** independent, standard-library-only offline planner, local ledger, mappings, procedures and geometric fixture. [User guide](cad-mcp-translator.md).

5. **CAD format translator:** owns `format_translation/`, its directional inventory example and source fixture. The installed planner runs independently. OpenSCAD and CadQuery are optional conversion runtimes. [User guide](cad-format-translator.md).

The [installation examples](../README.md#installing) select an agent and project/global scope, assign `SKILL_ROOT` to the installed directory, use a selected Python environment and check available operations. The skills CLI requires Node.js >=22.20 and npm/npx. Resolve bundled helpers from `SKILL_ROOT/scripts`. Supply source files, project roots, job records, output locations and the OCS session as caller inputs. [Installation](../README.md#installing).

## Maintain the packages

1. Edit reusable implementations under `scripts/`; edit each skill's instructions and references in its skill directory. New Python helpers automatically belong to CAD OCS Engineering. Source intake and drawing inspection receive their entry points' transitive local imports, including package initializers. The builder's `HOST_ONLY` declaration assigns build-only scripts to repository tooling. An import of build-only code or an unregistered script inside a distributed package fails validation.
2. Run `python3 scripts/build_skill_packages.py --finalize` after adding, changing or deleting reusable helpers or package dependencies/instructions. Supply the existing skills CLI and pinned Python dependency directories through `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT`, or `--cli-root` and `--reader-root`. The operation regenerates package copies, dependencies, licenses and source/hash manifests, then requires lifecycle and isolated installation checks. Missing prerequisites and failed checks return a nonzero exit status.
3. Run `python3 scripts/build_skill_packages.py --verify` for final validation. This checks synchronisation and executes the same mandatory tests without regeneration; a final sync check catches sources changed during the tests. Ordinary unittest discovery includes [the package sync and lifecycle gate](../tests/test_skill_package_build.py), which fails if regeneration was skipped. Record the PASS result before completing the reusable tooling improvement.
4. The [isolated package checks](../tests/test_skill_packages.py) copy dependencies into a temporary Python environment, install skills individually into temporary projects, check local references/imports/commands and exercise source-intake and DXF fixtures. Telemetry is disabled. Set a caller-selected `OCS_DESCRIPTOR` for the additional read-only OCS state check. Completion always requires the isolated package checks; live state access is conditional on that descriptor.
5. Commit canonical changes and generated copies/manifests in the same authorized batch, preserving unrelated work. `--check` remains a lightweight synchronisation check. For a historical comparison, `--committed --check` reads both the script inventory and bytes from local Git HEAD. Completion modes validate current sources and reject `--committed`.

### Tool index and attribution

1. Add each helper to [docs/tools.md](tools.md) and each main CAD procedure to [skills/README.md](../skills/README.md).
2. Keep required licences, notices and source links with the distributed code. Runtime availability belongs in the user’s local catalogue. Git preserves implementation history.

## Runtime ownership

Generic `cadtools` runtime, geometry and persistence functions are maintained here. Component recipes, dimensions, model files, source originals and job results retain their owning project. [Runtime provenance](../scripts/cadtools/NOTICE.md).

Package and dependency checks establish software execution and retained bytes. Component geometry and saved-file checks are recorded by their own modeling job.

## Skill name migration

1. `drawing-inspection` is now `cad-drawing-inspection`; `source-intake` is now `cad-source-intake`. Installation commands use the CAD-prefixed names.
2. An existing old-name installation remains its own local copy. Install the new skill by its current name; review and remove an old local copy separately when migrating that environment.

3. `component-cad` is now `cad-ocs-engineering`. From the repository checkout, run `npx skills add . --skill cad-ocs-engineering --agent claude-code --copy --yes` to install it for Claude Code.

Run `python3 -m unittest discover -s tests -p test_ocs_skill_merge.py` to check the CAD skill identity and documentation paths.

## Translator ownership

Canonical translator-only helpers live in `translator/`. The builder explicitly includes each module and bundled asset in the fourth package. Register an added module in the builder, installed checker, tools catalogue and any applicable distribution notices. Validate in an empty Python environment; the package checks modified, missing and unexpected assets. Existing OCS, drawing inspection and intake distributions keep their original contents.
