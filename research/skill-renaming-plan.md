# CAD skill renaming plan

Date: 13 November 2026. State: DONE. Execution: [rename report](../execution/skill-renaming-2026-11-13.md).

1. **Requested names:** `drawing-inspection` becomes `cad-drawing-inspection`; `source-intake` becomes `cad-source-intake`. The supplied reason is public-repository indexing. `component-cad` retains its name.
2. **Scope:** rename the two installable skills and update their package identities, installation commands, active documentation, references, generators and tests. The Python helper names `dxf_inspect.py` and `source_intake.py` retain their existing APIs and filenames.
3. **Inventory:** the [source and reference inventory](sources/skill-renaming-plan-2026-11-13.json) records matching tracked files, hashes and reference categories. Refresh it against concurrent work immediately before implementation.

## Execution sequence

1. **Checkpoint:** inspect staged and unstaged changes; create the required local checkpoint with only the rename batch's authorized files. Preserve the ongoing modeling work. Record the committed canonical source revision used for package generation.
2. **Package directories and identity:** move `skills/drawing-inspection/` to `skills/cad-drawing-inspection/` and `skills/source-intake/` to `skills/cad-source-intake/`. Change each `SKILL.md` frontmatter `name`. Retain descriptions, instructions, helper contents, dependency declarations, licenses and attribution. Remove the old discoverable directory names as part of the moves.
3. **Generator and checks:** update `SKILLS`, skill-specific branches and package identity fields in `scripts/build_skill_packages.py`; update `NAMES`, per-skill expectations and fixture selectors in `tests/test_skill_packages.py`. Inspect `scripts/package_check.py` for name-based conditions. Regenerate manifests under the new directories and check copied script origins. Use committed canonical helper bytes to preserve concurrent implementations; inspect generated-file diffs before staging.
4. **Installation and documentation:** update README installation commands, skill invocations, displayed identifiers and directory links; mirror the changes in `docs/index.md`. Update `docs/tools.md`, `docs/skill-packaging.md`, `skills/README.md`, `scripts/README.md`, cross-skill links and applicable repository instructions. Update active research/action-queue skill pointers and the separation plan's current references. Recheck every other inventoried match by meaning.
5. **Historical references:** keep original source identifiers, supplied URLs, captured source bytes, hashes and execution receipts. Repair navigational links to the moved skill files. Add explicit current locators or rename mappings beside historical source paths, preserving the recorded original locator. Existing `execution/source-intake/` artifacts and `execution/dxf-inspection.md` retain their artifact names; review their outgoing skill links. Record the renamed skills in the new execution report.
6. **Installed copies:** document installation with the new names and explain that an existing old-name installation remains a separate local copy until migrated. Repository work updates package contents and instructions. Keep installed user directories, private publishing records and public listings within their separately scoped work.
7. **Verification:** perform the checks below, review the scoped diff and staged files, then create the local result commit. Record the actual checks and model identity when available.

## Verification

1. Cached skills CLI discovery reports exactly `component-cad`, `cad-drawing-inspection` and `cad-source-intake`, with matching folder and frontmatter names.
2. Each renamed skill installs individually into a temporary project and carries its scripts, requirements, instructions, license and valid package manifest.
3. Local references and anchors resolve. Active installation commands and skill invocations use the new names. Remaining old names are classified historical identifiers, artifact paths, original locators or explicit migration mappings.
4. The package generator's consistency check passes against the authorized committed source. Generated-file diffs contain the scoped rename and regeneration changes.
5. Isolated Python imports and command entry points pass; source-intake and DXF fixtures preserve their source files and produce checked outputs. Component CAD retains its existing discovery and package checks.
6. JSON parses, Markdown links and shell blocks pass their appropriate checks. Record results under `execution/` with sources under `research/sources/`.

## Preservation and commit boundaries

1. The planning batch writes this plan, its source inventory and the research index, with a checkpoint and result commit.
2. The implementation batch receives its own checkpoint and result commit when the rename is executed. Stage explicit paths and review generated copies before committing; the previous packaging finding showed why concurrent source edits require this check.
3. Keep `chores/` ignored and its personal contents outside Git history. Preserve concurrent modeling files and staged changes, component-project data, source originals and confidential material. Use local Git only.
