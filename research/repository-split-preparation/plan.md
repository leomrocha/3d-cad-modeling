# Generic tooling and FERME separation plan

Date: 13 November 2026. Status: proposed migration. Preparation authorized by the current request. Existing component development plan and geometry remain preserved.

## Ownership

1. 3dmodeling owns shared modeling algorithms, interfaces, source-intake and drawing tools, action definitions, generic research, procedures, synthetic tests and tooling-development reports.
2. FERME owns component identities, chosen/proposed parameters, manufacturer originals, model files, component recipes, measurements, captures, action occurrences, component progress, build journals and integration fixtures/results.
3. Mixed documents are split by subject. Retain the reusable finding and exact tool revision here; link to the component evidence in FERME. A component example supports the generic finding through a reference.
4. Classify by function and inputs. Generic functions receive geometry and expectations as arguments. A recipe requiring a FERME part ID or embedded project selection belongs in FERME. A product name alone does not decide ownership.

## Proposed destinations

1. Existing CAD files: retain FERME `engineering/module-development/cad/parts/` and its actual model index.
2. Existing component work: reuse its attributed FERME job directory under `engineering/module-development/cad/work/component-led-2026-11-12/` when a matching job is identified.
3. Historical component reports currently here: proposed archive `engineering/module-development/cad/work/repository-split-2026-11-13/3dmodeling/<original-relative-path>`. This preserves provenance; link it to the actual component job. Manifest destinations are proposals.
4. Downloaded component originals: proposed archive `engineering/module-development/parts/dimension-evidence/source-files/repository-split-2026-11-13/<original-relative-path>`. Reuse an existing identical original after hash and source-identity comparison.
5. Component recipes and integration tests: proposed FERME `skills/cad-construction/scripts/component_recipes/` and `skills/cad-construction/tests/`. Confirm Python import layout against existing cadtools before implementation.
6. Shared code and synthetic tests retain their 3dmodeling paths. General source records remain here; component observations move to FERME with links from reusable findings.

## Preparation delivered in this batch

1. Top-level folder purposes and ownership in the root README; usage and evidence rules in folder READMEs.
2. File-by-file snapshot manifest with proposed operations, source hashes, rationale and destination checks. SPLIT rows require section/function/record-level extraction, retaining the generic part here.
3. Script-change specification and modeling-agent instructions. Preparation changes documentation only.
4. Local source and proposal records. Web research is outside this preparation.

## Later migration sequence

1. Inspect both repositories' AGENTS.md and Git status. Identify the executing agent's current files and retain its work. Refresh the manifest and incoming-reference inventory against current bytes. Coordinate a completed component checkpoint for each affected active path; unrelated modeling continues.
2. Create scoped checkpoint commits in both repositories. Include only migration-owned changes; preserve concurrent staged and unstaged work. Refresh destinations, compare source identity and hashes, and record existing matching evidence before selecting COPY, REUSE or SPLIT.
3. First implement and verify explicit path/import support from script-changes.md. Maintain current readers until all callers of an affected path have been updated. Record the exact shared-tool commit used by FERME.
4. Copy each component artifact to its final destination with unchanged bytes. Compare hashes. For mixed reports preserve the original as dated evidence in FERME, then retain a generic summary and destination link here. Split source registers per observation; preserve source IDs, exact URLs, retrieval metadata and hashes.
5. Update live callers, tests, model/work records, source registers, generators, READMEs and skill references. Historical request text and old receipts remain exact; add a relocation mapping rather than rewriting historical quotations.
6. Run generic tests independently, FERME integration tests with explicit roots and dependencies, and link/reference checks. Reconcile actual test results and skipped integration cases separately. Check actual model inventory without rebuilding completed components.
7. Remove a source duplicate only after verified destination, updated callers, documented provenance and a safe checkpoint for any writer using that path. Commit scoped results in both repositories and record commits in the relocation map.

## Maintaining separation during continuing work

1. Apply the modeling-agent output routing now for future artifacts. Keep current active input/output paths intact until an individually coordinated transition.
2. Each iteration records component result paths in FERME and generic tool changes here, linked by component identity and tool commit. Commit each repository's own authorized files separately.
3. Proposed automated check: detect new FERME part-specific recipes, manufacturer originals and component journals under shared directories; review findings by content. Explicitly allow generic regression fixtures and linked component examples with stated ownership.
4. Proposed automated check: generic unit tests run without FERME; explicit integration tests report external-data requirements. Source registrations validate local targets and original hashes.
5. Future AGENTS.md cleanup: retain generic working rules here and reference FERME's current rules for farm work. Preserve the user instructions and their scope; prepare any removal separately. The live addition in this batch explains output routing without deleting existing rules.

## Completion conditions for the later split

1. Every manifest row has a final disposition and current hash; all proposed mixed-content extractions have reviewed outputs and links.
2. Component records resolve inside FERME; generic code accepts explicit external paths; shared-library dependencies are documented and tested.
3. Tests, imports, source/model references and original hashes pass their relevant checks; active work retains its artifacts and recorded state.
4. The executing agent uses the same ownership rules for subsequent iterations.
