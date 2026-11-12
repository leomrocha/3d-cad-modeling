# Main frame longitudinal rail: source actions and native build

Date: 12 November 2026. Executing model: **gpt-6.1-sol**. State: **BUILT_REOPENED_FEATURE_CHECK_REQUIRED**. Starting checkpoints: tooling `9c19f7b`, FERME `2745480`.

## Delivered geometry and checks

1. [Native rail DWG](/home/leo/projects/ferme/engineering/module-development/cad/parts/p01-main-frame-longitudinal-rail-reference.dwg): one source-labelled nominal hollow section, proposed 40 × 40 × 3 mm, 600 mm length; EN 10219-2:2019 nominal calculation radii 6 mm outside / 3 mm inside. Local section XY, front-end centre at origin, cut length+Z. Dimensions remain project-proposal and standard-calculation values.
2. [Native pre-save checks](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/pre-save-checks.json): five groups PASS—section/length extents, X wall planes, Y wall planes, end planes and all eight corner cylindrical surfaces. Numerical comparison threshold1e−7 mm is a readback threshold.
3. [Persistence receipt](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/persistence.json): DWG 2018 save/hash/audit-manifest checks PASS, one solid, zero dropped entities, hash `e7bd8c78f2bd07126b170becccc9475d9b9c80becde387d458dc048c2c755e90`; reopened document 71.
4. [Reopened feature check](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-checks.json): UNKNOWN. The native record exposes20,277 bytes of SAB binary data. The implemented surface reader supports SAT text. The helper preserves the raw record and classifies the encoding explicitly.
5. [End view](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-viewport.png) and [isometric view](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-isometric.png) inspected: the reopened document shows the hollow rounded section and longitudinal edges. [Reopened measure result](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-measure.json) reports mesh volume 252167.41146658108 mm³ and zero bounds. Preserve that bounds/mesh discrepancy as an OCS readback finding.

## Recorded source actions

1. The earlier [standards research report](/home/leo/projects/3dmodeling/research/tube-corner-research.md) and13 individual source observations documented the supplier lookup, cold/hot standard branches, access results and calculations. The current batch adds four [reusable source-action definitions](/home/leo/projects/3dmodeling/research/action-audit/component-source-actions.json) and appends their actual occurrences in FERME.
2. **Find an existing stock component and its supplier record (COMP-SRC-A01):** reused the exact Fers & Métaux item040819 record and attributed40×40×3 mm exterior dimensions to the listing.
3. **Find standards for the component and feature (COMP-SRC-A02):** requested Luna research found EN 10219-2:2019 and EN 10210-2:2019 process-specific alternatives. Requested model `gpt-6-luna`; actual researcher runtime identity unavailable. No new external search was commissioned in this construction batch.
4. **Check source access and attribute each technical claim (COMP-SRC-A03):** retained readable clauses, indexed Annex formulas, metadata-only PDF open, failed source access and the corrected formula attribution.
5. **Calculate nominal feature values from the standard (COMP-SRC-A04):** applied2T/T to nominal T = 3 mm for the reference model’s 6/3 mm radii, with4.8–7.2 mm manufacturing-profile evidence separately recorded.
6. **Select a supported solid feature route (CAD-10-A01):** [source revision 2](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/source-job-r02.json) pins the research report and original component sheet; readiness passes. Revision1 and its earlier NEEDS_INPUT observation remain historical records.

## Actual build attempts and applied improvements

1. Attempt1, document 68: initial extrusion completed without changes after the shared helper sent select(clear=True,handles=...). Local OCS implementation and selection readback show clear=True clears only. The preserved profile coordinates/bulges were inspected before resuming. `SelectionCheckedClient` now sends explicit nonempty picks with clear=False and verifies actual selection. Resumed outer/cutter extrusions produced the source-defined extents.
2. Attempt1 native solid subtraction returned **“SUBTRACT: the selected topology could not be cut safely.”** Base and cutter records and measurements are retained. Attempt2, document 69, returned the same error for planar-region subtraction. Each retains its request journal and result.
3. Attempt3, document 70: direct bounded-area extrusion between the two rounded closed profiles produced the hollow solid. The helper derives the wall-interior pick from the section inputs. Its temporary profile entities were removed; native source metadata retained. Original unrelated wheel document 52 remains revision 2/dirty=true in the captured state.
4. The new [Python helper](/home/leo/projects/3dmodeling/scripts/rounded_tube.py) reuses FERME Client/Journal/Geometry/save_reopen and the installed control helper. It supplies the verified selection adaptation, parameterised hollow-section route, source readiness, checkpoints, native SAT checks and explicit reopened-encoding result. The default route is the exercised bounded-area route. Solid/planar subtraction route names retain the observed failure cases.
5. The [component skill](/home/leo/projects/3dmodeling/skills/component-cad/SKILL.md) now routes standard-feature preparation and hollow-section work to the [actual procedure and recovery notes](/home/leo/projects/3dmodeling/skills/component-cad/references/source-first-and-tube.md).
6. Helper regression suite: **28 tests PASS**. Tests cover recorded clear-only selection behavior, actual selection mismatch, wrong dimensions/walls/radii and reopened binary-encoding status in addition to the existing 18 source/index/occurrence tests. Skill validation has its own receipt.
7. Isometric capture initially exceeded the runtime's query-count bound; same-ID recovery completed the original capture. Its original request and recovered response remain in the view journal.
8. Initial schema reads required request/document identifiers. The installed `guide`/`entity_schema` operations returned unknown_operation; document-bound `record_schema` supplied the actual profile/solid definitions. VPOINT returned unknown_command; supported `-VIEW SEISO` and `ZOOM EXTENTS` produced the captured view. These responses remain linked in the attempt evidence.

## Current implementation point

1. FERME [component work index](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/component-work.json) links the rail DWG and [current result](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/result.json).
2. The next required rail action is reading/querying the reopened SAB feature geometry, repeating the source-linked dimensions and investigating the zero-bounds discrepancy. The crossmember's existing rail dependency remains in its work record.
3. Original operation graph, rankings and component plan remain unchanged. The four supplemental source-action definitions link to existing intake/solid-construction actions. All13 appended semantic occurrences and native request journals belong to FERME; reusable code/instructions belong here.

## Verification receipt

[Batch checks and retained stage statuses](/home/leo/projects/3dmodeling/execution/p01-rail-checks.json) record source hashes, source readiness, independent native-record comparisons, unchanged original models/graphs, action-registry append checks, skill validation and documentation rebuild comparison.

FERME result commit: `243964d` (native model, source revisions, action history and build/check evidence).
