# Source register

Registered: 2026-11-13.

Each entry preserves the original URL or local source path and records its summary, evidence status and referring documents. Detailed observations are retained in [source-register.json](source-register.json).

<a id="src-001b3a40cfd7"></a>

## SRC-001b3a40cfd7 — Source-bound driver exterior checks

Original source: [${MODELING_ROOT}/scripts/driver_checks.py](../../scripts/driver_checks.py)

Summary: Uses the shared functions and pinned component expectations to check 116 separate solids, mounting features, terminal geometry and connector span. Original span fails; corrected saved derivative passes all141 checks.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-00a3a7e8697d"></a>

## SRC-00a3a7e8697d — Agent skill: openscad

Original source: [https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/skills/openscad/SKILL.md](https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/skills/openscad/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: openscad. Source class: agent skill instructions. Original reuse terms: Apache-2.0; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-00ae3f8da761"></a>

## SRC-00ae3f8da761 — COLMAP LICENSE

Original source: [https://github.com/colmap/colmap/blob/main/LICENSE](https://github.com/colmap/colmap/blob/main/LICENSE)

Summary: Primary repository licence text for COLMAP.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r06.md.

<a id="src-00b33c4777ca"></a>

## SRC-00b33c4777ca — Driver iteration — opened-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/opened-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/opened-state.json`)

Summary: Recovered original open state identifies driver document77 and original saved path.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-00e7f773e988"></a>

## SRC-00e7f773e988 — Perspective-n-Point (PnP) pose computation — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html)

Summary: OpenCV 4.13.0 documents solvePnP inputs as 3D object points, matching 2D image projections, camera intrinsic matrix and distortion coefficients. rvec/tvec transform object-frame points into camera-frame coordinates; camera axes are X right, Y down, Z forward. The page documents method-specific point-count and planarity conditions, alternative solutions returned by solvePnPGeneric, and RANSAC PnP for outliers. This is API capability evidence, not a local pose result or accuracy report.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-00ef88b61c5d"></a>

## SRC-00ef88b61c5d — Independent procedure review — Point 01 model brief

Original source: [${MODELING_ROOT}/research/action-audit/reviews/independent-review.md](../action-audit/reviews/independent-review.md)

Summary: Authored audit document recording Independent procedure review — Point 01 model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-00fe5418f4eb"></a>

## SRC-00fe5418f4eb — ocs-skill-improvements.md — proposed_skill_extension

Original source: ${FERME_ROOT}/skills/ocs-skill-improvements.md (`${FERME_ROOT}/skills/ocs-skill-improvements.md`)

Summary: Proposed OCS additions derived from recorded commands, topology recovery and representation/display observations. Applicability: Held in ferme; installation is a separate action.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-08/component-plan-sources.json, research/sources/round-09/component-execution-sources.json.

<a id="src-011a79e3f993"></a>

## SRC-011a79e3f993 — Driver iteration — reopened-side.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-side.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-side.png`)

Summary: Inspected side image shows housing taper, mounting base and separate projecting connector/terminal geometry against source side outline.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-011e8da740e4"></a>

## SRC-011e8da740e4 — ifcopenshell.api.feature.add_feature — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `feature.add_feature(file, feature, element)` for projecting, voiding or surface features. Its example first creates a wall and its geometry, then separately creates an IfcOpeningElement, assigns opening geometry and placement, and finally calls add_feature with the existing opening and wall. For the voiding opening shown, the call returns an IfcRelVoidsElement; the documentation describes voiding features as cutting host geometry but does not specify when the Boolean geometry is evaluated. The function does not create the opening element or assign its geometry/placement; the result depends on the selected feature type. The page says semantic openings should be represented distinctly when they have their own meaning.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r10.md.

<a id="src-017b462fd1bf"></a>

## SRC-017b462fd1bf — Stop-button source-readiness result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/readiness.json`)

Summary: Existing source/hash gate returns NEEDS_INPUT foroperator/mounting body andcontact/terminal geometry.

Evidence: executed_readiness_result.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-01a105b9ee75"></a>

## SRC-01a105b9ee75 — imported-records-24.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-24.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-24.json`)

Summary: imported native record snapshot: B7:Insert, B8:Insert, B9:Insert, BA:Insert, BB:Insert, BC:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-021178edf288"></a>

## SRC-021178edf288 — Driver iteration — header.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/header.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/header.json`)

Summary: Actual driver document header records its millimetre units.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-023374825488"></a>

## SRC-023374825488 — dom-r01.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r01.md](../workflows/details/dom-r01.md)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-027053bdee43"></a>

## SRC-027053bdee43 — https://colmap.github.io/pycolmap/index.html

Original source: [https://colmap.github.io/pycolmap/index.html](https://colmap.github.io/pycolmap/index.html)

Summary: - pycolmap API: https://colmap.github.io/pycolmap/index.html

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-0287d1d4de8a"></a>

## SRC-0287d1d4de8a — https://github.com/colmap/colmap

Original source: [https://github.com/colmap/colmap](https://github.com/colmap/colmap)

Summary: - COLMAP repository (scope and license): https://github.com/colmap/colmap

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/cad-sources.json, research/sources/round-02/reconstruction-sources.json, research/workflows/details/cad-r06.md.

<a id="src-0308beb80af5"></a>

## SRC-0308beb80af5 — P01 p01-build-01 — rail-doc-schema-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-doc-schema-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-doc-schema-0.json`)

Summary: p01-build-01 rail-doc-schema-0.json: Installed API response unknown_operation: Unknown operation; retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-031b438ece44"></a>

## SRC-031b438ece44 — Leaf iteration — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/result.json`)

Summary: Completed Leaf iteration records 29 native checks, unchanged model hash, audit/persistence, inspected source/model views and applied checker/shared reader with 44 tests.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-03256efc5e07"></a>

## SRC-03256efc5e07 — SKILL.md

Original source: ${CODEX_HOME}/skills/ocs-engineering/SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-0347392e2577"></a>

## SRC-0347392e2577 — BIM Library docs

Original source: [https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html](https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html)

Summary: FreeCAD BIM Library ; FreeCAD BIM can browse and insert FCStd, STEP and BREP entries from the FreeCAD Parts Library, either offline or through its experimental online library option. BIM Library docs, Parts Library repository ; The BIM insertion feature does not change the license of inserted assets. The Parts Library collection is listed as CC-BY-3.0 in FreeCAD Addons; verify individual item attribution and embedded files. Many entries are generic architecture/MEP objects, not certified building product specifications.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r07.md, research/workflows/domain-paths.md.

<a id="src-035204d4e7eb"></a>

## SRC-035204d4e7eb — Driver iteration — reopened-audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-audit.json`)

Summary: Saved derivative audit preserves116 solids/eight text labels and zero errors/warnings.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-0374f064147a"></a>

## SRC-0374f064147a — pcl::SACSegmentationFromNormals<PointT, PointNT> Class Template Reference — Point Cloud Library 1.15.1-dev

Original source: [https://pointclouds.org/documentation/classpcl_1_1_s_a_c_segmentation_from_normals.html](https://pointclouds.org/documentation/classpcl_1_1_s_a_c_segmentation_from_normals.html)

Summary: The PCL API documents normal-based sample-consensus segmentation, input point cloud and normal cloud, and segment(PointIndices&, ModelCoefficients&) outputs. It describes normal-distance weighting and inherited consensus controls including method, maximum iterations, probability, distance threshold, radius limits and axis/angle constraints. This is API documentation, not a local runtime result.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-independent.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-038ae5e03363"></a>

## SRC-038ae5e03363 — source-placement-plan.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/source-placement-plan.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/source-placement-plan.json`)

Summary: 28 STEP source frames and27 unique inverse-matched native insert corrections.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-03adf43b9941"></a>

## SRC-03adf43b9941 — Kelly KLS7240N controller (C015) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c015-kelly-kls7240n-controller.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c015-kelly-kls7240n-controller.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind exact controller candidate record. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-03ea53a6f519"></a>

## SRC-03ea53a6f519 — OpenCV 4.13 Camera Calibration

Original source: [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)

Summary: Known target object coordinates and corresponding image detections support intrinsic/distortion calibration; tutorial recommends at least ten pattern views. Calibration does not set the scale of an unrelated monocular reconstruction.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r03.md.

<a id="src-04350e8a74da"></a>

## SRC-04350e8a74da — local-inventory.json

Original source: [${MODELING_ROOT}/research/local-inventory.json](../local-inventory.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-04583314396e"></a>

## SRC-04583314396e — ME0907 save and reopen receipt

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/persistence.json`)

Summary: Records matching saved DWG hash and audit manifest, zero audit errors/warnings and recovery of the original reopen operation after its polling bound.

Evidence: executed_persistence_result.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-045e4e413150"></a>

## SRC-045e4e413150 — P02 crossmember — interface-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/interface-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/interface-checks.json`)

Summary: Actual saved crossmember span260mm equals340mm sourced outside frame width minus twice actual rail width40mm; local midpoint Z130mm also passes.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-047ea9576020"></a>

## SRC-047ea9576020 — dom-r03.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r03.md](../workflows/details/dom-r03.md)

Summary: Existing local source cited by point 06 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-056984789982"></a>

## SRC-056984789982 — MuJoCo overview

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst)

Summary: Primary descriptions of units, inertial/body frames, mesh inputs, convex collision geometry and model representations.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-05a74004d0aa"></a>

## SRC-05a74004d0aa — earthtojake/text-to-cad

Original source: [https://github.com/earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

Summary: earthtojake/text-to-cad ; Code-defined parametric models with `cadgen`/build123d, saved-file measurement and preview ; Assess pinned runtime/bootstrap, telemetry, source conventions and output checks. The separately advertised `step-parts` skill searches a component catalogue.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-05baf05685b3"></a>

## SRC-05baf05685b3 — component_records.py

Original source: [${MODELING_ROOT}/scripts/component_records.py](../../scripts/component_records.py)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: authored_document_or_code_inspected, local_implementation_or_execution_record_inspected, local_source_or_executed_inspection.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-17/source-intake-sources.json, research/sources/round-18/dxf-inspection-sources.json.

<a id="src-0697ecbb0ad0"></a>

## SRC-0697ecbb0ad0 — document-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/document-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/document-checkpoint.json`)

Summary: Newisolateddocument84binding,revisionandrequestnamespacebeforeenclosureimport.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-06c5ba590bdd"></a>

## SRC-06c5ba590bdd — Completed crossmember iteration report

Original source: [${MODELING_ROOT}/execution/p02-crossmember.md](../../execution/p02-crossmember.md)

Summary: Records source-ready260mm crossmember, isolated document72/reopened73, five pre-save and six reopened groups, two nominal interface/datum checks, inspected views and the applied shared-helper improvement.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-071deb628e4d"></a>

## SRC-071deb628e4d — Caster support arm (P06) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p06-caster-support-arm.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p06-caster-support-arm.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Removable support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-0724f34c3f7f"></a>

## SRC-0724f34c3f7f — reconstruction-detail-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-03/reconstruction-detail-sources.json](round-03/reconstruction-detail-sources.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-075213db418c"></a>

## SRC-075213db418c — step-format.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/step-format.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/step-format.json`)

Summary: Actual import dialog STEP-format selection result.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-081496ab4ae6"></a>

## SRC-081496ab4ae6 — SKF iteration — capture-top.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/capture-top.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/capture-top.json`)

Summary: Completed native top capture response binds derivative document75 to the inspected two-slot/bearing projection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-082d081b5a44"></a>

## SRC-082d081b5a44 — Driver iteration — capture-front.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/capture-front.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/capture-front.json`)

Summary: Completed front capture response binds actual driver document78 and its inspected front projection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-0868c7d42c7e"></a>

## SRC-0868c7d42c7e — Point 02 visual, semantic and evidence-merge review

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-02-visual.md](../action-audit/reviews/point-02-visual.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-0895e33945c4"></a>

## SRC-0895e33945c4 — Executed axial motor procedure

Original source: [${MODELING_ROOT}/skills/component-cad/references/axial-motor.md](../../skills/cad-ocs-engineering/references/axial-motor.md)

Summary: Documents source-leader review, explicit keyway reconstruction, bounded native construction, surface-based dimensions, save/reopen recovery and per-feature downstream handoffs established by this actual motor.

Evidence: executed_procedure_documentation.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-08989edb31e4"></a>

## SRC-08989edb31e4 — first action plan

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/first-action-plan.md](../action-audit/implementation-queue/first-action-plan.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected, local_source_inspected, local_implementation_or_execution_record_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-07/parts-catalogue-sources.json, research/sources/round-17/source-intake-sources.json.

<a id="src-08a4605c6182"></a>

## SRC-08a4605c6182 — ME0907 component feature-stage state

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/result.json`)

Summary: Mechanical interfaces are saved with18 passing checks. Exterior source lookup is complete; cooling-slot, terminal and connector geometry have a named required input, with manufacturer and supplier evidence linked.

Evidence: executed_component_stage_record.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-0910720e555c"></a>

## SRC-0910720e555c — Point 05 independent procedure review — CAD, photographs and scans alignment

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-05-independent.md](../action-audit/reviews/point-05-independent.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-09342e239988"></a>

## SRC-09342e239988 — Tyro Gemini1S remote-stop receiver (C047) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c047-tyro-gemini1s-remote-stop-receiver.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c047-tyro-gemini1s-remote-stop-receiver.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Separate stop equipment; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-096e1d7af9e5"></a>

## SRC-096e1d7af9e5 — dom-r07.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r07.md](../workflows/details/dom-r07.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-09acefc0b51b"></a>

## SRC-09acefc0b51b — Extracted Pilz SVG linework

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/vector-extraction/pilz-drawing.svg (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/vector-extraction/pilz-drawing.svg`)

Summary: Actual Poppler derivative retains47 paths,including side-profile linework andcase/cover endpoint offsets.

Evidence: executed_source_conversion.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-09f3c0537603"></a>

## SRC-09f3c0537603 — P01 p01-build-01 — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/initial-state.json`)

Summary: p01-build-01 initial-state.json: Observed document 52 revision 2 with open-document identities and camera/command state; used for write isolation or capture provenance.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-0a10e8f57dac"></a>

## SRC-0a10e8f57dac — official OCCT overview

Original source: [https://dev.opencascade.org/doc/overview/html/index.html](https://dev.opencascade.org/doc/overview/html/index.html)

Summary: Primary sources: official OCCT overview, OCCT source repository/licence. Inspected 2026-11-12. Commercial/proprietary uses need licence review against the exact OCCT distribution and linked components; do not assume every wrapper or dependency shares OCCT's terms.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-0a1618ea28ab"></a>

## SRC-0a1618ea28ab — import/export guide

Original source: [https://build123d.readthedocs.io/en/stable/import_export.html](https://build123d.readthedocs.io/en/stable/import_export.html)

Summary: Primary sources: build123d repository/licence, official docs, import/export guide. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-0a1bb25ac612"></a>

## SRC-0a1bb25ac612 — PicoGK project file

Original source: [https://raw.githubusercontent.com/leap71/PicoGK/main/PicoGK.csproj](https://raw.githubusercontent.com/leap71/PicoGK/main/PicoGK.csproj)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: PicoGK project file. Source class: official repository project source, XML text. Original reuse terms: Repository identifies Apache-2.0; project file includes package metadata. Preserve source notices when redistributing.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-0a87ef91b4b8"></a>

## SRC-0a87ef91b4b8 — Stop-button source findings

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/source-notes.md`)

Summary: Exact manufacturer variant,dimension leaders,panel mounting conditions andactual gated CAD routes.

Evidence: delegated_source_review_record.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-0aace313f4cb"></a>

## SRC-0aace313f4cb — Curtis 1243-4303 controller (C014) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c014-curtis-1243-4303-controller.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c014-curtis-1243-4303-controller.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; BT; original kind donor controller reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-0acbe2450bde"></a>

## SRC-0acbe2450bde — SB50 source feature contract

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source-job.json`)

Summary: Pins manufacturer dimensions/hash andtwo named required housing/contact geometry inputs.

Evidence: implementation_input_artifact.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-0ad259094c61"></a>

## SRC-0ad259094c61 — Driver iteration — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/initial-state.json`)

Summary: Actual pre-open OCS state identifies prior Leaf document76 and other open work before driver inspection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-0afc75d0368f"></a>

## SRC-0afc75d0368f — Blender repository/licence

Original source: [https://github.com/blender/blender](https://github.com/blender/blender)

Summary: Licence details for the upstream source, installed package and MCP integrations are recorded in domains and components. Primary sources: Blender repository/licence, Python API quickstart, Mesh API. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-0b06ee1720d4"></a>

## SRC-0b06ee1720d4 — reopened-top.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-top.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-top.png`)

Summary: Actualsavedtopviewshowscover,lockandexternalkeyholefeet.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-0b5ad789671d"></a>

## SRC-0b5ad789671d — Ohmite TA-series package datasheet copy

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/Ohmite-TA-Series-DigiKey-copy.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/Ohmite-TA-Series-DigiKey-copy.pdf`)

Summary: Manufacturer-authored PDF retained from DigiKey. Page50 TA310PA row gives25.4mm length/height and7.62mm pitch; PA diagram identifies pin section and terminal/clip callouts.

Evidence: downloaded_original.

Documents: research/sources/round-20/component-sources.json.

<a id="src-0bc5d8f02292"></a>

## SRC-0bc5d8f02292 — Trelleborg T539 tyre (C001) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c001-trelleborg-t539-tyre.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c001-trelleborg-t539-tyre.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Common wheel reference; original kind manufacturer specification recorded locally. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-0c098ecd90ed"></a>

## SRC-0c098ecd90ed — Local tool and source baseline

Original source: [${MODELING_ROOT}/research/local-baseline.md](../local-baseline.md)

Summary: Inspected in this research turn; records OCS STEP representation finding and environment/source inspection.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-0c559ba0bc9f"></a>

## SRC-0c559ba0bc9f — Upstream COPYING

Original source: [https://github.com/blender/blender/blob/main/COPYING](https://github.com/blender/blender/blob/main/COPYING)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-0cb70285e323"></a>

## SRC-0cb70285e323 — Leaf iteration — capture-top.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/capture-top.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/capture-top.json`)

Summary: Completed top capture response binds document 76, camera and module image for actual visual inspection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-0d1de3da8732"></a>

## SRC-0d1de3da8732 — OCS capture/control source

Original source: ${OCS_ROOT}/src/app/control/mod.rs (`${OCS_ROOT}/src/app/control/mod.rs`)

Summary: Local source describes deferred frame capture andnativeactivate routing;source inspection is separate from installed runtime evidence.

Evidence: inspected_local_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-0d57f06ba877"></a>

## SRC-0d57f06ba877 — Open CASCADE Technology Reference Manual 8.0.1: STEPCAFControl_Reader Class Reference

Original source: [https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___reader.html](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___reader.html)

Summary: The official OCCT API reference describes STEPCAFControl_Reader as importing STEP shapes including assemblies and supporting colors and part names. The documented ReadFile and Transfer operations load STEP content into a DECAF document; Transfer can read all roots or one root and can compose multiple results as an assembly. Name and color modes are enabled by default in the documented constructor and can be controlled. The dev.opencascade.org URL redirected to the OCCT3D-hosted 8.0.1 manual. This documents API capability, not a local build, unit outcome, or tested preservation result.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-sources.md, research/sources/round-05/point-02-web-sources.json.

<a id="src-0d6d9bc1a30b"></a>

## SRC-0d6d9bc1a30b — https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html

Original source: [https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html](https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html)

Summary: Four direct page attempts did not yield page contents: ROS Rolling URDF tutorial (`https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html`, access denied by Anubis); ROS REP-103 mirror (`https://www.ros.org/reps/rep-0103.html`, access denied by Anubis; the source-controlled REP page was inspected successfully instead); Blender glTF manual (`https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html`, HTTP 402); and guessed IfcOpenShell geometry-settings URL (`https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html`, unavailable via the web tool). These failed attempts support no technical claim. Existing source-register records were reused for MuJoCo/IfcOpenShell/CoACD licensing and earlier workflow descriptions; they are not counted as fresh inspection. No local runtime or implementation capability is established by this source audit.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-06-sources.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-0da51768e908"></a>

## SRC-0da51768e908 — Leaf iteration — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/initial-state.json`)

Summary: Native pre-open state identifies SKF document 75 and unrelated open work before opening the Leaf drawing.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-0db17291beb9"></a>

## SRC-0db17291beb9 — Source-intake fidelity and failure tests

Original source: [${MODELING_ROOT}/tests/test_source_intake.py](../../tests/test_source_intake.py)

Summary: Twelve passing cases cover sources, corrections, changed revisions, zero-network URL registration, invalid records, interrupted publication and protected earlier artifacts. Final reference checks reject repeated conflict identities.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-0de1ce69cd32"></a>

## SRC-0de1ce69cd32 — Initial delegated resistor transcription

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/source-notes-initial.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/source-notes-initial.md`)

Summary: Preserved original research notes include general-dimensional-tolerance and no-scale statements excluded by coordinator review of the retained PDF. Package-table dimensions remain attributed to TA310PA. Actual researcher runtime identity unavailable.

Evidence: initial_transcription_with_reviewed_corrections.

Documents: research/sources/round-20/component-sources.json.

<a id="src-0df55f79b2d5"></a>

## SRC-0df55f79b2d5 — https://www.ros.org/reps/rep-0103.html

Original source: [https://www.ros.org/reps/rep-0103.html](https://www.ros.org/reps/rep-0103.html)

Summary: Four direct page attempts did not yield page contents: ROS Rolling URDF tutorial (`https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html`, access denied by Anubis); ROS REP-103 mirror (`https://www.ros.org/reps/rep-0103.html`, access denied by Anubis; the source-controlled REP page was inspected successfully instead); Blender glTF manual (`https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html`, HTTP 402); and guessed IfcOpenShell geometry-settings URL (`https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html`, unavailable via the web tool). These failed attempts support no technical claim. Existing source-register records were reused for MuJoCo/IfcOpenShell/CoACD licensing and earlier workflow descriptions; they are not counted as fresh inspection. No local runtime or implementation capability is established by this source audit.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-06-sources.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-0e057ef39322"></a>

## SRC-0e057ef39322 — CadQuery documentation

Original source: [https://cadquery.readthedocs.io/en/stable/](https://cadquery.readthedocs.io/en/stable/)

Summary: Official CadQuery documentation describes Python parametric CAD scripting and supported imports/exports; native Python source carries its parametric construction record.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-visual.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/cad-r06.md, research/workflows/details/cad-r07.md, research/workflows/details/cad-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md.

<a id="src-0ecb978bb734"></a>

## SRC-0ecb978bb734 — Driver iteration — capture-side.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/capture-side.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/capture-side.json`)

Summary: Completed side capture response binds document78 and inspected housing/connector height view.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-0f1f289478e2"></a>

## SRC-0f1f289478e2 — Wheel splash panel (P24) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p24-wheel-splash-panel.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p24-wheel-splash-panel.md`)

Summary: Input sheet registered from the inspected ferme manifest: guards; Common withroute-specificshape; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-0fe51d659523"></a>

## SRC-0fe51d659523 — Manufacturer Harmony XB5 catalogue

Original source: [https://iportal.se.com/Contents/docs/HARMONY%20XB5_CATALOG.PDF](https://iportal.se.com/Contents/docs/HARMONY%20XB5_CATALOG.PDF)

Summary: Printed44/PDF45 explicitly mapsXB5AS8445 toZB5AZ105 contact body andZB5AS844 head,1NO+1NC andturn release.

Evidence: downloaded_original.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-106d47161026"></a>

## SRC-106d47161026 — Gland source feature contract

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source-job.json`)

Summary: Pins exactmanufacturer page findings through acquisition hash andnames three required geometry inputs.

Evidence: implementation_input_artifact.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-10fb35c8f807"></a>

## SRC-10fb35c8f807 — Python API quickstart

Original source: [https://docs.blender.org/api/current/info_quickstart.html](https://docs.blender.org/api/current/info_quickstart.html)

Summary: Licence details for the upstream source, installed package and MCP integrations are recorded in domains and components. Primary sources: Blender repository/licence, Python API quickstart, Mesh API. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-115e3fe90a0c"></a>

## SRC-115e3fe90a0c — c029_feature_checks.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/c029_feature_checks.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/c029_feature_checks.py`)

Summary: Measuredsourcebody/covermembersagainst3drawingdimensionsandchecked12closedshellgraphs.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-1179a9bfdd5a"></a>

## SRC-1179a9bfdd5a — Victron supported shelf (P19) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p19-victron-supported-shelf.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p19-victron-supported-shelf.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Victron or BT-V; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-1195ea9b1b28"></a>

## SRC-1195ea9b1b28 — Wheel shaft bearing support plate (P13) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p13-wheel-shaft-bearing-support-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p13-wheel-shaft-bearing-support-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-11a3ab01c356"></a>

## SRC-11a3ab01c356 — Project workflow composition rules

Original source: [${MODELING_ROOT}/research/workflows/composition-rules.md](../workflows/composition-rules.md)

Summary: Project proposal defining sequences, branches, evidence merges, component substitution, representation forks and revisioned edit/compare loops, with explicit handoff conditions and research questions.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/project-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-11b52766dd34"></a>

## SRC-11b52766dd34 — Local Python 3.14 hashlib source

Original source: ${SYSTEM_ROOT}/usr/lib/python3.14/hashlib.py (`${SYSTEM_ROOT}/usr/lib/python3.14/hashlib.py`)

Summary: Documented byte hashing and SHA-256 constructors used as source evidence for input revision identity.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json.

<a id="src-11c693014725"></a>

## SRC-11c693014725 — Source-bound axial motor construction and checker

Original source: [${MODELING_ROOT}/scripts/axial_motor.py](../../scripts/axial_motor.py)

Summary: New Python recipe calls existing guarded native geometry for housing/pilot, blind patterns, keyed shaft and rear region. Checks analytic cylinders and individual blind-bottom planes instead of estimating circle diameter from seam vertices.

Evidence: implementation_artifact.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-11f42e602b33"></a>

## SRC-11f42e602b33 — `freecad-developer/SKILL.md`

Original source: [https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-developer/SKILL.md](https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-developer/SKILL.md)

Summary: FreeCAD skills suite (`glotoff/freecad-skills`) ; Archived `freecad-user/SKILL.md` routes UI/modeling/workbench/import-export and topological naming guidance; `freecad-power-user/SKILL.md` covers Python, Part/Sketcher/Draft, B-rep, FeaturePython and headless/RPC automation; `freecad-developer/SKILL.md` covers C++ build/workbench development. README says skills derive from official FreeCAD documentation. Root skill suite licence is MIT; copied FreeCAD docs have separate attribution/licensing. ; Adapt `freecad-user` and `freecad-power-user` selectively as a complementary parametric backend; `developer` is outside normal modeling scope. The supplied suite is knowledge guidance, not tested evidence that generated files meet requirements. Source links: `freecad-user/SKILL.md`, `freecad-power-user/SKILL.md`, `freecad-developer/SKILL.md`. Archived local files were inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-1273100b3546"></a>

## SRC-1273100b3546 — SOLIDWORKS help

Original source: [https://help.solidworks.com/2022/english/SolidWorks/sldworks/r_3d_contentcentral.htm?id=12.6.2.0](https://help.solidworks.com/2022/english/SolidWorks/sldworks/r_3d_contentcentral.htm?id=12.6.2.0)

Summary: 3D ContentCentral ; Supplier-certified and user library models in multiple CAD formats. SOLIDWORKS help ; Platform access requires agreement; contributor terms give the platform broad indexing/adaptation/distribution rights but do not establish a blanket open license for each downloaded model. Record per-item license/terms; do not treat the catalog as open data. Contributor terms

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-12a05a05db24"></a>

## SRC-12a05a05db24 — SB50 contact source image

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/sb50-datasheet-page-2.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/sb50-datasheet-page-2.png`)

Summary: Actual page2 shows30mm contact overall,11.1 axial segment,7.2 barrel profile and5900 A5.59 table row.

Evidence: derived_pdf_render.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-1341a6b69ecb"></a>

## SRC-1341a6b69ecb — AGENTS.md

Original source: ${FERME_ROOT}/AGENTS.md (`${FERME_ROOT}/AGENTS.md`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected.

Documents: research/local-baseline.md, research/sources/local-evidence.json.

<a id="src-134b4e103e48"></a>

## SRC-134b4e103e48 — OpenMVG documentation: OpenMVS stages

Original source: [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/)

Summary: OpenMVS imports an OpenMVG scene and runs DensifyPointCloud, ReconstructMesh and TextureMesh as separate command-line stages.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r06.md.

<a id="src-1361cced4e93"></a>

## SRC-1361cced4e93 — 520 roller chain (C007) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c007-520-roller-chain.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c007-520-roller-chain.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907 chain example; original kind source size family. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-13e9587720a2"></a>

## SRC-13e9587720a2 — Fuse source-readiness gate

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/readiness.json`)

Summary: Existing source/hash validation returns NEEDS_INPUT with thethree required geometry questions and actual retained-source observations.

Evidence: executed_readiness_result.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-13f08bab005f"></a>

## SRC-13f08bab005f — source repository/licence

Original source: [https://github.com/openscad/openscad](https://github.com/openscad/openscad)

Summary: Primary sources: official documentation, language reference, source repository/licence. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-144b4a816641"></a>

## SRC-144b4a816641 — cad-r09.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r09.md](../workflows/details/cad-r09.md)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-14d64147c232"></a>

## SRC-14d64147c232 — XB5AS8445 mounting render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/schneider-xb5as8445-page-4.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/schneider-xb5as8445-page-4.png`)

Summary: Actual panel-cutout image givesØ22.3+0.4/0 recommended22.5,lug3.2+0.2/0,24.1+0.4/0 height,r≤0.8 andscrew-clamp40/30 spacing.

Evidence: derived_pdf_render.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-15006ce1a525"></a>

## SRC-15006ce1a525 — Stop-button source-stage report

Original source: [${MODELING_ROOT}/execution/c049-stop-button-source.md](../../execution/c049-stop-button-source.md)

Summary: Documents exact assembly mapping,finished panel tolerances,source access outcomes andseparate panel/full-body actions.

Evidence: executed_work_report.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-158c2c4848c2"></a>

## SRC-158c2c4848c2 — AGENTS.md — energy project instructions

Original source: ${ENERGY_ROOT}/AGENTS.md (`${ENERGY_ROOT}/AGENTS.md`)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: AGENTS.md — energy project instructions. Source class: project research and communication instructions. Original reuse terms: Local instructions; referenced in place without duplication.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-15f1b4d0281d"></a>

## SRC-15f1b4d0281d — Leaf iteration — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/ocs-journal.jsonl`)

Summary: Guarded requests retain the original Leaf open polling-bound result and same-ID recovery, followed by actual top, terminal-end and isometric view/capture operations.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-16d2d9b6a0cb"></a>

## SRC-16d2d9b6a0cb — P01 p01-build-01 — rail-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-state.json`)

Summary: p01-build-01 rail-state.json: Observed document 52 revision 2 with open-document identities and camera/command state; used for write isolation or capture provenance.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-170cae45c8e7"></a>

## SRC-170cae45c8e7 — Leaf cassette support rail (P17R) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p17r-leaf-cassette-support-rail.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p17r-leaf-cassette-support-rail.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Leaf; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-172ac1af7b52"></a>

## SRC-172ac1af7b52 — Pilz PNOZX3 774310 relay (C048) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c048-pilz-pnozx3-774310-relay.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c048-pilz-pnozx3-774310-relay.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Stop equipment; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-172fdcc953c4"></a>

## SRC-172fdcc953c4 — The model contract and STEP generation

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/step-generation.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/step-generation.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: The model contract and STEP generation. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-17542ff2880d"></a>

## SRC-17542ff2880d — Project skill catalogue

Original source: [${MODELING_ROOT}/skills/README.md](../../skills/README.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected, authored_document_or_code_inspected, local_implementation_or_execution_record_inspected, local_source_or_executed_inspection.

Documents: research/sources/round-05/audit-index-sources.json, research/sources/round-09/component-execution-sources.json, research/sources/round-17/source-intake-sources.json, research/sources/round-18/dxf-inspection-sources.json.

<a id="src-17a777175a39"></a>

## SRC-17a777175a39 — Four observed component-source action definitions

Original source: [${MODELING_ROOT}/research/action-audit/component-source-actions.json](../action-audit/component-source-actions.json)

Summary: Defines stock/supplier lookup, feature-standard search, per-claim access review and nominal feature calculation, including software/agent roles, units, preserved information, alternatives and downstream conditions. Links original intake/solid-route actions and the FERME occurrence registry.

Evidence: authored_code_or_procedure_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-17d541c31dfa"></a>

## SRC-17d541c31dfa — Source-vector reconstruction proposal

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/vector-extraction/procedure.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/vector-extraction/procedure.md`)

Summary: Separates actual PDF-to-SVG extraction fromproposed source-view selection,unit checks,joining/part-boundary rules andnative extrusion.

Evidence: proposal_linked_to_executed_extraction.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-18305cb33c69"></a>

## SRC-18305cb33c69 — Source-bound pillow-block checker

Original source: [${MODELING_ROOT}/scripts/pillow_block.py](../../scripts/pillow_block.py)

Summary: Reads ten exact metadata-labelled native parts and compares housing, slots, shaft, ring, screw, seals and fitting against externally pinned source features; original crown fails and corrected reopened derivative passes62checks.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json.

<a id="src-184a5ba4315f"></a>

## SRC-184a5ba4315f — imported-records-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-0.json`)

Summary: importednativeentitysnapshot: 81:Solid3D, 85:Solid3D, 89:Solid3D, 8D:Solid3D, 91:Solid3D, 95:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-19255db776eb"></a>

## SRC-19255db776eb — MCP Market 3D Modeling Specialist

Original source: [https://mcpmarket.com/tools/skills/3d-modeling-specialist](https://mcpmarket.com/tools/skills/3d-modeling-specialist)

Summary: MCP Market 3D Modeling Specialist ; Listing by Kedhareswer: game/film art workflow covering quad topology, UV unwrapping, texel density, baking, retopology, LOD and Blender/Maya/ZBrush. It reports 0 GitHub stars and an install path `kedhareswer/kedhar_brain`, skill `3d-modeling`. ; Mesh/art skill, not mechanical CAD. Listing page inspected. Upstream source SKILL.md, licence and service requirements were not retrieved, so listing description is not treated as verified code behavior.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-194cc6d76652"></a>

## SRC-194cc6d76652 — ezdxf1.4.5 native SAB decoder source

Original source: ${NATIVE_READER_ROOT}/ezdxf/acis/sab.py (`${NATIVE_READER_ROOT}/ezdxf/acis/sab.py`)

Summary: MIT library source implements typed binary token decoding, versioned record construction and pointer resolution through parse_sab. Its existing parser reads the saved P01 binary record without changing CAD geometry.

Evidence: local_execution_evidence_inspected, local_source_or_execution_record_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-14/bearing-sources.json.

<a id="src-196d24be8370"></a>

## SRC-196d24be8370 — Installed MIT-licensed DXF units mapping

Original source: ${NATIVE_READER_ROOT}/ezdxf/units.py (`${NATIVE_READER_ROOT}/ezdxf/units.py`)

Summary: Inspected decode maps actual INSUNITS enum codes to unit labels. The inspector preserves code0 as unresolved unit evidence and actual code6 as metres.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-199449a3713f"></a>

## SRC-199449a3713f — Fibox source acquisition metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/acquisition.json`)

Summary: Records3exactmanufacturer-linkedGETresults,timestamps,MIME,sizes,hashes andderivedpreviews.

Evidence: executed_acquisition_record.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-19a03b5f035d"></a>

## SRC-19a03b5f035d — blender-modeling — roble3/cc-blender-skill

Original source: [https://www.skills.sh/roble3/cc-blender-skill/blender-modeling](https://www.skills.sh/roble3/cc-blender-skill/blender-modeling)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: blender-modeling — roble3/cc-blender-skill. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-19e1d74855d9"></a>

## SRC-19e1d74855d9 — ME0907 supported wheel shaft (P12) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p12-me0907-supported-wheel-shaft.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p12-me0907-supported-wheel-shaft.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-1a05e425438e"></a>

## SRC-1a05e425438e — REP-103: Standard Units of Measure and Coordinate Conventions — ros-infrastructure/rep master

Original source: [https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst)

Summary: ROS REP source page accessed 2026-11-12. Repository page says archived October 23, 2025; REP text labels itself Active/Informational. Specifies SI metre, kilogram, second; radian; right-handed frames; body x-forward/y-left/z-up; optical z-forward/x-right/y-down. Branch is mutable.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-1a10c8033611"></a>

## SRC-1a10c8033611 — reconstruction-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-02/reconstruction-sources.json](round-02/reconstruction-sources.json)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-1a2bd5aac217"></a>

## SRC-1a2bd5aac217 — execution record

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/execution-record.md](../action-audit/implementation-queue/execution-record.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-1a9d2f4c6a7a"></a>

## SRC-1a9d2f4c6a7a — assets

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/assets.md](../action-audit/implementation-queue/assets.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-1ae836243bfc"></a>

## SRC-1ae836243bfc — P01 p01-build-01 — rail-after-cut-measure.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-after-cut-measure.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-after-cut-measure.json`)

Summary: p01-build-01 rail-after-cut-measure.json: Retained native response with fields document_id, geometry_revision, measurements, ok; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-1b0d9fc7bcf8"></a>

## SRC-1b0d9fc7bcf8 — manifest.tsv

Original source: ${FERME_ROOT}/research/base-component-completion-2026-11-12/sources-frame/manifest.tsv (`${FERME_ROOT}/research/base-component-completion-2026-11-12/sources-frame/manifest.tsv`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-10/tube-corner-sources.json.

<a id="src-1b1ca9a7f6a5"></a>

## SRC-1b1ca9a7f6a5 — start_c029.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/start_c029.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/start_c029.py`)

Summary: Createdisolateddocument84andimportedhash-pinnedmanufacturerSTEPwithsuccessfulnativeImportFilefields.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-1b2c3957498a"></a>

## SRC-1b2c3957498a — OCCT source repository/licence

Original source: [https://github.com/Open-Cascade-SAS/OCCT](https://github.com/Open-Cascade-SAS/OCCT)

Summary: Primary sources: official OCCT overview, OCCT source repository/licence. Inspected 2026-11-12. Commercial/proprietary uses need licence review against the exact OCCT distribution and linked components; do not assume every wrapper or dependency shares OCCT's terms.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-1b3804492890"></a>

## SRC-1b3804492890 — P01 p01-build-02 — document-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/document-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/document-checkpoint.json`)

Summary: p01-build-02 document-checkpoint.json: Binds partial/native stage to document 69, revision 0 and named part handles {}; supports inspected recovery.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-1be5a18aa751"></a>

## SRC-1be5a18aa751 — https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html

Original source: [https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html](https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html)

Summary: - Meshroom hardware requirements (legacy version; treat numbers as historical): https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-1bf6e9a12d73"></a>

## SRC-1bf6e9a12d73 — dom-r06.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r06.md](../workflows/details/dom-r06.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-1c03ba612505"></a>

## SRC-1c03ba612505 — Pinned native-reader dependency environment

Original source: [${MODELING_ROOT}/requirements-native.txt](../../requirements-native.txt)

Summary: Pins ezdxf1.4.5 and the observed fonttools4.68.0/numpy2.5.4/pyparsing3.3.3/typing_extensions4.16.0 dependencies installed in isolated temporary target. This pin set was exercised with Python3.12.9.

Evidence: local_execution_evidence_inspected, local_source_or_executed_inspection.

Documents: research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-18/dxf-inspection-sources.json.

<a id="src-1c1ff9274d77"></a>

## SRC-1c1ff9274d77 — SKF iteration — audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/audit.json`)

Summary: Original ten-solid native audit has zeroerrors/warnings; geometric source comparison subsequently finds crown dimension failure.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-1c30dee16aac"></a>

## SRC-1c30dee16aac — Shared parts catalogue discussion

Original source: [${MODELING_ROOT}/research/action-audit/parts-catalogue-proposal.md](../action-audit/parts-catalogue-proposal.md)

Summary: Authored proposal: requested identity/standards/location/search fields, storage alternatives and explicit future material/resistance/work-domain extensions.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-07/parts-catalogue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-1d0764f851b0"></a>

## SRC-1d0764f851b0 — Battery exterior iteration result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/result.json`)

Summary: New native battery file,source frame,21 definitions/39 instances,actual checks,source dimensional observations,inspected views and applied reusable improvement linked by path/hash.

Evidence: executed_component_result.

Documents: research/sources/round-20/component-sources.json.

<a id="src-1d41a99d4236"></a>

## SRC-1d41a99d4236 — Anderson SB50 manufacturer datasheet

Original source: [https://p1.aprimocdn.net/idealindustries/d7c0a682-e691-4b60-8e76-b3f000737d74/ap-web_product-assets_default_data-sheets_ds-sb50_Original%20file.pdf](https://p1.aprimocdn.net/idealindustries/d7c0a682-e691-4b60-8e76-b3f000737d74/ap-web_product-assets_default_data-sheets_ds-sb50_Original%20file.pdf)

Summary: Original DS-SB50 revision9 maps blue992G4 andsilver high-force5900;dimensioned housing,mated pair andwire contacts.

Evidence: downloaded_original.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-1d9ccefff7d7"></a>

## SRC-1d9ccefff7d7 — SKF iteration — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/ocs-journal.jsonl`)

Summary: Append-only guarded requests retain original-open/reopen polling-bound outcomes and same-ID recovery, two housingSLICE commands, verifiedsave and actual captures.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-1dbeea3c6e30"></a>

## SRC-1dbeea3c6e30 — Full Fibox dimension drawing render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-8121020-drawing-page-1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-8121020-drawing-page-1.png`)

Summary: Actualrear/sectiondrawingviewwith300×200body,152.5depth,10footprojection andwall/covercallouts.

Evidence: derived_pdf_render.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-1df8ac8c2937"></a>

## SRC-1df8ac8c2937 — imported-records-6.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-6.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-6.json`)

Summary: imported native record snapshot: 99:Solid3D, 9D:Solid3D, A1:Solid3D, A5:Solid3D, A9:Insert, AA:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-1e8dca4fc3d4"></a>

## SRC-1e8dca4fc3d4 — Axial motor failure regression cases

Original source: [${MODELING_ROOT}/tests/test_axial_motor.py](../../tests/test_axial_motor.py)

Summary: Eight focused software tests exercise seam-only vertices, missing hole, swapped depths, wrong blind depth, wrong keyway floor, wrong diameter, invalid extents and unit/overrun rejection.

Evidence: implementation_test_artifact.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-1eac959ecbf4"></a>

## SRC-1eac959ecbf4 — P01 p01-build-03 — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/persistence.json`)

Summary: p01-build-03 persistence.json: DWG2018 save/reopen audit/hash/manifest result PASS, one native solid, zero dropped entities. Detailed reopened geometry has its own separate receipt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-1eb8186891cc"></a>

## SRC-1eb8186891cc — reopened-records-6.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-6.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-6.json`)

Summary: reopened native record snapshot: 99:Solid3D, 9D:Solid3D, A1:Solid3D, A5:Solid3D, A9:Insert, AA:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-1f314fe4accc"></a>

## SRC-1f314fe4accc — raster_image.rs

Original source: ${OCS_ROOT}/src/modules/draw/draw/raster_image.rs (`${OCS_ROOT}/src/modules/draw/draw/raster_image.rs`)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-1f361eaafa20"></a>

## SRC-1f361eaafa20 — Earlier SKF part record

Original source: ${FERME_ROOT}/engineering/module-development/parts/mechanical-connections/skf-sy-20-tf.md (`${FERME_ROOT}/engineering/module-development/parts/mechanical-connections/skf-sy-20-tf.md`)

Summary: Supplies component identity and source relationships; its0.588kg figure differs from the retained technical sheet0.56kg, registered as a source finding without changing the record.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-1f4431787dd4"></a>

## SRC-1f4431787dd4 — https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html)

Summary: Four direct page attempts did not yield page contents: ROS Rolling URDF tutorial (`https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html`, access denied by Anubis); ROS REP-103 mirror (`https://www.ros.org/reps/rep-0103.html`, access denied by Anubis; the source-controlled REP page was inspected successfully instead); Blender glTF manual (`https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html`, HTTP 402); and guessed IfcOpenShell geometry-settings URL (`https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html`, unavailable via the web tool). These failed attempts support no technical claim. Existing source-register records were reused for MuJoCo/IfcOpenShell/CoACD licensing and earlier workflow descriptions; they are not counted as fresh inspection. No local runtime or implementation capability is established by this source audit.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-06-sources.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-1f466f80fd41"></a>

## SRC-1f466f80fd41 — Point cloud — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html)

Summary: Open3D 0.20.0 documents `segment_plane(distance_threshold, ransac_n, num_iterations)` returning plane coefficients and inlier indices; the distance threshold is in point-cloud coordinate units. It also documents `cluster_dbscan(eps, min_points)` returning labels, with -1 for noise. These routines report sampled point subsets and geometric candidates; they do not classify engineering features or report parameter uncertainty.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r04.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r07.md, research/workflows/details/rec-r10.md.

<a id="src-1f8a84e3e367"></a>

## SRC-1f8a84e3e367 — Fuse exact-part outline lookup

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/source-notes.md`)

Summary: Retains manufacturer datasheet URL/revision,shared M6 suffix applicability,reported dimension labels and exact acquisition outcomes.60/42 leader associations remain named geometry inputs.

Evidence: delegated_web_review_record.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-1f99e1c91c5c"></a>

## SRC-1f99e1c91c5c — imported-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-isometric.png`)

Summary: Actual converter capture attempt imported-isometric;image repeats the previous Fibox enclosure. Included as failed visual evidence,withhash comparison in capture-identity-checks.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-1fe1bf3380df"></a>

## SRC-1fe1bf3380df — https://github.com/openMVG/openMVG

Original source: [https://github.com/openMVG/openMVG](https://github.com/openMVG/openMVG)

Summary: - OpenMVG repository and license: https://github.com/openMVG/openMVG

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md.

<a id="src-1fe7a6d498a1"></a>

## SRC-1fe7a6d498a1 — imported-records-18.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-18.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-18.json`)

Summary: imported native record snapshot: B1:Insert, B2:Insert, B3:Insert, B4:Insert, B5:Insert, B6:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-20296fc40b95"></a>

## SRC-20296fc40b95 — SKF iteration — original-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/original-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/original-checks.json`)

Summary: Actual original native geometry produces61PASS and crownFAIL32mmversus21mm; preserves measured defect before revision.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-20676393d92d"></a>

## SRC-20676393d92d — SKF iteration — presave-correction-check.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/presave-correction-check.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/presave-correction-check.json`)

Summary: Post-cut crown21mmPASS and byteidentical nine other solid geometry records recorded before derivative save.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-208dce2b3f17"></a>

## SRC-208dce2b3f17 — Saved battery inspection and source-bound check procedure

Original source: [${MODELING_ROOT}/skills/component-cad/references/existing-battery.md](../../skills/cad-ocs-engineering/references/existing-battery.md)

Summary: Details exact source variant, metadata identity, unchanged-file persistence, transformed shell and terminal checks, source/model views and verified shared-reader extraction.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-20a206cdbbd8"></a>

## SRC-20a206cdbbd8 — README.md — evidence_index

Original source: ${FERME_ROOT}/skills/README.md (`${FERME_ROOT}/skills/README.md`)

Summary: Scope, source session/review boundary, OCS build and document use order. Applicability:

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-20b61505fcba"></a>

## SRC-20b61505fcba — SAM 3D Objects — official repository, main branch

Original source: [https://github.com/facebookresearch/sam-3d-objects](https://github.com/facebookresearch/sam-3d-objects)

Summary: Official mutable main repository inspected 2026-11-12. Example loads image and segmentation mask, runs inference, and saves `output["gs"]` as Gaussian splat PLY. The inspected example does not demonstrate triangle-mesh output. License is separately covered by an existing source-register record.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r10.md.

<a id="src-20cfbd87583b"></a>

## SRC-20cfbd87583b — setup/features/security sections

Original source: [https://github.com/ahujasid/mcp-for-blender#limitations--security-considerations](https://github.com/ahujasid/mcp-for-blender#limitations--security-considerations)

Summary: The separate community project ahujasid/mcp-for-blender is explicitly not affiliated with Blender Foundation. Its package metadata declares MIT, and its current README supports Blender 3.0 or newer, so its stated Blender minimum includes the installed 5.0.1. It provides scene/object inspection and mutation, visual inspection, arbitrary Blender Python execution, and external asset integrations such as Poly Haven, Sketchfab and Poly Pizza. This broader feature set also increases the amount of connected code and network access. The repository documents an opt-in `BLENDER_MCP_SAFE_MODE=1`; that mode is a project feature, not an operating-system sandbox. Package metadata, setup/features/security sections.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-20e0d88c245b"></a>

## SRC-20e0d88c245b — Repository

Original source: [https://github.com/nophead/NopSCADlib](https://github.com/nophead/NopSCADlib)

Summary: NopSCADlib ; OpenSCAD library and project framework with a `vitamins` collection of modeled real-world hardware and a `tests` directory. Repository, usage ; GPL-3.0. It is reusable parametric OpenSCAD code and geometry; check whether the intended use is to redistribute library code, generated part files or merely reference it, and retain notices.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md.

<a id="src-20e32f7b4337"></a>

## SRC-20e32f7b4337 — ezdxf documentation

Original source: [https://ezdxf.readthedocs.io/en/stable/](https://ezdxf.readthedocs.io/en/stable/)

Summary: Official ezdxf docs identify it as Python software to create/read/modify/write DXF, state supported DXF revisions, MIT licence and core dependencies.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-221c17026037"></a>

## SRC-221c17026037 — imported-records-6.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-6.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-6.json`)

Summary: importednativeentitysnapshot: 96:Insert, 9A:Solid3D, 9E:Solid3D, 9F:Solid3D, A3:Solid3D, A7:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-2277b3d17f5b"></a>

## SRC-2277b3d17f5b — Pilz source-stage result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/result.json`)

Summary: Connects source gate andexecuted PDF-vector extraction alternative.

Evidence: executed_component_stage_record.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-228e61d4e7a6"></a>

## SRC-228e61d4e7a6 — Resistor source gate result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/readiness.json`)

Summary: Existing source-readiness code reports NEEDS_INPUT for ceramic substrate thickness; source-backed dimensions are retained for later dependent geometry.

Evidence: executed_readiness_result.

Documents: research/sources/round-20/component-sources.json.

<a id="src-22b94e3ef160"></a>

## SRC-22b94e3ef160 — Caster angle-setting pin (C019) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c019-caster-angle-setting-pin.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c019-caster-angle-setting-pin.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Retained fixed-setting arm proposal; original kind pin component geometry input. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-22d386b03b6c"></a>

## SRC-22d386b03b6c — Front attachment support plate (P08) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p08-front-attachment-support-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p08-front-attachment-support-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: attachments; Front mount proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-22fcdfd7f96a"></a>

## SRC-22fcdfd7f96a — Exact XB5AS8445 manufacturer datasheet

Original source: [https://iportal.se.com/Contents/docs/SQD-XB5AS8445.PDF](https://iportal.se.com/Contents/docs/SQD-XB5AS8445.PDF)

Summary: Original exactpart data withpage3 operator/panel projections andpage4 finished cutout tolerances,screw-clamp spacing andclamping range.

Evidence: downloaded_original.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-234298cb79b4"></a>

## SRC-234298cb79b4 — P01 p01-build-03 — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/result.json`)

Summary: p01-build-03 result.json: Observed attempt state BUILT_REOPENED_FEATURE_CHECK_REQUIRED; Read/query reopened SAB feature geometry and repeat the source-linked dimension checks; investigate zero native bounds alongside nonzero mesh and visible geometry.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-23588c0d99a2"></a>

## SRC-23588c0d99a2 — SKF iteration — native-query.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/native-query.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/native-query.json`)

Summary: Original document74 query identifies ten actual solid handles before feature checks and selective revision.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-240fe89d1198"></a>

## SRC-240fe89d1198 — EN 10210-2:2019 (E), SIST sample — Hot finished structural hollow sections, Part 2

Original source: [https://cdn.standards.iteh.ai/samples/38061/b2cb736a37f94d2f8a72c739a042aa44/SIST-EN-10210-2-2019.pdf](https://cdn.standards.iteh.ai/samples/38061/b2cb736a37f94d2f8a72c739a042aa44/SIST-EN-10210-2-2019.pdf)

Summary: EN 10210-2:2019 sample observations exposed rounded internal corners and the stated weld-corner exception in Clause6.2, Table2 default external maximum3T and Clause5.2 Option2.2 purchaser maximum2T. The PDF search-result excerpt exposed AnnexA.3 nominal calculation formulas ro=1.5T and ri=1.0T. At T=3mm the calculation radii are4.5mm/3mm, default external maximum9mm and optional maximum6mm.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-243b037b93ab"></a>

## SRC-243b037b93ab — CAD and skills assessment

Original source: [${MODELING_ROOT}/research/cad-and-skills.md](../cad-and-skills.md)

Summary: Inspected in this research turn; records OCS baseline, CAD representation tradeoffs and alternate authoring backends.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-24ffaaff970e"></a>

## SRC-24ffaaff970e — BMW cell supervision circuit (C053) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c053-bmw-cell-supervision-circuit.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c053-bmw-cell-supervision-circuit.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; BMW; original kind OEM component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-251464b38bc3"></a>

## SRC-251464b38bc3 — CadQuery quickstart

Original source: [https://cadquery.readthedocs.io/en/stable/quickstart.html](https://cadquery.readthedocs.io/en/stable/quickstart.html)

Summary: Primary usage examples for parameterized Python solid construction.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r09.md.

<a id="src-25413f03b05d"></a>

## SRC-25413f03b05d — source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source-job.json`)

Summary: Pins C043 target identity to reviewed source metadata andnames required exact geometry/depth revision inputs.

Evidence: implementation_input_artifact.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-257da81e1cf3"></a>

## SRC-257da81e1cf3 — repair_c045.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/repair_c045.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/repair_c045.py`)

Summary: Applied existing tested placement helper to27 native inserts andchecked nine unchanged solid definitions.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-25f843f2d67d"></a>

## SRC-25f843f2d67d — Kelly archive member 48VCCW.pdf

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/kelly-archive/48VCCW.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/kelly-archive/48VCCW.pdf`)

Summary: Retained original48V counterclockwise performance-curve PDF extracted with the supplied motor archive. Acquired as original archive content; this geometry batch makes no curve-value interpretation.

Evidence: extracted_original_archive_member.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-261ec2be4f36"></a>

## SRC-261ec2be4f36 — Body-linked native SAB feature adapter

Original source: [${MODELING_ROOT}/scripts/native_acis.py](../../scripts/native_acis.py)

Summary: Uses ezdxf1.4.5 parse_sab to traverse the actual single ACIS700 body graph, collect referenced planes/cylinders/points, and check closed reciprocal edge partners. Reports ACIS units metadata separately and rejects unsupported transforms/surfaces.

Evidence: local_execution_evidence_inspected, local_source_or_execution_record_inspected, implementation_artifact, implementation_exercised_on_saved_native_geometry.

Documents: research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json, research/sources/round-20/component-sources.json, research/sources/circular-boundary-reader-2026-11-13.json, execution/circular-boundary-reader-2026-11-13.md, skills/cad-ocs-engineering/SKILL.md.

<a id="src-2626ebf073f7"></a>

## SRC-2626ebf073f7 — Pilz source-readiness result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/readiness.json`)

Summary: Existing gate returns NEEDS_INPUT forterminal bank andrail-clip interface geometry.

Evidence: executed_readiness_result.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-26397bd1f7c2"></a>

## SRC-26397bd1f7c2 — P01 p01-build-01 — rail-schema-3.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-3.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-3.json`)

Summary: p01-build-01 rail-schema-3.json: Retained native response with fields command, ok; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-26613ca599a7"></a>

## SRC-26613ca599a7 — Main frame crossmember nominal native model

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/p02-main-frame-crossmember-reference.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/p02-main-frame-crossmember-reference.dwg`)

Summary: New DWG2018 contains one hollow260mm crossmember with proposed40x40x3mm section and standard-calculation outer6mm/inner3mm corner radii. Native pre-save/reopened dimensions, persistence and inspected views pass.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-26ba505a1c89"></a>

## SRC-26ba505a1c89 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/earthtojake/text-to-cad/git/trees/HEAD?recursive=1](https://api.github.com/repos/earthtojake/text-to-cad/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-26efa4c0263d"></a>

## SRC-26efa4c0263d — kmammou/v-hacd LICENSE

Original source: [https://github.com/kmammou/v-hacd/blob/master/LICENSE](https://github.com/kmammou/v-hacd/blob/master/LICENSE)

Summary: - V-HACD: convex decomposition implementation, with BSD-3-Clause at kmammou/v-hacd LICENSE.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-27385cb38c95"></a>

## SRC-27385cb38c95 — Initial delegated Orion metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/acquisition-initial.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/acquisition-initial.json`)

Summary: Preserves initial assertion that retained manual includes48/12-30,subsequently contradicted by coordinator extraction;original download hashes retained.

Evidence: delegated_initial_source_review.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-2752296f9685"></a>

## SRC-2752296f9685 — point-03-operations

Original source: [${MODELING_ROOT}/research/action-audit/point-03-operations.json](../action-audit/point-03-operations.json)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-2759f46214ed"></a>

## SRC-2759f46214ed — SarahWeiii/CoACD README and repository page

Original source: [https://github.com/SarahWeiii/CoACD](https://github.com/SarahWeiii/CoACD)

Summary: Official repository page accessed 2026-11-12; mutable main branch, no commit pin inspected. README documents OBJ input, OBJ/WRL output, convex components, `-i/--input`, `-o/--output`, `-t/--threshold` default 0.05, metre-scale `-rm/--real-metric`, and `-sp/--split` individual pieces. Existing source register separately records MIT license and 2022 copyright.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r08.md.

<a id="src-27d968161e9f"></a>

## SRC-27d968161e9f — OCS window-restore source

Original source: ${OCS_ROOT}/src/sys.rs (`${OCS_ROOT}/src/sys.rs`)

Summary: Local source inspected for capture window-restore behavior;no application source edits made.

Evidence: inspected_local_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-280cbbe6b531"></a>

## SRC-280cbbe6b531 — SKF page4 fitting and slot image

Original source: ${TEMP_ROOT}/opencode/skf-sy20tf-technical-page4.png (`${TEMP_ROOT}/opencode/skf-sy20tf-technical-page4.png`)

Summary: Actual inspected primary page image confirms slotlength20.5mm,locking-sidefaceoffset18.3mm and45degree,2mmoffset greasefitting with7mmhex and6.5mmhead.

Evidence: retained_source_render_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-28c1ea6ca46e"></a>

## SRC-28c1ea6ca46e — GProp_GProps Class Reference — Open CASCADE Technology Reference Manual 8.0.1

Original source: [https://dev.opencascade.org/doc/refman/html/class_g_prop___g_props.html](https://dev.opencascade.org/doc/refman/html/class_g_prop___g_props.html)

Summary: Official OCCT reference accessed 2026-11-12. Requested dev.opencascade.org URL redirected to occt3d.com. GProp_GProps provides mass, absolute-frame centre of mass and central inertia tensor; Add(component,density) composes properties and automatically applies Huygens parallel-axis shifts. The docs warn to use coherent geometry/density units and avoid applying density twice.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-28f1e37fe3ab"></a>

## SRC-28f1e37fe3ab — OpenCV Python camera calibration tutorial

Original source: [https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html)

Summary: Official OpenCV tutorial maps known 3D object points to image points, detects/refines chessboard corners and uses calibrateCamera; square dimensions establish physical units.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-05-visual.md, research/sources/round-02/cad-sources.json.

<a id="src-2945aa520dc5"></a>

## SRC-2945aa520dc5 — Authorized action-audit execution record

Original source: [${MODELING_ROOT}/research/action-audit/execution-record.md](../action-audit/execution-record.md)

Summary: Observed dispatch, actual identity reports, review dispositions, scope finding and source-registration integration for this authorized documentation batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-296ae586672b"></a>

## SRC-296ae586672b — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/persistence.json`)

Summary: Recovered original reopen request withmatching savehash,manifest andzero-error audit.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-29c790174a58"></a>

## SRC-29c790174a58 — Robot tow-ball support plate (P07) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p07-robot-tow-ball-support-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p07-robot-tow-ball-support-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: hitch; Trailer ball-coupling proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-29e05b3b3047"></a>

## SRC-29e05b3b3047 — OpenCADStudio kernel body path note

Original source: ${OCS_ROOT}/docs/cadkernel-body-path.md (`${OCS_ROOT}/docs/cadkernel-body-path.md`)

Summary: Local OCS design/implementation note describes supported kernel-body paths and history limitations; it does not establish STEP analytic-surface export.

Evidence: existing_report_registered, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-05/point-03-local-sources.json.

<a id="src-2a3f02ebc764"></a>

## SRC-2a3f02ebc764 — reopened-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-checkpoint.json`)

Summary: Saved/reopened document87 identity andgeometry revision.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-2a63549fb0bc"></a>

## SRC-2a63549fb0bc — Data conventions — Nerfstudio documentation

Original source: [https://docs.nerf.studio/quickstart/data_conventions.html](https://docs.nerf.studio/quickstart/data_conventions.html)

Summary: Current Nerfstudio data-conventions page inspected 2026-11-12; release not pinned. Defines OpenGL/Blender/NeRF camera axes, +Z-up world, pixel-centre convention, transforms.json camera basis columns and origin translation. Depth images are assumed 16/32-bit millimetres, zero means unknown, and `depth_unit_scale_factor` changes scale; depth images resize to RGB by default. Page does not specify selected parser auto-orientation/scale-normalization runtime config.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-2aa9c1b61444"></a>

## SRC-2aa9c1b61444 — start_c045.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/start_c045.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/start_c045.py`)

Summary: Validated source-covered C045 feature contract,created isolated native document86 andimported pinned STEP.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-2ad28cfa19ba"></a>

## SRC-2ad28cfa19ba — Point 06 — software and API review

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-06-software.md](../action-audit/reviews/point-06-software.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-2b16462315c1"></a>

## SRC-2b16462315c1 — Automatic 3D CAD models reconstruction from 2D orthographic drawings

Original source: [https://www.sciencedirect.com/science/article/pii/S0097849323000766](https://www.sciencedirect.com/science/article/pii/S0097849323000766)

Summary: Computers & Graphics 2023 paper describes matching projected edge features across views to create a 3D wireframe, then detecting loops/faces and trimming/stitching a watertight model; reported F-score is study-specific.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r05.md, research/workflows/details/cad-r09.md, research/workflows/details/mix-r08.md.

<a id="src-2b834d92a1e6"></a>

## SRC-2b834d92a1e6 — Point 06 — Building and robot structure and properties

Original source: [${MODELING_ROOT}/research/action-audit/point-06-building-and-robot.md](../action-audit/point-06-building-and-robot.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-2bcc72542265"></a>

## SRC-2bcc72542265 — Geometry creation — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html)

Summary: IfcOpenShell 0.9.0post1 guide accessed 2026-11-12. Records representation creation examples and placement/unit distinction; used as background source for separating IFC geometric representation authoring from semantic product creation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-2bdc86cc68a8"></a>

## SRC-2bdc86cc68a8 — Checked Sumitomo driver derivative

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-smartris-driver-ch52308-checked.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-smartris-driver-ch52308-checked.dwg`)

Summary: Separate native derivative retains116 solids/eight text labels and corrects connector-shell span to116.7mm by moving the complete X2 group -0.15mm in X; saved141 checks pass.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-2c5893d8360b"></a>

## SRC-2c5893d8360b — ME0907 additional exterior-source findings

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/source-review.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/source-review.md`)

Summary: Bounded delegated review identifies the direct manufacturer drawing, Kelly archive variant, EVEA CAD-on-request page and cover150-011 with three Phillips screws. Exact URLs and download outcomes are retained. Actual agent identity unavailable.

Evidence: delegated_web_review_record.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-2cea52720940"></a>

## SRC-2cea52720940 — P01 p01-build-03 — reopened-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-checks.json`)

Summary: p01-build-03 reopened-checks.json: Feature/source check result UNKNOWN; Reopened record stores SAB binary; this feature reader supports SAT text

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-2cf7a4eb3a5d"></a>

## SRC-2cf7a4eb3a5d — RGBDImageFactory.cpp — Open3D v0.20.0 source

Original source: [https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp)

Summary: Official raw source on tag v0.20.0 inspected 2026-11-12. `CreateFromColorAndDepth` accepts caller-provided depth_scale/depth_trunc/intensity flag, passes scale and truncation to `ConvertDepthToFloatImage`, and requires matching color/depth dimensions. Default arguments are declared in RGBDImage.h, not in this function definition.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-2d09726ce736"></a>

## SRC-2d09726ce736 — Reviewed motor dimensions and feature associations

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/coordinator-review.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/coordinator-review.md`)

Summary: Source-image review corrects the two mounting group associations, identifies 30 mm shaft-thread depth and 19.58 mm keyway section distance, and retains source tolerances and server-date attribution.

Evidence: manufacturer_dimension_review.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-2d331dacc4f0"></a>

## SRC-2d331dacc4f0 — Execution plan: define one workflow point at a time

Original source: [${MODELING_ROOT}/research/action-audit/plan.md](../action-audit/plan.md)

Summary: Authorized documentation method: fifteen fields per action, alternative software/agent modes, evidence-based merges, feature-specific accuracy and local-compute-first definition order.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-2d407c9d997c"></a>

## SRC-2d407c9d997c — point-06-operations

Original source: [${MODELING_ROOT}/research/action-audit/point-06-operations.json](../action-audit/point-06-operations.json)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-2d6abe7b467d"></a>

## SRC-2d6abe7b467d — decimal — Decimal fixed-point and floating-point arithmetic — Python 3.15.2 documentation

Original source: [https://docs.python.org/3/library/decimal.html](https://docs.python.org/3/library/decimal.html)

Summary: Official Python documentation describes Decimal construction from strings and exact representation of decimal values, while Decimal construction from a binary float preserves that float's binary approximation. For intake, passing a source numeric string directly to Decimal preserves its decimal value and spelling-significance digits for subsequent controlled arithmetic. Decimal does not assign units, distinguish engineering tolerances from measurement uncertainty or validate feature association; arithmetic context and rounding still govern calculations.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-01-model-brief.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-04/intake-sources.json.

<a id="src-2d95a53e76b4"></a>

## SRC-2d95a53e76b4 — cad-r02.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r02.md](../workflows/details/cad-r02.md)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-2db8e2fc7613"></a>

## SRC-2db8e2fc7613 — https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp

Original source: [https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp](https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp)

Summary: Four page attempts failed and support no technical claim: Open3D 0.20.0 `RGBDImage` API page `https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html` timed out; versioned API URL `https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html` was unavailable via the web tool; GitHub HTML for `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp` returned cache miss; and `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp` returned cache miss. The default parameters were verified in the successful raw v0.20.0 `RGBDImage.h` declaration; conversion behavior was inspected in the raw `RGBDImageFactory.cpp` and `Image.cpp` sources recorded above. No further failed URLs support technical claims.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-2e05ef8b5192"></a>

## SRC-2e05ef8b5192 — MuJoCo modeling guide — main branch

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst)

Summary: Official repository guide on mutable main, accessed 2026-11-12. Documents spatial frames, right-handed orientation handling, quaternion/frame serialization and angle conventions; source branch is not a pinned runtime version.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/action-audit/reviews/visual-review.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r07.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-2e1174c2d05e"></a>

## SRC-2e1174c2d05e — activated-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/activated-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/activated-isometric.png`)

Summary: Actual converter capture attempt activated-isometric;image repeats the previous Fibox enclosure. Included as failed visual evidence,withhash comparison in capture-identity-checks.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-2e711cc8d780"></a>

## SRC-2e711cc8d780 — P01 p01-build-01 — rail-capabilities.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-capabilities.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-capabilities.json`)

Summary: p01-build-01 rail-capabilities.json: Retained native response with fields api, concurrency, editor, geometry, ok, operations, records; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-2e8d8f25e086"></a>

## SRC-2e8d8f25e086 — p02-source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-source-job.json`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-2e92a48ed867"></a>

## SRC-2e92a48ed867 — Structural Analysis and Shape Descriptors — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html)

Summary: OpenCV 4.13.0 documents `findContours` on an 8-bit single-channel binary image; nonzero pixels are foreground and the API returns contour coordinates and hierarchy. Contours support shape analysis but are pixel-derived boundaries, not engineering feature classes.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r08.md.

<a id="src-2f10709cdd89"></a>

## SRC-2f10709cdd89 — Schneider XB5AS8445 emergency button (C049) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c049-schneider-xb5as8445-emergency-button.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c049-schneider-xb5as8445-emergency-button.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Local stop equipment; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-2f413e970d01"></a>

## SRC-2f413e970d01 — P01 p01-build-02 — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/result.json`)

Summary: p01-build-02 result.json: Observed attempt state FAIL; Retains the definitive native subtraction error and the preserved recovery context.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-2fad977d4fe9"></a>

## SRC-2fad977d4fe9 — ${MODELING_ROOT}/research/workflows/cad-paths.json

Original source: [${MODELING_ROOT}/research/workflows/cad-paths.json](../workflows/cad-paths.json)

Summary: Source referenced for the stated workflow; see the owning documentation or research item.

Evidence: existing_report_registered, local_reference_registered, local_source_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-2fe2fa4714a1"></a>

## SRC-2fe2fa4714a1 — Local Python 3.14 decimal interface source

Original source: ${SYSTEM_ROOT}/usr/lib/python3.14/decimal.py (`${SYSTEM_ROOT}/usr/lib/python3.14/decimal.py`)

Summary: Decimal interface source inspected by software reviewer; official decimal documentation separately supports exact string construction.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-3018a0ce5798"></a>

## SRC-3018a0ce5798 — FreeCAD Part::TopoShape Class Reference

Original source: [https://freecad.github.io/SourceDoc/d8/ded/classPart_1_1TopoShape.html](https://freecad.github.io/SourceDoc/d8/ded/classPart_1_1TopoShape.html)

Summary: Official FreeCAD source documentation accessed 2026-11-12. General TopoShape reference lists read/write/import/export/validity APIs but did not expose mass, centre-of-mass or inertia methods in the inspected page; no mass-property claim relies on this page.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-3083e6298cf7"></a>

## SRC-3083e6298cf7 — Driver iteration — source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/source-job.json`)

Summary: Current source job pins15 manufacturer/reconstruction expectations, exact116-part handle mapping and explicit housing structure-only method; builder evidence uses durable retained copy.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-30936b6bad80"></a>

## SRC-30936b6bad80 — P01 p01-build-03 — reopened-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-records.json`)

Summary: p01-build-03 reopened-records.json: 1 native entity records in document 71, revision 0; stores exact geometry encoding and properties for interpretation independently of PASS labels.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-30ccd7c0d9d0"></a>

## SRC-30ccd7c0d9d0 — ME0907 source drawing render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/ME0907-page1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/ME0907-page1.png`)

Summary: Rendered original sheet inspected for front/side/section associations, exterior slots, terminals, connectors and source notes.

Evidence: derived_source_render_inspected.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-3126762ba53b"></a>

## SRC-3126762ba53b — cad-workflow-findings.md — recorded_execution_summary

Original source: ${FERME_ROOT}/skills/cad-workflow-findings.md (`${FERME_ROOT}/skills/cad-workflow-findings.md`)

Summary: OCS 2026.42 component constructions, import/save results, failed requests and component-specific recoveries. Applicability: Claims are attributed to the retained reports/session identifiers; raw session replay is a separate result.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-08/component-plan-sources.json, research/sources/round-09/component-execution-sources.json.

<a id="src-3161922d5c21"></a>

## SRC-3161922d5c21 — P01 p01-build-01 — readiness-r02.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/readiness-r02.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/readiness-r02.json`)

Summary: p01-build-01 readiness-r02.json: Retained native response with fields job_id, part_id, part_name, state, questions, source_observations, meaning; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-31664957c5f6"></a>

## SRC-31664957c5f6 — imported-blocks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-blocks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-blocks.json`)

Summary: Initialblockdefinitionsandmembershipincludingroot,base,cover,lock,feetandplate.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-319fc05dec23"></a>

## SRC-319fc05dec23 — corrected-records-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-0.json`)

Summary: corrected native record snapshot: 81:Solid3D, 85:Insert, 89:Solid3D, 8D:Solid3D, 91:Solid3D, 95:Solid3D. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-31a38faa2037"></a>

## SRC-31a38faa2037 — Point 07 designer notes — reconstruction procedures

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-07-designer.md](../action-audit/reviews/point-07-designer.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-31cafb73df3e"></a>

## SRC-31cafb73df3e — https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html)

Summary: 1. Name: Open3D RGB-D odometry; Role: Register RGB and depth frames and estimate sequence poses; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Dependency contract: Use the linked branch dossier and original software documentation for the selected backend and version.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r09.md.

<a id="src-31ce89d89be0"></a>

## SRC-31ce89d89be0 — build_leaf_gen2.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/build_leaf_gen2.py (`${TEMP_ROOT}/opencode/build_leaf_gen2.py`)

Summary: top and staged recovery functions reconstruct shell/terminal features; finish checks and saves the component. Applicability: Component-specific dimensions and staged resumption; imports shared battery/item/wrapper/SAT modules.

Evidence: local_source_inspected, local_source_or_execution_record_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-15/leaf-sources.json.

<a id="src-31e3c7199ce2"></a>

## SRC-31e3c7199ce2 — Anderson SB50 6331G5 connector assembly (C038) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c038-anderson-sb50-6331g5-connector-assembly.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c038-anderson-sb50-6331g5-connector-assembly.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Charge port proposal; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-31f850cbf25b"></a>

## SRC-31f850cbf25b — step-source.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/step-source.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/step-source.json`)

Summary: Actual import dialog exact family-STEP path binding.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-31fb748a20df"></a>

## SRC-31fb748a20df — CAD project structure

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/project-layout.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/project-layout.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: CAD project structure. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-32250745fda8"></a>

## SRC-32250745fda8 — saved-assembly-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/saved-assembly-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/saved-assembly-checks.json`)

Summary: 29passingchecks:16sourceplacements,12definitionpointsetsandnestedinstancepreservation.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-32a6140acc3a"></a>

## SRC-32a6140acc3a — reopened-records-18.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-18.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-18.json`)

Summary: reopenednativeentitysnapshot: BA:Insert, BB:Insert, BC:Insert, BD:Insert, BE:Insert, BF:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-331dc8c3567f"></a>

## SRC-331dc8c3567f — License text

Original source: [https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/LICENSE](https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-334ea37bde4d"></a>

## SRC-334ea37bde4d — build_bmw_i3_94ah.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/build_bmw_i3_94ah.py (`${TEMP_ROOT}/opencode/build_bmw_i3_94ah.py`)

Summary: build/accessories/cable_done/finish reconstruct exterior parts and swept cable with checks. Applicability: Component-specific dimensions, paths and cable pose; imports shared battery/item/wrapper/SAT modules.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-336b06f67c34"></a>

## SRC-336b06f67c34 — https://github.com/nerfstudio-project/gsplat

Original source: [https://github.com/nerfstudio-project/gsplat](https://github.com/nerfstudio-project/gsplat)

Summary: - gsplat repository/license: https://github.com/nerfstudio-project/gsplat

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-07-visual.md, research/reconstruction.md.

<a id="src-339862a5c701"></a>

## SRC-339862a5c701 — official Python API guidance

Original source: [https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst](https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst)

Summary: Blender also supports scripted background work using `blender --background --python <script>` per the official Python API guidance. For repeatable import/export and geometry checks, a pinned background script is easier to version and reproduce than a natural-language-only interaction. MCP may add interactive inspection and iterative scene edits; it should call versioned task scripts or typed operations for deterministic project outputs. This split is a proposal, not a tested comparison.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r05.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r09.md, research/workflows/domain-paths.md.

<a id="src-33a3c43268b3"></a>

## SRC-33a3c43268b3 — text-to-cad

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/README.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: text-to-cad. Source class: repository README. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-33c6833035f2"></a>

## SRC-33c6833035f2 — P01 p01-build-03 — pre-save-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/pre-save-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/pre-save-checks.json`)

Summary: p01-build-03 pre-save-checks.json: Feature/source check result PASS; 5 retained check groups with document/revision evidence.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-341c5dce719a"></a>

## SRC-341c5dce719a — raw source

Original source: [https://raw.githubusercontent.com/freshtechbro/claudedesignskills/main/.claude/skills/web3d-integration-patterns/SKILL.md](https://raw.githubusercontent.com/freshtechbro/claudedesignskills/main/.claude/skills/web3d-integration-patterns/SKILL.md)

Summary: freshtechbro `web3d-integration-patterns/SKILL.md` (raw source) ; Raw source describes integration patterns for Three.js, GSAP ScrollTrigger, React Three Fiber, Motion and React Spring. It includes browser scene setup, render loops, state coordination, scroll animation and performance patterns; references the constituent library skills. ; Web scene and animation skill, not CAD. Its listed tools require JavaScript/npm packages and browser runtime. The page identifies no hosted AI or geometry-generation API. Repository-wide licence was not checked in this pass; no source copying recommended. Raw SKILL.md was web-inspected on 2026-11-12, not downloaded.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-34471858a5cb"></a>

## SRC-34471858a5cb — 50mm2 main cable geometry (C059) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c059-50mm2-main-cable-geometry.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c059-50mm2-main-cable-geometry.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Existing main cable example; original kind source cable reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-347a968ad00e"></a>

## SRC-347a968ad00e — https://www.microsoft.com/en-us/research/workbench/project/trellis

Original source: [https://www.microsoft.com/en-us/research/workbench/project/trellis](https://www.microsoft.com/en-us/research/workbench/project/trellis)

Summary: - TRELLIS.2 Microsoft Research overview: https://www.microsoft.com/en-us/research/workbench/project/trellis

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-348e931a03fa"></a>

## SRC-348e931a03fa — P01 p01-build-01 — schema-discovery-findings.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/schema-discovery-findings.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/schema-discovery-findings.json`)

Summary: p01-build-01 schema-discovery-findings.json: Retained native response with fields evidence, document_context, observations; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-34adb5d3d452"></a>

## SRC-34adb5d3d452 — reopened-records-12.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-12.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-12.json`)

Summary: reopened native record snapshot: AB:Insert, AC:Insert, AD:Insert, AE:Insert, AF:Insert, B0:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-34ed7ccfd827"></a>

## SRC-34ed7ccfd827 — Point 02 — Existing components and CAD files to inspected reusable inputs

Original source: [${MODELING_ROOT}/research/action-audit/point-02-component-reuse.md](../action-audit/point-02-component-reuse.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-353e59cb2694"></a>

## SRC-353e59cb2694 — Bonsai georeferencing guide

Original source: [https://docs.bonsaibim.org/guides/authoring/georeferencing.html](https://docs.bonsaibim.org/guides/authoring/georeferencing.html)

Summary: Official guidance for site CRS, coordinate transformations and project north; coordinate parameters must come from survey/engineering sources.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

<a id="src-3555fbfacefa"></a>

## SRC-3555fbfacefa — iTeh catalogue access for EN 10219-2:2019

Original source: [https://standards.iteh.ai/catalog/standards/cen/073cb87d-d24a-4cde-b626-79d9b01cb537/en-10219-2-2019](https://standards.iteh.ai/catalog/standards/cen/073cb87d-d24a-4cde-b626-79d9b01cb537/en-10219-2-2019)

Summary: Direct open attempt returned HTTP 502. Standard content was instead inspected from the linked SIST-EN-10219-2-2019 PDF sample and AFNOR catalogue record. This catalogue failure is recorded without supporting claims.

Evidence: access_failed.

Documents: research/sources/round-10/tube-corner-sources.json.

<a id="src-35a34c26c8e5"></a>

## SRC-35a34c26c8e5 — P02 crossmember — reopened-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-records.json`)

Summary: Raw native SAB body in reopened document73 supplies independent persisted-geometry observations.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-35cca1cb0d7e"></a>

## SRC-35cca1cb0d7e — blender_gltf.py — Blender glTF importer source, main branch

Original source: [https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py](https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py)

Summary: Official Blender source on mutable main, accessed 2026-11-12. Import code maps glTF Y-up to Blender Z-up `(x,-z,y)` and scales locations by `1 / scene.unit_settings.scale_length` as Blender units per metre. Does not pin installed Blender version or prove local import output.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-360ae57eba52"></a>

## SRC-360ae57eba52 — Driver iteration — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/ocs-journal.jsonl`)

Summary: Guarded request history preserves original open/reopen polling-bound results, same-ID recovery, whole-X2 translation, verified save and actual captures.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-368cf414765d"></a>

## SRC-368cf414765d — FreeCAD File Formats & Interoperability Guide

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/file_formats_interop.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/file_formats_interop.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD File Formats & Interoperability Guide. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-36ec74f82716"></a>

## SRC-36ec74f82716 — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/readiness.json`)

Summary: Existing gate returns NEEDS_INPUT for exact48/12 mounting/terminal geometry andhousing depth revision.

Evidence: executed_readiness_result.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-36fd06b4fde4"></a>

## SRC-36fd06b4fde4 — https://github.com/cdcseacave/openMVS

Original source: [https://github.com/cdcseacave/openMVS](https://github.com/cdcseacave/openMVS)

Summary: - OpenMVS repository: https://github.com/cdcseacave/openMVS

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-37228572b45c"></a>

## SRC-37228572b45c — Saved ME0907 analytic geometry observations

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/final-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/final-checks.json`)

Summary: 18 passing checks read actual saved surfaces and topology: cylinder axes/radii, individual hole-bottom centres, end stations, keyway planes/rounded end and three closed connected bodies.

Evidence: executed_verification_result.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-379d3077df35"></a>

## SRC-379d3077df35 — FreeCAD Draft SVG documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md)

Summary: Official FreeCAD docs list supported SVG paths/shapes, flattening of Z on import, use of viewBox/physical dimensions, and 90-DPI fallback when physical size is absent.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-3832553f9cb5"></a>

## SRC-3832553f9cb5 — 02-fabrication-requirements.md

Original source: ${FERME_ROOT}/engineering/module-development/physical-build/02-fabrication-requirements.md (`${FERME_ROOT}/engineering/module-development/physical-build/02-fabrication-requirements.md`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-3844fad0d2f9"></a>

## SRC-3844fad0d2f9 — Orion Jr2 16cell BMS (C027) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c027-orion-jr2-16cell-bms.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c027-orion-jr2-16cell-bms.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Leaf main bank; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-390f5c71910b"></a>

## SRC-390f5c71910b — Existing Victron acquisition provenance

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/existing-source-provenance.tsv (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/existing-source-provenance.tsv`)

Summary: Retains the earlier source URLs,byte counts,digests and reported retrieval timestamps for exact STEP,PDF,manual and product page. Copied unchanged from the concurrent FERME provenance file.

Evidence: existing_acquisition_record_reused.

Documents: research/sources/round-20/component-sources.json.

<a id="src-393afe62bdcb"></a>

## SRC-393afe62bdcb — capture-identity-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/capture-identity-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/capture-identity-checks.json`)

Summary: Failed visual identity:previous enclosure remains visible andall new ISO/TOP/activate/REGEN image hashes are identical.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-39a648fd2c2a"></a>

## SRC-39a648fd2c2a — rec-r03.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r03.md](../workflows/details/rec-r03.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-39a675ae7e31"></a>

## SRC-39a675ae7e31 — P01 p01-build-01 — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/ocs-journal.jsonl`)

Summary: p01-build-01 append-only request journal retains 52 events across 22 request identities, with original intents and responses. It supplies the native command/recovery history for this named attempt; request tokens are excluded.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-39b9dbfcfb8e"></a>

## SRC-39b9dbfcfb8e — AFNOR Éditions — NF EN 10219-2

Original source: [https://www.boutique.afnor.org/fr-fr/norme/nf-en-102192/profils-creux-de-construction-soudes-formes-a-froid-en-aciers-partie-2-tole/fa177343/83616](https://www.boutique.afnor.org/fr-fr/norme/nf-en-102192/profils-creux-de-construction-soudes-formes-a-froid-en-aciers-partie-2-tole/fa177343/83616)

Summary: AFNOR catalogue lists NF EN 10219-2 as published May 2019 and in force, identifies European parent EN 10219-2:2019, describes coverage of cold-formed welded circular/square/rectangular/elliptical hollow sections, and says Annex A contains section-property formulas for structural design and Annex B gives properties for a limited common-size range. The 2006 NF edition is marked annulée/replaced.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-39d84cf3ce70"></a>

## SRC-39d84cf3ce70 — Driver iteration — corrected-presave-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/corrected-presave-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/corrected-presave-records.json`)

Summary: Actual post-translation records preserve the complete moved X2 group and all93 unaffected entity properties before save.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-39f868616f62"></a>

## SRC-39f868616f62 — OpenCV calibration module overview

Original source: [https://docs.opencv.org/5.0/main_modules/calib.html](https://docs.opencv.org/5.0/main_modules/calib.html)

Summary: Official OpenCV reference describes camera calibration, pose estimation, calibration target correspondences and reprojection-error optimization. A planar homography relates points on a plane and does not recover depth.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-05-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r08.md.

<a id="src-39fee200cbbf"></a>

## SRC-39fee200cbbf — usage

Original source: [https://github.com/nophead/NopSCADlib/blob/master/docs/usage.md](https://github.com/nophead/NopSCADlib/blob/master/docs/usage.md)

Summary: NopSCADlib ; OpenSCAD library and project framework with a `vitamins` collection of modeled real-world hardware and a `tests` directory. Repository, usage ; GPL-3.0. It is reusable parametric OpenSCAD code and geometry; check whether the intended use is to redistribute library code, generated part files or merely reference it, and retain notices.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md.

<a id="src-3a0be7d2ba98"></a>

## SRC-3a0be7d2ba98 — Dimension Drawing - Orion-Large, Rev01

Original source: [https://www.victronenergy.com/upload/documents/Orion-Tr-Smart-Charger-Isolated-12V-24V-360W.pdf](https://www.victronenergy.com/upload/documents/Orion-Tr-Smart-Charger-Isolated-12V-24V-360W.pdf)

Summary: Manufacturer Rev01 drawing explicitly names24/12 ORI241236120;187 flange,174×71 slot pitches,86 depth reference andR4 open slots.

Evidence: downloaded_original.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-3a1449ac8a6c"></a>

## SRC-3a1449ac8a6c — Converter execution report

Original source: [${MODELING_ROOT}/execution/c043-c045-converters.md](../../execution/c043-c045-converters.md)

Summary: Explains exact C045 CAD,39 checks,failed views,applied procedure,C043 source gate andretained manual correction.

Evidence: executed_work_report.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-3a199df280ce"></a>

## SRC-3a199df280ce — LICENSE

Original source: [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)

Summary: - CoACD: approximate convex decomposition implementation SarahWeiii/CoACD. Its LICENSE is MIT, copyright Xinyue Wei and Minghua Liu (2022). Pin the reviewed revision and retain its notice when distributing the tool.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-3a866415e567"></a>

## SRC-3a866415e567 — P01 p01-build-03 — view-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/view-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/view-journal.jsonl`)

Summary: p01-build-03 append-only request journal retains 28 events across 5 request identities, with original intents and responses. It supplies the native command/recovery history for this named attempt; request tokens are excluded.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-3b28b3defd8a"></a>

## SRC-3b28b3defd8a — LEAP71_ShapeKernel official repository page and README

Original source: [https://github.com/leap71/LEAP71_ShapeKernel](https://github.com/leap71/LEAP71_ShapeKernel)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: LEAP71_ShapeKernel official repository page and README. Source class: official repository page containing README excerpt and repository metadata. Original reuse terms: Repository identifies Apache-2.0; the archive contains the repository page, not the full LICENSE text. Preserve upstream copyright and notices; exact licence terms require the original LICENSE file.

Evidence: archived_original_referenced, existing_report_registered.

Documents: research/sources/round-02/archive-sources.json, research/sources/round-02/project-sources.json.

<a id="src-3b4f5ef46a7f"></a>

## SRC-3b4f5ef46a7f — MCP automation guide

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/docs/automation/README.md](https://github.com/HakanSeven12/OpenCADStudio/blob/main/docs/automation/README.md)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-3b555e7e7db8"></a>

## SRC-3b555e7e7db8 — License text

Original source: [https://raw.githubusercontent.com/github/awesome-copilot/main/LICENSE](https://raw.githubusercontent.com/github/awesome-copilot/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-3b6d17115e2e"></a>

## SRC-3b6d17115e2e — README setup/telemetry

Original source: [https://github.com/earthtojake/text-to-cad#install](https://github.com/earthtojake/text-to-cad#install)

Summary: `cad` from `earthtojake/text-to-cad` ; Archived `skills/cad/SKILL.md` uses `cadgen` wrappers around build123d/OCCT, Python model scripts, STEP/mesh export, a CAD Viewer and local `cadgen mcp`. README pins Python 3.13 and `cadgen==0.7.25` in its command examples; `uvx` downloads managed runtime/dependencies. It says first run needs network. Usage statistics and crash reports are on by default with random install IDs; README says turn off using `uvx cadgen telemetry off`. Core modeling path is local after runtime download; optional manufacturing-service integrations are separate. Repository and skill licence are MIT. ; Strong candidate for an optional build123d-backed modeling and inspection path, with telemetry disabled or disclosed and the pinned environment audited. It brings its own runtime/server/viewer and is not only a prompt skill. The source supports editable Python source and exact B-rep through build123d/OCCT; exported meshes remain tessellated. Source links: `skills/cad/SK...

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-3b89f4bc986b"></a>

## SRC-3b89f4bc986b — Leaf iteration — native-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/native-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/native-records.json`)

Summary: Actual eight-solid saved SAB records provide transformed shell vertices, analytic surfaces and terminal geometry for 29 source-bound checks.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-3bb79a82bdb3"></a>

## SRC-3bb79a82bdb3 — kernel body path note

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/docs/cadkernel-body-path.md](https://github.com/HakanSeven12/OpenCADStudio/blob/main/docs/cadkernel-body-path.md)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-3bc1484f7601"></a>

## SRC-3bc1484f7601 — P02 crossmember — source-job-r02.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/source-job-r02.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/source-job-r02.json`)

Summary: Immutable P02 source revision2 pins proposed section/length, standard calculation radii,340mm outside frame width, source hashes and explicit local midpoint datum mapping.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-3bdbace92938"></a>

## SRC-3bdbace92938 — https://pointclouds.org/documentation/classpcl_1_1_sample_consensus_1_1_sample_consensus_model_cylinder.html

Original source: [https://pointclouds.org/documentation/classpcl_1_1_sample_consensus_1_1_sample_consensus_model_cylinder.html](https://pointclouds.org/documentation/classpcl_1_1_sample_consensus_1_1_sample_consensus_model_cylinder.html)

Summary: These sources provide an evidenced candidate fitter and adapter contract. The cylinder model still depends on valid corresponding normals, an adequately sampled and visible cylindrical surface, configured thresholds/radius range, and the selected consensus method. The fitted cylinder and inliers describe the supplied sampled cloud; they do not establish physical feature identity, design intent, or parameter uncertainty. A short arc can leave radius weakly constrained, so retain coverage and held-out residual checks. The attempted PCL Doxygen URL `https://pointclouds.org/documentation/classpcl_1_1_sample_consensus_1_1_sample_consensus_model_cylinder.html` returned “Internal Error / URL not accessible via this tool.” No claims rely on that failed page. There are 13 successfully inspected pages (ten initial plus three follow-up) and one recorded failed access attempt.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-3c3c9e360b9d"></a>

## SRC-3c3c9e360b9d — Export geometry — Nerfstudio documentation

Original source: [https://docs.nerf.studio/quickstart/export_geometry.html](https://docs.nerf.studio/quickstart/export_geometry.html)

Summary: Current Nerfstudio export guide inspected 2026-11-12; release not pinned. Documents point-cloud PLY and textured mesh OBJ output; TSDF mesh export applies across models; Poisson mesh requires a model computing/predicting normals. Model-specific export stages remain distinct from Gaussian PLY export.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-3c5050fd6ac5"></a>

## SRC-3c5050fd6ac5 — Driver iteration — reopened-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-checks.json`)

Summary: All141 saved native checks pass, with housing graph/vertex method separated from analytic measurement methods.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-3cb645d27838"></a>

## SRC-3cb645d27838 — Part scripting — FreeCAD documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md)

Summary: The FreeCAD Part scripting page describes Part as an Open CASCADE B-rep module with Python-accessible geometric primitives and TopoShapes including vertices, edges, wires, faces, solids and compounds. It shows creating a primitive, converting it to a shape, assigning the shape to a Part::Feature and recomputing. The inspected rendered GitHub page was paired with its raw view at https://raw.githubusercontent.com/FreeCAD/FreeCAD-documentation/main/wiki/Part_scripting.md to read the content. This documents native B-rep construction, not image interpretation or a validity check.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-05-software.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-3d1d4ee7af09"></a>

## SRC-3d1d4ee7af09 — P01 p01-build-01 — document-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/document-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/document-checkpoint.json`)

Summary: p01-build-01 document-checkpoint.json: Binds partial/native stage to document 68, revision 0 and named part handles {}; supports inspected recovery.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-3d22000abccf"></a>

## SRC-3d22000abccf — ARCA 203015T, 8121020 | 200 x 300 x 150 | ARCA 203015

Original source: [https://www.fibox.com/products/arca-iec/arca-203015/8121020](https://www.fibox.com/products/arca-iec/arca-203015/8121020)

Summary: Exact manufacturer product identity and page-listed dimensions, cover/locking/hinge description, package content, material, colour and ratings.

Evidence: downloaded_original.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-3d2c6bb76580"></a>

## SRC-3d2c6bb76580 — Main-frame rail native execution report

Original source: [${MODELING_ROOT}/execution/p01-rail-build.md](../../execution/p01-rail-build.md)

Summary: Records the source-first action registration, three native attempts, successful hollow-section dimensions and save/reopen identity, captured views, applied selection/script/skill improvements,28 passing helper tests and the next binary-feature readback issue.

Evidence: authored_code_or_procedure_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-3d593dd6ed4a"></a>

## SRC-3d593dd6ed4a — README

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/README.md](../action-audit/implementation-queue/README.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-07/parts-catalogue-sources.json.

<a id="src-3d8897df5de5"></a>

## SRC-3d8897df5de5 — Leaf iteration — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-isometric.png`)

Summary: Inspected current isometric image shows both shell outlines, pressed features, corner mounts and three contacts corresponding to the retained source illustration.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-3d8ba9ae669c"></a>

## SRC-3d8ba9ae669c — sequence.md

Original source: [${MODELING_ROOT}/research/action-audit/sequence.md](../action-audit/sequence.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-3d8e9cd2ace9"></a>

## SRC-3d8e9cd2ace9 — ngv064_ocs.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/ngv064_ocs.py (`${TEMP_ROOT}/opencode/ngv064_ocs.py`)

Summary: read/write/step, checkpoint, revolve_z, cylinder and subtract wrap native requests and stepped command state. Applicability: Fixed session, temporary paths/prefix allowlist; module import selects a descriptor; accepted/running polling is unbounded; write treats waiting_input as failure, while step permits it.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-3e2691ad3057"></a>

## SRC-3e2691ad3057 — https://www.reddit.com/r/aigamedev/comments/1xj5z85/any_claude_code_skills_youd_recommend_for/

Original source: [https://www.reddit.com/r/aigamedev/comments/1xj5z85/any_claude_code_skills_youd_recommend_for/](https://www.reddit.com/r/aigamedev/comments/1xj5z85/any_claude_code_skills_youd_recommend_for/)

Summary: - Reddit: “Any Claude Code skills you’d recommend for building a 3D game from scratch?” https://www.reddit.com/r/aigamedev/comments/1xj5z85/any_claude_code_skills_youd_recommend_for/ — opened successfully. It is a community discussion, not a technical test or primary model source. Comments mention Blender MCP and hosted services including Meshy, Hunyuan, Tripo and Rodin, but provide no reproducible quality/accuracy comparisons. One commenter reports a generated model with two million faces; this is an anecdote and not a performance specification. It motivates mesh-decimation/topology checks for game assets, outside dimensional CAD evidence.

Evidence: existing_report_registered.

Documents: research/reconstruction.md, research/user-supplied-links.md.

<a id="src-3e48dbdca207"></a>

## SRC-3e48dbdca207 — bmw-i3-94ah-native-checks.json — recorded_check_results

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json (`${FERME_ROOT}/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json`)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-3e575abffb8a"></a>

## SRC-3e575abffb8a — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/mitsuhiko/agent-stuff](https://api.github.com/repos/mitsuhiko/agent-stuff)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-3e6c1657a06b"></a>

## SRC-3e6c1657a06b — rec-r02.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r02.md](../workflows/details/rec-r02.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-3ea30e7b5209"></a>

## SRC-3ea30e7b5209 — Documentary verification method

Original source: [${MODELING_ROOT}/research/action-audit/verification-method.md](../action-audit/verification-method.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-3eaf1eca263a"></a>

## SRC-3eaf1eca263a — Main frame longitudinal rail proposal

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p01-main-frame-longitudinal-rail.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p01-main-frame-longitudinal-rail.md`)

Summary: Existing local component/action/skill/catalogue source reused by the consolidated plan. Evidence and proposal boundaries remain in the original record.

Evidence: local_source_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-09/component-execution-sources.json, research/sources/round-10/tube-corner-sources.json.

<a id="src-3ec7111d8cd7"></a>

## SRC-3ec7111d8cd7 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill/git/trees/HEAD?recursive=1](https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-3f924501d4f4"></a>

## SRC-3f924501d4f4 — Saved battery isometric view

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/reopened-isometric.png`)

Summary: Actual reopened exterior capture shows seated terminals,lid,casing ribs,side handle recess and mounting tabs; source geometry and insertion values retain independent checks.

Evidence: model_capture_inspected.

Documents: research/sources/round-20/component-sources.json.

<a id="src-3fc1850b2202"></a>

## SRC-3fc1850b2202 — Saved converter hash before recheck

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/file-before.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/file-before.json`)

Summary: Pins the existing native DWG path and hash before current-view capture, for preservation comparison.

Evidence: executed_file_inspection.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-3fe2f4ec6c23"></a>

## SRC-3fe2f4ec6c23 — Blender MCP license

Original source: [https://projects.blender.org/lab/blender_mcp/src/branch/main/LICENSE](https://projects.blender.org/lab/blender_mcp/src/branch/main/LICENSE)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-402780a7bc37"></a>

## SRC-402780a7bc37 — Point 07 primary-source check: photographs, depth and learned reconstruction

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-07-sources.md](../action-audit/reviews/point-07-sources.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-40579db9c7a7"></a>

## SRC-40579db9c7a7 — microsoft/TRELLIS.2-4B — Hugging Face model card

Original source: [https://huggingface.co/microsoft/TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B)

Summary: Named TRELLIS.2-4B model card inspected 2026-11-12. Card labels this checkpoint MIT; this claim applies to this model card, not all associated datasets/assets or other model releases.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r10.md.

<a id="src-407da05c0cd4"></a>

## SRC-407da05c0cd4 — Resistor pinned source inputs

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source-job.json`)

Summary: Pins body length,height and lead pitch to the original PDF hash and names ceramic thickness as the required geometry input.

Evidence: implementation_input_artifact.

Documents: research/sources/round-20/component-sources.json.

<a id="src-409fb1abfc4f"></a>

## SRC-409fb1abfc4f — SKF page3 dimensions image

Original source: ${TEMP_ROOT}/opencode/skf-sy20tf-technical-page3.png (`${TEMP_ROOT}/opencode/skf-sy20tf-technical-page3.png`)

Summary: Actual inspected primary page image confirms A1=21mm crown and A=32mm base with housing/mounting/shaft dimensions; supplies visual attribution for original model failure.

Evidence: retained_source_render_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-40beea4e687b"></a>

## SRC-40beea4e687b — Victron Orion24-12 converter (C045) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c045-victron-orion24-12-converter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c045-victron-orion24-12-converter.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; BT; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-40fd07a56db7"></a>

## SRC-40fd07a56db7 — Retained EVShop bare-terminal module illustration

Original source: ${FERME_ROOT}/engineering/module-development/cad/2d_schemas/images/source-pages/leaf-gen2/evshop-photo-original-4566.jpg (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/images/source-pages/leaf-gen2/evshop-photo-original-4566.jpg`)

Summary: Actual source image inspected against current top, terminal-end and isometric views. Pressed pan/ribs, four corner mounts and three bare terminal pedestals identify the exercised external reconstruction.

Evidence: retained_source_image_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-410617a348da"></a>

## SRC-410617a348da — Fibox side-section detail

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-side-detail.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-side-detail.png`)

Summary: Derivedsectioncropretains152.5bodydepth,10footprojection,wall3.8 andcover3.5leaders.

Evidence: derived_pdf_render.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-41482c223014"></a>

## SRC-41482c223014 — Ferme part manifest

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json (`${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json`)

Summary: Existing 103 part records and their identity, route, dependency, source and model-reference fields; proposed catalogue seed.

Evidence: local_source_inspected.

Documents: research/sources/round-07/parts-catalogue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-416cb87ab6bb"></a>

## SRC-416cb87ab6bb — ezdxf repository

Original source: [https://github.com/mozman/ezdxf](https://github.com/mozman/ezdxf)

Summary: Primary source repository and MIT licence metadata.

Evidence: existing_report_registered, web_inspected, installed_package_metadata_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-12/saved-rail-reader-sources.json, research/workflows/details/cad-r04.md.

<a id="src-41a47f716081"></a>

## SRC-41a47f716081 — prior-model-hashes.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/prior-model-hashes.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/prior-model-hashes.json`)

Summary: Pre-build hashes of24 saved DWGs used to confirm existing CAD preservation.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-41bb93ea7d3f"></a>

## SRC-41bb93ea7d3f — nerfstudio_dataparser.py — Nerfstudio main source

Original source: [https://raw.githubusercontent.com/nerfstudio-project/nerfstudio/main/nerfstudio/data/dataparsers/nerfstudio_dataparser.py](https://raw.githubusercontent.com/nerfstudio-project/nerfstudio/main/nerfstudio/data/dataparsers/nerfstudio_dataparser.py)

Summary: Official raw Nerfstudio main-branch parser inspected 2026-11-12; branch is mutable and installed version not checked. Exposes orientation_method=up, center_method=poses, auto_scale_poses=true, scale_factor=1 and scene_scale=1; computes pose transform/scale and emits dataparser_transform/dataparser_scale. Uses metadata orientation_override/applied_transform/applied_scale when supplied, with a fallback COLMAP axis mapping when COLMAP output exists. No runtime parser was executed.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-41c2058cbabf"></a>

## SRC-41c2058cbabf — RGBDImage.h — Open3D v0.20.0 API declaration

Original source: [https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImage.h](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImage.h)

Summary: Official raw Open3D v0.20.0 header inspected 2026-11-12. Declares `CreateFromColorAndDepth` defaults depth_scale=1000.0, depth_trunc=3.0, convert_rgb_to_intensity=true and states scale occurs before truncation; equal-size registered color/depth images are required by RGBDImage contract.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-427835ebb48d"></a>

## SRC-427835ebb48d — Proposed skills linked to reviewed action procedures

Original source: [${MODELING_ROOT}/research/action-audit/skill-to-actions.md](../action-audit/skill-to-actions.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-427c3c0e8259"></a>

## SRC-427c3c0e8259 — V-HACD repository status

Original source: [https://github.com/kmammou/v-hacd/blob/master/README.md](https://github.com/kmammou/v-hacd/blob/master/README.md)

Summary: Upstream repository says V-HACD is archived/end-of-life and directs new development to CoACD.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md.

<a id="src-4285b32bca80"></a>

## SRC-4285b32bca80 — Executed manufacturer assembly import procedure

Original source: [${MODELING_ROOT}/skills/component-cad/references/manufacturer-assembly.md](../../skills/cad-ocs-engineering/references/manufacturer-assembly.md)

Summary: Documents prior import-field reuse,definition/instance counts,inverse source placement diagnosis,guarded correction,persistence,35 saved checks,view differences and source dimensional handoffs.

Evidence: executed_procedure_documentation, executed_case_procedure, applied_case_procedure.

Documents: research/sources/round-20/component-sources.json, research/sources/round-23/enclosure-sources.json, research/sources/round-24/converter-sources.json.

<a id="src-42c5c688de76"></a>

## SRC-42c5c688de76 — NEN — NEN-EN 10210-1:2026 Ontw. en (draft) catalogue entry

Original source: [https://www.nen.nl/nen-en-10210-1-2026-ontw-en-350480](https://www.nen.nl/nen-en-10210-1-2026-ontw-en-350480)

Summary: NEN identifies a 2026 Part 1 delivery-condition text as draft and dates it 1 April 2026. Its scope covers hot-finished hollow sections, including cold-formed product subsequently heat-treated above 580 °C to obtain equivalent properties. Its note says the sectional properties in EN 10210-2 and EN 10219-2 are not equivalent. This is 2026 draft-edition context; the corner-property evidence here comes from the separately inspected 2019 Part 2 documents.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-42ef176046c7"></a>

## SRC-42ef176046c7 — Agent Stuff

Original source: [https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/README.md](https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent Stuff. Source class: repository README. Original reuse terms: Apache-2.0; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-43041e997990"></a>

## SRC-43041e997990 — Existing Victron dimension drawing render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/dimension-drawing.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/dimension-drawing.png`)

Summary: Retained render inspected for exact shared variant,top/front/side arrangement,terminal and casing dimensional labels.

Evidence: derived_source_render_inspected.

Documents: research/sources/round-20/component-sources.json.

<a id="src-43744e9db2f6"></a>

## SRC-43744e9db2f6 — Front attachment crossmember doubler (P08D) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p08d-front-attachment-crossmember-doubler.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p08d-front-attachment-crossmember-doubler.md`)

Summary: Input sheet registered from the inspected ferme manifest: attachments; Front interface support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-43a296901978"></a>

## SRC-43a296901978 — Geometric Image Transformations — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html](https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html)

Summary: OpenCV 4.13.0 documents getPerspectiveTransform from four corresponding source/destination quadrangle points and warpPerspective using a 3×3 transform, output size, interpolation and border modes. The page states that geometric image transforms sample in reverse from destination pixels to source pixels; warpPerspective can take an inverse-map flag. These APIs transform pixel grids and do not establish metric calibration or independent validation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r02.md.

<a id="src-43abef0cc8e8"></a>

## SRC-43abef0cc8e8 — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-isometric.png`)

Summary: Actualpersistedisometricviewshowsassembledenclosureandfourfeet.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-441a0f0e29e3"></a>

## SRC-441a0f0e29e3 — Blickle LS-VLE250K caster reference (C017) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c017-blickle-ls-vle250k-caster-reference.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c017-blickle-ls-vle250k-caster-reference.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Caster reference alternative; original kind project reference envelope. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-447a55563fd3"></a>

## SRC-447a55563fd3 — MuJoCo software repository and licence

Original source: [https://github.com/google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

Summary: Primary repository identifies MuJoCo source code under Apache-2.0 and provides Python bindings; source/docs licences are separately described.

Evidence: existing_report_registered, web_inspected.

Documents: research/domains-and-components.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md.

<a id="src-4489f34f70ef"></a>

## SRC-4489f34f70ef — Driver iteration — audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/audit.json`)

Summary: Original native audit reports116 solids/eight text labels, zero errors/warnings and original file SHA.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-44cb08ec63a1"></a>

## SRC-44cb08ec63a1 — FERME save/reopen implementation reused by rail

Original source: ${FERME_ROOT}/skills/cad-construction/scripts/cadtools/verification.py (`${FERME_ROOT}/skills/cad-construction/scripts/cadtools/verification.py`)

Summary: Existing save_reopen checks audit manifests, dropped entities, output hash and reopened file identity. P01 passed those checks; its detailed reopened feature check separately reports SAB encoding and zero bounds beside a visible nonzero-volume mesh.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-4576a97efe3e"></a>

## SRC-4576a97efe3e — Battery removable hold-down (P20H) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p20h-battery-removable-hold-down.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p20h-battery-removable-hold-down.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Separate geometry per battery route; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-45aee6e7fdff"></a>

## SRC-45aee6e7fdff — Leaf iteration — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/readiness.json`)

Summary: All 14 required feature values and observed source hashes pass SOURCE_READY before geometry checks.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-46011fa591f5"></a>

## SRC-46011fa591f5 — cad-r07.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r07.md](../workflows/details/cad-r07.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-46482507fc3a"></a>

## SRC-46482507fc3a — FreeCAD Assembly Workbench documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md)

Summary: The FreeCAD documentation describes creating root and nested assemblies, inserting components, and grounding/linking objects. It lists fixed, revolute, cylindrical, slider, ball, distance, parallel, perpendicular, angle, rack-and-pinion, screw, gear and belt joints. The link-based workflow leaves source objects outside the assembly and creates links. This is documented assembly behavior; it does not demonstrate the current FreeCAD runtime or STEP round-trip preservation. The documentation repository page reports that its repository was archived on 2026-04-01.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-sources.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-4658b352c90f"></a>

## SRC-4658b352c90f — point-03-web-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-05/point-03-web-sources.json](round-05/point-03-web-sources.json)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-465ffa6730dd"></a>

## SRC-465ffa6730dd — P01 p01-build-01 — rail-record-schema-1.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-record-schema-1.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-record-schema-1.json`)

Summary: p01-build-01 rail-record-schema-1.json: Retained native response with fields annotation_scale_value, current_layer, current_text_style, insertion_units, ltscale, ok, pdmode; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-469662006b7c"></a>

## SRC-469662006b7c — SKF iteration — reopened-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-checks.json`)

Summary: All62 source-bound native checksPASS in derivative document75 after save/reopen, including corrected21mm crown.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-469daa8796cd"></a>

## SRC-469daa8796cd — DXF implementation execution report

Original source: [${MODELING_ROOT}/execution/dxf-inspection.md](../../execution/dxf-inspection.md)

Summary: Records two actual OCS fixture inspections, eight software tests, reused library/source hashing, exact action scope and agent/software responsibility boundaries.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-46a693242819"></a>

## SRC-46a693242819 — Rounded hollow-section OCS helper

Original source: [${MODELING_ROOT}/scripts/rounded_tube.py](../../scripts/rounded_tube.py)

Summary: Source-bound nominal tube builder reuses FERME guarded runtime and geometry modules. The live P01 run established explicit selection readback and bounded-area extrusion; native pre-save checks pass. The reader returns UNKNOWN for reopened SAB records and preserves their raw bytes. Solid and planar subtraction attempts retain their failed routes.

Evidence: authored_code_or_procedure_inspected, local_execution_evidence_inspected, local_execution_source_inspected.

Documents: research/sources/round-11/rail-execution-sources.json, research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-13/crossmember-sources.json.

<a id="src-46f27524d072"></a>

## SRC-46f27524d072 — Driver iteration — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/result.json`)

Summary: DONE driver iteration records derivative SHA,141 saved checks, actual views, preserved original and shared-function improvement with50 tests.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-47301af50b05"></a>

## SRC-47301af50b05 — corrected-records-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-0.json`)

Summary: correctednativeentitysnapshot: 81:Solid3D, 85:Solid3D, 89:Solid3D, 8D:Solid3D, 91:Solid3D, 95:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-47401a0e9609"></a>

## SRC-47401a0e9609 — Controller thermal mounting plate (P21) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p21-controller-thermal-mounting-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p21-controller-thermal-mounting-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; One variant per controller; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-4740401a7d90"></a>

## SRC-4740401a7d90 — Initial Orion source transcription

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/source-notes-initial.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/source-notes-initial.md`)

Summary: Records delegated product mapping,reported price-list row,source ranges andfamily applicability before coordinator manual review.

Evidence: delegated_initial_source_review.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-474e58a9c0ea"></a>

## SRC-474e58a9c0ea — plan_c045.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/plan_c045.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/plan_c045.py`)

Summary: Compared28 source frames withnative inserts andgenerated27 unique reversed-placement corrections.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-47d588ded00a"></a>

## SRC-47d588ded00a — source-linked guide

Original source: [https://majiayu000.github.io/claude-skill-registry/skills/3d-modeling-0127cdf66a41/](https://majiayu000.github.io/claude-skill-registry/skills/3d-modeling-0127cdf66a41/)

Summary: Skills Directory `majiayu000` 3D Modeling ; Directory displays a copied 3D-art skill and 666 stars/25 copies/101 views. Registry's source-linked guide traces the canonical entry to `omer-metin/skills-for-antigravity/skills/3d-modeling/SKILL.md` and lists exact-content copies including `Kedhareswer/kedhar_brain/agents/skills/design-ui-ux/3d-modeling/SKILL.md`. The accessible source SKILL.md covers topology, UVs, game/film exports and art references. Registry page shows Apache-2.0 metadata for omer-metin's copy, while explicitly directing readers to check original permission; the exact original author's licence remains unverified. ; Mesh/art skill, not engineering CAD. Readable source copy was web-inspected; repository source and licence provenance were inspected via the registry guide. It has no stated CAD kernel or AI service dependency. Listing counts and security scan are directory claims, not CAD validation.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-484ebea9c7f7"></a>

## SRC-484ebea9c7f7 — P02 crossmember — pre-save-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/pre-save-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/pre-save-checks.json`)

Summary: Five source-linked native dimension check groups PASS for the260mm crossmember before saving.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-487d52ab6ca8"></a>

## SRC-487d52ab6ca8 — RGBDImage.cpp — Open3D v0.20.0 source

Original source: [https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImage.cpp](https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImage.cpp)

Summary: Official Open3D v0.20.0 source file inspected 2026-11-12. Contains RGBDImage container operations but not the color-depth conversion implementation; no depth-scale claim relies on this file.

Evidence: web_inspected.

Documents: research/sources/round-05/point-07-web-sources.json.

<a id="src-49217bd84235"></a>

## SRC-49217bd84235 — urdf_model/joint.hpp — ros/urdfdom_headers rolling branch

Original source: [https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/joint.hpp)

Summary: Official ROS URDFDOM header on mutable rolling branch, accessed 2026-11-12. Defines joint axis meaning by type, parent-to-joint transform, parent/child link identifiers, and child frame equal to joint frame. No commit pin or runtime parser version checked.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-49518696c006"></a>

## SRC-49518696c006 — Battery native save and same-ID reopen recovery

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/persistence.json`)

Summary: Saved file hash and audit manifest match the reopened document83; native audit reports zero errors/warnings. Original reopen was recovered after repeated bounded pending checks.

Evidence: executed_persistence_result.

Documents: research/sources/round-20/component-sources.json.

<a id="src-4956c1c938ca"></a>

## SRC-4956c1c938ca — ME0907 pinned feature inputs

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source-job.json`)

Summary: Binds 19 dimensions to original PDF/hash/locators, mm frame and mechanical-interface representation. Separately labels cutting overrun and reconstructed R2.39 mm keyway end.

Evidence: implementation_input_artifact.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-49d1aa4fd35a"></a>

## SRC-49d1aa4fd35a — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/reyk/freecad-ai-skill/git/trees/HEAD?recursive=1](https://api.github.com/repos/reyk/freecad-ai-skill/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-49f830258969"></a>

## SRC-49f830258969 — Gland variant and drawn-feature review

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/source-notes.md`)

Summary: Separates exactLG page fromWH datasheet, assigns explicit dimension labels,retains variable length/clamp range meanings and actual CAD acquisition outcomes.

Evidence: delegated_source_review_record.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-4a09800705cd"></a>

## SRC-4a09800705cd — IfcOpenShell code examples

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html](https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html)

Summary: Official end-to-end API examples for creating an IFC project, assigning units, creating contexts and spatial hierarchy, creating a wall and writing IFC.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

<a id="src-4a3c376f9a29"></a>

## SRC-4a3c376f9a29 — P01 p01-build-01 — rail-schema-1.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-1.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-1.json`)

Summary: p01-build-01 rail-schema-1.json: Installed API response document_required: Read state and supply document_id; retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-4a6934063635"></a>

## SRC-4a6934063635 — hashlib — Secure hashes and message digests — Python 3.15.2 documentation

Original source: [https://docs.python.org/3/library/hashlib.html](https://docs.python.org/3/library/hashlib.html)

Summary: Official Python documentation describes hash objects that accept bytes-like input and return a digest for the concatenated bytes; SHA-256 is a documented constructor. For intake, a SHA-256 digest can identify and compare the exact byte content recorded for an input revision. A digest does not establish who supplied the bytes, source authority, correctness or semantic equivalence.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-01-model-brief.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-04/intake-sources.json.

<a id="src-4a6c22d94dd3"></a>

## SRC-4a6c22d94dd3 — MuJoCo XML reference

Original source: [https://mujoco.readthedocs.io/en/latest/XMLreference.html](https://mujoco.readthedocs.io/en/latest/XMLreference.html)

Summary: Official MJCF element reference for body, joints, inertial, mesh assets, geoms and compiler behavior.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r07.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md.

<a id="src-4afcbdb352d9"></a>

## SRC-4afcbdb352d9 — skills-findings.md

Original source: ${EOLIENNES_ROOT}/research/cad-workflow/skills-findings.md (`${EOLIENNES_ROOT}/research/cad-workflow/skills-findings.md`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected.

Documents: research/local-baseline.md, research/sources/local-evidence.json.

<a id="src-4b50dfc03e47"></a>

## SRC-4b50dfc03e47 — imported-blocks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-blocks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-blocks.json`)

Summary: Initial source-covered converter block hierarchy,including heatsink,terminals,cover andhardware.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-4ba8cc4436be"></a>

## SRC-4ba8cc4436be — imported-records-18.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-18.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-18.json`)

Summary: importednativeentitysnapshot: BA:Insert, BB:Insert, BC:Insert, BD:Insert, BE:Insert, BF:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-4bd0fe0b900a"></a>

## SRC-4bd0fe0b900a — Local OCS automation selection implementation

Original source: ${OCS_ROOT}/src/app/automation.rs (`${OCS_ROOT}/src/app/automation.rs`)

Summary: The local select implementation deselects all and selects supplied handles only when clear is not true. This source explains the rail’s observed empty selection; live readback confirms the adapter’s corrected nonempty pick.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-4c99f214f0b2"></a>

## SRC-4c99f214f0b2 — `freecad-scripts/SKILL.md`

Original source: [https://github.com/github/awesome-copilot/blob/main/skills/freecad-scripts/SKILL.md](https://github.com/github/awesome-copilot/blob/main/skills/freecad-scripts/SKILL.md)

Summary: `freecad-scripts` from `github/awesome-copilot` ; Archived skill documents FreeCAD Python console/macros, Part/B-rep primitives, Sketcher constraints, document model and GUI. It expects installed FreeCAD (0.19+, recommends 0.21+/1.0+), bundled Python, optional PySide/Pivy. Repo licence is MIT. ; Useful API reference after version checks, not an automated modeling bridge or tested parametric quality guarantee. Source link: `freecad-scripts/SKILL.md`; archive path gives repository path `skills/freecad-scripts/SKILL.md`.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-4cb8874a1a39"></a>

## SRC-4cb8874a1a39 — pre-save-assembly-measurements.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/pre-save-assembly-measurements.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/pre-save-assembly-measurements.json`)

Summary: 27 source-corrected instance paths andactual pre-save point geometry.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-4cbe441f37a2"></a>

## SRC-4cbe441f37a2 — cad-r04.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r04.md](../workflows/details/cad-r04.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-4cc49dfadc47"></a>

## SRC-4cc49dfadc47 — Upper deck panel (P04) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p04-upper-deck-panel.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p04-upper-deck-panel.md`)

Summary: Input sheet registered from the inspected ferme manifest: frame; Common deck proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered, local_source_or_execution_record_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-15/leaf-sources.json.

<a id="src-4d1602b2855e"></a>

## SRC-4d1602b2855e — https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html

Original source: [https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html](https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html)

Summary: Four page attempts failed and support no technical claim: Open3D 0.20.0 `RGBDImage` API page `https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html` timed out; versioned API URL `https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html` was unavailable via the web tool; GitHub HTML for `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp` returned cache miss; and `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp` returned cache miss. The default parameters were verified in the successful raw v0.20.0 `RGBDImage.h` declaration; conversion behavior was inspected in the raw `RGBDImageFactory.cpp` and `Image.cpp` sources recorded above. No further failed URLs support technical claims.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-4d2254355a66"></a>

## SRC-4d2254355a66 — P01 p01-build-01 — rail-first-measure.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-first-measure.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-first-measure.json`)

Summary: p01-build-01 rail-first-measure.json: Retained native response with fields document_id, geometry_revision, measurements, ok; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-4d342aad4f2b"></a>

## SRC-4d342aad4f2b — imported-records-12.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-12.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-12.json`)

Summary: importednativeentitysnapshot: A8:Insert, A9:Insert, AA:Insert, AE:Solid3D, B2:Solid3D, B6:Solid3D. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-4d3746ad7211"></a>

## SRC-4d3746ad7211 — ezdxf ACIS body/entity reference definitions

Original source: ${NATIVE_READER_ROOT}/ezdxf/acis/entities.py (`${NATIVE_READER_ROOT}/ezdxf/acis/entities.py`)

Summary: Body/lump/shell/face/coedge definitions describe parent and partner relationships. These existing definitions and the observed record layout guide the adapter’s body traversal and reciprocal partner checks.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-4d871dcad456"></a>

## SRC-4d871dcad456 — P01 p01-build-01 — rail-schema-2.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-2.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-2.json`)

Summary: p01-build-01 rail-schema-2.json: Installed API response document_required: Read state and supply document_id; retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-4d88a7d32b7f"></a>

## SRC-4d88a7d32b7f — Detailed point procedures and reviews

Original source: [${MODELING_ROOT}/research/action-audit/point-index.md](../action-audit/point-index.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-4dbc6baf3db1"></a>

## SRC-4dbc6baf3db1 — Point 07 visual and evidence review — photographs, depth and learned reconstruction

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-07-visual.md](../action-audit/reviews/point-07-visual.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-4de79e2f8bfe"></a>

## SRC-4de79e2f8bfe — Caster joint spacer or bush (P05S) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p05s-caster-joint-spacer-or-bush.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p05s-caster-joint-spacer-or-bush.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Removable caster support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-4e6ff41dcd81"></a>

## SRC-4e6ff41dcd81 — P02 crossmember — view-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/view-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/view-journal.jsonl`)

Summary: Retains guarded end/isometric camera commands and actual capture requests for the reopened crossmember.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-4e718650fd66"></a>

## SRC-4e718650fd66 — Image.cpp — Open3D v0.20.0 source

Original source: [https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/Image.cpp](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/Image.cpp)

Summary: Official raw source on tag v0.20.0 inspected 2026-11-12. `ConvertDepthToFloatImage` creates float depth, divides by depth_scale, and sets samples >= depth_trunc to zero; raw zeros remain zero after division. This establishes source-code behavior for this pinned tag.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-4eb42ece1132"></a>

## SRC-4eb42ece1132 — imported-records-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-0.json`)

Summary: imported native record snapshot: 81:Solid3D, 85:Insert, 89:Solid3D, 8D:Solid3D, 91:Solid3D, 95:Solid3D. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-4f0c8d392a38"></a>

## SRC-4f0c8d392a38 — component-work.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/component-work.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/component-work.json`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected, local_execution_evidence_inspected, local_execution_source_inspected, local_source_or_execution_record_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-11/rail-execution-sources.json, research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-13/crossmember-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json.

<a id="src-4f49d9c8767a"></a>

## SRC-4f49d9c8767a — PRO-M ring to rim adapter (P14SM) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p14sm-pro-m-ring-to-rim-adapter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p14sm-pro-m-ring-to-rim-adapter.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Sumitomo PRO-M; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-4f8a40b0e12a"></a>

## SRC-4f8a40b0e12a — TripoSR source licence

Original source: [https://github.com/VAST-AI-Research/TripoSR/blob/main/LICENSE](https://github.com/VAST-AI-Research/TripoSR/blob/main/LICENSE)

Summary: Repository code is MIT licensed; check weights/dependencies and input/output rights separately.

Evidence: web_inspected.

Documents: research/sources/round-03/domain-detail-sources.json.

<a id="src-4fe74310edd3"></a>

## SRC-4fe74310edd3 — Part Design concepts

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_and_PartDesign.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_and_PartDesign.md)

Summary: Primary sources: FreeCAD source/licence, Sketcher Python scripting, Part scripting, Python scripting tutorial, Part Design concepts. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-4fe9c9192b9b"></a>

## SRC-4fe9c9192b9b — SB50 source-stage report

Original source: [${MODELING_ROOT}/execution/c038-sb50-source.md](../../execution/c038-sb50-source.md)

Summary: Documents exactkit,reviewed dimensions,current sourcegate,actual source actions andmodel identities.

Evidence: executed_work_report.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-4ff31c35be7c"></a>

## SRC-4ff31c35be7c — Battery guarded native journal

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/ocs-journal.jsonl`)

Summary: Records isolated document82,successful STEP format/path dialog fields,original import/capture/open identities,13 compare-and-set placement edits,verified save and model views.

Evidence: executed_native_operation_record.

Documents: research/sources/round-20/component-sources.json.

<a id="src-500be17749c8"></a>

## SRC-500be17749c8 — MuJoCo asset decoder plugins

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst)

Summary: Lists built-in OBJ/STL and optional USD mesh/scene decoders and extension mechanisms.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-502c2eec4519"></a>

## SRC-502c2eec4519 — source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/source-job.json`)

Summary: Pre-import SOURCE_READY contract pins exact C045 drawing row andfamilySTEP hashes,mount labels andsource frame.

Evidence: implementation_input_artifact.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-5042379f8832"></a>

## SRC-5042379f8832 — harness-findings.md

Original source: ${EOLIENNES_ROOT}/research/cad-workflow/harness-findings.md (`${EOLIENNES_ROOT}/research/cad-workflow/harness-findings.md`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json.

<a id="src-50b834655ede"></a>

## SRC-50b834655ede — item_ocs_parts.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/item_ocs_parts.py (`${TEMP_ROOT}/opencode/item_ocs_parts.py`)

Summary: extrude, rotate, move, combine and tag provide explicit source-labelled native constructions. Applicability: Imports native-wrapper; dimensions and several recipes are ITEM-specific.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-50e5314209fb"></a>

## SRC-50e5314209fb — Camera Calibration and 3D Reconstruction — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html)

Summary: OpenCV 4.13.0 documents findHomography as a perspective transform between two planes from paired source/target points, with least-squares and robust methods (RANSAC, LMeDS, RHO), a reprojection threshold and inlier mask. The robust algorithms use four-pair subsets and discard collinear subsets; an unestimable homography returns an empty matrix. The same calib3d reference documents undistort(src, cameraMatrix, distCoeffs, ...) as compensation for radial and tangential lens distortion, implemented through a remap. These are geometric API claims, not measured calibration or accuracy results.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-sources.md, research/sources/round-05/point-04-web-sources.json.

<a id="src-5149721d596f"></a>

## SRC-5149721d596f — SPP ZSK0750 trailer coupling (C024) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c024-spp-zsk0750-trailer-coupling.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c024-spp-zsk0750-trailer-coupling.md`)

Summary: Input sheet registered from the inspected ferme manifest: hitch; Trailer ball-coupling proposal; original kind source coupling reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-518a5353a3f2"></a>

## SRC-518a5353a3f2 — Source-intake execution and scope report

Original source: [${MODELING_ROOT}/execution/source-intake.md](../../execution/source-intake.md)

Summary: Records the new implementation, reused helpers, actual four-source capture, twelve tests, agent scope review and staged-publication design.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-51bc1eab5201"></a>

## SRC-51bc1eab5201 — Leaf iteration — header.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/header.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/header.json`)

Summary: Current OCS document header identifies millimetres for source-bound native-coordinate checks.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-51e2013a5b3c"></a>

## SRC-51e2013a5b3c — neugart-ngv064-wheel-160-native.json — recorded_check_results

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json`)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-5211764e8dfb"></a>

## SRC-5211764e8dfb — P02 crossmember — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/readiness.json`)

Summary: Required P02 feature coverage and all pinned source observations return SOURCE_READY before native construction.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-5219c6a1df9e"></a>

## SRC-5219c6a1df9e — step-confirm.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/step-confirm.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/step-confirm.json`)

Summary: Actual completed STEP import confirmation in the isolated converter document.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-522e8d24462e"></a>

## SRC-522e8d24462e — FreeCAD AI Agent Skills Suite

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/README.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD AI Agent Skills Suite. Source class: repository README. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5252655a404a"></a>

## SRC-5252655a404a — https://huggingface.co/tencent/Hunyuan3D-2.1

Original source: [https://huggingface.co/tencent/Hunyuan3D-2.1](https://huggingface.co/tencent/Hunyuan3D-2.1)

Summary: - Hunyuan3D-2.1 model card/license: https://huggingface.co/tencent/Hunyuan3D-2.1

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-5270d066fe0f"></a>

## SRC-5270d066fe0f — Reopened rail document-unit observation

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/document-header.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/document-header.json`)

Summary: OCS header reports insertion_units4, millimetres, for the actual reopened rail document. This records the document coordinate unit independently from the ACIS header metadata.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-528c832b5179"></a>

## SRC-528c832b5179 — ME0907 acquisition response and hash

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/acquisition.json`)

Summary: Records retained PDF path, HTTP status/content type and digest. The coordinator review classifies the retrieved_at field as copied server HTTP Date metadata.

Evidence: executed_acquisition_record.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-529bea09ca56"></a>

## SRC-529bea09ca56 — Existing IFC-to-GLB provenance record

Original source: ${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json (`${ENERGY_SIM_ROOT}/data/real-house-ifc/provenance.json`)

Summary: Existing artifact pattern: source hashes, declared mm-to-m conversion, identity status, runtime and geometry mapping.

Evidence: existing_report_registered, local_reference_registered.

Documents: research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-52d0800bbbcf"></a>

## SRC-52d0800bbbcf — Victron Orion48-24 converter (C044) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c044-victron-orion48-24-converter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c044-victron-orion48-24-converter.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; 44–51.2 V battery routes; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-5336889bffab"></a>

## SRC-5336889bffab — Shared M6 mechanical-family source and model terms

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/followup-shared-m6-outline.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/followup-shared-m6-outline.md`)

Summary: Manufacturer family table and common M6 drawing support proposed shared exterior reuse. Records DigiKey60A STEP listing and concrete internal-use/employer-binding terms; no download control accepted.

Evidence: delegated_web_review_record.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-53486b514e1a"></a>

## SRC-53486b514e1a — ifcopenshell.api.unit.assign_unit — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `assign_unit(file, units=None, length=None, area=None, volume=None)` for default project units. The page identifies defaults of millimetres for length, square metres for area and cubic metres for volume; explicit units can be assigned through supplied unit entities. Project unit assignment is separate from the placement API is_si choice.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md.

<a id="src-53588e078081"></a>

## SRC-53588e078081 — Pilz vector-source observations

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/vector-extraction/extraction.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/vector-extraction/extraction.json`)

Summary: Records exact conversion command,source/output hashes,47 paths andunit/join interpretations requiring verification before3D.

Evidence: executed_vector_inspection.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-536bee2e3614"></a>

## SRC-536bee2e3614 — Blender command-line manual

Original source: [https://docs.blender.org/manual/en/latest/advanced/command_line/](https://docs.blender.org/manual/en/latest/advanced/command_line/)

Summary: Official Blender manual covers background/CLI automation and Python script operation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r05.md, research/workflows/details/dom-r07.md.

<a id="src-5374d3ebf57e"></a>

## SRC-5374d3ebf57e — SolveSpace official site

Original source: [https://solvespace.com/](https://solvespace.com/)

Summary: Primary source: SolveSpace official site, source repository and GPL licence. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-538c56bd7120"></a>

## SRC-538c56bd7120 — FIBOX ARCA IEC 203015T

Original source: [https://www.fibox.com/hubfs/assets/8121020_FIBOX%20ARCA%20IEC%20203015T.pdf](https://www.fibox.com/hubfs/assets/8121020_FIBOX%20ARCA%20IEC%20203015T.pdf)

Summary: Metric rear and side-section views dimension the body, external mounting features, internal mounting-plate features, wall and cover. Dimension leaders and view associations are transcribed in source-notes.md.

Evidence: downloaded_original.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-53975df039a6"></a>

## SRC-53975df039a6 — Nerfstudio source repository

Original source: [https://github.com/nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio)

Summary: Nerfstudio includes NeRF/Gaussian methods, Apache-2.0 code, and its repository describes CUDA/NVIDIA stack prerequisites.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/rec-r02.md.

<a id="src-53b138cae8c2"></a>

## SRC-53b138cae8c2 — reopened-records-24.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-24.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-24.json`)

Summary: reopenednativeentitysnapshot: C0:Insert, C1:Insert, C2:Insert, C3:Insert, C4:Insert, C5:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-53baa792380a"></a>

## SRC-53baa792380a — SKF iteration — corrected-presave-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/corrected-presave-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/corrected-presave-records.json`)

Summary: Actual post-cut native SAT housing and preserved nineSABsolid records support21mm crown measurement and bytecomparison.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-53f84ab8112a"></a>

## SRC-53f84ab8112a — Coordinate transformations of engineering drawings for 3D reconstruction from orthographic views

Original source: [https://xnjdxb.swjtu.edu.cn/en/article/id/9616](https://xnjdxb.swjtu.edu.cn/en/article/id/9616)

Summary: Journal article describes segmenting engineering drawing views, linking coordinates with intermediate 2.5D frames, and establishing coordinate constraints between views.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r05.md, research/workflows/details/cad-r09.md, research/workflows/details/mix-r08.md.

<a id="src-5458b9b0d8db"></a>

## SRC-5458b9b0d8db — https://github.com/TomekGancarczyk/kata-workshop-cc

Original source: [https://github.com/TomekGancarczyk/kata-workshop-cc](https://github.com/TomekGancarczyk/kata-workshop-cc)

Summary: - MCP Market: “Generate 3D Model” https://mcpmarket.com/tools/skills/generate-3d-model — listing opened. It describes a downloadable Claude Code skill by TomekGancarczyk that calls Fal.ai `fal-ai/sam-3/3d-objects`, performs image/mask segmentation and cloud generation, downloads GLB assets, and emits React Three Fiber/Rapier snippets. The source skill/GitHub repository was identified as https://github.com/TomekGancarczyk/kata-workshop-cc; the skill file itself was not retrieved through the listing's failed “SKILL.md” click, so its complete prompt, dependency list, and behavior remain uninspected. The repository is a MIT-licensed React Three Fiber game workshop starter, not evidence that the hosted model or its generated outputs carry MIT terms. Do not treat the listing's “open” description as evidence of local inference.

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-5502cfd4bd53"></a>

## SRC-5502cfd4bd53 — cad-r05.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r05.md](../workflows/details/cad-r05.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-551ba8137607"></a>

## SRC-551ba8137607 — Retained Sumitomo ECO outline page1, CH52308G10

Original source: [https://assets.sumitomodrive.com/sites/default/files/2023-09/smartris-eco.pdf](https://assets.sumitomodrive.com/sites/default/files/2023-09/smartris-eco.pdf)

Summary: Actual page1 inspected visually:186x116 base,168x98 mounting centres, four13mm holes,84.25/69/72mm heights, nominalM6,19.2mm divider clear space and116.7mm connector span. Pins the independent driver expectations.

Evidence: retained_manufacturer_outline_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-5537b62dfae7"></a>

## SRC-5537b62dfae7 — Sumitomo standard driver CH52308G10G10 (C012) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c012-sumitomo-standard-driver-ch52308g10g10.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c012-sumitomo-standard-driver-ch52308g10g10.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Sumitomo; original kind manufacturer outline reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered, local_source_or_execution_record_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-16/driver-sources.json.

<a id="src-5545b27ec2a0"></a>

## SRC-5545b27ec2a0 — Cross-component feature-check procedure

Original source: [${MODELING_ROOT}/skills/component-cad/references/shared-feature-checks.md](../../skills/cad-ocs-engineering/references/shared-feature-checks.md)

Summary: Explains how an action becomes shared software using independent expectations and actual native measurements. Driver and Leaf mounting-hole patterns exercise one function with different dimensions.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-554c43270f1b"></a>

## SRC-554c43270f1b — IfcOpenShell repository and software licences

Original source: [https://github.com/IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)

Summary: Repository identifies IfcOpenShell as LGPL-3.0-or-later and Bonsai as GPL-3.0-or-later; tool software licences do not license imported assets.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r02.md, research/workflows/details/dom-r07.md.

<a id="src-5561868d066a"></a>

## SRC-5561868d066a — Live reopened rail dimension and topology checks

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/native-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/native-checks.json`)

Summary: Six native check groups PASS: source-defined section/length, X/Y walls, end planes, eight corner surfaces and one connected closed body with18 faces and reciprocal closed partners.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-556d712120d7"></a>

## SRC-556d712120d7 — P01 p01-build-03 — isometric-capture.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/isometric-capture.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/isometric-capture.json`)

Summary: p01-build-03 isometric-capture.json: Completed original isometric capture response, recovered under the same request identity; ties the actual image to reopened document71 and camera state.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-55a8e99c38e5"></a>

## SRC-55a8e99c38e5 — Assembly positioning and mating

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/positioning.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/positioning.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Assembly positioning and mating. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5641ae68d50e"></a>

## SRC-5641ae68d50e — urdf_model/link.hpp — ros/urdfdom_headers rolling branch

Original source: [https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/link.hpp](https://github.com/ros/urdfdom_headers/blob/rolling/include/urdf_model/link.hpp)

Summary: Official ROS URDFDOM header on mutable rolling branch, accessed 2026-11-12. `Link::Inertial` contains an origin pose, mass and six symmetric inertia tensor terms. No unit system is declared by the C++ data structure; ROS SI convention is separately recorded in REP-103.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-56687776c458"></a>

## SRC-56687776c458 — BT OEM169536 geared drive assembly (C013) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c013-bt-oem169536-geared-drive-assembly.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c013-bt-oem169536-geared-drive-assembly.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; BT; original kind donor assembly reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-566a523ea815"></a>

## SRC-566a523ea815 — OCS operation declaration source

Original source: ${OCS_ROOT}/src/mcp_ops.rs (`${OCS_ROOT}/src/mcp_ops.rs`)

Summary: Local source describes activate as switching an open drawing tab;current native activate executed andcompleted in this case.

Evidence: inspected_local_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-56813006b275"></a>

## SRC-56813006b275 — EVEA ME0907 fan cover listing

Original source: [https://www.evea-solutions.com/en/engine-accessories/1372-fan-cover-for-me0907-pmsm-brushless-motor.html](https://www.evea-solutions.com/en/engine-accessories/1372-fan-cover-for-me0907-pmsm-brushless-motor.html)

Summary: Cover reference 150-011; black openwork plastic; three Phillips-head screws. No dimensions published.

Evidence: delegated_web_inspection.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-56b9d47414e7"></a>

## SRC-56b9d47414e7 — Point 04 — Raster drawings and interpreted dimensions

Original source: [${MODELING_ROOT}/research/action-audit/point-04-raster-drawings.md](../action-audit/point-04-raster-drawings.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-56c822eef16f"></a>

## SRC-56c822eef16f — FreeCAD Python API Reference

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/python_api_reference.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/python_api_reference.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Python API Reference. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5780c8aca8ae"></a>

## SRC-5780c8aca8ae — Retained EVShop Leaf Gen2 module listing

Original source: [https://evshop.eu/en/batteries/321-module-from-nissan-leaf-gen-2-24kwh.html](https://evshop.eu/en/batteries/321-module-from-nissan-leaf-gen-2-24kwh.html)

Summary: Actual retained page text inspected: 300 x 222 x 34 mm supplies this reconstruction case convention. Original retrieval metadata remains in the existing provenance register.

Evidence: retained_seller_page_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-57e794a1c1cb"></a>

## SRC-57e794a1c1cb — License

Original source: [https://polyhaven.com/license](https://polyhaven.com/license)

Summary: Poly Haven ; Library of 3D models, materials and HDRI environments useful for scene dressing, architectural visualization and lighting. Asset catalog ; Poly Haven states all site assets are CC0, including commercial use without attribution. This is useful for visual environments and render context; asset dimensions/geometry are not engineering component specifications. License

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-580683a4cc41"></a>

## SRC-580683a4cc41 — Pilz dimension drawing render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source/pilz-p9745-2009094-page-1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source/pilz-p9745-2009094-page-1.png`)

Summary: Actual six-view drawing shows terminal banks andrail-clip profile;coordinator inspected dimension leaders.

Evidence: derived_pdf_render.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-582825becec4"></a>

## SRC-582825becec4 — License text

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/LICENSE](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5860303c6b7e"></a>

## SRC-5860303c6b7e — Importing and Exporting Files — CadQuery Documentation

Original source: [https://cadquery.readthedocs.io/en/stable/importexport.html](https://cadquery.readthedocs.io/en/stable/importexport.html)

Summary: Official CadQuery documentation gives `importers.importDXF(...).wires().toPending().extrude(10)` as a DXF-profile construction path; all DXF layers are imported by default with include/exclude options. `importStep(..., unit=...)` converts declared STEP units to millimetres by default or a selected unit. STEP export writes Workplane geometry; assembly export writes nested STEP with colors but default assembly object names are generated and per-object names are not preserved. Export unit and outputUnit settings can scale coordinates; STL, AMF and 3MF are identified as mesh formats. DXF/SVG/STEP are exchange formats and do not preserve CadQuery's parametric source history; the documented parametric representation is Python code.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-02-component-reuse.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r09.md.

<a id="src-587c68a13074"></a>

## SRC-587c68a13074 — ahujasid/mcp-for-blender

Original source: [https://github.com/ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)

Summary: The separate community project ahujasid/mcp-for-blender is explicitly not affiliated with Blender Foundation. Its package metadata declares MIT, and its current README supports Blender 3.0 or newer, so its stated Blender minimum includes the installed 5.0.1. It provides scene/object inspection and mutation, visual inspection, arbitrary Blender Python execution, and external asset integrations such as Poly Haven, Sketchfab and Poly Pizza. This broader feature set also increases the amount of connected code and network access. The repository documents an opt-in `BLENDER_MCP_SAFE_MODE=1`; that mode is a project feature, not an operating-system sandbox. Package metadata, setup/features/security sections.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/domain-paths.md.

<a id="src-58e9ce4c7811"></a>

## SRC-58e9ce4c7811 — Checkedplacementwritehelper

Original source: [${MODELING_ROOT}/scripts/assembly_repair.py](../../scripts/assembly_repair.py)

Summary: Extractedrepeatedreviewedsource-planwriteactionwithfullinsertpreflight,CAS,matrixreadbackandunchangedACISchecks.

Evidence: implemented_and_exercised_software.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-58eb12a69f1a"></a>

## SRC-58eb12a69f1a — Current rotated Victron 24/12 converter view

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/current-user-view.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/current-user-view.png`)

Summary: Actual inspected image shows cover, heatsink fins, mounting slots, terminal housing and hardware. Its hash differs from the earlier repeated enclosure image.

Evidence: executed_native_capture.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-59097305d36e"></a>

## SRC-59097305d36e — Battery exterior execution report

Original source: [${MODELING_ROOT}/execution/c023-victron-battery.md](../../execution/c023-victron-battery.md)

Summary: Records newly saved native model,actual source reuse,13 placement corrections,21 unchanged definitions,39 instances,35 saved checks and per-source geometry observations.

Evidence: executed_work_report.

Documents: research/sources/round-20/component-sources.json.

<a id="src-599641f63e9d"></a>

## SRC-599641f63e9d — P01 p01-build-03 — reopened-measure.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-measure.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-measure.json`)

Summary: p01-build-03 reopened-measure.json: Reopened native API returns zero bounds alongside nonzero mesh volume252167.41146658108mm³; this records the bounds/mesh discrepancy.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-59bd5a7cb61a"></a>

## SRC-59bd5a7cb61a — https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md

Original source: [https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md](https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md)

Summary: 2. Name: Tesseract; Role: Dimension text candidates with boxes/confidence; humans verify engineering notation.; License: Apache-2.0 upstream.; Apis: tesseract image outputbase -l eng tsv; TSV bbox/confidence review; Dependencies: Tesseract OCR binary plus eng traineddata; TSV output is text candidates only.; Source urls: https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md; https://github.com/tesseract-ocr/tesseract

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md.

<a id="src-5a8b5891ac1d"></a>

## SRC-5a8b5891ac1d — ocs_module.rs

Original source: ${OCS_ROOT}/plugins/opencad-python/src/ocs_module.rs (`${OCS_ROOT}/plugins/opencad-python/src/ocs_module.rs`)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-5afc1d03b483"></a>

## SRC-5afc1d03b483 — OCS session control helper source

Original source: ${CODEX_HOME}/skills/ocs-engineering/scripts/ocs_control.py (`${CODEX_HOME}/skills/ocs-engineering/scripts/ocs_control.py`)

Summary: Session preflight and mutation transport helper for a later authorized live CAD operation.

Evidence: local_source_inspected, local_reference_registered, local_execution_evidence_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-06/implementation-queue-sources.json, research/sources/round-11/rail-execution-sources.json.

<a id="src-5b7a1024db32"></a>

## SRC-5b7a1024db32 — Leaf stack end restraint plate (P17E) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p17e-leaf-stack-end-restraint-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p17e-leaf-stack-end-restraint-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Leaf; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-5b8ba14d70b1"></a>

## SRC-5b8ba14d70b1 — Altec ALT-SB50RAMBKT bracket (C039) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c039-altec-alt-sb50rambkt-bracket.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c039-altec-alt-sb50rambkt-bracket.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Charge port proposal; original kind seller component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-5b8f29b55228"></a>

## SRC-5b8f29b55228 — Shared measured-feature comparisons

Original source: [${MODELING_ROOT}/scripts/feature_checks.py](../../scripts/feature_checks.py)

Summary: Adds source-independent numeric comparison, closed-body connectivity, vertex-range and Cartesian cylindrical-pattern functions. Driver and Leaf checks use the same functions with their own source values; invalid expectations are rejected.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-5c0d49b55a8f"></a>

## SRC-5c0d49b55a8f — Source-checked SKF bearing derivative

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/skf-sy20tf-checked.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/skf-sy20tf-checked.dwg`)

Summary: Native DWG2018 preserves ten solids with housing crown21mm. Original other nine solids remain unchanged before save; reopened dimension checks and persistence pass.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-5c5742981c2f"></a>

## SRC-5c5742981c2f — ShapeKernel upstream LICENSE file

Original source: [https://raw.githubusercontent.com/leap71/LEAP71_ShapeKernel/main/LICENSE](https://raw.githubusercontent.com/leap71/LEAP71_ShapeKernel/main/LICENSE)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: ShapeKernel upstream LICENSE file. Source class: official repository license original, plain text. Original reuse terms: Apache License 2.0; preserve the complete license text and notices.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5c74a56ff439"></a>

## SRC-5c74a56ff439 — Source-bound saved battery geometry checker

Original source: [${MODELING_ROOT}/scripts/battery_module.py](../../scripts/battery_module.py)

Summary: Adds 29 checks for actual saved Leaf shells, case envelope, mounting bore centres and axes, inner walls, nominal terminal bores, contact faces and pedestal sections. Expected values come from the external source job.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json.

<a id="src-5d152842ea12"></a>

## SRC-5d152842ea12 — solid3d.rs

Original source: ${OCS_ROOT}/src/app/command_driver/solid3d.rs (`${OCS_ROOT}/src/app/command_driver/solid3d.rs`)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-5d313d6528a8"></a>

## SRC-5d313d6528a8 — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/ocs-journal.jsonl`)

Summary: Write-aheadactualnativeimport,placement,CAS,save,reopen,captureandrecoveryrequests/results.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-5d32161e7c40"></a>

## SRC-5d32161e7c40 — Holybro PM02V3 module (C055) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c055-holybro-pm02v3-module.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c055-holybro-pm02v3-module.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Auxiliary controller supply proposal; original kind manufacturer hardware reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-5d5609650edf"></a>

## SRC-5d5609650edf — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/mitsuhiko/agent-stuff/git/trees/HEAD?recursive=1](https://api.github.com/repos/mitsuhiko/agent-stuff/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5d973824a4de"></a>

## SRC-5d973824a4de — FreeCAD Addons

Original source: [https://www.freecad.org/addons.php?lang=eng_EN](https://www.freecad.org/addons.php?lang=eng_EN)

Summary: FreeCAD Parts Library ; Community library distributed in FCStd, STEP, STL and BREP, grouped across mechanical, electrical/electronic, architectural, medical, hydraulic, HVAC and piping families. FreeCAD Addons ; FreeCAD's add-on listing identifies the library as CC-BY-3.0. Preserve attribution and license with each copied part; verify the individual component's attribution and source because the collection can contain third-party contributions. FreeCAD software's license does not license each model automatically.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-5dd5375bc1d0"></a>

## SRC-5dd5375bc1d0 — step-source.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/step-source.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/step-source.json`)

Summary: ActualImportFileactionbindingtheexacthashedFiboxSTEPpath.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-5e0d7de82f1b"></a>

## SRC-5e0d7de82f1b — Research record

Original source: [${MODELING_ROOT}/research/research-log.md](../research-log.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-5e5932bb68e1"></a>

## SRC-5e5932bb68e1 — Pipeline formats

Original source: [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/action-audit/reviews/point-07-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r05.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r09.md, research/workflows/domain-paths.md.

<a id="src-5e7bb9363c2a"></a>

## SRC-5e7bb9363c2a — reopened-front.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-front.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-front.png`)

Summary: Actualsavedfrontviewshowsbody/coverseam,lockprojectionandfeet.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-5e95b95a8287"></a>

## SRC-5e95b95a8287 — import/export formats

Original source: [https://github.com/CadQuery/cadquery/blob/master/doc/importexport.rst](https://github.com/CadQuery/cadquery/blob/master/doc/importexport.rst)

Summary: Primary sources: CadQuery repository/licence, official docs, import/export formats. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-5ec353e869e2"></a>

## SRC-5ec353e869e2 — mitsuhiko/agent-stuff OpenSCAD skill

Original source: [https://github.com/mitsuhiko/agent-stuff](https://github.com/mitsuhiko/agent-stuff)

Summary: mitsuhiko/agent-stuff OpenSCAD skill ; Parameterized CSG, command-line render and multi-view review ; Adapt the local OpenSCAD workflow and verify the resulting mesh.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-5eec8caedfa9"></a>

## SRC-5eec8caedfa9 — build123d repository/licence

Original source: [https://github.com/gumyr/build123d](https://github.com/gumyr/build123d)

Summary: Primary sources: build123d repository/licence, official docs, import/export guide. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/next-step-proposal.md.

<a id="src-5ef5b6f41faf"></a>

## SRC-5ef5b6f41faf — Package metadata

Original source: [https://github.com/ahujasid/mcp-for-blender/blob/main/pyproject.toml](https://github.com/ahujasid/mcp-for-blender/blob/main/pyproject.toml)

Summary: The separate community project ahujasid/mcp-for-blender is explicitly not affiliated with Blender Foundation. Its package metadata declares MIT, and its current README supports Blender 3.0 or newer, so its stated Blender minimum includes the installed 5.0.1. It provides scene/object inspection and mutation, visual inspection, arbitrary Blender Python execution, and external asset integrations such as Poly Haven, Sketchfab and Poly Pizza. This broader feature set also increases the amount of connected code and network access. The repository documents an opt-in `BLENDER_MCP_SAFE_MODE=1`; that mode is a project feature, not an operating-system sandbox. Package metadata, setup/features/security sections.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-5f744c173454"></a>

## SRC-5f744c173454 — heatsink-analytic-features.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/heatsink-analytic-features.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/heatsink-analytic-features.json`)

Summary: Existing SAB reader observes heatsink planes,cylinders,cones andloops;R4 slot centres identify174.3×71mm pattern.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-5f9c829cdfd0"></a>

## SRC-5f9c829cdfd0 — Existing manufacturer-source provenance index

Original source: ${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/README.md (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/README.md`)

Summary: Inspected Sumitomo entries identify original ECO/PRO drawing URLs, source descriptions and retained paths; these locate the exact local drawing reused by the iteration.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-6002c90d8336"></a>

## SRC-6002c90d8336 — Implemented immutable source intake

Original source: [${MODELING_ROOT}/scripts/source_intake.py](../../scripts/source_intake.py)

Summary: New script validates source/scope records, preserves exact text and corrections, reuses existing JSON/hash helpers, checks prior revisions and protects completed outputs through staged publication and failure records.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-6038042a0445"></a>

## SRC-6038042a0445 — point-02-web-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-05/point-02-web-sources.json](round-05/point-02-web-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-608f9d6fff1b"></a>

## SRC-608f9d6fff1b — dom-r04.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r04.md](../workflows/details/dom-r04.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-60e0a613e21d"></a>

## SRC-60e0a613e21d — Point 07 — reconstruction software and API review

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-07-software.md](../action-audit/reviews/point-07-software.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-611132c2602f"></a>

## SRC-611132c2602f — Native converter plot attempt

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-isometric.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-isometric.pdf`)

Summary: Actual OCS one-page plot output;subsequent Poppler inspection shows an entirelywhite page. Export completion andfailed visualcontent retained separately.

Evidence: executed_plot_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-618fca25dd4d"></a>

## SRC-618fca25dd4d — corrected-records-30.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-30.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-30.json`)

Summary: corrected native record snapshot: BD:Insert, BE:Insert, BF:Insert, C0:Insert, C1:Insert, C2:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-61c6ad4341d0"></a>

## SRC-61c6ad4341d0 — cad-r03.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r03.md](../workflows/details/cad-r03.md)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-61f08f559e99"></a>

## SRC-61f08f559e99 — Agent skill: freecad-developer

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-developer/SKILL.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-developer/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-developer. Source class: agent skill instructions. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-620ff17ef7cd"></a>

## SRC-620ff17ef7cd — point-07-operations

Original source: [${MODELING_ROOT}/research/action-audit/point-07-operations.json](../action-audit/point-07-operations.json)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-62706c66f40b"></a>

## SRC-62706c66f40b — Query Entities — ezdxf 1.4.5 documentation

Original source: [https://ezdxf.readthedocs.io/en/stable/tasks/query.html](https://ezdxf.readthedocs.io/en/stable/tasks/query.html)

Summary: Official ezdxf documentation describes entity selection from layouts and entity sequences using `query()` with DXF type and attribute expressions. Query results are EntityQuery sequences; unsupported attributes do not match the entity, and assignment to unsupported attributes is silently ignored. This identifies document/entity inspection operations; query results do not normalize units, resolve block insert transforms or classify a profile as a constrained sketch.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-sources.md, research/sources/round-05/point-03-web-sources.json.

<a id="src-62879528068d"></a>

## SRC-62879528068d — reyk/freecad-ai-skill

Original source: [https://github.com/reyk/freecad-ai-skill](https://github.com/reyk/freecad-ai-skill)

Summary: reyk/freecad-ai-skill ; Terminal-to-running-FreeCAD Python bridge ; Compare its session control with a direct local adapter before adopting its bridge.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-63043c7b233e"></a>

## SRC-63043c7b233e — queue

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/queue.md](../action-audit/implementation-queue/queue.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-63185270fad3"></a>

## SRC-63185270fad3 — Additional motor source acquisition manifest

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/acquisition.json`)

Summary: Records URLs, downloaded originals, archive members, byte counts, MIME types and hashes; page-only Autodesk viewer/cache-miss and EVEA CAD-on-request observations remain distinct. Date fields match the recorded HTTP Date and are preserved as reported acquisition metadata.

Evidence: executed_acquisition_record.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-6350270f836a"></a>

## SRC-6350270f836a — https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html

Original source: [https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html)

Summary: Four direct page attempts did not yield page contents: ROS Rolling URDF tutorial (`https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html`, access denied by Anubis); ROS REP-103 mirror (`https://www.ros.org/reps/rep-0103.html`, access denied by Anubis; the source-controlled REP page was inspected successfully instead); Blender glTF manual (`https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html`, HTTP 402); and guessed IfcOpenShell geometry-settings URL (`https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html`, unavailable via the web tool). These failed attempts support no technical claim. Existing source-register records were reused for MuJoCo/IfcOpenShell/CoACD licensing and earlier workflow descriptions; they are not counted as fresh inspection. No local runtime or implementation capability is established by this source audit.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-06-sources.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-63530860ce5d"></a>

## SRC-63530860ce5d — SKF iteration — reopened-audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-audit.json`)

Summary: Reopened derivative has same ten-solid manifest as verified save, zeroerrors/warnings and retained source/file identity.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-6372bc22f3fc"></a>

## SRC-6372bc22f3fc — P01 p01-build-03 — pre-save-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/pre-save-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/pre-save-records.json`)

Summary: p01-build-03 pre-save-records.json: 1 native entity records in document 70, revision 8; stores exact geometry encoding and properties for interpretation independently of PASS labels.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-6398638998c9"></a>

## SRC-6398638998c9 — OpenCADStudio Automation API — Specification 1.1

Original source: ${OCS_ROOT}/docs/automation/API-SPEC.md (`${OCS_ROOT}/docs/automation/API-SPEC.md`)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: OpenCADStudio Automation API — Specification 1.1. Source class: local primary product documentation; exact byte copy from local source repository. Original reuse terms: GPL-3.0-or-later repository license; see ${OCS_ROOT}/LICENSE

Evidence: archived_original_referenced, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/archive-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-64196dacabad"></a>

## SRC-64196dacabad — Independent review — Point 02 component and CAD reuse

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-02-independent.md](../action-audit/reviews/point-02-independent.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-64327fe17901"></a>

## SRC-64327fe17901 — Point 02 source check: existing components and CAD files

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-02-sources.md](../action-audit/reviews/point-02-sources.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-6435b92f204d"></a>

## SRC-6435b92f204d — corrected-records-24.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-24.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-24.json`)

Summary: correctednativeentitysnapshot: C0:Insert, C1:Insert, C2:Insert, C3:Insert, C4:Insert, C5:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-6436ad01395b"></a>

## SRC-6436ad01395b — Camera Models — COLMAP

Original source: [https://colmap.github.io/cameras.html](https://colmap.github.io/cameras.html)

Summary: COLMAP camera-model reference inspected 2026-11-12. Page identifies version 4.3.0.dev0, commit 3c1a1b9 (2026-11-08), and says camera +Z is the look direction. Lists models of varying complexity; SIMPLE_PINHOLE and PINHOLE are for images already undistorted. Projection includes perspective division, distortion and intrinsic transform; COLMAP uses corner-based pixels with top-left pixel centre at (0.5,0.5).

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-647254850698"></a>

## SRC-647254850698 — part_index.py

Original source: [${MODELING_ROOT}/scripts/part_index.py](../../scripts/part_index.py)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: authored_document_or_code_inspected, local_implementation_or_execution_record_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-17/source-intake-sources.json.

<a id="src-64aded16baff"></a>

## SRC-64aded16baff — SKF iteration — source-findings.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/source-findings.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/source-findings.json`)

Summary: Records actual32mm original crown versus SKF21mm and source mass0.56kg versus older0.588kg record.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-6507a5c7f8da"></a>

## SRC-6507a5c7f8da — contract.json

Original source: [${MODELING_ROOT}/research/workflows/details/contract.json](../workflows/details/contract.json)

Summary: Analyst classification contract: independent manual effort, software setup and computing classes; required evidence, input and output fields.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-6523f7bc1fa7"></a>

## SRC-6523f7bc1fa7 — Reviewed SB50 source findings

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/source-notes.md`)

Summary: Links exact blue kit mapping andactual dimension directions;separates mated view,wire contacts,yellow key family andPowerclaw alternative.

Evidence: reviewed_source_interpretation.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-65f2ca319152"></a>

## SRC-65f2ca319152 — OCS state before the requested view recheck

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/state-before.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/state-before.json`)

Summary: Active document 87 is the saved Victron 24/12 converter. The camera records the current user-rotated view before capture.

Evidence: executed_native_state_read.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-66546119d7fd"></a>

## SRC-66546119d7fd — Driver iteration — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/persistence.json`)

Summary: Verified-save SHA, zero dropped entities, preserved manifest and recovered reopened audit all pass for the checked derivative.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-665cfb1ddd3b"></a>

## SRC-665cfb1ddd3b — Original Sumitomo driver drawing

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-smartris-driver-ch52308.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-smartris-driver-ch52308.dwg`)

Summary: Preserved original contains116 solids and eight text labels. Its connector shells span116.85mm; the retained manufacturer drawing gives116.7mm.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-667b0ab089a4"></a>

## SRC-667b0ab089a4 — Side connector mounting panel (P23) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p23-side-connector-mounting-panel.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p23-side-connector-mounting-panel.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Route-specific panel proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-668386d68294"></a>

## SRC-668386d68294 — 2026-11-12-component-led.md

Original source: [${MODELING_ROOT}/execution/2026-11-12-component-led.md](../../execution/2026-11-12-component-led.md)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: authored_document_or_code_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-6712dfc9aea8"></a>

## SRC-6712dfc9aea8 — Retained resistor package drawing render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/Ohmite-TA-Series-page1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/Ohmite-TA-Series-page1.png`)

Summary: Full manufacturer-authored page inspected for TA310PA table,row applicability and PA low-wattage package callouts.

Evidence: derived_source_render_inspected.

Documents: research/sources/round-20/component-sources.json.

<a id="src-672023a44bcd"></a>

## SRC-672023a44bcd — Local OCS bounded-area construction implementation

Original source: ${OCS_ROOT}/src/scene/model/presspull_model.rs (`${OCS_ROOT}/src/scene/model/presspull_model.rs`)

Summary: Local source describes nested planar boundary loops and direct region extrusion. It supported testing PRESSPULL at the wall-interior pick after solid and planar-region Boolean subtraction were refused. The P01 native checks established the actual result.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-6767227cb6dc"></a>

## SRC-6767227cb6dc — CPC-T5008 cable lug (C058) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c058-cpc-t5008-cable-lug.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c058-cpc-t5008-cable-lug.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; M8 terminal example; original kind source terminal reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-67c3aa703e13"></a>

## SRC-67c3aa703e13 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/github/awesome-copilot/git/trees/HEAD?recursive=1](https://api.github.com/repos/github/awesome-copilot/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-68222de9fed6"></a>

## SRC-68222de9fed6 — DXF Units — ezdxf 1.4.5 documentation

Original source: [https://ezdxf.readthedocs.io/en/stable/concepts/units.html](https://ezdxf.readthedocs.io/en/stable/concepts/units.html)

Summary: Official ezdxf documentation states that DXF coordinate values are unitless; document/modelspace units are declared by `$INSUNITS`, and blocks can declare their own units. It states that ezdxf and CAD applications do not implicitly convert block units when inserting a block; the INSERT scaling must be applied explicitly. The documentation says these unit observations are based on BricsCAD experiments and may differ in other CAD applications. A unit declaration is source evidence, not a measured scale check.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-6835419dcf57"></a>

## SRC-6835419dcf57 — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/initial-state.json`)

Summary: NativeOCSbaselineactivedocument83 and6existingopendocumentsbeforecreating84.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-688d8e475957"></a>

## SRC-688d8e475957 — p01-readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-readiness.json`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-68f329d41232"></a>

## SRC-68f329d41232 — Open CASCADE Technology Reference Manual 8.0.1: STEPCAFControl_Writer Class Reference

Original source: [https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___writer.html](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___writer.html)

Summary: The official OCCT API reference describes STEPCAFControl_Writer as exporting a DECAF document to STEP, including assembly shapes, colors and part names. Transfer accepts a document, a label or a sequence of root assemblies; Write emits the produced models. The documented unit helper looks for a length unit on the root label and otherwise uses the Cascade length unit. Name and color output modes are configurable. The dev.opencascade.org URL redirected to the OCCT3D-hosted 8.0.1 manual. This documents API capability, not local behavior or cross-consumer unit and assembly preservation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-sources.md, research/action-audit/reviews/point-03-independent.md, research/action-audit/reviews/point-03-sources.md, research/sources/round-05/point-02-web-sources.json.

<a id="src-695bf75cf83e"></a>

## SRC-695bf75cf83e — Output Format — COLMAP

Original source: [https://colmap.github.io/format.html](https://colmap.github.io/format.html)

Summary: COLMAP current documentation inspected 2026-11-12; no local executable version checked. `images.txt` stores camera world-to-camera projection as Hamilton quaternion QW,QX,QY,QZ and translation TX,TY,TZ, plus camera/image IDs and 2D observations.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-69c044526e3f"></a>

## SRC-69c044526e3f — Point 01 — Descriptions and explicit dimensions to a model brief

Original source: [${MODELING_ROOT}/research/action-audit/point-01-model-brief.md](../action-audit/point-01-model-brief.md)

Summary: Proposed ten-action source-to-model-brief procedure with software, AI and user assignments, four execution modes, per-feature requirements, candidate comparison/merge, eight development components and thirteen future validation cases.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-6a20dc32784d"></a>

## SRC-6a20dc32784d — reopened-blocks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-blocks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-blocks.json`)

Summary: Persisted converter block hierarchy fromsaved document87.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-6a6bf0c0ce39"></a>

## SRC-6a6bf0c0ce39 — PCL SampleConsensusModelCylinder header — master branch

Original source: [https://raw.githubusercontent.com/PointCloudLibrary/pcl/master/sample_consensus/include/pcl/sample_consensus/sac_model_cylinder.h](https://raw.githubusercontent.com/PointCloudLibrary/pcl/master/sample_consensus/include/pcl/sample_consensus/sac_model_cylinder.h)

Summary: The official PCL header defines seven cylinder coefficients in order: point on axis x,y,z; axis direction x,y,z; radius. It declares model size 7, sample size 2, and documents coefficient-based distance, inlier selection, optimization and point projection methods. The master-branch URL is mutable and does not pin a released PCL version; no local source or runtime version was checked.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-independent.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-6a6e188c27d3"></a>

## SRC-6a6e188c27d3 — skill-to-actions

Original source: [${MODELING_ROOT}/research/action-audit/skill-to-actions.json](../action-audit/skill-to-actions.json)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-6a8670ea9c90"></a>

## SRC-6a8670ea9c90 — Independent review — Point 03 vectors, sketches and solids

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-03-independent.md](../action-audit/reviews/point-03-independent.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-6aa38cb021a0"></a>

## SRC-6aa38cb021a0 — Four observed shared comparison action details

Original source: [${MODELING_ROOT}/research/action-audit/shared-check-actions.json](../action-audit/shared-check-actions.json)

Summary: Registers functions, inputs, outputs, prerequisites, measurement limits, agent/software ownership and actual driver/Leaf evidence as implementation details of native verification; original graph boundaries remain.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-6ab8413122ee"></a>

## SRC-6ab8413122ee — redirect destination

Original source: [https://occt3d.com/dev/doc/refman/html/class_s_t_e_p_control___writer.html](https://occt3d.com/dev/doc/refman/html/class_s_t_e_p_control___writer.html)

Summary: 2. The source observation retains the exact supplied OCCT URL and its redirect destination, identifying the served reference as OCCT 8.0.1. It attributes `Transfer(TopoDS_Shape, STEPControl_StepModelType, ...)`, model modes and `Write`/`WriteStream` to the shape-oriented writer. Separate transfer roots remain source API behavior; actual geometry, interpreted units and consumer fidelity retain their future readback requirements.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-03-independent.md, research/action-audit/reviews/point-03-sources.md.

<a id="src-6b239a9bfdd1"></a>

## SRC-6b239a9bfdd1 — SKILL.md

Original source: [${MODELING_ROOT}/skills/component-cad/SKILL.md](../../skills/cad-ocs-engineering/SKILL.md)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: authored_document_or_code_inspected, authored_code_or_procedure_inspected, local_source_or_execution_record_inspected, implemented_skill_guidance.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-11/rail-execution-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json, research/sources/round-23/enclosure-sources.json, research/sources/round-24/converter-sources.json.

<a id="src-6b30ccb4447f"></a>

## SRC-6b30ccb4447f — https://github.com/isl-org/Open3D

Original source: [https://github.com/isl-org/Open3D](https://github.com/isl-org/Open3D)

Summary: - Open3D repository/license: https://github.com/isl-org/Open3D

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-6b70d88d2033"></a>

## SRC-6b70d88d2033 — Driver correction and generic-check iteration report

Original source: [${MODELING_ROOT}/execution/c012-driver.md](../../execution/c012-driver.md)

Summary: Records manufacturer dimensions, original116.85mm versus116.7mm span failure, intact31-solid X2 translation,141 saved checks, actual views and shared-function adoption with50 tests.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-6b9134b4349d"></a>

## SRC-6b9134b4349d — repair_c029.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/repair_c029.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/repair_c029.py`)

Summary: Executedtheextractedhelperagainst16nativeplacements,preserved12ACISdefinitionsandcapturedpostwriteview.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-6bbd844182e8"></a>

## SRC-6bbd844182e8 — https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE

Original source: [https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE](https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE)

Summary: - SAM 3D custom license (covers source, checkpoints and code): https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md.

<a id="src-6c1f23fbb942"></a>

## SRC-6c1f23fbb942 — P02 crossmember — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-isometric.png`)

Summary: Inspected reopened isometric view shows the260mm crossmember longitudinal edges and hollow end section.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-6c38d73efa65"></a>

## SRC-6c38d73efa65 — Frequently Asked Questions — COLMAP

Original source: [https://colmap.github.io/faq.html](https://colmap.github.io/faq.html)

Summary: COLMAP current FAQ inspected 2026-11-12. For OpenCV/Kalibr calibration imported to COLMAP, add 0.5 to cx and cy only to convert integer-centred OpenCV/Kalibr coordinates into COLMAP's corner-based convention; fx, fy and distortion remain unchanged. OPENCV distortion order is k1,k2,p1,p2; FULL_OPENCV adds k3,k4,k5,k6.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r06.md, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-6c38f0dfe089"></a>

## SRC-6c38f0dfe089 — saved-assembly-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/saved-assembly-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/saved-assembly-checks.json`)

Summary: 37 passing saved source-placement,definition point-set andnested-instance checks;source revision values remain separately attributed.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-6c6db30cba74"></a>

## SRC-6c6db30cba74 — CadQuery repository/licence

Original source: [https://github.com/CadQuery/cadquery](https://github.com/CadQuery/cadquery)

Summary: Primary sources: CadQuery repository/licence, official docs, import/export formats. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/next-step-proposal.md.

<a id="src-6ca63dd2611f"></a>

## SRC-6ca63dd2611f — check_ngv064_wheel.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/check_ngv064_wheel.py (`${TEMP_ROOT}/opencode/check_ngv064_wheel.py`)

Summary: sat_features extracts selected SAT cylinders, planes, tori and points; verify checks the wheel. Applicability: Top-level import loads native-wrapper. Restricted SAT fields; one body transform, unit scale; SAB requires a separate supported reader.

Evidence: local_source_inspected, local_execution_evidence_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-11/rail-execution-sources.json.

<a id="src-6ca9f8e9b9c2"></a>

## SRC-6ca9f8e9b9c2 — https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md

Original source: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md)

Summary: 2. https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r08.md.

<a id="src-6cbca4f9761c"></a>

## SRC-6cbca4f9761c — project documentation

Original source: [https://docs.ifcopenshell.org/introduction.html](https://docs.ifcopenshell.org/introduction.html)

Summary: Bonsai / IfcOpenShell ; Bonsai is a native IFC authoring and analysis platform integrated with Blender. IfcOpenShell provides C++/Python APIs, conversion, IDS validation, querying, clash and geometry tools. The documented conversion tool is IfcConvert. Bonsai docs, IfcOpenShell introduction ; IfcOpenShell libraries/tooling: LGPL-3.0-or-later; Bonsai: GPL-3.0-or-later, per project documentation. IFC is an open building data schema; the authoring application remains separately licensed. ; Building authoring and IFC import/export adapter. Use IFC entity relationships and property sets as semantic BIM data; do not flatten the only copy into meshes. Use IDS as machine-readable delivery checks.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r06.md, research/workflows/domain-paths.md.

<a id="src-6cc50a6a40b8"></a>

## SRC-6cc50a6a40b8 — compute_rgbd_odometry — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/python_api/open3d.pipelines.odometry.compute_rgbd_odometry.html](https://www.open3d.org/docs/latest/python_api/open3d.pipelines.odometry.compute_rgbd_odometry.html)

Summary: Open3D 0.20.0 API inspected 2026-11-12. `compute_rgbd_odometry` estimates 6D rigid motion from source and target RGBDImage and returns success, 4x4 motion matrix and 6x6 information matrix. Local trajectory composition direction is not inferred from the pair API alone.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-6d5424825e51"></a>

## SRC-6d5424825e51 — SKF source inspection and completed derivative report

Original source: [${MODELING_ROOT}/execution/c009-bearing.md](../../execution/c009-bearing.md)

Summary: Documents the original32-versus21mm crown defect, native housing-only revision,62saved checks,40tests, preserved original, actual view inspection and applied script/skill improvement.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-6d6dde7514cd"></a>

## SRC-6d6dde7514cd — Drive support gusset (P03G) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p03g-drive-support-gusset.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p03g-drive-support-gusset.md`)

Summary: Input sheet registered from the inspected ferme manifest: frame; Applicable support variant; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-6d7e6a84d972"></a>

## SRC-6d7e6a84d972 — Original SKF construction program

Original source: ${TEMP_ROOT}/opencode/build_skf_geometry.py (`${TEMP_ROOT}/opencode/build_skf_geometry.py`)

Summary: Existing local builder defines outline, mounting slots, seal/ring components and two linear32-to21mm draft wedges. Saved model retained32mm crown; new iteration restores its documented intended draft using nativeSLICE.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-6d89ac359e55"></a>

## SRC-6d89ac359e55 — Published exact request and scope

Original source: [${MODELING_ROOT}/execution/source-intake/live-01/revision/scope.md](../../execution/source-intake/live-01/revision/scope.md)

Summary: Actual Markdown output preserves the supplied request and explicitly limits implementation to the unfinished intake action and its deliverables.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-6df970fcb6f8"></a>

## SRC-6df970fcb6f8 — parts-and-standards.json

Original source: ${FERME_ROOT}/skills/dictionaries/parts-and-standards.json (`${FERME_ROOT}/skills/dictionaries/parts-and-standards.json`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-6e28384e1b5f"></a>

## SRC-6e28384e1b5f — CadQuery LICENSE

Original source: [https://github.com/CadQuery/cadquery/blob/master/LICENSE](https://github.com/CadQuery/cadquery/blob/master/LICENSE)

Summary: Repository license text: Apache-2.0.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r01.md.

<a id="src-6e4167b03b67"></a>

## SRC-6e4167b03b67 — Stop-button acquisition metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/acquisition.json`)

Summary: Retains original source URLs,redirect URL,time/MIME/hash,render metadata andactual verification/login/403 route outcomes.

Evidence: executed_acquisition_record.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-6e6b9cf6af3c"></a>

## SRC-6e6b9cf6af3c — https://alicevision.org/

Original source: [https://alicevision.org/](https://alicevision.org/)

Summary: - AliceVision official project (MPL-2.0; workflows): https://alicevision.org/

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md.

<a id="src-6e7a85a22dae"></a>

## SRC-6e7a85a22dae — WISKA-ESKV-25-page-3.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page-3.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page-3.png`)

Summary: RenderedWH datasheet page3:axialschematic withTL,L,D,SW/E leaders.

Evidence: derived_pdf_render.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-6e8a1b7fa38b"></a>

## SRC-6e8a1b7fa38b — Resistor PDF acquisition metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/acquisition.json`)

Summary: Retains exact URL,HTTP content type/status,174915bytes,digest and reported file timestamp. Server HTTP Date is separate; coordinator timezone correction is explicit.

Evidence: executed_acquisition_record.

Documents: research/sources/round-20/component-sources.json.

<a id="src-6e951925cbb7"></a>

## SRC-6e951925cbb7 — Noyron — a foundational Large Computational Engineering Model

Original source: [https://leap71.com/noyron/](https://leap71.com/noyron/)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: Noyron — a foundational Large Computational Engineering Model. Source class: official company product-description HTML; claims, not independent validation. Original reuse terms: Website copyright LEAP 71; all rights reserved per page. No reuse licence identified.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-6f5062ead541"></a>

## SRC-6f5062ead541 — Project cross-domain workflow recipes and additional ideas

Original source: [${MODELING_ROOT}/research/workflows/combined-paths.json](../workflows/combined-paths.json)

Summary: Original project proposals combining CAD, photogrammetry, controls, component libraries, IFC and robot models, with named artifact roles and explicit handoff conditions. Also records concept-image and procedural-field research questions.

Evidence: local_source_inspected.

Documents: research/sources/round-02/project-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-6f5dbc4f4bd8"></a>

## SRC-6f5dbc4f4bd8 — reopened-records-30.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-30.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-30.json`)

Summary: reopened native record snapshot: BD:Insert, BE:Insert, BF:Insert, C0:Insert, C1:Insert, C2:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-6f832566dcde"></a>

## SRC-6f832566dcde — corrected-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-isometric.png`)

Summary: Actualpostpropertycorrectioncapturestillshowsdisplacedviewportgeometry;retainedwithactualmatrixreadbacks.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-6fdd6f04d055"></a>

## SRC-6fdd6f04d055 — cad-r08.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r08.md](../workflows/details/cad-r08.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-7018bc2fbb81"></a>

## SRC-7018bc2fbb81 — Product CAD

Original source: [https://www.noritake-elec.com/support/3d-cad-data?id=cu22042-y1a&part=CU22042-Y100](https://www.noritake-elec.com/support/3d-cad-data?id=cu22042-y1a&part=CU22042-Y100)

Summary: Manufacturer product CAD ; Vendor sites commonly provide STEP/IGES for configured product models. For example, NORITAKE offers STEP/IGES for named product CU22042-Y100 and warns files may be incomplete, inaccurate, not to scale or outdated, under vendor terms. Product CAD. CONTEC terms expressly limit use and prohibit changing/adapting its CAD data. ; Downloadability is not an open license. Store the exact terms and source URL with each asset. Default to private project use only as the terms allow; do not redistribute vendor files or converted derivatives absent permission.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-70208d220176"></a>

## SRC-70208d220176 — Deck support ledge (P04L) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p04l-deck-support-ledge.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p04l-deck-support-ledge.md`)

Summary: Input sheet registered from the inspected ferme manifest: frame; Common deck proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-702aefd0f6c1"></a>

## SRC-702aefd0f6c1 — imported-query.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-query.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-query.json`)

Summary: Importedentityhandle/typeinventoryusedforboundedrecordreads.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-703184413ae8"></a>

## SRC-703184413ae8 — Delegated initial motor drawing transcription

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/source-notes.md`)

Summary: Initial Luna-assigned transcription of the retained drawing. Its mounting group, thread-depth and tolerance associations are preserved with separate coordinator corrections; actual delegated runtime identity unavailable.

Evidence: initial_transcription_with_reviewed_corrections.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-704288e14b9b"></a>

## SRC-704288e14b9b — Caster clevis cheek (P05A) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p05a-caster-clevis-cheek.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p05a-caster-clevis-cheek.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Removable caster support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-707585d22a36"></a>

## SRC-707585d22a36 — Tyro Indus1S handheld stop remote (C056) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c056-tyro-indus1s-handheld-stop-remote.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c056-tyro-indus1s-handheld-stop-remote.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Handheld operator equipment; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-70879a2c2cb0"></a>

## SRC-70879a2c2cb0 — TechDraw ExportPageSVG — FreeCAD documentation main branch

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_ExportPageSVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_ExportPageSVG.md)

Summary: Official FreeCAD documentation repository page inspected 2026-11-12 as targeted DOM-25 follow-up. Documents `TechDrawGui.exportPageAsSvg(DrawPageObject, FilePath)` for macros/Python console when the FreeCAD GUI module is active. The page states hatch patterns are not exported and text positions/sizes may be inaccurate. Repository was archived 2026-04-01; documentation page does not pin a FreeCAD release.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-708aa14d658e"></a>

## SRC-708aa14d658e — Gland source acquisition metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/acquisition.json`)

Summary: Records original PDF and HTML hashes,URLs,retrieval outcomes,rendered images and exact-order CAD selector availability.

Evidence: executed_acquisition_record.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-70f3c3558125"></a>

## SRC-70f3c3558125 — native-plot-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-isometric.png`)

Summary: ActualnativeplotPDF render is entirelywhite;pixel extrema andvisualcheck recorded.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-717a1bbd2f70"></a>

## SRC-717a1bbd2f70 — dom-r05.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r05.md](../workflows/details/dom-r05.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-71c2ebea0058"></a>

## SRC-71c2ebea0058 — Ferme component input index

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/README.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/README.md`)

Summary: Existing component sheet and source/model dependency index; relationship to proposed catalogue.

Evidence: local_source_inspected.

Documents: research/sources/round-07/parts-catalogue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-71dee9d2e674"></a>

## SRC-71dee9d2e674 — Visual interpretation review — descriptions and explicit dimensions to a model brief

Original source: [${MODELING_ROOT}/research/action-audit/reviews/visual-review.md](../action-audit/reviews/visual-review.md)

Summary: Authored audit document recording Visual interpretation review — descriptions and explicit dimensions to a model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-71df4a24323d"></a>

## SRC-71df4a24323d — Point 06 primary-source check: building and robot structure and properties

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-06-sources.md](../action-audit/reviews/point-06-sources.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-724b2d11a6eb"></a>

## SRC-724b2d11a6eb — DA3 Streaming README — main branch

Original source: [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md)

Summary: Official mutable main README inspected 2026-11-12. Documents camera pose and intrinsic text files, combined point cloud PLY and optional per-frame RGB/depth/confidence outputs. Peak VRAM table depends on named datasets, resolutions, chunk sizes and overlap; it is not a universal resource requirement.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md.

<a id="src-72fd254a4766"></a>

## SRC-72fd254a4766 — P01 p01-build-01 — source-job-r02.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/source-job-r02.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/source-job-r02.json`)

Summary: p01-build-01 source-job-r02.json: Immutable source revision2 binds P01 proposed dimensions to the researched6/3mm nominal corner convention, pinned source hashes and local XY/+Z frame. It supersedes revision1 for this build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-7300061feed8"></a>

## SRC-7300061feed8 — Amphenol AHDBM04-24-91PN receptacle (C040) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c040-amphenol-ahdbm04-24-91pn-receptacle.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c040-amphenol-ahdbm04-24-91pn-receptacle.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Agricultural interface provision; original kind manufacturer source reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-735d336832fb"></a>

## SRC-735d336832fb — Schneider XB5AA31 reset button (C050) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c050-schneider-xb5aa31-reset-button.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c050-schneider-xb5aa31-reset-button.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Local reset equipment; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-73c5c15a332f"></a>

## SRC-73c5c15a332f — Driver iteration — source-job-r01.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/source-job-r01.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/source-job-r01.json`)

Summary: Original pinned source-job revision retains temporary original-builder source paths used for the first check.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-740290c1bc47"></a>

## SRC-740290c1bc47 — SKF iteration — source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/source-job.json`)

Summary: Pins required SKF and reconstruction feature values, evidence status, source pages and hashes; names ten components and the existing local coordinate frame.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-744990fc5c15"></a>

## SRC-744990fc5c15 — Fibox dimension-leader corrections

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/coordinator-review.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/coordinator-review.md`)

Summary: Recordsactualimageassociationreview:152.5fromrearbodyplane;261.5×161innerbodyopening;keepsinitialnotes andsavedMPSplate observationsseparate.

Evidence: executed_coordinator_review.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-74d5d4738857"></a>

## SRC-74d5d4738857 — Source contract findings and implementation conditions

Original source: [${MODELING_ROOT}/research/action-audit/findings.md](../action-audit/findings.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-74d8fd75f81f"></a>

## SRC-74d8fd75f81f — reopened-blocks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-blocks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-blocks.json`)

Summary: Persistedblockmembershipreadbackfromsaved/reopeneddocument85.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-7508372349a9"></a>

## SRC-7508372349a9 — Pilz source/vector-stage report

Original source: [${MODELING_ROOT}/execution/c048-pilz-source.md](../../execution/c048-pilz-source.md)

Summary: Documents exact relay sources,dimensions,blocked STEP route andactual2D vector extraction withseparate reconstruction proposal.

Evidence: executed_work_report.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-750882b224a7"></a>

## SRC-750882b224a7 — battery_ocs_parts.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/battery_ocs_parts.py (`${TEMP_ROOT}/opencode/battery_ocs_parts.py`)

Summary: rr, axial_x, face_x and tag reuse rounded sections, transforms and metadata. Applicability: Imports item and session wrappers; caller must supply source-backed geometry.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-75511277c637"></a>

## SRC-75511277c637 — TripoSR inference README

Original source: [https://github.com/VAST-AI-Research/TripoSR/blob/main/README.md](https://github.com/VAST-AI-Research/TripoSR/blob/main/README.md)

Summary: Official README command is `python run.py <image> --output-dir <dir>`; it states about 6 GB VRAM per single image and MIT terms for code and pretrained models.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r10.md, research/workflows/reconstruction-paths.md.

<a id="src-75dbfddac2b8"></a>

## SRC-75dbfddac2b8 — Geometry processing — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html)

Summary: IfcOpenShell 0.9.0post1 documentation accessed 2026-11-12. Documents create_shape element/representation processing, triangle and OpenCASCADE B-rep routes, geometry iterator, local vertices plus transformation matrix, opening subtraction defaults, and GLB serializer settings including meter unit declaration and optional element GUIDs.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-75ebd4f71d22"></a>

## SRC-75ebd4f71d22 — source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source-job.json`)

Summary: PinnedSTEP/drawinggeometrycontractforexact203015Tvariantandretainedsourceframe.

Evidence: implementation_input_artifact.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-7606cf6527a4"></a>

## SRC-7606cf6527a4 — Implemented source-intake skill

Original source: [${MODELING_ROOT}/skills/source-intake/SKILL.md](../../skills/cad-source-intake/SKILL.md)

Summary: Documents the actual input schema, command, output layout, failure exit codes, recovery, reusable completed revisions and agent/software responsibility boundary.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-76b9efd76055"></a>

## SRC-76b9efd76055 — OpenMVS Usage Guide — develop branch

Original source: [https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md](https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md)

Summary: Official OpenMVS usage guide on mutable develop branch inspected 2026-11-12. Documents COLMAP image_undistorter output, `InterfaceCOLMAP -i dense -o scene.mvs --image-folder dense/images`, DensifyPointCloud, ReconstructMesh, optional refinement/texturing, a CPU SGM route and memory sub-scene splitting that may leave seams.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-76f855deeb5a"></a>

## SRC-76f855deeb5a — XB5AS8445 dimension render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/schneider-xb5as8445-page-3.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source/schneider-xb5as8445-page-3.png`)

Summary: Actual exactpart image givesØ40 operator,43 overall height,39.5 front and43 rear projections,1–6mm panel range.

Evidence: derived_pdf_render.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-773aa3a5f61a"></a>

## SRC-773aa3a5f61a — CAD Modeling Pattern Library

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/cad_modeling_patterns.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/cad_modeling_patterns.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: CAD Modeling Pattern Library. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-77594e51ac89"></a>

## SRC-77594e51ac89 — Existing operation inventory and detailed-review state

Original source: [${MODELING_ROOT}/research/action-audit/operation-inventory.md](../action-audit/operation-inventory.md)

Summary: Authored audit document recording Existing operation inventory and detailed-review state. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json.

<a id="src-777fed96f232"></a>

## SRC-777fed96f232 — Local OCS plane-slice command implementation

Original source: ${OCS_ROOT}/src/modules/model/slice_cmd.rs (`${OCS_ROOT}/src/modules/model/slice_cmd.rs`)

Summary: Inspected constructor and point-state handling establish preselected target, three plane points and retained-side point; live installedSLICE subsequently completed both intended housing cuts.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-785d8cbc2541"></a>

## SRC-785d8cbc2541 — rec-r07.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r07.md](../workflows/details/rec-r07.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-789932d05ce2"></a>

## SRC-789932d05ce2 — 3D reconstruction research report

Original source: [${MODELING_ROOT}/research/reconstruction.md](../reconstruction.md)

Summary: Prior repository report assesses image/depth reconstruction methods, source terms and prerequisites. This batch references it for scan-to-CAD transition context and does not repeat that research.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-792e6e233cf9"></a>

## SRC-792e6e233cf9 — reopened-records-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-0.json`)

Summary: reopenednativeentitysnapshot: 81:Solid3D, 85:Solid3D, 89:Solid3D, 8D:Solid3D, 91:Solid3D, 95:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-7986969c7a59"></a>

## SRC-7986969c7a59 — Point 06 designer notes — building and robot structure and properties

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-06-designer.md](../action-audit/reviews/point-06-designer.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-79edac842934"></a>

## SRC-79edac842934 — Actual native insertion corrections

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/placement-corrections.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/placement-corrections.json`)

Summary: Readback records show each of13 native insert matrices matching the reviewed source frame after compare-and-set normal,rotation and position updates.

Evidence: executed_native_correction_result.

Documents: research/sources/round-20/component-sources.json.

<a id="src-79f9dd42f446"></a>

## SRC-79f9dd42f446 — step.rs

Original source: ${OCS_ROOT}/src/io/step.rs (`${OCS_ROOT}/src/io/step.rs`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json.

<a id="src-7a5a898279b3"></a>

## SRC-7a5a898279b3 — Pilz source acquisition findings

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source/source-notes.md`)

Summary: Records exact774310 mapping,manufacturer source dimensions,STEP403 andbacked mirror route.

Evidence: delegated_source_review_record.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-7a9b6fde0c01"></a>

## SRC-7a9b6fde0c01 — reconstruction-paths.json

Original source: [${MODELING_ROOT}/research/workflows/reconstruction-paths.json](../workflows/reconstruction-paths.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-7b3c4ff0a101"></a>

## SRC-7b3c4ff0a101 — source SKILL.md

Original source: [https://github.com/omer-metin/skills-for-antigravity/blob/main/skills/3d-modeling/SKILL.md](https://github.com/omer-metin/skills-for-antigravity/blob/main/skills/3d-modeling/SKILL.md)

Summary: Skills Directory `majiayu000` 3D Modeling ; Directory displays a copied 3D-art skill and 666 stars/25 copies/101 views. Registry's source-linked guide traces the canonical entry to `omer-metin/skills-for-antigravity/skills/3d-modeling/SKILL.md` and lists exact-content copies including `Kedhareswer/kedhar_brain/agents/skills/design-ui-ux/3d-modeling/SKILL.md`. The accessible source SKILL.md covers topology, UVs, game/film exports and art references. Registry page shows Apache-2.0 metadata for omer-metin's copy, while explicitly directing readers to check original permission; the exact original author's licence remains unverified. ; Mesh/art skill, not engineering CAD. Readable source copy was web-inspected; repository source and licence provenance were inspected via the registry guide. It has no stated CAD kernel or AI service dependency. Listing counts and security scan are directory claims, not CAD validation.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-7b3f397d3342"></a>

## SRC-7b3f397d3342 — P02 crossmember — iso-capture.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/iso-capture.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/iso-capture.json`)

Summary: Completed isometric capture response binds the actual crossmember image to its native document and camera.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-7baec7354391"></a>

## SRC-7baec7354391 — https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html

Original source: [https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html](https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html)

Summary: Four page attempts failed and support no technical claim: Open3D 0.20.0 `RGBDImage` API page `https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html` timed out; versioned API URL `https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html` was unavailable via the web tool; GitHub HTML for `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp` returned cache miss; and `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp` returned cache miss. The default parameters were verified in the successful raw v0.20.0 `RGBDImage.h` declaration; conversion behavior was inspected in the raw `RGBDImageFactory.cpp` and `Image.cpp` sources recorded above. No further failed URLs support technical claims.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-7bc0b8d43055"></a>

## SRC-7bc0b8d43055 — SB50 source-readiness result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/readiness.json`)

Summary: Existing required-feature/hash gate returns NEEDS_INPUT forblue housing seating/key geometry andcontact transition/blade.

Evidence: executed_readiness_result.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-7bd91f2e39d7"></a>

## SRC-7bd91f2e39d7 — Completed current-view capture response

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/capture-result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/capture-result.json`)

Summary: Actual completed response for the original capture request c045-view-recheck-20261113:current-user-view.

Evidence: executed_capture_result.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-7be225e2793e"></a>

## SRC-7be225e2793e — cad-detail-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-03/cad-detail-sources.json](round-03/cad-detail-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-7c108255a4eb"></a>

## SRC-7c108255a4eb — provenance.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/provenance.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/provenance.json`)

Summary: Actual temporary driver paths,retained hashes andoriginal bootstrap dependency conditions.

Evidence: execution_provenance_record.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-7c623f2c8b68"></a>

## SRC-7c623f2c8b68 — FreeCAD Modeling Best Practices & TNP Mitigation

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/modeling_best_practices.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/modeling_best_practices.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Modeling Best Practices & TNP Mitigation. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-7c655a6cf054"></a>

## SRC-7c655a6cf054 — Retained VT-Tech Leaf reuse article

Original source: [https://vt-tech.eu/en/articles/ev-transport/7-nissan-leaf-salvaged-battery-modules](https://vt-tech.eu/en/articles/ev-transport/7-nissan-leaf-salvaged-battery-modules)

Summary: Actual retained article inspected: 9.1 mm mounting holes and M6 power/M4 tap terminals support nominal bore geometry. Its combined Gen1/Gen2 case dimensions 303 x 223 x 35 mm retain their separate attribution.

Evidence: retained_reuse_source_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-7c8a5bf54e7c"></a>

## SRC-7c8a5bf54e7c — Electrical equipment bracket (P22) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p22-electrical-equipment-bracket.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p22-electrical-equipment-bracket.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Route-specific equipment support; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-7c8bdf666637"></a>

## SRC-7c8bdf666637 — mount-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/mount-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/mount-checks.json`)

Summary: Two passing R4-slot/count andvertical-pitch checks;records STEP174.3 vsdrawing174 pitch and186.6 vs187 flange observation.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-7cd4f7a294b2"></a>

## SRC-7cd4f7a294b2 — imported-records-24.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-24.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-records-24.json`)

Summary: importednativeentitysnapshot: C0:Insert, C1:Insert, C2:Insert, C3:Insert, C4:Insert, C5:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-7d065c90de76"></a>

## SRC-7d065c90de76 — Saved Victron24/12 native assembly

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/victron-orion-tr-smart-24-12-30a.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/victron-orion-tr-smart-24-12-30a.dwg`)

Summary: New DWG2018 has9 solid definitions and27 source-corrected instances;39 numeric checks pass andvisual identity check remainsFAIL.

Evidence: executed_native_cad_artifact.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-7d7038c13789"></a>

## SRC-7d7038c13789 — FreeCAD AI

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/README.md](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD AI. Source class: repository README. Original reuse terms: permissive terms as archived; GitHub API SPDX=ISC; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-7d74315cc8c4"></a>

## SRC-7d74315cc8c4 — Placement and instance traversal regression cases

Original source: [${MODELING_ROOT}/tests/test_step_placements.py](../../tests/test_step_placements.py)

Summary: Ten passing software cases cover direct source axes,observed inverse mapping,already-correct/ambiguous/unsupported inputs,nested repeated paths,cycles and instance bounds.

Evidence: implementation_test_artifact.

Documents: research/sources/round-20/component-sources.json.

<a id="src-7db7da4f6264"></a>

## SRC-7db7da4f6264 — Tube-corner source observations

Original source: [${MODELING_ROOT}/research/sources/round-10/tube-corner-sources.json](round-10/tube-corner-sources.json)

Summary: Individual delegated web observations, exact standard clauses, supplier listing details, catalogue edition evidence, access failures and existing FERME sheet relationships underpin the tube-corner report. Each source retains its own concrete summary and evidence status.

Evidence: authored_research_document_inspected.

Documents: research/sources/round-10/tube-corner-local-sources.json.

<a id="src-7dbfb81bf992"></a>

## SRC-7dbfb81bf992 — P01 p01-build-01 — rail-type-Solid3D.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-type-Solid3D.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-type-Solid3D.json`)

Summary: p01-build-01 rail-type-Solid3D.json: Retained native response with fields collection, definitions, editing, fields, notes, ok, record_type; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-7e07ebce5d02"></a>

## SRC-7e07ebce5d02 — check_c045_mounts.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/check_c045_mounts.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/check_c045_mounts.py`)

Summary: Read fourR4 mount-slot ends,computed71/174.3mm pitches anddetected byte-identical captures.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-7e97117530b1"></a>

## SRC-7e97117530b1 — P02 crossmember — reopened-end.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-end.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-end.png`)

Summary: Inspected reopened end view shows the outer and inner rounded-square section of the P02 hollow crossmember.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-7ec6b1588bb0"></a>

## SRC-7ec6b1588bb0 — P01 p01-build-03 — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-isometric.png`)

Summary: Reopened isometric capture shows the P01 rail longitudinal edges and hollow section. The original asynchronous capture request completed through same-ID recovery.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-7f544def9af7"></a>

## SRC-7f544def9af7 — Robot tow ball (C025) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c025-robot-tow-ball.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c025-robot-tow-ball.md`)

Summary: Input sheet registered from the inspected ferme manifest: hitch; Trailer ball-coupling proposal; original kind mating component input. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-7f6eca002620"></a>

## SRC-7f6eca002620 — AMP 520BS10HT-7-8 motor sprocket (C006) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c006-amp-520bs10ht-7-8-motor-sprocket.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c006-amp-520bs10ht-7-8-motor-sprocket.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907 chain example; original kind source component interface example. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-7f7508ffab83"></a>

## SRC-7f7508ffab83 — Potrace: a polygon-based tracing algorithm

Original source: [https://potrace.sourceforge.net/potrace.pdf](https://potrace.sourceforge.net/potrace.pdf)

Summary: Peter Selinger’s 2003 paper describes Potrace tracing black/white bitmaps into smooth Bezier contours, using polygons internally. It explicitly notes that several outlines can generate the same bitmap and that tracing cannot generate information absent from the input. This supports a vectorization capability and its information limit; it does not identify a locally selected executable, version or license.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-sources.md, research/sources/round-05/point-04-web-sources.json.

<a id="src-7f797955889e"></a>

## SRC-7f797955889e — Initial SB50 source metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/acquisition-initial.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/acquisition-initial.json`)

Summary: Preserves original download metadata andsource classifications before drawingleader correction.

Evidence: delegated_initial_source_review.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-7fb788503589"></a>

## SRC-7fb788503589 — Happymodel EP1 receiver (C051) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c051-happymodel-ep1-receiver.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c051-happymodel-ep1-receiver.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Normal radio equipment; original kind existing component record. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-7fc6417a02f1"></a>

## SRC-7fc6417a02f1 — Victron BAT524110620 shared exterior STEP

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/LiFePO4-Battery-25.6V100Ah-NG.stp (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/LiFePO4-Battery-25.6V100Ah-NG.stp`)

Summary: Frozen byte-identical copy of already acquired manufacturer AP214 model shared with BAT512120620. Source length units are mm; retained shape definitions and19 placement frames support the new native assembly.

Evidence: existing_downloaded_original_reused.

Documents: research/sources/round-20/component-sources.json.

<a id="src-7fe70bbaa630"></a>

## SRC-7fe70bbaa630 — Driver iteration — original-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/original-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/original-checks.json`)

Summary: Original native model passes140 checks and fails connector-shell span116.85mm versus manufacturer116.7mm.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-8089d1901b4f"></a>

## SRC-8089d1901b4f — Asset catalog

Original source: [https://polyhaven.com/](https://polyhaven.com/)

Summary: Poly Haven ; Library of 3D models, materials and HDRI environments useful for scene dressing, architectural visualization and lighting. Asset catalog ; Poly Haven states all site assets are CC0, including commercial use without attribution. This is useful for visual environments and render context; asset dimensions/geometry are not engineering component specifications. License

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-80962f129a41"></a>

## SRC-80962f129a41 — Software review: raster drawings and interpreted dimensions

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-04-software.md](../action-audit/reviews/point-04-software.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-80af5eb42a78"></a>

## SRC-80af5eb42a78 — P02 crossmember — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/result.json`)

Summary: Current P02 iteration result is DONE with saved DWG hash, native/persistence/view passes, midpoint130mm, nominal gap260mm and applied helper SHA.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-80d56f29af4a"></a>

## SRC-80d56f29af4a — Agent skill: freecad-scripts

Original source: [https://raw.githubusercontent.com/github/awesome-copilot/main/skills/freecad-scripts/SKILL.md](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/freecad-scripts/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-scripts. Source class: agent skill instructions. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-80d86d504e13"></a>

## SRC-80d86d504e13 — Exact ESKV25 LG manufacturer product page

Original source: [https://www.wiska.com/en/30/pde/10066413/eskv-25-lg.html](https://www.wiska.com/en/30/pde/10066413/eskv-25-lg.html)

Summary: Original HTML identifies10066413,RAL7035 and matching dimensional values; links exact-order CAD selector and datasheet href.

Evidence: downloaded_original.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-80f9c2092927"></a>

## SRC-80f9c2092927 — ME0907 motor adjustment plate (P11) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p11-me0907-motor-adjustment-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p11-me0907-motor-adjustment-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-812380a2589c"></a>

## SRC-812380a2589c — Current FreeCAD API Notes

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/references/current-api.md](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/references/current-api.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Current FreeCAD API Notes. Source class: skill reference documentation. Original reuse terms: permissive terms as archived; GitHub API SPDX=ISC; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-816d7accc0c5"></a>

## SRC-816d7accc0c5 — Point 04 visual and evidence review — raster drawings and orthographic views

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-04-visual.md](../action-audit/reviews/point-04-visual.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-8173158dcbfb"></a>

## SRC-8173158dcbfb — cad-automation-and-reuse.md

Original source: ${FERME_ROOT}/skills/cad-automation-and-reuse.md (`${FERME_ROOT}/skills/cad-automation-and-reuse.md`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-819035442c74"></a>

## SRC-819035442c74 — https://mcpmarket.com/tools/skills/generate-3d-model

Original source: [https://mcpmarket.com/tools/skills/generate-3d-model](https://mcpmarket.com/tools/skills/generate-3d-model)

Summary: - MCP Market: “Generate 3D Model” https://mcpmarket.com/tools/skills/generate-3d-model — listing opened. It describes a downloadable Claude Code skill by TomekGancarczyk that calls Fal.ai `fal-ai/sam-3/3d-objects`, performs image/mask segmentation and cloud generation, downloads GLB assets, and emits React Three Fiber/Rapier snippets. The source skill/GitHub repository was identified as https://github.com/TomekGancarczyk/kata-workshop-cc; the skill file itself was not retrieved through the listing's failed “SKILL.md” click, so its complete prompt, dependency list, and behavior remain uninspected. The repository is a MIT-licensed React Three Fiber game workshop starter, not evidence that the hosted model or its generated outputs carry MIT terms. Do not treat the listing's “open” description as evidence of local inference.

Evidence: existing_report_registered.

Documents: research/reconstruction.md, research/user-supplied-links.md.

<a id="src-82658321d621"></a>

## SRC-82658321d621 — neugart-ngv064-wheel-160.md — recorded_execution_report

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md (`${FERME_ROOT}/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md`)

Summary: Component-specific native checks, save/reopen observations and source paths for OCS 2026.42. Applicability:

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-82875df94520"></a>

## SRC-82875df94520 — Sumitomo PRO-L CH54527G10 gearmotor (C011) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c011-sumitomo-pro-l-ch54527g10-gearmotor.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c011-sumitomo-pro-l-ch54527g10-gearmotor.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Sumitomo PRO-L; original kind manufacturer geometry in retained drawing. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-82d9fa8ce417"></a>

## SRC-82d9fa8ce417 — domain-detail-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-03/domain-detail-sources.json](round-03/domain-detail-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-82e88e67d3cf"></a>

## SRC-82e88e67d3cf — Littelfuse75921-10 service disconnect (C032) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c032-littelfuse75921-10-service-disconnect.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c032-littelfuse75921-10-service-disconnect.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Battery isolation proposal; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-82f59b1215c1"></a>

## SRC-82f59b1215c1 — SKF iteration — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/persistence.json`)

Summary: Recovered verifiedsave/reopen receipt proves fileSHA,zero droppedentities,ten-solid manifest and reopened zeroerror/warning audit.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-832bc3ab6751"></a>

## SRC-832bc3ab6751 — ME0907 transmission guard (P16) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p16-me0907-transmission-guard.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p16-me0907-transmission-guard.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-83551fe43914"></a>

## SRC-83551fe43914 — Leaf iteration — audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/audit.json`)

Summary: Current opened Leaf audit contains eight solids, zero errors/warnings and the original saved-file identity.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-837950156e9e"></a>

## SRC-837950156e9e — Contributor terms

Original source: [https://www.3dcontentcentral.com/includes/Attachments/Terms_and_Conditions_for_Contributions.pdf](https://www.3dcontentcentral.com/includes/Attachments/Terms_and_Conditions_for_Contributions.pdf)

Summary: 3D ContentCentral ; Supplier-certified and user library models in multiple CAD formats. SOLIDWORKS help ; Platform access requires agreement; contributor terms give the platform broad indexing/adaptation/distribution rights but do not establish a blanket open license for each downloaded model. Record per-item license/terms; do not treat the catalog as open data. Contributor terms

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-83daf3ad8d92"></a>

## SRC-83daf3ad8d92 — Driving the OpenCADStudio native builds

Original source: ${OCS_ROOT}/docs/automation/native.md (`${OCS_ROOT}/docs/automation/native.md`)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: Driving the OpenCADStudio native builds. Source class: local primary product documentation; exact byte copy from local source repository. Original reuse terms: GPL-3.0-or-later repository license; see ${OCS_ROOT}/LICENSE

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-840b108e75da"></a>

## SRC-840b108e75da — iTeh catalogue access for EN 10210-2:2019

Original source: [https://standards.iteh.ai/catalog/standards/cen/7f06ebee-2a61-4278-a970-6bf6ad05e1ab/en-10210-2-2019](https://standards.iteh.ai/catalog/standards/cen/7f06ebee-2a61-4278-a970-6bf6ad05e1ab/en-10210-2-2019)

Summary: Direct open attempt returned HTTP 502. Standard content was instead inspected from the linked SIST-EN-10210-2-2019 PDF sample. This catalogue failure is recorded without supporting claims.

Evidence: access_failed.

Documents: research/sources/round-10/tube-corner-sources.json.

<a id="src-840d8b69fd8f"></a>

## SRC-840d8b69fd8f — Software review: CAD, photographs and scans alignment

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-05-software.md](../action-audit/reviews/point-05-software.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-84b231f10122"></a>

## SRC-84b231f10122 — Nissan Leaf Gen2 battery module (C021) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c021-nissan-leaf-gen2-battery-module.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c021-nissan-leaf-gen2-battery-module.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Leaf bank or BT-L alternative; original kind source component/model reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered, local_source_or_execution_record_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-15/leaf-sources.json.

<a id="src-84c081bf3776"></a>

## SRC-84c081bf3776 — P01 p01-build-03 — document-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/document-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/document-checkpoint.json`)

Summary: p01-build-03 document-checkpoint.json: Binds partial/native stage to document 70, revision 0 and named part handles {}; supports inspected recovery.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-8505da5fe91f"></a>

## SRC-8505da5fe91f — read_c045.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/read_c045.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/read_c045.py`)

Summary: Read imported manifest/records andrequested initial ISO capture,whose contents laterfailed identity review.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-856db78a1b1e"></a>

## SRC-856db78a1b1e — Drive support plate (P03) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p03-drive-support-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p03-drive-support-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: frame; One variant per drive route; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered, local_source_or_execution_record_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-15/leaf-sources.json.

<a id="src-856f00288f07"></a>

## SRC-856f00288f07 — Optional Computer Use Workflow

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/computer_use_workflow.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/computer_use_workflow.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Optional Computer Use Workflow. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-85767f154783"></a>

## SRC-85767f154783 — P01 p01-build-03 — isometric-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/isometric-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/isometric-state.json`)

Summary: p01-build-03 isometric-state.json: Observed document 71 revision 0 with open-document identities and camera/command state; used for write isolation or capture provenance.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-85b949b4c1e5"></a>

## SRC-85b949b4c1e5 — Point 06 independent review — building and robot structure and properties

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-06-independent.md](../action-audit/reviews/point-06-independent.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-8611e98b9ce8"></a>

## SRC-8611e98b9ce8 — Using custom data — Nerfstudio documentation

Original source: [https://docs.nerf.studio/quickstart/custom_dataset.html](https://docs.nerf.studio/quickstart/custom_dataset.html)

Summary: Current Nerfstudio custom-data guide inspected 2026-11-12; release not pinned. States per-image camera poses are required; `ns-process-data images;video` uses COLMAP and FFmpeg; supplied pose paths include Metashape XML and RealityCapture CSV. The guide alone does not specify parser auto-orientation/scale settings.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r08.md, research/workflows/reconstruction-paths.md.

<a id="src-868fbd6b345d"></a>

## SRC-868fbd6b345d — Knott 402386.001 steel rim (C004) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c004-knott-402386-001-steel-rim.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c004-knott-402386-001-steel-rim.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Knott wheel alternative; original kind seller/manufacturer dimensions recorded locally. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-86cdf9c119df"></a>

## SRC-86cdf9c119df — Splatfacto — Nerfstudio documentation

Original source: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)

Summary: Current Nerfstudio Splatfacto guide inspected 2026-11-12; release not pinned. Documents trained Gaussian splat export to PLY via `ns-export gaussian-splat`; page says mesh and point-cloud export are currently unsupported for Splatfacto's own export path.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/mix-r09.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md, research/workflows/reconstruction-paths.md.

<a id="src-8700820313fd"></a>

## SRC-8700820313fd — Victron converter current-view recheck report

Original source: [${MODELING_ROOT}/execution/c045-view-recheck-2026-11-13.md](../../execution/c045-view-recheck-2026-11-13.md)

Summary: Documents the newly successful current-view identity check, user rotation report, actual capture recovery and unchanged saved native CAD hash.

Evidence: executed_verification_report.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-878a429a2c73"></a>

## SRC-878a429a2c73 — Saved battery front view

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/reopened-front.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/reopened-front.png`)

Summary: Actual reopened orthographic view inspected for case,lid,terminal heights,edge ribs and bottom restraint geometry.

Evidence: model_capture_inspected.

Documents: research/sources/round-20/component-sources.json.

<a id="src-87d4523a6fea"></a>

## SRC-87d4523a6fea — BMW i3 94Ah battery module (C022) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c022-bmw-i3-94ah-battery-module.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c022-bmw-i3-94ah-battery-module.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; BMW; original kind source component/model reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-882c011aea56"></a>

## SRC-882c011aea56 — OCS state after the current-view capture

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/state-after.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/state-after.json`)

Summary: Native state retained after recovering and inspecting the captured converter view. Document and camera observations remain explicit.

Evidence: executed_native_state_read.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-885be68868de"></a>

## SRC-885be68868de — Pilz manufacturer P97/45 drawing

Original source: [https://www.pilz.com/download/open/P9745_2009094_-.pdf](https://www.pilz.com/download/open/P9745_2009094_-.pdf)

Summary: Original drawing2009094/model2006038 gives45×87 front and120.6/115.4 side dimensions,dated30June2011.

Evidence: downloaded_original.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-885fe0a26a5e"></a>

## SRC-885fe0a26a5e — glotoff/freecad-skills

Original source: [https://github.com/glotoff/freecad-skills](https://github.com/glotoff/freecad-skills)

Summary: glotoff/freecad-skills ; FreeCAD user/power-user modeling and API references ; Adapt only the exercised operations needed for constrained sketches and editable features.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-887713f8625d"></a>

## SRC-887713f8625d — item-profile-02633-segment-100mm-native.json — recorded_check_results

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json`)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-891a60e9bc7b"></a>

## SRC-891a60e9bc7b — Main frame crossmember proposal

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p02-main-frame-crossmember.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p02-main-frame-crossmember.md`)

Summary: Existing local component/action/skill/catalogue source reused by the consolidated plan. Evidence and proposal boundaries remain in the original record.

Evidence: local_source_inspected, local_execution_source_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-09/component-execution-sources.json, research/sources/round-10/tube-corner-sources.json, research/sources/round-13/crossmember-sources.json.

<a id="src-8926d9c1e68c"></a>

## SRC-8926d9c1e68c — Driver iteration — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-isometric.png`)

Summary: Inspected isometric image shows tapered housing, separate studs/washers/dividers, recessed signal connectors and contacts.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-896c4a89c975"></a>

## SRC-896c4a89c975 — Agent skill: freecad-ai

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/SKILL.md](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-ai. Source class: agent skill instructions. Original reuse terms: permissive terms as archived; GitHub API SPDX=ISC; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-89c0679bdda3"></a>

## SRC-89c0679bdda3 — Proposed next stages from the workflow research

Original source: [${MODELING_ROOT}/research/next-step-proposal.md](../next-step-proposal.md)

Summary: Seven proposed work packages: targeted route review, shared records, existing OCS pilot, text/drawing routes, measured reconstruction, architecture/robotics/component reuse, and packaging exercised workflows. Preserves the existing implementation plan.

Evidence: local_source_inspected.

Documents: research/sources/round-02/project-sources.json.

<a id="src-8a3139cd3bdf"></a>

## SRC-8a3139cd3bdf — P01 p01-build-03 — reopened-view-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-view-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-view-state.json`)

Summary: p01-build-03 reopened-view-state.json: Observed document 71 revision 0 with open-document identities and camera/command state; used for write isolation or capture provenance.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-8a5ee96b7077"></a>

## SRC-8a5ee96b7077 — SurLok SLPIPB50BSO0 cable plug (C036) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c036-surlok-slpipb50bso0-cable-plug.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c036-surlok-slpipb50bso0-cable-plug.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Battery service pole candidate; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-8a7317b2bcc0"></a>

## SRC-8a7317b2bcc0 — cad2urdf repository

Original source: [https://github.com/boelnasr/CAD_TO_URDF](https://github.com/boelnasr/CAD_TO_URDF)

Summary: Repository describes conversion of mesh plus YAML joints or STEP/IGES assemblies into ROS URDF packages; automatic joint hypotheses require review.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-8a94739a62eb"></a>

## SRC-8a94739a62eb — native-plot-visual-check.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-visual-check.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-visual-check.json`)

Summary: Actual Poppler rendering andpixel extrema show anentirelywhite page;visualcheck FAIL whileexport operationcompleted.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-8a9e1c41280d"></a>

## SRC-8a9e1c41280d — Brake caliper reaction bracket (P15) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p15-brake-caliper-reaction-bracket.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p15-brake-caliper-reaction-bracket.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907 or separate service-brake proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-8a9f0d7330ec"></a>

## SRC-8a9f0d7330ec — SB50 source-stage result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/result.json`)

Summary: Retains exact6331G5 kit identity,source model roles anddependent geometry questions.

Evidence: executed_component_stage_record.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-8ab7d0d86617"></a>

## SRC-8ab7d0d86617 — 02-frame-hitch-supports.md

Original source: ${FERME_ROOT}/research/base-component-completion-2026-11-12/02-frame-hitch-supports.md (`${FERME_ROOT}/research/base-component-completion-2026-11-12/02-frame-hitch-supports.md`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected, local_execution_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-10/tube-corner-sources.json, research/sources/round-13/crossmember-sources.json.

<a id="src-8ae740d518bb"></a>

## SRC-8ae740d518bb — test_component_tools.py

Original source: [${MODELING_ROOT}/tests/test_component_tools.py](../../tests/test_component_tools.py)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: authored_document_or_code_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-8b8ba89972cd"></a>

## SRC-8b8ba89972cd — Blickle LS-PS310K caster reference (C016) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c016-blickle-ls-ps310k-caster-reference.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c016-blickle-ls-ps310k-caster-reference.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Caster reference alternative; original kind project reference envelope. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-8ba644c474b4"></a>

## SRC-8ba644c474b4 — Driver iteration — native-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/native-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/native-records.json`)

Summary: Raw original SAB solids and text records supply independent geometry observations and preserved baseline properties.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-8bf87f7a8c04"></a>

## SRC-8bf87f7a8c04 — AENOR — DIN EN 10210-1:2026-03 catalogue entry for prEN 10210-1:2026

Original source: [https://tienda.aenor.com/p/norma-din-en-10210-1-2026-03-399626373](https://tienda.aenor.com/p/norma-din-en-10210-1-2026-03-399626373)

Summary: AENOR page identifies the March 2026 German/English prEN 10210-1:2026 text as intended to replace DIN EN 10210-1:2006 and DIN EN 10210-3:2020, and its description covers hot-finished structural hollow sections. Used only as cross-check on the 2026 Part 1 edition transition; no corner claims are drawn from this source.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-8c216bd07f9d"></a>

## SRC-8c216bd07f9d — Franka Emika Panda MJCF file

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/panda.xml](https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/panda.xml)

Summary: Actual example robot model source file for the Menagerie Panda; use only at a pinned revision and with model-specific rights.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r04.md.

<a id="src-8c3e1acbd99d"></a>

## SRC-8c3e1acbd99d — check_c045_saved.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/check_c045_saved.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/check_c045_saved.py`)

Summary: Computed37 actual persisted placement/point/instance checks andseparate source-dimension observations.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-8ce066c08d57"></a>

## SRC-8ce066c08d57 — Kelly ME0907 drawing/test-data archive

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/Kelly-ME0907-dimensions-testdata.zip (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/Kelly-ME0907-dimensions-testdata.zip`)

Summary: Original ZIP linked by Kelly ME0907 page, acquired with three PDF members. The outline member is titled Mars Electric ME0201013001; it retains its own variant identity.

Evidence: downloaded_original.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-8d633a1cae00"></a>

## SRC-8d633a1cae00 — P01 p01-build-03 — reopened-viewport.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-viewport.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-viewport.png`)

Summary: Reopened end-view capture shows the outer and inner rounded-square outlines of the P01 rail.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-8da82a2f23b9"></a>

## SRC-8da82a2f23b9 — reopened-records-36.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-36.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-36.json`)

Summary: reopened native record snapshot: C3:Insert, C4:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-8db7870af183"></a>

## SRC-8db7870af183 — Dave Snider, “Claude tips for 3D work”

Original source: [https://davesnider.com/claude-3D](https://davesnider.com/claude-3D)

Summary: Dave Snider, “Claude tips for 3D work” ; Article dated March 13, 2026 describes browser 3D applications, app-state/camera/debug-marker feedback loops and visual review. It notes screenshots and logs helped expose spatial mistakes in his workflow. ; Visual-debugging article, not a CAD skill or kernel. Web inspected; no packaged skill or licence. Visual feedback complements numerical geometry measurements; it does not replace them.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-8de314785eed"></a>

## SRC-8de314785eed — ${OCS_ROOT}/LICENSE

Original source: ${OCS_ROOT}/LICENSE (`${OCS_ROOT}/LICENSE`)

Summary: Source referenced for the stated workflow; see the owning documentation or research item.

Evidence: existing_report_registered, local_reference_registered, local_source_or_executed_inspection.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-18/dxf-inspection-sources.json.

<a id="src-8e6d7648b52e"></a>

## SRC-8e6d7648b52e — Command-line Interface — COLMAP

Original source: [https://colmap.github.io/cli.html](https://colmap.github.io/cli.html)

Summary: COLMAP current CLI documentation inspected 2026-11-12; no local binary version checked. Shows sparse matching/mapper, image_undistorter, patch_match_stereo, stereo_fusion, poisson_mesher and delaunay_mesher stages. PatchMatch requires the undistorted workspace; fusion creates colored cloud. GPU backend support depends on selected build/options.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r06.md, research/workflows/reconstruction-paths.md.

<a id="src-8f09660dbc00"></a>

## SRC-8f09660dbc00 — Earlier Leaf native construction and verification report

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/nissan-leaf-gen2.md (`${FERME_ROOT}/engineering/module-development/cad/checks/nissan-leaf-gen2.md`)

Summary: Identifies the eight-solid drawing, earlier 14 pre-save checks, verified-save SHA and historical viewport failure. The current iteration reads saved SAB and inspects successful current captures.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-8f19f4f777d2"></a>

## SRC-8f19f4f777d2 — Resistor dimension association and timestamp review

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/coordinator-review.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/coordinator-review.md`)

Summary: Confirms package-table/pin values,keeps2.54mm terminal span separate from substrate thickness,excludes initial unsupported general-tolerance/no-scale claims,and identifies CET versus reported CEST label.

Evidence: manufacturer_dimension_review.

Documents: research/sources/round-20/component-sources.json.

<a id="src-8f369f8f1381"></a>

## SRC-8f369f8f1381 — Python — MuJoCo Documentation

Original source: [https://mujoco.readthedocs.io/en/stable/python.html](https://mujoco.readthedocs.io/en/stable/python.html)

Summary: Stable MuJoCo Python binding documentation accessed 2026-11-12. Establishes the Python bindings are close to the C API; used alongside the model-editing page for Python method names. No local package version was checked.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-8f7945ad1ed7"></a>

## SRC-8f7945ad1ed7 — P01 p01-build-03 — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/ocs-journal.jsonl`)

Summary: p01-build-03 append-only request journal retains 35 events across 13 request identities, with original intents and responses. It supplies the native command/recovery history for this named attempt; request tokens are excluded.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-8f8532cac48e"></a>

## SRC-8f8532cac48e — Domain and component research report

Original source: [${MODELING_ROOT}/research/domains-and-components.md](../domains-and-components.md)

Summary: Prior project report compares reusable component sources and downstream architecture/robotics domains. This batch uses it for source-library and assembly handoffs.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-8f9b6f25cd0d"></a>

## SRC-8f9b6f25cd0d — AGENTS.md

Original source: [${MODELING_ROOT}/AGENTS.md](../../AGENTS.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-8fd31c82a6fe"></a>

## SRC-8fd31c82a6fe — Recorded native binary regression tests

Original source: [${MODELING_ROOT}/tests/test_native_acis.py](../../tests/test_native_acis.py)

Summary: Four integration tests use FERME saved rail evidence: source dimensions pass, pre-save/reopened vertex and radius sets agree, wrong260mm expectation fails for600mm rail, and truncated binary is rejected.

Evidence: local_execution_evidence_inspected, local_execution_source_inspected, local_source_or_execution_record_inspected, implementation_test_artifact.

Documents: research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-13/crossmember-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json, research/sources/round-20/component-sources.json.

<a id="src-90428f0f4c05"></a>

## SRC-90428f0f4c05 — TripoSR model card and weights

Original source: [https://huggingface.co/stabilityai/TripoSR](https://huggingface.co/stabilityai/TripoSR)

Summary: Model card labels weights MIT and identifies single-image feed-forward reconstruction; trained using Objaverse renders.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/dom-r06.md, research/workflows/details/rec-r10.md.

<a id="src-90d5093f2a51"></a>

## SRC-90d5093f2a51 — P01 p01-build-01 — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/result.json`)

Summary: p01-build-01 result.json: Observed attempt state FAIL; Retains the definitive native subtraction error and the preserved recovery context.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-90f352cc1a15"></a>

## SRC-90f352cc1a15 — reopened-records-24.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-24.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-24.json`)

Summary: reopened native record snapshot: B7:Insert, B8:Insert, B9:Insert, BA:Insert, BB:Insert, BC:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-9133612f3fad"></a>

## SRC-9133612f3fad — reopened-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-checkpoint.json`)

Summary: Reopeneddocument85bindingandcurrentgeometryrevisionafterverifiedpersistence.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-91466ed68e96"></a>

## SRC-91466ed68e96 — Python plugin declaration

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/plugins/opencad-python/plugin.toml](https://github.com/HakanSeven12/OpenCADStudio/blob/main/plugins/opencad-python/plugin.toml)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-91d52ea5a02e"></a>

## SRC-91d52ea5a02e — Ferme geometric dependency order

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/dependency-order.tsv (`${FERME_ROOT}/engineering/module-development/cad-inputs/dependency-order.tsv`)

Summary: Existing local component/action/skill/catalogue source reused by the consolidated plan. Evidence and proposal boundaries remain in the original record.

Evidence: local_source_inspected.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-926884ef85e8"></a>

## SRC-926884ef85e8 — Foster1202/cad-modeling-fusion-skill

Original source: [https://github.com/Foster1202/cad-modeling-fusion-skill](https://github.com/Foster1202/cad-modeling-fusion-skill)

Summary: Foster1202/cad-modeling-fusion-skill ; ModelSpec schema and code-generation patterns with Fusion, FreeCAD and OpenSCAD backends ; Assess reusable schema and open-backend content under its licence. Use the open software backends for this project.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-92ae5f12a6ef"></a>

## SRC-92ae5f12a6ef — imported-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-isometric.png`)

Summary: Actualprecorrectionimportviewshowsdisplacedassemblycomponents.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-92b7a09b7e3a"></a>

## SRC-92b7a09b7e3a — Local Python 3.14 CSV source

Original source: ${SYSTEM_ROOT}/usr/lib/python3.14/csv.py (`${SYSTEM_ROOT}/usr/lib/python3.14/csv.py`)

Summary: CSV dialect/field parsing source inspected by the software reviewer; retain source strings and explicit dialect.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-92f126438f43"></a>

## SRC-92f126438f43 — reopened-records-18.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-18.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-18.json`)

Summary: reopened native record snapshot: B1:Insert, B2:Insert, B3:Insert, B4:Insert, B5:Insert, B6:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-93087004fdb3"></a>

## SRC-93087004fdb3 — imported-audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/imported-audit.json`)

Summary: Initial12solid/18blockreferenceauditwithzeroerrorsorwarningsbeforeplacementcorrection.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-932141965717"></a>

## SRC-932141965717 — Blender Lab MCP page

Original source: [https://www.blender.org/lab/mcp-server/](https://www.blender.org/lab/mcp-server/)

Summary: The Blender-hosted Blender Lab MCP repository is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its setup page requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The Blender Lab MCP page search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's scripting security guidance says Python scripts can perform unrestricted operations.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-9332105dc85a"></a>

## SRC-9332105dc85a — nissan-leaf-gen2-native.json — recorded_check_results

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json`)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-934308b209a1"></a>

## SRC-934308b209a1 — Awesome Skills `earthtojake-text-to-cad-step-parts`

Original source: [https://awesomeskill.ai/skill/earthtojake-text-to-cad-step-parts](https://awesomeskill.ai/skill/earthtojake-text-to-cad-step-parts)

Summary: Awesome Skills `earthtojake-text-to-cad-step-parts` ; Page identifies skill `step-parts`: query hosted step.parts catalog for purchasable parts, fuzzy search/standards, obtain canonical STEP, verify checksums and hand off to a viewer. It reports 5,937 stars, 710 forks, updated 2026-06-10. ; Hosted component-catalog integration, not text-to-parametric CAD. Network/API and external catalog are intrinsic to advertised behavior. Source SKILL.md was not downloaded. This is distinct from the archived `earthtojake/text-to-cad` skill and must not be conflated.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-9345ab05320c"></a>

## SRC-9345ab05320c — corrected-records-36.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-36.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-36.json`)

Summary: corrected native record snapshot: C3:Insert, C4:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-937929a512bd"></a>

## SRC-937929a512bd — Point 05 designer notes — alignment and parametric remodeling

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-05-designer.md](../action-audit/reviews/point-05-designer.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-93942b7c50fd"></a>

## SRC-93942b7c50fd — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/reyk/freecad-ai-skill](https://api.github.com/repos/reyk/freecad-ai-skill)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-93aef666d1eb"></a>

## SRC-93aef666d1eb — rec-r10.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r10.md](../workflows/details/rec-r10.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-93b47d856776"></a>

## SRC-93b47d856776 — Local Python 3.14 JSON interface source

Original source: ${SYSTEM_ROOT}/usr/lib/python3.14/json/__init__.py (`${SYSTEM_ROOT}/usr/lib/python3.14/json/__init__.py`)

Summary: Decoder callbacks, numeric token handling and nonfinite/default behavior inspected as intake design evidence.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-93cc6c46876e"></a>

## SRC-93cc6c46876e — imported-records-12.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-12.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-12.json`)

Summary: imported native record snapshot: AB:Insert, AC:Insert, AD:Insert, AE:Insert, AF:Insert, B0:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-9409ef71b08a"></a>

## SRC-9409ef71b08a — P01 p01-build-01 — rail-schema-4.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-4.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-4.json`)

Summary: p01-build-01 rail-schema-4.json: Retained native response with fields command, ok; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-940fb4ea2921"></a>

## SRC-940fb4ea2921 — Point 06 visual and evidence review — building and robot structure and properties

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-06-visual.md](../action-audit/reviews/point-06-visual.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-94415df8565c"></a>

## SRC-94415df8565c — Point 07 — Capture, reconstruction and appearance scenes

Original source: [${MODELING_ROOT}/research/action-audit/point-07-reconstruction.md](../action-audit/point-07-reconstruction.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-944a92cb8bdf"></a>

## SRC-944a92cb8bdf — Published four-source intake index

Original source: [${MODELING_ROOT}/execution/source-intake/live-01/revision/source-index.json](../../execution/source-intake/live-01/revision/source-index.json)

Summary: Actual execution retains two exact user messages, two file observations, byte hashes, scope and request identity with no network acquisition.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-9463773b6a12"></a>

## SRC-9463773b6a12 — OpenSCAD Documentation index

Original source: [https://openscad.org/documentation](https://openscad.org/documentation)

Summary: The official OpenSCAD documentation page links to the User Manual, Language Reference, and the manual section 'Using OpenSCAD in a command line environment'. This inspected index confirms the official documentation route for scripted modeling and command-line use; it does not expose a command example or mesh-export flag on the index page. The project's existing source register records an earlier inspection of the official OpenSCAD manuals for command-line rendering/export and mesh-oriented formats.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/cad-r10.md, research/workflows/details/mix-r02.md.

<a id="src-9498bff46463"></a>

## SRC-9498bff46463 — SurLok SLPIRBBPSO0 receptacle (C037) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c037-surlok-slpirbbpso0-receptacle.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c037-surlok-slpirbbpso0-receptacle.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Battery service pole candidate; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-952bf146bbc5"></a>

## SRC-952bf146bbc5 — FreeCAD Headless Execution & Automation

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/headless_execution.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/headless_execution.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Headless Execution & Automation. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-95551de04df8"></a>

## SRC-95551de04df8 — Sumitomo PRO-M CH54065G10 gearmotor (C010) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c010-sumitomo-pro-m-ch54065g10-gearmotor.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c010-sumitomo-pro-m-ch54065g10-gearmotor.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Sumitomo PRO-M; original kind manufacturer geometry in retained drawing. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-9557e8c0e378"></a>

## SRC-9557e8c0e378 — point-02-operations

Original source: [${MODELING_ROOT}/research/action-audit/point-02-operations.json](../action-audit/point-02-operations.json)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-95aacf0e0f5c"></a>

## SRC-95aacf0e0f5c — ifcopenshell.api.geometry.edit_object_placement — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `edit_object_placement(file, product, matrix=None, is_si=True, should_transform_children=False)` for a 4×4 local placement matrix. is_si=True means matrix translations are SI; False means project units. Only local placements are supported; the child flag controls whether nested children move with the parent or retain world position through rewritten local placements.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md.

<a id="src-95f6c0cb869a"></a>

## SRC-95f6c0cb869a — Pinned fuse source labels and unresolved geometry inputs

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source-job.json`)

Summary: Pins reader-reported overall length,hole diameter,strip thickness andend-circle label to the acquisition record/hash. Body length,hole pitch andcontact-plane association are explicit required inputs.

Evidence: implementation_input_artifact.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-9641fd75954c"></a>

## SRC-9641fd75954c — ICP registration — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)

Summary: Open3D 0.20.0 documents `evaluate_registration(source, target, threshold, trans_init)` and `registration_icp` with source, target, distance threshold, initial transformation and selected objective. ICP output maps source to target. The inspected 0.20.0 tutorial defines fitness as inlier correspondences divided by source point count; this record does not generalize that denominator to other releases or uninspected local implementations; inlier_rmse is the RMSE over inlier correspondences. Point-to-plane ICP uses point-to-plane residuals and requires normals; default ICP convergence uses up to 30 iterations. Metrics measure thresholded fit and overlap, not uncertainty or pose uniqueness.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r03.md, research/workflows/details/rec-r04.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r07.md, research/workflows/details/rec-r09.md, research/workflows/details/rec-r10.md.

<a id="src-96ae0c43af7d"></a>

## SRC-96ae0c43af7d — Example Workflow: Designing a Parametric Enclosure

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/examples/parametric_part_workflow.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/examples/parametric_part_workflow.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Example Workflow: Designing a Parametric Enclosure. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-96b0604f6e83"></a>

## SRC-96b0604f6e83 — Albright SW80B-40 contactor (C033) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c033-albright-sw80b-40-contactor.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c033-albright-sw80b-40-contactor.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Leaf or BMW candidate; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-96c77b310d08"></a>

## SRC-96c77b310d08 — Battery solid-definition preservation

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/geometry-preservation.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/geometry-preservation.json`)

Summary: Exact ACIS record comparison confirms all21 solid definitions remain unchanged during placement-only correction.

Evidence: executed_verification_result.

Documents: research/sources/round-20/component-sources.json.

<a id="src-96e5bd9ad8ba"></a>

## SRC-96e5bd9ad8ba — Full-sequence independent integration review

Original source: [${MODELING_ROOT}/research/action-audit/reviews/full-sequence-independent.md](../action-audit/reviews/full-sequence-independent.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-9794ead44d0e"></a>

## SRC-9794ead44d0e — ifcopenshell.api.georeference — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `add_georeferencing` creating projected-CRS and map-conversion entities with blank parameters, and `edit_georeferencing` setting CRS and coordinate-operation attributes. CRS and transform values must be supplied; the API does not estimate a survey transform. IFC2X3 uses its map-conversion property-set route.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md.

<a id="src-97cf3ff5244d"></a>

## SRC-97cf3ff5244d — reopened-records-12.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-12.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-12.json`)

Summary: reopenednativeentitysnapshot: A8:Insert, A9:Insert, AA:Insert, AE:Solid3D, B2:Solid3D, B6:Solid3D. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-97ed6b862899"></a>

## SRC-97ed6b862899 — P01 p01-build-01 — rail-schema-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-schema-0.json`)

Summary: p01-build-01 rail-schema-0.json: Installed API response document_required: Read state and supply document_id; retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-989f5c3e411a"></a>

## SRC-989f5c3e411a — template-check_c023_saved.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/template-check_c023_saved.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/template-check_c023_saved.py`)

Summary: Preservedexisting29/35checkalgorithmtemplateusedbytheactualFiboxsaved-checkdriver.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-98a1a3cd7fd0"></a>

## SRC-98a1a3cd7fd0 — Agent skill: freecad-power-user

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/SKILL.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-power-user. Source class: agent skill instructions. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-98af64fdd846"></a>

## SRC-98af64fdd846 — Converter current-view recheck result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/result.json`)

Summary: One current-view identity check passes. Saved DWG bytes match the earlier component record; prior failed captures remain preserved.

Evidence: executed_visual_verification.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-98e17e4710fb"></a>

## SRC-98e17e4710fb — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/result.json`)

Summary: C043 source-stage result retains target identity andlinks C045 reuse of acquired originals.

Evidence: executed_readiness_result.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-993c97d817f0"></a>

## SRC-993c97d817f0 — P01 p01-build-01 — rail-record-schema-2.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-record-schema-2.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-record-schema-2.json`)

Summary: p01-build-01 rail-record-schema-2.json: Retained native response with fields command, ok; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-994ff56f9968"></a>

## SRC-994ff56f9968 — Orion-Tr Smart-rev00-3D

Original source: [https://www.victronenergy.com/upload/documents/Orion-Tr-Smart-Charger-Isolated-12V-24V-360W-%28stp%29.STEP](https://www.victronenergy.com/upload/documents/Orion-Tr-Smart-Charger-Isolated-12V-24V-360W-%28stp%29.STEP)

Summary: Manufacturer rev00/2019 AP214 model names24/12-30 hardware,contains9 solid definitions and27 placed solids;supports C045.

Evidence: downloaded_original.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-9968cbf922d2"></a>

## SRC-9968cbf922d2 — Leaf iteration — reopened-terminal.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-terminal.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-terminal.png`)

Summary: Inspected current end image shows separate power/tap/power terminal assemblies aligned along the reconstructed row.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-9969afca68d8"></a>

## SRC-9969afca68d8 — Point 04 designer notes — raster drawings and interpreted dimensions

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-04-designer.md](../action-audit/reviews/point-04-designer.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-998613bbc692"></a>

## SRC-998613bbc692 — Implemented DXF entity/context inspector

Original source: [${MODELING_ROOT}/scripts/dxf_inspect.py](../../scripts/dxf_inspect.py)

Summary: New read-only adapter inventories original source handles, curve types, attributes, spaces/layers, units, source coordinate systems and nested INSERT transforms. Preserves hashes and guards explicit resource/output limits.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-99954d282c44"></a>

## SRC-99954d282c44 — Point 03 designer notes — vector profiles and small solids

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-03-designer.md](../action-audit/reviews/point-03-designer.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-99bfdb2d1a9e"></a>

## SRC-99bfdb2d1a9e — CONTEC example terms

Original source: [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280)

Summary: STEP / Open CASCADE ; STEP represents exchangeable CAD geometry; use AP242 where supported for product structure, geometry and PMI; test actual receiving application behavior. Manufacturer libraries frequently provide STEP, with separate download terms. ; STEP files from a manufacturer are not automatically openly licensed. CONTEC example terms restrict access/use to purchasers or prospective purchasers, bar adapting the data and disclaim warranty. ; Preserve native STEP plus supplier identity and terms. Import only within stated terms; derive a display/collision mesh only where permitted. Open CASCADE tooling is a geometry kernel/translator candidate, not a semantic library.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-99fd15613b4b"></a>

## SRC-99fd15613b4b — P01 p01-build-03 — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/initial-state.json`)

Summary: p01-build-03 initial-state.json: Observed document 69 revision 7 with open-document identities and camera/command state; used for write isolation or capture provenance.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-9a40d7c5ca24"></a>

## SRC-9a40d7c5ca24 — Model Editing — MuJoCo Documentation

Original source: [https://mujoco.readthedocs.io/en/stable/programming/modeledit.html](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html)

Summary: Stable MuJoCo documentation accessed 2026-11-12; page does not pin an installed release. Documents mjSpec parsing of MJCF/URDF through Python from_file/from_string, compilation to mjModel, and mj_saveXML/mj_saveXMLString/mj_encode serialization. XML output flattens spec; savecompiled controls source-spec versus compilation-made values and parser-expansion losses.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md.

<a id="src-9a4cc68545a8"></a>

## SRC-9a4cc68545a8 — Command Line Usage — Tesseract documentation

Original source: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)

Summary: The official command page shows `tsv` output with page/block/paragraph/line/word identifiers, pixel left/top/width/height, confidence and recognized text. Its hOCR example uses word boxes and `x_wconf`; the page describes available engines in Tesseract 5 and one sample output identifies an example build `5.0.1-64-g3c22`. The page does not identify a local binary or traineddata version; OCR values and confidence remain candidates for source review.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-01-model-brief.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-02/cad-sources.json, research/sources/round-04/intake-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md.

<a id="src-9a847c6724b8"></a>

## SRC-9a847c6724b8 — reopened-top.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-top.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-top.png`)

Summary: Actual converter capture attempt reopened-top;image repeats the previous Fibox enclosure. Included as failed visual evidence,withhash comparison in capture-identity-checks.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-9adef416e57c"></a>

## SRC-9adef416e57c — Retained SKF insert catalogue page image

Original source: ${TEMP_ROOT}/opencode/skf-yar204-catalogue-page92.png (`${TEMP_ROOT}/opencode/skf-yar204-catalogue-page92.png`)

Summary: Actual inspected catalogue page image shows YAR204-2F20mmbore,47mmouterdiameter,31mminnerringwidth and18.3mmfaceoffset supporting the existing insert record.

Evidence: retained_source_render_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-9b8eb3a2b709"></a>

## SRC-9b8eb3a2b709 — corrected-records-24.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-24.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-24.json`)

Summary: corrected native record snapshot: B7:Insert, B8:Insert, B9:Insert, BA:Insert, BB:Insert, BC:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-9b9b3c47b23f"></a>

## SRC-9b9b3c47b23f — Completed saved Leaf module iteration report

Original source: [${MODELING_ROOT}/execution/c021-leaf-module.md](../../execution/c021-leaf-module.md)

Summary: Records reuse of the eight-solid model, the retained 300 x 222 x 34 mm case convention, 29 native checks, persistence, actual source/view inspection and the applied checker with 44 tests.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-9bffb9dff56b"></a>

## SRC-9bffb9dff56b — OCS repository

Original source: [https://github.com/HakanSeven12/OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-9c0fbe89719d"></a>

## SRC-9c0fbe89719d — Driver iteration — correction.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/correction.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/correction.json`)

Summary: Records source-derived -0.15mm X translation,31 owned X2 solids, original116.85mm span and target116.7mm; unaffected entities preserved.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-9ce53648c6f9"></a>

## SRC-9ce53648c6f9 — WISKA-ESKV-25-page3-detail.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page3-detail.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page3-detail.png`)

Summary: Detailed page3 rasterused for actual drawnfeatureassociation;no additional numerical segmentheights.

Evidence: derived_pdf_render.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-9cfb720a2d78"></a>

## SRC-9cfb720a2d78 — reopen_c029.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/reopen_c029.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/reopen_c029.py`)

Summary: Recoveredoriginalopenrequest,verifiedsavehash/manifestandcapturedpersistedrecords/isometric.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-9cfde96bb911"></a>

## SRC-9cfde96bb911 — csv — CSV file reading and writing — Python 3.15.2 documentation

Original source: [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)

Summary: Official Python documentation describes CSV readers and writers, configurable dialects and formatting parameters, and reader rows returned as strings by default. The QUOTE_NONNUMERIC option converts unquoted fields to floats. For intake, a declared dialect preserves field boundaries and reading as strings preserves source spellings for later interpretation. Parsing does not determine units, numeric locale or the meaning of a column.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-01-model-brief.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-04/intake-sources.json.

<a id="src-9d121e4915e5"></a>

## SRC-9d121e4915e5 — Leaf iteration — capture-isometric.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/capture-isometric.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/capture-isometric.json`)

Summary: Completed isometric capture response binds document 76 and the model image compared with the source.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-9df6cac46941"></a>

## SRC-9df6cac46941 — 🤖 Awesome GitHub Copilot

Original source: [https://raw.githubusercontent.com/github/awesome-copilot/main/README.md](https://raw.githubusercontent.com/github/awesome-copilot/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: 🤖 Awesome GitHub Copilot. Source class: repository README. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-9e3aa6c6cce6"></a>

## SRC-9e3aa6c6cce6 — P02 crossmember — body-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/body-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/body-checkpoint.json`)

Summary: Checkpoint identifies the P02 native hollow body before dimension inspection and saving.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-9e57d453372b"></a>

## SRC-9e57d453372b — queue

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/queue.json](../action-audit/implementation-queue/queue.json)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected, local_source_inspected, local_source_or_executed_inspection.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-07/parts-catalogue-sources.json, research/sources/round-08/component-plan-sources.json, research/sources/round-18/dxf-inspection-sources.json.

<a id="src-9e5cbb874a32"></a>

## SRC-9e5cbb874a32 — P01 p01-build-01 — rail-doc-schema-1.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-doc-schema-1.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-doc-schema-1.json`)

Summary: p01-build-01 rail-doc-schema-1.json: Installed API response unknown_operation: Unknown operation; retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-9e97a14e9164"></a>

## SRC-9e97a14e9164 — pre-save-assembly-measurements.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/pre-save-assembly-measurements.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/pre-save-assembly-measurements.json`)

Summary: Source-corrected16instancepathsandpointspansbeforepersistence;accessoriesincluded.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-9e9899193ac9"></a>

## SRC-9e9899193ac9 — Software review: confirmed dimensions and vector drawings to CAD

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-03-software.md](../action-audit/reviews/point-03-software.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-9ea228a27dc2"></a>

## SRC-9ea228a27dc2 — FreeCAD Assembly4-to-URDF exporter

Original source: [https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF](https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF)

Summary: Third-party source describes Python scripts exporting Assembly4 assemblies to URDF; feature support and licence must be checked at the pinned revision.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/domain-paths.md.

<a id="src-9ec25a7b74a7"></a>

## SRC-9ec25a7b74a7 — corrected-records-12.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-12.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-12.json`)

Summary: corrected native record snapshot: AB:Insert, AC:Insert, AD:Insert, AE:Insert, AF:Insert, B0:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-9f577a14e903"></a>

## SRC-9f577a14e903 — Actual intake completion receipt

Original source: [${MODELING_ROOT}/execution/source-intake/live-01/revision/receipt.json](../../execution/source-intake/live-01/revision/receipt.json)

Summary: Records COMPLETE publication, tool/input/artifact hashes, Python runtime, elapsed time and zero network requests for the executed capture.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-9f71130cf873"></a>

## SRC-9f71130cf873 — Leaf iteration — native-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/native-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/native-checks.json`)

Summary: All 29 current saved-geometry comparisons pass for eight closed solids, case dimensions, mounting bores, inner walls and three nominal terminal assemblies.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-9f9c7199168b"></a>

## SRC-9f9c7199168b — local project README

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/README.md](https://github.com/HakanSeven12/OpenCADStudio/blob/main/README.md)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-9fdfe0a67f6a"></a>

## SRC-9fdfe0a67f6a — Actual implementation job input

Original source: [${MODELING_ROOT}/execution/source-intake/job-input.json](../../execution/source-intake/job-input.json)

Summary: Preserves exact current execution/no-redo instructions and identifies project rules plus the existing first-action plan as local source inputs.

Evidence: local_implementation_or_execution_record_inspected.

Documents: research/sources/round-17/source-intake-sources.json.

<a id="src-9ff47adead00"></a>

## SRC-9ff47adead00 — README.md

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/README.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/README.md`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected, local_execution_evidence_inspected, local_execution_source_inspected, local_source_or_execution_record_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-11/rail-execution-sources.json, research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-13/crossmember-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json.

<a id="src-a00bd3c7c755"></a>

## SRC-a00bd3c7c755 — Caster primary removable pin (C018) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c018-caster-primary-removable-pin.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c018-caster-primary-removable-pin.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Retained fixed-setting arm proposal; original kind pin component geometry input. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-a07601074c08"></a>

## SRC-a07601074c08 — Point 03 source check: confirmed dimensions and vector drawings

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-03-sources.md](../action-audit/reviews/point-03-sources.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-a086c5a04ee4"></a>

## SRC-a086c5a04ee4 — README.md

Original source: ${OCS_ROOT}/README.md (`${OCS_ROOT}/README.md`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-a0ba78259618"></a>

## SRC-a0ba78259618 — PlankAssembly: Robust 3D Reconstruction from Three Orthographic Views with Learnt Shape Programs

Original source: [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html)

Summary: ICCV 2023 paper proposes a transformer/shape-program mapping from three orthographic views to CAD models and evaluates noisy/incomplete views on a benchmark dataset.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r05.md, research/workflows/details/cad-r09.md, research/workflows/details/mix-r08.md.

<a id="src-a0f13205bc91"></a>

## SRC-a0f13205bc91 — SKF iteration — first-slice-response.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/first-slice-response.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/first-slice-response.json`)

Summary: Completed nativeSLICE positive draft modifies only owned housingD7 with actual revision/state readback.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-a189f01c9855"></a>

## SRC-a189f01c9855 — Holybro Pixhawk6C hardware (C052) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c052-holybro-pixhawk6c-hardware.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c052-holybro-pixhawk6c-hardware.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Controller hardware proposal; original kind existing component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-a1b86705dc1b"></a>

## SRC-a1b86705dc1b — Mesh API

Original source: [https://docs.blender.org/api/current/bpy.types.Mesh.html](https://docs.blender.org/api/current/bpy.types.Mesh.html)

Summary: Licence details for the upstream source, installed package and MCP integrations are recorded in domains and components. Primary sources: Blender repository/licence, Python API quickstart, Mesh API. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-a1e82dcf8fcb"></a>

## SRC-a1e82dcf8fcb — document_model.py

Original source: ${OCS_ROOT}/plugins/opencad-python/src/document_model.py (`${OCS_ROOT}/plugins/opencad-python/src/document_model.py`)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-a1fc353f03bd"></a>

## SRC-a1fc353f03bd — Victron Lynx Smart BMS NG500 M10 (C026) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c026-victron-lynx-smart-bms-ng500-m10.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c026-victron-lynx-smart-bms-ng500-m10.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Victron NG; original kind manufacturer assembly reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-a22f0b43932b"></a>

## SRC-a22f0b43932b — Workflow and source register builder

Original source: [${MODELING_ROOT}/research/tools/build_workflow_register.py](../tools/build_workflow_register.py)

Summary: Combines retained sources and round-specific evidence; checks operation inputs and recipe types; parses Markdown-link destinations separately from bare URLs to preserve original source addresses.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json, research/sources/round-04/audit-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-a234ddd91071"></a>

## SRC-a234ddd91071 — P01 p01-build-01 — rail-first-query.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-first-query.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-first-query.json`)

Summary: p01-build-01 rail-first-query.json: Retained native response with fields count, document_id, entities, geometry_revision, next_offset, ok, returned; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-a28ae7692d9d"></a>

## SRC-a28ae7692d9d — SKF iteration — second-slice-response.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/second-slice-response.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/second-slice-response.json`)

Summary: Completed mirrored nativeSLICE negative draft modifies only owned housingD7 and retains inside bearing side.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-a2ddc249d60b"></a>

## SRC-a2ddc249d60b — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/initial-state.json`)

Summary: Native document85 andexisting open-document state before creating converter document86.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-a2e021f0ada1"></a>

## SRC-a2e021f0ada1 — Meshroom command-line batch usage

Original source: [https://github.com/alicevision/Meshroom/blob/develop/INSTALL.md](https://github.com/alicevision/Meshroom/blob/develop/INSTALL.md)

Summary: Official Meshroom instructions document `meshroom_batch --input INPUT_IMAGES_FOLDER --output OUTPUT_FOLDER`; the executable also accepts a saved pipeline graph.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-a318f3e786ed"></a>

## SRC-a318f3e786ed — DA3Metric-Large — Hugging Face model card

Original source: [https://huggingface.co/depth-anything/DA3Metric-Large](https://huggingface.co/depth-anything/DA3Metric-Large)

Summary: DA3Metric-Large model card inspected 2026-11-12; URL redirected to uppercase repository slug. Card labels this specific checkpoint Apache 2.0, claims monocular metric depth with canonical depth multiplied by focal length, and shows inference depth/confidence maps, world-to-camera extrinsics, intrinsics and GLB/NPZ/PLY/Gaussian exports. The inspected card does not state a canonical focal reference or normalization divisor; do not generalize to every DA3 model.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-a36a990b86b7"></a>

## SRC-a36a990b86b7 — step-format.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/step-format.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/step-format.json`)

Summary: ActualImportFileactionselectingSTEPformat;waiting_inputdialogresult.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-a3700fe5d4e2"></a>

## SRC-a3700fe5d4e2 — Skills Directory `majiayu000` 3D Modeling

Original source: [https://www.skillsdirectory.com/skills/majiayu000-3d-modeling-claude-skill-registry](https://www.skillsdirectory.com/skills/majiayu000-3d-modeling-claude-skill-registry)

Summary: Skills Directory `majiayu000` 3D Modeling ; Directory displays a copied 3D-art skill and 666 stars/25 copies/101 views. Registry's source-linked guide traces the canonical entry to `omer-metin/skills-for-antigravity/skills/3d-modeling/SKILL.md` and lists exact-content copies including `Kedhareswer/kedhar_brain/agents/skills/design-ui-ux/3d-modeling/SKILL.md`. The accessible source SKILL.md covers topology, UVs, game/film exports and art references. Registry page shows Apache-2.0 metadata for omer-metin's copy, while explicitly directing readers to check original permission; the exact original author's licence remains unverified. ; Mesh/art skill, not engineering CAD. Readable source copy was web-inspected; repository source and licence provenance were inspected via the registry guide. It has no stated CAD kernel or AI service dependency. Listing counts and security scan are directory claims, not CAD validation.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-a3a2d5382a80"></a>

## SRC-a3a2d5382a80 — Battery terminal cover (P20C) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p20c-battery-terminal-cover.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p20c-battery-terminal-cover.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Separate geometry per battery route; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-a3e03c0d00b9"></a>

## SRC-a3e03c0d00b9 — cad — earthtojake/text-to-cad

Original source: [https://www.skills.sh/earthtojake/text-to-cad/cad](https://www.skills.sh/earthtojake/text-to-cad/cad)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: cad — earthtojake/text-to-cad. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-a426faf2681b"></a>

## SRC-a426faf2681b — Anderson3-6055P2 boot (C061) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c061-anderson3-6055p2-boot.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c061-anderson3-6055p2-boot.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Charge-port accessory; original kind source accessory reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-a43126b0540b"></a>

## SRC-a43126b0540b — `openscad/SKILL.md`

Original source: [https://github.com/mitsuhiko/agent-stuff/blob/main/skills/openscad/SKILL.md](https://github.com/mitsuhiko/agent-stuff/blob/main/skills/openscad/SKILL.md)

Summary: OpenSCAD skill (`mitsuhiko/agent-stuff`) ; Archived `openscad/SKILL.md` depends on installed `openscad` executable and shell scripts for preview, multi-angle snapshots, parameter extraction, syntax validation and STL export; it suggests Homebrew installation, which is OS-specific. Repo root licence is Apache-2.0. Source link: `openscad/SKILL.md`. ; Adapt its preview/validation pattern only after adjusting install commands to the host OS and checking scripts. It outputs mesh and does not give exact engineering B-rep or a feature tree. No service dependency is described.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-a4830284e0af"></a>

## SRC-a4830284e0af — Vectorizing Building Blueprints

Original source: [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf)

Summary: ACCV 2022 paper studies automatic vectorization of raster building blueprints and reviews primitive detection, floor-plan vectorization and structured reconstruction.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md.

<a id="src-a539aa71a816"></a>

## SRC-a539aa71a816 — Agent skill: cad-modeling-fusion

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/SKILL.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: cad-modeling-fusion. Source class: agent skill instructions. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-a5ea2c11ee81"></a>

## SRC-a5ea2c11ee81 — Franka Emika Panda Menagerie model README

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/README.md)

Summary: Identifies the Panda MJCF model, states MuJoCo 2.3.3 or later, Apache-2.0 model licence and documented derivation/geometry/inertia work.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r04.md.

<a id="src-a60085185158"></a>

## SRC-a60085185158 — Original SKF bearing drawing preserved

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/skf-sy20tf.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/skf-sy20tf.dwg`)

Summary: Existing ten-solid native reconstruction; measured crown32mm fails SKF A1=21mm. Original bytes match checkpointb36c147; corrected derivative uses a distinct path.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-a62979656e4c"></a>

## SRC-a62979656e4c — Leaf iteration — reopened-top.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-top.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-top.png`)

Summary: Inspected current top image shows case outline, pressed pan/ribs, four corner mounting bores and terminal projection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-a62b176d4381"></a>

## SRC-a62b176d4381 — SKF iteration — reopened-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-state.json`)

Summary: Actual recovered reopen state identifies derivative document75 and preserved unrelated open drawing identities.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-a635c02f99cb"></a>

## SRC-a635c02f99cb — OCS numerical contract checker source

Original source: ${CODEX_HOME}/skills/ocs-engineering/scripts/check_contract.py (`${CODEX_HOME}/skills/ocs-engineering/scripts/check_contract.py`)

Summary: Reads supplied point/axis/plane observations with one length/angular threshold pair per invocation; later adapter must preserve feature-specific applicability.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-a66a9495624e"></a>

## SRC-a66a9495624e — Driver iteration — reopened-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-state.json`)

Summary: Recovered derivative-open state identifies document78 and the separate checked driver path.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-a680edc6892e"></a>

## SRC-a680edc6892e — URDF model reference

Original source: [https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html)

Summary: URDF / ROS tooling ; Official `urdf_tutorial` teaches visual geometry, movable joints, collision and inertial properties, and Xacro; it is BSD-3-Clause. Tutorial repository. URDF model guidance states metres/radians and kilograms for position/mass conventions. URDF model reference ; URDF is a format; package and mesh licenses are independent. Tutorial: BSD-3-Clause. ; Robot kinematic interchange and ROS visualization/control workflows. URDF does not express all closed-chain or advanced dynamics semantics; preserve source domain model and report unsupported fields.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/domain-paths.md.

<a id="src-a6ae4a99861b"></a>

## SRC-a6ae4a99861b — imported-records-30.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-30.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-30.json`)

Summary: imported native record snapshot: BD:Insert, BE:Insert, BF:Insert, C0:Insert, C1:Insert, C2:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-a6e8373ba9d0"></a>

## SRC-a6e8373ba9d0 — Side lifting tab (P10) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p10-side-lifting-tab.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p10-side-lifting-tab.md`)

Summary: Input sheet registered from the inspected ferme manifest: frame; Side support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-a764655900e1"></a>

## SRC-a764655900e1 — FreeCAD contributing and licensing

Original source: [https://www.freecad.org/contributing.php?lang=eng](https://www.freecad.org/contributing.php?lang=eng)

Summary: Project license information; primary FreeCAD project page.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md.

<a id="src-a79889909bbf"></a>

## SRC-a79889909bbf — SKF iteration — capture-front.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/capture-front.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/capture-front.json`)

Summary: Completed native front capture response binds derivative document75,camera and image to actual request.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-a7aa934ff7de"></a>

## SRC-a7aa934ff7de — Retained Sumitomo PRO outline page1 cross-check

Original source: [https://assets.sumitomodrive.com/sites/default/files/2023-09/smartris-pro.pdf](https://assets.sumitomodrive.com/sites/default/files/2023-09/smartris-pro.pdf)

Summary: Actual page1 rendered and inspected; shows the same CH52308G10 driver outline and dimensions as the ECO drawing. The bound job uses the ECO original to preserve existing construction attribution.

Evidence: retained_manufacturer_outline_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-a7c2279a0c45"></a>

## SRC-a7c2279a0c45 — Motenergy ME0907 outline 0JWT.301.073

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/ME0907.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source/ME0907.pdf`)

Summary: Original dimensioned motor drawing retained from EV Europe. Supplies mounting groups, shaft/keyway section, locating pilot, main/rear axial stations, nominal thread designations and exterior outlines. DO NOT SCALE accompanies the drawing.

Evidence: downloaded_original.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-a807c8e08b82"></a>

## SRC-a807c8e08b82 — Existing OCS metric page-setup DXF fixture

Original source: ${OCS_ROOT}/tests/fixtures/plot/page-setups-metric.dxf (`${OCS_ROOT}/tests/fixtures/plot/page-setups-metric.dxf`)

Summary: Original existing fixture used read-only for the second inspection; actual INSUNITS code6 identifies metres. Original bytes remain unchanged.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-a83674c889fd"></a>

## SRC-a83674c889fd — point-05-web-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-05/point-05-web-sources.json](round-05/point-05-web-sources.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-a8b84ecb56bc"></a>

## SRC-a8b84ecb56bc — P01 p01-build-02 — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/ocs-journal.jsonl`)

Summary: p01-build-02 append-only request journal retains 43 events across 19 request identities, with original intents and responses. It supplies the native command/recovery history for this named attempt; request tokens are excluded.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-a8d7ba68a870"></a>

## SRC-a8d7ba68a870 — Enclosureiterationreport

Original source: [${MODELING_ROOT}/execution/c029-fibox-enclosure.md](../../execution/c029-fibox-enclosure.md)

Summary: Documentsexactvariant,newCAD,44checks,sourcecorrections,sourceframe,appliedhelperandactualmodels.

Evidence: executed_work_report.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-a8e753f7f1eb"></a>

## SRC-a8e753f7f1eb — Actual metric page-setup DXF inventory

Original source: [${MODELING_ROOT}/execution/dxf-inspection/page-setup-inventory.json](../../execution/dxf-inspection/page-setup-inventory.json)

Summary: Actual read-only run records one LINE and one DIMENSION; source header code6 declares metres, preserving actual units rather than inferring them from a filename.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-a9d0f0d71c99"></a>

## SRC-a9d0f0d71c99 — Installed DXF file-reading API source

Original source: ${NATIVE_READER_ROOT}/ezdxf/filemanagement.py (`${NATIVE_READER_ROOT}/ezdxf/filemanagement.py`)

Summary: Inspected readfile/read API supports strict decoding and original file parsing. The implementation chooses readfile with strict errors and performs no recovery rewrite.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-aa5f4c33e807"></a>

## SRC-aa5f4c33e807 — P02 crossmember — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/persistence.json`)

Summary: DWG2018 save/hash/audit-manifest and reopened identity checks PASS with one solid and zero dropped entities.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-aadc9e21c0ad"></a>

## SRC-aadc9e21c0ad — check_repair_cases.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/check_repair_cases.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/check_repair_cases.py`)

Summary: RannewhelperofflineonretainedbatteryandenclosurenativerecordswithoutchangingoldCAD.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-abde4c7c95ff"></a>

## SRC-abde4c7c95ff — Actual viewport-fixture DXF inventory

Original source: [${MODELING_ROOT}/execution/dxf-inspection/viewport-model-inventory.json](../../execution/dxf-inspection/viewport-model-inventory.json)

Summary: Actual read-only run records eight entity occurrences and preserved handles/context. Source header code0 produces NEEDS_UNIT_EVIDENCE rather than an assumed physical scale.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-ac0ff15cdc81"></a>

## SRC-ac0ff15cdc81 — check_c029_saved.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/check_c029_saved.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/check_c029_saved.py`)

Summary: Adaptedretainedsaved-checktemplateforFiboxandwrote29actualpersistedchecks.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-ac15e16a45ad"></a>

## SRC-ac15e16a45ad — Pilz source feature contract

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source-job.json`)

Summary: Pins45/87/120.6 dimensions andnames terminal/rail-clip geometry inputs.

Evidence: implementation_input_artifact.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-ac24864ef496"></a>

## SRC-ac24864ef496 — upstream GPL text

Original source: [https://github.com/blender/blender/blob/main/doc/license/GPL-license.txt](https://github.com/blender/blender/blob/main/doc/license/GPL-license.txt)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-ac393c8456b2"></a>

## SRC-ac393c8456b2 — https://raw.githubusercontent.com/cdcseacave/openMVS/master/LICENSE

Original source: [https://raw.githubusercontent.com/cdcseacave/openMVS/master/LICENSE](https://raw.githubusercontent.com/cdcseacave/openMVS/master/LICENSE)

Summary: - OpenMVS exact upstream license: https://raw.githubusercontent.com/cdcseacave/openMVS/master/LICENSE

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-07-software.md, research/reconstruction.md.

<a id="src-ac77c9e8c1c8"></a>

## SRC-ac77c9e8c1c8 — https://github.com/opencv/opencv/blob/4.x/LICENSE

Original source: [https://github.com/opencv/opencv/blob/4.x/LICENSE](https://github.com/opencv/opencv/blob/4.x/LICENSE)

Summary: 1. Name: OpenCV; Role: Planar image rectification and raster line candidates.; License: Apache-2.0 upstream.; Apis: cv2.getPerspectiveTransform(4 point pairs); cv2.warpPerspective; cv2.HoughLinesP; cv2.findContours/cv2.approxPolyDP; Dependencies: Python 3, OpenCV Python bindings (opencv-python or system package), NumPy; image file raster source.; Source urls: https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html; https://github.com/opencv/opencv/blob/4.x/LICENSE

Evidence: existing_report_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md.

<a id="src-ac94df9079cf"></a>

## SRC-ac94df9079cf — Parts Library repository

Original source: [https://github.com/FreeCAD/FreeCAD-library](https://github.com/FreeCAD/FreeCAD-library)

Summary: FreeCAD BIM Library ; FreeCAD BIM can browse and insert FCStd, STEP and BREP entries from the FreeCAD Parts Library, either offline or through its experimental online library option. BIM Library docs, Parts Library repository ; The BIM insertion feature does not change the license of inserted assets. The Parts Library collection is listed as CC-BY-3.0 in FreeCAD Addons; verify individual item attribution and embedded files. Many entries are generic architecture/MEP objects, not certified building product specifications.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r07.md, research/workflows/domain-paths.md.

<a id="src-acbface446ee"></a>

## SRC-acbface446ee — Keiyama JA08-700-4T100-02 steel rim (C003) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c003-keiyama-ja08-700-4t100-02-steel-rim.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c003-keiyama-ja08-700-4t100-02-steel-rim.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Keiyama wheel alternative; original kind seller/manufacturer dimensions recorded locally. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-accaca72881d"></a>

## SRC-accaca72881d — KiCad Libraries License

Original source: [https://www.kicad.org/libraries/license/](https://www.kicad.org/libraries/license/)

Summary: KiCad states that its library data is licensed under CC-BY-SA 4.0 with an exception for electronic designs and generated files that use the data. The exception permits use in a project without relicensing that project under CC-BY-SA; redistribution of the libraries or parts as a collection retains the library license and attribution. This statement applies to KiCad library data, not every third-party CAD asset.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-sources.md, research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-ace3d4ff19ae"></a>

## SRC-ace3d4ff19ae — https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp

Original source: [https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp](https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp)

Summary: Four page attempts failed and support no technical claim: Open3D 0.20.0 `RGBDImage` API page `https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html` timed out; versioned API URL `https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html` was unavailable via the web tool; GitHub HTML for `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp` returned cache miss; and `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp` returned cache miss. The default parameters were verified in the successful raw v0.20.0 `RGBDImage.h` declaration; conversion behavior was inspected in the raw `RGBDImageFactory.cpp` and `Image.cpp` sources recorded above. No further failed URLs support technical claims.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-ad068197fdc2"></a>

## SRC-ad068197fdc2 — IfcOpenShell add_profile_representation API

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_profile_representation/index.html)

Summary: Documents a profile extrusion IFC representation, depth in metres and profile placement axes.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r07.md, research/workflows/domain-paths.md.

<a id="src-ad0cb8976c1e"></a>

## SRC-ad0cb8976c1e — Earlier SKF reconstruction and dimension record

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/skf-sy20tf.md (`${FERME_ROOT}/engineering/module-development/cad/checks/skf-sy20tf.md`)

Summary: Retains original housing and insert reconstruction dimensions, drawing-derived seal/flinger dimensions, screw spacing and source references. The source-bound iteration preserves it as historical input and detects actual saved crown mismatch.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-ad1f82234be8"></a>

## SRC-ad1f82234be8 — Geometry Validation Rules

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/geometry_validation_rules.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/geometry_validation_rules.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Geometry Validation Rules. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ad3c319de0b3"></a>

## SRC-ad3c319de0b3 — plugin_host.rs

Original source: ${OCS_ROOT}/src/app/plugin_host.rs (`${OCS_ROOT}/src/app/plugin_host.rs`)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-ad47e1f99cf8"></a>

## SRC-ad47e1f99cf8 — Littelfuse20EV100 bolt-down fuse (C030) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c030-littelfuse20ev100-bolt-down-fuse.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c030-littelfuse20ev100-bolt-down-fuse.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Traction fuse candidate; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-ad9e8b3c3670"></a>

## SRC-ad9e8b3c3670 — Shared-family CAD follow-up metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/followup-acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/followup-acquisition.json`)

Summary: Retains exact source pages,family inference and actual non-download status with license/access observations.

Evidence: executed_acquisition_record.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-adb5f990a3ee"></a>

## SRC-adb5f990a3ee — Add-on listing

Original source: [https://www.freecad.org/addons.php?lang=en_EN](https://www.freecad.org/addons.php?lang=en_EN)

Summary: FreeCAD add-on step.parts connector ; FreeCAD listing describes searching an online open STEP parts catalog and inserting into the document. Add-on listing ; The connector's license is not sufficient evidence for every catalog asset's reuse rights. Capture item-level rights before caching or distributing.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-adc1b41ef30c"></a>

## SRC-adc1b41ef30c — P01 p01-build-01 — rail-entity_schema.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-entity_schema.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-entity_schema.json`)

Summary: p01-build-01 rail-entity_schema.json: Installed API response request_id_required: Supply a unique request_id (maximum 128 bytes); retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-ae16b67b352c"></a>

## SRC-ae16b67b352c — Coordinate Systems, Transformations and Units — SVG 2

Original source: [https://www.w3.org/TR/SVG2/coords.html](https://www.w3.org/TR/SVG2/coords.html)

Summary: The W3C SVG 2 specification defines each SVG viewport as a width/height drawing region in abstract user units. A `viewBox` transforms the user coordinate system relative to the viewport, and nested viewports and element `transform` properties add coordinate mappings. Absolute lengths follow CSS units; the specification defines 1 inch as 96 CSS pixels. SVG pixel or user-unit values therefore need their viewport, viewBox, nested transforms and physical-size interpretation retained before they become model dimensions.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-sources.md, research/sources/round-05/point-03-web-sources.json.

<a id="src-ae42dbaf6d16"></a>

## SRC-ae42dbaf6d16 — Installed MIT-licensed INSERT API source

Original source: ${NATIVE_READER_ROOT}/ezdxf/entities/insert.py (`${NATIVE_READER_ROOT}/ezdxf/entities/insert.py`)

Summary: Inspected matrix44 handles block base point, OCS, scale and rotation. multi_insert supplies rotated array-cell positions without scaling grid spacing; these existing APIs are used directly.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-ae801910597e"></a>

## SRC-ae801910597e — Original Sumitomo reconstruction source

Original source: ${TEMP_ROOT}/opencode/build_remaining_sumitomo.py (`${TEMP_ROOT}/opencode/build_remaining_sumitomo.py`)

Summary: Read existing driver construction and source attribution:186x116 base,168x98 mounting pattern, nominal terminals, loft and reconstructed connector positions. An unchanged copy is retained with the job.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-ae970b750172"></a>

## SRC-ae970b750172 — FreeCAD Topological Data Scripting (`Part` Module)

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/topological_scripting.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/topological_scripting.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Topological Data Scripting (`Part` Module). Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-aea29b81cf2e"></a>

## SRC-aea29b81cf2e — SKF iteration — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/result.json`)

Summary: CompletedSKFiteration records derivative SHA,62nativePASS,persistence,inspectedviews and appliedPython/skill improvement with40tests.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-aec737b38b33"></a>

## SRC-aec737b38b33 — SimpBMS board (C028) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c028-simpbms-board.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c028-simpbms-board.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; BMW; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-af8c2d79e989"></a>

## SRC-af8c2d79e989 — cad-r06.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r06.md](../workflows/details/cad-r06.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-afa0b4d5a10b"></a>

## SRC-afa0b4d5a10b — domain-paths.json

Original source: [${MODELING_ROOT}/research/workflows/domain-paths.json](../workflows/domain-paths.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-afba409b6281"></a>

## SRC-afba409b6281 — Gland source-readiness result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/readiness.json`)

Summary: Existing gate returns NEEDS_INPUT forcap/bodysegmentheights,assembledposition andpassagegeometry.

Evidence: executed_readiness_result.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-b00b92c70647"></a>

## SRC-b00b92c70647 — Depth Anything 3 — official repository, main branch

Original source: [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)

Summary: Official mutable main repository page inspected 2026-11-12. Documents monocular/multi-view depth, pose-conditioned depth, camera intrinsics/extrinsics estimation and `da3 video` CLI example with fps and GLB export options. Repository page advertises Apache-2.0 code; checkpoint/model terms remain model-specific.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r05.md.

<a id="src-b079e75fd12d"></a>

## SRC-b079e75fd12d — P02 crossmember — end-capture.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/end-capture.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/end-capture.json`)

Summary: Completed end-view capture response identifies the reopened component camera/document context.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-b08d4de19a31"></a>

## SRC-b08d4de19a31 — Fuse source-stage execution report

Original source: [${MODELING_ROOT}/execution/c030-fuse-source.md](../../execution/c030-fuse-source.md)

Summary: Explains exactpart source findings,shared M6 alternative,actual acquisition results and the named construction inputs.

Evidence: executed_work_report.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-b123fa7af4ef"></a>

## SRC-b123fa7af4ef — Orion Rev01 drawing render

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/Victron-Orion-Tr-Smart-dimension-drawing-preview.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/Victron-Orion-Tr-Smart-dimension-drawing-preview.png`)

Summary: Actual dimensioned front/side/detail views explicitly listORI241236120 andits mounting-slot reference labels.

Evidence: derived_pdf_render.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-b1451ce1d409"></a>

## SRC-b1451ce1d409 — License text

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/LICENSE](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-b165af8a4b88"></a>

## SRC-b165af8a4b88 — Usage — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/ifcconvert/usage.html](https://docs.ifcopenshell.org/ifcconvert/usage.html)

Summary: IfcConvert documentation accessed 2026-11-12; embedded CLI manual identifies example build 0.8.4-158fe92 with OCC 7.8.1. Lists GLB as binary glTF 2.0, metre default and convert-back-units, placement baking option, GlobalId filtering, serializer ID-name limits, and separate Z-up node option.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-b18991f27bde"></a>

## SRC-b18991f27bde — dom-r08.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r08.md](../workflows/details/dom-r08.md)

Summary: Existing local source cited by point 06 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-b1ac5466cbd1"></a>

## SRC-b1ac5466cbd1 — CadQuery Class Summary — CadQuery Documentation

Original source: [https://cadquery.readthedocs.io/en/stable/classreference.html](https://cadquery.readthedocs.io/en/stable/classreference.html)

Summary: The CadQuery Shape API documents `isValid()` as true when no defect is detected on the shape or any subshape, referring to OCCT `BRepCheck_Analyzer::IsValid` for the checks performed. This is a kernel-shape integrity check and does not establish agreement with the source drawing, correct units, dimensional accuracy or manufacturing suitability.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r09.md.

<a id="src-b238ff5da9a9"></a>

## SRC-b238ff5da9a9 — point-05-operations

Original source: [${MODELING_ROOT}/research/action-audit/point-05-operations.json](../action-audit/point-05-operations.json)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-b254a6b0bd67"></a>

## SRC-b254a6b0bd67 — Blender Scene API RNA source (main branch)

Original source: [https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_scene_api.cc](https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_scene_api.cc)

Summary: Official Blender RNA source defines Scene.ray_cast with a required depsgraph, world-space origin/direction and maximum distance. It documents evaluated geometry and outputs including hit boolean, location, normal, evaluated-mesh face index, original object and matrix. Location, normal and index correspond to the evaluated mesh; index can be -1 when original data is unavailable. The main-branch source does not identify an installed release.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-b264855e91e7"></a>

## SRC-b264855e91e7 — corrected-records-18.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-18.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-18.json`)

Summary: correctednativeentitysnapshot: BA:Insert, BB:Insert, BC:Insert, BD:Insert, BE:Insert, BF:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-b2d596e125f6"></a>

## SRC-b2d596e125f6 — SavedFiboxenclosure

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/fibox-arca-203015t-8121020.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/fibox-arca-203015t-8121020.dwg`)

Summary: NewnativeDWG2018manufacturerassembly;12soliddefinitions,16placedsolids,sourcecorrectedframes.

Evidence: executed_native_cad_artifact.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-b2e6a72711e2"></a>

## SRC-b2e6a72711e2 — Driver iteration — source-outline-page1.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/source-outline-page1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/source-outline-page1.png`)

Summary: Inspected rendering of retained ECO page1 identifies exact CH52308G10 drawing dimensions and physical features.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-b30357886048"></a>

## SRC-b30357886048 — https://github.com/microsoft/TRELLIS

Original source: [https://github.com/microsoft/TRELLIS](https://github.com/microsoft/TRELLIS)

Summary: - TRELLIS repository (repository declares MIT; dataset/model-weight terms and restrictions must be assessed separately): https://github.com/microsoft/TRELLIS

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-b32f7db38a9b"></a>

## SRC-b32f7db38a9b — https://github.com/tesseract-ocr/tesseract

Original source: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

Summary: 2. Name: Tesseract; Role: Dimension text candidates with boxes/confidence; humans verify engineering notation.; License: Apache-2.0 upstream.; Apis: tesseract image outputbase -l eng tsv; TSV bbox/confidence review; Dependencies: Tesseract OCR binary plus eng traineddata; TSV output is text candidates only.; Source urls: https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md; https://github.com/tesseract-ocr/tesseract

Evidence: existing_report_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md.

<a id="src-b33d12d0b924"></a>

## SRC-b33d12d0b924 — P01 p01-build-03 — body-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/body-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/body-checkpoint.json`)

Summary: p01-build-03 body-checkpoint.json: Binds partial/native stage to document 70, revision 8 and named part handles {'tube': '80'}; supports inspected recovery.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-b37df47b9e75"></a>

## SRC-b37df47b9e75 — Unitree Go1 model BSD-3-Clause license

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_go1/LICENSE](https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_go1/LICENSE)

Summary: - Unitree Go1 model BSD-3-Clause license

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-b3eaf3b1142c"></a>

## SRC-b3eaf3b1142c — ME0907 wheel shaft to rim adapter (P14ME) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p14me-me0907-wheel-shaft-to-rim-adapter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p14me-me0907-wheel-shaft-to-rim-adapter.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-b423063cc3e8"></a>

## SRC-b423063cc3e8 — placement-corrections.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/placement-corrections.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/placement-corrections.json`)

Summary: Actualhelperrunreadbacksfor16nativeCAScorrectionsand12unchangedACISdefinitions.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-b47fffcd39a7"></a>

## SRC-b47fffcd39a7 — 3D modeling implementation plan

Original source: [${MODELING_ROOT}/research/implementation-plan.md](../implementation-plan.md)

Summary: Prior project proposal identifies OCS as the interactive baseline, FreeCAD for constrained feature trees, code-CAD for scripted solids, raster plans, drawing conversion and verification routes. Used as existing project context, not as runtime evidence.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-b4cef6ac5426"></a>

## SRC-b4cef6ac5426 — SKF SY20TF bearing unit (C009) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c009-skf-sy20tf-bearing-unit.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c009-skf-sy20tf-bearing-unit.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907 supported-shaft candidate; original kind manufacturer dimensions in existing record. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered, local_source_or_execution_record_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-14/bearing-sources.json.

<a id="src-b51ee490a99b"></a>

## SRC-b51ee490a99b — Resistor source-readiness execution report

Original source: [${MODELING_ROOT}/execution/c035-resistor-source.md](../../execution/c035-resistor-source.md)

Summary: Records retained exact package datasheet,source-backed length/height/pitch and the named substrate-thickness input requirement from the actual review.

Evidence: executed_work_report.

Documents: research/sources/round-20/component-sources.json.

<a id="src-b56bc21f14db"></a>

## SRC-b56bc21f14db — rec-r06.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r06.md](../workflows/details/rec-r06.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-b5b5f2bbfc67"></a>

## SRC-b5b5f2bbfc67 — host.rs

Original source: ${OCS_ROOT}/crates/ocs_plugin_api/src/host.rs (`${OCS_ROOT}/crates/ocs_plugin_api/src/host.rs`)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-b600ecb1a3e1"></a>

## SRC-b600ecb1a3e1 — BMW module tray (P18) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p18-bmw-module-tray.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p18-bmw-module-tray.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; BMW; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-b64f05c5a931"></a>

## SRC-b64f05c5a931 — Fuse component source-stage result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/result.json`)

Summary: Connects shared-family exterior proposal,target100A identity,actual acquisition/access routes and dependent geometry evidence.

Evidence: executed_component_stage_record.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-b6504258277a"></a>

## SRC-b6504258277a — Point 03 visual and evidence review — vectors, sketches and small solids

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-03-visual.md](../action-audit/reviews/point-03-visual.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-b667bec43458"></a>

## SRC-b667bec43458 — https://github.com/CloudCompare/CloudCompare

Original source: [https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare)

Summary: - CloudCompare repository and license: https://github.com/CloudCompare/CloudCompare

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r07.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r04.md.

<a id="src-b66eb65ce0b7"></a>

## SRC-b66eb65ce0b7 — scripting security guidance

Original source: [https://docs.staging.blender.org/manual/en/latest/advanced/scripting/security.html](https://docs.staging.blender.org/manual/en/latest/advanced/scripting/security.html)

Summary: The Blender-hosted Blender Lab MCP repository is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its setup page requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The Blender Lab MCP page search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's scripting security guidance says Python scripts can perform unrestricted operations.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-b70a1a95f34d"></a>

## SRC-b70a1a95f34d — reopened-records-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-records-0.json`)

Summary: reopened native record snapshot: 81:Solid3D, 85:Insert, 89:Solid3D, 8D:Solid3D, 91:Solid3D, 95:Solid3D. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-b739e4946d72"></a>

## SRC-b739e4946d72 — MuJoCo model editing and MJZ

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst)

Summary: Documents mjSpec editing, XML/URDF parsing, compilation, MJCF and asset packaging.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-b74bd207d260"></a>

## SRC-b74bd207d260 — P01 p01-build-03 — reopened-audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-audit.json`)

Summary: p01-build-03 reopened-audit.json: Retained native response with fields bounds, document_id, issues, manifest, ok, source, status; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-b77d14bbded9"></a>

## SRC-b77d14bbded9 — TDK I1C2W010A120V converter board (C046) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c046-tdk-i1c2w010a120v-converter-board.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c046-tdk-i1c2w010a120v-converter-board.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; BT24 V regulation proposal; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-b794725381cf"></a>

## SRC-b794725381cf — Rounded-tube helper regression tests

Original source: [${MODELING_ROOT}/tests/test_rounded_tube.py](../../tests/test_rounded_tube.py)

Summary: Ten regression tests cover native clear-only selection semantics and mismatched picks, exact quarter-circle profile encoding, incorrect wall/radius/length observations, unsupported transformed/incomplete SAT and explicit UNKNOWN classification for reopened SAB data. Together with the existing18 tests the suite passed28 cases.

Evidence: authored_code_or_procedure_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-b7aa02d92193"></a>

## SRC-b7aa02d92193 — Local Python 3.14 JSON decoder source

Original source: ${SYSTEM_ROOT}/usr/lib/python3.14/json/decoder.py (`${SYSTEM_ROOT}/usr/lib/python3.14/json/decoder.py`)

Summary: Independent review inspected ordered pairs, dictionary conversion and nonfinite constants, supporting duplicate/nonfinite guards.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-b7d893687f49"></a>

## SRC-b7d893687f49 — p02-readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-readiness.json`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-b7e8e5d17d10"></a>

## SRC-b7e8e5d17d10 — SKF iteration — capture-isometric.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/capture-isometric.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/capture-isometric.json`)

Summary: Completed native isometric capture response identifies document75 and camera for inspected bearing component image.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-b81d432f6f0a"></a>

## SRC-b81d432f6f0a — KiCad library repositories

Original source: [https://github.com/KiCad/kicad-packages3D](https://github.com/KiCad/kicad-packages3D)

Summary: KiCad 3D library ; Board-footprint-linked 3D models for electronic components; the official package library is available through the KiCad library repositories. ; Library data is CC-BY-SA-4.0 with a specific exception: use in a design does not itself force licensing the design under CC-BY-SA; redistribution of the library or parts as a collection retains the library license and attribution. Official terms

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-b82677ad8889"></a>

## SRC-b82677ad8889 — MuJoCo Menagerie repository

Original source: [https://github.com/google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie)

Summary: Curated robot MJCF models and asset files; repository states each model directory has its own licence.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-b83d2a638faa"></a>

## SRC-b83d2a638faa — step-confirm.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/step-confirm.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/step-confirm.json`)

Summary: CompletedoriginalSTEPimportconfirmationresultforthenewdocument.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-b884395f7485"></a>

## SRC-b884395f7485 — c045_presave_measurements.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/c045_presave_measurements.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/c045_presave_measurements.py`)

Summary: Traversed source-corrected instance paths andrecorded point-set geometry before saving.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-b914a224eaf5"></a>

## SRC-b914a224eaf5 — rec-r01.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r01.md](../workflows/details/rec-r01.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-b9a7ffca5f8c"></a>

## SRC-b9a7ffca5f8c — skills.sh leaderboard

Original source: [https://www.skills.sh/](https://www.skills.sh/)

Summary: Skill catalogue sources inspected 2026-11-12: skills.sh leaderboard, glotoff/freecad-skills, reyk/freecad-ai-skill, mitsuhiko/agent-stuff, earthtojake/text-to-cad, Foster1202/cad-modeling-fusion-skill, and the installed OCS engineering skill. Existing findings are at `${EOLIENNES_ROOT}/research/cad-workflow/`; source candidates are also archived under `${ENERGY_RAW_ROOT}/wind-prototypes/cad-workflow/skills/`. The detailed OCS harness findings describe an installed-build read-only inspection and existing API receipts; the skill research contains captured source files and hashes. These findings were reused, not reacquired or changed.

Evidence: existing_report_registered, archived_original_referenced.

Documents: research/cad-and-skills.md, research/sources/round-02/archive-sources.json.

<a id="src-b9c03a1f1d09"></a>

## SRC-b9c03a1f1d09 — SKF iteration — reopened-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-records.json`)

Summary: Actual derivative ten-solid SAB records from document75 support independent savedfeature checks and regression inputs.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-b9f01467bce4"></a>

## SRC-b9f01467bce4 — P02 crossmember — document-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/document-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/document-checkpoint.json`)

Summary: Initial isolated P02 document identity/revision checkpoint supports inspected stage recovery without touching prior models.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-ba1c34303c57"></a>

## SRC-ba1c34303c57 — https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md)

Summary: 3. https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md

Evidence: existing_report_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r04.md.

<a id="src-ba79f85a852f"></a>

## SRC-ba79f85a852f — Action-by-action workflow audit

Original source: [${MODELING_ROOT}/research/action-audit/README.md](../action-audit/README.md)

Summary: Authored audit document recording Action-by-action workflow audit. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json.

<a id="src-bad31f6c036a"></a>

## SRC-bad31f6c036a — Point 03 — Confirmed dimensions and vector drawings to small CAD models

Original source: [${MODELING_ROOT}/research/action-audit/point-03-vector-and-solid.md](../action-audit/point-03-vector-and-solid.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-bae586b9c767"></a>

## SRC-bae586b9c767 — ModelSpec JSON Format

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/model_spec_schema.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/model_spec_schema.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: ModelSpec JSON Format. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-bb0cc073eb92"></a>

## SRC-bb0cc073eb92 — OpenSCAD library catalog

Original source: [https://openscad.org/libraries.html](https://openscad.org/libraries.html)

Summary: BOSL2 ; Parametric OpenSCAD shapes, masks and manipulators; OpenSCAD library catalog identifies BSD-2-Clause. Repository describes it as beta. BOSL2 repository ; BSD-2-Clause per official catalog; check repository license/version when vendoring. Parametric code is useful for generated primitives and fixtures, not a catalog of measured commercial hardware.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md.

<a id="src-bb1660749c18"></a>

## SRC-bb1660749c18 — STEPControl_Writer Class Reference — Open CASCADE Technology Reference Manual 8.0.1

Original source: [https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_control___writer.html](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_control___writer.html)

Summary: The supplied dev.opencascade.org URL redirects to https://occt3d.com/dev/doc/refman/html/class_s_t_e_p_control___writer.html. The served page identifies Open CASCADE Technology and its Reference Manual as version 8.0.1. It documents STEPControl_Writer::Transfer(TopoDS_Shape, STEPControl_StepModelType, ...) translating a shape to a STEP entity, with AsIs, ManifoldSolidBrep, FacetedBrep, ShellBasedSurfaceModel and GeometricCurveSet modes; each translation operation outputs a distinct root entity. Write(filename) writes the STEP model to a file and WriteStream(ostream) writes it to a stream. This is the shape-oriented STEPControl_Writer API; the separate STEPCAFControl_Writer reference documents CAF document/label and root-assembly transfer.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-03-independent.md, research/action-audit/reviews/point-03-sources.md, research/sources/round-05/point-03-web-sources.json.

<a id="src-bb6e841ed0bc"></a>

## SRC-bb6e841ed0bc — Gland source-stage result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/result.json`)

Summary: Connects exactLGidentity,familyWHdrawing,locatedCADselector andsourcegate.

Evidence: executed_component_stage_record.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-bbe2770322c8"></a>

## SRC-bbe2770322c8 — SKF iteration — native-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/native-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/native-records.json`)

Summary: Raw original ten-solid SAB observations from document74 retain actual faulty housing and complete other part geometry for independent comparisons.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-bbfca0dda33f"></a>

## SRC-bbfca0dda33f — corrected-blocks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-blocks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-blocks.json`)

Summary: Blockmembershipreadbackafter16sourceframecorrections.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-bc2defd7afa9"></a>

## SRC-bc2defd7afa9 — Raster-to-Graph floor-plan recognition

Original source: [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf)

Summary: Computer Graphics Forum paper describes a learned raster-floorplan framework that predicts wall junctions and segments as an ordered graph representation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md.

<a id="src-bc59d9c5c5c8"></a>

## SRC-bc59d9c5c5c8 — Point 05 visual and evidence review — existing CAD with photographs and scans

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-05-visual.md](../action-audit/reviews/point-05-visual.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-bc5f6a777dc4"></a>

## SRC-bc5f6a777dc4 — Leaf iteration — reopened-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/reopened-state.json`)

Summary: Recovered open state binds document 76 to the exact existing Leaf DWG and preserves other open drawing identities.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-bc6235b9e567"></a>

## SRC-bc6235b9e567 — corrected-blocks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-blocks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-blocks.json`)

Summary: Block membership readback after27 source placement corrections.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-bcae1b9fb83c"></a>

## SRC-bcae1b9fb83c — P02 crossmember — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/initial-state.json`)

Summary: Pre-build OCS state identifies the active rail document and all open work; later new-document construction preserves unrelated documents.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-bce7d3359ed2"></a>

## SRC-bce7d3359ed2 — Motenergy ME0907 motor (C005) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c005-motenergy-me0907-motor.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c005-motenergy-me0907-motor.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind component geometry reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-bcf9f8ff8137"></a>

## SRC-bcf9f8ff8137 — source repository and GPL licence

Original source: [https://github.com/solvespace/solvespace](https://github.com/solvespace/solvespace)

Summary: Primary source: SolveSpace official site, source repository and GPL licence. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-bd0f14e5688e"></a>

## SRC-bd0f14e5688e — README.md

Original source: ${ARCHITECTURE_ROOT}/research/README.md (`${ARCHITECTURE_ROOT}/research/README.md`)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-bd5ead990898"></a>

## SRC-bd5ead990898 — Initial Fibox drawing transcription

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/source-notes-initial.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/source-notes-initial.md`)

Summary: Initialdelegatedtableincludesrearfootdepthdatumandmountingplateopeningmisassociations,preservedbeforecoordinatorcorrection.

Evidence: delegated_initial_source_review.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-bda744cda1c8"></a>

## SRC-bda744cda1c8 — `skills/cad/SKILL.md`

Original source: [https://github.com/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md)

Summary: `cad` from `earthtojake/text-to-cad` ; Archived `skills/cad/SKILL.md` uses `cadgen` wrappers around build123d/OCCT, Python model scripts, STEP/mesh export, a CAD Viewer and local `cadgen mcp`. README pins Python 3.13 and `cadgen==0.7.25` in its command examples; `uvx` downloads managed runtime/dependencies. It says first run needs network. Usage statistics and crash reports are on by default with random install IDs; README says turn off using `uvx cadgen telemetry off`. Core modeling path is local after runtime download; optional manufacturing-service integrations are separate. Repository and skill licence are MIT. ; Strong candidate for an optional build123d-backed modeling and inspection path, with telemetry disabled or disclosed and the pinned environment audited. It brings its own runtime/server/viewer and is not only a prompt skill. The source supports editable Python source and exact B-rep through build123d/OCCT; exported meshes remain tessellated. Source links: `skills/cad/SK...

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-bddb6be8c5b8"></a>

## SRC-bddb6be8c5b8 — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/persistence.json`)

Summary: Recoveredoriginalreopenrequest,matchingDWGhash/manifestandzero-errorzero-warningaudit.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-be135dffe792"></a>

## SRC-be135dffe792 — Point 02 — Procedure designer notes

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-02-designer.md](../action-audit/reviews/point-02-designer.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-be85a93a4c48"></a>

## SRC-be85a93a4c48 — Fuse PDF and exact-model acquisition record

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/acquisition.json`)

Summary: Records manufacturer403,Mouser transfer failure,reader-only dimensions and screenshot placeholder. Distinguishes PDF-reader observations from retained originals and exact target identity from adjacent60A CAD.

Evidence: executed_acquisition_record.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-bea676f3a5b9"></a>

## SRC-bea676f3a5b9 — Caster frame doubler (P05D) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p05d-caster-frame-doubler.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p05d-caster-frame-doubler.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Removable caster support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-bec11051e812"></a>

## SRC-bec11051e812 — SKILL.md — documented_skill

Original source: ${FERME_ROOT}/skills/cad-construction/SKILL.md (`${FERME_ROOT}/skills/cad-construction/SKILL.md`)

Summary: Reusable source, component/frame, construction, feature-check and saved-file procedure. Applicability: Repository skill instructions and reproduction-package specification.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json, research/sources/round-07/parts-catalogue-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-bec1fb0c7b0c"></a>

## SRC-bec1fb0c7b0c — freshtechbro `web3d-integration-patterns/SKILL.md`

Original source: [https://github.com/freshtechbro/claudedesignskills/blob/main/.claude/skills/web3d-integration-patterns/SKILL.md](https://github.com/freshtechbro/claudedesignskills/blob/main/.claude/skills/web3d-integration-patterns/SKILL.md)

Summary: freshtechbro `web3d-integration-patterns/SKILL.md` (raw source) ; Raw source describes integration patterns for Three.js, GSAP ScrollTrigger, React Three Fiber, Motion and React Spring. It includes browser scene setup, render loops, state coordination, scroll animation and performance patterns; references the constituent library skills. ; Web scene and animation skill, not CAD. Its listed tools require JavaScript/npm packages and browser runtime. The page identifies no hosted AI or geometry-generation API. Repository-wide licence was not checked in this pass; no source copying recommended. Raw SKILL.md was web-inspected on 2026-11-12, not downloaded.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-bedb22ee447a"></a>

## SRC-bedb22ee447a — Saved battery placement and geometry checks

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/saved-assembly-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/saved-assembly-checks.json`)

Summary: 35 passing preservation checks cover13 source matrices,21 reachable vertex sets and39 instance paths/transforms. Reports17 closed-partner definitions,four open-partner records and source drawing/STEP dimensional observations separately.

Evidence: executed_verification_result.

Documents: research/sources/round-20/component-sources.json.

<a id="src-bee391035496"></a>

## SRC-bee391035496 — Precharge resistor Ohmite TA310PA1K00JE (C035) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c035-precharge-resistor-ohmite-ta310pa1k00je.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c035-precharge-resistor-ohmite-ta310pa1k00je.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Kelly wiring candidate; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-bf335a662f43"></a>

## SRC-bf335a662f43 — Awesome Skills 3d-models tag

Original source: [https://awesomeskill.ai/tag/3d-models](https://awesomeskill.ai/tag/3d-models)

Summary: Awesome Skills 3d-models tag ; Marketplace tag index lists many different skills; related tags include 3D modeling, generation, reconstruction, rendering and assets. ; Discovery index only, not a skill or quality result. Each candidate needs source `SKILL.md`, source code, licence and service-dependency review.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-bf686019745b"></a>

## SRC-bf686019745b — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/github/awesome-copilot](https://api.github.com/repos/github/awesome-copilot)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-bf7c144ea436"></a>

## SRC-bf7c144ea436 — reopen_c045.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/reopen_c045.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/reopen_c045.py`)

Summary: Recovered original reopen,verified hash/manifest/audit andretained saved records;capture laterfailed image identity.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-bfb6141184a2"></a>

## SRC-bfb6141184a2 — Direct Motenergy ME0907 outline copy

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/Motenergy-ME0907-outline.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/Motenergy-ME0907-outline.pdf`)

Summary: Original PDF acquired from the drawing link on Motenergy ME0907 page. Drawing title0JWT.301.073 and existing interfaces are identified in the delegated review; this retains the manufacturer-linked source separately from the EV Europe copy.

Evidence: downloaded_original.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-bfd136961cc3"></a>

## SRC-bfd136961cc3 — Nerfstudio installation and CLI examples

Original source: [https://docs.nerf.studio/quickstart/installation.html](https://docs.nerf.studio/quickstart/installation.html)

Summary: Official install guide documents CLI environment and a video-processing command; used only for documented CLI context, no installation was run.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r08.md.

<a id="src-bfdf4432e2de"></a>

## SRC-bfdf4432e2de — reopened-records-6.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-6.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reopened-records-6.json`)

Summary: reopenednativeentitysnapshot: 96:Insert, 9A:Solid3D, 9E:Solid3D, 9F:Solid3D, A3:Solid3D, A7:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-bfe06f8511b1"></a>

## SRC-bfe06f8511b1 — ROS URDF tutorial

Original source: [https://github.com/ros/urdf_tutorial](https://github.com/ros/urdf_tutorial)

Summary: Primary tutorial covers links, visual, movable joints, collision and inertial properties; repository declares BSD-3-Clause.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-bffa49b1e1cc"></a>

## SRC-bffa49b1e1cc — Global registration — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)

Summary: Open3D 0.20.0 documents point-cloud downsampling, normal estimation, FPFH feature matching and RANSAC for coarse source/target registration. RANSAC checks distance, edge-length similarity and optionally normal affinity; it returns a transformation applied to the source cloud to align with the target. The documented coarse result is followed by ICP refinement. These are source-documented pipeline operations, not local registration measurements.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r04.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r03.md, research/workflows/details/rec-r09.md.

<a id="src-c01e327d09e4"></a>

## SRC-c01e327d09e4 — P01 p01-build-01 — rail-profile-readback.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-profile-readback.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-profile-readback.json`)

Summary: p01-build-01 rail-profile-readback.json: Retained native response with fields collection, count, document_id, geometry_revision, next_offset, ok, records; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-c026420b57f4"></a>

## SRC-c026420b57f4 — ifcopenshell.api.geometry.add_representation — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html)

Summary: IfcOpenShell 0.9.0post1 API reference accessed 2026-11-12. `add_representation` takes an IFC context and Blender object/data geometry, optional SI offset and unit scale, and returns an IfcShapeRepresentation or None. API dependency and output do not amount to product classification, placement or relationship creation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-c057807eb5f6"></a>

## SRC-c057807eb5f6 — cad-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-02/cad-sources.json](round-02/cad-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-c0bd9d377ee7"></a>

## SRC-c0bd9d377ee7 — Saved battery terminal-face view

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/reopened-top.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/reopened-top.png`)

Summary: Actual reopened orthographic view inspected against the source top drawing; two terminals,polarity marks,centre fitting,logo and mounting tabs are visible.

Evidence: model_capture_inspected.

Documents: research/sources/round-20/component-sources.json.

<a id="src-c0ffb325c952"></a>

## SRC-c0ffb325c952 — Snapshot review

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/snapshot-review.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/snapshot-review.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Snapshot review. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c14ca78d0641"></a>

## SRC-c14ca78d0641 — Software review: existing components and CAD files to inspected reusable inputs

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-02-software.md](../action-audit/reviews/point-02-software.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-c19fa9da345e"></a>

## SRC-c19fa9da345e — Driver iteration — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/readiness.json`)

Summary: All15 required source expectations and pinned hashes pass SOURCE_READY with durable retained reconstruction evidence.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-c1fccd6db551"></a>

## SRC-c1fccd6db551 — `freecad-power-user/SKILL.md`

Original source: [https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-power-user/SKILL.md](https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-power-user/SKILL.md)

Summary: FreeCAD skills suite (`glotoff/freecad-skills`) ; Archived `freecad-user/SKILL.md` routes UI/modeling/workbench/import-export and topological naming guidance; `freecad-power-user/SKILL.md` covers Python, Part/Sketcher/Draft, B-rep, FeaturePython and headless/RPC automation; `freecad-developer/SKILL.md` covers C++ build/workbench development. README says skills derive from official FreeCAD documentation. Root skill suite licence is MIT; copied FreeCAD docs have separate attribution/licensing. ; Adapt `freecad-user` and `freecad-power-user` selectively as a complementary parametric backend; `developer` is outside normal modeling scope. The supplied suite is knowledge guidance, not tested evidence that generated files meet requirements. Source links: `freecad-user/SKILL.md`, `freecad-power-user/SKILL.md`, `freecad-developer/SKILL.md`. Archived local files were inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-c2506583d058"></a>

## SRC-c2506583d058 — PicoGK documentation index

Original source: [https://picogk.org/doc/](https://picogk.org/doc/)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: PicoGK documentation index. Source class: official documentation HTML. Original reuse terms: Documentation page provides no explicit reuse terms; archive does not grant additional rights.

Evidence: archived_original_referenced, existing_report_registered.

Documents: research/sources/round-02/archive-sources.json, research/sources/round-02/project-sources.json.

<a id="src-c2bf631e3721"></a>

## SRC-c2bf631e3721 — Square-tube corner research for main-frame rails and crossmembers

Original source: [${MODELING_ROOT}/research/tube-corner-research.md](../tube-corner-research.md)

Summary: Luna report compares EN 10219-2:2019 cold-formed and EN 10210-2:2019 hot-finished nominal section-property corner radii, external manufacturing profile limits and seller evidence for item040819. It links these findings to P01/P02 and records reference-model and measured-stock alternatives as proposals.

Evidence: authored_research_document_inspected.

Documents: research/sources/round-10/tube-corner-local-sources.json.

<a id="src-c2f8f1ee81fd"></a>

## SRC-c2f8f1ee81fd — acis_export.rs

Original source: ${OCS_ROOT}/src/scene/convert/acis_export.rs (`${OCS_ROOT}/src/scene/convert/acis_export.rs`)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-c2fb7b743a7c"></a>

## SRC-c2fb7b743a7c — build123d modeling patterns

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/build123d-modeling.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/build123d-modeling.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: build123d modeling patterns. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c30253c39c7d"></a>

## SRC-c30253c39c7d — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/result.json`)

Summary: C045 IN_PROGRESS result:39 native checks andpersistence pass,visual check fails;applied capture-identity procedure linked.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-c325f62a1a2e"></a>

## SRC-c325f62a1a2e — Python scripting tutorial

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Python_scripting_tutorial.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Python_scripting_tutorial.md)

Summary: Primary sources: FreeCAD source/licence, Sketcher Python scripting, Part scripting, Python scripting tutorial, Part Design concepts. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-c35c5442f991"></a>

## SRC-c35c5442f991 — SKF iteration — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/readiness.json`)

Summary: All required bound SKF source features and pinned source hashes returnSOURCE_READY before dependent revision.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-c3a52bea4793"></a>

## SRC-c3a52bea4793 — SB50 housing source image

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/sb50-datasheet-page-1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/sb50-datasheet-page-1.png`)

Summary: Actual manufacturer page1 shows housing bottom view and35.1 width/22.5+19.1+6.4 axial chain,Ø3.7 holes andmated81.3×15.9 view.

Evidence: derived_pdf_render.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-c3c48b5318f8"></a>

## SRC-c3c48b5318f8 — Kelly archive member 48VCW.pdf

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/kelly-archive/48VCW.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/kelly-archive/48VCW.pdf`)

Summary: Retained original48V clockwise performance-curve PDF extracted with the supplied motor archive. Acquired as original archive content; this geometry batch makes no curve-value interpretation.

Evidence: extracted_original_archive_member.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-c4427df066e7"></a>

## SRC-c4427df066e7 — corrected-records-18.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-18.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-18.json`)

Summary: corrected native record snapshot: B1:Insert, B2:Insert, B3:Insert, B4:Insert, B5:Insert, B6:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-c49f0a4410c4"></a>

## SRC-c49f0a4410c4 — Installed CAD and computational engineering command availability inventory

Original source: ${ENERGY_RAW_ROOT}/wind-prototypes/cad-workflow/harness/installed-tools-path-inventory.json (`${ENERGY_RAW_ROOT}/wind-prototypes/cad-workflow/harness/installed-tools-path-inventory.json`)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: Installed CAD and computational engineering command availability inventory. Source class: read-only local PATH lookup and version probes. Original reuse terms: not applicable; locally generated environment observation

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c4bd2d7b4e79"></a>

## SRC-c4bd2d7b4e79 — Interpreting a CAD request

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/cad-brief.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/cad-brief.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Interpreting a CAD request. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c52a21c8147a"></a>

## SRC-c52a21c8147a — New motor implementation report

Original source: [${MODELING_ROOT}/execution/c005-me0907.md](../../execution/c005-me0907.md)

Summary: Records new FERME model dimensions/detail, 18 saved checks, eight focused tests, source corrections, inspected views and the reusable axial construction/check improvement.

Evidence: executed_work_report.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-c5c9233bf7a9"></a>

## SRC-c5c9233bf7a9 — Rear attachment crossmember doubler (P09D) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p09d-rear-attachment-crossmember-doubler.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p09d-rear-attachment-crossmember-doubler.md`)

Summary: Input sheet registered from the inspected ferme manifest: attachments; Rear interface support proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-c5c9d3ec5705"></a>

## SRC-c5c9d3ec5705 — OpenCADStudio 2026.42 generated capability, command, and record-schema responses

Original source: ${ENERGY_RAW_ROOT}/wind-prototypes/cad-workflow/harness/installed-2026.42-readonly-api-receipts.json (`${ENERGY_RAW_ROOT}/wind-prototypes/cad-workflow/harness/installed-2026.42-readonly-api-receipts.json`)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: OpenCADStudio 2026.42 generated capability, command, and record-schema responses. Source class: read-only live runtime API observation; not product documentation. Original reuse terms: not applicable; locally generated observation of installed application output

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c5e854fd419c"></a>

## SRC-c5e854fd419c — cad.py

Original source: ${FERME_ROOT}/skills/cad-construction/scripts/cad.py (`${FERME_ROOT}/skills/cad-construction/scripts/cad.py`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-c65b8007a000"></a>

## SRC-c65b8007a000 — Nerfstudio export geometry

Original source: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md)

Summary: Documents ns-export pointcloud to PLY, TSDF meshes as available for all models, Poisson meshes only for models predicting normals, OBJ textured meshes and NeRF texture transfer to existing meshes.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r08.md.

<a id="src-c66fe74bfd16"></a>

## SRC-c66fe74bfd16 — Existing CAD and checks index

Original source: ${FERME_ROOT}/engineering/module-development/cad/README.md (`${FERME_ROOT}/engineering/module-development/cad/README.md`)

Summary: Existing local component/action/skill/catalogue source reused by the consolidated plan. Evidence and proposal boundaries remain in the original record.

Evidence: local_source_inspected, local_execution_evidence_inspected, local_execution_source_inspected, local_source_or_execution_record_inspected.

Documents: research/sources/round-08/component-plan-sources.json, research/sources/round-11/rail-execution-sources.json, research/sources/round-13/crossmember-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json.

<a id="src-c69eb556dd4e"></a>

## SRC-c69eb556dd4e — control-bootstrap-prefix.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/control-bootstrap-prefix.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/control-bootstrap-prefix.py`)

Summary: Exact actual control bootstrap prefix loads existing guarded client/helper andexplicit session;private descriptor content omitted.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-c70fd33bd9df"></a>

## SRC-c70fd33bd9df — Operations — build123d 0.13.1.dev341+gc0fb3a896 documentation

Original source: [https://build123d.readthedocs.io/en/latest/operations.html](https://build123d.readthedocs.io/en/latest/operations.html)

Summary: Official build123d documentation says operations accept existing objects and return new objects; `extrude()` creates a 3D Part from a Sketch or Face, using a specified amount/direction or an `until` target. Operations work through Algebra and Builder APIs over build123d objects. This is kernel-part construction documentation, not a constraint-solving sketch API claim or an observed validity result. The page's `latest` documentation reported a development version at access.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-c748eeb196bb"></a>

## SRC-c748eeb196bb — rec-r05.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r05.md](../workflows/details/rec-r05.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-c75f41a7dcd4"></a>

## SRC-c75f41a7dcd4 — https://github.com/alicevision/Meshroom/blob/develop/COPYING.md

Original source: [https://github.com/alicevision/Meshroom/blob/develop/COPYING.md](https://github.com/alicevision/Meshroom/blob/develop/COPYING.md)

Summary: - Meshroom copying/licenses: https://github.com/alicevision/Meshroom/blob/develop/COPYING.md

Evidence: existing_report_registered.

Documents: research/reconstruction.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r06.md.

<a id="src-c777cf43a2bb"></a>

## SRC-c777cf43a2bb — Trelleborg tube 6.00-9TR15 (C002) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c002-trelleborg-tube-6-00-9tr15.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c002-trelleborg-tube-6-00-9tr15.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Common wheel reference; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-c7a5d7a2632d"></a>

## SRC-c7a5d7a2632d — rec-r08.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r08.md](../workflows/details/rec-r08.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-c838814ff6f2"></a>

## SRC-c838814ff6f2 — Current converter capture request and recovery

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/recheck-2026-11-13/ocs-journal.jsonl`)

Summary: Write-ahead capture intent, initial polling-bound responses and original-request recovery for the current user view.

Evidence: executed_capture_journal.

Documents: research/sources/round-28/converter-view-recheck-sources.json.

<a id="src-c84e8663456d"></a>

## SRC-c84e8663456d — TRELLIS.2 — official repository, main branch

Original source: [https://github.com/microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)

Summary: Official mutable main repository inspected 2026-11-12. Example runs `pipeline.run(image)[0]` to produce a mesh and exports via O-Voxel `to_glb`. README says tested only on Linux, requires NVIDIA GPU with at least 24 GB memory, and recommends CUDA Toolkit 12.4. These are source setup conditions, not local measurements.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r10.md.

<a id="src-c98a5b96ef0d"></a>

## SRC-c98a5b96ef0d — Blender Scene Python API

Original source: [https://docs.blender.org/api/current/bpy.types.Scene.html](https://docs.blender.org/api/current/bpy.types.Scene.html)

Summary: Search-indexed API identifies Scene.ray_cast and scene annotation properties for world-space surface picking; direct page retrieval returned HTTP 402 in this research session. Claim limited to the indexed API entry; exact signature should be checked from installed Blender API at implementation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-visual.md, research/sources/round-02/reconstruction-sources.json, research/workflows/details/mix-r07.md, research/workflows/details/rec-r07.md.

<a id="src-c9c4bd1b2994"></a>

## SRC-c9c4bd1b2994 — point-04-operations

Original source: [${MODELING_ROOT}/research/action-audit/point-04-operations.json](../action-audit/point-04-operations.json)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-c9c50a504fb8"></a>

## SRC-c9c50a504fb8 — json — JSON encoder and decoder — Python 3.15.2 documentation

Original source: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)

Summary: Official Python documentation describes JSON decoding, default conversions, custom parse_float and parse_int callbacks receiving numeric token strings, parse_constant for NaN/Infinity tokens, object_pairs_hook receiving ordered object pairs, and JSONDecodeError for malformed documents. By default, the decoder accepts NaN/Infinity extensions and repeated object names, keeping only the last repeated value. For strict intake, a caller can reject constants and inspect pairs to detect duplicate names. Decoding exposes structure and syntax; it does not assign units, feature identity or engineering meaning.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-01-model-brief.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-04/intake-sources.json.

<a id="src-c9cb9090afed"></a>

## SRC-c9cb9090afed — Driver iteration — capture-isometric.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/capture-isometric.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/capture-isometric.json`)

Summary: Completed isometric capture response identifies document78 and actual component image.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-ca19e3275b4b"></a>

## SRC-ca19e3275b4b — native-plot-result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/native-plot-result.json`)

Summary: Completed native PDF plot response fordocument87,one297×210mm page;visual content checked separately.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-ca3076996fa5"></a>

## SRC-ca3076996fa5 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill](https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-caa0e7dcf088"></a>

## SRC-caa0e7dcf088 — Battery fuse CNL150 (C065) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c065-battery-fuse-cnl150.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c065-battery-fuse-cnl150.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Mersen fuse alternative; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-cab5e73f144b"></a>

## SRC-cab5e73f144b — Existing OCS viewport-association DXF fixture

Original source: ${OCS_ROOT}/tests/fixtures/dim_assoc/viewport_associations.dxf (`${OCS_ROOT}/tests/fixtures/dim_assoc/viewport_associations.dxf`)

Summary: Original existing fixture used read-only for the first actual DXF inspection; contains model/paper contexts and diverse entity types. Original bytes remain unchanged.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-cabea6f9d38d"></a>

## SRC-cabea6f9d38d — Category1 lower linkage pin (C063) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c063-category1-lower-linkage-pin.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c063-category1-lower-linkage-pin.md`)

Summary: Input sheet registered from the inspected ferme manifest: attachments; Reference attachment interface; original kind source component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-cad1c2a4c242"></a>

## SRC-cad1c2a4c242 — Command line mode — CloudCompare wiki

Original source: [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode)

Summary: The official CloudCompare CLI page states command-line mode exists since 2.3 and lists version 2.14.beta options. `-C2C_DIST` compares the first loaded/generated cloud against the second reference cloud; `-C2M_DIST` compares the first cloud against the first mesh. Results are distance scalar fields on compared cloud points; cloud-to-cloud `-SPLIT_XYZ` adds displacement components, and `-MAX_DIST` caps nearest-neighbor search. Distances inherit coordinate units and comparison direction from argument order.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r04.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r07.md, research/workflows/details/rec-r09.md, research/workflows/details/rec-r10.md.

<a id="src-cb2c93b6107b"></a>

## SRC-cb2c93b6107b — OpenCV 4.13 Perspective-n-Point pose computation

Original source: [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)

Summary: solvePnP estimates object/world-to-camera rotation and translation from 3D/2D correspondences, intrinsics and distortion; camera axes are X right, Y down, Z forward.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/rec-r03.md, research/workflows/details/rec-r07.md, research/workflows/details/rec-r09.md.

<a id="src-cb4319e9559f"></a>

## SRC-cb4319e9559f — Initial SB50 delegated notes

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/source-notes-initial.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/source-notes-initial.md`)

Summary: Preserves original kit mapping/source outcomes andinitial mistaken11.1 barrel-diameter interpretation.

Evidence: delegated_initial_source_review.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-cb44d69bba55"></a>

## SRC-cb44d69bba55 — AHDBM06 mating plug geometry (C062) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c062-ahdbm06-mating-plug-geometry.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c062-ahdbm06-mating-plug-geometry.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Agricultural interface provision; original kind manufacturer mate-family reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-cb56cc1e6215"></a>

## SRC-cb56cc1e6215 — corrected-records-6.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-6.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-6.json`)

Summary: correctednativeentitysnapshot: 96:Insert, 9A:Solid3D, 9E:Solid3D, 9F:Solid3D, A3:Solid3D, A7:Insert. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-cb5cec23d032"></a>

## SRC-cb5cec23d032 — Workflow routes linked to detailed actions

Original source: [${MODELING_ROOT}/research/action-audit/workflow-to-actions.md](../action-audit/workflow-to-actions.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-05/audit-index-sources.json, research/sources/round-08/component-plan-sources.json.

<a id="src-cb92cde3eea0"></a>

## SRC-cb92cde3eea0 — P02 crossmember — reopened-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-checkpoint.json`)

Summary: Reopened checkpoint binds the saved P02 component handle and document/revision to its completed body.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-cb939ff4c2d6"></a>

## SRC-cb939ff4c2d6 — Completed saved rail verification report

Original source: [${MODELING_ROOT}/execution/p01-saved-verification.md](../../execution/p01-saved-verification.md)

Summary: Reports live saved-body checks, unchanged DWG hash, body-derived versus zero API bounds, documented OCS/ACIS unit metadata, dependency installation results,32 passing tests and the eligible crossmember.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-cbdfa4a88a6b"></a>

## SRC-cbdfa4a88a6b — Leaf iteration — capture-terminal.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/capture-terminal.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/capture-terminal.json`)

Summary: Completed terminal-end capture response identifies document 76 and its three distinct terminal assemblies.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-cc34a83be8f3"></a>

## SRC-cc34a83be8f3 — Caster pin positive keeper (C020) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c020-caster-pin-positive-keeper.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c020-caster-pin-positive-keeper.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Removable support proposal; original kind retention component geometry input. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-cc58c415a1bb"></a>

## SRC-cc58c415a1bb — EVEA ME0907 product page / Autodesk Gallery viewer

Original source: [https://www.evea-solutions.com/fr/moteurs-synchrones/668-moteur-synchrone-me0907-pmsm-brushless.html](https://www.evea-solutions.com/fr/moteurs-synchrones/668-moteur-synchrone-me0907-pmsm-brushless.html)

Summary: Page states 3D model available on request and links a public Autodesk Gallery viewer. No request was sent.

Evidence: delegated_web_inspection.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-cc688c1df94b"></a>

## SRC-cc688c1df94b — RadioMaster Pocket ELRS transmitter (C057) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c057-radiomaster-pocket-elrs-transmitter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c057-radiomaster-pocket-elrs-transmitter.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Handheld operator equipment; original kind existing component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-ccbf0b22fcf6"></a>

## SRC-ccbf0b22fcf6 — cad-r10.md

Original source: [${MODELING_ROOT}/research/workflows/details/cad-r10.md](../workflows/details/cad-r10.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-ccd90649a995"></a>

## SRC-ccd90649a995 — source-placement-plan.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source-placement-plan.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source-placement-plan.json`)

Summary: 17sourceframesand16uniqueinverse-matchednativeplacementswithreviewedtargetfields.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-cce96de57cbe"></a>

## SRC-cce96de57cbe — Ideas

Original source: [${MODELING_ROOT}/research/action-audit/ideas.json](../action-audit/ideas.json)

Summary: Authored audit document recording Ideas. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected, local_source_inspected, registered_proposal_and_execution_evidence, registered_proposal.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json, research/sources/round-06/implementation-queue-sources.json, research/sources/round-21/fuse-sources.json, research/sources/round-26/relay-sources.json.

<a id="src-cd7868332c03"></a>

## SRC-cd7868332c03 — `SKILL.md`

Original source: [https://github.com/Foster1202/cad-modeling-fusion-skill/blob/main/SKILL.md](https://github.com/Foster1202/cad-modeling-fusion-skill/blob/main/SKILL.md)

Summary: `cad-modeling-fusion` (`Foster1202/cad-modeling-fusion-skill`) ; Archived `SKILL.md` and README describe a ModelSpec JSON validated by Python scripts, generators for Autodesk Fusion, FreeCAD and OpenSCAD, STEP/STL/OBJ export attempts, and optional Computer Use for Fusion. Python core uses standard library; backend application required only to run its generated code. Root licence is MIT. ; Consider its intermediate ModelSpec/validation structure, but route output to FreeCAD/OpenSCAD only and do not require Fusion. Backends have different semantics and may emit approximations; inspect output and generated warnings. Source link: `SKILL.md`. Archived local skill and references were inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-cd8d24d026d3"></a>

## SRC-cd8d24d026d3 — Point 05 — Alignment and parametric remodeling

Original source: [${MODELING_ROOT}/research/action-audit/point-05-alignment-and-remodeling.md](../action-audit/point-05-alignment-and-remodeling.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-ce0594707cbb"></a>

## SRC-ce0594707cbb — item-angle-bracket-set-41115-native.json — recorded_check_results

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json (`${FERME_ROOT}/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json`)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-ce70036fb35b"></a>

## SRC-ce70036fb35b — 3D modeling

Original source: [${MODELING_ROOT}/README.md](../../README.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-ce92c7f02e89"></a>

## SRC-ce92c7f02e89 — OpenSCAD documentation

Original source: [https://openscad.org/documentation.html](https://openscad.org/documentation.html)

Summary: Documents OpenSCAD source and command-line usage for rendering/exporting geometry.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-03-visual.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r10.md.

<a id="src-cea6a9237427"></a>

## SRC-cea6a9237427 — Integrated Orion source review

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/source-notes.md`)

Summary: Links coordinator correction to preserved initial interpretation andretains original links,dimension labels andC045 family applicability.

Evidence: reviewed_source_interpretation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-cf13f71acbca"></a>

## SRC-cf13f71acbca — corrected-records-12.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-12.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/corrected-records-12.json`)

Summary: correctednativeentitysnapshot: A8:Insert, A9:Insert, AA:Insert, AE:Solid3D, B2:Solid3D, B6:Solid3D. ExactpropertiesandACISbytesusedforplacement/geometrycomparison.

Evidence: executed_native_record_read.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-cf30fb2ca81a"></a>

## SRC-cf30fb2ca81a — Driver iteration — reopened-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-records.json`)

Summary: Actual saved derivative SAB records supply all141 passing feature checks and regression inputs.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-cf410cec238a"></a>

## SRC-cf410cec238a — Actual retained-manual model-table review

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/coordinator-review.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/coordinator-review.md`)

Summary: PDF text extraction finds48/12-20 andno48/12-30;separates retained PDF,delegated price-list claim,project input andexact C045 drawing coverage.

Evidence: executed_coordinator_review.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-cf6156d88759"></a>

## SRC-cf6156d88759 — P01 p01-build-02 — initial-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/initial-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-02/initial-state.json`)

Summary: p01-build-02 initial-state.json: Observed document 68 revision 8 with open-document identities and camera/command state; used for write isolation or capture provenance.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-cf83883aed8c"></a>

## SRC-cf83883aed8c — Victron smallBMS NG (C054) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c054-victron-smallbms-ng.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c054-victron-smallbms-ng.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Victron alternative BMS arrangement; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-cfdbfbbc0d31"></a>

## SRC-cfdbfbbc0d31 — imported-audit.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-audit.json`)

Summary: Initial nine-solid/29-block-reference manifest withzeroerrors/warnings.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-cfeb029989f0"></a>

## SRC-cfeb029989f0 — Point 04 source check: raster interpretation, orthographic views and IFC

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-04-sources.md](../action-audit/reviews/point-04-sources.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-d0312b87a2c9"></a>

## SRC-d0312b87a2c9 — P02 crossmember — pre-save-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/pre-save-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/pre-save-records.json`)

Summary: Raw native SAT record of the actual P02 solid in document72 supplies the original surface/vertex observations.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-d08c92fa1104"></a>

## SRC-d08c92fa1104 — P01 p01-build-01 — rail-after-cut-records.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-after-cut-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-after-cut-records.json`)

Summary: p01-build-01 rail-after-cut-records.json: 2 native entity records in document 68, revision 8; stores exact geometry encoding and properties for interpretation independently of PASS labels.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-d0936a70fd33"></a>

## SRC-d0936a70fd33 — reusable-repair-regression.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reusable-repair-regression.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/reusable-repair-regression.json`)

Summary: Twoofflinerecordedcomponenthelperchecks:13battery/16enclosureplacementsand21/12unchangeddefinitions.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d130021486e1"></a>

## SRC-d130021486e1 — PicoGK upstream LICENSE file

Original source: [https://raw.githubusercontent.com/leap71/PicoGK/main/LICENSE](https://raw.githubusercontent.com/leap71/PicoGK/main/LICENSE)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: PicoGK upstream LICENSE file. Source class: official repository license original, plain text. Original reuse terms: Apache License 2.0; preserve the complete license text and notices.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-d1328d9f4a93"></a>

## SRC-d1328d9f4a93 — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/readiness.json`)

Summary: SOURCE_READYresultfromexistingrequiredfeature/sourcehashgate.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d17309e8596a"></a>

## SRC-d17309e8596a — Fibox rear-view detail

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-front-detail.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-front-detail.png`)

Summary: Derivedrear-viewcropretainsmounting/openingleadersforfeatureassociation.

Evidence: derived_pdf_render.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d191df74c19e"></a>

## SRC-d191df74c19e — control-bootstrap-prefix.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/control-bootstrap-prefix.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/control-bootstrap-prefix.py`)

Summary: Exactexecutedcontrolprefixloadingexistingguardedclient/helperandexplicitOCSsession;descriptorcontentsomitted.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d19d818a7706"></a>

## SRC-d19d818a7706 — Perrin / Fers & Métaux — Tube carré 40×40×3, item 040819

Original source: [https://www.fers-metaux.com/mes-produits/fer/tubes-carres/3004g-tube-carre](https://www.fers-metaux.com/mes-produits/fer/tubes-carres/3004g-tube-carre)

Summary: Seller page identifies product 040819 as TUBE CARRE 40X40X3, lists 5.62 EUR TTC per metre and 19.8 kg, states bars are 6 m, dimensions are exterior, standard or cut lengths are available, and cutting tolerance is +5 mm. The inspected page provides no manufacturing route, EN standard, grade or corner-radius measurement.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-d1c0e9f5deef"></a>

## SRC-d1c0e9f5deef — Authorized cleanup of newly authored examples

Original source: [${MODELING_ROOT}/research/cleanup-record.md](../cleanup-record.md)

Summary: Records the removal of 13 example files, verified original Git revision and SHA-256 values, prior scope finding and replacement of active example references with documented third-party APIs.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-d1cfd29ff4b9"></a>

## SRC-d1cfd29ff4b9 — Retained SKF technical data sheet

Original source: [https://docs.rs-online.com/9fa3/A700000007995170.pdf](https://docs.rs-online.com/9fa3/A700000007995170.pdf)

Summary: Primary6pagePDF inspected with text and actual page3/4images. A=32,A1=21,L=127,H2=64.5,H=33.3,d=20,J=97,N=11.5,N1=20.5,B=31,s1=18.3,B4=4.5; fitting and M6 screw details pin sourcejob expectations. Mass0.56kg registered separately.

Evidence: retained_primary_document_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-d25b3e6e0e1d"></a>

## SRC-d25b3e6e0e1d — workflow-to-actions

Original source: [${MODELING_ROOT}/research/action-audit/workflow-to-actions.json](../action-audit/workflow-to-actions.json)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-05/audit-index-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-d25c92b0aebf"></a>

## SRC-d25c92b0aebf — PicoGK official repository page and README

Original source: [https://github.com/leap71/PicoGK](https://github.com/leap71/PicoGK)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: PicoGK official repository page and README. Source class: official repository page containing README excerpt and repository metadata. Original reuse terms: Repository identifies Apache-2.0; the archive contains the repository page, not the full LICENSE text. Preserve upstream copyright and notices; exact licence terms require the original LICENSE file.

Evidence: archived_original_referenced, existing_report_registered.

Documents: research/sources/round-02/archive-sources.json, research/sources/round-02/project-sources.json.

<a id="src-d3096ede4e6f"></a>

## SRC-d3096ede4e6f — Driver iteration — retained-source/original-construction-source.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/retained-source/original-construction-source.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/retained-source/original-construction-source.py`)

Summary: Unchanged retained copy of the inspected original Sumitomo builder; used as reconstruction source evidence, with its original code and attribution preserved.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-d32e74eebf36"></a>

## SRC-d32e74eebf36 — build_item_profile_segment.py — existing_component_code

Original source: ${TEMP_ROOT}/opencode/build_item_profile_segment.py (`${TEMP_ROOT}/opencode/build_item_profile_segment.py`)

Summary: contours samples retained text curves and normalizes the section; build/complete/verify construct and check the profile. Applicability: Uses extracted contour text rather than a DXF parser; fixed 40 mm normalization, 100 mm length, output paths, session wrapper and component checks.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-d340255b4d7f"></a>

## SRC-d340255b4d7f — SKF iteration — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-isometric.png`)

Summary: Actual inspected isometric image shows tapered housing,bore,two mounting feet/slots and fitting/screw details.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-d36213956fa8"></a>

## SRC-d36213956fa8 — build123d stable documentation

Original source: [https://build123d.readthedocs.io/en/stable/](https://build123d.readthedocs.io/en/stable/)

Summary: Official build123d documentation for a Python parametric B-rep modeling framework over Open CASCADE; used as an implementation reference, not runtime result.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-03-visual.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/cad-r04.md, research/workflows/details/cad-r05.md, research/workflows/details/cad-r06.md, research/workflows/details/cad-r07.md, research/workflows/details/cad-r08.md, research/workflows/details/cad-r09.md, research/workflows/details/cad-r10.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r09.md.

<a id="src-d3ede955b815"></a>

## SRC-d3ede955b815 — PointCloud API — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/python_api/open3d.geometry.PointCloud.html](https://www.open3d.org/docs/latest/python_api/open3d.geometry.PointCloud.html)

Summary: Open3D 0.20.0 API inspected 2026-11-12. Documents consistent tangent-plane normal orientation using a k-nearest-neighbour Riemannian graph and related normal orientation methods; consistency does not establish globally outward direction.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-d4dbbb69bd1c"></a>

## SRC-d4dbbb69bd1c — P01 p01-build-01 — rail-record-schema-0.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-record-schema-0.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-record-schema-0.json`)

Summary: p01-build-01 rail-record-schema-0.json: Retained native response with fields collection, collections, count, editing, next, next_offset, ok; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-d52309ad63a6"></a>

## SRC-d52309ad63a6 — combined-details.json

Original source: [${MODELING_ROOT}/research/workflows/details/combined-details.json](../workflows/details/combined-details.json)

Summary: Ten proposed combined workflow dossiers with source-backed operations, frame controls, tool/API entry points, resource conditions and relative classifications.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-d526125ac341"></a>

## SRC-d526125ac341 — Source check: intake operations

Original source: [${MODELING_ROOT}/research/action-audit/reviews/source-check.md](../action-audit/reviews/source-check.md)

Summary: Authored audit document recording Source check: intake operations. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-d5265b630533"></a>

## SRC-d5265b630533 — find-skills — skill discovery workflow

Original source: ${AGENT_SKILLS_ROOT}/find-skills/SKILL.md (`${AGENT_SKILLS_ROOT}/find-skills/SKILL.md`)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: find-skills — skill discovery workflow. Source class: local discovery skill instructions. Original reuse terms: Local instructions; referenced in place without duplication.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-d58501ecc5d1"></a>

## SRC-d58501ecc5d1 — feature-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/feature-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/feature-checks.json`)

Summary: 15passingchecks:300×200×152.5body/coververtexspansand12closededgepartnergraphs;sourcecounts/frameobservations.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d5c6dba4409f"></a>

## SRC-d5c6dba4409f — document-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/document-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/document-checkpoint.json`)

Summary: New isolated document86 binding,revision andrequest namespace before import.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-d5f6d3131aaa"></a>

## SRC-d5f6d3131aaa — Integrated Fibox drawing andvariant review

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/source-notes.md`)

Summary: Identifies203015Texactvariant,correctedrearbodydepthdatum,inneropeningassociation andsourcevsproductpageconditions.

Evidence: reviewed_source_interpretation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d64a3133bef1"></a>

## SRC-d64a3133bef1 — provenance.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/provenance.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/provenance.json`)

Summary: Exactoriginaltemporarydriverpaths,retainedhashesandcontrolprefixextraction;recordsoriginaldependencyconditions.

Evidence: execution_provenance_record.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d6bb83cc4fbe"></a>

## SRC-d6bb83cc4fbe — setup page

Original source: [https://projects.blender.org/lab/blender_mcp/wiki/Setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

Summary: The Blender-hosted Blender Lab MCP repository is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its setup page requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The Blender Lab MCP page search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's scripting security guidance says Python scripts can perform unrestricted operations.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md.

<a id="src-d6f3a12f4f78"></a>

## SRC-d6f3a12f4f78 — PRO-L ring to rim adapter (P14SL) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p14sl-pro-l-ring-to-rim-adapter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p14sl-pro-l-ring-to-rim-adapter.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; Sumitomo PRO-L; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-d74883941311"></a>

## SRC-d74883941311 — p01-source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-source-job.json`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-d7af850e4bd9"></a>

## SRC-d7af850e4bd9 — Independent review — Point 04 raster drawings and interpreted dimensions

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-04-independent.md](../action-audit/reviews/point-04-independent.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-d84e68b6a0ca"></a>

## SRC-d84e68b6a0ca — P01 p01-build-03 — reopened-checkpoint.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-checkpoint.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-03/reopened-checkpoint.json`)

Summary: p01-build-03 reopened-checkpoint.json: Binds partial/native stage to document 71, revision 0 and named part handles {'tube': '80'}; supports inspected recovery.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-d87cb7ce3b84"></a>

## SRC-d87cb7ce3b84 — views_c029.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/views_c029.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/views_c029.py`)

Summary: CapturedreopenedTOP/FRONTviewswithfitandmargincommands.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-d8bff2262475"></a>

## SRC-d8bff2262475 — XML Reference — MuJoCo Documentation

Original source: [https://mujoco.readthedocs.io/en/stable/XMLreference.html](https://mujoco.readthedocs.io/en/stable/XMLreference.html)

Summary: Stable XML reference accessed 2026-11-12; exact local release not checked. Documents MJCF angle default degrees versus URDF radians, compiler defaults, inertia fields/frames, mesh file types and inference modes, kinematic tree and equality constraints. `fullinertia` order is M11,M22,M33,M12,M13,M23 and is diagonalized by compilation. Compiler centers meshes and aligns principal axes; `mjModel.mesh_pos`, `mesh_quat` and `mesh_scale` preserve asset transforms to compose with geom pose.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-d928392d886f"></a>

## SRC-d928392d886f — build_workflow_details.py

Original source: [${MODELING_ROOT}/research/tools/build_workflow_details.py](../tools/build_workflow_details.py)

Summary: Documentation renderer validating recipe coverage, classification values and source references; builds workflow pages and independent sorted tables.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-d946b31f68ec"></a>

## SRC-d946b31f68ec — WISKA ESKV25 gland10066413 (C041) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c041-wiska-eskv25-gland10066413.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c041-wiska-eskv25-gland10066413.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Main cable entry candidate; original kind manufacturer source reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-d9490cdbdfa2"></a>

## SRC-d9490cdbdfa2 — https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1

Original source: [https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1)

Summary: - Hunyuan3D-2.1 repository and model usage: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-d9b54d7ca1b6"></a>

## SRC-d9b54d7ca1b6 — Leaf iteration — persistence.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/persistence.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/persistence.json`)

Summary: Current file SHA matches the earlier verified-save SHA. Opened native audit has eight solids and zero errors/warnings; original file bytes remain preserved.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-da01bd7cde5d"></a>

## SRC-da01bd7cde5d — imported-query.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-query.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-query.json`)

Summary: Actual native imported entity handle/type inventory.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-da6cb18472ad"></a>

## SRC-da6cb18472ad — P01 p01-build-01 — rail-doc-schema-2.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-doc-schema-2.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-doc-schema-2.json`)

Summary: p01-build-01 rail-doc-schema-2.json: Installed API response unknown_operation: Unknown operation; retained as a protocol/schema discovery failure for this rail build.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-da7e7e83673f"></a>

## SRC-da7e7e83673f — COLMAP command-line interface

Original source: [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)

Summary: COLMAP documents command-line reconstruction; reused as the SfM/camera and MVS alternative in these recipes.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/cad-sources.json, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/cad-r06.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md.

<a id="src-db5de105c935"></a>

## SRC-db5de105c935 — language reference

Original source: [https://files.openscad.org/documentation/manual/The_OpenSCAD_Language.html](https://files.openscad.org/documentation/manual/The_OpenSCAD_Language.html)

Summary: Primary sources: official documentation, language reference, source repository/licence. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-03-software.md, research/cad-and-skills.md.

<a id="src-db6151dedc21"></a>

## SRC-db6151dedc21 — ESKV25 WH original manufacturer datasheet

Original source: [https://www.wiska.com/en/pdf/10102748/ESKV-25.pdf](https://www.wiska.com/en/pdf/10102748/ESKV-25.pdf)

Summary: Original WH10102748 sheet supplies M25 thread,10mm length,29mm flats,32mm collar and38–47mm total length. Family diagram associates TL,L,D,SW/E;exactLG identity stays with its own page.

Evidence: downloaded_original.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-db98256a44dd"></a>

## SRC-db98256a44dd — Point 07 independent review — photographs, depth and learned reconstruction

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-07-independent.md](../action-audit/reviews/point-07-independent.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-dba1e4dff6ac"></a>

## SRC-dba1e4dff6ac — Original driver component mapping

Original source: ${TEMP_ROOT}/opencode/sumitomo-smartris-driver-ch52308-state.json (`${TEMP_ROOT}/opencode/sumitomo-smartris-driver-ch52308-state.json`)

Summary: Existing mapping identifies116 component handles and their construction names, used to bind actual native records and select the complete31-solid X2 group. An unchanged copy is retained in FERME.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-dbc7c88be85f"></a>

## SRC-dbc7c88be85f — test_cadtools.py

Original source: ${FERME_ROOT}/skills/cad-construction/tests/test_cadtools.py (`${FERME_ROOT}/skills/cad-construction/tests/test_cadtools.py`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-dc4ad193013b"></a>

## SRC-dc4ad193013b — SAM 3D Objects setup — main branch

Original source: [https://github.com/facebookresearch/sam-3d-objects/blob/main/doc/setup.md](https://github.com/facebookresearch/sam-3d-objects/blob/main/doc/setup.md)

Summary: Official mutable main setup page inspected 2026-11-12. States Linux 64-bit and NVIDIA GPU with at least 32 GB VRAM; notes some PyTorch3D components require GPU-enabled compilation. These are setup claims for the documented route, not local measurements.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-dcb27ebfc1f2"></a>

## SRC-dcb27ebfc1f2 — “3D Modeling with Claude Code: A Practical Blender Workflow”

Original source: [https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0](https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0)

Summary: The assigned UX Planet article, “3D Modeling with Claude Code: A Practical Blender Workflow”, was retrieved as a Medium HTML page on 12 November 2026. Its visible introduction says to use the language model as an agent controlling Blender through Blender MCP and shows a Claude Code → Blender MCP → Blender path. The article is member-only; the accessible page exposed the title, author, publication date, introductory claims and section headings, but not the detailed procedure, implementation code or full workflow. Retrieval outcome: partial page content accessible; full text inaccessible. The article is practitioner commentary, not a primary implementation source.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/user-supplied-links.md, research/workflows/details/dom-r05.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r09.md, research/workflows/domain-paths.md.

<a id="src-dcb41c3ce9ea"></a>

## SRC-dcb41c3ce9ea — Fibox ARCA203015 enclosure (C029) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c029-fibox-arca203015-enclosure.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c029-fibox-arca203015-enclosure.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; Control enclosure proposal; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-dcc824a0bc1a"></a>

## SRC-dcc824a0bc1a — BOSL2 repository

Original source: [https://github.com/BelfrySCAD/BOSL2](https://github.com/BelfrySCAD/BOSL2)

Summary: BOSL2 ; Parametric OpenSCAD shapes, masks and manipulators; OpenSCAD library catalog identifies BSD-2-Clause. Repository describes it as beta. BOSL2 repository ; BSD-2-Clause per official catalog; check repository license/version when vendoring. Parametric code is useful for generated primitives and fixtures, not a catalog of measured commercial hardware.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md.

<a id="src-dcd239b413da"></a>

## SRC-dcd239b413da — Pilz source provenance

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-01/source/acquisition.json`)

Summary: Original PDF retrieval time,MIME/hash,derived render metadata andactual blocked STEP access outcome.

Evidence: executed_acquisition_record.

Documents: research/sources/round-26/relay-sources.json.

<a id="src-dd1f5b2ca39f"></a>

## SRC-dd1f5b2ca39f — FreeCAD Draft DXF documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md)

Summary: Official FreeCAD docs list DXF entity support for C++ and legacy importers, format/version conditions, and note that 3D ACIS SAT blobs in DXF are not currently read by FreeCAD.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-dd1fcc78e97c"></a>

## SRC-dd1fcc78e97c — Independent DXF transform and context tests

Original source: [${MODELING_ROOT}/tests/test_dxf_inspect.py](../../tests/test_dxf_inspect.py)

Summary: Eight passing cases verify nested world-coordinate control, layer inheritance, model/paper contexts, preserved bulges and bytes, unitless records, cycles, array identities and bounded expansion.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-dd4c729f9ace"></a>

## SRC-dd4c729f9ace — Victron Orion48-12 converter (C043) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c043-victron-orion48-12-converter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c043-victron-orion48-12-converter.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; 44–51.2 V battery routes; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-ddbe71fda666"></a>

## SRC-ddbe71fda666 — workflow details

Original source: [${MODELING_ROOT}/research/workflows/details/workflow-details.json](../workflows/details/workflow-details.json)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-ddc04ee3002f"></a>

## SRC-ddc04ee3002f — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/glotoff/freecad-skills](https://api.github.com/repos/glotoff/freecad-skills)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-de3fef8057a3"></a>

## SRC-de3fef8057a3 — ME0907 actual native operation journal

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/ocs-journal.jsonl`)

Summary: Records isolated document creation, cylinders, pilot union, two blind-hole groups, end-thread/keyway cuts, save, same-identity reopen recovery and model captures.

Evidence: executed_native_operation_record.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-de7c1927c29d"></a>

## SRC-de7c1927c29d — Saved rail hash and native API bounds observation

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/native-audit.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/native-audit.json`)

Summary: Actual reopened document audit identifies the saved DWG and its SHA256, one-solid manifest and zero-error audit; reported bounds are zero. Native decoded features provide the independent nonzero bounds.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-dec8ef1082c6"></a>

## SRC-dec8ef1082c6 — Implemented drawing-inspection skill

Original source: [${MODELING_ROOT}/skills/drawing-inspection/SKILL.md](../../skills/cad-drawing-inspection/SKILL.md)

Summary: Documents the tested DXF command, dependency setup, coordinate matrix semantics, source-unit evidence, resource limits and agent handoff to mapped derivative selection.

Evidence: local_source_or_executed_inspection.

Documents: research/sources/round-18/dxf-inspection-sources.json.

<a id="src-df08a712232a"></a>

## SRC-df08a712232a — Driver iteration — native-query.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/native-query.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/native-query.json`)

Summary: Actual original query identifies116 solid entities and eight text labels, preserving all native handles.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-df6405fd9570"></a>

## SRC-df6405fd9570 — computational-engineering.md

Original source: ${CODEX_HOME}/skills/ocs-engineering/references/computational-engineering.md (`${CODEX_HOME}/skills/ocs-engineering/references/computational-engineering.md`)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-dfb07e5c3d9b"></a>

## SRC-dfb07e5c3d9b — Manufacturing Rules

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/manufacturing_rules.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/manufacturing_rules.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Manufacturing Rules. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-dfbf09c1f151"></a>

## SRC-dfbf09c1f151 — point-04-web-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-05/point-04-web-sources.json](round-05/point-04-web-sources.json)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-dfe4eca1f71a"></a>

## SRC-dfe4eca1f71a — imported-records-36.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-36.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/imported-records-36.json`)

Summary: imported native record snapshot: C3:Insert, C4:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-dfe7c160f462"></a>

## SRC-dfe7c160f462 — OCS model contract

Original source: ${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`)

Summary: Requirements for units, frames, source corrections, parts, tolerances and supplied numerical check observations.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-dfeba86ef6d2"></a>

## SRC-dfeba86ef6d2 — point-07-web-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-05/point-07-web-sources.json](round-05/point-07-web-sources.json)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-e0ea93a3ecb8"></a>

## SRC-e0ea93a3ecb8 — result.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/result.json`)

Summary: Completedmanufacturerassemblyiterationlinks44nativechecks,persistence,views,sourceconfigurationandappliedhelper.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-e11abaaead0b"></a>

## SRC-e11abaaead0b — Gland source-stage execution report

Original source: [${MODELING_ROOT}/execution/c041-cable-gland-source.md](../../execution/c041-cable-gland-source.md)

Summary: Documents exactvariant,dimensionedsourcefields,actualsourceinspection andnextdependentgeometryinputs.

Evidence: executed_work_report.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-e1ca3a166ec3"></a>

## SRC-e1ca3a166ec3 — Inspecting and checking saved CAD in Python

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/inspection-and-validation.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/inspection-and-validation.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Inspecting and checking saved CAD in Python. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-e24faff4c00b"></a>

## SRC-e24faff4c00b — Point 05 source check: calibration, scan alignment and coordinate frames

Original source: [${MODELING_ROOT}/research/action-audit/reviews/point-05-sources.md](../action-audit/reviews/point-05-sources.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-e2aad65f4cd1"></a>

## SRC-e2aad65f4cd1 — https://github.com/xy-gao/DA3-blender

Original source: [https://github.com/xy-gao/DA3-blender](https://github.com/xy-gao/DA3-blender)

Summary: - DA3 Blender add-on source (third-party): https://github.com/xy-gao/DA3-blender

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/workflows/details/rec-r05.md.

<a id="src-e304a1483122"></a>

## SRC-e304a1483122 — https://meshroom.readthedocs.io/en/latest/

Original source: [https://meshroom.readthedocs.io/en/latest/](https://meshroom.readthedocs.io/en/latest/)

Summary: - Meshroom install/automation docs: https://meshroom.readthedocs.io/en/latest/

Evidence: existing_report_registered.

Documents: research/reconstruction.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r06.md.

<a id="src-e3ba6f17358b"></a>

## SRC-e3ba6f17358b — Operation Inventory

Original source: [${MODELING_ROOT}/research/action-audit/operation-inventory.json](../action-audit/operation-inventory.json)

Summary: Authored audit document recording Operation Inventory. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json.

<a id="src-e3d853f6ef1d"></a>

## SRC-e3d853f6ef1d — views_c045.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/views_c045.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/executed-drivers/views_c045.py`)

Summary: Requested saved TOP/FRONT views;first TOP request hit polling bound andits repeated image wasretained.

Evidence: executed_driver_source.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-e3d95e78d033"></a>

## SRC-e3d95e78d033 — https://github.com/Tencent-Hunyuan/Hunyuan3D-2

Original source: [https://github.com/Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)

Summary: - Hunyuan3D-2 source and current community license: https://github.com/Tencent-Hunyuan/Hunyuan3D-2

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-e4073c405422"></a>

## SRC-e4073c405422 — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/ocs-journal.jsonl`)

Summary: Actual guarded import,CAS corrections,save/reopen,view/capture,recovery,activate andREGEN write/readback history.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-e4113edcaa23"></a>

## SRC-e4113edcaa23 — Existing bearing inspection and selective revision procedure

Original source: [${MODELING_ROOT}/skills/component-cad/references/existing-bearing.md](../../skills/cad-ocs-engineering/references/existing-bearing.md)

Summary: Defines source binding, transformed native checks, coplanar fragment cancellation, exact source-defined plane cuts, preserved nine-solid geometry, same-ID recovery and save/view completion.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-e556fe740218"></a>

## SRC-e556fe740218 — Anderson3-6054P2 boot (C060) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c060-anderson3-6054p2-boot.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c060-anderson3-6054p2-boot.md`)

Summary: Input sheet registered from the inspected ferme manifest: connectors; Charge-port accessory; original kind source accessory reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-e55c2ad4734f"></a>

## SRC-e55c2ad4734f — Observed implementation status overlay

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/implementation-status.json](../action-audit/implementation-queue/implementation-status.json)

Summary: Marks source intake as implemented with actual code, skill, test and execution paths while preserving the original planning queue.

Evidence: local_implementation_or_execution_record_inspected, local_source_or_executed_inspection.

Documents: research/sources/round-17/source-intake-sources.json, research/sources/round-18/dxf-inspection-sources.json.

<a id="src-e5981cd49734"></a>

## SRC-e5981cd49734 — PBR 4384 520 50T driven sprocket (C008) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c008-pbr-4384-520-50t-driven-sprocket.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c008-pbr-4384-520-50t-driven-sprocket.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907 chain example; original kind source component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-e5ab2b710c51"></a>

## SRC-e5ab2b710c51 — Integrated resistor package source notes

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/source-notes.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/source/source-notes.md`)

Summary: Retains applicable TA310PA dimensions and terminal/body association distinctions,with absolute original/render links. Coordinator removed unsupported PDF tolerance/no-scale attributions while preserving initial notes.

Evidence: reviewed_source_notes.

Documents: research/sources/round-20/component-sources.json.

<a id="src-e5af12a0873d"></a>

## SRC-e5af12a0873d — Research and proposed implementation

Original source: [${MODELING_ROOT}/research/README.md](../README.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-e601a94ea182"></a>

## SRC-e601a94ea182 — Reviewed SB50 acquisition metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/acquisition.json`)

Summary: Records original PDF URL/time/MIME/hash,distributor mapping,login-gated manufacturer CAD route andcorrected axial11.1 dimension association.

Evidence: reviewed_acquisition_record.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-e618fbde3a91"></a>

## SRC-e618fbde3a91 — https://fal.ai/models/fal-ai/sam-3/3d-objects/api

Original source: [https://fal.ai/models/fal-ai/sam-3/3d-objects/api](https://fal.ai/models/fal-ai/sam-3/3d-objects/api)

Summary: - Underlying SAM 3D model service https://fal.ai/models/fal-ai/sam-3/3d-objects/api — official Fal endpoint documentation opened. It requires an API key and sends an image URL or uploaded/base64 image to a hosted API; output schema includes Gaussian splat PLY, GLB mesh, metadata and optional per-object results. This is cloud inference, not a local reconstruction workflow. The endpoint advertises commercial use; that is Fal's service claim and does not by itself establish whether this endpoint uses the exact upstream Meta checkpoint or the terms governing output reuse. The API accepts optional pointmap/depth input, but this does not make output metrically validated.

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-e632f00983a2"></a>

## SRC-e632f00983a2 — reopened-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/reopened-isometric.png`)

Summary: Actual converter capture attempt reopened-isometric;image repeats the previous Fibox enclosure. Included as failed visual evidence,withhash comparison in capture-identity-checks.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-e635bf5bcf73"></a>

## SRC-e635bf5bcf73 — Live reopened rail native entity record

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/native-records.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/native-records.json`)

Summary: Current OCS document71 native record contains the unchanged saved SAB body; its bytes match the earlier saved record. This record supplies the actual feature observations for the successful repeat check.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-e6c61c3caf92"></a>

## SRC-e6c61c3caf92 — P02 crossmember — view-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/view-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/view-state.json`)

Summary: Actual OCS view state identifies reopened document73 and preserves unrelated original wheel document52 revision2.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-e70585fd1821"></a>

## SRC-e70585fd1821 — Leaf iteration — source-job.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c021-reuse-01/source-job.json`)

Summary: Pins 14 feature values with specific source sections, hashes, units, evidence labels and eight exact component names.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-e7211c15cdf1"></a>

## SRC-e7211c15cdf1 — P02 crossmember — reopened-checks.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-checks.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/reopened-checks.json`)

Summary: Six native SAB groups PASS: section/length, X/Y walls, ends, eight corner surfaces and a connected closed body.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-e74aa94bbb50"></a>

## SRC-e74aa94bbb50 — Procedure-design review notes — Point 01 model brief

Original source: [${MODELING_ROOT}/research/action-audit/reviews/designer-notes.md](../action-audit/reviews/designer-notes.md)

Summary: Authored audit document recording Procedure-design review notes — Point 01 model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-e796d575e829"></a>

## SRC-e796d575e829 — Software review: descriptions and dimensions to a model brief

Original source: [${MODELING_ROOT}/research/action-audit/reviews/software-review.md](../action-audit/reviews/software-review.md)

Summary: Authored audit document recording Software review: descriptions and dimensions to a model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-e7c712c212f9"></a>

## SRC-e7c712c212f9 — WISKA-ESKV-25-page-1.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page-1.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page-1.png`)

Summary: RenderedWH datasheet page1:material,thread,length,flats,collar,TLrange andpartidentity.

Evidence: derived_pdf_render.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-e7f1135e0337"></a>

## SRC-e7f1135e0337 — Albright SW200-281 contactor (C034) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c034-albright-sw200-281-contactor.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c034-albright-sw200-281-contactor.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; BT candidate; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-e86237284595"></a>

## SRC-e86237284595 — Victron battery dimension drawing revision02

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/LiFePO4-Battery-25.6V100Ah-NG.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/LiFePO4-Battery-25.6V100Ah-NG.pdf`)

Summary: Original companion drawing identifies both battery SKUs,341.2mm width,160.3mm depth,234.7/234.3mm height callouts and220mm terminal pitch; source values remain distinct from STEP vertex/placement observations.

Evidence: existing_downloaded_original_reused.

Documents: research/sources/round-20/component-sources.json.

<a id="src-e8734095736c"></a>

## SRC-e8734095736c — parts-and-standards-dictionary.md

Original source: ${FERME_ROOT}/skills/parts-and-standards-dictionary.md (`${FERME_ROOT}/skills/parts-and-standards-dictionary.md`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-e8c6f17f90e5"></a>

## SRC-e8c6f17f90e5 — RGBD integration — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)

Summary: Open3D 0.20.0 RGB-D tutorial inspected 2026-11-12. Describes UniformTSDFVolume and ScalableTSDFVolume, voxel length and SDF truncation examples; sample integrates with inverse(camera_poses[i].pose). Tutorial calls create_from_color_and_depth with depth_trunc 4.0; this example value differs from API defaults. No local integration was run.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/cad-r06.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r09.md.

<a id="src-e8fb08827bf0"></a>

## SRC-e8fb08827bf0 — FreeCAD source/licence

Original source: [https://github.com/FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)

Summary: Primary sources: FreeCAD source/licence, Sketcher Python scripting, Part scripting, Python scripting tutorial, Part Design concepts. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/next-step-proposal.md.

<a id="src-e8fb488a4b54"></a>

## SRC-e8fb488a4b54 — BT output to rim adapter (P14BT) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p14bt-bt-output-to-rim-adapter.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p14bt-bt-output-to-rim-adapter.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; BT; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-e9161d79c2fb"></a>

## SRC-e9161d79c2fb — component-procedure.md

Original source: [${MODELING_ROOT}/skills/component-cad/references/component-procedure.md](../../skills/cad-ocs-engineering/references/component-procedure.md)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: authored_document_or_code_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-e91ac441ccab"></a>

## SRC-e91ac441ccab — c029_presave_measurements.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/c029_presave_measurements.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/c029_presave_measurements.py`)

Summary: Traversedsource-correctednativeinstancesandretainedpresavepointgeometry.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-e935d3ebe64f"></a>

## SRC-e935d3ebe64f — FreeCAD Import Export Preferences documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md)

Summary: The FreeCAD documentation describes STEP import structure choices including assembly per document and object per document, options for link groups, instance names and compound expansion, and export settings for STEP length units and application protocol. It identifies AP203 as mechanical parts and assemblies and AP214 as automotive mechanical design. It states that single-object placement can be embedded in shape geometry on reimport. These are documented UI preferences; the archived documentation page does not prove a selected FreeCAD build, Python API behavior, or lossless unit and hierarchy transfer.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-sources.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-web-sources.json, research/workflows/details/dom-r02.md.

<a id="src-e941de7f22bc"></a>

## SRC-e941de7f22bc — Existing Leaf module saved native model

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/nissan-leaf-gen2-module-300x222x34.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/nissan-leaf-gen2-module-300x222x34.dwg`)

Summary: Original eight-solid reconstruction reused without changing its bytes. Current 29 source-bound native checks, file hash/audit and actual view inspection pass.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-ea12fb9678d8"></a>

## SRC-ea12fb9678d8 — COLMAP licence

Original source: [https://github.com/colmap/colmap/blob/main/doc/license.rst](https://github.com/colmap/colmap/blob/main/doc/license.rst)

Summary: Primary COLMAP BSD-3-Clause licence statement; third-party dependencies have separate licences.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

<a id="src-ea4fc60c7176"></a>

## SRC-ea4fc60c7176 — License text

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/LICENSE](https://raw.githubusercontent.com/glotoff/freecad-skills/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ea862cbd31ad"></a>

## SRC-ea862cbd31ad — OCS source exporter

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/src/io/step.rs](https://github.com/HakanSeven12/OpenCADStudio/blob/main/src/io/step.rs)

Summary: Evidence: local baseline, OCS source exporter.

Evidence: existing_report_registered.

Documents: research/next-step-proposal.md.

<a id="src-ea9c2cdf1768"></a>

## SRC-ea9c2cdf1768 — freecad-scripts — github/awesome-copilot

Original source: [https://www.skills.sh/github/awesome-copilot/freecad-scripts](https://www.skills.sh/github/awesome-copilot/freecad-scripts)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: freecad-scripts — github/awesome-copilot. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-eb24664fc3c0"></a>

## SRC-eb24664fc3c0 — TripoSR inference entry point

Original source: [https://github.com/VAST-AI-Research/TripoSR/blob/main/run.py](https://github.com/VAST-AI-Research/TripoSR/blob/main/run.py)

Summary: Actual source implements preprocessing, single-image inference, mesh extraction and OBJ/GLB export; chunk size trades memory for runtime.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-visual.md, research/sources/round-03/domain-detail-sources.json.

<a id="src-eb5bcb4295ce"></a>

## SRC-eb5bcb4295ce — Kelly archive predecessor motor outline

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/kelly-archive/bldcmotor.pdf (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/exterior-source-review/kelly-archive/bldcmotor.pdf`)

Summary: Original archive member for ME0201013001, drawing0JWT.300.117. Delegated review identifies it as related visual evidence under Motenergy direct-replacement claim; it supplies its own title and is kept separate from exact ME0907 dimensions.

Evidence: extracted_original_archive_member.

Documents: research/sources/round-19/me0907-sources.json.

<a id="src-eb82077bb446"></a>

## SRC-eb82077bb446 — Reviewed Orion acquisition metadata

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/acquisition.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/acquisition.json`)

Summary: Original PDF/STEP/manual URLs,times,MIME,hashes andactual price-list access outcomes;retained-manual attribution corrected with initial copy preserved.

Evidence: reviewed_acquisition_record.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-eb880f7efbac"></a>

## SRC-eb880f7efbac — ${CODEX_HOME}/skills/ocs-engineering/references/ocs-control.md

Original source: ${CODEX_HOME}/skills/ocs-engineering/references/ocs-control.md (`${CODEX_HOME}/skills/ocs-engineering/references/ocs-control.md`)

Summary: Source referenced for the stated workflow; see the owning documentation or research item.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-ebd6e769a79a"></a>

## SRC-ebd6e769a79a — `freecad-user/SKILL.md`

Original source: [https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-user/SKILL.md](https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-user/SKILL.md)

Summary: FreeCAD skills suite (`glotoff/freecad-skills`) ; Archived `freecad-user/SKILL.md` routes UI/modeling/workbench/import-export and topological naming guidance; `freecad-power-user/SKILL.md` covers Python, Part/Sketcher/Draft, B-rep, FeaturePython and headless/RPC automation; `freecad-developer/SKILL.md` covers C++ build/workbench development. README says skills derive from official FreeCAD documentation. Root skill suite licence is MIT; copied FreeCAD docs have separate attribution/licensing. ; Adapt `freecad-user` and `freecad-power-user` selectively as a complementary parametric backend; `developer` is outside normal modeling scope. The supplied suite is knowledge guidance, not tested evidence that generated files meet requirements. Source links: `freecad-user/SKILL.md`, `freecad-power-user/SKILL.md`, `freecad-developer/SKILL.md`. Archived local files were inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-ebe044688086"></a>

## SRC-ebe044688086 — Driver iteration — retained-source/original-part-map.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/retained-source/original-part-map.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/retained-source/original-part-map.json`)

Summary: Unchanged retained copy of the original116-part handle map, enabling source-to-native identity review and bounded X2 group selection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-ebf77b364ed5"></a>

## SRC-ebf77b364ed5 — OpenCV image processing feature detection

Original source: [https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html)

Summary: Official API documents probabilistic HoughLinesP on binary images and returns line-segment endpoint coordinates in pixel space.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r08.md.

<a id="src-ecc97be7318c"></a>

## SRC-ecc97be7318c — point-06-web-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-05/point-06-web-sources.json](round-05/point-06-web-sources.json)

Summary: Existing local source cited by point 06 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-ecdea17f6078"></a>

## SRC-ecdea17f6078 — WISKA-ESKV-25-page-2.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page-2.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c041-build-01/source/WISKA-ESKV-25-page-2.png`)

Summary: RenderedWH datasheet page2:accessoryordercodes andprinteddate.

Evidence: derived_pdf_render.

Documents: research/sources/round-22/gland-sources.json.

<a id="src-ece5f904e49d"></a>

## SRC-ece5f904e49d — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/glotoff/freecad-skills/git/trees/HEAD?recursive=1](https://api.github.com/repos/glotoff/freecad-skills/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ed02d8942690"></a>

## SRC-ed02d8942690 — SKF iteration — initial-open-state.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/initial-open-state.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/initial-open-state.json`)

Summary: Native original-open state identifies document74, original SKF source path and unrelated open work, including preserved dirty wheel document52.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-ed09b653131a"></a>

## SRC-ed09b653131a — openscad — mitsuhiko/agent-stuff

Original source: [https://www.skills.sh/mitsuhiko/agent-stuff/openscad](https://www.skills.sh/mitsuhiko/agent-stuff/openscad)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: openscad — mitsuhiko/agent-stuff. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ed1c06986d4c"></a>

## SRC-ed1c06986d4c — Stop-button feature contract

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source-job.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/source-job.json`)

Summary: Pins finished panel-interface bounds andindividual required operator/contact body geometry questions.

Evidence: implementation_input_artifact.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-ede1a41b29c4"></a>

## SRC-ede1a41b29c4 — Caster head mounting plate (P06B) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p06b-caster-head-mounting-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p06b-caster-head-mounting-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: caster; Chosen caster reference; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-ede9c64cd596"></a>

## SRC-ede9c64cd596 — rec-r09.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r09.md](../workflows/details/rec-r09.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-edf75a7ba1f0"></a>

## SRC-edf75a7ba1f0 — placement-corrections.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/placement-corrections.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/placement-corrections.json`)

Summary: Actual checked helper application:27 matrices corrected,nine ACIS definitions unchanged.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-ee88cef821b6"></a>

## SRC-ee88cef821b6 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/earthtojake/text-to-cad](https://api.github.com/repos/earthtojake/text-to-cad)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-eeafae2a7d94"></a>

## SRC-eeafae2a7d94 — Mersen FTFH fuse holder (C031) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c031-mersen-ftfh-fuse-holder.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c031-mersen-ftfh-fuse-holder.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; CNL fuse alternative; original kind component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-eedbcb57b436"></a>

## SRC-eedbcb57b436 — Complete component input coverage

Original source: [${MODELING_ROOT}/research/component-development-coverage.md](../component-development-coverage.md)

Summary: Plan-side source coverage and ownership reference linking to the authoritative FERME 103-part data; group counts and proposed first two jobs are explicit.

Evidence: authored_document_inspected.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-ef7f25d50b37"></a>

## SRC-ef7f25d50b37 — item-profile-02633-segment-100mm.md — recorded_execution_report

Original source: ${FERME_ROOT}/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md (`${FERME_ROOT}/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md`)

Summary: Component-specific native checks, save/reopen observations and source paths for OCS 2026.42. Applicability:

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-ef86743da4af"></a>

## SRC-ef86743da4af — Read-only source/native placement and assembly helpers

Original source: [${MODELING_ROOT}/scripts/step_placements.py](../../scripts/step_placements.py)

Summary: Exercised AP214 frame reader detects unique inverse matches,round-trips proposed native fields and traverses bounded single-insert unit-scale zero-base block trees. Includes identity-SAT point reader used for pre-save comparison.

Evidence: implementation_artifact.

Documents: research/sources/round-20/component-sources.json.

<a id="src-f052fe7cc9cb"></a>

## SRC-f052fe7cc9cb — Resistor current component state

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c035-build-01/result.json`)

Summary: Records exact input requirement and source review; CAD construction is dependent on the named substrate/terminal geometry evidence.

Evidence: executed_component_stage_record.

Documents: research/sources/round-20/component-sources.json.

<a id="src-f06b7c033d40"></a>

## SRC-f06b7c033d40 — 8121020_FIBOX ARCA IEC 203015T

Original source: [https://9349002.fs1.hubspotusercontent-na1.net/hubfs/9349002/assets/8121020_FIBOX%20ARCA%20IEC%20203015T.step](https://9349002.fs1.hubspotusercontent-na1.net/hubfs/9349002/assets/8121020_FIBOX%20ARCA%20IEC%20203015T.step)

Summary: ExactmanufacturerSTEP8121020 with12soliddefinitions;retainsbase,cover,hinges,lock,plate,feet andsourceconfiguration.

Evidence: downloaded_original.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-f06d3b316cfc"></a>

## SRC-f06d3b316cfc — rec-r04.md

Original source: [${MODELING_ROOT}/research/workflows/details/rec-r04.md](../workflows/details/rec-r04.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-f088ec7f4848"></a>

## SRC-f088ec7f4848 — MuJoCo Menagerie README

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md)

Summary: The repository catalogue associates each listed robot model with a license. Its terms section says XML and asset files in individual model directories can have different terms and directs users to the LICENSE file in the specific model subdirectory; remaining repository content is Apache-2.0. This supports per-model/per-asset license lookup before reuse. The repository says it is not an officially supported Google product.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-sources.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-f08b8003c0e4"></a>

## SRC-f08b8003c0e4 — TriangleMesh API — Open3D 0.20.0 documentation

Original source: [https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html](https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html)

Summary: Open3D 0.20.0 API inspected 2026-11-12. Documents Poisson reconstruction from a point cloud (mesh plus density values), ball pivoting from oriented PointCloud and quadric decimation targeting triangle count with maximum-error/boundary-weight parameters.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/dom-r06.md, research/workflows/details/dom-r08.md.

<a id="src-f0d4b933a88b"></a>

## SRC-f0d4b933a88b — Leaf source attribution and reconstruction geometry record

Original source: ${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/leaf-gen2-geometry.md (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/leaf-gen2-geometry.md`)

Summary: Separates EVShop case dimensions, VT-Tech mounting holes and nominal terminal sizes, Jay Summet reuse pitch, and reconstructed shell/pan/terminal features. Supplies pinned feature expectations.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-15/leaf-sources.json.

<a id="src-f1c693b775e0"></a>

## SRC-f1c693b775e0 — `skills/freecad-ai/SKILL.md`

Original source: [https://github.com/reyk/freecad-ai-skill/blob/main/skills/freecad-ai/SKILL.md](https://github.com/reyk/freecad-ai-skill/blob/main/skills/freecad-ai/SKILL.md)

Summary: FreeCAD AI (`reyk/freecad-ai-skill`) ; Archived `freecad-ai/SKILL.md` requires a running GUI, load `freecad-server.py` in its Python console, then call `freecad-client.py`; examples execute Python in the live process and recommend small changes, recompute and inspect. No hosted AI service is required by the bridge itself. Archived `LICENSE` grants ISC-style permissive terms. ; Use only after reviewing the bridge code and with scope-appropriate process isolation. It executes caller-supplied Python inside the live CAD process. Skill link: `skills/freecad-ai/SKILL.md`. Archived local source was inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-f1c875f602ad"></a>

## SRC-f1c875f602ad — CAD Modeling Skill

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/README.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: CAD Modeling Skill. Source class: repository README. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-f1ece207e03f"></a>

## SRC-f1ece207e03f — Completed P01 component iteration result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-verify-04/result.json`)

Summary: P01 state DONE links saved native geometry, passed binary feature checks, original views, applied reader improvement and32 passing tests; records decoded bounds and contradictory API bounds.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-f21f3a511691"></a>

## SRC-f21f3a511691 — prior-model-hashes.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/prior-model-hashes.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/prior-model-hashes.json`)

Summary: Pre-buildhashesof23existingsavedDWGsforbytepreservationcomparison.

Evidence: executed_native_observation.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-f22443c65bee"></a>

## SRC-f22443c65bee — Source-first tube construction and recovery procedure

Original source: [${MODELING_ROOT}/skills/component-cad/references/source-first-and-tube.md](../../skills/cad-ocs-engineering/references/source-first-and-tube.md)

Summary: Numbered source preparation, installed schema/selection interpretation, exact rounded-profile construction, bounded-area extrusion, native checks, save/reopen and content inspection steps. Records refused Boolean routes, same-ID capture recovery and the reopened SAB-reader/bounds issues.

Evidence: authored_code_or_procedure_inspected, local_execution_evidence_inspected, local_execution_source_inspected.

Documents: research/sources/round-11/rail-execution-sources.json, research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-13/crossmember-sources.json.

<a id="src-f278cbf89b6d"></a>

## SRC-f278cbf89b6d — Victron NG25.6V100Ah battery (C023) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c023-victron-ng25-6v100ah-battery.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c023-victron-ng25-6v100ah-battery.md`)

Summary: Input sheet registered from the inspected ferme manifest: battery; Victron pair or single BT-V; original kind manufacturer case reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-f279f6325539"></a>

## SRC-f279f6325539 — SKF iteration — reopened-top.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-top.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-top.png`)

Summary: Actual inspected top image shows two closed mounting slots, axial housing draft and bearing/fitting projection.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-f2c662a213ab"></a>

## SRC-f2c662a213ab — GitHub Copilot FreeCAD scripting skill

Original source: [https://github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)

Summary: GitHub Copilot FreeCAD scripting skill ; FreeCAD Python documents, Part/Sketcher geometry and recompute ; Reuse as an API reference, with pinned-version geometry fixtures. Archived exact skill is available in the existing CAD research.

Evidence: existing_report_registered.

Documents: skills/README.md.

<a id="src-f2c7a1c3b5b3"></a>

## SRC-f2c7a1c3b5b3 — ifcopenshell.geom — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/geom/index.html)

Summary: IfcOpenShell 0.9.0post1 API reference accessed 2026-11-12. Inspected as the registered geometry API reference; detailed documented return forms/settings used here are from the geometry-processing page in this same version.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-f2cbfd7c15e2"></a>

## SRC-f2cbfd7c15e2 — Hitch support gusset (P07G) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p07g-hitch-support-gusset.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p07g-hitch-support-gusset.md`)

Summary: Input sheet registered from the inspected ferme manifest: hitch; Trailer ball-coupling proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-f31b446de956"></a>

## SRC-f31b446de956 — Blue Sea5026 auxiliary fuse block (C042) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c042-blue-sea5026-auxiliary-fuse-block.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c042-blue-sea5026-auxiliary-fuse-block.md`)

Summary: Input sheet registered from the inspected ferme manifest: electrical; 12 or24 V branch distribution; original kind manufacturer component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-f343e0d088b6"></a>

## SRC-f343e0d088b6 — corrected-records-6.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-6.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-records-6.json`)

Summary: corrected native record snapshot: 99:Solid3D, 9D:Solid3D, A1:Solid3D, A5:Solid3D, A9:Insert, AA:Insert. Preserves exact fields/ACIS for source-frame andsaved geometry comparisons.

Evidence: executed_native_record_read.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-f3798f920e4f"></a>

## SRC-f3798f920e4f — Driven sprocket axle carrier (P12B) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p12b-driven-sprocket-axle-carrier.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p12b-driven-sprocket-axle-carrier.md`)

Summary: Input sheet registered from the inspected ferme manifest: drive; ME0907; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-f3ceeaee0041"></a>

## SRC-f3ceeaee0041 — supplier-hosted standard PDF

Original source: [https://www.botopsteelpipes.com/wp-content/uploads/2024/08/EN-10219-2-2019.pdf](https://www.botopsteelpipes.com/wp-content/uploads/2024/08/EN-10219-2-2019.pdf)

Summary: For a 40 × 40 × 3 mm cold-formed welded structural hollow section using the EN 10219-2:2019 corner and property conventions, the standard distinguishes two corner values. The applicable delivery-condition requirements belong to the corresponding Part 1; the corner evidence below combines the readable EN 10219-2:2019 sample for Clause 6.2 and Table 3 with the indexed Annex A.3 excerpt of the supplier-hosted standard PDF for the calculation radii:

Evidence: existing_report_registered, search_excerpt_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-f428be8d9008"></a>

## SRC-f428be8d9008 — readiness.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/readiness.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/readiness.json`)

Summary: Existing source/hash gate SOURCE_READY result before native construction.

Evidence: executed_native_observation.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-f47d7610aaad"></a>

## SRC-f47d7610aaad — Placementhelpertests

Original source: [${MODELING_ROOT}/tests/test_assembly_repair.py](../../tests/test_assembly_repair.py)

Summary: Sixexecutedcasescoverrepeatedsuccess,staleinputs,tamperedfields,duplicatehandles,readbackfailureandchangedsoliddefinition.

Evidence: executed_software_tests.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-f4b8da3b384e"></a>

## SRC-f4b8da3b384e — runtime.py

Original source: ${FERME_ROOT}/skills/cad-construction/scripts/cadtools/runtime.py (`${FERME_ROOT}/skills/cad-construction/scripts/cadtools/runtime.py`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected, local_execution_evidence_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-11/rail-execution-sources.json.

<a id="src-f4c2cf5fb241"></a>

## SRC-f4c2cf5fb241 — Orion-Tr Smart DC-DC Charger Isolated

Original source: [https://www.victronenergy.com/upload/documents/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/34439-Orion-Tr_Smart_DC-DC_Charger-pdf-en.pdf](https://www.victronenergy.com/upload/documents/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/34439-Orion-Tr_Smart_DC-DC_Charger-pdf-en.pdf)

Summary: Retained manual page29 names48/12-20;higher-power table includes24/12-30 and130×186×80 nominal envelope. Coordinator separates this from the delegated48/12-30 price-list observation.

Evidence: downloaded_original.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-f4e7d302c752"></a>

## SRC-f4e7d302c752 — TripoSR — official repository, main branch

Original source: [https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR)

Summary: Official mutable main README inspected 2026-11-12. Shows `python run.py examples/chair.png --output-dir output/`; default single-image route states about 6 GB VRAM, with optional texture baking. Code/checkpoint terms are separately registered; no inference was run.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/dom-r06.md, research/workflows/details/rec-r10.md.

<a id="src-f51b1cc13707"></a>

## SRC-f51b1cc13707 — MCP repository

Original source: [https://projects.blender.org/lab/blender_mcp/src/branch/main](https://projects.blender.org/lab/blender_mcp/src/branch/main)

Summary: The Blender-hosted Blender Lab MCP repository is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its setup page requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The Blender Lab MCP page search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's scripting security guidance says Python scripts can perform unrestricted operations.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r05.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r09.md, research/workflows/domain-paths.md.

<a id="src-f5689f245f38"></a>

## SRC-f5689f245f38 — assets

Original source: [${MODELING_ROOT}/research/action-audit/implementation-queue/assets.json](../action-audit/implementation-queue/assets.json)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-f5ab2b9f1eb3"></a>

## SRC-f5ab2b9f1eb3 — SKF iteration — reopened-front.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-front.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/reopened-front.png`)

Summary: Actual inspected front image shows shaft bore, housing outer silhouette, fitting and locking components of the saved derivative.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-f5b26686d5af"></a>

## SRC-f5b26686d5af — Cargo.toml

Original source: ${OCS_ROOT}/Cargo.toml (`${OCS_ROOT}/Cargo.toml`)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-f5d6cbd7ce2c"></a>

## SRC-f5d6cbd7ce2c — P01 p01-build-01 — rail-type-LwPolyline.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-type-LwPolyline.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p01-build-01/rail-type-LwPolyline.json`)

Summary: p01-build-01 rail-type-LwPolyline.json: Retained native response with fields collection, definitions, editing, fields, notes, ok, record_type; links this installed API/schema or geometry observation to the corresponding P01 attempt.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-f5feb81d0023"></a>

## SRC-f5feb81d0023 — Residential Floor Plan Recognition and Reconstruction

Original source: [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html)

Summary: CVPR 2021 paper proposes residential floor-plan recognition/reconstruction, including segmentation and vectorization; paper reports tests on floor-plan imagery and method-specific results.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r08.md.

<a id="src-f6203f32e04a"></a>

## SRC-f6203f32e04a — license

Original source: [https://www.blender.org/about/license/](https://www.blender.org/about/license/)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-07-visual.md, research/domains-and-components.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json.

<a id="src-f6b02162a39c"></a>

## SRC-f6b02162a39c — Bonsai docs

Original source: [https://docs.ifcopenshell.org/bonsai.html](https://docs.ifcopenshell.org/bonsai.html)

Summary: Bonsai / IfcOpenShell ; Bonsai is a native IFC authoring and analysis platform integrated with Blender. IfcOpenShell provides C++/Python APIs, conversion, IDS validation, querying, clash and geometry tools. The documented conversion tool is IfcConvert. Bonsai docs, IfcOpenShell introduction ; IfcOpenShell libraries/tooling: LGPL-3.0-or-later; Bonsai: GPL-3.0-or-later, per project documentation. IFC is an open building data schema; the authoring application remains separately licensed. ; Building authoring and IFC import/export adapter. Use IFC entity relationships and property sets as semantic BIM data; do not flatten the only copy into meshes. Use IDS as machine-readable delivery checks.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-f745b3b2abdf"></a>

## SRC-f745b3b2abdf — Agent skill: freecad-user

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/SKILL.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-user. Source class: agent skill instructions. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-f77e765324d1"></a>

## SRC-f77e765324d1 — geometry.py

Original source: ${FERME_ROOT}/skills/cad-construction/scripts/cadtools/geometry.py (`${FERME_ROOT}/skills/cad-construction/scripts/cadtools/geometry.py`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected, local_execution_evidence_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-11/rail-execution-sources.json.

<a id="src-f77f55667d7d"></a>

## SRC-f77f55667d7d — domain-sources.json

Original source: [${MODELING_ROOT}/research/sources/round-02/domain-sources.json](round-02/domain-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-f7e7cce18547"></a>

## SRC-f7e7cce18547 — Blender Object API RNA source (main branch)

Original source: [https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_object_api.cc](https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_object_api.cc)

Summary: Official Blender RNA source defines Object.ray_cast with object-space origin/direction, maximum distance and optional depsgraph for evaluated mesh access. It returns hit boolean, location, normal and face index. This query is against evaluated object geometry in object-space, not a physical measurement; the mutable main-branch source does not pin an installed release.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-f80023f6c2fa"></a>

## SRC-f80023f6c2fa — corrected-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/corrected-isometric.png`)

Summary: Actual converter capture attempt corrected-isometric;image repeats the previous Fibox enclosure. Included as failed visual evidence,withhash comparison in capture-identity-checks.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-f828b291cc6f"></a>

## SRC-f828b291cc6f — OpenCADStudio MCP automation guide

Original source: ${OCS_ROOT}/docs/automation/README.md (`${OCS_ROOT}/docs/automation/README.md`)

Summary: Local OCS guide describes stdio MCP and drawing inspection, mutation, measurements, audits and verified save. It supports application-level drawing workflow claims.

Evidence: local_source_inspected, local_reference_registered, inspected_local_source.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-24/converter-sources.json.

<a id="src-f828ba9d8d3b"></a>

## SRC-f828ba9d8d3b — EN 10219-2:2019 (E), SIST sample — Cold formed welded structural hollow sections, Part 2

Original source: [https://cdn.standards.iteh.ai/samples/38063/99682514fcf94faabd079f41b1a7854e/SIST-EN-10219-2-2019.pdf](https://cdn.standards.iteh.ai/samples/38063/99682514fcf94faabd079f41b1a7854e/SIST-EN-10219-2-2019.pdf)

Summary: Readable EN 10219-2:2019 sample output exposed Clause 6.2 (rounded internal corners, internal profile unspecified), Table 3 (external corner profile 1.6T–2.4T for T≤6 mm) and Clause 7.7 (radius gauge or corner-offset measurement). At nominal T=3 mm the external interval calculates to 4.8–7.2 mm. The Annex A.3 nominal radii are attributed separately to the indexed supplier-hosted standard excerpt.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-10/tube-corner-sources.json, research/tube-corner-research.md.

<a id="src-f85e4e244a2b"></a>

## SRC-f85e4e244a2b — Browser source-image route outcome

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/followup-browser-route.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c030-build-01/source/followup-browser-route.md`)

Summary: CUA inventory had no browser/app surface,so this exact-PDF route produced no raster or source bytes. Earlier source evidence remains preserved.

Evidence: executed_tool_availability_record.

Documents: research/sources/round-21/fuse-sources.json.

<a id="src-f87051bef24f"></a>

## SRC-f87051bef24f — catalogue.py

Original source: ${FERME_ROOT}/skills/cad-construction/scripts/cadtools/catalogue.py (`${FERME_ROOT}/skills/cad-construction/scripts/cadtools/catalogue.py`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected.

Documents: research/sources/round-09/component-execution-sources.json.

<a id="src-f945f7d18313"></a>

## SRC-f945f7d18313 — action-occurrences.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/action-occurrences.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/action-occurrences.jsonl`)

Summary: Component-led execution source: actual reusable implementation, source-readiness/action job record, tests, skill guidance or retained FERME source. Evidence stage and observed results are detailed in execution/2026-11-12-component-led.md.

Evidence: local_source_inspected, local_execution_evidence_inspected, local_execution_source_inspected, local_source_or_execution_record_inspected.

Documents: research/sources/round-09/component-execution-sources.json, research/sources/round-11/rail-execution-sources.json, research/sources/round-12/saved-rail-reader-sources.json, research/sources/round-13/crossmember-sources.json, research/sources/round-14/bearing-sources.json, research/sources/round-15/leaf-sources.json, research/sources/round-16/driver-sources.json.

<a id="src-f954ab80c148"></a>

## SRC-f954ab80c148 — Agent skill: cad

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/SKILL.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: cad. Source class: agent skill instructions. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-f9d2b64c1fb2"></a>

## SRC-f9d2b64c1fb2 — SKF iteration — header.json

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/header.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/header.json`)

Summary: Actual original OCS document header identifies millimetre units for source-linked geometric coordinate checks.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-14/bearing-sources.json.

<a id="src-f9d4243f4cec"></a>

## SRC-f9d4243f4cec — Category1 upper linkage pin (C064) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/c064-category1-upper-linkage-pin.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/c064-category1-upper-linkage-pin.md`)

Summary: Input sheet registered from the inspected ferme manifest: attachments; Reference attachment interface; original kind source component reference. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-f9e1dbc024e2"></a>

## SRC-f9e1dbc024e2 — dom-r02.md

Original source: [${MODELING_ROOT}/research/workflows/details/dom-r02.md](../workflows/details/dom-r02.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-fa8c58e8c7a1"></a>

## SRC-fa8c58e8c7a1 — Open3D licence

Original source: [https://github.com/isl-org/Open3D/blob/main/LICENSE](https://github.com/isl-org/Open3D/blob/main/LICENSE)

Summary: Primary source gives Open3D MIT licence; third-party dependencies remain separately governed.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

<a id="src-fabfe00e465d"></a>

## SRC-fabfe00e465d — ezdxf ACIS header interpretation

Original source: ${NATIVE_READER_ROOT}/ezdxf/acis/hdr.py (`${NATIVE_READER_ROOT}/ezdxf/acis/hdr.py`)

Summary: Existing AcisHeader exposes units_in_mm and version fields. The P01 reader reports decoded metadata10.0 beside OCS document millimetres and preserves native coordinates; the same value occurs before saving.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-12/saved-rail-reader-sources.json.

<a id="src-fae815d28e80"></a>

## SRC-fae815d28e80 — Rear attachment support plate (P09) — CAD input sheet

Original source: ${FERME_ROOT}/engineering/module-development/cad-inputs/p09-rear-attachment-support-plate.md (`${FERME_ROOT}/engineering/module-development/cad-inputs/p09-rear-attachment-support-plate.md`)

Summary: Input sheet registered from the inspected ferme manifest: attachments; Rear ISO730 reference proposal; original kind custom proposal. Detailed geometry review belongs to its component iteration.

Evidence: existing_report_registered.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-fb567caa0d5c"></a>

## SRC-fb567caa0d5c — Battery inverse-placement diagnosis and plan

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source-placement-plan.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source-placement-plan.json`)

Summary: All13 nonidentity native inserts uniquely match inverse source STEP frames. Plan records original and expected matrices,source entity IDs and proposed object-coordinate native fields.

Evidence: executed_source_placement_inspection.

Documents: research/sources/round-20/component-sources.json.

<a id="src-fb5d6f6a65cc"></a>

## SRC-fb5d6f6a65cc — read_c029.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/read_c029.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/read_c029.py`)

Summary: Retainedimportedaudit,blocks,entitiesandactualprecorrectionview;capturepollboundlaterrecovered.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-fbf7ed489d76"></a>

## SRC-fbf7ed489d76 — https://arxiv.org/abs/2403.02151

Original source: [https://arxiv.org/abs/2403.02151](https://arxiv.org/abs/2403.02151)

Summary: - TripoSR research paper: https://arxiv.org/abs/2403.02151

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-fc97ce67556a"></a>

## SRC-fc97ce67556a — P02 crossmember — ocs-journal.jsonl

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/ocs-journal.jsonl (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/p02-build-01/ocs-journal.jsonl`)

Summary: Append-only native request journal records isolated document creation, exact rounded profiles, bounded-area extrusion, temporary-profile cleanup, metadata, save and reopen with stable identities.

Evidence: local_execution_source_inspected.

Documents: research/sources/round-13/crossmember-sources.json.

<a id="src-fcb5653f90bc"></a>

## SRC-fcb5653f90bc — regen-isometric.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/regen-isometric.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/regen-isometric.png`)

Summary: Actual converter capture attempt regen-isometric;image repeats the previous Fibox enclosure. Included as failed visual evidence,withhash comparison in capture-identity-checks.

Evidence: executed_visual_failure.

Documents: research/sources/round-24/converter-sources.json.

<a id="src-fcdc74aed22e"></a>

## SRC-fcdc74aed22e — FreeCAD Sketcher scripting documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)

Summary: The FreeCAD scripting page shows `Sketcher::SketchObject`, `addGeometry`, `addConstraint` with a Coincident constraint, and `doc.recompute()`. The example adds three line segments and one coincidence relation; it demonstrates API construction, not a closed or fully constrained profile or solver-status check. The page is in the FreeCAD documentation repository, which GitHub reports was archived on 2026-04-01.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/visual-review.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/cad-r05.md, research/workflows/details/cad-r09.md, research/workflows/details/mix-r02.md.

<a id="src-fcf66e735eb6"></a>

## SRC-fcf66e735eb6 — plan_c029.py

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/plan_c029.py (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/executed-drivers/plan_c029.py`)

Summary: Read17STEPframesandgenerated16uniqueinverse-placementchangesagainstactualnativeinserts.

Evidence: executed_driver_source.

Documents: research/sources/round-23/enclosure-sources.json.

<a id="src-fcfc3aa6479a"></a>

## SRC-fcfc3aa6479a — SB50 leader andchain review

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/coordinator-review.md (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c038-build-01/source/coordinator-review.md`)

Summary: Actual source-image review corrects11.1 axial segment andcalculates48mm housing length fromdimension chain.

Evidence: executed_coordinator_review.

Documents: research/sources/round-25/connector-sources.json.

<a id="src-fe0ed186d8d8"></a>

## SRC-fe0ed186d8d8 — Main frame longitudinal rail nominal reference DWG

Original source: ${FERME_ROOT}/engineering/module-development/cad/parts/p01-main-frame-longitudinal-rail-reference.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/p01-main-frame-longitudinal-rail-reference.dwg`)

Summary: Saved native DWG2018 contains one source-labelled P01 hollow rail with proposed40x40x3mm section,600mm length and EN10219 nominal6/3mm corner radii. Pre-save feature checks pass; save/hash/manifest and reopened views pass; detailed reopened SAB feature checks have UNKNOWN status.

Evidence: local_execution_evidence_inspected.

Documents: research/sources/round-11/rail-execution-sources.json.

<a id="src-fe66e203f22d"></a>

## SRC-fe66e203f22d — IfcOpenShell geometry API index

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/index.html)

Summary: Lists IFC geometry creation helpers including profiles, meshes, doors and representation assignment.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r07.md, research/workflows/domain-paths.md.

<a id="src-fe69883eeede"></a>

## SRC-fe69883eeede — License text

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/LICENSE](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-fe7b635af96d"></a>

## SRC-fe7b635af96d — Stop-button source-stage result

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c049-build-01/result.json`)

Summary: Connects exactvariant,source-defined panel interface,unresolved full body features andseparate nominal/projection labels.

Evidence: executed_component_stage_record.

Documents: research/sources/round-27/stop-button-sources.json.

<a id="src-fe876787e9e0"></a>

## SRC-fe876787e9e0 — Component-led CAD and tooling development plan

Original source: [${MODELING_ROOT}/COMPONENT_DEVELOPMENT_PLAN.md](../../COMPONENT_DEVELOPMENT_PLAN.md)

Summary: Consolidated proposal: minimum records, first rail/crossmember builds, per-component execution/check/improvement cycle, Python extraction, catalogue/search, priority rules and future extensions.

Evidence: authored_document_inspected.

Documents: research/sources/round-08/component-plan-sources.json.

<a id="src-fe980d416f56"></a>

## SRC-fe980d416f56 — sequence

Original source: [${MODELING_ROOT}/research/action-audit/sequence.json](../action-audit/sequence.json)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-fea7e6f61e34"></a>

## SRC-fea7e6f61e34 — Driver iteration — reopened-front.png

Original source: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-front.png (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c012-reuse-01/reopened-front.png`)

Summary: Inspected front image shows four mounting bores, six terminal assemblies, X1/X2 connectors and indicator details; X1/X2/W/B markings render visibly.

Evidence: local_source_or_execution_record_inspected.

Documents: research/sources/round-16/driver-sources.json.

<a id="src-ff0bc4de820c"></a>

## SRC-ff0bc4de820c — Cylinder model segmentation — Point Cloud Library 1.15.1-dev documentation

Original source: [https://pointclouds.org/documentation/tutorials/cylinder_segmentation.html](https://pointclouds.org/documentation/tutorials/cylinder_segmentation.html)

Summary: The official PCL tutorial demonstrates SACSegmentationFromNormals<PointXYZ, Normal> with a point cloud and normals, SACMODEL_CYLINDER, RANSAC, normal-distance weight 0.1, 10000 iterations, 0.05 distance threshold, and radius limits 0 to 0.1. The example identifies the latter length settings as metres (5 cm threshold and 10 cm maximum radius). segment(inliers, coefficients) returns inlier indices and coefficients. Example evidence only; no project cloud was processed.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-independent.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-ff22572efb1e"></a>

## SRC-ff22572efb1e — BRepGProp Class Reference — Open CASCADE Technology Reference Manual 8.0.1

Original source: [https://occt3d.com/dev/doc/refman/html/class_b_rep_g_prop.html](https://occt3d.com/dev/doc/refman/html/class_b_rep_g_prop.html)

Summary: Official OCCT 8.0.1 reference inspected 2026-11-12 as targeted mass-property follow-up. `BRepGProp::VolumeProperties` computes volume properties into `GProp_GProps` for finite solid(s), no density attached; requires no free boundary and coherent orientation, which the API does not check. `UseTriangulation` selects triangulated or exact surfaces. Epsilon overload uses adaptive 2D Gauss integration and returns estimated relative error; Eps > 0.001 uses non-adaptive integration.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-ffac5faf4062"></a>

## SRC-ffac5faf4062 — License text

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/LICENSE](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

## Component iterations — 13 November 2026

### Lynx audit evidence — SRC-a4a7445ec595

Original source: Lynx audit evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/audit.json`)

Summary: Existing Lynx audit reports 95 solids and 128 block references; compared with the saved derivative audit.

Evidence: executed_native_state_read.

### Original Lynx CAD and source hashes — SRC-9f96098ee90a

Original source: Original Lynx CAD and source hashes (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/baseline.json`)

Summary: Pins the original DWG and manufacturer STEP bytes before correction; source hash matches the retained acquisition record.

Evidence: executed_file_inspection.

### Lynx blocks evidence — SRC-2fb804239b51

Original source: Lynx blocks evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/blocks.json`)

Summary: Native block membership at blocks stage; used to traverse the 130 placed solids and preserve their full insertion paths.

Evidence: executed_native_state_read.

### Lynx corrected blocks evidence — SRC-8383735f7fe8

Original source: Lynx corrected blocks evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-blocks.json`)

Summary: Native block membership at corrected blocks stage; used to traverse the 130 placed solids and preserve their full insertion paths.

Evidence: executed_native_state_read.

### Corrected Lynx placed solid hierarchy — SRC-5c766056233f

Original source: Corrected Lynx placed solid hierarchy (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-instances.json`)

Summary: 130 complete native solid instance paths and matrices after reviewed correction; outer millimetre-to-metre scale retained.

Evidence: executed_assembly_inspection.

### Lynx corrected records 0 native records — SRC-be2093995f07

Original source: Lynx corrected records 0 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-0.json`)

Summary: Native document 88 records for handles 81, 85, 89, 8D, 91, 95, 99, 9D. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 104 native records — SRC-9781d66101ed

Original source: Lynx corrected records 104 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-104.json`)

Summary: Native document 88 records for handles 1BB, 1BF, 1C3, 1C7, 1CB, 1CF, 1D3, 1D7. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 112 native records — SRC-c8dfce5c7575

Original source: Lynx corrected records 112 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-112.json`)

Summary: Native document 88 records for handles 1DB, 1DF, 1E3, 1E7, 1EB, 1EF, 1F3, 1F7. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 120 native records — SRC-1a99c0bf98d7

Original source: Lynx corrected records 120 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-120.json`)

Summary: Native document 88 records for handles 1FB, 1FF, 203, 207, 20B, 20F, 213, 214. Contains 6 solid definitions and 2 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 128 native records — SRC-fcb3e15bb17b

Original source: Lynx corrected records 128 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-128.json`)

Summary: Native document 88 records for handles 215, 216, 217, 218, 219, 21A, 21B, 21C. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 136 native records — SRC-b3bfb5570f38

Original source: Lynx corrected records 136 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-136.json`)

Summary: Native document 88 records for handles 21D, 21E, 21F, 220, 221, 222, 223, 224. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 144 native records — SRC-71bf5f751f30

Original source: Lynx corrected records 144 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-144.json`)

Summary: Native document 88 records for handles 225, 226, 227, 228, 229, 22A, 22B, 22C. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 152 native records — SRC-8ed937c0b7b8

Original source: Lynx corrected records 152 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-152.json`)

Summary: Native document 88 records for handles 22D, 22E, 22F, 230, 231, 232, 233, 234. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 16 native records — SRC-836615063de7

Original source: Lynx corrected records 16 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-16.json`)

Summary: Native document 88 records for handles BB, BC, BD, BE, BF, C3, C4, C5. Contains 3 solid definitions and 5 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 160 native records — SRC-0d314595fa4a

Original source: Lynx corrected records 160 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-160.json`)

Summary: Native document 88 records for handles 235, 236, 237, 238, 239, 23A, 23E, 23F. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 168 native records — SRC-fd8367c1e3f3

Original source: Lynx corrected records 168 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-168.json`)

Summary: Native document 88 records for handles 240, 241, 242, 243, 244, 245, 246, 247. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 176 native records — SRC-6a7e1cdf3015

Original source: Lynx corrected records 176 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-176.json`)

Summary: Native document 88 records for handles 248, 249, 24A, 24B, 24C, 24D, 24E, 24F. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 184 native records — SRC-5eac9403ed9d

Original source: Lynx corrected records 184 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-184.json`)

Summary: Native document 88 records for handles 250, 251, 252, 253, 254, 255, 256, 257. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 192 native records — SRC-ccdbf25e82c6

Original source: Lynx corrected records 192 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-192.json`)

Summary: Native document 88 records for handles 258, 259, 25A, 25B, 25C, 25D, 25E, 25F. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 200 native records — SRC-97954e9ed7ce

Original source: Lynx corrected records 200 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-200.json`)

Summary: Native document 88 records for handles 260, 261, 262, 263, 264, 265, 266, 267. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 208 native records — SRC-c65cf5c41654

Original source: Lynx corrected records 208 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-208.json`)

Summary: Native document 88 records for handles 268, 269, 26A, 26B, 26C, 26D, 26E, 26F. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 216 native records — SRC-f0e03c5ef882

Original source: Lynx corrected records 216 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-216.json`)

Summary: Native document 88 records for handles 270, 271, 272, 273, 274, 275, 276. Contains 0 solid definitions and 7 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 24 native records — SRC-45e10de48de3

Original source: Lynx corrected records 24 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-24.json`)

Summary: Native document 88 records for handles C9, CD, D1, D2, D6, DA, DE, E2. Contains 5 solid definitions and 3 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 32 native records — SRC-07381c175a35

Original source: Lynx corrected records 32 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-32.json`)

Summary: Native document 88 records for handles E3, E4, E8, EC, F0, F4, F8, F9. Contains 6 solid definitions and 2 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 40 native records — SRC-f60856cbdfb4

Original source: Lynx corrected records 40 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-40.json`)

Summary: Native document 88 records for handles FA, FB, FC, FD, 101, 102, 103, 104. Contains 4 solid definitions and 4 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 48 native records — SRC-d31478416fae

Original source: Lynx corrected records 48 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-48.json`)

Summary: Native document 88 records for handles 105, 109, 10D, 111, 115, 119, 11D, 11E. Contains 5 solid definitions and 3 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 56 native records — SRC-f272cb0c9c5c

Original source: Lynx corrected records 56 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-56.json`)

Summary: Native document 88 records for handles 122, 126, 12A, 12E, 132, 136, 13A, 13E. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 64 native records — SRC-74ea95f4c61a

Original source: Lynx corrected records 64 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-64.json`)

Summary: Native document 88 records for handles 142, 146, 14A, 14E, 152, 156, 15A, 15E. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 72 native records — SRC-550c25dedf92

Original source: Lynx corrected records 72 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-72.json`)

Summary: Native document 88 records for handles 162, 163, 164, 165, 166, 167, 168, 169. Contains 0 solid definitions and 8 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 8 native records — SRC-f64b6c2462f9

Original source: Lynx corrected records 8 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-8.json`)

Summary: Native document 88 records for handles A1, A5, A9, AD, B1, B2, B3, B7. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 80 native records — SRC-fce472423429

Original source: Lynx corrected records 80 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-80.json`)

Summary: Native document 88 records for handles 16A, 16B, 16C, 16D, 16E, 16F, 173, 177. Contains 2 solid definitions and 6 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 88 native records — SRC-b2615d68e946

Original source: Lynx corrected records 88 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-88.json`)

Summary: Native document 88 records for handles 17B, 17F, 183, 187, 18B, 18F, 193, 197. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx corrected records 96 native records — SRC-e7b396f933b9

Original source: Lynx corrected records 96 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/corrected-records-96.json`)

Summary: Native document 88 records for handles 19B, 19F, 1A3, 1A7, 1AB, 1AF, 1B3, 1B7. Contains 8 solid definitions and 0 insertions; stage corrected working model.

Evidence: executed_native_record_read.

### Lynx document checkpoint evidence — SRC-256d9dcd0f49

Original source: Lynx document checkpoint evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/document-checkpoint.json`)

Summary: Native state and document identity at the document checkpoint boundary; preserves the operation revision used for subsequent checks.

Evidence: executed_native_state_read.

### Executed Lynx driver check_lynx — SRC-eeed397bd2e6

Original source: Executed Lynx driver check_lynx (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/check_lynx.py`)

Summary: Compares 95 saved solid definitions, 60 source placements, 130 instance paths, metre units, outer scale and original-file hash; calculates explicit metre and millimetre vertex ranges.

Evidence: executed_implementation_artifact.

### Executed Lynx driver lynx_views — SRC-a2a785715504

Original source: Executed Lynx driver lynx_views (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/lynx_views.py`)

Summary: Sets native top and front views of saved document 89, captures both and recovers bounded capture requests under their original identities.

Evidence: executed_implementation_artifact.

### Lynx provenance evidence — SRC-75d0575521ec

Original source: Lynx provenance evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/provenance.json`)

Summary: Hashes the exact executed Lynx driver files and identifies their local helper bootstrap without recording authentication tokens.

Evidence: executed_artifact_provenance.

### Executed Lynx driver read_lynx — SRC-ca32afe0f973

Original source: Executed Lynx driver read_lynx (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/read_lynx.py`)

Summary: Recovers the original open, reads document 88 audit, 223 entity records and block membership, then captures the displaced initial assembly.

Evidence: executed_implementation_artifact.

### Executed Lynx driver record_lynx_source — SRC-6188c6fbaa58

Original source: Executed Lynx driver record_lynx_source (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/record_lynx_source.py`)

Summary: Writes the source-linked Lynx job and runs its source-readiness validation using retained STEP identity, units and placement frames.

Evidence: executed_implementation_artifact.

### Executed Lynx driver reopen_lynx — SRC-fe62091d82e4

Original source: Executed Lynx driver reopen_lynx (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/reopen_lynx.py`)

Summary: Recovers the pending derivative reopen, verifies saved hash and manifest, reads document 89 geometry and header and requests its isometric view.

Evidence: executed_implementation_artifact.

### Executed Lynx driver repair_lynx — SRC-7ec44d4b4885

Original source: Executed Lynx driver repair_lynx (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/repair_lynx.py`)

Summary: Builds the reviewed 60-placement source plan, retains the outer 0.001 scale, applies guarded corrections, reads corrected records and saves a separate checked derivative.

Evidence: executed_implementation_artifact.

### Executed Lynx driver resume_lynx — SRC-082426c6d5f2

Original source: Executed Lynx driver resume_lynx (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/executed-drivers/resume_lynx.py`)

Summary: Pins the original Lynx DWG and manufacturer STEP hashes and starts opening the existing saved assembly under a journaled request.

Evidence: executed_implementation_artifact.

### Lynx existing isometric view — SRC-9377f9a6519a

Original source: Lynx existing isometric view (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/existing-isometric.png`)

Summary: Actual initial image shows hardware displaced from the enclosure.

Evidence: executed_native_capture.

### Lynx front capture evidence — SRC-6bf28649add0

Original source: Lynx front capture evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/front-capture.json`)

Summary: Completed original capture request response for the front capture image, retained beside the inspected native image.

Evidence: executed_native_capture_result.

### Original Lynx drawing units — SRC-5cd1611c89a0

Original source: Original Lynx drawing units (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/header.json`)

Summary: Native header declares insertion unit code 6, metres, providing the interpretation of the retained 0.001 outer insertion scale.

Evidence: executed_native_state_read.

### Lynx isometric capture evidence — SRC-6ce289f7395b

Original source: Lynx isometric capture evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/isometric-capture.json`)

Summary: Completed original capture request response for the isometric capture image, retained beside the inspected native image.

Evidence: executed_native_capture_result.

### Lynx native operation journal — SRC-36ecfc230ce2

Original source: Lynx native operation journal (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/ocs-journal.jsonl`)

Summary: Append-only intent and response history for existing-model inspection, 60 guarded placement writes, verified save, reopen and view captures.

Evidence: executed_native_operation_journal.

### Lynx verified save and reopen — SRC-019bb82ec263

Original source: Lynx verified save and reopen (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/persistence.json`)

Summary: Separate checked derivative passes file hash, manifest and zero-error audit comparisons; original pending reopen request was recovered.

Evidence: executed_persistence_check.

### Lynx guarded correction readback — SRC-45f98d367645

Original source: Lynx guarded correction readback (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/placement-corrections.json`)

Summary: Sixty source placement writes pass readback; all 95 solid definitions remain unchanged.

Evidence: executed_native_correction.

### Lynx query evidence — SRC-727ae37a310c

Original source: Lynx query evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/query.json`)

Summary: Existing Lynx entity inventory identifies 223 native entities for bounded record inspection.

Evidence: executed_native_state_read.

### Lynx source readiness — SRC-d88062a24ef8

Original source: Lynx source readiness (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/readiness.json`)

Summary: Executed requirement validation for the exact manufacturer assembly and source-backed frame inputs.

Evidence: executed_input_validation.

### Lynx records 0 native records — SRC-ab9d1cc0b15b

Original source: Lynx records 0 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-0.json`)

Summary: Native document 88 records for handles 81, 85, 89, 8D, 91, 95, 99, 9D. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 104 native records — SRC-23b2720611ee

Original source: Lynx records 104 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-104.json`)

Summary: Native document 88 records for handles 1BB, 1BF, 1C3, 1C7, 1CB, 1CF, 1D3, 1D7. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 112 native records — SRC-b8a5068c8697

Original source: Lynx records 112 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-112.json`)

Summary: Native document 88 records for handles 1DB, 1DF, 1E3, 1E7, 1EB, 1EF, 1F3, 1F7. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 120 native records — SRC-058be1c6022d

Original source: Lynx records 120 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-120.json`)

Summary: Native document 88 records for handles 1FB, 1FF, 203, 207, 20B, 20F, 213, 214. Contains 6 solid definitions and 2 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 128 native records — SRC-510fdce758c7

Original source: Lynx records 128 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-128.json`)

Summary: Native document 88 records for handles 215, 216, 217, 218, 219, 21A, 21B, 21C. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 136 native records — SRC-e9bbfc1a980e

Original source: Lynx records 136 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-136.json`)

Summary: Native document 88 records for handles 21D, 21E, 21F, 220, 221, 222, 223, 224. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 144 native records — SRC-2751b2ee10da

Original source: Lynx records 144 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-144.json`)

Summary: Native document 88 records for handles 225, 226, 227, 228, 229, 22A, 22B, 22C. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 152 native records — SRC-33a0a0ddc238

Original source: Lynx records 152 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-152.json`)

Summary: Native document 88 records for handles 22D, 22E, 22F, 230, 231, 232, 233, 234. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 16 native records — SRC-567fe01db45e

Original source: Lynx records 16 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-16.json`)

Summary: Native document 88 records for handles BB, BC, BD, BE, BF, C3, C4, C5. Contains 3 solid definitions and 5 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 160 native records — SRC-da6832088dfd

Original source: Lynx records 160 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-160.json`)

Summary: Native document 88 records for handles 235, 236, 237, 238, 239, 23A, 23E, 23F. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 168 native records — SRC-b02199f3c627

Original source: Lynx records 168 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-168.json`)

Summary: Native document 88 records for handles 240, 241, 242, 243, 244, 245, 246, 247. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 176 native records — SRC-26c2d547c0a8

Original source: Lynx records 176 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-176.json`)

Summary: Native document 88 records for handles 248, 249, 24A, 24B, 24C, 24D, 24E, 24F. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 184 native records — SRC-89ab56f3445e

Original source: Lynx records 184 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-184.json`)

Summary: Native document 88 records for handles 250, 251, 252, 253, 254, 255, 256, 257. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 192 native records — SRC-9005f607e412

Original source: Lynx records 192 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-192.json`)

Summary: Native document 88 records for handles 258, 259, 25A, 25B, 25C, 25D, 25E, 25F. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 200 native records — SRC-9f0bd1cc0d2c

Original source: Lynx records 200 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-200.json`)

Summary: Native document 88 records for handles 260, 261, 262, 263, 264, 265, 266, 267. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 208 native records — SRC-9f0195c3ab12

Original source: Lynx records 208 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-208.json`)

Summary: Native document 88 records for handles 268, 269, 26A, 26B, 26C, 26D, 26E, 26F. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 216 native records — SRC-37a036bdf257

Original source: Lynx records 216 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-216.json`)

Summary: Native document 88 records for handles 270, 271, 272, 273, 274, 275, 276. Contains 0 solid definitions and 7 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 24 native records — SRC-500cc7b95998

Original source: Lynx records 24 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-24.json`)

Summary: Native document 88 records for handles C9, CD, D1, D2, D6, DA, DE, E2. Contains 5 solid definitions and 3 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 32 native records — SRC-169e80504fc9

Original source: Lynx records 32 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-32.json`)

Summary: Native document 88 records for handles E3, E4, E8, EC, F0, F4, F8, F9. Contains 6 solid definitions and 2 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 40 native records — SRC-b9c57ffb89e0

Original source: Lynx records 40 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-40.json`)

Summary: Native document 88 records for handles FA, FB, FC, FD, 101, 102, 103, 104. Contains 4 solid definitions and 4 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 48 native records — SRC-a7eb4b31ed51

Original source: Lynx records 48 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-48.json`)

Summary: Native document 88 records for handles 105, 109, 10D, 111, 115, 119, 11D, 11E. Contains 5 solid definitions and 3 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 56 native records — SRC-a258fd85727d

Original source: Lynx records 56 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-56.json`)

Summary: Native document 88 records for handles 122, 126, 12A, 12E, 132, 136, 13A, 13E. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 64 native records — SRC-09b214595569

Original source: Lynx records 64 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-64.json`)

Summary: Native document 88 records for handles 142, 146, 14A, 14E, 152, 156, 15A, 15E. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 72 native records — SRC-8ff54e1de411

Original source: Lynx records 72 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-72.json`)

Summary: Native document 88 records for handles 162, 163, 164, 165, 166, 167, 168, 169. Contains 0 solid definitions and 8 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 8 native records — SRC-080bd6b4503a

Original source: Lynx records 8 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-8.json`)

Summary: Native document 88 records for handles A1, A5, A9, AD, B1, B2, B3, B7. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 80 native records — SRC-d5211fa06d19

Original source: Lynx records 80 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-80.json`)

Summary: Native document 88 records for handles 16A, 16B, 16C, 16D, 16E, 16F, 173, 177. Contains 2 solid definitions and 6 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 88 native records — SRC-42ef68c0a219

Original source: Lynx records 88 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-88.json`)

Summary: Native document 88 records for handles 17B, 17F, 183, 187, 18B, 18F, 193, 197. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx records 96 native records — SRC-7087a96dadb8

Original source: Lynx records 96 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/records-96.json`)

Summary: Native document 88 records for handles 19B, 19F, 1A3, 1A7, 1AB, 1AF, 1B3, 1B7. Contains 8 solid definitions and 0 insertions; stage existing original import.

Evidence: executed_native_record_read.

### Lynx reopened blocks evidence — SRC-467e7131ee59

Original source: Lynx reopened blocks evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-blocks.json`)

Summary: Native block membership at reopened blocks stage; used to traverse the 130 placed solids and preserve their full insertion paths.

Evidence: executed_native_state_read.

### Lynx reopened checkpoint evidence — SRC-0a751f4d81c2

Original source: Lynx reopened checkpoint evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-checkpoint.json`)

Summary: Native state and document identity at the reopened checkpoint boundary; preserves the operation revision used for subsequent checks.

Evidence: executed_native_state_read.

### Lynx reopened front view — SRC-d11186282897

Original source: Lynx reopened front view (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-front.png`)

Summary: Actual reopened native view shows the assembled BMS cover, busbars and connection hardware; orientation is front.

Evidence: executed_native_capture.

### Saved Lynx drawing units — SRC-bdfdc162dfc5

Original source: Saved Lynx drawing units (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-header.json`)

Summary: Reopened checked derivative retains insertion unit code 6, metres.

Evidence: executed_native_state_read.

### Lynx reopened isometric view — SRC-aaaf6c5dd563

Original source: Lynx reopened isometric view (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-isometric.png`)

Summary: Actual reopened native view shows the assembled BMS cover, busbars and connection hardware; orientation is isometric.

Evidence: executed_native_capture.

### Lynx reopened records 0 native records — SRC-c43671ae8097

Original source: Lynx reopened records 0 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-0.json`)

Summary: Native document 89 records for handles 81, 85, 89, 8D, 91, 95, 99, 9D. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 104 native records — SRC-9ca25aacaf1c

Original source: Lynx reopened records 104 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-104.json`)

Summary: Native document 89 records for handles 1BB, 1BF, 1C3, 1C7, 1CB, 1CF, 1D3, 1D7. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 112 native records — SRC-ff6e7f977ca2

Original source: Lynx reopened records 112 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-112.json`)

Summary: Native document 89 records for handles 1DB, 1DF, 1E3, 1E7, 1EB, 1EF, 1F3, 1F7. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 120 native records — SRC-148f28990b68

Original source: Lynx reopened records 120 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-120.json`)

Summary: Native document 89 records for handles 1FB, 1FF, 203, 207, 20B, 20F, 213, 214. Contains 6 solid definitions and 2 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 128 native records — SRC-b14a6a2b185d

Original source: Lynx reopened records 128 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-128.json`)

Summary: Native document 89 records for handles 215, 216, 217, 218, 219, 21A, 21B, 21C. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 136 native records — SRC-c7081b3be440

Original source: Lynx reopened records 136 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-136.json`)

Summary: Native document 89 records for handles 21D, 21E, 21F, 220, 221, 222, 223, 224. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 144 native records — SRC-49c894b64172

Original source: Lynx reopened records 144 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-144.json`)

Summary: Native document 89 records for handles 225, 226, 227, 228, 229, 22A, 22B, 22C. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 152 native records — SRC-f0168c67c897

Original source: Lynx reopened records 152 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-152.json`)

Summary: Native document 89 records for handles 22D, 22E, 22F, 230, 231, 232, 233, 234. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 16 native records — SRC-38cef6ed62af

Original source: Lynx reopened records 16 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-16.json`)

Summary: Native document 89 records for handles BB, BC, BD, BE, BF, C3, C4, C5. Contains 3 solid definitions and 5 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 160 native records — SRC-03d1a09f78f8

Original source: Lynx reopened records 160 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-160.json`)

Summary: Native document 89 records for handles 235, 236, 237, 238, 239, 23A, 23E, 23F. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 168 native records — SRC-56a0f5891cd3

Original source: Lynx reopened records 168 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-168.json`)

Summary: Native document 89 records for handles 240, 241, 242, 243, 244, 245, 246, 247. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 176 native records — SRC-9919cced30fa

Original source: Lynx reopened records 176 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-176.json`)

Summary: Native document 89 records for handles 248, 249, 24A, 24B, 24C, 24D, 24E, 24F. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 184 native records — SRC-1a7c8d68bce8

Original source: Lynx reopened records 184 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-184.json`)

Summary: Native document 89 records for handles 250, 251, 252, 253, 254, 255, 256, 257. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 192 native records — SRC-01f96907504c

Original source: Lynx reopened records 192 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-192.json`)

Summary: Native document 89 records for handles 258, 259, 25A, 25B, 25C, 25D, 25E, 25F. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 200 native records — SRC-91332cccbebc

Original source: Lynx reopened records 200 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-200.json`)

Summary: Native document 89 records for handles 260, 261, 262, 263, 264, 265, 266, 267. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 208 native records — SRC-064e69f97070

Original source: Lynx reopened records 208 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-208.json`)

Summary: Native document 89 records for handles 268, 269, 26A, 26B, 26C, 26D, 26E, 26F. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 216 native records — SRC-c5392ad41c00

Original source: Lynx reopened records 216 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-216.json`)

Summary: Native document 89 records for handles 270, 271, 272, 273, 274, 275, 276. Contains 0 solid definitions and 7 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 24 native records — SRC-daa51fe3fdd2

Original source: Lynx reopened records 24 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-24.json`)

Summary: Native document 89 records for handles C9, CD, D1, D2, D6, DA, DE, E2. Contains 5 solid definitions and 3 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 32 native records — SRC-9e08629c78a3

Original source: Lynx reopened records 32 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-32.json`)

Summary: Native document 89 records for handles E3, E4, E8, EC, F0, F4, F8, F9. Contains 6 solid definitions and 2 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 40 native records — SRC-f09ccd9cf02a

Original source: Lynx reopened records 40 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-40.json`)

Summary: Native document 89 records for handles FA, FB, FC, FD, 101, 102, 103, 104. Contains 4 solid definitions and 4 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 48 native records — SRC-70229263a540

Original source: Lynx reopened records 48 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-48.json`)

Summary: Native document 89 records for handles 105, 109, 10D, 111, 115, 119, 11D, 11E. Contains 5 solid definitions and 3 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 56 native records — SRC-c2acb8079d68

Original source: Lynx reopened records 56 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-56.json`)

Summary: Native document 89 records for handles 122, 126, 12A, 12E, 132, 136, 13A, 13E. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 64 native records — SRC-dbebc08b0ba9

Original source: Lynx reopened records 64 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-64.json`)

Summary: Native document 89 records for handles 142, 146, 14A, 14E, 152, 156, 15A, 15E. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 72 native records — SRC-d4820d22dee4

Original source: Lynx reopened records 72 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-72.json`)

Summary: Native document 89 records for handles 162, 163, 164, 165, 166, 167, 168, 169. Contains 0 solid definitions and 8 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 8 native records — SRC-71ccf5670468

Original source: Lynx reopened records 8 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-8.json`)

Summary: Native document 89 records for handles A1, A5, A9, AD, B1, B2, B3, B7. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 80 native records — SRC-3311aa5fea40

Original source: Lynx reopened records 80 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-80.json`)

Summary: Native document 89 records for handles 16A, 16B, 16C, 16D, 16E, 16F, 173, 177. Contains 2 solid definitions and 6 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 88 native records — SRC-3569e6d94947

Original source: Lynx reopened records 88 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-88.json`)

Summary: Native document 89 records for handles 17B, 17F, 183, 187, 18B, 18F, 193, 197. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened records 96 native records — SRC-816e64244f99

Original source: Lynx reopened records 96 native records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-records-96.json`)

Summary: Native document 89 records for handles 19B, 19F, 1A3, 1A7, 1AB, 1AF, 1B3, 1B7. Contains 8 solid definitions and 0 insertions; stage saved derivative.

Evidence: executed_native_record_read.

### Lynx reopened top view — SRC-7f94a2475be7

Original source: Lynx reopened top view (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/reopened-top.png`)

Summary: Actual reopened native view shows the assembled BMS cover, busbars and connection hardware; orientation is top.

Evidence: executed_native_capture.

### Completed Lynx component iteration — SRC-7798e76e43a5

Original source: Completed Lynx component iteration (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/result.json`)

Summary: Records the checked DWG, source correction, scale-aware Python improvement, three inspected views and actual test/recovery history.

Evidence: executed_component_result.

### Lynx saved geometry checks — SRC-6c9c15d8564c

Original source: Lynx saved geometry checks (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/saved-assembly-checks.json`)

Summary: 159 comparisons pass for solid equality, 60 source placements, 130 instance paths/matrices, metre units, preserved 0.001 scale and original DWG bytes. Point ranges are explicitly converted into millimetres.

Evidence: executed_saved_geometry_check.

### Lynx source-linked feature requirements — SRC-426f459cb6f3

Original source: Lynx source-linked feature requirements (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/source-job.json`)

Summary: Binds exact rev04 M10 assembly, STEP length units and source placement frames to the retained manufacturer original.

Evidence: implementation_artifact.

### Reviewed Lynx placement corrections — SRC-e1fe7974d0c3

Original source: Reviewed Lynx placement corrections (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/source-placement-plan.json`)

Summary: Sixty internal insertions uniquely match inverted source frames. Outer 0.001 scaling is preserved because source millimetres convert into native drawing metres.

Evidence: executed_source_comparison.

### Lynx state evidence — SRC-9c538ca9300c

Original source: Lynx state evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/state.json`)

Summary: Existing Lynx opened in document 88 with current camera and document identities recorded.

Evidence: executed_native_state_read.

### Lynx top capture evidence — SRC-2b1e0de0467b

Original source: Lynx top capture evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c026-reuse-01/top-capture.json`)

Summary: Completed original capture request response for the top capture image, retained beside the inspected native image.

Evidence: executed_native_capture_result.

### Converter front capture evidence — SRC-e9e70b8fbc2d

Original source: Converter front capture evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/front-capture.json`)

Summary: Native front capture observation from document 87 during completion of the converter orthographic view checks.

Evidence: executed_native_capture_result.

### Converter front view — SRC-d03faba9877b

Original source: Converter front view (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/front.png`)

Summary: Actual native front image shows the converter terminal/cover or mounting/heatsink face. Inspected alongside the earlier successful rotated view.

Evidence: executed_native_capture.

### Converter orthographic capture journal — SRC-f98bb31e988b

Original source: Converter orthographic capture journal (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/ocs-journal.jsonl`)

Summary: Native top/front commands, capture intents and same-request recovery responses used to finish visual verification.

Evidence: executed_native_operation_journal.

### Completed converter iteration — SRC-fb7487babc95

Original source: Completed converter iteration (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/result.json`)

Summary: Combines the existing 39 passing saved geometry checks with three successful component views, preserving earlier failed result records.

Evidence: executed_component_result.

### Converter state after evidence — SRC-9303bc078b8c

Original source: Converter state after evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/state-after.json`)

Summary: Native state after observation from document 87 during completion of the converter orthographic view checks.

Evidence: executed_native_state_read.

### Converter state before evidence — SRC-77a21a6666d5

Original source: Converter state before evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/state-before.json`)

Summary: Native state before observation from document 87 during completion of the converter orthographic view checks.

Evidence: executed_native_state_read.

### Converter top capture evidence — SRC-b682e9c40220

Original source: Converter top capture evidence (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/top-capture.json`)

Summary: Native top capture observation from document 87 during completion of the converter orthographic view checks.

Evidence: executed_native_capture_result.

### Converter top view — SRC-2d34ea14c9fd

Original source: Converter top view (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c045-build-01/completion-2026-11-13/top.png`)

Summary: Actual native top image shows the converter terminal/cover or mounting/heatsink face. Inspected alongside the earlier successful rotated view.

Evidence: executed_native_capture.

### Scale-aware native assembly traversal — SRC-ef86743da4af

Original source: [Scale-aware native assembly traversal](../../scripts/step_placements.py)

Summary: Adds explicit positive uniform-scale support to native matrices and nested instance traversal, preserving default unit-scale guards. Exercised on the Lynx metre drawing and 130 placed solids.

Evidence: implementation_artifact.

### Uniform-scale assembly regression tests — SRC-1365d8cb5b94

Original source: [Uniform-scale assembly regression tests](../../tests/test_scaled_assembly.py)

Summary: Four cases verify rotation/translation with scale, invalid scales, unequal scales and all 130 recorded Lynx instance paths.

Evidence: implementation_artifact.

### Procedure for source-to-drawing unit conversion — SRC-e24ea3f3e131

Original source: [Procedure for source-to-drawing unit conversion](../../skills/cad-ocs-engineering/references/scaled-assemblies.md)

Summary: Documents the actual Lynx millimetre-source/metre-drawing conversion, separate internal correction and saved geometry handoffs.

Evidence: implementation_artifact.

### Resumed CAD helper regression execution — SRC-8bab030cd5d3

Original source: [Resumed CAD helper regression execution](../../execution/resumed-cad-tests-2026-11-13.txt)

Summary: Full recorded unittest execution: 100 tests pass in 15.323 seconds. The protected-output test intentionally emits its rejected-write result.

Evidence: executed_software_test_result.

### Lynx completed iteration report — SRC-6b5bcf790212

Original source: [Lynx completed iteration report](../../execution/c026-lynx-2026-11-13.md)

Summary: Reports corrected manufacturer assembly, 159 saved checks, explicit units, applied scale reader improvement and actual source and recovery evidence.

Evidence: executed_verification_report.

### Converter completed iteration report — SRC-36b3ef66e551

Original source: [Converter completed iteration report](../../execution/c045-completion-2026-11-13.md)

Summary: Reports reuse of saved converter geometry, newly successful orthographic views and the applied capture verification procedure.

Evidence: executed_verification_report.

### Lynx Smart BMS 500 NG M10 rev04 STEP original — SRC-a6c30a318e46

Original source: Lynx Smart BMS 500 NG M10 rev04 STEP original (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/Lynx-Smart-BMS-500-NG-M10-3D.stp`)

Summary: Existing retained manufacturer AP214 assembly declares millimetres and explicit source placement frames. Reused unchanged for the 60 internal correction comparisons.

Evidence: existing_local_manufacturer_original_inspected.

## BMW saved-check iteration — 13 November 2026

### BMW activated isometric capture — SRC-c1cd17605690

Original source: BMW activated isometric capture (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/activated-isometric.png`)

Summary: Actual inspected activated isometric image shows the previous Lynx BMS. The four capture bytes are identical despite the recorded BMW document and camera actions.

Evidence: executed_native_capture_failed_identity.

### BMW current native audit — SRC-7c43c07f98cd

Original source: BMW current native audit (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/audit.json`)

Summary: Saved document reports 13 solids and zero audit errors/warnings.

Evidence: executed_native_audit.

### BMW document native capabilities — SRC-8c2f0d50aa2d

Original source: BMW document native capabilities (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/capabilities.json`)

Summary: Installed native automation capabilities and document record collections were read before additional viewport inspection.

Evidence: executed_native_capability_read.

### BMW copy isometric capture — SRC-8a2300ee7ccd

Original source: BMW copy isometric capture (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/copy-isometric.png`)

Summary: Actual inspected copy isometric image shows the previous Lynx BMS. The four capture bytes are identical despite the recorded BMW document and camera actions.

Evidence: executed_native_capture_failed_identity.

### BMW isolated inspection document state — SRC-100b4715becf

Original source: BMW isolated inspection document state (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/copy-state.json`)

Summary: Fresh document 90 addresses an exact-byte BMW inspection copy; captured image retains the earlier Lynx view.

Evidence: executed_native_state_read.

### Executed BMW isolated-view driver — SRC-f35676bd27f5

Original source: Executed BMW isolated-view driver (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/executed-drivers/bmw_isolated_view.py`)

Summary: Copies exact original DWG bytes into a diagnostic path and opens a fresh document for a component-identity capture.

Evidence: executed_implementation_artifact.

### Executed BMW source and geometry driver — SRC-5cc1a26a5c2b

Original source: Executed BMW source and geometry driver (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/executed-drivers/check_bmw_iteration.py`)

Summary: Writes the initial source job and compares native case, mounting and cover features; later source revision 2 retains corrected report attribution separately.

Evidence: executed_implementation_artifact.

### BMW executed driver provenance — SRC-202743c156fc

Original source: BMW executed driver provenance (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/executed-drivers/provenance.json`)

Summary: Hashes retained inspection drivers and source reconstruction program; identifies the restricted helper bootstrap and preserves the original construction program as source.

Evidence: executed_artifact_provenance.

### Executed BMW inspection driver — SRC-e433169a1ce6

Original source: Executed BMW inspection driver (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/executed-drivers/start_bmw_iteration.py`)

Summary: Opens the existing module, checks original hash, reads header/audit and 13 saved native solids, then requests the first isometric capture.

Evidence: executed_implementation_artifact.

### BMW drawing units — SRC-ed75a17d7f36

Original source: BMW drawing units (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/header.json`)

Summary: Saved drawing insertion units code 4 identifies millimetres for source-bound geometry checks.

Evidence: executed_native_state_read.

### BMW isometric capture — SRC-b33b1135609a

Original source: BMW isometric capture (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/isometric.png`)

Summary: Actual inspected isometric image shows the previous Lynx BMS. The four capture bytes are identical despite the recorded BMW document and camera actions.

Evidence: executed_native_capture_failed_identity.

### BMW saved native geometry records — SRC-12777a7a34c9

Original source: BMW saved native geometry records (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/native-records.json`)

Summary: Document 79 readback contains all 13 exterior solids with component metadata and native SAB geometry used by the new checker.

Evidence: executed_native_record_read.

### BMW current native request journal — SRC-13f3a3686de7

Original source: BMW current native request journal (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/ocs-journal.jsonl`)

Summary: Stable request intents and responses preserve existing open, view setup, explicit activation, pointer event, exact-byte-copy open and captures.

Evidence: executed_native_operation_journal.

### BMW pointer isometric capture — SRC-b0614d34bbd7

Original source: BMW pointer isometric capture (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/pointer-isometric.png`)

Summary: Actual inspected pointer isometric image shows the previous Lynx BMS. The four capture bytes are identical despite the recorded BMW document and camera actions.

Evidence: executed_native_capture_failed_identity.

### BMW native pointer response — SRC-b02693d9042f

Original source: BMW native pointer response (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/pointer-result.json`)

Summary: Supported native pointer move and wheel action completed; subsequent capture still shows the Lynx BMS.

Evidence: executed_native_view_action.

### BMW input coverage check — SRC-5ae53054d5c4

Original source: BMW input coverage check (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/readiness.json`)

Summary: Current source revision passes required feature/hash coverage before the 19 saved-geometry comparisons.

Evidence: executed_input_validation.

### BMW iteration stage result — SRC-da0f92d3a5e0

Original source: BMW iteration stage result (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/result.json`)

Summary: Saved geometry and the applied planar-pattern helper pass; component remains IN_PROGRESS with a blocked visual identity stage. Original BMW file hash stays unchanged.

Evidence: executed_component_result.

### BMW saved geometry comparisons — SRC-f5b9e2c34e6f

Original source: BMW saved geometry comparisons (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/saved-checks.json`)

Summary: 19 passing comparisons cover 13 closed solids, case dimensions, four mounting bores and all 24 closed cover recesses.

Evidence: executed_saved_geometry_check.

### Existing BMW reconstruction source program — SRC-94d4b9997579

Original source: Existing BMW reconstruction source program (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/source/build_bmw_i3_94ah.py`)

Summary: Preserved original construction parameters supply the six-by-four pressing grid and existing exterior interpretation. Its construction function was not rerun.

Evidence: existing_local_implementation_source_inspected.

### BMW initial source requirements — SRC-4bf57d873df3

Original source: BMW initial source requirements (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/source-job-r01.json`)

Summary: Preserves the initial direct-HTML dimension binding before source review identified the report as the actual retained dimensional evidence.

Evidence: historical_implementation_artifact.

### BMW source requirements revision 2 — SRC-6bfdf70ce9d1

Original source: BMW source requirements revision 2 (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/source-job.json`)

Summary: Binds reported case dimensions to the existing geometry report and reconstruction features to their retained records; includes exact expected 24 recess centres.

Evidence: implementation_artifact.

### BMW source evidence review — SRC-e8db5a8bec64

Original source: BMW source evidence review (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/source-review.json`)

Summary: Three retained EVShop HTML copies lack the recorded dimension text; current source revision attributes dimensions through the existing geometry report. Numeric expectations stay unchanged.

Evidence: executed_local_source_review.

### BMW existing document state — SRC-79b348f11de4

Original source: BMW existing document state (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/state.json`)

Summary: Records existing saved BMW document 79, its camera and document identity before current inspection.

Evidence: executed_native_state_read.

### BMW failed capture identity checks — SRC-cc7a5085d90e

Original source: BMW failed capture identity checks (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/visual-checks.json`)

Summary: Four native images have the same SHA-256 and show the previous Lynx BMS while native BMW documents are 79 and 90.

Evidence: executed_visual_verification.

### BMW diagnostic copy provenance — SRC-9a7e251c187a

Original source: BMW diagnostic copy provenance (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/visual-copy.json`)

Summary: Pins original and inspection-copy paths and their identical DWG SHA-256; purpose is viewport diagnosis with zero geometry or format changes.

Evidence: executed_file_copy_provenance.

### BMW byte-identical inspection copy — SRC-35c99d126bf6

Original source: BMW byte-identical inspection copy (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/visual-inspection-copy.dwg`)

Summary: Exact original saved geometry opened in isolated document 90 to test stale existing-tab rendering; this is a diagnostic work artifact.

Evidence: executed_byte_identical_copy.

### Shared repeated planar-boundary checker — SRC-5b8f29b55228

Original source: [Shared repeated planar-boundary checker](../../scripts/feature_checks.py)

Summary: Adds a source-bound plane level, complete closed-boundary count, centres and span comparison for repeated recesses.

Evidence: implementation_artifact.

### Named battery case measurement groups — SRC-5c74a56ff439

Original source: [Named battery case measurement groups](../../scripts/battery_module.py)

Summary: Adds check_tabbed_case, reusing source readiness, named native parts, closed-body and mounting-pattern checks with explicit component measurement groups.

Evidence: implementation_artifact.

### BMW saved-case and recess regression tests — SRC-c4061056ed3f

Original source: [BMW saved-case and recess regression tests](../../tests/test_tabbed_battery.py)

Summary: Six actual-record cases pass; they exercise correct geometry and detection of incorrect length, shifted/missing recesses, incorrect floor and open boundary.

Evidence: implementation_artifact.

### Current component iteration skill — SRC-6b239a9bfdd1

Original source: [Current component iteration skill](../../skills/cad-ocs-engineering/SKILL.md)

Summary: Routes component work through existing source, native geometry, persistence, visual identity and checked improvement procedures, including scaled assemblies and multi-solid battery cases.

Evidence: implementation_artifact.

### Tabbed battery and cover-pattern procedure — SRC-240f5a0db534

Original source: [Tabbed battery and cover-pattern procedure](../../skills/cad-ocs-engineering/references/tabbed-battery.md)

Summary: Records the saved BMW case measurement groups, source/reconstruction attribution, repeated-boundary checker and concrete stale-capture failure.

Evidence: implementation_artifact.

### BMW saved-check iteration report — SRC-de515b0eea67

Original source: [BMW saved-check iteration report](../../execution/c022-bmw-2026-11-13.md)

Summary: Reports 19 passing saved comparisons, the applied six-test improvement, report-bound dimensional evidence and blocked visual identity stage.

Evidence: executed_verification_report.

### BMW iteration full regression result — SRC-2cf3d0d9c4d9

Original source: [BMW iteration full regression result](../../execution/bmw-iteration-tests-2026-11-13.txt)

Summary: Records the final full helper test run after source revision 2. All 106 tests pass; protected-output rejection is an intentional test case.

Evidence: executed_software_test_result.

### Retained BMW seller HTML evshop_page_fr.html — SRC-d8586951cbe6

Original source: Retained BMW seller HTML evshop_page_fr.html (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/bmw-i3-94ah/evshop_page_fr.html`)

Summary: Inspected exact retained HTML content during source review. This inspection led to current report-based dimension binding; the original file remains unchanged.

Evidence: existing_local_original_inspected.

### Retained BMW seller HTML evshop_page_de.html — SRC-149df552e1f9

Original source: Retained BMW seller HTML evshop_page_de.html (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/bmw-i3-94ah/evshop_page_de.html`)

Summary: Inspected exact retained HTML content during source review. This inspection led to current report-based dimension binding; the original file remains unchanged.

Evidence: existing_local_original_inspected.

### Retained BMW seller HTML evshop_page_en.html — SRC-a351e9134375

Original source: Retained BMW seller HTML evshop_page_en.html (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/bmw-i3-94ah/evshop_page_en.html`)

Summary: Inspected exact retained HTML content during source review. This inspection led to current report-based dimension binding; the original file remains unchanged.

Evidence: existing_local_original_inspected.

### Existing BMW geometry and attribution record — SRC-c170afb93281

Original source: Existing BMW geometry and attribution record (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/bmw-i3-94ah-geometry.md`)

Summary: Records EVShop-attributed 410/385/310/150 mm case dimensions and separately labelled reconstructed mounting centres, cover pattern and loose cable pose. Supplies current component-check inputs.

Evidence: existing_local_report_inspected.

### Local OCS control source actions.rs — SRC-c8f3cb9eeded

Original source: Local OCS control source actions.rs (`${OCS_ROOT}/src/app/control/actions.rs`)

Summary: Local source read to identify native pointer, document activation and capture actions. The current pointer call completed and its observed capture result is retained separately.

Evidence: local_implementation_source_inspected.

### Local OCS control source mod.rs — SRC-0d1de3da8732

Original source: Local OCS control source mod.rs (`${OCS_ROOT}/src/app/control/mod.rs`)

Summary: Local source read to identify native pointer, document activation and capture actions. The current pointer call completed and its observed capture result is retained separately.

Evidence: local_implementation_source_inspected.

## Existing-model reconciliation — 13 November 2026

### Actual-file component start check — SRC-33d3e8961151

Original source: [Actual-file component start check](../../scripts/model_inventory.py)

Summary: Reads manifest and work-record model/output/native_model paths, sheet links and filesystem files. Returns skip, locate, review or new-model action without opening CAD.

Evidence: implementation_artifact.

### Existing-model start regression tests — SRC-cb2e35b829eb

Original source: [Existing-model start regression tests](../../tests/test_model_inventory.py)

Summary: Ten tests cover stale status, recorded path fields, sheet discovery, unlinked files, dependency models, 2D references and completed-state preservation.

Evidence: implementation_artifact.

### Component iteration skill with mandatory file lookup — SRC-6b239a9bfdd1

Original source: [Component iteration skill with mandatory file lookup](../../skills/cad-ocs-engineering/SKILL.md)

Summary: Requires actual 3D file and prior-record inspection before every component start and reuse of existing completed models.

Evidence: implementation_artifact.

### Existing-model start procedure — SRC-758d94d927aa

Original source: [Existing-model start procedure](../../skills/cad-ocs-engineering/references/existing-model-start-check.md)

Summary: Documents each lookup result, exact FERME command, identity review, reuse of existing checks and separation of 2D references.

Evidence: implementation_artifact.

### Standing existing-model reuse instruction — SRC-8f9b6f25cd0d

Original source: [Standing existing-model reuse instruction](../../AGENTS.md)

Summary: Records the 13 November instruction to check actual files before every start and mark matching existing models DONE in the current list.

Evidence: registered_user_instruction.

### Existing-model reconciliation report — SRC-2adf14e1a45e

Original source: [Existing-model reconciliation report](../../execution/existing-model-audit-2026-11-13.md)

Summary: Reports 103 checked rows, 43 files, 13 existing matching models and four stale status corrections, with the next tyre file lookup.

Evidence: executed_reconciliation_report.

### Existing-model guard test result — SRC-f6862578e31e

Original source: [Existing-model guard test result](../../execution/existing-model-start-tests-2026-11-13.txt)

Summary: Recorded execution of ten focused start-check tests; all pass.

Evidence: executed_software_test_result.

### Full before-and-after component file audit — SRC-67b43e6b7da4

Original source: Full before-and-after component file audit (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/audit.json`)

Summary: Contains all 103 before/after entries and 43 file hashes; identifies 13 matching existing 3D components and four status corrections.

Evidence: executed_filesystem_reconciliation.

### Human-readable completed component file list — SRC-d32e5f329b48

Original source: Human-readable completed component file list (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/README.md`)

Summary: Lists 13 DONE components with actual file paths, the four status corrections and next-component file check.

Evidence: executed_reconciliation_report.

### Trelleborg T539 actual-file start check — SRC-cd1b7c790611

Original source: Trelleborg T539 actual-file start check (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/next-component-check.json`)

Summary: C001 tyre lookup scans all 43 available model/reference files and returns NEW_MODEL_REQUIRED. Existing completed components stay outside this construction candidate.

Evidence: executed_filesystem_start_check.

### Current component manifest with CAD completion states — SRC-41482c223014

Original source: Current component manifest with CAD completion states (`${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json`)

Summary: Preserves all 103 component identities and source/dependency fields; adds current CAD states and preferred existing paths for 13 modeled components.

Evidence: implementation_data_artifact.

### Reconciled component work states — SRC-4f0c8d392a38

Original source: Reconciled component work states (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/component-work.json`)

Summary: Four stale statuses become DONE with linked existing geometry, preserved prior records and current filesystem-check evidence. All existing CAD is reused.

Evidence: implementation_data_artifact.

### CAD model index with current completion list — SRC-c66fe74bfd16

Original source: CAD model index with current completion list (`${FERME_ROOT}/engineering/module-development/cad/README.md`)

Summary: Adds the current 13-component completion list and mandatory actual-file lookup above the preserved component table and dated iteration records.

Evidence: implementation_documentation.

### Motenergy ME0907 motor completion reconciliation — SRC-30a98a34cb6d

Original source: Motenergy ME0907 motor completion reconciliation (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/component-results/C005.json`)

Summary: Marks C005 DONE from its existing matching 3D file and retained checks. Previous state IN_PROGRESS and historical result reference are preserved.

Evidence: executed_status_reconciliation.

### Sumitomo PRO-M CH54065G10 gearmotor completion reconciliation — SRC-78e4e9208e59

Original source: Sumitomo PRO-M CH54065G10 gearmotor completion reconciliation (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/component-results/C010.json`)

Summary: Marks C010 DONE from its existing matching 3D file and retained checks. Previous state NOT_STARTED and historical result reference are preserved.

Evidence: executed_status_reconciliation.

### Sumitomo PRO-L CH54527G10 gearmotor completion reconciliation — SRC-1e186a487fe5

Original source: Sumitomo PRO-L CH54527G10 gearmotor completion reconciliation (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/component-results/C011.json`)

Summary: Marks C011 DONE from its existing matching 3D file and retained checks. Previous state NOT_STARTED and historical result reference are preserved.

Evidence: executed_status_reconciliation.

### BMW i3 94Ah battery module completion reconciliation — SRC-afdbd5edcfcc

Original source: BMW i3 94Ah battery module completion reconciliation (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/existing-model-audit-2026-11-13/component-results/C022.json`)

Summary: Marks C022 DONE from its existing matching 3D file and retained checks. Previous state IN_PROGRESS and historical result reference are preserved.

Evidence: executed_status_reconciliation.

### blickle-ls-ps310k-support-wheel-reference.dwg — existing file inventory — SRC-e4d0aa2ce4b4

Original source: blickle-ls-ps310k-support-wheel-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/blickle-ls-ps310k-support-wheel-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### blickle-ls-vle250k-support-wheel-reference.dwg — existing file inventory — SRC-f4e146422d3e

Original source: blickle-ls-vle250k-support-wheel-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/blickle-ls-vle250k-support-wheel-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### hy400-hy70716a-rim-interface-reference.dwg — existing file inventory — SRC-622a7b1a5254

Original source: hy400-hy70716a-rim-interface-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/hy400-hy70716a-rim-interface-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### iso730-category-1-interface-reference.dwg — existing file inventory — SRC-76dc483c3633

Original source: iso730-category-1-interface-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/iso730-category-1-interface-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### iso730-category-1n-interface-reference.dwg — existing file inventory — SRC-9806f18177c5

Original source: iso730-category-1n-interface-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/iso730-category-1n-interface-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### item-line8-m8-connection-interface-reference.dwg — existing file inventory — SRC-aa161a4cd4c0

Original source: item-line8-m8-connection-interface-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/item-line8-m8-connection-interface-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### kc14940-square-tube-connection-reference.dwg — existing file inventory — SRC-e4b4947b4986

Original source: kc14940-square-tube-connection-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/kc14940-square-tube-connection-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### quadboss-steely-608489-rim-interface-reference.dwg — existing file inventory — SRC-419bd0e5cdaf

Original source: quadboss-steely-608489-rim-interface-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/quadboss-steely-608489-rim-interface-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### skf-sy20tf-mounting-reference.dwg — existing file inventory — SRC-487528ab019b

Original source: skf-sy20tf-mounting-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/skf-sy20tf-mounting-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### spp-zsk0750-trailer-interface-reference.dwg — existing file inventory — SRC-133be125123c

Original source: spp-zsk0750-trailer-interface-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/2d_schemas/drawings/spp-zsk0750-trailer-interface-reference.dwg`)

Summary: Existing 2D interface reference included in the filesystem inventory and kept separate from completed 3D component files.

Evidence: existing_local_2d_file_inventory.

### bmw-i3-94ah-module.dwg — existing file inventory — SRC-f66bd429303e

Original source: bmw-i3-94ah-module.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/bmw-i3-94ah-module.dwg`)

Summary: Existing 3D file associated with C022 — BMW i3 94Ah battery module. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### fibox-arca-203015t-8121020.dwg — existing file inventory — SRC-b2d596e125f6

Original source: fibox-arca-203015t-8121020.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/fibox-arca-203015t-8121020.dwg`)

Summary: Existing 3D file associated with C029 — Fibox ARCA203015 enclosure. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### item-angle-bracket-set-8-40x40-41115.dwg — existing file inventory — SRC-32ccc223976e

Original source: item-angle-bracket-set-8-40x40-41115.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/item-angle-bracket-set-8-40x40-41115.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### item-profile-8-40x40-light-02633-segment-100mm.dwg — existing file inventory — SRC-cbf5e1960412

Original source: item-profile-8-40x40-light-02633-segment-100mm.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/item-profile-8-40x40-light-02633-segment-100mm.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### item-t-slot-nut-8-st-m8-02618.dwg — existing file inventory — SRC-cf54653f6b35

Original source: item-t-slot-nut-8-st-m8-02618.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/item-t-slot-nut-8-st-m8-02618.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### motenergy-me0907-mechanical-reference.dwg — existing file inventory — SRC-bac57ae3a67d

Original source: motenergy-me0907-mechanical-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/motenergy-me0907-mechanical-reference.dwg`)

Summary: Existing 3D file associated with C005 — Motenergy ME0907 motor. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### neugart-ngv064-wheel-160.dwg — existing file inventory — SRC-b0ae08bfa359

Original source: neugart-ngv064-wheel-160.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/neugart-ngv064-wheel-160.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### neugart-ngv090-wheel-200.dwg — existing file inventory — SRC-d9bf927f1b4a

Original source: neugart-ngv090-wheel-200.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/neugart-ngv090-wheel-200.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### neugart-ngv110-wheel-250.dwg — existing file inventory — SRC-98e16cfbc51e

Original source: neugart-ngv110-wheel-250.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/neugart-ngv110-wheel-250.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### nissan-leaf-gen2-module-300x222x34.dwg — existing file inventory — SRC-e941de7f22bc

Original source: nissan-leaf-gen2-module-300x222x34.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/nissan-leaf-gen2-module-300x222x34.dwg`)

Summary: Existing 3D file associated with C021 — Nissan Leaf Gen2 battery module. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### p01-main-frame-longitudinal-rail-reference.dwg — existing file inventory — SRC-fe0ed186d8d8

Original source: p01-main-frame-longitudinal-rail-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/p01-main-frame-longitudinal-rail-reference.dwg`)

Summary: Existing 3D file associated with P01 — Main frame longitudinal rail. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### p02-main-frame-crossmember-reference.dwg — existing file inventory — SRC-26613ca599a7

Original source: p02-main-frame-crossmember-reference.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/p02-main-frame-crossmember-reference.dwg`)

Summary: Existing 3D file associated with P02 — Main frame crossmember. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### roboteq-mdc2x-manufacturer-assembly.dwg — existing file inventory — SRC-e3336ac55611

Original source: roboteq-mdc2x-manufacturer-assembly.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/roboteq-mdc2x-manufacturer-assembly.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### skf-sy20tf-checked.dwg — existing file inventory — SRC-5c0d49b55a8f

Original source: skf-sy20tf-checked.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/skf-sy20tf-checked.dwg`)

Summary: Existing 3D file associated with C009 — SKF SY20TF bearing unit. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### skf-sy20tf.dwg — existing file inventory — SRC-a60085185158

Original source: skf-sy20tf.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/skf-sy20tf.dwg`)

Summary: Existing 3D file associated with C009 — SKF SY20TF bearing unit. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### sumitomo-eco-m-ch52578.dwg — existing file inventory — SRC-2d9d30506fd3

Original source: sumitomo-eco-m-ch52578.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-eco-m-ch52578.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### sumitomo-eco-s-absolute-ch54149.dwg — existing file inventory — SRC-179ceac88c1a

Original source: sumitomo-eco-s-absolute-ch54149.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-eco-s-absolute-ch54149.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### sumitomo-eco-s-resolver-ch51944.dwg — existing file inventory — SRC-79411293ac82

Original source: sumitomo-eco-s-resolver-ch51944.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-eco-s-resolver-ch51944.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### sumitomo-pro-l-ch54527.dwg — existing file inventory — SRC-0dd3c026cbac

Original source: sumitomo-pro-l-ch54527.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-pro-l-ch54527.dwg`)

Summary: Existing 3D file associated with C011 — Sumitomo PRO-L CH54527G10 gearmotor. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### sumitomo-pro-m-ch54065.dwg — existing file inventory — SRC-8746a0585203

Original source: sumitomo-pro-m-ch54065.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-pro-m-ch54065.dwg`)

Summary: Existing 3D file associated with C010 — Sumitomo PRO-M CH54065G10 gearmotor. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### sumitomo-smartris-driver-ch52308-checked.dwg — existing file inventory — SRC-2bdc86cc68a8

Original source: sumitomo-smartris-driver-ch52308-checked.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-smartris-driver-ch52308-checked.dwg`)

Summary: Existing 3D file associated with C012 — Sumitomo standard driver CH52308G10G10. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### sumitomo-smartris-driver-ch52308.dwg — existing file inventory — SRC-665cfb1ddd3b

Original source: sumitomo-smartris-driver-ch52308.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/sumitomo-smartris-driver-ch52308.dwg`)

Summary: Existing 3D file associated with C012 — Sumitomo standard driver CH52308G10G10. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### victron-lithium-ng-25.6v-100ah.dwg — existing file inventory — SRC-e8bdba090964

Original source: victron-lithium-ng-25.6v-100ah.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/victron-lithium-ng-25.6v-100ah.dwg`)

Summary: Existing 3D file associated with C023 — Victron NG25.6V100Ah battery. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### victron-lynx-smart-bms-500-ng-m10-checked.dwg — existing file inventory — SRC-4b603333faf9

Original source: victron-lynx-smart-bms-500-ng-m10-checked.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/victron-lynx-smart-bms-500-ng-m10-checked.dwg`)

Summary: Existing 3D file associated with C026 — Victron Lynx Smart BMS NG500 M10. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### victron-lynx-smart-bms-500-ng-m10.dwg — existing file inventory — SRC-3e0b8d150d0e

Original source: victron-lynx-smart-bms-500-ng-m10.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/victron-lynx-smart-bms-500-ng-m10.dwg`)

Summary: Existing 3D file associated with C026 — Victron Lynx Smart BMS NG500 M10. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### victron-orion-tr-smart-24-12-30a.dwg — existing file inventory — SRC-7d065c90de76

Original source: victron-orion-tr-smart-24-12-30a.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/parts/victron-orion-tr-smart-24-12-30a.dwg`)

Summary: Existing 3D file associated with C045 — Victron Orion24-12 converter. Checked file existence, size and SHA-256; existing geometry and recorded checks are reused.

Evidence: existing_local_3d_file_inventory.

### visual-inspection-copy.dwg — existing file inventory — SRC-35c99d126bf6

Original source: visual-inspection-copy.dwg — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/visual-inspection-copy.dwg`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### LiFePO4-Battery-25.6V100Ah-NG.stp — existing file inventory — SRC-7fc6417a02f1

Original source: LiFePO4-Battery-25.6V100Ah-NG.stp — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/source/LiFePO4-Battery-25.6V100Ah-NG.stp`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### Fibox-ARCA-203015T-8121020.step — existing file inventory — SRC-ec27d08dafa1

Original source: Fibox-ARCA-203015T-8121020.step — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c029-build-01/source/Fibox-ARCA-203015T-8121020.step`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### Victron-Orion-Tr-Smart-Isolated-12-24-360W-family.STEP — existing file inventory — SRC-3814905f350e

Original source: Victron-Orion-Tr-Smart-Isolated-12-24-360W-family.STEP — existing file inventory (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c043-build-01/source/Victron-Orion-Tr-Smart-Isolated-12-24-360W-family.STEP`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### Lynx-Smart-BMS-500-NG-M10-3D.stp — existing file inventory — SRC-a6c30a318e46

Original source: Lynx-Smart-BMS-500-NG-M10-3D.stp — existing file inventory (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/Lynx-Smart-BMS-500-NG-M10-3D.stp`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### Roboteq-MDC2x-step3d.stp — existing file inventory — SRC-8207668e8d28

Original source: Roboteq-MDC2x-step3d.stp — existing file inventory (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/Roboteq-MDC2x-step3d.stp`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

### LiFePO4-Battery-25.6V100Ah-NG.stp — existing file inventory — SRC-d628632cecd6

Original source: LiFePO4-Battery-25.6V100Ah-NG.stp — existing file inventory (`${FERME_ROOT}/engineering/module-development/parts/dimension-evidence/source-files/victron-ng/LiFePO4-Battery-25.6V100Ah-NG.stp`)

Summary: Existing 3D library/source/work file included in the project-wide lookup. Its actual path, size and SHA-256 are retained for component identity review.

Evidence: existing_local_3d_file_inventory.

## Tyre source stage — 13 November 2026

### Trelleborg Technical manual — SRC-40bcecc74df2

Original source: [Trelleborg Technical manual](https://www.trelleborg-tires.com/-/media/tires-aft/datatsheet/technical-manual/trelleborg-technical-manual-en.pdf?hash=AB0C897622FFD6443624A33BDFA5552E&rev=258948143820400e9a05c5a63b8c7ae0&sc_lang=en)

Summary: The exact 18x8.50-8, PR 6, T539 Farming row lists 7.00I rim, permitted 6.50-8, OD 466 mm ±1.5%, section width 222 mm ±2%, max air pressure 2.8 bar, max load 475 kg at 30 km/h, and rolling circumference 1384 mm ±2.5%. This is exterior envelope and nominal rim-contour evidence. The row gives no bead-seat, bead profile, wall, tread-depth or sectional profile dimensions. PDF metadata dates creation 2026-10-05 and modification 2026-10-06.

Evidence: downloaded_original.

### Trelleborg Light service tires brochure — SRC-f7d0f172c13c

Original source: [Trelleborg Light service tires brochure](https://www.trelleborg-tires.com/-/media/tires-aft/datatsheet/brochure/trelleborgtires_light_services_tire_eng.pdf?hash=B973556E3AB61ED5496649FACDE2834A%3F&openpdf=1&rev=9426684de3c84c7f8f90224ee3eccacc&sc_lang=en)

Summary: Lists 18x8.50-8 T539 TL, 4 PR, with rim 7.00I, OD 472 mm, section 222 mm, 1.5 bar, 375 kg at 30 km/h, rolling circumference 1402 mm. This is a different 4PR tubeless row and does not supply dimensions for C001's 6PR tube-type variant. No profile or bead drawing found.

Evidence: downloaded_original.

### Trelleborg Visual Folder — SRC-83397b2076da

Original source: [Trelleborg Visual Folder](https://www.trelleborg-tires.com/-/media/tires-aft/datatsheet/brochure/trelleborgtires-visual-folder-en.pdf?hash=F1F4348D02B7B629FEE0733E5A80B6B0&rev=1544b91184bf44bfbf71dc7ecd5da91f&sc_lang=en)

Summary: Manufacturer visual folder contains a T539 family label. It provides no size-specific 18x8.50-8 drawing or dimensioned tyre profile.

Evidence: downloaded_original.

### Trelleborg T539 product image, 575x575 — SRC-e1ef859bc0e3

Original source: [Trelleborg T539 product image, 575x575](https://www.trelleborg-tires.com/-/media/tires-aft/tires-images/light-service-tires/light-service-575x575/trelleborgt539-575x575.jpg?h=575&iar=0&w=575&rev=5e7c124eacaf40c4b510185dcfe12cea&hash=0E3DE6519BDC6FD8343FB5A78A15BACB)

Summary: Exact T539 manufacturer product image linked by the T539 product page. It shows a three-quarter tyre and mounted rim, with tread and sidewall visible. The page and image do not associate this image with the 18x8.50-8 size; use it as visual tread/sidewall reference only, not as a dimensioned interface source.

Evidence: downloaded_manufacturer_product_image.

### Trelleborg T539 product page (English) — SRC-803fb306f940

Original source: [Trelleborg T539 product page (English)](https://www.trelleborg-tires.com/en/products-and-solutions/agriculture-and-forestry-tires/gardening-club-cars-and-snow-tires/gardening/t539)

Summary: The official product page identifies T539, links the Light service tires brochure and Visual Folder, and embeds the retained T539 product image. Its page HTML does not contain a STEP/CAD file or a dimensioned section/bead drawing.

Evidence: downloaded_web_page_snapshot.

### trelleborg light service brochure response headers — SRC-bc2905798e67

Original source: trelleborg light service brochure response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/trelleborg-light-service-brochure-response-headers.txt`)

Summary: Retained HTTP response headers for trelleborg-light-service-brochure acquisition, including actual response status/content type when provided.

Evidence: executed_retrieval_metadata.

### trelleborg manual response headers — SRC-c3e6932e4972

Original source: trelleborg manual response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/trelleborg-manual-response-headers.txt`)

Summary: Retained HTTP response headers for trelleborg-manual acquisition, including actual response status/content type when provided.

Evidence: executed_retrieval_metadata.

### trelleborg t539 page response headers — SRC-2126824b9855

Original source: trelleborg t539 page response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/trelleborg-t539-page-response-headers.txt`)

Summary: Retained HTTP response headers for trelleborg-t539-page acquisition, including actual response status/content type when provided.

Evidence: executed_retrieval_metadata.

### trelleborg t539 photo response headers — SRC-f1f846f920ea

Original source: trelleborg t539 photo response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/trelleborg-t539-photo-response-headers.txt`)

Summary: Retained HTTP response headers for trelleborg-t539-photo acquisition, including actual response status/content type when provided.

Evidence: executed_retrieval_metadata.

### trelleborg visual folder response headers — SRC-6e85c2c8ade7

Original source: trelleborg visual folder response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/trelleborg-visual-folder-response-headers.txt`)

Summary: Retained HTTP response headers for trelleborg-visual-folder acquisition, including actual response status/content type when provided.

Evidence: executed_retrieval_metadata.

### Tyre original acquisition manifest — SRC-d09376951e70

Original source: Tyre original acquisition manifest (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/acquisition.json`)

Summary: Individual original URLs, actual retrieval outcomes, content types, times, local paths, hashes and source summaries; requested and actual model identities kept distinct.

Evidence: executed_source_acquisition.

### Tyre manufacturer geometry review — SRC-da905bba09d5

Original source: Tyre manufacturer geometry review (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/source-review.md`)

Summary: Separates the exact 6PR manual row, different 4PR brochure row and undimensioned family photo; identifies the bead/section input required for construction.

Evidence: executed_source_review.

### Exact tyre manual page rendering — SRC-847a7f8f1a9a

Original source: Exact tyre manual page rendering (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/trelleborg-technical-manual-pdf-page-111.png`)

Summary: Full PDF page 111, printed 220–221 spread, visually inspected for the 18x8.50-8 6PR T539 row and tolerance headings.

Evidence: executed_pdf_render_and_inspection.

### Tyre pre-start actual-file lookup — SRC-e055d2981083

Original source: Tyre pre-start actual-file lookup (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/existing-model-start.json`)

Summary: Fresh lookup finds no matching tyre 3D file among the project model/reference inventory; completed models remain reuse inputs.

Evidence: executed_filesystem_start_check.

### Initial tyre source job — SRC-8a8c1be024b8

Original source: Initial tyre source job (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-job-r01.json`)

Summary: Existing recorded envelope dimensions and rim designation with a named required section-profile input.

Evidence: implementation_data_artifact.

### Tyre source job bound to original manual — SRC-d5b677175f7e

Original source: Tyre source job bound to original manual (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-job-r02.json`)

Summary: Rebinds OD, width and rim designation to the exact downloaded manufacturer row; preserves source tolerances and the initial revision.

Evidence: implementation_data_artifact.

### Initial tyre input gate — SRC-3824e4bbeff1

Original source: Initial tyre input gate (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/readiness-r01.json`)

Summary: Existing requirement checker reports the named bead/section requirement before original-manual source review.

Evidence: executed_input_validation.

### Reviewed tyre input gate — SRC-68e0a74a126a

Original source: Reviewed tyre input gate (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/readiness-r02.json`)

Summary: Reviewed dimensional sources pass their hash bindings; the bead/section requirement remains the construction input question.

Evidence: executed_input_validation.

### OCS state before tyre work — SRC-275835f08b76

Original source: OCS state before tyre work (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/initial-state.json`)

Summary: Read-only state inspection preserves existing open drawings and establishes the native session for a later source-ready build.

Evidence: executed_native_state_read.

### Tyre source-stage result — SRC-281cdf03a461

Original source: Tyre source-stage result (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/result.json`)

Summary: Source review completed; component state NEEDS_INPUT for its bead/section geometry. No native geometry operation was performed.

Evidence: executed_source_stage_result.

### Tyre source-stage execution report — SRC-c1d36f59f5e8

Original source: [Tyre source-stage execution report](../../execution/c001-tyre-source-2026-11-13.md)

Summary: Documents actual exact-variant evidence, source gate, completed lookup and coordinator/research identities.

Evidence: executed_verification_report.

### Installed OCS CIRCLE command declaration — SRC-38d1476f2f41

Original source: Installed OCS CIRCLE command declaration (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/command-circle.json`)

Summary: Read installed CIRCLE command schema during source-stage preflight; declaration retained separately from construction execution.

Evidence: executed_native_capability_read.

### Installed OCS TORUS command declaration — SRC-c54dec652b41

Original source: Installed OCS TORUS command declaration (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/command-torus.json`)

Summary: Read installed TORUS command schema during source-stage preflight; declaration retained separately from construction execution.

Evidence: executed_native_capability_read.

### Installed OCS REVOLVE command declaration — SRC-d199c522d4c1

Original source: Installed OCS REVOLVE command declaration (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/command-revolve.json`)

Summary: Read installed REVOLVE command schema during source-stage preflight; declaration retained separately from construction execution.

Evidence: executed_native_capability_read.

## TDK converter source stage — 13 November 2026

### TDK Product Center exact-part page — I1C2W010A120V-000-R — SRC-9f5f0a78c8a0

Source: [TDK Product Center exact-part page — I1C2W010A120V-000-R](https://product.tdk.com/en/search/power/switching-power/dc-dc-converter/info?part_no=I1C2W010A120V-000-R)

Summary: The exact-part product page lists a manufacturer 3D STEP outline. The STEP link resolves to i1c_000_001.stp. The manufacturer's usage restrictions state that the 3D data is for internal company use, prohibits sharing with third parties, may be simplified, and must be checked against the delivery specification before use.

Evidence: manufacturer_product_page_web_inspection.

### TDK Product Center i1C technical data and STEP association — SRC-ec801c6b5cde

Source: [TDK Product Center i1C technical data and STEP association](https://product.tdk.com/en/search/power/switching-power/dc-dc-converter/tec_data/ps_i1c)

Summary: The technical-data table associates shared STEP file i1c_000_001.stp with base model I1C2W010A120V options -000-R and -001-R. The separate -004-R/-005-R pair links i1c_004_005.stp, consistent with the different pin-length option. The table explains that CAD files are compressed.

Evidence: manufacturer_technical_data_web_inspection.

### TDK i1C shared STEP outline for -000-R / -001-R — SRC-51f1aab9e632

Source: [TDK i1C shared STEP outline for -000-R / -001-R](https://product.tdk.com/system/files/dam/doc/product/power/switching-power/dc-dc-converter/3doutline_step/i1c_000_001.stp)

Summary: TDK explicitly links this STEP to both I1C2W010A120V-000-R and -001-R. It is a shared outline for variants with the same package and pin geometry. TDK does not expose a different official host for the same STEP. No STEP bytes were retained or geometrically inspected locally.

Evidence: manufacturer_step_listed_but_not_downloaded.

### TDK i1C Series specification — mechanical drawing — SRC-46710b5f460b

Source: [TDK i1C Series specification — mechanical drawing](https://product.tdk.com/system/files/dam/doc/product/power/switching-power/dc-dc-converter/specification/i1c_spec.pdf)

Summary: The mechanical drawing covers -00x-R options and states dimensions in mm [in]. Exact -000-R pin length comes from the option table. The drawing provides footprint, nominal body height, six pin diameters, pin-view order, pitch callouts and keepout callouts. Direct drawing bytes were not retained locally.

Evidence: manufacturer_specification_web_inspection.

### TDK-Lambda EMEA i1C product and CAD listing — SRC-f03a1d26c3a0

Source: [TDK-Lambda EMEA i1C product and CAD listing](https://www.emea.lambda.tdk.com/uk/products/i1c)

Summary: The regional page independently lists the i1C Datasheet and i1C 3D Drawing (STEP file). Its STEP download resolves to the same Product Center asset, not a different file host.

Evidence: manufacturer_regional_catalog_route_web_inspection.

### TDK-Lambda EMEA 3D drawings library — SRC-cb9f7650a8ea

Source: [TDK-Lambda EMEA 3D drawings library](https://www.emea.lambda.tdk.com/dk/technical-data/data?resource=3D-Drawings)

Summary: The official regional 3D drawing catalog routes to the same i1c_000_001.stp Product Center URL.

Evidence: manufacturer_catalog_route_web_inspection.

### DigiKey exact-part listing and CAD model route — SRC-742ac0b5bd12

Source: [DigiKey exact-part listing and CAD model route](https://www.digikey.com/en/products/detail/tdk-lambda/I1C2W010A120V-000-R/25281353)

Summary: The DigiKey part page identifies manufacturer part I1C2W010A120V-000-R. Its datasheet link routes to TDK's i1C series catalog PDF. Its CAD link routes to the DigiKey model page showing I1C 000 001.STP; no direct DigiKey-hosted copy of the STEP or detailed i1C specification PDF was found.

Evidence: distributor_exact_part_web_inspection.

### TDK-Lambda i1C series datasheet — SRC-277b9dcbad32

Source: [TDK-Lambda i1C series datasheet](https://www.sg.lambda.tdk.com/wp-content/uploads/i1c_e.pdf)

Summary: Manufacturer series brochure repeats the outline and top-view PCB hole pattern. The mechanical specification PDF is the more explicit source for pin diameter and exact option pin length.

Evidence: manufacturer_series_brochure_web_inspection.

### existing model start — SRC-9cdf6153dc98

Source: existing model start (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/existing-model-start.json`)

Summary: Fresh actual-file lookup identifies C046 as requiring a new model; existing completed components retain their models.

Evidence: executed_filesystem_start_check.

### result — SRC-758fb57013c6

Source: result (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/result.json`)

Summary: Names the six-pin geometry input and exact failed acquisition routes; component NEEDS_INPUT, native CAD mutations zero.

Evidence: executed_source_stage_result.

### acquisition — SRC-f4fa3d9206c2

Source: acquisition (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/acquisition.json`)

Summary: Individual manufacturer and distributor URLs, exact variant dimensions, source locators and actual HTTP/TLS/model-download outcomes.

Evidence: executed_acquisition_record.

### source review — SRC-243a0dcd9117

Source: source review (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/source-review.md`)

Summary: Separates exact -000 pin length, top-view pattern callouts and acquisition failures; no pin centers inferred from extracted text.

Evidence: delegated_source_review_record.

### tdk i1c series datasheet response headers — SRC-c04f80f53d85

Source: tdk i1c series datasheet response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/tdk-i1c-series-datasheet-response-headers.txt`)

Summary: Actual acquisition response headers for tdk i1c series datasheet response headers, retained to identify HTTP status and returned content type.

Evidence: executed_retrieval_metadata.

### tdk i1c spec response headers retry — SRC-9379662c6e30

Source: tdk i1c spec response headers retry (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/tdk-i1c-spec-response-headers-retry.txt`)

Summary: Actual acquisition response headers for tdk i1c spec response headers retry, retained to identify HTTP status and returned content type.

Evidence: executed_retrieval_metadata.

### tdk i1c spec response headers — SRC-4dd718bf4ffe

Source: tdk i1c spec response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/tdk-i1c-spec-response-headers.txt`)

Summary: Actual acquisition response headers for tdk i1c spec response headers, retained to identify HTTP status and returned content type.

Evidence: executed_retrieval_metadata.

### tdk i1c step response headers retry — SRC-9c06519d3e5d

Source: tdk i1c step response headers retry (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/tdk-i1c-step-response-headers-retry.txt`)

Summary: Actual acquisition response headers for tdk i1c step response headers retry, retained to identify HTTP status and returned content type.

Evidence: executed_retrieval_metadata.

### tdk i1c step response headers — SRC-4ead276ff16f

Source: tdk i1c step response headers (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c046-build-01/source/tdk-i1c-step-response-headers.txt`)

Summary: Actual acquisition response headers for tdk i1c step response headers, retained to identify HTTP status and returned content type.

Evidence: executed_retrieval_metadata.

### TDK converter source-stage execution report — SRC-5159849b1129

Source: [TDK converter source-stage execution report](../../execution/c046-tdk-source-2026-11-13.md)

Summary: Exact variant evidence, acquisition errors, construction input gate and next eligible component selection; coordinator and researcher identities attributed separately.

Evidence: executed_work_report.

## Orion 48/24 source stage — 13 November 2026

### Victron Orion-Tr Smart DC-DC Charger Isolated — SRC-83ad3c89cbcc

Source: [Victron Orion-Tr Smart DC-DC Charger Isolated](https://www.victronenergy.com/dc-dc-converters/orion-tr-smart)

Summary: The page offers an official STEP labeled Orion-Tr Smart Charger Isolated 12V-24V 360W. This label and associated product family do not identify ORI482438120, a 48/24-16A, 380W target. The page's target photos identify the exact product but provide no dimensioned interfaces.

Evidence: manufacturer_exact_product_page_web_inspection.

### Orion-Tr Smart Charger Isolated 12V-24V 360W — STEP — SRC-994ff56f9968

Source: [Orion-Tr Smart Charger Isolated 12V-24V 360W — STEP](https://www.victronenergy.com/upload/documents/Orion-Tr-Smart-Charger-Isolated-12V-24V-360W-%28stp%29.STEP)

Summary: Official page labels the file 12V-24V 360W Smart family. Existing STEP product labels identify Orion-Tr Smart 24-12-30A outer body and heat sink; no ORI482438120 label or exact variant mapping. Do not treat as exact C044 geometry.

Evidence: official_manufacturer_step_related_family_not_target.

### Orion-Tr Smart DC-DC Charger Isolated manual — SRC-f4c2cf5fb241

Source: [Orion-Tr Smart DC-DC Charger Isolated manual](https://www.victronenergy.com/upload/documents/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/34439-Orion-Tr_Smart_DC-DC_Charger-pdf-en.pdf)

Summary: Supports target model family and the 130 x 186 x 70 mm envelope. The exact target is not listed in the dimension drawing's model association. Do not use drawing mounting-hole or terminal dimensions as target-specific.

Evidence: manufacturer_manual_exact_electrical_model_table_and_group_envelope.

### Dimension Drawing - Orion-Large, Rev01 — SRC-3a0be7d2ba98

Source: [Dimension Drawing - Orion-Large, Rev01](https://www.victronenergy.com/upload/documents/Orion-Tr-Smart-Charger-Isolated-12V-24V-360W.pdf)

Summary: This related 12V-24V 360W drawing is already preserved in C043 source. It does not provide source-supported mounting or terminal geometry for exact target C044.

Evidence: manufacturer_related_dimension_drawing_existing_copy.

### Victron Orion-Tr Smart isolated specifications — SRC-95ac79e87962

Source: [Victron Orion-Tr Smart isolated specifications](https://www.victronenergy.com/media/pg/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/en/specifications.html)

Summary: The exact model row confirms 48V input / 24V output, 16A, 380W at 40°C. The dimensional group gives 130 x 186 x 70 mm for models without a 12V input or output. It does not show mounting or terminal geometry.

Evidence: manufacturer_manual_specification_web_inspection.

### Victron Orion-Tr Smart exact 48/24-16 product photos — SRC-83ad3c89cbcc

Source: [Victron Orion-Tr Smart exact 48/24-16 product photos](https://www.victronenergy.com/dc-dc-converters/orion-tr-smart)

Summary: The exact target product photos show external form, input/output ends and top-face arrangement. They contain no stated dimensions and cannot establish the mounting pattern.

Evidence: manufacturer_product_photo_web_inspection.

### Dimension Drawing - Orion 380W-400W isolated, Rev01 — SRC-536366b54ef5

Source: [Dimension Drawing - Orion 380W-400W isolated, Rev01](https://www.victronenergy.com/upload/documents/DimensionDrawing-Orion-Tr-%28380-400W%29.pdf)

Summary: Drawing lists ORI482441110, the non-Smart 48/24-16 model, not ORI482438120. It is not used to attribute mounting features to C044.

Evidence: manufacturer_non_smart_drawing_excluded.

### existing model start — SRC-e35b2a1b7a0c

Source: existing model start (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c044-build-01/existing-model-start.json`)

Summary: Fresh inventory identifies C044 as NEW_MODEL_REQUIRED; 43 model/reference files checked.

Evidence: executed_filesystem_start_check.

### initial state — SRC-9f8bf013cc70

Source: initial state (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c044-build-01/initial-state.json`)

Summary: Read-only OCS session and document state before source-qualified converter work.

Evidence: executed_native_state_read.

### prior model hashes — SRC-bbc7e71e7aa0

Source: prior model hashes (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c044-build-01/prior-model-hashes.json`)

Summary: Hashes of all 26 prior final DWGs retained before the new component source stage.

Evidence: executed_existing_model_hashes.

### result — SRC-921d733e06a7

Source: result (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c044-build-01/result.json`)

Summary: Names the exact-model mounting/terminal input gate and source-family mismatch; CAD mutations zero.

Evidence: executed_source_stage_result.

### acquisition — SRC-bc97944dd4fa

Source: acquisition (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c044-build-01/source/acquisition.json`)

Summary: Original URLs, reused source bytes and hashes, exact model associations, manual envelope and actual web-inspection attribution.

Evidence: executed_source_review_record.

### source review — SRC-a2878ff6a7f7

Source: source review (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c044-build-01/source/source-review.md`)

Summary: Manufacturer source findings separate the exact Smart target from listed 12/24 V variants and the non-Smart drawing.

Evidence: delegated_source_review_record.

### c044 orion source 2026 11 13 — SRC-3cbd18cb5a50

Source: [c044 orion source 2026 11 13](../../execution/c044-orion-source-2026-11-13.md)

Summary: Execution report identifies source reuse, target attribution, component state and next sequential selection.

Evidence: executed_work_report.

## Parallel wheel work launch — 13 November 2026

### Parallel wheel work dispatch — SRC-471f14ab2093

Source: [Parallel wheel work dispatch](../../execution/wheel-parallel-2026-11-13/launch.md)

Summary: Records three explicitly authorized concurrent tyre/rim/hub source and construction-readiness assignments, their disjoint paths, local-first checks and single native writer.

Evidence: executed_agent_dispatch.

### Existing exact tyre source-stage result — SRC-281cdf03a461

Source: Existing exact tyre source-stage result (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/result.json`)

Summary: Prior manufacturer source review and bead/section input gate reused by the running tyre assignment.

Evidence: inspected_local_executed_result.

### Existing steel rim findings — SRC-b817b2002bf4

Source: Existing steel rim findings (`${FERME_ROOT}/research/wheel-mount-battery-details-2026-11-12/01-steel-rims.md`)

Summary: Exact Keiyama and Knott rim identities, wheel-mount interface and separate hole/seat variants reused for the running rim assignment.

Evidence: inspected_local_research.

### Existing wheel hub and shaft findings — SRC-a84a21f49930

Source: Existing wheel hub and shaft findings (`${FERME_ROOT}/research/wheel-mount-battery-details-2026-11-12/02-hubs-shafts-bearings-brakes.md`)

Summary: Named hub, shaft, bearing and brake component interfaces and route alternatives reused by the running hub/adapter assignment.

Evidence: inspected_local_research.

## Wheel interface source results — 13 November 2026

### Tyre profile source review — SRC-5d76e97c65ab

Source: [Tyre profile source review](../../execution/wheel-parallel-2026-11-13/tyre/README.md)

Summary: Reuses exact T539 table; records mating rim references, section input gate, nominal envelope frame and source version discrepancy.

Evidence: delegated_source_review.

### Tyre source records — SRC-edf64ae7a4e8

Source: [Tyre source records](../../execution/wheel-parallel-2026-11-13/tyre/source-records.json)

Summary: Original Continental/Petlas URLs, observed claims, existing Trelleborg original hash and flange-width source discrepancy.

Evidence: executed_source_registration.

### Tyre source-stage progress — SRC-6c9455412f0c

Source: [Tyre source-stage progress](../../execution/wheel-parallel-2026-11-13/tyre/progress.json)

Summary: Actual C001 start-gate result, source-stage completion and separate component input-gate state; no CAD mutation.

Evidence: executed_source_stage_result.

### Exact rim source review — SRC-36b728154357

Source: [Exact rim source review](../../execution/wheel-parallel-2026-11-13/rims/report.md)

Summary: Keiyama/Knott identities, separate fixing seats, standardized profile references and product-section input questions.

Evidence: delegated_source_review.

### Rim geometric handoff — SRC-bfe15fc3a1f9

Source: [Rim geometric handoff](../../execution/wheel-parallel-2026-11-13/rims/geometry-handoff.json)

Summary: Named dimensions, units/frame, mounting pattern and per-product partial source coverage with construction handoff.

Evidence: implementation_input_artifact.

### Rim source observations — SRC-8e40f450fc7f

Source: [Rim source observations](../../execution/wheel-parallel-2026-11-13/rims/sources.csv)

Summary: Exact supplied/canonical URLs, observed date and actual web-inspection evidence; originals not acquired in this stage.

Evidence: executed_source_registration.

### Rim source-stage progress — SRC-e996f690d362

Source: [Rim source-stage progress](../../execution/wheel-parallel-2026-11-13/rims/progress.json)

Summary: Two component-specific new-model checks and partial-source construction state.

Evidence: executed_source_stage_result.

### Wheel hub and shaft source/action review — SRC-4e988ebfcaad

Source: [Wheel hub and shaft source/action review](../../execution/wheel-parallel-2026-11-13/hubs/source-and-actions.md)

Summary: Six distinct file gates, source-derived PRO ring/mount patterns, actual PBR50T/BT followup findings and feature-specific work orders.

Evidence: delegated_source_review.

### Hub and adapter source-stage progress — SRC-fab209186151

Source: [Hub and adapter source-stage progress](../../execution/wheel-parallel-2026-11-13/hubs/progress.json)

Summary: Per-component file identity/candidate decisions, supported interfaces and exact remaining source conditions.

Evidence: executed_source_stage_result.

### Coordinator wheel source integration — SRC-1a944a3da043

Source: [Coordinator wheel source integration](../../execution/wheel-parallel-2026-11-13/integration.md)

Summary: Summarizes the distinct source-ready wheel interfaces, input gates, source statuses, preserved completed models and subsequent active implementation assignments.

Evidence: executed_integration_report.

### Agricultural tyre/rim table, Continental Agricultural Databook — SRC-36eb88cc0cf7

Source: [Agricultural tyre/rim table, Continental Agricultural Databook](https://www.continental-tyres.co.uk/content/dam/conti-tires-cms/continental/b2b/agriculture/Continental__AG__Databook__A4__EN__copy.pdf.coredownload.pdf)

Summary: Observed source claims: {"rim_contour": "7.00I", "rim_type": "5° drop-center symmetric", "specified_width_A_mm": 178, "flange_height_G_mm": 16, "minimum_flange_width_Bmin_mm": 10, "minimum_bead_seat_width_Pmin_mm": 23}; locator: Printed page 87, section 5° Drop-Center Symmetric, 7.00I row and adjacent rim contour diagram

Evidence: web_inspection.

### Tire Guide, Industrial & OTR Tires, Petlas — SRC-a9a1c5e60bf3

Source: [Tire Guide, Industrial & OTR Tires, Petlas](https://www.petlas.com/en/powerguid/)

Summary: Observed source claims: {"rim_contour": "7.00I", "specified_width_A_mm": 178, "flange_height_G_mm": 16, "minimum_bead_seat_width_Pmin_mm": 23, "nominal_rim_code": 8, "rim_diameter_D_mm": 202.4}; locator: RIMS / 5° Drop-Centre Rim - DD(L) Rim Contour table; Semi-drop & divided rim table; Rim Diameters table

Evidence: web_inspection.

### Trelleborg Technical Manual — SRC-40bcecc74df2

Source: [Trelleborg Technical Manual](https://www.trelleborg-tires.com/-/media/tires-aft/datatsheet/technical-manual/trelleborg-technical-manual-en.pdf?hash=AB0C897622FFD6443624A33BDFA5552E&rev=258948143820400e9a05c5a63b8c7ae0&sc_lang=en)

Summary: Observed source claims: {"rim_contour": "7.00I", "permitted_rim": "6.50-8", "outside_diameter_mm": 466, "outside_diameter_tolerance_percent": 1.5, "section_width_mm": 222, "section_width_tolerance_percent": 2, "rolling_circumference_mm": 1384, "rolling_circumference_tolerance_percent": 2.5, "maximum_air_pressure_bar": 2.8, "maximum_load_kg": 475, "speed_km_h": 30}; locator: PDF page 111; printed page 221; 18x8.50-8, 6PR, T539, Farming row

Evidence: existing_downloaded_original_and_source_review.

### Continental Technical Data Book — Agriculture, printed p. 84 — SRC-f002508a1eb2

Source: [Continental Technical Data Book — Agriculture, printed p. 84](https://prod.continental-tires.com/content/dam/conti-tires-cms/continental/b2b/agriculture/CO_TechnicalDataBook_PDF_EN_CS.pdf.coredownload.pdf)

Summary: Manufacturer table for7.00I nominal rim contour dimensions; version-specific flange-width minimum retained.

Evidence: web_inspected_source_claim.

### Petlas Tire Guide — Industrial & OTR Tires — SRC-a9a1c5e60bf3

Source: [Petlas Tire Guide — Industrial & OTR Tires](https://www.petlas.com/en/powerguid/)

Summary: Manufacturer rim reference tables for7.00I width/flange/bead-seat values and nominal diameter code8.

Evidence: web_inspected_source_claim.

### Knott rim 7.00Ix8 item 402386.001 — SRC-26778a23c9b6

Source: [Knott rim 7.00Ix8 item 402386.001](https://www.knott-trailer-shop.com/rim_7_00ix8.html)

Summary: Exact Knott402386.001 product listing for7.00Ix8,4x100,Ø60,ET0 and D12 spherical-seat fasteners.

Evidence: web_inspected_source_claim.

### Keiyama JA08-700-4T100-02 steel rim — SRC-da99f2ecb321

Source: [Keiyama JA08-700-4T100-02 steel rim](https://www.keiyama.eu/jante-nue-agraire-acier-grise-700x8-et0-4-trous-60x100.html)

Summary: Exact KeiyamaJA08-700-4T100-02 listing for7x8,4x100,Ø60,ET0 andØ13.5 fixing/Ø11.3 valve holes.

Evidence: web_inspected_source_claim.

<a id="src-0ee6f66e73f1"></a>

## SRC-0ee6f66e73f1 — Existing isolated skill installation suite

Original source: [${MODELING_ROOT}/tests/test_skill_packages.py](../../tests/test_skill_packages.py)

Summary: Reused actual local CLI copy installations, isolated Python environments, local-link and import checks, intake/DXF fixtures and optional state check.

Evidence: local_source_inspected_and_reused.

Documents: research/sources/skill-completion-gate-2026-11-13.json, execution/skill-completion-gate-2026-11-13.md, docs/skill-packaging.md, skills/cad-ocs-engineering/references/package-completion.md.

<a id="src-2a5b2783d970"></a>

## SRC-2a5b2783d970 — Saved nominal free washer M5-2H

Original source: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c076-build-01/configurations/M5-2H/result-r01.json`

Summary: Executed source-bound revolution; six saved cone/body geometry checks, source metadata and point persistence passed. Both owned documents closed. Individual source dimensions remain in the external job.

Evidence: executed_native_geometry_and_persistence_result.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-2b01d57fa463"></a>

## SRC-2b01d57fa463 — Saved nominal free washer M6-2L

Original source: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c076-build-01/configurations/M6-2L/result-r01.json`

Summary: Executed source-bound revolution; six saved cone/body geometry checks, source metadata and point persistence passed. Both owned documents closed. Individual source dimensions remain in the external job.

Evidence: executed_native_geometry_and_persistence_result.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-387295c13815"></a>

## SRC-387295c13815 — Conical-washer package integration

Original source: [${MODELING_ROOT}/execution/conical-washer-package-checks-2026-11-13.json](../../execution/conical-washer-package-checks-2026-11-13.json)

Summary: Current merged cad-ocs-engineering package includes the helper and procedure; five isolated package tests passed and optional live OCS test skipped. Generated files match committed canonical source.

Evidence: executed_package_checks.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-4ef2a718e505"></a>

## SRC-4ef2a718e505 — Conical free-washer implementation

Original source: [${MODELING_ROOT}/scripts/conical_washer_profile.py](../../scripts/conical_washer_profile.py)

Summary: Validates external source dimensions and solves the unique supported shallow strip geometry; constructs by existing revolution and verifies saved conical surfaces and metadata.

Evidence: implementation_artifact.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-4f408aece302"></a>

## SRC-4f408aece302 — Conical washer modeling procedure

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/conical-washer-profile.md](../../skills/cad-ocs-engineering/references/conical-washer-profile.md)

Summary: Records exact source dimension directions, supported shallow branch, source/loaded height separation, native cone checks, persistence and completed-document closure.

Evidence: documented_procedure.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-668e7636873a"></a>

## SRC-668e7636873a — Existing installed package checker

Original source: [${MODELING_ROOT}/scripts/package_check.py](../../scripts/package_check.py)

Summary: Reused packaged hashes, isolated imports, pinned dependencies and optional read-only OCS state check; kept CAD-only runtime imports conditional.

Evidence: local_source_inspected_and_reused.

Documents: research/sources/skill-completion-gate-2026-11-13.json, execution/skill-completion-gate-2026-11-13.md, docs/skill-packaging.md, skills/cad-ocs-engineering/references/package-completion.md.

<a id="src-7246d756742b"></a>

## SRC-7246d756742b — Saved nominal free washer M5-2L

Original source: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c076-build-01/configurations/M5-2L/result-r01.json`

Summary: Executed source-bound revolution; six saved cone/body geometry checks, source metadata and point persistence passed. Both owned documents closed. Individual source dimensions remain in the external job.

Evidence: executed_native_geometry_and_persistence_result.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-76a35b7a97b4"></a>

## SRC-76a35b7a97b4 — Saved nominal free washer M6-2H

Original source: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c076-build-01/configurations/M6-2H/result-r01.json`

Summary: Executed source-bound revolution; six saved cone/body geometry checks, source metadata and point persistence passed. Both owned documents closed. Individual source dimensions remain in the external job.

Evidence: executed_native_geometry_and_persistence_result.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-bb12be45b6cf"></a>

## SRC-bb12be45b6cf — Existing skill package builder

Original source: [${MODELING_ROOT}/scripts/build_skill_packages.py](../../scripts/build_skill_packages.py)

Summary: Reused source discovery, per-package copying and source/hash manifests; extended registration, dependency traversal and completion gates.

Evidence: local_source_inspected_and_reused.

Documents: research/sources/skill-completion-gate-2026-11-13.json, execution/skill-completion-gate-2026-11-13.md, docs/skill-packaging.md, skills/cad-ocs-engineering/references/package-completion.md.

<a id="src-d03221452d4f"></a>

## SRC-d03221452d4f — Current component development workflow

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/SKILL.md](../../skills/cad-ocs-engineering/SKILL.md)

Summary: Added mandatory package completion and validation before recording a reusable tooling improvement complete.

Evidence: local_source_inspected_and_reused.

Documents: research/sources/skill-completion-gate-2026-11-13.json, execution/skill-completion-gate-2026-11-13.md, docs/skill-packaging.md, skills/cad-ocs-engineering/references/package-completion.md.

<a id="src-e867218640dd"></a>

## SRC-e867218640dd — Synthetic conical washer tests

Original source: [${MODELING_ROOT}/tests/test_conical_washer_profile.py](../../tests/test_conical_washer_profile.py)

Summary: Ten passing tests cover independent forward-generated section geometry, source hash/root resolution, normal thickness and area invariants, invalid/ambiguous inputs, guarded construction and native inspection epochs.

Evidence: executed_synthetic_tests.

Documents: research/sources/conical-washer-profile-2026-11-13.json, execution/conical-washer-profile-2026-11-13.md.

<a id="src-00583f58b6df"></a>

## SRC-00583f58b6df — Envelope reference

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/envelope-reference.md](../../skills/cad-ocs-engineering/references/envelope-reference.md)

Summary: Use `${SKILL_ROOT}/scripts/envelope_reference.py` when the source supports an overall product or clearance envelope and a detailed component body is not available. The output is one axis-aligned reference volume. It carries no implied PCB outline, mounting surface, connector locations or physical construction.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-073a85efa0cf"></a>

## SRC-073a85efa0cf — Source variant table

Original source: [${MODELING_ROOT}/scripts/source_variant_table.py](../../scripts/source_variant_table.py)

Summary: Select one value from a reviewer-transcribed variant comparison table.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-09518fd8874a"></a>

## SRC-09518fd8874a — Existing bearing

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/existing-bearing.md](../../skills/cad-ocs-engineering/references/existing-bearing.md)

Summary: Executed case: [SKF SY20TF iteration](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/c009-bearing.md). Runtime: gpt-6.1-sol, 12 November 2026.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-09a3bbda44d7"></a>

## SRC-09a3bbda44d7 — Component procedure

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/component-procedure.md](../../skills/cad-ocs-engineering/references/component-procedure.md)

Summary: 1. **Index reading:** `scripts/part_index.py` accepts explicit `--index` paths. It reads a FERME-style component list or an existing dictionary with `entries`. `--id` selects an exact identity; `--query` matches all supplied case-insensitive text terms in the original record. Returned rows retain record kind, source path, source SHA-256 and original fields.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-194f723b82c9"></a>

## SRC-194f723b82c9 — Tabbed battery

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/tabbed-battery.md](../../skills/cad-ocs-engineering/references/tabbed-battery.md)

Summary: Executed case: BMW i3 94 Ah saved exterior (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c022-reuse-02/source-job.json`). Model: gpt-6.1-sol.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-1d565b48e952"></a>

## SRC-1d565b48e952 — Envelope job runner

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/envelope-job-runner.md](../../skills/cad-ocs-engineering/references/envelope-job-runner.md)

Summary: Use `scripts/envelope_job_runner.py` to run an external, source-pinned envelope job through the existing OCS `Client`, `Journal`, `envelope_reference`, `source_metadata`, and `save_reopen` APIs. Component names, source values, request namespace, output path, and scope stay in the caller's job directory. The generic runner contains no product identifiers or dimensions.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-1d84d83da1e5"></a>

## SRC-1d84d83da1e5 — Small bms

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/small-bms.md](../../skills/cad-ocs-engineering/references/small-bms.md)

Summary: The official Rev00 dimension drawing identifies `BMS400100300 smallBMS NG`, states millimetres, and gives the housing envelope as 107 × 46 × 23 mm. Its mounting detail gives 97 mm slot-axis pitch, 12 mm slot-end-arc centre separation, `R1.75 (4x)`, and 3 mm mounting-foot thickness. The STEP AP214 file is linked from the same official product page and contains nine placed solids inside thirteen block references. Preserve the drawing values as source claims and record the STEP member names and coordinates as separate model observations.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-2299f268daed"></a>

## SRC-2299f268daed — Dimension limits and datums

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/dimension-limits-and-datums.md](../../skills/cad-ocs-engineering/references/dimension-limits-and-datums.md)

Summary: Use a source callout as a dimensional limit when its label includes `Max`, `Min`, or another explicit bound. Preserve the bound in metadata and checks. A clearance-reference volume may use the bound as its limit surface, but its solid thickness or envelope is not a claim that the manufactured part equals that bound.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-2552764ce2c1"></a>

## SRC-2552764ce2c1 — Hexagonal reference

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/hexagonal-reference.md](../../skills/cad-ocs-engineering/references/hexagonal-reference.md)

Summary: Use `scripts/hexagonal_reference.py` when an external component job supplies a regular hexagonal across-flats dimension and axial height. The helper creates one six-sided prism reference with the caller's placement frame. A caller may add a source-dimensioned coaxial through-bore by binding a required diameter feature; a nominal thread designation by itself remains axis metadata.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-25547b53182a"></a>

## SRC-25547b53182a — Assembly units

Original source: [${MODELING_ROOT}/scripts/assembly_units.py](../../scripts/assembly_units.py)

Summary: Plan a drawing-unit change for explicit native assembly root inserts.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-27305c93cb67"></a>

## SRC-27305c93cb67 — Profile reference

Original source: [${MODELING_ROOT}/scripts/profile_reference.py](../../scripts/profile_reference.py)

Summary: Build and inspect a source-traced polygon extruded as a reference volume.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-2c4d624166ce"></a>

## SRC-2c4d624166ce — Verification

Original source: [${MODELING_ROOT}/scripts/cadtools/verification.py](../../scripts/cadtools/verification.py)

Summary: Offline feature checks and explicit live save/reopen checks.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-2d515a15b8e7"></a>

## SRC-2d515a15b8e7 — Document cleanup

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/document-cleanup.md](../../skills/cad-ocs-engineering/references/document-cleanup.md)

Summary: Use `scripts/ocs_document_cleanup.py` after a component model has passed its save/reopen persistence checks. The helper returns a separate cleanup result; it never changes the component's completed model status.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-2d89ba45ac89"></a>

## SRC-2d89ba45ac89 — Small bms

Original source: [${MODELING_ROOT}/scripts/small_bms.py](../../scripts/small_bms.py)

Summary: Source-recorded smallBMS assembly persistence checks.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-31b9e4edfeca"></a>

## SRC-31b9e4edfeca — Manufacturer assembly

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/manufacturer-assembly.md](../../skills/cad-ocs-engineering/references/manufacturer-assembly.md)

Summary: Executed case: Victron BAT524110620 battery (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c023-build-01/result.json`). Coordinator/model: gpt-6.1-sol. Reusable implementation: [step_placements.py](../scripts/step_placements.py), with the existing [native ACIS reader](../scripts/native_acis.py).

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-463c9a6ee135"></a>

## SRC-463c9a6ee135 — Annular reference

Original source: [${MODELING_ROOT}/scripts/annular_reference.py](../../scripts/annular_reference.py)

Summary: Build and check a source-bound annular solid reference.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-4b20bd4fb621"></a>

## SRC-4b20bd4fb621 — Shared feature checks

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/shared-feature-checks.md](../../skills/cad-ocs-engineering/references/shared-feature-checks.md)

Summary: Executed evidence: [driver iteration](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/c012-driver.md), [Leaf module iteration](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/c021-leaf-module.md). Code: [feature_checks.py](../scripts/feature_checks.py).

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-4b9adca071bd"></a>

## SRC-4b9adca071bd — Envelope reference

Original source: [${MODELING_ROOT}/scripts/envelope_reference.py](../../scripts/envelope_reference.py)

Summary: Build and inspect a source-dimensioned axis-aligned reference envelope.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-4c498075e81e"></a>

## SRC-4c498075e81e — Ocs runtime

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/ocs-runtime.md](../../skills/cad-ocs-engineering/references/ocs-runtime.md)

Summary: 1. **Software:** Python 3.12 on Linux or macOS, the pinned packages in [requirements.txt](../requirements.txt), and an already-running OpenCADStudio native-control session. The transport uses a local TCP socket and the existing session descriptor. It reads the session's authentication token privately.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-508abf022105"></a>

## SRC-508abf022105 — Pixhawk

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/pixhawk.md](../../skills/cad-ocs-engineering/references/pixhawk.md)

Summary: Use this procedure for C052 when the currently retained source is the Holybro

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-5866f70afb27"></a>

## SRC-5866f70afb27 — Calibrated trace

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/calibrated-trace.md](../../skills/cad-ocs-engineering/references/calibrated-trace.md)

Summary: Use `scripts/calibrated_trace.py` when reconstructing external geometry from a dimensioned raster drawing and no manufacturer 3D CAD is available. The helper receives source pixel points, a pixel origin, signed per-axis scale, point-pick/origin/scale uncertainties, and optional coordinate units. It returns source pixels, mapped coordinates, and a conservative per-axis worst-case interval. It performs no image tracing and does not choose datums, dimensions, units, or geometry.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-5fdb93056178"></a>

## SRC-5fdb93056178 — Toroidal reference

Original source: [${MODELING_ROOT}/scripts/toroidal_reference.py](../../scripts/toroidal_reference.py)

Summary: Construct and inspect source-bound circular-section torus references.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-60725e76bcc2"></a>

## SRC-60725e76bcc2 — Ocs control

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/ocs-control.md](../../skills/cad-ocs-engineering/references/ocs-control.md)

Summary: Initial live evidence: OCS 2026.42, Linux, 2026-10-20. Native control works even without MCP tools exposed in this chat. Existing session descriptors under OCS configuration (normal or Snap) contain a session ID, local port and private token. Never print tokens. Do not launch another editor/headless process or change connection settings to evade a connection failure.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-64b83159bd9a"></a>

## SRC-64b83159bd9a — Hexagonal reference

Original source: [${MODELING_ROOT}/scripts/hexagonal_reference.py](../../scripts/hexagonal_reference.py)

Summary: Construct and verify a source-bound regular hexagonal prism reference.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-694cbef94f11"></a>

## SRC-694cbef94f11 — Source perimeter chains

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/source-perimeter-chains.md](../../skills/cad-ocs-engineering/references/source-perimeter-chains.md)

Summary: Use this procedure when a technical drawing stores a projected outline as separate vector paths and a source-traced profile reference needs one closed boundary. Keep the source drawing, vector extraction, trace, and constructed profile as separate records.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-70ca2e222888"></a>

## SRC-70ca2e222888 — Computational engineering

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/computational-engineering.md](../../skills/cad-ocs-engineering/references/computational-engineering.md)

Summary: Read for actual equations, procedural geometry or solver preparation. This reference installs nothing and selects no model fidelity.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-76d4d724e45e"></a>

## SRC-76d4d724e45e — Retained artifacts

Original source: [${MODELING_ROOT}/scripts/retained_artifacts.py](../../scripts/retained_artifacts.py)

Summary: Verify an external retained-file manifest without changing its artifacts.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-78b4c1846983"></a>

## SRC-78b4c1846983 — Pixhawk

Original source: [${MODELING_ROOT}/scripts/pixhawk.py](../../scripts/pixhawk.py)

Summary: Build and check the source-dimensioned Pixhawk 6C mechanical envelope.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-7a2c10dcacbb"></a>

## SRC-7a2c10dcacbb — Source first and tube

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/source-first-and-tube.md](../../skills/cad-ocs-engineering/references/source-first-and-tube.md)

Summary: Observed case: main frame longitudinal rail (P01), 12 November 2026. Executing model: gpt-6.1-sol. [Execution evidence](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/p01-rail-build.md).

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-7acf2b76d395"></a>

## SRC-7acf2b76d395 — Ocs control

Original source: [${MODELING_ROOT}/scripts/ocs_control.py](../../scripts/ocs_control.py)

Summary: Existing-session OCS native control. Discovery/read default; explicit guarded writes.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-7f29357f014b"></a>

## SRC-7f29357f014b — Profile reference

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/profile-reference.md](../../skills/cad-ocs-engineering/references/profile-reference.md)

Summary: Use `scripts/profile_reference.py` when an external project supplies a closed, straight-segment profile trace and a source-defined extrusion depth for a reference volume. This representation can preserve a manufacturer-view silhouette for packaging or clearance work. It does not infer curved edges, hidden features, wall thickness or manufacturing construction.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-8407d03dcbf7"></a>

## SRC-8407d03dcbf7 — Step solid inventory

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/step-solid-inventory.md](../../skills/cad-ocs-engineering/references/step-solid-inventory.md)

Summary: Use `scripts/step_solid_inventory.py::inventory_step_solids` before comparing

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-8781126ff549"></a>

## SRC-8781126ff549 — Paths

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/paths.md](../../skills/cad-ocs-engineering/references/paths.md)

Summary: 1. `SKILL_ROOT` is the installed cad-ocs-engineering directory containing `SKILL.md`. Resolve its bundled code from `SKILL_ROOT/scripts`; keep the package intact.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-887904ceece4"></a>

## SRC-887904ceece4 — Geometry

Original source: [${MODELING_ROOT}/scripts/cadtools/geometry.py](../../scripts/cadtools/geometry.py)

Summary: OCS recipes adapted from ngv064_ocs.py and item_ocs_parts.py.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-8da213acf424"></a>

## SRC-8da213acf424 — Spherical seat profile

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/spherical-seat-profile.md](../../skills/cad-ocs-engineering/references/spherical-seat-profile.md)

Summary: 1. **Inputs:** caller-owned sphere radius and axial centre, collar radius and start station, shaft radius and tip station, and blend radius. Use one unit for all inputs. Bind printed dimensions, source approximations and calculated reconstruction points separately in the component job.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-90298e431c37"></a>

## SRC-90298e431c37 — Source metadata

Original source: [${MODELING_ROOT}/scripts/source_metadata.py](../../scripts/source_metadata.py)

Summary: Compare string metadata with an actual native entity record.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-9480873c9e5a"></a>

## SRC-9480873c9e5a — Runtime

Original source: [${MODELING_ROOT}/scripts/cadtools/runtime.py](../../scripts/cadtools/runtime.py)

Summary: Guarded OCS adapter; extracted from the inspected ocs_control/NGV workflow.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-94eb405ef343"></a>

## SRC-94eb405ef343 — Check contract

Original source: [${MODELING_ROOT}/scripts/check_contract.py](../../scripts/check_contract.py)

Summary: Check supplied geometric measurements; does not query CAD or validate physical performance.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-97262ee882c7"></a>

## SRC-97262ee882c7 — Spherical seat profile

Original source: [${MODELING_ROOT}/scripts/spherical_seat_profile.py](../../scripts/spherical_seat_profile.py)

Summary: Derive an exact circular-arc profile for a spherical-seat shaft transition.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-b02ebb04744c"></a>

## SRC-b02ebb04744c — Test source registration

Original source: [${MODELING_ROOT}/tests/test_source_registration.py](../../tests/test_source_registration.py)

Summary: Focused source-register merges preserve history and validate both indexes.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md, docs/skill-packaging.md.

<a id="src-b3ff112677ac"></a>

## SRC-b3ff112677ac — Annular reference

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/annular-reference.md](../../skills/cad-ocs-engineering/references/annular-reference.md)

Summary: Use [`annular_reference.py`](../scripts/annular_reference.py) when a component source defines a plain ring by bore diameter, outside diameter and axial thickness.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-c12bedd365cc"></a>

## SRC-c12bedd365cc — Source variant tables

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/source-variant-tables.md](../../skills/cad-ocs-engineering/references/source-variant-tables.md)

Summary: Use `${SKILL_ROOT}/scripts/source_variant_table.py` when a manufacturer or engineering table places specifications for multiple variants in adjacent columns. The helper selects one cell from an explicitly transcribed table using the exact column header and exact row label.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-c88d4b2c97ac"></a>

## SRC-c88d4b2c97ac — Package completion

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/package-completion.md](../../skills/cad-ocs-engineering/references/package-completion.md)

Summary: This development operation runs from the 3D CAD Modeling source repository root after an authorized reusable tooling change. The source repository owns `scripts/build_skill_packages.py` and its tests. The installed skill carries its runtime code.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-c8f378e73049"></a>

## SRC-c8f378e73049 — Non geometric requirements

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/non-geometric-requirements.md](../../skills/cad-ocs-engineering/references/non-geometric-requirements.md)

Summary: Use this classification only when the component input explicitly states that no CAD geometry is required. The classification is a caller-supplied job declaration; the checker does not infer it from a component name, group, prose or feature values.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-cc2786c6982f"></a>

## SRC-cc2786c6982f — Toroidal reference

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/toroidal-reference.md](../../skills/cad-ocs-engineering/references/toroidal-reference.md)

Summary: Use [`toroidal_reference.py`](../scripts/toroidal_reference.py) when a

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-cf9699adeab7"></a>

## SRC-cf9699adeab7 — Existing battery

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/existing-battery.md](../../skills/cad-ocs-engineering/references/existing-battery.md)

Summary: Executed case: [Leaf module iteration](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/c021-leaf-module.md), 12 November 2026, gpt-6.1-sol.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-d1cb0e75b1e3"></a>

## SRC-d1cb0e75b1e3 — Calibrated trace

Original source: [${MODELING_ROOT}/scripts/calibrated_trace.py](../../scripts/calibrated_trace.py)

Summary: Map source-image points into calibrated 2D coordinates with uncertainty.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-d4cb9b6ed7a6"></a>

## SRC-d4cb9b6ed7a6 — Drawing feature checks

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/drawing-feature-checks.md](../../skills/cad-ocs-engineering/references/drawing-feature-checks.md)

Summary: Use this procedure when a drawing dimension is compared with imported or reconstructed geometry.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-d864b71e4224"></a>

## SRC-d864b71e4224 — Ocs document cleanup

Original source: [${MODELING_ROOT}/scripts/ocs_document_cleanup.py](../../scripts/ocs_document_cleanup.py)

Summary: Safely close one active OCS document owned by a completed CAD job.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-e4457f692304"></a>

## SRC-e4457f692304 — Source metadata

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/source-metadata.md](../../skills/cad-ocs-engineering/references/source-metadata.md)

Summary: Use [source_metadata.py](../scripts/source_metadata.py) when verifying the string metadata written by the existing OCS `Geometry.metadata` adapter.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-e718961d3c9e"></a>

## SRC-e718961d3c9e — Step solid inventory

Original source: [${MODELING_ROOT}/scripts/step_solid_inventory.py](../../scripts/step_solid_inventory.py)

Summary: Inventory STEP solid-definition entities without counting nested shells.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-e9dc4d4b63a4"></a>

## SRC-e9dc4d4b63a4 — Envelope job runner

Original source: [${MODELING_ROOT}/scripts/envelope_job_runner.py](../../scripts/envelope_job_runner.py)

Summary: Run an external source-bound envelope job through guarded OCS APIs.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-ea5cca4068c6"></a>

## SRC-ea5cca4068c6 — Scaled assemblies

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/scaled-assemblies.md](../../skills/cad-ocs-engineering/references/scaled-assemblies.md)

Summary: Executed component: Victron Lynx Smart BMS NG 500 M10, LYN034163010. Model: gpt-6.1-sol.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-ec804e897334"></a>

## SRC-ec804e897334 — Axial motor

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/axial-motor.md](../../skills/cad-ocs-engineering/references/axial-motor.md)

Summary: Executed case: Motenergy ME0907 source job (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c005-build-01/source-job.json`). Original: [Motenergy outline 0JWT.301.073](https://eveurope.eu/wp-content/uploads/2024/03/ME0907.pdf). Reusable code: [axial_motor.py](../scripts/axial_motor.py). Runtime model: gpt-6.1-sol.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-f2991edcea4f"></a>

## SRC-f2991edcea4f — Assembly units

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/assembly-units.md](../../skills/cad-ocs-engineering/references/assembly-units.md)

Summary: Use `scripts/assembly_units.py::plan_root_unit_change` to prepare a read-only plan when an assembly root insertion converts coordinates between drawing units. Supply the complete root insert records and explicit source and destination unit mappings from the caller's job. Each mapping contains a readable `label`, an integer `code`, and `millimetres_per_drawing_unit`; codes are descriptive inputs and do not determine scale.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-f2dd7dc83962"></a>

## SRC-f2dd7dc83962 — Existing model start check

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/existing-model-start-check.md](../../skills/cad-ocs-engineering/references/existing-model-start-check.md)

Summary: 1. Run this check before every component start. It reads the external input manifest, work index, model paths, input-sheet links and files. It runs no CAD operations. Existing model paths, recorded scope and checks supply reuse evidence.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-f5a8295df542"></a>

## SRC-f5a8295df542 — Model contract

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/model-contract.md](../../skills/cad-ocs-engineering/references/model-contract.md)

Summary: Record project-specific facts, not an invented design:

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-f5b63a29220e"></a>

## SRC-f5b63a29220e — Retained artifact checks

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/retained-artifact-checks.md](../../skills/cad-ocs-engineering/references/retained-artifact-checks.md)

Summary: Use `scripts/retained_artifacts.py` after the final source/path/provenance edits and before the component result commit. It reads caller-owned files and prints a JSON result; it changes no artifact or manifest and connects to no CAD session.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-fa769befc290"></a>

## SRC-fa769befc290 — Sources and capabilities

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/sources-and-capabilities.md](../../skills/cad-ocs-engineering/references/sources-and-capabilities.md)

Summary: Original OCS-specific synthesis, research date2026-10-20. No third-party skill code/instructions were copied or installed. Archived original sources/licenses remain in the project.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-fab6a72dd382"></a>

## SRC-fab6a72dd382 — Source view evidence

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/source-view-evidence.md](../../skills/cad-ocs-engineering/references/source-view-evidence.md)

Summary: Use this procedure when a manufacturer drawing is available as a retained raster image or as a rendered page from a retained original PDF. It records how a source view supports dimensions, a traced outline, or both.

Evidence: local_artifact_inspected_and_registered.

Documents: research/sources/tooling-registration-2026-11-13.json, docs/tools.md, skills/README.md, execution/tooling-registration-2026-11-13.md.

<a id="src-a0d612cd0827"></a>

## SRC-a0d612cd0827 — Synthetic boundary decoder tests

Original source: [${MODELING_ROOT}/tests/test_native_circle_boundaries.py](../../tests/test_native_circle_boundaries.py)

Summary: Twelve passing synthetic cases cover full/partial circles, ellipses, straight curves, transforms, token layouts, nonfinite spans and invalid partner edges.

Evidence: executed_synthetic_tests.

Documents: research/sources/circular-boundary-reader-2026-11-13.json, execution/circular-boundary-reader-2026-11-13.md, skills/cad-ocs-engineering/SKILL.md.

<a id="src-429533a8f966"></a>

## SRC-429533a8f966 — Saved circular boundary procedure

Original source: [${MODELING_ROOT}/skills/cad-ocs-engineering/references/circular-boundary-checks.md](../../skills/cad-ocs-engineering/references/circular-boundary-checks.md)

Summary: Records source attribution and the graph conditions required to connect circular cap loops to cylindrical side faces across required planes.

Evidence: documented_exercised_procedure.

Documents: research/sources/circular-boundary-reader-2026-11-13.json, execution/circular-boundary-reader-2026-11-13.md, skills/cad-ocs-engineering/SKILL.md.

<a id="src-563e96314ba9"></a>

## SRC-563e96314ba9 — Saved retaining-ring circular opening checks

Original source: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c112-build-01/saved-hole-boundary-checks-r01.json`

Summary: Two source-bound circular opening checks passed through the opt-in reader, using preserved saved SAB; no CAD reopening or geometry reconstruction.

Evidence: executed_offline_native_geometry_check.

Documents: research/sources/circular-boundary-reader-2026-11-13.json, execution/circular-boundary-reader-2026-11-13.md.

<a id="src-3f52f358d61b"></a>

## SRC-3f52f358d61b — Circular boundary package completion checks

Original source: [${MODELING_ROOT}/execution/circular-boundary-package-checks-2026-11-13.json](../../execution/circular-boundary-package-checks-2026-11-13.json)

Summary: Finalize and final verify passed lifecycle, source-registration and isolated installation checks; packaged reader hash matches canonical source.

Evidence: executed_package_completion_checks.

Documents: research/sources/circular-boundary-reader-2026-11-13.json, execution/circular-boundary-reader-2026-11-13.md.

<a id="src-f36ae4007ec3"></a>

## SRC-f36ae4007ec3 — Agent Skills specification

Original source: [https://agentskills.io/specification](https://agentskills.io/specification)

Summary: Required SKILL.md metadata, name constraints and optional fields; recommended progressive disclosure and document size.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.

<a id="src-9a9e59417d11"></a>

## SRC-9a9e59417d11 — Creating skills

Original source: [https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md)

Summary: Skill discovery layouts and packaging conventions.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.

<a id="src-eea8cf0cd544"></a>

## SRC-eea8cf0cd544 — Skills CLI commands

Original source: [https://github.com/vercel-labs/skills/blob/main/docs/commands.md](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)

Summary: Repository syntax, skill selection, copy installation and project/global scope.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.

<a id="src-3888c0e32096"></a>

## SRC-3888c0e32096 — Skills CLI README

Original source: [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)

Summary: Node.js >=22.20 and npm/npx prerequisites.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.

<a id="src-05bbfa90e9fa"></a>

## SRC-05bbfa90e9fa — Skills CLI troubleshooting

Original source: [https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md)

Summary: Telemetry environment settings.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.

<a id="src-c22ddeb6403b"></a>

## SRC-c22ddeb6403b — skills.sh FAQ

Original source: [https://www.skills.sh/docs/faq](https://www.skills.sh/docs/faq)

Summary: Automatic directory listing through installation telemetry.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.

<a id="src-cf7ca0e991c1"></a>

## SRC-cf7ca0e991c1 — Skills automatic indexing issue

Original source: [https://github.com/vercel-labs/skills/issues/880](https://github.com/vercel-labs/skills/issues/880)

Summary: Collaborator antfu confirms installation telemetry indexes skills automatically.

Evidence: delegated_web_inspection_report.

Documents: research/sources/skills-compliance-2026-11-13.json, README.md, docs/index.md, docs/skill-packaging.md, execution/skills-installation-guide-2026-11-13.md.
