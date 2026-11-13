# Skill packages

Each skill directory is its installation unit. The skills CLI copies the selected directory and its contents.

1. **Source intake:** source capture, component-record hashing and part-index parsing; Python standard library.
2. **Drawing inspection:** DXF inspection, component-record hashing and part-index parsing; pinned native-reader dependencies.
3. **Component CAD:** the shared modeling and inspection helpers, `cadtools` geometry/runtime/save-reopen code, OCS transport and coordinate-contract checker; pinned native-reader dependencies and a running OpenCADStudio session.

Set `SKILL_ROOT` to the installed directory. Resolve bundled helpers from `SKILL_ROOT/scripts`. Supply source files, project roots, job records, output locations and the OCS session as caller inputs. [Installation](../README.md#installing).

## Maintain the packages

1. Edit reusable implementations under `scripts/`; edit each skill's instructions and references in its skill directory.
2. Run `python scripts/build_skill_packages.py`. It copies only the modules needed by source intake and drawing inspection, and the current shared helper set into component CAD. Each package also receives its dependency declaration, MIT license, attribution notice and a manifest of generated-file hashes.
3. Run `python scripts/build_skill_packages.py --check` to check that generated copies match the canonical code. Commit source changes and regenerated copies in the same authorized batch. During concurrent work, `--committed` reads canonical bytes from local Git HEAD; use `--committed --check` to verify packages against that committed source while preserving another agent’s pending edits.
4. Run [isolated package checks](../tests/test_skill_packages.py) using the existing pinned dependency directory and cached skills CLI as explicit test inputs. The checks copy dependencies into a temporary Python environment, install skills individually into temporary projects, check local references/imports/commands and exercise source-intake and DXF fixtures. A separate read-only OCS state check uses the caller's selected descriptor.

## Runtime ownership

Generic `cadtools` runtime, geometry and persistence functions are maintained here. The existing component-project copies remain intact for current callers. Component recipes, dimensions, model files, source originals and job results retain their owning project. [Runtime provenance](../scripts/cadtools/NOTICE.md). [Migration update](../research/repository-split-preparation/script-changes.md#independent-skill-packaging).

Package and dependency checks establish software execution and retained bytes. Component geometry and saved-file checks are recorded by their own modeling job.
