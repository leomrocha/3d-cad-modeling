# Point 03 visual and evidence review — vectors, sketches and small solids

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Registration date: 2026-11-12. Status: **DONE — local documentary review**. The procedures and cases below are proposals. Scope: CAD-08, CAD-09, CAD-10, CAD-13, CAD-14, CAD-15, DOM-03, DOM-04, DOM-05 and DOM-40, with readable operation names below.

Requested assignment: `gpt-6.1-sol`, reasoning effort `xhigh`. Actual executing model identity: **unavailable in this agent environment**. Evidence: live project instructions, audit plan, original operation records, local reports and registered source summaries. Original URLs are reused from those records. The executed output is this review document.

The [point-02 visual review](point-02-visual.md) supplies the shared identity/frame/view package, four execution options, revision-bound merge procedure and resource-record fields. This review adds the vector/profile/feature-specific requirements.

## 1. Findings for the point-03 definition

1. **Profile identity begins with source entities.** Retain source drawing hash, entity/path IDs, layers, block occurrence transforms, model/paper space, source units and selected sketch plane. A clean profile also needs an explicit outer-loop, hole-loop, island and separate-region interpretation for the requested part. [CAD-08 and CAD-09](../../workflows/cad-paths.json) and [DOM-03](../../workflows/domain-paths.json) provide the original selection and topology checks.
2. **SVG display scale and physical scale need separate evidence.** The registered FreeCAD SVG summary records viewBox/physical-dimension handling, a 90-DPI fallback when physical size is absent, and flattened Z on import. Record the actual importer result and the supplied control dimension. Keep a display-derived interpretation of size beside its evidence. The [round-two CAD source register](../../sources/round-02/cad-sources.json) supplies this source claim.
3. **Closure and constraint solving have distinct results.** Closure/intersection checks concern the selected curves. A sketch solver concerns the added constraints. Source correspondence concerns whether those curves and constraints represent the intended component, holes, datum and dimensions. Preserve all three results against the same revision.
4. **Tool branches need representation-specific handoffs.** DOM-03 lists CadQuery DXF import and OpenSCAD extrusion alongside a constrained-sketch output. Record the explicit constraint data produced by the selected route; a clean wire or CSG profile branch carries its actual representation. DOM-04 and DOM-40 include OpenSCAD among tools producing a CAD solid; CAD-15 already provides the explicit OpenSCAD-to-mesh branch. Keep that branch alongside the supported B-rep route required by the goal.
5. **Feature direction and component boundaries persist through construction.** Store sketch-plane normal, signed extrusion/revolve/cut direction, datum, hole axis and intended separate parts. Check them in native geometry and after exchange. A silhouette or valid solid can retain the wrong depth direction or omit an intended hole.
6. **Verification reports findings; recovery selects the next scoped transition.** CAD-13 reads the saved artifact and retains failed checks. CAD-14 consumes the brief/report and returns a revised brief or bounded recovery direction. A correction is executed through its named interpretation, sketch, construction or export action, with the earlier failed artifact retained.

## 2. Operation-specific inspection and retained evidence

A **VLM — vision-language model** processes images and language together. Here it examines labelled source views, selected curves, sketch/feature views and numerical reports to propose source-to-feature associations and compare alternatives. Geometry software supplies the recorded topology, dimensions and transforms.

| Operation | Concrete visual/semantic review | Software checks and retained output |
| --- | --- | --- |
| **CAD-08 — Read and clean vector drawing geometry** | Identify the intended view, part outline, hole contours, construction/annotation geometry and relevant layers. Compare original and cleaned overlays to find a removed feature, altered curve, duplicate occurrence or scale/orientation change. Inspect ambiguous SVG path/fill/stroke interpretation against the requested profile. | Retain original entity/path IDs and transforms; report entity counts by type/layer, unsupported/dropped entities, duplicates, endpoints, planarity and intersections. Each join, removal, discretization or repair has its before/after mapping and criterion. Compare bounds, area and controlling dimensions. |
| **CAD-09 — Build and constrain an editable planar sketch** | Associate each constraint with the intended source feature: diameter/radius, centre/edge distance, axis, symmetry, equality or datum. Review the constraints that change imported geometry and retain alternate associations when the source permits several readings. | Preserve support plane, datum, geometry IDs and named constraint IDs; record source value/unit/status and solver state, degrees of freedom, residuals and overconstraints. Recheck loop topology and source-to-constraint values after recompute. The original contract consumes vector geometry plus a brief, dimensions or measurement evidence. |
| **CAD-10 — Create a kernel solid and native model document from confirmed parameters** | Inspect whether the feature sequence creates the intended holes, depth, handedness and separate parts. Compare orthographic views and source feature associations from the same native revision. | Query valid solids, part count, face types, bounds, volume and required dimensions. Preserve feature/source or executable-source identity. Verify the named parameter change, regeneration and save/reopen on a bounded future case. Record actual kernel/export representations. |
| **CAD-13 — Verify model geometry and saved output** | Examine source versus saved/reopened views for semantic errors such as a different hole set, reversed feature direction or merged parts. Check that every reported number refers to the intended geometric feature. | Retain document revision, source/output hashes, operation IDs, units, criteria and actual measured results, including errors. Inspect native editability separately from geometry exchange. Reopen in the named independent consumer and measure its actual artifact. |
| **CAD-14 — Recover from failed interpretation or geometry construction** | Identify the earliest failed association or changed feature using source overlays, failed-check rows, logs and current geometry. Propose the exact source interpretation or feature transition to revisit. | Query operation state and actual revision first. Retain failed outputs and previous valid revision; invalidate only affected dependent checks/artifacts. Produce the bounded recovery brief, its evidence and next operation. |
| **CAD-15 — Render source-defined CSG as a mesh** | Compare the final evaluated mesh with the source-defined features and intended part boundaries. Inspect curved edges, small holes and contact features at the required views and scale. | Preserve OpenSCAD source, parameters, version and tessellation/export settings. Check actual saved mesh topology, normals, bounds, units, required feature dimensions and dimensional deviation. Associate any preview separately with the final mesh hash. |
| **DOM-03 — DXF/SVG drawing to constrained profile** | Review the complete profile interpretation: outer loop, holes, islands, separate regions and source annotations. Select the route that supplies the required editability and feature evidence. | Consume CAD-08's normalized geometry/evidence and CAD-09's actual constraint result when a constrained sketch is required. Preserve source entity-to-profile mapping. A CadQuery wire/CSG route receives its actual geometry/parameter representation and corresponding checks. |
| **DOM-04 — Brief/profile to native CAD solid** | Compare the chosen application-native construction with the confirmed brief/profile. Review additions, cuts, motion/separate-part meaning and source-associated dimensions. | Record the selected backend and supported features, native document/script, parameter names and component boundaries. Query valid shape/part counts, analytic/faceted surfaces, controlling dimensions and saved-file reopen. Use the explicit CAD-15 branch for a mesh-output CSG route. |
| **DOM-05 — Export STEP solid** | Compare native and reopened corresponding views for required feature presence, orientation, part boundaries and source correspondence. | Snapshot native identity/revision, export settings and required-feature manifest; create a new STEP derivative/hash. Reopen and compare solids, units, frames, bounds, volume, bore/interface dimensions and actual surface types. Preserve native model/history and the exchange loss map. |
| **DOM-40 — Script-parametric CAD authoring** | Review parameter-to-source association and operation meaning before generation; compare produced features with the same brief. Inspect a bounded parameter-edit result for an unintended dependent change. | Preserve source hash, environment/package versions, parameters/units, deterministic inputs and generated artifact hashes. Verify generated geometry with CAD-13. Keep B-rep generation and CAD-15 mesh generation as declared output branches. |

The original [CAD-R04 clean-profile recipe](../../workflows/details/cad-r04.md) gives a one-selected-wire baseline and assigns richer hole/multiple-region cases their own interpretation. Its millimetre and selected-profile checks retain their recipe scope. The generic point records the actual source unit, feature criteria and desired region set.

## 3. Branch comparison and selection within the stated intent

| Proposed branch | Goal and retained detail | Comparison with other branches |
| --- | --- | --- |
| Source-preserving vector branch | Keep selected source curves and explicit transforms for a drawing or sketch arrangement | Compare entity identity, scale, plane, loop selection and required dimensions |
| Constrained native-sketch branch | Add source-linked geometric/dimensional constraints for required editable features | Compare pre/post-solver curve changes, required constraints, loop/hole meaning and source values |
| Parameter-driven B-rep branch | Build the confirmed small part with native features or a pinned CadQuery/build123d/FreeCAD script | Compare controlling features, signed directions, part boundaries and preserved source parameters |
| Reduced-detail sketch branch | Retain the features required for the stated arrangement goal; label simplification lineage | Compare retained controlling dimensions and excluded feature effects against that particular goal |
| CSG mesh branch | Generate an OpenSCAD mesh from the explicit source/parameters | Compare source features, units, saved mesh dimensions, tessellation deviation and required topology |

Proposed selection/merge steps:

1. Give branches the same source/brief revision, intended use, units, datum, axes and required-feature criteria. A lower-detail branch can omit an appearance detail when that omission fits the supplied goal; its controlling interface criteria stay attached to the relevant features.
2. Map source entities to candidate loops, sketch geometries, constraints and native feature IDs. Keep separate candidates when a nested contour can mean a hole, island, separate part or annotation under the available evidence.
3. Measure each candidate's controlling features. Retain a difference row for source coordinates, unit conversion, loop/feature association, solver movement, construction direction or export approximation.
4. Give the VLM the full source view, labelled candidate overlays, raw source values, topology/solver reports and measured differences. Ask for an evidence-linked whole-candidate selection or compatible feature/evidence merge within the stated intent. Record the reason and retained alternatives.
5. Preserve explicit source dimensions while combining complementary evidence about the same identified feature. A proposed change to design intent or a conflict requiring new intent becomes a precise question for the dependent feature.
6. Create a new merged revision with selected source-to-feature mappings and parameters. Recompute topology, constraints and required feature dimensions. Independently review source-to-feature semantics and the numerical results; then check the actual saved derivative hash.

Examples of purpose-specific criteria:

1. **Sketch arrangement:** overall envelope, selected datum, principal axes and named component boundaries required by the brief.
2. **Robot interface:** bore/shaft diameter, mounting pitch, plane offset, axis location/direction and any required finite-span clearance, each with its own sourced dimensional/angular criterion.
3. **Building feature:** opening dimensions/position, wall thickness or elevation required by the particular task, with source-local and project-frame placement retained.
4. **Mesh derivative:** required feature deviation, surface approximation, topology and unit/frame criteria stated for the consumer.

These are feature categories. Numerical criteria come from the supplied brief, source specifications or an explicit scoped decision, with units and evidence class.

## 4. Persisted meaning across the vector-to-output chain

| Meaning | Required mapping/check |
| --- | --- |
| Source scale and orientation | SVG viewBox/physical unit or DXF unit evidence → numerical conversion factor → sketch-plane transform → model frame → export frame |
| Profile membership | Source entity/path IDs → loop IDs → outer/hole/island/separate-region role → face/profile consumed by the feature |
| Drawing annotation | Source value and region/entity → intended feature parameter → constraint/script parameter → actual queried feature |
| Feature direction | Signed depth/angle and named axis/plane → constructed feature → saved/reopened feature query |
| Component boundary | Source component identity → native body/part → exported solid/mesh component and occurrence mapping |
| Curve approximation | Original curve → join/discretization/tessellation settings and revision → required-feature deviation report |
| Editability | Native sketch constraints, application feature data or executable source → saved/reopened native artifact; exchange geometry receives its own representation record |

A shape-validity result states the kernel's result for that shape. A source-correspondence result states whether the checked feature is the one required by the source. Visual inspection can identify a suspicious relationship; the measurement receipt records the queried quantity and geometry revision. The OCS engineering contract (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and model-contract reference (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) supply the same-revision readback/view rule.

## 5. Repeatable software migration and exception rules

| Proposed software responsibility | Agent responsibility retained | Condition for software-led use |
| --- | --- | --- |
| Vector manifest: units, layers, entity types, transforms and retained/dropped IDs | Associate source content with the requested component/profile | The parser/importer version and supported entity class are demonstrated on the retained cases |
| Profile audit: endpoints, closed loops, intersections, containment candidates and before/after changes | Resolve hole/island/separate-part meaning and source-authorized repairs | The selected profile roles and repair criteria are explicit inputs |
| Constraint comparison: named source/constraint fields, residuals and solver movement | Choose the semantic association and diagnose competing constraints | Geometry/constraint IDs and source criterion are machine-readable |
| Solid construction: explicit parameters, signed operations and part boundaries | Interpret feature sequence and diagnose source/geometry disagreement | A demonstrated part family and parameter domain apply |
| Saved-output checks: native/STEP/mesh identity and required-feature measurements | Review semantic correspondence and importer/exporter exceptions | The adapter supports the actual representation and required features |
| Recovery dependency tracing | Identify the earliest semantic error and select a bounded correction | Explicit input/output dependencies and stable operation states exist |

1. **Agent directs work:** use named tool operations and queries for an ambiguous profile/constraint/feature case; retain the interpretation and source evidence.
2. **Software and agent work together:** batch supported parsing, topology, solver and geometry queries; the agent resolves feature associations and reviews exceptions.
3. **Software handles ordinary cases:** run a demonstrated vector/profile/part class; dispatch unsupported entities, conflicting units, ambiguous loop roles or changed required topology with their evidence package.
4. **Software handles the complete action:** process explicit entity selections, profile roles, constraints/parameters and checks through the supported adapter. Record actual exceptions and stop the affected dependent transition.

Migration applies to the particular action/input class after representative successful, ambiguous, invalid and interrupted cases have expected outcomes and an authorized implementation has demonstrated them. The [implementation plan](../../implementation-plan.md) retains its existing stage order and proposed `drawing-to-cad`, `parametric-solid-modeling`, `model-verification` and OCS adapter roles.

## 6. Failure and bounded recovery cases

| Observed future failure | Retained evidence | Next bounded action |
| --- | --- | --- |
| SVG scale or DXF unit evidence conflicts | Original metadata, imported control values and conversion record | Resolve the named source-unit/scale interpretation; regenerate affected profiles and derivatives |
| Importer drops/changes a required entity or block occurrence | Input/output entity manifests, unsupported-entity report and overlay | Select the supported documented importer/route or preserve that source geometry for a scoped interpretation |
| Loop closure repair changes a required feature | Original endpoints/curves, repair rule and dimensional differences | Revisit only the affected repair/profile role using the source criterion |
| Nested contours permit competing hole/island/part interpretations | Candidate loop graph, full source view and brief association | Retain alternatives and resolve the exact feature association before dependent construction |
| Constraints solve with changed source meaning | Constraint/source map, solver displacement and correct source annotation | Revise the named association/constraint; rerun affected sketch and feature checks |
| Boolean or feature construction fails | Valid prior revision, failed feature/log and parameter/source record | Diagnose the specific feature transition; preserve component boundaries and controlling dimensions |
| Saved native/STEP/mesh differs from the checked live geometry | Live revision, saved hash, reopen measurements and view manifests | Verify the save/export stage for that frozen revision; rerun dependent derivative checks |
| Timed-out mutation/export has uncertain completion | Stable operation/request ID, expected revision and partial output | Query the same operation identity and actual current state before another mutation |

A correction to one source dimension invalidates dependent constraints/features/exports according to the recorded dependency graph. Independent source evidence and unaffected earlier results retain their revisions.

## 7. Validation cases and resource observations for a future run

1. **SVG physical scale versus viewBox:** retain source declarations and a supplied control length; expected result is an explicit mapping and measured control comparison.
2. **DXF block/layer selection:** include repeated transformed source entities and annotation; expected result preserves original identity and selects the intended profile occurrences.
3. **Near-closed loop:** supply a gap and a source-based repair criterion; expected result records the endpoint change and tests the criterion before construction.
4. **Nested contours:** include an outer loop, hole, island and separate region with checked intended roles; expected result preserves those roles into native/output geometry.
5. **Solver success with wrong association:** constrain the wrong circle or edge; expected result is a source-correspondence finding despite a successful solver result.
6. **Signed construction:** use an explicit axis and signed depth/cut direction; expected result verifies the intended frame, face and feature placement after save/reopen.
7. **Reduced detail and precision interface:** compare purpose-specific branches; expected result retains required controlling criteria in both and labels the differing detail.
8. **Curved B-rep and faceted exchange:** compare analytic surface types and required dimensions after each actual export route; expected result records the route-specific representation and deviations.
9. **OpenSCAD final mesh:** compare source parameters, saved mesh dimensions, topology and approximation settings; expected result associates checks with the final file hash.
10. **Parameter edit and dependency regression:** change one declared input; expected result changes the intended dependent feature and preserves unrelated required features and source identity.
11. **Independent merge check:** combine compatible branch evidence, then measure/review the merged revision; expected result includes its own source, topology, numerical and saved-output checks.
12. **Interrupted operation:** lose a response after construction/export; expected result queries the same operation state and resumes only the incomplete bounded stage.

The [CAD-R04 recipe](../../workflows/details/cad-r04.md) records a CPU geometry baseline, with profile edges, nested contours and Boolean topology as scaling drivers. A future run records parsing/topology/solver/construction/export time separately, along with entity/edge/loop/constraint/face/triangle counts, peak RAM, render GPU/VRAM where used, input/output bytes and dependency versions. VLM comparison records page/view/crop count and resolution, transmitted evidence size, model/effort metadata, latency/cost and manual interpretation time. Compare required-feature accuracy, semantic correctness, retained editability and subsequent refinement work for the same intended use.

## 8. Local evidence and original links reused

Local evidence was read on 2026-11-12. External links retain the inspection status already held in their source records.

| Read local record / original URL | Concrete summary used here | Evidence status |
| --- | --- | --- |
| [CAD operations](../../workflows/cad-paths.json), [domain operations](../../workflows/domain-paths.json) | Original ten operation contracts, actual inputs/outputs, tool branches, preservation and checks | Local records inspected |
| [Audit plan](../plan.md), [point-02 visual review](point-02-visual.md), [composition rules](../../workflows/composition-rules.md) | Common evidence/frame/merge contract and goal-specific action criteria | Local procedure proposals inspected |
| [CAD-R04 clean-profile recipe](../../workflows/details/cad-r04.md) | CadQuery/ezdxf unit/layer and selected-wire extrusion path, FreeCAD SVG branch, readback checks and topology scaling drivers | Existing local assessment inspected |
| [CAD assessment](../../cad-and-skills.md), [local baseline](../../local-baseline.md), [implementation plan](../../implementation-plan.md) | Native/parametric/mesh/B-rep ownership, OCS faceted STEP source finding and retained staged toolkit proposals | Existing local reports/proposal inspected |
| OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`), model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) | Explicit part/frame/feature meaning, revision-bound measurements/views and operation-state recovery | Local source read in point-02 review and reused |
| [FreeCAD Draft DXF](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md) | Registered summary lists importer-specific entity support, format/version conditions and unsupported 3D ACIS SAT payloads | `web_inspected`, reused from [round-two CAD records](../../sources/round-02/cad-sources.json) |
| [FreeCAD Draft SVG](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md) | Registered summary lists supported paths/shapes, flattened Z, physical/viewBox scale and fallback DPI behavior | `web_inspected`, reused from [round-two CAD records](../../sources/round-02/cad-sources.json) |
| [ezdxf documentation](https://ezdxf.readthedocs.io/en/stable/), [units](https://ezdxf.readthedocs.io/en/stable/concepts/units.html) | Registered summaries cover DXF parsing/writing and `$INSUNITS` conversion; unitless coordinates use external scale evidence | `web_inspected`, reused from [round-two](../../sources/round-02/cad-sources.json) and [round-three CAD records](../../sources/round-03/cad-detail-sources.json) |
| [FreeCAD Sketcher scripting](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md), [Part scripting](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md) | Registered summaries describe geometric/dimensional constraints and B-rep vertices/edges/wires/faces/solids/Booleans | `web_inspected`, reused from [round-two CAD records](../../sources/round-02/cad-sources.json) |
| [CadQuery import/export](https://cadquery.readthedocs.io/en/stable/importexport.html), [API reference](https://cadquery.readthedocs.io/en/stable/classreference.html) | Registered summaries cover DXF and STEP exchange/units, validity, bounds, volume and transforms | `web_inspected`, reused from [round-three CAD records](../../sources/round-03/cad-detail-sources.json) |
| [build123d operations](https://build123d.readthedocs.io/en/latest/operations.html), [stable documentation](https://build123d.readthedocs.io/en/stable/) | Registered summaries cover OCCT B-rep construction and sketch/face extrusion | `web_inspected`, reused from [round-two CAD records](../../sources/round-02/cad-sources.json) |
| [OpenSCAD documentation supplied in operation records](https://openscad.org/documentation), [separately registered documentation URL](https://openscad.org/documentation.html) | Registered summaries describe source-defined CSG, parameterization, profile imports/extrusion, CLI and mesh export; exact URL spellings retained | `web_inspected`, reused from [round-two](../../sources/round-02/cad-sources.json) and [round-three CAD records](../../sources/round-03/cad-detail-sources.json) |

## 9. Integration handoff

1. Integrate profile-role/source mapping, actual constraint representation, signed feature persistence and per-output checks into point 03 as proposals.
2. Record the original DOM-03/DOM-04/DOM-40 tool/output branch issues as bounded handoff findings; preserve the original operation records.
3. The coordinator owns source registration, graph consistency and checkpoint/result commits. This review writes only its assigned document.
