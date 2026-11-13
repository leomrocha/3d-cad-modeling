# Documentation and GitHub Pages repair plan

Date: 2026-11-13. Plan status: proposal. Audit: executed. Authorized repair execution: DONE.

[Executed changes and verification](../../execution/documentation-rename-repairs-2026-11-13.md). [Occurrence resolutions](repair-results.json). The observations below retain the pre-repair audit state.

## Current skill identities

1. **OCS engineering:** `cad-ocs-engineering`, combining the original OCS engineering and repository component workflows.
2. **Drawing inspection:** `cad-drawing-inspection`.
3. **Source intake:** `cad-source-intake`.

The three folder names, frontmatter names and package-manifest identities agree. The old names remain valid as recorded historical names and original-source identities. Current installation selectors and current procedure links use the three names above.

## Observed failures and changes

1. **Eight broken generated links:** `research/sources/source-register.md` contains summary links copied from skill references without rebasing them to the register's directory. The exact source line, target and error are in [audit results](checks.json). For example, `../scripts/step_placements.py` resolves under `research/scripts/`, while the relevant helper belongs to the skill's bundled scripts. The same error affects native ACIS, feature checks, dependencies, annular, toroidal, metadata and axial-motor links.
2. **Current versus historical skill instructions:** `skills/README.md:44,58` still directs readers to the external original OCS skill. The dated research section needs an explicit link to the current merged skill. `COMPONENT_DEVELOPMENT_PLAN.md:9` and `research/next-step-proposal.md:33` also direct reuse of that installed original. The original source locator remains attributed alongside a current execution link.
3. **Old paths in report text:** code-formatted paths in reports still name `skills/component-cad/`. Examples include `execution/c014-dimension-limits-2026-11-13.md:15`, `execution/c015-source-view-evidence-2026-11-13.md:9`, `execution/drawing-scale-and-dual-unit-review-2026-11-13.md:6`, and `execution/component-iteration-results-2026-11-13.md:5–7`. Add current procedure links beside the recorded historical references. The JSON appendix inventories every old-path candidate, including historical snapshots.
4. **Workflow catalogue naming:** `research/action-audit/skill-to-actions.md:17` uses the heading `ocs-engineering`; `skills/README.md:58` uses that same proposed workflow label. Preserve the dated proposal and identify the implemented package as OCS engineering (`cad-ocs-engineering`). Update incoming anchors if a heading changes. Workflow JSON, detail pages and source indexes contain original external-skill provenance; attach current execution mappings where those records guide current use.
5. **Missing path-reference document:** `AGENTS.md` directs readers to `docs/paths.md`, which is absent. The existing root-map instructions are in `skills/cad-ocs-engineering/references/paths.md`. Proposed correction: point the instruction to that existing reference and retain the document's ownership in the skill.
6. **Three shell examples have syntax errors:** one fenced block in `research/action-audit/implementation-queue/first-action-plan.md:50`, and two in `research/workflows/reconstruction-paths.md:242,259`, use angle-bracket placeholders as shell redirections. Replace placeholders with quoted caller-supplied variables or label schematic examples as text. These examples are dated proposals; retain that status.
7. **GitHub Pages result:** native Jekyll built `docs/` successfully. Its rendered homepage has 17 local href/src references; those targets and anchors pass. Current installation selectors and skill links on the homepage use the three current names. `docs/index.md` links repository documentation through GitHub blob URLs; the local audit checked those targets against the checkout.
8. **Pages source arrangement:** `docs/_config.yml` uses `/3d-cad-modeling` as baseurl. Its exclusions retain examples and tools as repository-linked documentation. `docs/skill-packaging.md` has no frontmatter and is copied as Markdown in the build; the homepage links its GitHub rendering. Preserve those destinations while repairing names. Future publication as additional styled site pages would require a separate content decision.

## Ordered repair batches

1. **Refresh and checkpoint.** Inspect current Git status and compare this audit with the latest concurrent edits. Record the exact authorized file list. Create a local checkpoint commit. Preserve the active annular runner, its procedure and tests, and the unrelated native-Pages records.
2. **Correct current entry points.** Review `README.md`, `docs/index.md`, `docs/tools.md`, `docs/skill-packaging.md`, `skills/README.md`, `scripts/README.md`, `COMPONENT_DEVELOPMENT_PLAN.md`, and `research/next-step-proposal.md`. Update current skill selectors, readable labels, install paths and execution links. Retain the wording edited by the user, exact helper filenames and completed merge content. Compare README and Pages sections after allowing for page-relative images and repository URLs.
3. **Correct linked workflow instructions.** Update the current execution mapping in `research/action-audit/skill-to-actions.md` and the relevant workflow records/details. Review every incoming anchor before changing headings. For dated research, retain original names as source history and add a clearly labelled current package link. Keep operation IDs, original URLs, status labels and numerical results stable.
4. **Repair report navigation.** Classify all locations in `checks.json` as current execution instructions, historical originals, dated snapshot paths, migration descriptions, helper/artifact names or test assertions. Replace current operational locators. Add current links beside historical report paths. Retain original locators, source hashes, dated merge inventories and split-manifest original paths. Retain artifact directories such as `execution/source-intake/` and helper names such as `source_intake.py`.
5. **Repair generated-register rendering at its source.** Inspect `research/tools/build_workflow_register.py` and `research/sources/tooling-registration-2026-11-13.json`. The register builder inserts Markdown-bearing summaries directly into a document in another directory. Preserve original summary observations; render embedded relative links against their actual source document before emitting register Markdown. Verify the eight destinations against the originating reference. Add a focused regression case for nested-reference summaries, existing anchors and repeated generation. Regenerate only affected register entries using the existing merge interface; preserve source IDs and observations.
6. **Correct the path reference and shell syntax.** Change the existing AGENTS path pointer to the packaged path reference. Rewrite only the three flagged command examples, preserving their proposed interfaces and source-backed reconstruction operations. Run shell syntax checks with positive controls; avoid executing the research pipelines.
7. **Keep GitHub Pages consistent.** Review `docs/index.md`, `_config.yml`, `_layouts/default.html`, assets, exclusions and example links together. Keep native branch deployment from `/docs`. Build safely into a caller-selected temporary directory. Check rendered navigation IDs, stylesheet/image paths, own-repository URLs, the repository link and `/3d-cad-modeling/` routing. Preserve existing images and patent confidentiality. Commit source files; GitHub generates the published output.
8. **Validate skill instructions and generated copies.** Check folder/frontmatter/manifest identity, all local references and command selectors. If a skill instruction or reusable generator changes, run the repository's required package `--finalize` and `--verify` procedures with the existing CLI/dependency directories, reviewing generated diffs against concurrent canonical edits. Keep canonical and generated files in that authorized repair batch.
9. **Record and commit results.** Rerun the full Markdown/JSON/site checks, list each resolved or retained historical occurrence, record actual counts and remaining concrete errors, inspect the scoped diff, and create the local result commit.

## Verification criteria

1. Each current skill instruction and install selector resolves to one of the three matching folder/frontmatter/manifest names.
2. Local Markdown links, images, explicit reference-style links, HTML references and own-repository links resolve. Anchors exist in the destination renderer. Code-formatted operational locators resolve or have an explicit caller-supplied root map.
3. The eight generated-register links resolve after regeneration. A repeated targeted generation preserves the same output and retained source observations.
4. Historical original locators and hashes remain unchanged, with current mappings where readers need navigation.
5. README and Pages retain equivalent installation instructions and examples; their URL forms match their respective renderers.
6. Native Jekyll builds from `/docs`; rendered local routes, IDs and assets resolve under the configured baseurl. Generated output remains outside tracked files.
7. Documented runnable shell blocks pass `bash -n`; schematic examples retain a literal-text label. Final JSON records parse after their last writes.
8. Scoped diff review confirms concurrent files remain with their owner. Only the authorized repair batch is staged and committed locally.

## Audit evidence

1. [Machine-readable locations and check results](checks.json): 286 tracked Markdown files, 4,080 local or own-repository link occurrences, eight link failures, 33 shell blocks and three shell syntax failures. The scan found 1,108 old-name occurrences and 220 old-path candidates; these counts include historical originals, helper names and snapshots.
2. [Sources inspected](../sources/documentation-rename-audit-2026-11-13.json): exact local source locators, dates, summaries, hashes and relationships.
3. Audit execution model: unavailable. Jekyll output was generated in a temporary directory. The audit performed local inspection and recorded this proposed repair plan.
