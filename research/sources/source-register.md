# Source register

Registered: 2026-11-12.

Each entry preserves the original URL or local source path and records its summary, evidence status and referring documents. Detailed observations are retained in [source-register.json](/home/leo/projects/3dmodeling/research/sources/source-register.json).

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

<a id="src-00e7f773e988"></a>

## SRC-00e7f773e988 — Perspective-n-Point (PnP) pose computation — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html)

Summary: OpenCV 4.13.0 documents solvePnP inputs as 3D object points, matching 2D image projections, camera intrinsic matrix and distortion coefficients. rvec/tvec transform object-frame points into camera-frame coordinates; camera axes are X right, Y down, Z forward. The page documents method-specific point-count and planarity conditions, alternative solutions returned by solvePnPGeneric, and RANSAC PnP for outliers. This is API capability evidence, not a local pose result or accuracy report.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-00ef88b61c5d"></a>

## SRC-00ef88b61c5d — Independent procedure review — Point 01 model brief

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/independent-review.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/independent-review.md)

Summary: Authored audit document recording Independent procedure review — Point 01 model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-00fe5418f4eb"></a>

## SRC-00fe5418f4eb — ocs-skill-improvements.md — proposed_skill_extension

Original source: [/home/leo/projects/ferme/skills/ocs-skill-improvements.md](/home/leo/projects/ferme/skills/ocs-skill-improvements.md)

Summary: Proposed OCS additions derived from recorded commands, topology recovery and representation/display observations. Applicability: Held in ferme; installation is a separate action.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-011e8da740e4"></a>

## SRC-011e8da740e4 — ifcopenshell.api.feature.add_feature — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `feature.add_feature(file, feature, element)` for projecting, voiding or surface features. Its example first creates a wall and its geometry, then separately creates an IfcOpeningElement, assigns opening geometry and placement, and finally calls add_feature with the existing opening and wall. For the voiding opening shown, the call returns an IfcRelVoidsElement; the documentation describes voiding features as cutting host geometry but does not specify when the Boolean geometry is evaluated. The function does not create the opening element or assign its geometry/placement; the result depends on the selected feature type. The page says semantic openings should be represented distinctly when they have their own meaning.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r10.md.

<a id="src-023374825488"></a>

## SRC-023374825488 — dom-r01.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r01.md)

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

<a id="src-03256efc5e07"></a>

## SRC-03256efc5e07 — SKILL.md

Original source: [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-0347392e2577"></a>

## SRC-0347392e2577 — BIM Library docs

Original source: [https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html](https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html)

Summary: FreeCAD BIM Library ; FreeCAD BIM can browse and insert FCStd, STEP and BREP entries from the FreeCAD Parts Library, either offline or through its experimental online library option. BIM Library docs, Parts Library repository ; The BIM insertion feature does not change the license of inserted assets. The Parts Library collection is listed as CC-BY-3.0 in FreeCAD Addons; verify individual item attribution and embedded files. Many entries are generic architecture/MEP objects, not certified building product specifications.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r07.md, research/workflows/domain-paths.md.

<a id="src-0374f064147a"></a>

## SRC-0374f064147a — pcl::SACSegmentationFromNormals<PointT, PointNT> Class Template Reference — Point Cloud Library 1.15.1-dev

Original source: [https://pointclouds.org/documentation/classpcl_1_1_s_a_c_segmentation_from_normals.html](https://pointclouds.org/documentation/classpcl_1_1_s_a_c_segmentation_from_normals.html)

Summary: The PCL API documents normal-based sample-consensus segmentation, input point cloud and normal cloud, and segment(PointIndices&, ModelCoefficients&) outputs. It describes normal-distance weighting and inherited consensus controls including method, maximum iterations, probability, distance threshold, radius limits and axis/angle constraints. This is API documentation, not a local runtime result.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-independent.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-03ea53a6f519"></a>

## SRC-03ea53a6f519 — OpenCV 4.13 Camera Calibration

Original source: [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)

Summary: Known target object coordinates and corresponding image detections support intrinsic/distortion calibration; tutorial recommends at least ten pattern views. Calibration does not set the scale of an unrelated monocular reconstruction.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-05-visual.md, research/action-audit/reviews/point-07-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r03.md.

<a id="src-04350e8a74da"></a>

## SRC-04350e8a74da — local-inventory.json

Original source: [/home/leo/projects/3dmodeling/research/local-inventory.json](/home/leo/projects/3dmodeling/research/local-inventory.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-047ea9576020"></a>

## SRC-047ea9576020 — dom-r03.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r03.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r03.md)

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

<a id="src-0724f34c3f7f"></a>

## SRC-0724f34c3f7f — reconstruction-detail-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-03/reconstruction-detail-sources.json](/home/leo/projects/3dmodeling/research/sources/round-03/reconstruction-detail-sources.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-0868c7d42c7e"></a>

## SRC-0868c7d42c7e — Point 02 visual, semantic and evidence-merge review

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-visual.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-visual.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-08989edb31e4"></a>

## SRC-08989edb31e4 — first action plan

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-0910720e555c"></a>

## SRC-0910720e555c — Point 05 independent procedure review — CAD, photographs and scans alignment

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-independent.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-096e1d7af9e5"></a>

## SRC-096e1d7af9e5 — dom-r07.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r07.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r07.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json.

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

<a id="src-0afc75d0368f"></a>

## SRC-0afc75d0368f — Blender repository/licence

Original source: [https://github.com/blender/blender](https://github.com/blender/blender)

Summary: Licence details for the upstream source, installed package and MCP integrations are recorded in domains and components. Primary sources: Blender repository/licence, Python API quickstart, Mesh API. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-0c098ecd90ed"></a>

## SRC-0c098ecd90ed — Local tool and source baseline

Original source: [/home/leo/projects/3dmodeling/research/local-baseline.md](/home/leo/projects/3dmodeling/research/local-baseline.md)

Summary: Inspected in this research turn; records OCS STEP representation finding and environment/source inspection.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-0c559ba0bc9f"></a>

## SRC-0c559ba0bc9f — Upstream COPYING

Original source: [https://github.com/blender/blender/blob/main/COPYING](https://github.com/blender/blender/blob/main/COPYING)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

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

<a id="src-10fb35c8f807"></a>

## SRC-10fb35c8f807 — Python API quickstart

Original source: [https://docs.blender.org/api/current/info_quickstart.html](https://docs.blender.org/api/current/info_quickstart.html)

Summary: Licence details for the upstream source, installed package and MCP integrations are recorded in domains and components. Primary sources: Blender repository/licence, Python API quickstart, Mesh API. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-11a3ab01c356"></a>

## SRC-11a3ab01c356 — Project workflow composition rules

Original source: [/home/leo/projects/3dmodeling/research/workflows/composition-rules.md](/home/leo/projects/3dmodeling/research/workflows/composition-rules.md)

Summary: Project proposal defining sequences, branches, evidence merges, component substitution, representation forks and revisioned edit/compare loops, with explicit handoff conditions and research questions.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/project-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-11b52766dd34"></a>

## SRC-11b52766dd34 — Local Python 3.14 hashlib source

Original source: [/usr/lib/python3.14/hashlib.py](/usr/lib/python3.14/hashlib.py)

Summary: Documented byte hashing and SHA-256 constructors used as source evidence for input revision identity.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json.

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

<a id="src-1341a6b69ecb"></a>

## SRC-1341a6b69ecb — AGENTS.md

Original source: [/home/leo/projects/ferme/AGENTS.md](/home/leo/projects/ferme/AGENTS.md)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected.

Documents: research/local-baseline.md, research/sources/local-evidence.json.

<a id="src-134b4e103e48"></a>

## SRC-134b4e103e48 — OpenMVG documentation: OpenMVS stages

Original source: [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/)

Summary: OpenMVS imports an OpenMVG scene and runs DensifyPointCloud, ReconstructMesh and TextureMesh as separate command-line stages.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r06.md.

<a id="src-13f08bab005f"></a>

## SRC-13f08bab005f — source repository/licence

Original source: [https://github.com/openscad/openscad](https://github.com/openscad/openscad)

Summary: Primary sources: official documentation, language reference, source repository/licence. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-144b4a816641"></a>

## SRC-144b4a816641 — cad-r09.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r09.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r09.md)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-158c2c4848c2"></a>

## SRC-158c2c4848c2 — AGENTS.md — energy project instructions

Original source: [/home/leo/projects/energy/AGENTS.md](/home/leo/projects/energy/AGENTS.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: AGENTS.md — energy project instructions. Source class: project research and communication instructions. Original reuse terms: Local instructions; referenced in place without duplication.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-172fdcc953c4"></a>

## SRC-172fdcc953c4 — The model contract and STEP generation

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/step-generation.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/step-generation.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: The model contract and STEP generation. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-17542ff2880d"></a>

## SRC-17542ff2880d — Project skill catalogue

Original source: [/home/leo/projects/3dmodeling/skills/README.md](/home/leo/projects/3dmodeling/skills/README.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-19255db776eb"></a>

## SRC-19255db776eb — MCP Market 3D Modeling Specialist

Original source: [https://mcpmarket.com/tools/skills/3d-modeling-specialist](https://mcpmarket.com/tools/skills/3d-modeling-specialist)

Summary: MCP Market 3D Modeling Specialist ; Listing by Kedhareswer: game/film art workflow covering quad topology, UV unwrapping, texel density, baking, retopology, LOD and Blender/Maya/ZBrush. It reports 0 GitHub stars and an install path `kedhareswer/kedhar_brain`, skill `3d-modeling`. ; Mesh/art skill, not mechanical CAD. Listing page inspected. Upstream source SKILL.md, licence and service requirements were not retrieved, so listing description is not treated as verified code behavior.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-19a03b5f035d"></a>

## SRC-19a03b5f035d — blender-modeling — roble3/cc-blender-skill

Original source: [https://www.skills.sh/roble3/cc-blender-skill/blender-modeling](https://www.skills.sh/roble3/cc-blender-skill/blender-modeling)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: blender-modeling — roble3/cc-blender-skill. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-1a05e425438e"></a>

## SRC-1a05e425438e — REP-103: Standard Units of Measure and Coordinate Conventions — ros-infrastructure/rep master

Original source: [https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst](https://github.com/ros-infrastructure/rep/blob/master/rep-0103.rst)

Summary: ROS REP source page accessed 2026-11-12. Repository page says archived October 23, 2025; REP text labels itself Active/Informational. Specifies SI metre, kilogram, second; radian; right-handed frames; body x-forward/y-left/z-up; optical z-forward/x-right/y-down. Branch is mutable.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-1a10c8033611"></a>

## SRC-1a10c8033611 — reconstruction-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-02/reconstruction-sources.json](/home/leo/projects/3dmodeling/research/sources/round-02/reconstruction-sources.json)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-1a2bd5aac217"></a>

## SRC-1a2bd5aac217 — execution record

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/execution-record.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/execution-record.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-1a9d2f4c6a7a"></a>

## SRC-1a9d2f4c6a7a — assets

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/assets.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/assets.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-1b2c3957498a"></a>

## SRC-1b2c3957498a — OCCT source repository/licence

Original source: [https://github.com/Open-Cascade-SAS/OCCT](https://github.com/Open-Cascade-SAS/OCCT)

Summary: Primary sources: official OCCT overview, OCCT source repository/licence. Inspected 2026-11-12. Commercial/proprietary uses need licence review against the exact OCCT distribution and linked components; do not assume every wrapper or dependency shares OCCT's terms.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-1be5a18aa751"></a>

## SRC-1be5a18aa751 — https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html

Original source: [https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html](https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html)

Summary: - Meshroom hardware requirements (legacy version; treat numbers as historical): https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-1bf6e9a12d73"></a>

## SRC-1bf6e9a12d73 — dom-r06.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r06.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r06.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-1f314fe4accc"></a>

## SRC-1f314fe4accc — raster_image.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/src/modules/draw/draw/raster_image.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/modules/draw/draw/raster_image.rs)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

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

<a id="src-1fe1bf3380df"></a>

## SRC-1fe1bf3380df — https://github.com/openMVG/openMVG

Original source: [https://github.com/openMVG/openMVG](https://github.com/openMVG/openMVG)

Summary: - OpenMVG repository and license: https://github.com/openMVG/openMVG

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md.

<a id="src-20a206cdbbd8"></a>

## SRC-20a206cdbbd8 — README.md — evidence_index

Original source: [/home/leo/projects/ferme/skills/README.md](/home/leo/projects/ferme/skills/README.md)

Summary: Scope, source session/review boundary, OCS build and document use order. Applicability:

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

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

<a id="src-243b037b93ab"></a>

## SRC-243b037b93ab — CAD and skills assessment

Original source: [/home/leo/projects/3dmodeling/research/cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md)

Summary: Inspected in this research turn; records OCS baseline, CAD representation tradeoffs and alternate authoring backends.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-251464b38bc3"></a>

## SRC-251464b38bc3 — CadQuery quickstart

Original source: [https://cadquery.readthedocs.io/en/stable/quickstart.html](https://cadquery.readthedocs.io/en/stable/quickstart.html)

Summary: Primary usage examples for parameterized Python solid construction.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r07.md, research/workflows/details/mix-r09.md.

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

<a id="src-2752296f9685"></a>

## SRC-2752296f9685 — point-03-operations

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-2759f46214ed"></a>

## SRC-2759f46214ed — SarahWeiii/CoACD README and repository page

Original source: [https://github.com/SarahWeiii/CoACD](https://github.com/SarahWeiii/CoACD)

Summary: Official repository page accessed 2026-11-12; mutable main branch, no commit pin inspected. README documents OBJ input, OBJ/WRL output, convex components, `-i/--input`, `-o/--output`, `-t/--threshold` default 0.05, metre-scale `-rm/--real-metric`, and `-sp/--split` individual pieces. Existing source register separately records MIT license and 2022 copyright.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r08.md.

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/execution-record.md](/home/leo/projects/3dmodeling/research/action-audit/execution-record.md)

Summary: Observed dispatch, actual identity reports, review dispositions, scope finding and source-registration integration for this authorized documentation batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-29e05b3b3047"></a>

## SRC-29e05b3b3047 — OpenCADStudio kernel body path note

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md)

Summary: Local OCS design/implementation note describes supported kernel-body paths and history limitations; it does not establish STEP analytic-surface export.

Evidence: existing_report_registered, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-05/point-03-local-sources.json.

<a id="src-2a63549fb0bc"></a>

## SRC-2a63549fb0bc — Data conventions — Nerfstudio documentation

Original source: [https://docs.nerf.studio/quickstart/data_conventions.html](https://docs.nerf.studio/quickstart/data_conventions.html)

Summary: Current Nerfstudio data-conventions page inspected 2026-11-12; release not pinned. Defines OpenGL/Blender/NeRF camera axes, +Z-up world, pixel-centre convention, transforms.json camera basis columns and origin translation. Depth images are assumed 16/32-bit millimetres, zero means unknown, and `depth_unit_scale_factor` changes scale; depth images resize to RGB by default. Page does not specify selected parser auto-orientation/scale-normalization runtime config.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-2ad28cfa19ba"></a>

## SRC-2ad28cfa19ba — Point 06 — software and API review

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-software.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-software.md)

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md](/home/leo/projects/3dmodeling/research/action-audit/point-06-building-and-robot.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-2bcc72542265"></a>

## SRC-2bcc72542265 — Geometry creation — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html)

Summary: IfcOpenShell 0.9.0post1 guide accessed 2026-11-12. Records representation creation examples and placement/unit distinction; used as background source for separating IFC geometric representation authoring from semantic product creation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/sources/round-05/point-06-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-2cf7a4eb3a5d"></a>

## SRC-2cf7a4eb3a5d — RGBDImageFactory.cpp — Open3D v0.20.0 source

Original source: [https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp)

Summary: Official raw source on tag v0.20.0 inspected 2026-11-12. `CreateFromColorAndDepth` accepts caller-provided depth_scale/depth_trunc/intensity flag, passes scale and truncation to `ConvertDepthToFloatImage`, and requires matching color/depth dimensions. Default arguments are declared in RGBDImage.h, not in this function definition.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-2d331dacc4f0"></a>

## SRC-2d331dacc4f0 — Execution plan: define one workflow point at a time

Original source: [/home/leo/projects/3dmodeling/research/action-audit/plan.md](/home/leo/projects/3dmodeling/research/action-audit/plan.md)

Summary: Authorized documentation method: fifteen fields per action, alternative software/agent modes, evidence-based merges, feature-specific accuracy and local-compute-first definition order.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-2d407c9d997c"></a>

## SRC-2d407c9d997c — point-06-operations

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-06-operations.json)

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

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r02.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r02.md)

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

<a id="src-2e92a48ed867"></a>

## SRC-2e92a48ed867 — Structural Analysis and Shape Descriptors — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html)

Summary: OpenCV 4.13.0 documents `findContours` on an 8-bit single-channel binary image; nonzero pixels are foreground and the API returns contour coordinates and hierarchy. Contours support shape analysis but are pixel-derived boundaries, not engineering feature classes.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r08.md.

<a id="src-2fad977d4fe9"></a>

## SRC-2fad977d4fe9 — /home/leo/projects/3dmodeling/research/workflows/cad-paths.json

Original source: [/home/leo/projects/3dmodeling/research/workflows/cad-paths.json](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json)

Summary: Source referenced for the stated workflow; see the owning documentation or research item.

Evidence: existing_report_registered, local_reference_registered, local_source_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-2fe2fa4714a1"></a>

## SRC-2fe2fa4714a1 — Local Python 3.14 decimal interface source

Original source: [/usr/lib/python3.14/decimal.py](/usr/lib/python3.14/decimal.py)

Summary: Decimal interface source inspected by software reviewer; official decimal documentation separately supports exact string construction.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-3018a0ce5798"></a>

## SRC-3018a0ce5798 — FreeCAD Part::TopoShape Class Reference

Original source: [https://freecad.github.io/SourceDoc/d8/ded/classPart_1_1TopoShape.html](https://freecad.github.io/SourceDoc/d8/ded/classPart_1_1TopoShape.html)

Summary: Official FreeCAD source documentation accessed 2026-11-12. General TopoShape reference lists read/write/import/export/validity APIs but did not expose mass, centre-of-mass or inertia methods in the inspected page; no mass-property claim relies on this page.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-3126762ba53b"></a>

## SRC-3126762ba53b — cad-workflow-findings.md — recorded_execution_summary

Original source: [/home/leo/projects/ferme/skills/cad-workflow-findings.md](/home/leo/projects/ferme/skills/cad-workflow-findings.md)

Summary: OCS 2026.42 component constructions, import/save results, failed requests and component-specific recoveries. Applicability: Claims are attributed to the retained reports/session identifiers; raw session replay is a separate result.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-31a38faa2037"></a>

## SRC-31a38faa2037 — Point 07 designer notes — reconstruction procedures

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-designer.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-designer.md)

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

Original source: [/tmp/opencode/build_leaf_gen2.py](/tmp/opencode/build_leaf_gen2.py)

Summary: top and staged recovery functions reconstruct shell/terminal features; finish checks and saves the component. Applicability: Component-specific dimensions and staged resumption; imports shared battery/item/wrapper/SAT modules.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-31fb748a20df"></a>

## SRC-31fb748a20df — CAD project structure

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/project-layout.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/project-layout.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: CAD project structure. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-331dc8c3567f"></a>

## SRC-331dc8c3567f — License text

Original source: [https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/LICENSE](https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/LICENSE)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: License text. Source class: repository license text. Original reuse terms: License text retained verbatim; see archived license file.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-334ea37bde4d"></a>

## SRC-334ea37bde4d — build_bmw_i3_94ah.py — existing_component_code

Original source: [/tmp/opencode/build_bmw_i3_94ah.py](/tmp/opencode/build_bmw_i3_94ah.py)

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

<a id="src-341c5dce719a"></a>

## SRC-341c5dce719a — raw source

Original source: [https://raw.githubusercontent.com/freshtechbro/claudedesignskills/main/.claude/skills/web3d-integration-patterns/SKILL.md](https://raw.githubusercontent.com/freshtechbro/claudedesignskills/main/.claude/skills/web3d-integration-patterns/SKILL.md)

Summary: freshtechbro `web3d-integration-patterns/SKILL.md` (raw source) ; Raw source describes integration patterns for Three.js, GSAP ScrollTrigger, React Three Fiber, Motion and React Spring. It includes browser scene setup, render loops, state coordination, scroll animation and performance patterns; references the constituent library skills. ; Web scene and animation skill, not CAD. Its listed tools require JavaScript/npm packages and browser runtime. The page identifies no hosted AI or geometry-generation API. Repository-wide licence was not checked in this pass; no source copying recommended. Raw SKILL.md was web-inspected on 2026-11-12, not downloaded.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-347a968ad00e"></a>

## SRC-347a968ad00e — https://www.microsoft.com/en-us/research/workbench/project/trellis

Original source: [https://www.microsoft.com/en-us/research/workbench/project/trellis](https://www.microsoft.com/en-us/research/workbench/project/trellis)

Summary: - TRELLIS.2 Microsoft Research overview: https://www.microsoft.com/en-us/research/workbench/project/trellis

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-34ed7ccfd827"></a>

## SRC-34ed7ccfd827 — Point 02 — Existing components and CAD files to inspected reusable inputs

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md](/home/leo/projects/3dmodeling/research/action-audit/point-02-component-reuse.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-353e59cb2694"></a>

## SRC-353e59cb2694 — Bonsai georeferencing guide

Original source: [https://docs.bonsaibim.org/guides/authoring/georeferencing.html](https://docs.bonsaibim.org/guides/authoring/georeferencing.html)

Summary: Official guidance for site CRS, coordinate transformations and project north; coordinate parameters must come from survey/engineering sources.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

<a id="src-35cca1cb0d7e"></a>

## SRC-35cca1cb0d7e — blender_gltf.py — Blender glTF importer source, main branch

Original source: [https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py](https://github.com/blender/blender/blob/main/scripts/addons_core/io_scene_gltf2/blender/imp/blender_gltf.py)

Summary: Official Blender source on mutable main, accessed 2026-11-12. Import code maps glTF Y-up to Blender Z-up `(x,-z,y)` and scales locations by `1 / scene.unit_settings.scale_length` as Blender units per metre. Does not pin installed Blender version or prove local import output.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-368cf414765d"></a>

## SRC-368cf414765d — FreeCAD File Formats & Interoperability Guide

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/file_formats_interop.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/file_formats_interop.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD File Formats & Interoperability Guide. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-36fd06b4fde4"></a>

## SRC-36fd06b4fde4 — https://github.com/cdcseacave/openMVS

Original source: [https://github.com/cdcseacave/openMVS](https://github.com/cdcseacave/openMVS)

Summary: - OpenMVS repository: https://github.com/cdcseacave/openMVS

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-379d3077df35"></a>

## SRC-379d3077df35 — FreeCAD Draft SVG documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md)

Summary: Official FreeCAD docs list supported SVG paths/shapes, flattening of Z on import, use of viewBox/physical dimensions, and 90-DPI fallback when physical size is absent.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-39a648fd2c2a"></a>

## SRC-39a648fd2c2a — rec-r03.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r03.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r03.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

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

<a id="src-3a199df280ce"></a>

## SRC-3a199df280ce — LICENSE

Original source: [https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE](https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE)

Summary: - CoACD: approximate convex decomposition implementation SarahWeiii/CoACD. Its LICENSE is MIT, copyright Xinyue Wei and Minghua Liu (2022). Pin the reviewed revision and retain its notice when distributing the tool.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

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

<a id="src-3bb79a82bdb3"></a>

## SRC-3bb79a82bdb3 — kernel body path note

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/docs/cadkernel-body-path.md](https://github.com/HakanSeven12/OpenCADStudio/blob/main/docs/cadkernel-body-path.md)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

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

<a id="src-3cb645d27838"></a>

## SRC-3cb645d27838 — Part scripting — FreeCAD documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md)

Summary: The FreeCAD Part scripting page describes Part as an Open CASCADE B-rep module with Python-accessible geometric primitives and TopoShapes including vertices, edges, wires, faces, solids and compounds. It shows creating a primitive, converting it to a shape, assigning the shape to a Part::Feature and recomputing. The inspected rendered GitHub page was paired with its raw view at https://raw.githubusercontent.com/FreeCAD/FreeCAD-documentation/main/wiki/Part_scripting.md to read the content. This documents native B-rep construction, not image interpretation or a validity check.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-05-software.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-3d593dd6ed4a"></a>

## SRC-3d593dd6ed4a — README

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/README.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/README.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-3d8ba9ae669c"></a>

## SRC-3d8ba9ae669c — sequence.md

Original source: [/home/leo/projects/3dmodeling/research/action-audit/sequence.md](/home/leo/projects/3dmodeling/research/action-audit/sequence.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-3d8e9cd2ace9"></a>

## SRC-3d8e9cd2ace9 — ngv064_ocs.py — existing_component_code

Original source: [/tmp/opencode/ngv064_ocs.py](/tmp/opencode/ngv064_ocs.py)

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

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/bmw-i3-94ah-native-checks.json)

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

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r02.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r02.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-3ea30e7b5209"></a>

## SRC-3ea30e7b5209 — Documentary verification method

Original source: [/home/leo/projects/3dmodeling/research/action-audit/verification-method.md](/home/leo/projects/3dmodeling/research/action-audit/verification-method.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-3ec7111d8cd7"></a>

## SRC-3ec7111d8cd7 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill/git/trees/HEAD?recursive=1](https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-3fe2f4ec6c23"></a>

## SRC-3fe2f4ec6c23 — Blender MCP license

Original source: [https://projects.blender.org/lab/blender_mcp/src/branch/main/LICENSE](https://projects.blender.org/lab/blender_mcp/src/branch/main/LICENSE)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-402780a7bc37"></a>

## SRC-402780a7bc37 — Point 07 primary-source check: photographs, depth and learned reconstruction

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-sources.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-sources.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-40579db9c7a7"></a>

## SRC-40579db9c7a7 — microsoft/TRELLIS.2-4B — Hugging Face model card

Original source: [https://huggingface.co/microsoft/TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B)

Summary: Named TRELLIS.2-4B model card inspected 2026-11-12. Card labels this checkpoint MIT; this claim applies to this model card, not all associated datasets/assets or other model releases.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r10.md.

<a id="src-416cb87ab6bb"></a>

## SRC-416cb87ab6bb — ezdxf repository

Original source: [https://github.com/mozman/ezdxf](https://github.com/mozman/ezdxf)

Summary: Primary source repository and MIT licence metadata.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r04.md.

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.md](/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-427c3c0e8259"></a>

## SRC-427c3c0e8259 — V-HACD repository status

Original source: [https://github.com/kmammou/v-hacd/blob/master/README.md](https://github.com/kmammou/v-hacd/blob/master/README.md)

Summary: Upstream repository says V-HACD is archived/end-of-life and directs new development to CoACD.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md.

<a id="src-42ef176046c7"></a>

## SRC-42ef176046c7 — Agent Stuff

Original source: [https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/README.md](https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent Stuff. Source class: repository README. Original reuse terms: Apache-2.0; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-43a296901978"></a>

## SRC-43a296901978 — Geometric Image Transformations — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html](https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html)

Summary: OpenCV 4.13.0 documents getPerspectiveTransform from four corresponding source/destination quadrangle points and warpPerspective using a 3×3 transform, output size, interpolation and border modes. The page states that geometric image transforms sample in reverse from destination pixels to source pixels; warpPerspective can take an inverse-map flag. These APIs transform pixel grids and do not establish metric calibration or independent validation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-sources.md, research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-04-web-sources.json, research/workflows/details/cad-r02.md.

<a id="src-447a55563fd3"></a>

## SRC-447a55563fd3 — MuJoCo software repository and licence

Original source: [https://github.com/google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

Summary: Primary repository identifies MuJoCo source code under Apache-2.0 and provides Python bindings; source/docs licences are separately described.

Evidence: existing_report_registered, web_inspected.

Documents: research/domains-and-components.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r08.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r10.md.

<a id="src-46011fa591f5"></a>

## SRC-46011fa591f5 — cad-r07.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r07.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r07.md)

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

Original source: [/home/leo/projects/3dmodeling/research/sources/round-05/point-03-web-sources.json](/home/leo/projects/3dmodeling/research/sources/round-05/point-03-web-sources.json)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-47d588ded00a"></a>

## SRC-47d588ded00a — source-linked guide

Original source: [https://majiayu000.github.io/claude-skill-registry/skills/3d-modeling-0127cdf66a41/](https://majiayu000.github.io/claude-skill-registry/skills/3d-modeling-0127cdf66a41/)

Summary: Skills Directory `majiayu000` 3D Modeling ; Directory displays a copied 3D-art skill and 666 stars/25 copies/101 views. Registry's source-linked guide traces the canonical entry to `omer-metin/skills-for-antigravity/skills/3d-modeling/SKILL.md` and lists exact-content copies including `Kedhareswer/kedhar_brain/agents/skills/design-ui-ux/3d-modeling/SKILL.md`. The accessible source SKILL.md covers topology, UVs, game/film exports and art references. Registry page shows Apache-2.0 metadata for omer-metin's copy, while explicitly directing readers to check original permission; the exact original author's licence remains unverified. ; Mesh/art skill, not engineering CAD. Readable source copy was web-inspected; repository source and licence provenance were inspected via the registry guide. It has no stated CAD kernel or AI service dependency. Listing counts and security scan are directory claims, not CAD validation.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

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

<a id="src-49d1aa4fd35a"></a>

## SRC-49d1aa4fd35a — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/reyk/freecad-ai-skill/git/trees/HEAD?recursive=1](https://api.github.com/repos/reyk/freecad-ai-skill/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-4a09800705cd"></a>

## SRC-4a09800705cd — IfcOpenShell code examples

Original source: [https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html](https://docs.ifcopenshell.org/ifcopenshell-python/code_examples.html)

Summary: Official end-to-end API examples for creating an IFC project, assigning units, creating contexts and spatial hierarchy, creating a wall and writing IFC.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

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

Original source: [/home/leo/projects/energy/eoliennes/research/cad-workflow/skills-findings.md](/home/leo/projects/energy/eoliennes/research/cad-workflow/skills-findings.md)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected.

Documents: research/local-baseline.md, research/sources/local-evidence.json.

<a id="src-4c99f214f0b2"></a>

## SRC-4c99f214f0b2 — `freecad-scripts/SKILL.md`

Original source: [https://github.com/github/awesome-copilot/blob/main/skills/freecad-scripts/SKILL.md](https://github.com/github/awesome-copilot/blob/main/skills/freecad-scripts/SKILL.md)

Summary: `freecad-scripts` from `github/awesome-copilot` ; Archived skill documents FreeCAD Python console/macros, Part/B-rep primitives, Sketcher constraints, document model and GUI. It expects installed FreeCAD (0.19+, recommends 0.21+/1.0+), bundled Python, optional PySide/Pivy. Repo licence is MIT. ; Useful API reference after version checks, not an automated modeling bridge or tested parametric quality guarantee. Source link: `freecad-scripts/SKILL.md`; archive path gives repository path `skills/freecad-scripts/SKILL.md`.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-4cbe441f37a2"></a>

## SRC-4cbe441f37a2 — cad-r04.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r04.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r04.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-4d1602b2855e"></a>

## SRC-4d1602b2855e — https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html

Original source: [https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html](https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html)

Summary: Four page attempts failed and support no technical claim: Open3D 0.20.0 `RGBDImage` API page `https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html` timed out; versioned API URL `https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html` was unavailable via the web tool; GitHub HTML for `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp` returned cache miss; and `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp` returned cache miss. The default parameters were verified in the successful raw v0.20.0 `RGBDImage.h` declaration; conversion behavior was inspected in the raw `RGBDImageFactory.cpp` and `Image.cpp` sources recorded above. No further failed URLs support technical claims.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-4d88a7d32b7f"></a>

## SRC-4d88a7d32b7f — Detailed point procedures and reviews

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-index.md](/home/leo/projects/3dmodeling/research/action-audit/point-index.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-4dbc6baf3db1"></a>

## SRC-4dbc6baf3db1 — Point 07 visual and evidence review — photographs, depth and learned reconstruction

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-visual.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-visual.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-4e718650fd66"></a>

## SRC-4e718650fd66 — Image.cpp — Open3D v0.20.0 source

Original source: [https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/Image.cpp](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/Image.cpp)

Summary: Official raw source on tag v0.20.0 inspected 2026-11-12. `ConvertDepthToFloatImage` creates float depth, divides by depth_scale, and sets samples >= depth_trunc to zero; raw zeros remain zero after division. This establishes source-code behavior for this pinned tag.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

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

<a id="src-500be17749c8"></a>

## SRC-500be17749c8 — MuJoCo asset decoder plugins

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst)

Summary: Lists built-in OBJ/STL and optional USD mesh/scene decoders and extension mechanisms.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

<a id="src-5042379f8832"></a>

## SRC-5042379f8832 — harness-findings.md

Original source: [/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md](/home/leo/projects/energy/eoliennes/research/cad-workflow/harness-findings.md)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json.

<a id="src-50b834655ede"></a>

## SRC-50b834655ede — item_ocs_parts.py — existing_component_code

Original source: [/tmp/opencode/item_ocs_parts.py](/tmp/opencode/item_ocs_parts.py)

Summary: extrude, rotate, move, combine and tag provide explicit source-labelled native constructions. Applicability: Imports native-wrapper; dimensions and several recipes are ITEM-specific.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-50e5314209fb"></a>

## SRC-50e5314209fb — Camera Calibration and 3D Reconstruction — OpenCV 4.13.0

Original source: [https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html)

Summary: OpenCV 4.13.0 documents findHomography as a perspective transform between two planes from paired source/target points, with least-squares and robust methods (RANSAC, LMeDS, RHO), a reprojection threshold and inlier mask. The robust algorithms use four-pair subsets and discard collinear subsets; an unestimable homography returns an empty matrix. The same calib3d reference documents undistort(src, cameraMatrix, distCoeffs, ...) as compensation for radial and tangential lens distortion, implemented through a remap. These are geometric API claims, not measured calibration or accuracy results.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-sources.md, research/sources/round-05/point-04-web-sources.json.

<a id="src-51e2013a5b3c"></a>

## SRC-51e2013a5b3c — neugart-ngv064-wheel-160-native.json — recorded_check_results

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160-native.json)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

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

<a id="src-529bea09ca56"></a>

## SRC-529bea09ca56 — Existing IFC-to-GLB provenance record

Original source: [/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json](/home/leo/projects/energy-sim-3d/data/real-house-ifc/provenance.json)

Summary: Existing artifact pattern: source hashes, declared mm-to-m conversion, identity status, runtime and geometry mapping.

Evidence: existing_report_registered, local_reference_registered.

Documents: research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-53486b514e1a"></a>

## SRC-53486b514e1a — ifcopenshell.api.unit.assign_unit — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `assign_unit(file, units=None, length=None, area=None, volume=None)` for default project units. The page identifies defaults of millimetres for length, square metres for area and cubic metres for volume; explicit units can be assigned through supplied unit entities. Project unit assignment is separate from the placement API is_si choice.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md.

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

<a id="src-53975df039a6"></a>

## SRC-53975df039a6 — Nerfstudio source repository

Original source: [https://github.com/nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio)

Summary: Nerfstudio includes NeRF/Gaussian methods, Apache-2.0 code, and its repository describes CUDA/NVIDIA stack prerequisites.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/rec-r02.md.

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

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r05.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r05.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-554c43270f1b"></a>

## SRC-554c43270f1b — IfcOpenShell repository and software licences

Original source: [https://github.com/IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)

Summary: Repository identifies IfcOpenShell as LGPL-3.0-or-later and Bonsai as GPL-3.0-or-later; tool software licences do not license imported assets.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r02.md, research/workflows/details/dom-r07.md.

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

<a id="src-56b9d47414e7"></a>

## SRC-56b9d47414e7 — Point 04 — Raster drawings and interpreted dimensions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md](/home/leo/projects/3dmodeling/research/action-audit/point-04-raster-drawings.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-56c822eef16f"></a>

## SRC-56c822eef16f — FreeCAD Python API Reference

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/python_api_reference.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/python_api_reference.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Python API Reference. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-57e794a1c1cb"></a>

## SRC-57e794a1c1cb — License

Original source: [https://polyhaven.com/license](https://polyhaven.com/license)

Summary: Poly Haven ; Library of 3D models, materials and HDRI environments useful for scene dressing, architectural visualization and lighting. Asset catalog ; Poly Haven states all site assets are CC0, including commercial use without attribution. This is useful for visual environments and render context; asset dimensions/geometry are not engineering component specifications. License

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

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

<a id="src-59bd5a7cb61a"></a>

## SRC-59bd5a7cb61a — https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md

Original source: [https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md](https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md)

Summary: 2. Name: Tesseract; Role: Dimension text candidates with boxes/confidence; humans verify engineering notation.; License: Apache-2.0 upstream.; Apis: tesseract image outputbase -l eng tsv; TSV bbox/confidence review; Dependencies: Tesseract OCR binary plus eng traineddata; TSV output is text candidates only.; Source urls: https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md; https://github.com/tesseract-ocr/tesseract

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-04-visual.md, research/action-audit/reviews/visual-review.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md.

<a id="src-5a8b5891ac1d"></a>

## SRC-5a8b5891ac1d — ocs_module.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/plugins/opencad-python/src/ocs_module.rs](/home/leo/projects/3rdparty/OpenCADStudio/plugins/opencad-python/src/ocs_module.rs)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-5afc1d03b483"></a>

## SRC-5afc1d03b483 — OCS session control helper source

Original source: [/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py](/home/leo/.codex/skills/ocs-engineering/scripts/ocs_control.py)

Summary: Session preflight and mutation transport helper for a later authorized live CAD operation.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-5c5742981c2f"></a>

## SRC-5c5742981c2f — ShapeKernel upstream LICENSE file

Original source: [https://raw.githubusercontent.com/leap71/LEAP71_ShapeKernel/main/LICENSE](https://raw.githubusercontent.com/leap71/LEAP71_ShapeKernel/main/LICENSE)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: ShapeKernel upstream LICENSE file. Source class: official repository license original, plain text. Original reuse terms: Apache License 2.0; preserve the complete license text and notices.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-5d152842ea12"></a>

## SRC-5d152842ea12 — solid3d.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/src/app/command_driver/solid3d.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/app/command_driver/solid3d.rs)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

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

<a id="src-5e0d7de82f1b"></a>

## SRC-5e0d7de82f1b — Research record

Original source: [/home/leo/projects/3dmodeling/research/research-log.md](/home/leo/projects/3dmodeling/research/research-log.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-5e5932bb68e1"></a>

## SRC-5e5932bb68e1 — Pipeline formats

Original source: [https://www.blender.org/features/pipeline/](https://www.blender.org/features/pipeline/)

Summary: Blender ; Supports interchange including glTF, USD, OBJ, PLY, STL and Alembic; Blender artwork remains the creator's property. Pipeline formats, license ; Upstream `COPYING` points to the GNU GPL text, which is GPL version 2. The installed Debian Blender 5.0.1 package copyright record labels the main Blender files GPL-2+. Components and add-ons may have separate terms. Blender's GPL-2+ later-version option permits choosing GPL-3 when distributing a covered combined work with GPL-3+-licensed Blender MCP code; preserve exact notices and assess each shipped component. Upstream COPYING, upstream GPL text, Blender MCP license ; General scene inspection, image/mesh workflows, visualization and scripted conversions. OpenCADStudio remains the project's CAD baseline; Blender complements it for mesh/scene workflows, display and scripted conversions.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/action-audit/reviews/point-07-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r05.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r06.md, research/workflows/details/mix-r09.md, research/workflows/domain-paths.md.

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

<a id="src-6038042a0445"></a>

## SRC-6038042a0445 — point-02-web-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-05/point-02-web-sources.json](/home/leo/projects/3dmodeling/research/sources/round-05/point-02-web-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-608f9d6fff1b"></a>

## SRC-608f9d6fff1b — dom-r04.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r04.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r04.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-60e0a613e21d"></a>

## SRC-60e0a613e21d — Point 07 — reconstruction software and API review

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-software.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-software.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-61c6ad4341d0"></a>

## SRC-61c6ad4341d0 — cad-r03.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r03.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r03.md)

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-07-operations.json)

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.md](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.md)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-6350270f836a"></a>

## SRC-6350270f836a — https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html

Original source: [https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html)

Summary: Four direct page attempts did not yield page contents: ROS Rolling URDF tutorial (`https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/Building-a-Movable-Robot-Model-with-URDF.html`, access denied by Anubis); ROS REP-103 mirror (`https://www.ros.org/reps/rep-0103.html`, access denied by Anubis; the source-controlled REP page was inspected successfully instead); Blender glTF manual (`https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html`, HTTP 402); and guessed IfcOpenShell geometry-settings URL (`https://docs.ifcopenshell.org/ifcopenshell-python/geometry_settings.html`, unavailable via the web tool). These failed attempts support no technical claim. Existing source-register records were reused for MuJoCo/IfcOpenShell/CoACD licensing and earlier workflow descriptions; they are not counted as fresh inspection. No local runtime or implementation capability is established by this source audit.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-06-sources.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-6398638998c9"></a>

## SRC-6398638998c9 — OpenCADStudio Automation API — Specification 1.1

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: OpenCADStudio Automation API — Specification 1.1. Source class: local primary product documentation; exact byte copy from local source repository. Original reuse terms: GPL-3.0-or-later repository license; see /home/leo/projects/3rdparty/OpenCADStudio/LICENSE

Evidence: archived_original_referenced, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/archive-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-64196dacabad"></a>

## SRC-64196dacabad — Independent review — Point 02 component and CAD reuse

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-independent.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-64327fe17901"></a>

## SRC-64327fe17901 — Point 02 source check: existing components and CAD files

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-sources.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-sources.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-6436ad01395b"></a>

## SRC-6436ad01395b — Camera Models — COLMAP

Original source: [https://colmap.github.io/cameras.html](https://colmap.github.io/cameras.html)

Summary: COLMAP camera-model reference inspected 2026-11-12. Page identifies version 4.3.0.dev0, commit 3c1a1b9 (2026-11-08), and says camera +Z is the look direction. Lists models of varying complexity; SIMPLE_PINHOLE and PINHOLE are for images already undistorted. Projection includes perspective division, distortion and intrinsic transform; COLMAP uses corner-based pixels with top-left pixel centre at (0.5,0.5).

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-6507a5c7f8da"></a>

## SRC-6507a5c7f8da — contract.json

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/contract.json](/home/leo/projects/3dmodeling/research/workflows/details/contract.json)

Summary: Analyst classification contract: independent manual effort, software setup and computing classes; required evidence, input and output fields.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md](/home/leo/projects/3dmodeling/research/action-audit/point-01-model-brief.md)

Summary: Proposed ten-action source-to-model-brief procedure with software, AI and user assignments, four execution modes, per-feature requirements, candidate comparison/merge, eight development components and thirteen future validation cases.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-6a6bf0c0ce39"></a>

## SRC-6a6bf0c0ce39 — PCL SampleConsensusModelCylinder header — master branch

Original source: [https://raw.githubusercontent.com/PointCloudLibrary/pcl/master/sample_consensus/include/pcl/sample_consensus/sac_model_cylinder.h](https://raw.githubusercontent.com/PointCloudLibrary/pcl/master/sample_consensus/include/pcl/sample_consensus/sac_model_cylinder.h)

Summary: The official PCL header defines seven cylinder coefficients in order: point on axis x,y,z; axis direction x,y,z; radius. It declares model size 7, sample size 2, and documents coefficient-based distance, inlier selection, optimization and point projection methods. The master-branch URL is mutable and does not pin a released PCL version; no local source or runtime version was checked.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-independent.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-6a6e188c27d3"></a>

## SRC-6a6e188c27d3 — skill-to-actions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.json](/home/leo/projects/3dmodeling/research/action-audit/skill-to-actions.json)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-6a8670ea9c90"></a>

## SRC-6a8670ea9c90 — Independent review — Point 03 vectors, sketches and solids

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-independent.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-6ab8413122ee"></a>

## SRC-6ab8413122ee — redirect destination

Original source: [https://occt3d.com/dev/doc/refman/html/class_s_t_e_p_control___writer.html](https://occt3d.com/dev/doc/refman/html/class_s_t_e_p_control___writer.html)

Summary: 2. The source observation retains the exact supplied OCCT URL and its redirect destination, identifying the served reference as OCCT 8.0.1. It attributes `Transfer(TopoDS_Shape, STEPControl_StepModelType, ...)`, model modes and `Write`/`WriteStream` to the shape-oriented writer. Separate transfer roots remain source API behavior; actual geometry, interpreted units and consumer fidelity retain their future readback requirements.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-03-independent.md, research/action-audit/reviews/point-03-sources.md.

<a id="src-6b30ccb4447f"></a>

## SRC-6b30ccb4447f — https://github.com/isl-org/Open3D

Original source: [https://github.com/isl-org/Open3D](https://github.com/isl-org/Open3D)

Summary: - Open3D repository/license: https://github.com/isl-org/Open3D

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-6bbd844182e8"></a>

## SRC-6bbd844182e8 — https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE

Original source: [https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE](https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE)

Summary: - SAM 3D custom license (covers source, checkpoints and code): https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md.

<a id="src-6c38d73efa65"></a>

## SRC-6c38d73efa65 — Frequently Asked Questions — COLMAP

Original source: [https://colmap.github.io/faq.html](https://colmap.github.io/faq.html)

Summary: COLMAP current FAQ inspected 2026-11-12. For OpenCV/Kalibr calibration imported to COLMAP, add 0.5 to cx and cy only to convert integer-centred OpenCV/Kalibr coordinates into COLMAP's corner-based convention; fx, fy and distortion remain unchanged. OPENCV distortion order is k1,k2,p1,p2; FULL_OPENCV adds k3,k4,k5,k6.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r06.md, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-6c6db30cba74"></a>

## SRC-6c6db30cba74 — CadQuery repository/licence

Original source: [https://github.com/CadQuery/cadquery](https://github.com/CadQuery/cadquery)

Summary: Primary sources: CadQuery repository/licence, official docs, import/export formats. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/next-step-proposal.md.

<a id="src-6ca63dd2611f"></a>

## SRC-6ca63dd2611f — check_ngv064_wheel.py — existing_component_code

Original source: [/tmp/opencode/check_ngv064_wheel.py](/tmp/opencode/check_ngv064_wheel.py)

Summary: sat_features extracts selected SAT cylinders, planes, tori and points; verify checks the wheel. Applicability: Top-level import loads native-wrapper. Restricted SAT fields; one body transform, unit scale; SAB requires a separate supported reader.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

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

<a id="src-6e28384e1b5f"></a>

## SRC-6e28384e1b5f — CadQuery LICENSE

Original source: [https://github.com/CadQuery/cadquery/blob/master/LICENSE](https://github.com/CadQuery/cadquery/blob/master/LICENSE)

Summary: Repository license text: Apache-2.0.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r01.md.

<a id="src-6e6b9cf6af3c"></a>

## SRC-6e6b9cf6af3c — https://alicevision.org/

Original source: [https://alicevision.org/](https://alicevision.org/)

Summary: - AliceVision official project (MPL-2.0; workflows): https://alicevision.org/

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/workflows/details/mix-r01.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r09.md, research/workflows/details/rec-r01.md, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md.

<a id="src-6e951925cbb7"></a>

## SRC-6e951925cbb7 — Noyron — a foundational Large Computational Engineering Model

Original source: [https://leap71.com/noyron/](https://leap71.com/noyron/)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: Noyron — a foundational Large Computational Engineering Model. Source class: official company product-description HTML; claims, not independent validation. Original reuse terms: Website copyright LEAP 71; all rights reserved per page. No reuse licence identified.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-6f5062ead541"></a>

## SRC-6f5062ead541 — Project cross-domain workflow recipes and additional ideas

Original source: [/home/leo/projects/3dmodeling/research/workflows/combined-paths.json](/home/leo/projects/3dmodeling/research/workflows/combined-paths.json)

Summary: Original project proposals combining CAD, photogrammetry, controls, component libraries, IFC and robot models, with named artifact roles and explicit handoff conditions. Also records concept-image and procedural-field research questions.

Evidence: local_source_inspected.

Documents: research/sources/round-02/project-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-6fdd6f04d055"></a>

## SRC-6fdd6f04d055 — cad-r08.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r08.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r08.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-7018bc2fbb81"></a>

## SRC-7018bc2fbb81 — Product CAD

Original source: [https://www.noritake-elec.com/support/3d-cad-data?id=cu22042-y1a&part=CU22042-Y100](https://www.noritake-elec.com/support/3d-cad-data?id=cu22042-y1a&part=CU22042-Y100)

Summary: Manufacturer product CAD ; Vendor sites commonly provide STEP/IGES for configured product models. For example, NORITAKE offers STEP/IGES for named product CU22042-Y100 and warns files may be incomplete, inaccurate, not to scale or outdated, under vendor terms. Product CAD. CONTEC terms expressly limit use and prohibit changing/adapting its CAD data. ; Downloadability is not an open license. Store the exact terms and source URL with each asset. Default to private project use only as the terms allow; do not redistribute vendor files or converted derivatives absent permission.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-70879a2c2cb0"></a>

## SRC-70879a2c2cb0 — TechDraw ExportPageSVG — FreeCAD documentation main branch

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_ExportPageSVG.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_ExportPageSVG.md)

Summary: Official FreeCAD documentation repository page inspected 2026-11-12 as targeted DOM-25 follow-up. Documents `TechDrawGui.exportPageAsSvg(DrawPageObject, FilePath)` for macros/Python console when the FreeCAD GUI module is active. The page states hatch patterns are not exported and text positions/sizes may be inaccurate. Repository was archived 2026-04-01; documentation page does not pin a FreeCAD release.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-717a1bbd2f70"></a>

## SRC-717a1bbd2f70 — dom-r05.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r05.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r05.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-71dee9d2e674"></a>

## SRC-71dee9d2e674 — Visual interpretation review — descriptions and explicit dimensions to a model brief

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/visual-review.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/visual-review.md)

Summary: Authored audit document recording Visual interpretation review — descriptions and explicit dimensions to a model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-71df4a24323d"></a>

## SRC-71df4a24323d — Point 06 primary-source check: building and robot structure and properties

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-sources.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-sources.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-724b2d11a6eb"></a>

## SRC-724b2d11a6eb — DA3 Streaming README — main branch

Original source: [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md)

Summary: Official mutable main README inspected 2026-11-12. Documents camera pose and intrinsic text files, combined point cloud PLY and optional per-frame RGB/depth/confidence outputs. Peak VRAM table depends on named datasets, resolutions, chunk sizes and overlap; it is not a universal resource requirement.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r02.md, research/workflows/details/rec-r05.md.

<a id="src-74d5d4738857"></a>

## SRC-74d5d4738857 — Source contract findings and implementation conditions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/findings.md](/home/leo/projects/3dmodeling/research/action-audit/findings.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-750882b224a7"></a>

## SRC-750882b224a7 — battery_ocs_parts.py — existing_component_code

Original source: [/tmp/opencode/battery_ocs_parts.py](/tmp/opencode/battery_ocs_parts.py)

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

<a id="src-76b9efd76055"></a>

## SRC-76b9efd76055 — OpenMVS Usage Guide — develop branch

Original source: [https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md](https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md)

Summary: Official OpenMVS usage guide on mutable develop branch inspected 2026-11-12. Documents COLMAP image_undistorter output, `InterfaceCOLMAP -i dense -o scene.mvs --image-folder dense/images`, DensifyPointCloud, ReconstructMesh, optional refinement/texturing, a CPU SGM route and memory sub-scene splitting that may leave seams.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r01.md, research/workflows/reconstruction-paths.md.

<a id="src-773aa3a5f61a"></a>

## SRC-773aa3a5f61a — CAD Modeling Pattern Library

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/cad_modeling_patterns.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/cad_modeling_patterns.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: CAD Modeling Pattern Library. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-77594e51ac89"></a>

## SRC-77594e51ac89 — Existing operation inventory and detailed-review state

Original source: [/home/leo/projects/3dmodeling/research/action-audit/operation-inventory.md](/home/leo/projects/3dmodeling/research/action-audit/operation-inventory.md)

Summary: Authored audit document recording Existing operation inventory and detailed-review state. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json.

<a id="src-785d8cbc2541"></a>

## SRC-785d8cbc2541 — rec-r07.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r07.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r07.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-789932d05ce2"></a>

## SRC-789932d05ce2 — 3D reconstruction research report

Original source: [/home/leo/projects/3dmodeling/research/reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md)

Summary: Prior repository report assesses image/depth reconstruction methods, source terms and prerequisites. This batch references it for scan-to-CAD transition context and does not repeat that research.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-7986969c7a59"></a>

## SRC-7986969c7a59 — Point 06 designer notes — building and robot structure and properties

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-designer.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-designer.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-79f9dd42f446"></a>

## SRC-79f9dd42f446 — step.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json.

<a id="src-7a9b6fde0c01"></a>

## SRC-7a9b6fde0c01 — reconstruction-paths.json

Original source: [/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json](/home/leo/projects/3dmodeling/research/workflows/reconstruction-paths.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-7b3c4ff0a101"></a>

## SRC-7b3c4ff0a101 — source SKILL.md

Original source: [https://github.com/omer-metin/skills-for-antigravity/blob/main/skills/3d-modeling/SKILL.md](https://github.com/omer-metin/skills-for-antigravity/blob/main/skills/3d-modeling/SKILL.md)

Summary: Skills Directory `majiayu000` 3D Modeling ; Directory displays a copied 3D-art skill and 666 stars/25 copies/101 views. Registry's source-linked guide traces the canonical entry to `omer-metin/skills-for-antigravity/skills/3d-modeling/SKILL.md` and lists exact-content copies including `Kedhareswer/kedhar_brain/agents/skills/design-ui-ux/3d-modeling/SKILL.md`. The accessible source SKILL.md covers topology, UVs, game/film exports and art references. Registry page shows Apache-2.0 metadata for omer-metin's copy, while explicitly directing readers to check original permission; the exact original author's licence remains unverified. ; Mesh/art skill, not engineering CAD. Readable source copy was web-inspected; repository source and licence provenance were inspected via the registry guide. It has no stated CAD kernel or AI service dependency. Listing counts and security scan are directory claims, not CAD validation.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-7baec7354391"></a>

## SRC-7baec7354391 — https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html

Original source: [https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html](https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html)

Summary: Four page attempts failed and support no technical claim: Open3D 0.20.0 `RGBDImage` API page `https://www.open3d.org/docs/latest/python_api/open3d.geometry.RGBDImage.html` timed out; versioned API URL `https://www.open3d.org/docs/0.20.0/python_api/open3d.geometry.RGBDImage.html` was unavailable via the web tool; GitHub HTML for `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp` returned cache miss; and `https://github.com/isl-org/Open3D/blob/v0.20.0/cpp/pybind/geometry/image.cpp` returned cache miss. The default parameters were verified in the successful raw v0.20.0 `RGBDImage.h` declaration; conversion behavior was inspected in the raw `RGBDImageFactory.cpp` and `Image.cpp` sources recorded above. No further failed URLs support technical claims.

Evidence: existing_report_registered, access_failed.

Documents: research/action-audit/reviews/point-07-sources.md, research/sources/round-05/point-07-web-sources.json.

<a id="src-7be225e2793e"></a>

## SRC-7be225e2793e — cad-detail-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-03/cad-detail-sources.json](/home/leo/projects/3dmodeling/research/sources/round-03/cad-detail-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-7c623f2c8b68"></a>

## SRC-7c623f2c8b68 — FreeCAD Modeling Best Practices & TNP Mitigation

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/modeling_best_practices.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-user/references/modeling_best_practices.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Modeling Best Practices & TNP Mitigation. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-7d7038c13789"></a>

## SRC-7d7038c13789 — FreeCAD AI

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/README.md](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD AI. Source class: repository README. Original reuse terms: permissive terms as archived; GitHub API SPDX=ISC; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-7f7508ffab83"></a>

## SRC-7f7508ffab83 — Potrace: a polygon-based tracing algorithm

Original source: [https://potrace.sourceforge.net/potrace.pdf](https://potrace.sourceforge.net/potrace.pdf)

Summary: Peter Selinger’s 2003 paper describes Potrace tracing black/white bitmaps into smooth Bezier contours, using polygons internally. It explicitly notes that several outlines can generate the same bitmap and that tracing cannot generate information absent from the input. This supports a vectorization capability and its information limit; it does not identify a locally selected executable, version or license.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-sources.md, research/sources/round-05/point-04-web-sources.json.

<a id="src-8089d1901b4f"></a>

## SRC-8089d1901b4f — Asset catalog

Original source: [https://polyhaven.com/](https://polyhaven.com/)

Summary: Poly Haven ; Library of 3D models, materials and HDRI environments useful for scene dressing, architectural visualization and lighting. Asset catalog ; Poly Haven states all site assets are CC0, including commercial use without attribution. This is useful for visual environments and render context; asset dimensions/geometry are not engineering component specifications. License

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-80962f129a41"></a>

## SRC-80962f129a41 — Software review: raster drawings and interpreted dimensions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-software.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-software.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-80d56f29af4a"></a>

## SRC-80d56f29af4a — Agent skill: freecad-scripts

Original source: [https://raw.githubusercontent.com/github/awesome-copilot/main/skills/freecad-scripts/SKILL.md](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/freecad-scripts/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-scripts. Source class: agent skill instructions. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-812380a2589c"></a>

## SRC-812380a2589c — Current FreeCAD API Notes

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/references/current-api.md](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/references/current-api.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Current FreeCAD API Notes. Source class: skill reference documentation. Original reuse terms: permissive terms as archived; GitHub API SPDX=ISC; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-816d7accc0c5"></a>

## SRC-816d7accc0c5 — Point 04 visual and evidence review — raster drawings and orthographic views

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-visual.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-visual.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-819035442c74"></a>

## SRC-819035442c74 — https://mcpmarket.com/tools/skills/generate-3d-model

Original source: [https://mcpmarket.com/tools/skills/generate-3d-model](https://mcpmarket.com/tools/skills/generate-3d-model)

Summary: - MCP Market: “Generate 3D Model” https://mcpmarket.com/tools/skills/generate-3d-model — listing opened. It describes a downloadable Claude Code skill by TomekGancarczyk that calls Fal.ai `fal-ai/sam-3/3d-objects`, performs image/mask segmentation and cloud generation, downloads GLB assets, and emits React Three Fiber/Rapier snippets. The source skill/GitHub repository was identified as https://github.com/TomekGancarczyk/kata-workshop-cc; the skill file itself was not retrieved through the listing's failed “SKILL.md” click, so its complete prompt, dependency list, and behavior remain uninspected. The repository is a MIT-licensed React Three Fiber game workshop starter, not evidence that the hosted model or its generated outputs carry MIT terms. Do not treat the listing's “open” description as evidence of local inference.

Evidence: existing_report_registered.

Documents: research/reconstruction.md, research/user-supplied-links.md.

<a id="src-82658321d621"></a>

## SRC-82658321d621 — neugart-ngv064-wheel-160.md — recorded_execution_report

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/neugart-ngv064-wheel-160.md)

Summary: Component-specific native checks, save/reopen observations and source paths for OCS 2026.42. Applicability:

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-82d9fa8ce417"></a>

## SRC-82d9fa8ce417 — domain-detail-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-03/domain-detail-sources.json](/home/leo/projects/3dmodeling/research/sources/round-03/domain-detail-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-837950156e9e"></a>

## SRC-837950156e9e — Contributor terms

Original source: [https://www.3dcontentcentral.com/includes/Attachments/Terms_and_Conditions_for_Contributions.pdf](https://www.3dcontentcentral.com/includes/Attachments/Terms_and_Conditions_for_Contributions.pdf)

Summary: 3D ContentCentral ; Supplier-certified and user library models in multiple CAD formats. SOLIDWORKS help ; Platform access requires agreement; contributor terms give the platform broad indexing/adaptation/distribution rights but do not establish a blanket open license for each downloaded model. Record per-item license/terms; do not treat the catalog as open data. Contributor terms

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-83daf3ad8d92"></a>

## SRC-83daf3ad8d92 — Driving the OpenCADStudio native builds

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/native.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/native.md)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: Driving the OpenCADStudio native builds. Source class: local primary product documentation; exact byte copy from local source repository. Original reuse terms: GPL-3.0-or-later repository license; see /home/leo/projects/3rdparty/OpenCADStudio/LICENSE

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-840d8b69fd8f"></a>

## SRC-840d8b69fd8f — Software review: CAD, photographs and scans alignment

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-software.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-software.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-856f00288f07"></a>

## SRC-856f00288f07 — Optional Computer Use Workflow

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/computer_use_workflow.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/computer_use_workflow.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Optional Computer Use Workflow. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-85b949b4c1e5"></a>

## SRC-85b949b4c1e5 — Point 06 independent review — building and robot structure and properties

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-independent.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-8611e98b9ce8"></a>

## SRC-8611e98b9ce8 — Using custom data — Nerfstudio documentation

Original source: [https://docs.nerf.studio/quickstart/custom_dataset.html](https://docs.nerf.studio/quickstart/custom_dataset.html)

Summary: Current Nerfstudio custom-data guide inspected 2026-11-12; release not pinned. States per-image camera poses are required; `ns-process-data images;video` uses COLMAP and FFmpeg; supplied pose paths include Metashape XML and RealityCapture CSV. The guide alone does not specify parser auto-orientation/scale settings.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r08.md, research/workflows/reconstruction-paths.md.

<a id="src-86cdf9c119df"></a>

## SRC-86cdf9c119df — Splatfacto — Nerfstudio documentation

Original source: [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)

Summary: Current Nerfstudio Splatfacto guide inspected 2026-11-12; release not pinned. Documents trained Gaussian splat export to PLY via `ns-export gaussian-splat`; page says mesh and point-cloud export are currently unsupported for Splatfacto's own export path.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/findings.md, research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/mix-r09.md, research/workflows/details/rec-r05.md, research/workflows/details/rec-r06.md, research/workflows/details/rec-r08.md, research/workflows/reconstruction-paths.md.

<a id="src-885fe0a26a5e"></a>

## SRC-885fe0a26a5e — glotoff/freecad-skills

Original source: [https://github.com/glotoff/freecad-skills](https://github.com/glotoff/freecad-skills)

Summary: glotoff/freecad-skills ; FreeCAD user/power-user modeling and API references ; Adapt only the exercised operations needed for constrained sketches and editable features.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-887713f8625d"></a>

## SRC-887713f8625d — item-profile-02633-segment-100mm-native.json — recorded_check_results

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm-native.json)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-896c4a89c975"></a>

## SRC-896c4a89c975 — Agent skill: freecad-ai

Original source: [https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/SKILL.md](https://raw.githubusercontent.com/reyk/freecad-ai-skill/main/skills/freecad-ai/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-ai. Source class: agent skill instructions. Original reuse terms: permissive terms as archived; GitHub API SPDX=ISC; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-89c0679bdda3"></a>

## SRC-89c0679bdda3 — Proposed next stages from the workflow research

Original source: [/home/leo/projects/3dmodeling/research/next-step-proposal.md](/home/leo/projects/3dmodeling/research/next-step-proposal.md)

Summary: Seven proposed work packages: targeted route review, shared records, existing OCS pilot, text/drawing routes, measured reconstruction, architecture/robotics/component reuse, and packaging exercised workflows. Preserves the existing implementation plan.

Evidence: local_source_inspected.

Documents: research/sources/round-02/project-sources.json.

<a id="src-8a7317b2bcc0"></a>

## SRC-8a7317b2bcc0 — cad2urdf repository

Original source: [https://github.com/boelnasr/CAD_TO_URDF](https://github.com/boelnasr/CAD_TO_URDF)

Summary: Repository describes conversion of mesh plus YAML joints or STEP/IGES assemblies into ROS URDF packages; automatic joint hypotheses require review.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/dom-r04.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-8c216bd07f9d"></a>

## SRC-8c216bd07f9d — Franka Emika Panda MJCF file

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/panda.xml](https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_emika_panda/panda.xml)

Summary: Actual example robot model source file for the Menagerie Panda; use only at a pinned revision and with model-specific rights.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r04.md.

<a id="src-8db7870af183"></a>

## SRC-8db7870af183 — Dave Snider, “Claude tips for 3D work”

Original source: [https://davesnider.com/claude-3D](https://davesnider.com/claude-3D)

Summary: Dave Snider, “Claude tips for 3D work” ; Article dated March 13, 2026 describes browser 3D applications, app-state/camera/debug-marker feedback loops and visual review. It notes screenshots and logs helped expose spatial mistakes in his workflow. ; Visual-debugging article, not a CAD skill or kernel. Web inspected; no packaged skill or licence. Visual feedback complements numerical geometry measurements; it does not replace them.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-8de314785eed"></a>

## SRC-8de314785eed — /home/leo/projects/3rdparty/OpenCADStudio/LICENSE

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/LICENSE](/home/leo/projects/3rdparty/OpenCADStudio/LICENSE)

Summary: Source referenced for the stated workflow; see the owning documentation or research item.

Evidence: existing_report_registered, local_reference_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-8e6d7648b52e"></a>

## SRC-8e6d7648b52e — Command-line Interface — COLMAP

Original source: [https://colmap.github.io/cli.html](https://colmap.github.io/cli.html)

Summary: COLMAP current CLI documentation inspected 2026-11-12; no local binary version checked. Shows sparse matching/mapper, image_undistorter, patch_match_stereo, stereo_fusion, poisson_mesher and delaunay_mesher stages. PatchMatch requires the undistorted workspace; fusion creates colored cloud. GPU backend support depends on selected build/options.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-sources.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/dom-r01.md, research/workflows/details/dom-r06.md, research/workflows/reconstruction-paths.md.

<a id="src-8f369f8f1381"></a>

## SRC-8f369f8f1381 — Python — MuJoCo Documentation

Original source: [https://mujoco.readthedocs.io/en/stable/python.html](https://mujoco.readthedocs.io/en/stable/python.html)

Summary: Stable MuJoCo Python binding documentation accessed 2026-11-12. Establishes the Python bindings are close to the C API; used alongside the model-editing page for Python method names. No local package version was checked.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-8f8532cac48e"></a>

## SRC-8f8532cac48e — Domain and component research report

Original source: [/home/leo/projects/3dmodeling/research/domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md)

Summary: Prior project report compares reusable component sources and downstream architecture/robotics domains. This batch uses it for source-library and assembly handoffs.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-8f9b6f25cd0d"></a>

## SRC-8f9b6f25cd0d — AGENTS.md

Original source: [/home/leo/projects/3dmodeling/AGENTS.md](/home/leo/projects/3dmodeling/AGENTS.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-90428f0f4c05"></a>

## SRC-90428f0f4c05 — TripoSR model card and weights

Original source: [https://huggingface.co/stabilityai/TripoSR](https://huggingface.co/stabilityai/TripoSR)

Summary: Model card labels weights MIT and identifies single-image feed-forward reconstruction; trained using Objaverse renders.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/dom-r06.md, research/workflows/details/rec-r10.md.

<a id="src-91466ed68e96"></a>

## SRC-91466ed68e96 — Python plugin declaration

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/plugins/opencad-python/plugin.toml](https://github.com/HakanSeven12/OpenCADStudio/blob/main/plugins/opencad-python/plugin.toml)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-926884ef85e8"></a>

## SRC-926884ef85e8 — Foster1202/cad-modeling-fusion-skill

Original source: [https://github.com/Foster1202/cad-modeling-fusion-skill](https://github.com/Foster1202/cad-modeling-fusion-skill)

Summary: Foster1202/cad-modeling-fusion-skill ; ModelSpec schema and code-generation patterns with Fusion, FreeCAD and OpenSCAD backends ; Assess reusable schema and open-backend content under its licence. Use the open software backends for this project.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, skills/README.md.

<a id="src-92b7a09b7e3a"></a>

## SRC-92b7a09b7e3a — Local Python 3.14 CSV source

Original source: [/usr/lib/python3.14/csv.py](/usr/lib/python3.14/csv.py)

Summary: CSV dialect/field parsing source inspected by the software reviewer; retain source strings and explicit dialect.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-932141965717"></a>

## SRC-932141965717 — Blender Lab MCP page

Original source: [https://www.blender.org/lab/mcp-server/](https://www.blender.org/lab/mcp-server/)

Summary: The Blender-hosted Blender Lab MCP repository is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its setup page requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The Blender Lab MCP page search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's scripting security guidance says Python scripts can perform unrestricted operations.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-9332105dc85a"></a>

## SRC-9332105dc85a — nissan-leaf-gen2-native.json — recorded_check_results

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/nissan-leaf-gen2-native.json)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-934308b209a1"></a>

## SRC-934308b209a1 — Awesome Skills `earthtojake-text-to-cad-step-parts`

Original source: [https://awesomeskill.ai/skill/earthtojake-text-to-cad-step-parts](https://awesomeskill.ai/skill/earthtojake-text-to-cad-step-parts)

Summary: Awesome Skills `earthtojake-text-to-cad-step-parts` ; Page identifies skill `step-parts`: query hosted step.parts catalog for purchasable parts, fuzzy search/standards, obtain canonical STEP, verify checksums and hand off to a viewer. It reports 5,937 stars, 710 forks, updated 2026-06-10. ; Hosted component-catalog integration, not text-to-parametric CAD. Network/API and external catalog are intrinsic to advertised behavior. Source SKILL.md was not downloaded. This is distinct from the archived `earthtojake/text-to-cad` skill and must not be conflated.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-937929a512bd"></a>

## SRC-937929a512bd — Point 05 designer notes — alignment and parametric remodeling

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-designer.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-designer.md)

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

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r10.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r10.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-93b47d856776"></a>

## SRC-93b47d856776 — Local Python 3.14 JSON interface source

Original source: [/usr/lib/python3.14/json/__init__.py](/usr/lib/python3.14/json/__init__.py)

Summary: Decoder callbacks, numeric token handling and nonfinite/default behavior inspected as intake design evidence.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-940fb4ea2921"></a>

## SRC-940fb4ea2921 — Point 06 visual and evidence review — building and robot structure and properties

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-visual.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-06-visual.md)

Summary: Point 06 Building and robot structure and properties: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-94415df8565c"></a>

## SRC-94415df8565c — Point 07 — Capture, reconstruction and appearance scenes

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md](/home/leo/projects/3dmodeling/research/action-audit/point-07-reconstruction.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-9463773b6a12"></a>

## SRC-9463773b6a12 — OpenSCAD Documentation index

Original source: [https://openscad.org/documentation](https://openscad.org/documentation)

Summary: The official OpenSCAD documentation page links to the User Manual, Language Reference, and the manual section 'Using OpenSCAD in a command line environment'. This inspected index confirms the official documentation route for scripted modeling and command-line use; it does not expose a command example or mesh-export flag on the index page. The project's existing source register records an earlier inspection of the official OpenSCAD manuals for command-line rendering/export and mesh-oriented formats.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/cad-r10.md, research/workflows/details/mix-r02.md.

<a id="src-952bf146bbc5"></a>

## SRC-952bf146bbc5 — FreeCAD Headless Execution & Automation

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/headless_execution.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/headless_execution.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Headless Execution & Automation. Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-9557e8c0e378"></a>

## SRC-9557e8c0e378 — point-02-operations

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-02-operations.json)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-95aacf0e0f5c"></a>

## SRC-95aacf0e0f5c — ifcopenshell.api.geometry.edit_object_placement — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `edit_object_placement(file, product, matrix=None, is_si=True, should_transform_children=False)` for a 4×4 local placement matrix. is_si=True means matrix translations are SI; False means project units. Only local placements are supported; the child flag controls whether nested children move with the parent or retain world position through rewritten local placements.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-02-visual.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md.

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

<a id="src-96e5bd9ad8ba"></a>

## SRC-96e5bd9ad8ba — Full-sequence independent integration review

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/full-sequence-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/full-sequence-independent.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-9794ead44d0e"></a>

## SRC-9794ead44d0e — ifcopenshell.api.georeference — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html)

Summary: IfcOpenShell 0.9.0post1 documents `add_georeferencing` creating projected-CRS and map-conversion entities with blank parameters, and `edit_georeferencing` setting CRS and coordinate-operation attributes. CRS and transform values must be supplied; the API does not estimate a survey transform. IFC2X3 uses its map-conversion property-set route.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/point-05-sources.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-05-web-sources.json, research/workflows/details/dom-r01.md.

<a id="src-98a1a3cd7fd0"></a>

## SRC-98a1a3cd7fd0 — Agent skill: freecad-power-user

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/SKILL.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: freecad-power-user. Source class: agent skill instructions. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-9969afca68d8"></a>

## SRC-9969afca68d8 — Point 04 designer notes — raster drawings and interpreted dimensions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-designer.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-designer.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-99954d282c44"></a>

## SRC-99954d282c44 — Point 03 designer notes — vector profiles and small solids

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-designer.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-designer.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-99bfdb2d1a9e"></a>

## SRC-99bfdb2d1a9e — CONTEC example terms

Original source: [https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280)

Summary: STEP / Open CASCADE ; STEP represents exchangeable CAD geometry; use AP242 where supported for product structure, geometry and PMI; test actual receiving application behavior. Manufacturer libraries frequently provide STEP, with separate download terms. ; STEP files from a manufacturer are not automatically openly licensed. CONTEC example terms restrict access/use to purchasers or prospective purchasers, bar adapting the data and disclaim warranty. ; Preserve native STEP plus supplier identity and terms. Import only within stated terms; derive a display/collision mesh only where permitted. Open CASCADE tooling is a geometry kernel/translator candidate, not a semantic library.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r04.md, research/workflows/details/dom-r06.md, research/workflows/details/dom-r07.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/details/mix-r04.md, research/workflows/details/mix-r05.md, research/workflows/details/mix-r08.md, research/workflows/details/mix-r10.md, research/workflows/domain-paths.md.

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

<a id="src-9bffb9dff56b"></a>

## SRC-9bffb9dff56b — OCS repository

Original source: [https://github.com/HakanSeven12/OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-9cfde96bb911"></a>

## SRC-9cfde96bb911 — csv — CSV file reading and writing — Python 3.15.2 documentation

Original source: [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)

Summary: Official Python documentation describes CSV readers and writers, configurable dialects and formatting parameters, and reader rows returned as strings by default. The QUOTE_NONNUMERIC option converts unquoted fields to floats. For intake, a declared dialect preserves field boundaries and reading as strings preserves source spellings for later interpretation. Parsing does not determine units, numeric locale or the meaning of a column.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-01-model-brief.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-04/intake-sources.json.

<a id="src-9df6cac46941"></a>

## SRC-9df6cac46941 — 🤖 Awesome GitHub Copilot

Original source: [https://raw.githubusercontent.com/github/awesome-copilot/main/README.md](https://raw.githubusercontent.com/github/awesome-copilot/main/README.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: 🤖 Awesome GitHub Copilot. Source class: repository README. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-9e57d453372b"></a>

## SRC-9e57d453372b — queue

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-9e9899193ac9"></a>

## SRC-9e9899193ac9 — Software review: confirmed dimensions and vector drawings to CAD

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-software.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-software.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-9ea228a27dc2"></a>

## SRC-9ea228a27dc2 — FreeCAD Assembly4-to-URDF exporter

Original source: [https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF](https://github.com/life-efficient/FreeCAD-Assembly4-to-URDF)

Summary: Third-party source describes Python scripts exporting Assembly4 assemblies to URDF; feature support and licence must be checked at the pinned revision.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/domain-paths.md.

<a id="src-9f9c7199168b"></a>

## SRC-9f9c7199168b — local project README

Original source: [https://github.com/HakanSeven12/OpenCADStudio/blob/main/README.md](https://github.com/HakanSeven12/OpenCADStudio/blob/main/README.md)

Summary: License observed locally: project `LICENSE` begins with GNU Affero General Public License version 3; source dependencies have their own licences. Primary sources: OCS repository, local project README, MCP automation guide, kernel body path note, Python plugin declaration. Local checkout was inspected rather than fetched from those URLs; source date for this report is 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-a07601074c08"></a>

## SRC-a07601074c08 — Point 03 source check: confirmed dimensions and vector drawings

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-sources.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-sources.md)

Summary: Point 03 Confirmed dimensions and vector drawings to CAD: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-a086c5a04ee4"></a>

## SRC-a086c5a04ee4 — README.md

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-a0ba78259618"></a>

## SRC-a0ba78259618 — PlankAssembly: Robust 3D Reconstruction from Three Orthographic Views with Learnt Shape Programs

Original source: [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html)

Summary: ICCV 2023 paper proposes a transformer/shape-program mapping from three orthographic views to CAD models and evaluates noisy/incomplete views on a benchmark dataset.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r05.md, research/workflows/details/cad-r09.md, research/workflows/details/mix-r08.md.

<a id="src-a1b86705dc1b"></a>

## SRC-a1b86705dc1b — Mesh API

Original source: [https://docs.blender.org/api/current/bpy.types.Mesh.html](https://docs.blender.org/api/current/bpy.types.Mesh.html)

Summary: Licence details for the upstream source, installed package and MCP integrations are recorded in domains and components. Primary sources: Blender repository/licence, Python API quickstart, Mesh API. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-a1e82dcf8fcb"></a>

## SRC-a1e82dcf8fcb — document_model.py

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/plugins/opencad-python/src/document_model.py](/home/leo/projects/3rdparty/OpenCADStudio/plugins/opencad-python/src/document_model.py)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-a22f0b43932b"></a>

## SRC-a22f0b43932b — Workflow and source register builder

Original source: [/home/leo/projects/3dmodeling/research/tools/build_workflow_register.py](/home/leo/projects/3dmodeling/research/tools/build_workflow_register.py)

Summary: Combines retained sources and round-specific evidence; checks operation inputs and recipe types; parses Markdown-link destinations separately from bare URLs to preserve original source addresses.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json, research/sources/round-04/audit-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

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

<a id="src-a3700fe5d4e2"></a>

## SRC-a3700fe5d4e2 — Skills Directory `majiayu000` 3D Modeling

Original source: [https://www.skillsdirectory.com/skills/majiayu000-3d-modeling-claude-skill-registry](https://www.skillsdirectory.com/skills/majiayu000-3d-modeling-claude-skill-registry)

Summary: Skills Directory `majiayu000` 3D Modeling ; Directory displays a copied 3D-art skill and 666 stars/25 copies/101 views. Registry's source-linked guide traces the canonical entry to `omer-metin/skills-for-antigravity/skills/3d-modeling/SKILL.md` and lists exact-content copies including `Kedhareswer/kedhar_brain/agents/skills/design-ui-ux/3d-modeling/SKILL.md`. The accessible source SKILL.md covers topology, UVs, game/film exports and art references. Registry page shows Apache-2.0 metadata for omer-metin's copy, while explicitly directing readers to check original permission; the exact original author's licence remains unverified. ; Mesh/art skill, not engineering CAD. Readable source copy was web-inspected; repository source and licence provenance were inspected via the registry guide. It has no stated CAD kernel or AI service dependency. Listing counts and security scan are directory claims, not CAD validation.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

<a id="src-a3e03c0d00b9"></a>

## SRC-a3e03c0d00b9 — cad — earthtojake/text-to-cad

Original source: [https://www.skills.sh/earthtojake/text-to-cad/cad](https://www.skills.sh/earthtojake/text-to-cad/cad)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: cad — earthtojake/text-to-cad. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

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

<a id="src-a635c02f99cb"></a>

## SRC-a635c02f99cb — OCS numerical contract checker source

Original source: [/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py](/home/leo/.codex/skills/ocs-engineering/scripts/check_contract.py)

Summary: Reads supplied point/axis/plane observations with one length/angular threshold pair per invocation; later adapter must preserve feature-specific applicability.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-a680edc6892e"></a>

## SRC-a680edc6892e — URDF model reference

Original source: [https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html](https://choreonoid.org/en/documents/latest/handling-models/modelfile/modelfile-urdf.html)

Summary: URDF / ROS tooling ; Official `urdf_tutorial` teaches visual geometry, movable joints, collision and inertial properties, and Xacro; it is BSD-3-Clause. Tutorial repository. URDF model guidance states metres/radians and kilograms for position/mass conventions. URDF model reference ; URDF is a format; package and mesh licenses are independent. Tutorial: BSD-3-Clause. ; Robot kinematic interchange and ROS visualization/control workflows. URDF does not express all closed-chain or advanced dynamics semantics; preserve source domain model and report unsupported fields.

Evidence: existing_report_registered.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-software.md, research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md, research/sources/round-02/domain-sources.json, research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r02.md, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/domain-paths.md.

<a id="src-a764655900e1"></a>

## SRC-a764655900e1 — FreeCAD contributing and licensing

Original source: [https://www.freecad.org/contributing.php?lang=eng](https://www.freecad.org/contributing.php?lang=eng)

Summary: Project license information; primary FreeCAD project page.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md.

<a id="src-a83674c889fd"></a>

## SRC-a83674c889fd — point-05-web-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-05/point-05-web-sources.json](/home/leo/projects/3dmodeling/research/sources/round-05/point-05-web-sources.json)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

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

<a id="src-ad1f82234be8"></a>

## SRC-ad1f82234be8 — Geometry Validation Rules

Original source: [https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/geometry_validation_rules.md](https://raw.githubusercontent.com/Foster1202/cad-modeling-fusion-skill/main/references/geometry_validation_rules.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Geometry Validation Rules. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ad3c319de0b3"></a>

## SRC-ad3c319de0b3 — plugin_host.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/src/app/plugin_host.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/app/plugin_host.rs)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-adb5f990a3ee"></a>

## SRC-adb5f990a3ee — Add-on listing

Original source: [https://www.freecad.org/addons.php?lang=en_EN](https://www.freecad.org/addons.php?lang=en_EN)

Summary: FreeCAD add-on step.parts connector ; FreeCAD listing describes searching an online open STEP parts catalog and inserting into the document. Add-on listing ; The connector's license is not sufficient evidence for every catalog asset's reuse rights. Capture item-level rights before caching or distributing.

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-ae16b67b352c"></a>

## SRC-ae16b67b352c — Coordinate Systems, Transformations and Units — SVG 2

Original source: [https://www.w3.org/TR/SVG2/coords.html](https://www.w3.org/TR/SVG2/coords.html)

Summary: The W3C SVG 2 specification defines each SVG viewport as a width/height drawing region in abstract user units. A `viewBox` transforms the user coordinate system relative to the viewport, and nested viewports and element `transform` properties add coordinate mappings. Absolute lengths follow CSS units; the specification defines 1 inch as 96 CSS pixels. SVG pixel or user-unit values therefore need their viewport, viewBox, nested transforms and physical-size interpretation retained before they become model dimensions.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-sources.md, research/sources/round-05/point-03-web-sources.json.

<a id="src-ae970b750172"></a>

## SRC-ae970b750172 — FreeCAD Topological Data Scripting (`Part` Module)

Original source: [https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/topological_scripting.md](https://raw.githubusercontent.com/glotoff/freecad-skills/main/skills/freecad-power-user/references/topological_scripting.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: FreeCAD Topological Data Scripting (`Part` Module). Source class: skill reference documentation. Original reuse terms: MIT; repository README attributes adapted docs to official FreeCAD documentation under CC-BY 3.0 / LGPL-2.1+; file-specific applicability not established; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-af8c2d79e989"></a>

## SRC-af8c2d79e989 — cad-r06.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r06.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r06.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-afa0b4d5a10b"></a>

## SRC-afa0b4d5a10b — domain-paths.json

Original source: [/home/leo/projects/3dmodeling/research/workflows/domain-paths.json](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-b00b92c70647"></a>

## SRC-b00b92c70647 — Depth Anything 3 — official repository, main branch

Original source: [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)

Summary: Official mutable main repository page inspected 2026-11-12. Documents monocular/multi-view depth, pose-conditioned depth, camera intrinsics/extrinsics estimation and `da3 video` CLI example with fps and GLB export options. Repository page advertises Apache-2.0 code; checkpoint/model terms remain model-specific.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-07-reconstruction.md, research/action-audit/reviews/point-07-designer.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/reconstruction.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/sources/round-05/point-07-web-sources.json, research/workflows/details/rec-r05.md.

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

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r08.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r08.md)

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-05-operations.json)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-b254a6b0bd67"></a>

## SRC-b254a6b0bd67 — Blender Scene API RNA source (main branch)

Original source: [https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_scene_api.cc](https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_scene_api.cc)

Summary: Official Blender RNA source defines Scene.ray_cast with a required depsgraph, world-space origin/direction and maximum distance. It documents evaluated geometry and outputs including hit boolean, location, normal, evaluated-mesh face index, original object and matrix. Location, normal and index correspond to the evaluated mesh; index can be -1 when original data is unavailable. The main-branch source does not identify an installed release.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

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

<a id="src-b37df47b9e75"></a>

## SRC-b37df47b9e75 — Unitree Go1 model BSD-3-Clause license

Original source: [https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_go1/LICENSE](https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_go1/LICENSE)

Summary: - Unitree Go1 model BSD-3-Clause license

Evidence: existing_report_registered.

Documents: research/domains-and-components.md.

<a id="src-b47fffcd39a7"></a>

## SRC-b47fffcd39a7 — 3D modeling implementation plan

Original source: [/home/leo/projects/3dmodeling/research/implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md)

Summary: Prior project proposal identifies OCS as the interactive baseline, FreeCAD for constrained feature trees, code-CAD for scripted solids, raster plans, drawing conversion and verification routes. Used as existing project context, not as runtime evidence.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-02/domain-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-b56bc21f14db"></a>

## SRC-b56bc21f14db — rec-r06.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r06.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r06.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-b5b5f2bbfc67"></a>

## SRC-b5b5f2bbfc67 — host.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/crates/ocs_plugin_api/src/host.rs](/home/leo/projects/3rdparty/OpenCADStudio/crates/ocs_plugin_api/src/host.rs)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-b6504258277a"></a>

## SRC-b6504258277a — Point 03 visual and evidence review — vectors, sketches and small solids

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-visual.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-03-visual.md)

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

<a id="src-b739e4946d72"></a>

## SRC-b739e4946d72 — MuJoCo model editing and MJZ

Original source: [https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst](https://github.com/google-deepmind/mujoco/blob/main/doc/programming/modeledit.rst)

Summary: Documents mjSpec editing, XML/URDF parsing, compilation, MJCF and asset packaging.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-visual.md, research/sources/round-02/domain-sources.json, research/workflows/details/dom-r03.md, research/workflows/details/mix-r02.md, research/workflows/details/mix-r03.md, research/workflows/domain-paths.md.

<a id="src-b7aa02d92193"></a>

## SRC-b7aa02d92193 — Local Python 3.14 JSON decoder source

Original source: [/usr/lib/python3.14/json/decoder.py](/usr/lib/python3.14/json/decoder.py)

Summary: Independent review inspected ordered pairs, dictionary conversion and nonfinite constants, supporting duplicate/nonfinite guards.

Evidence: local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

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

<a id="src-b914a224eaf5"></a>

## SRC-b914a224eaf5 — rec-r01.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r01.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-b9a7ffca5f8c"></a>

## SRC-b9a7ffca5f8c — skills.sh leaderboard

Original source: [https://www.skills.sh/](https://www.skills.sh/)

Summary: Skill catalogue sources inspected 2026-11-12: skills.sh leaderboard, glotoff/freecad-skills, reyk/freecad-ai-skill, mitsuhiko/agent-stuff, earthtojake/text-to-cad, Foster1202/cad-modeling-fusion-skill, and the installed OCS engineering skill. Existing findings are at `/home/leo/projects/energy/eoliennes/research/cad-workflow/`; source candidates are also archived under `/home/leo/projects/energy/raw/wind-prototypes/cad-workflow/skills/`. The detailed OCS harness findings describe an installed-build read-only inspection and existing API receipts; the skill research contains captured source files and hashes. These findings were reused, not reacquired or changed.

Evidence: existing_report_registered, archived_original_referenced.

Documents: research/cad-and-skills.md, research/sources/round-02/archive-sources.json.

<a id="src-ba1c34303c57"></a>

## SRC-ba1c34303c57 — https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md)

Summary: 3. https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md

Evidence: existing_report_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r04.md.

<a id="src-ba79f85a852f"></a>

## SRC-ba79f85a852f — Action-by-action workflow audit

Original source: [/home/leo/projects/3dmodeling/research/action-audit/README.md](/home/leo/projects/3dmodeling/research/action-audit/README.md)

Summary: Authored audit document recording Action-by-action workflow audit. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json.

<a id="src-bad31f6c036a"></a>

## SRC-bad31f6c036a — Point 03 — Confirmed dimensions and vector drawings to small CAD models

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md)

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

<a id="src-bc2defd7afa9"></a>

## SRC-bc2defd7afa9 — Raster-to-Graph floor-plan recognition

Original source: [https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf)

Summary: Computer Graphics Forum paper describes a learned raster-floorplan framework that predicts wall junctions and segments as an ordered graph representation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md.

<a id="src-bc59d9c5c5c8"></a>

## SRC-bc59d9c5c5c8 — Point 05 visual and evidence review — existing CAD with photographs and scans

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-visual.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-visual.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-bcf9f8ff8137"></a>

## SRC-bcf9f8ff8137 — source repository and GPL licence

Original source: [https://github.com/solvespace/solvespace](https://github.com/solvespace/solvespace)

Summary: Primary source: SolveSpace official site, source repository and GPL licence. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-bd0f14e5688e"></a>

## SRC-bd0f14e5688e — README.md

Original source: [/home/leo/projects/architecture/research/README.md](/home/leo/projects/architecture/research/README.md)

Summary: Existing local source inspected in the initial research; its use is described in research/local-baseline.md.

Evidence: local_source_inspected, existing_report_registered, local_reference_registered.

Documents: research/local-baseline.md, research/sources/local-evidence.json, research/sources/round-02/cad-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-bda744cda1c8"></a>

## SRC-bda744cda1c8 — `skills/cad/SKILL.md`

Original source: [https://github.com/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md)

Summary: `cad` from `earthtojake/text-to-cad` ; Archived `skills/cad/SKILL.md` uses `cadgen` wrappers around build123d/OCCT, Python model scripts, STEP/mesh export, a CAD Viewer and local `cadgen mcp`. README pins Python 3.13 and `cadgen==0.7.25` in its command examples; `uvx` downloads managed runtime/dependencies. It says first run needs network. Usage statistics and crash reports are on by default with random install IDs; README says turn off using `uvx cadgen telemetry off`. Core modeling path is local after runtime download; optional manufacturing-service integrations are separate. Repository and skill licence are MIT. ; Strong candidate for an optional build123d-backed modeling and inspection path, with telemetry disabled or disclosed and the pinned environment audited. It brings its own runtime/server/viewer and is not only a prompt skill. The source supports editable Python source and exact B-rep through build123d/OCCT; exported meshes remain tessellated. Source links: `skills/cad/SK...

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-be135dffe792"></a>

## SRC-be135dffe792 — Point 02 — Procedure designer notes

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-designer.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-designer.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

<a id="src-bec11051e812"></a>

## SRC-bec11051e812 — SKILL.md — documented_skill

Original source: [/home/leo/projects/ferme/skills/cad-construction/SKILL.md](/home/leo/projects/ferme/skills/cad-construction/SKILL.md)

Summary: Reusable source, component/frame, construction, feature-check and saved-file procedure. Applicability: Repository skill instructions and reproduction-package specification.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-bec1fb0c7b0c"></a>

## SRC-bec1fb0c7b0c — freshtechbro `web3d-integration-patterns/SKILL.md`

Original source: [https://github.com/freshtechbro/claudedesignskills/blob/main/.claude/skills/web3d-integration-patterns/SKILL.md](https://github.com/freshtechbro/claudedesignskills/blob/main/.claude/skills/web3d-integration-patterns/SKILL.md)

Summary: freshtechbro `web3d-integration-patterns/SKILL.md` (raw source) ; Raw source describes integration patterns for Three.js, GSAP ScrollTrigger, React Three Fiber, Motion and React Spring. It includes browser scene setup, render loops, state coordination, scroll animation and performance patterns; references the constituent library skills. ; Web scene and animation skill, not CAD. Its listed tools require JavaScript/npm packages and browser runtime. The page identifies no hosted AI or geometry-generation API. Repository-wide licence was not checked in this pass; no source copying recommended. Raw SKILL.md was web-inspected on 2026-11-12, not downloaded.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md, research/user-supplied-links.md.

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

<a id="src-bfd136961cc3"></a>

## SRC-bfd136961cc3 — Nerfstudio installation and CLI examples

Original source: [https://docs.nerf.studio/quickstart/installation.html](https://docs.nerf.studio/quickstart/installation.html)

Summary: Official install guide documents CLI environment and a video-processing command; used only for documented CLI context, no installation was run.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/domain-detail-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r08.md.

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

<a id="src-c026420b57f4"></a>

## SRC-c026420b57f4 — ifcopenshell.api.geometry.add_representation — IfcOpenShell 0.9.0post1 documentation

Original source: [https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_representation/index.html)

Summary: IfcOpenShell 0.9.0post1 API reference accessed 2026-11-12. `add_representation` takes an IFC context and Blender object/data geometry, optional SI offset and unit scale, and returns an IfcShapeRepresentation or None. API dependency and output do not amount to product classification, placement or relationship creation.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-c057807eb5f6"></a>

## SRC-c057807eb5f6 — cad-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-02/cad-sources.json](/home/leo/projects/3dmodeling/research/sources/round-02/cad-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json.

<a id="src-c0ffb325c952"></a>

## SRC-c0ffb325c952 — Snapshot review

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/snapshot-review.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/snapshot-review.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Snapshot review. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c14ca78d0641"></a>

## SRC-c14ca78d0641 — Software review: existing components and CAD files to inspected reusable inputs

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-software.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-02-software.md)

Summary: Point 02 Existing components and CAD reuse: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-02-local-sources.json.

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

<a id="src-c2f8f1ee81fd"></a>

## SRC-c2f8f1ee81fd — acis_export.rs

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/src/scene/convert/acis_export.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/scene/convert/acis_export.rs)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-c2fb7b743a7c"></a>

## SRC-c2fb7b743a7c — build123d modeling patterns

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/build123d-modeling.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/build123d-modeling.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: build123d modeling patterns. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c325f62a1a2e"></a>

## SRC-c325f62a1a2e — Python scripting tutorial

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Python_scripting_tutorial.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Python_scripting_tutorial.md)

Summary: Primary sources: FreeCAD source/licence, Sketcher Python scripting, Part scripting, Python scripting tutorial, Part Design concepts. Inspected 2026-11-12.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-c49f0a4410c4"></a>

## SRC-c49f0a4410c4 — Installed CAD and computational engineering command availability inventory

Original source: [/home/leo/projects/energy/raw/wind-prototypes/cad-workflow/harness/installed-tools-path-inventory.json](/home/leo/projects/energy/raw/wind-prototypes/cad-workflow/harness/installed-tools-path-inventory.json)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: Installed CAD and computational engineering command availability inventory. Source class: read-only local PATH lookup and version probes. Original reuse terms: not applicable; locally generated environment observation

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c4bd2d7b4e79"></a>

## SRC-c4bd2d7b4e79 — Interpreting a CAD request

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/cad-brief.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/cad-brief.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Interpreting a CAD request. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c5c9d3ec5705"></a>

## SRC-c5c9d3ec5705 — OpenCADStudio 2026.42 generated capability, command, and record-schema responses

Original source: [/home/leo/projects/energy/raw/wind-prototypes/cad-workflow/harness/installed-2026.42-readonly-api-receipts.json](/home/leo/projects/energy/raw/wind-prototypes/cad-workflow/harness/installed-2026.42-readonly-api-receipts.json)

Summary: Existing archived source for OCS automation documentation and historical installed-capability receipts: OpenCADStudio 2026.42 generated capability, command, and record-schema responses. Source class: read-only live runtime API observation; not product documentation. Original reuse terms: not applicable; locally generated observation of installed application output

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-c65b8007a000"></a>

## SRC-c65b8007a000 — Nerfstudio export geometry

Original source: [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md)

Summary: Documents ns-export pointcloud to PLY, TSDF meshes as available for all models, Poisson meshes only for models predicting normals, OBJ textured meshes and NeRF texture transfer to existing meshes.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-07-software.md, research/action-audit/reviews/point-07-visual.md, research/sources/round-02/reconstruction-sources.json, research/sources/round-03/reconstruction-detail-sources.json, research/workflows/details/rec-r08.md.

<a id="src-c70fd33bd9df"></a>

## SRC-c70fd33bd9df — Operations — build123d 0.13.1.dev341+gc0fb3a896 documentation

Original source: [https://build123d.readthedocs.io/en/latest/operations.html](https://build123d.readthedocs.io/en/latest/operations.html)

Summary: Official build123d documentation says operations accept existing objects and return new objects; `extrude()` creates a 3D Part from a Sketch or Face, using a specified amount/direction or an `until` target. Operations work through Algebra and Builder APIs over build123d objects. This is kernel-part construction documentation, not a constraint-solving sketch API claim or an observed validity result. The page's `latest` documentation reported a development version at access.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-c748eeb196bb"></a>

## SRC-c748eeb196bb — rec-r05.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r05.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r05.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-c75f41a7dcd4"></a>

## SRC-c75f41a7dcd4 — https://github.com/alicevision/Meshroom/blob/develop/COPYING.md

Original source: [https://github.com/alicevision/Meshroom/blob/develop/COPYING.md](https://github.com/alicevision/Meshroom/blob/develop/COPYING.md)

Summary: - Meshroom copying/licenses: https://github.com/alicevision/Meshroom/blob/develop/COPYING.md

Evidence: existing_report_registered.

Documents: research/reconstruction.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r06.md.

<a id="src-c7a5d7a2632d"></a>

## SRC-c7a5d7a2632d — rec-r08.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r08.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r08.md)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered, local_source_inspected.

Documents: research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-c9c50a504fb8"></a>

## SRC-c9c50a504fb8 — json — JSON encoder and decoder — Python 3.15.2 documentation

Original source: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)

Summary: Official Python documentation describes JSON decoding, default conversions, custom parse_float and parse_int callbacks receiving numeric token strings, parse_constant for NaN/Infinity tokens, object_pairs_hook receiving ordered object pairs, and JSONDecodeError for malformed documents. By default, the decoder accepts NaN/Infinity extensions and repeated object names, keeping only the last repeated value. For strict intake, a caller can reject constants and inspect pairs to detect duplicate names. Decoding exposes structure and syntax; it does not assign units, feature identity or engineering meaning.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-01-model-brief.md, research/action-audit/reviews/software-review.md, research/action-audit/reviews/source-check.md, research/sources/round-04/intake-sources.json.

<a id="src-ca3076996fa5"></a>

## SRC-ca3076996fa5 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill](https://api.github.com/repos/Foster1202/cad-modeling-fusion-skill)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

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

<a id="src-cb5cec23d032"></a>

## SRC-cb5cec23d032 — Workflow routes linked to detailed actions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.md](/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-ccbf0b22fcf6"></a>

## SRC-ccbf0b22fcf6 — cad-r10.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/cad-r10.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r10.md)

Summary: Existing local source cited by point 03 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-03-local-sources.json.

<a id="src-cce96de57cbe"></a>

## SRC-cce96de57cbe — Ideas

Original source: [/home/leo/projects/3dmodeling/research/action-audit/ideas.json](/home/leo/projects/3dmodeling/research/action-audit/ideas.json)

Summary: Authored audit document recording Ideas. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-cd7868332c03"></a>

## SRC-cd7868332c03 — `SKILL.md`

Original source: [https://github.com/Foster1202/cad-modeling-fusion-skill/blob/main/SKILL.md](https://github.com/Foster1202/cad-modeling-fusion-skill/blob/main/SKILL.md)

Summary: `cad-modeling-fusion` (`Foster1202/cad-modeling-fusion-skill`) ; Archived `SKILL.md` and README describe a ModelSpec JSON validated by Python scripts, generators for Autodesk Fusion, FreeCAD and OpenSCAD, STEP/STL/OBJ export attempts, and optional Computer Use for Fusion. Python core uses standard library; backend application required only to run its generated code. Root licence is MIT. ; Consider its intermediate ModelSpec/validation structure, but route output to FreeCAD/OpenSCAD only and do not require Fusion. Backends have different semantics and may emit approximations; inspect output and generated warnings. Source link: `SKILL.md`. Archived local skill and references were inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-cd8d24d026d3"></a>

## SRC-cd8d24d026d3 — Point 05 — Alignment and parametric remodeling

Original source: [/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md](/home/leo/projects/3dmodeling/research/action-audit/point-05-alignment-and-remodeling.md)

Summary: Point 05 CAD, photographs and scans alignment: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-ce0594707cbb"></a>

## SRC-ce0594707cbb — item-angle-bracket-set-41115-native.json — recorded_check_results

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-angle-bracket-set-41115-native.json)

Summary: Retained feature/audit observations for the named component. Applicability: Pre-save stage; transfer conditions are retained in the matching report.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-ce70036fb35b"></a>

## SRC-ce70036fb35b — 3D modeling

Original source: [/home/leo/projects/3dmodeling/README.md](/home/leo/projects/3dmodeling/README.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-ce92c7f02e89"></a>

## SRC-ce92c7f02e89 — OpenSCAD documentation

Original source: [https://openscad.org/documentation.html](https://openscad.org/documentation.html)

Summary: Documents OpenSCAD source and command-line usage for rendering/exporting geometry.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/reviews/point-03-visual.md, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r10.md.

<a id="src-cfeb029989f0"></a>

## SRC-cfeb029989f0 — Point 04 source check: raster interpretation, orthographic views and IFC

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-sources.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-sources.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-d130021486e1"></a>

## SRC-d130021486e1 — PicoGK upstream LICENSE file

Original source: [https://raw.githubusercontent.com/leap71/PicoGK/main/LICENSE](https://raw.githubusercontent.com/leap71/PicoGK/main/LICENSE)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: PicoGK upstream LICENSE file. Source class: official repository license original, plain text. Original reuse terms: Apache License 2.0; preserve the complete license text and notices.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-d1c0e9f5deef"></a>

## SRC-d1c0e9f5deef — Authorized cleanup of newly authored examples

Original source: [/home/leo/projects/3dmodeling/research/cleanup-record.md](/home/leo/projects/3dmodeling/research/cleanup-record.md)

Summary: Records the removal of 13 example files, verified original Git revision and SHA-256 values, prior scope finding and replacement of active example references with documented third-party APIs.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-d25b3e6e0e1d"></a>

## SRC-d25b3e6e0e1d — workflow-to-actions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.json](/home/leo/projects/3dmodeling/research/action-audit/workflow-to-actions.json)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected, local_source_inspected.

Documents: research/sources/round-05/audit-index-sources.json, research/sources/round-06/implementation-queue-sources.json.

<a id="src-d25c92b0aebf"></a>

## SRC-d25c92b0aebf — PicoGK official repository page and README

Original source: [https://github.com/leap71/PicoGK](https://github.com/leap71/PicoGK)

Summary: Existing archived source for procedural geometry and computational-engineering source assessment: PicoGK official repository page and README. Source class: official repository page containing README excerpt and repository metadata. Original reuse terms: Repository identifies Apache-2.0; the archive contains the repository page, not the full LICENSE text. Preserve upstream copyright and notices; exact licence terms require the original LICENSE file.

Evidence: archived_original_referenced, existing_report_registered.

Documents: research/sources/round-02/archive-sources.json, research/sources/round-02/project-sources.json.

<a id="src-d32e74eebf36"></a>

## SRC-d32e74eebf36 — build_item_profile_segment.py — existing_component_code

Original source: [/tmp/opencode/build_item_profile_segment.py](/tmp/opencode/build_item_profile_segment.py)

Summary: contours samples retained text curves and normalizes the section; build/complete/verify construct and check the profile. Applicability: Uses extracted contour text rather than a DXF parser; fixed 40 mm normalization, 100 mm length, output paths, session wrapper and component checks.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

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

<a id="src-d52309ad63a6"></a>

## SRC-d52309ad63a6 — combined-details.json

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/combined-details.json](/home/leo/projects/3dmodeling/research/workflows/details/combined-details.json)

Summary: Ten proposed combined workflow dossiers with source-backed operations, frame controls, tool/API entry points, resource conditions and relative classifications.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-d526125ac341"></a>

## SRC-d526125ac341 — Source check: intake operations

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/source-check.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/source-check.md)

Summary: Authored audit document recording Source check: intake operations. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-d5265b630533"></a>

## SRC-d5265b630533 — find-skills — skill discovery workflow

Original source: [/home/leo/.agents/skills/find-skills/SKILL.md](/home/leo/.agents/skills/find-skills/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: find-skills — skill discovery workflow. Source class: local discovery skill instructions. Original reuse terms: Local instructions; referenced in place without duplication.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-d6bb83cc4fbe"></a>

## SRC-d6bb83cc4fbe — setup page

Original source: [https://projects.blender.org/lab/blender_mcp/wiki/Setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

Summary: The Blender-hosted Blender Lab MCP repository is the Blender project's own integration. Its README describes a two-process bridge: an MCP server launched by the client communicates over stdio and relays requests by TCP socket to a Blender add-on. The add-on executes requests inside Blender; the project exposes Blender Python execution and scene/file inspection tools. The repository license is GPL-3.0-or-later. Its setup page requires Blender 5.1 or newer. The installed workstation Blender is 5.0.1 (`/bin/blender --version`); this version is below the documented minimum, so the Blender Lab add-on has a version mismatch with the current installation. The Blender Lab MCP page search result states that generated code runs without guards against deleting data or sending it remotely; direct page open returned HTTP 403. Blender's scripting security guidance says Python scripts can perform unrestricted operations.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-06-visual.md, research/domains-and-components.md.

<a id="src-d7af850e4bd9"></a>

## SRC-d7af850e4bd9 — Independent review — Point 04 raster drawings and interpreted dimensions

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-independent.md)

Summary: Point 04 Raster drawings and interpreted dimensions: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-d8bff2262475"></a>

## SRC-d8bff2262475 — XML Reference — MuJoCo Documentation

Original source: [https://mujoco.readthedocs.io/en/stable/XMLreference.html](https://mujoco.readthedocs.io/en/stable/XMLreference.html)

Summary: Stable XML reference accessed 2026-11-12; exact local release not checked. Documents MJCF angle default degrees versus URDF radians, compiler defaults, inertia fields/frames, mesh file types and inference modes, kinematic tree and equality constraints. `fullinertia` order is M11,M22,M33,M12,M13,M23 and is diagonalized by compilation. Compiler centers meshes and aligns principal axes; `mjModel.mesh_pos`, `mesh_quat` and `mesh_scale` preserve asset transforms to compose with geom pose.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-06-building-and-robot.md, research/action-audit/reviews/point-06-designer.md, research/action-audit/reviews/point-06-software.md, research/sources/round-05/point-06-web-sources.json.

<a id="src-d928392d886f"></a>

## SRC-d928392d886f — build_workflow_details.py

Original source: [/home/leo/projects/3dmodeling/research/tools/build_workflow_details.py](/home/leo/projects/3dmodeling/research/tools/build_workflow_details.py)

Summary: Documentation renderer validating recipe coverage, classification values and source references; builds workflow pages and independent sorted tables.

Evidence: local_source_inspected.

Documents: research/sources/round-03/project-detail-sources.json.

<a id="src-d9490cdbdfa2"></a>

## SRC-d9490cdbdfa2 — https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1

Original source: [https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1)

Summary: - Hunyuan3D-2.1 repository and model usage: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

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

<a id="src-db98256a44dd"></a>

## SRC-db98256a44dd — Point 07 independent review — photographs, depth and learned reconstruction

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-independent.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-07-independent.md)

Summary: Point 07 Photographs, depth and learned reconstruction: authored procedure/action contracts or source-linked review. Contains the exact proposed software/agent assignments, alternatives, checks and evidence status.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/point-07-local-sources.json.

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

<a id="src-dcc824a0bc1a"></a>

## SRC-dcc824a0bc1a — BOSL2 repository

Original source: [https://github.com/BelfrySCAD/BOSL2](https://github.com/BelfrySCAD/BOSL2)

Summary: BOSL2 ; Parametric OpenSCAD shapes, masks and manipulators; OpenSCAD library catalog identifies BSD-2-Clause. Repository describes it as beta. BOSL2 repository ; BSD-2-Clause per official catalog; check repository license/version when vendoring. Parametric code is useful for generated primitives and fixtures, not a catalog of measured commercial hardware.

Evidence: existing_report_registered.

Documents: research/action-audit/reviews/point-02-visual.md, research/domains-and-components.md.

<a id="src-dd1f5b2ca39f"></a>

## SRC-dd1f5b2ca39f — FreeCAD Draft DXF documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md)

Summary: Official FreeCAD docs list DXF entity support for C++ and legacy importers, format/version conditions, and note that 3D ACIS SAT blobs in DXF are not currently read by FreeCAD.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-visual.md, research/sources/round-02/cad-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/mix-r02.md.

<a id="src-ddbe71fda666"></a>

## SRC-ddbe71fda666 — workflow details

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/workflow-details.json](/home/leo/projects/3dmodeling/research/workflows/details/workflow-details.json)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-ddc04ee3002f"></a>

## SRC-ddc04ee3002f — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/glotoff/freecad-skills](https://api.github.com/repos/glotoff/freecad-skills)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-df6405fd9570"></a>

## SRC-df6405fd9570 — computational-engineering.md

Original source: [/home/leo/.codex/skills/ocs-engineering/references/computational-engineering.md](/home/leo/.codex/skills/ocs-engineering/references/computational-engineering.md)

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

Original source: [/home/leo/projects/3dmodeling/research/sources/round-05/point-04-web-sources.json](/home/leo/projects/3dmodeling/research/sources/round-05/point-04-web-sources.json)

Summary: Existing local source cited by point 04 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-04-local-sources.json.

<a id="src-dfe7c160f462"></a>

## SRC-dfe7c160f462 — OCS model contract

Original source: [/home/leo/.codex/skills/ocs-engineering/references/model-contract.md](/home/leo/.codex/skills/ocs-engineering/references/model-contract.md)

Summary: Requirements for units, frames, source corrections, parts, tolerances and supplied numerical check observations.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json, research/sources/round-05/point-07-local-sources.json.

<a id="src-dfeba86ef6d2"></a>

## SRC-dfeba86ef6d2 — point-07-web-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-05/point-07-web-sources.json](/home/leo/projects/3dmodeling/research/sources/round-05/point-07-web-sources.json)

Summary: Existing local source cited by point 07 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-07-local-sources.json.

<a id="src-e1ca3a166ec3"></a>

## SRC-e1ca3a166ec3 — Inspecting and checking saved CAD in Python

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/inspection-and-validation.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/references/inspection-and-validation.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Inspecting and checking saved CAD in Python. Source class: skill reference documentation. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-e24faff4c00b"></a>

## SRC-e24faff4c00b — Point 05 source check: calibration, scan alignment and coordinate frames

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-sources.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-05-sources.md)

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/operation-inventory.json](/home/leo/projects/3dmodeling/research/action-audit/operation-inventory.json)

Summary: Authored audit document recording Operation Inventory. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json, research/sources/round-05/audit-index-sources.json.

<a id="src-e3d95e78d033"></a>

## SRC-e3d95e78d033 — https://github.com/Tencent-Hunyuan/Hunyuan3D-2

Original source: [https://github.com/Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)

Summary: - Hunyuan3D-2 source and current community license: https://github.com/Tencent-Hunyuan/Hunyuan3D-2

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-e5af12a0873d"></a>

## SRC-e5af12a0873d — Research and proposed implementation

Original source: [/home/leo/projects/3dmodeling/research/README.md](/home/leo/projects/3dmodeling/research/README.md)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

<a id="src-e618fbde3a91"></a>

## SRC-e618fbde3a91 — https://fal.ai/models/fal-ai/sam-3/3d-objects/api

Original source: [https://fal.ai/models/fal-ai/sam-3/3d-objects/api](https://fal.ai/models/fal-ai/sam-3/3d-objects/api)

Summary: - Underlying SAM 3D model service https://fal.ai/models/fal-ai/sam-3/3d-objects/api — official Fal endpoint documentation opened. It requires an API key and sends an image URL or uploaded/base64 image to a hosted API; output schema includes Gaussian splat PLY, GLB mesh, metadata and optional per-object results. This is cloud inference, not a local reconstruction workflow. The endpoint advertises commercial use; that is Fal's service claim and does not by itself establish whether this endpoint uses the exact upstream Meta checkpoint or the terms governing output reuse. The API accepts optional pointmap/depth input, but this does not make output metrically validated.

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-e74aa94bbb50"></a>

## SRC-e74aa94bbb50 — Procedure-design review notes — Point 01 model brief

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/designer-notes.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/designer-notes.md)

Summary: Authored audit document recording Procedure-design review notes — Point 01 model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

<a id="src-e796d575e829"></a>

## SRC-e796d575e829 — Software review: descriptions and dimensions to a model brief

Original source: [/home/leo/projects/3dmodeling/research/action-audit/reviews/software-review.md](/home/leo/projects/3dmodeling/research/action-audit/reviews/software-review.md)

Summary: Authored audit document recording Software review: descriptions and dimensions to a model brief. Includes source links, evidence status and its relationship to the first-point procedure and operation inventory.

Evidence: authored_document_inspected.

Documents: research/sources/round-04/audit-local-sources.json.

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

<a id="src-e935d3ebe64f"></a>

## SRC-e935d3ebe64f — FreeCAD Import Export Preferences documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md)

Summary: The FreeCAD documentation describes STEP import structure choices including assembly per document and object per document, options for link groups, instance names and compound expansion, and export settings for STEP length units and application protocol. It identifies AP203 as mechanical parts and assemblies and AP214 as automotive mechanical design. It states that single-object placement can be embedded in shape geometry on reimport. These are documented UI preferences; the archived documentation page does not prove a selected FreeCAD build, Python API behavior, or lossless unit and hierarchy transfer.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-02-component-reuse.md, research/action-audit/reviews/point-02-designer.md, research/action-audit/reviews/point-02-software.md, research/action-audit/reviews/point-02-sources.md, research/sources/round-03/domain-detail-sources.json, research/sources/round-05/point-02-web-sources.json, research/workflows/details/dom-r02.md.

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

<a id="src-eb880f7efbac"></a>

## SRC-eb880f7efbac — /home/leo/.codex/skills/ocs-engineering/references/ocs-control.md

Original source: [/home/leo/.codex/skills/ocs-engineering/references/ocs-control.md](/home/leo/.codex/skills/ocs-engineering/references/ocs-control.md)

Summary: Source referenced for the stated workflow; see the owning documentation or research item.

Evidence: existing_report_registered, local_source_inspected, local_reference_registered.

Documents: research/sources/round-03/cad-detail-sources.json, research/sources/round-04/audit-local-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json, research/sources/round-05/point-05-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-ebd6e769a79a"></a>

## SRC-ebd6e769a79a — `freecad-user/SKILL.md`

Original source: [https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-user/SKILL.md](https://github.com/glotoff/freecad-skills/blob/main/skills/freecad-user/SKILL.md)

Summary: FreeCAD skills suite (`glotoff/freecad-skills`) ; Archived `freecad-user/SKILL.md` routes UI/modeling/workbench/import-export and topological naming guidance; `freecad-power-user/SKILL.md` covers Python, Part/Sketcher/Draft, B-rep, FeaturePython and headless/RPC automation; `freecad-developer/SKILL.md` covers C++ build/workbench development. README says skills derive from official FreeCAD documentation. Root skill suite licence is MIT; copied FreeCAD docs have separate attribution/licensing. ; Adapt `freecad-user` and `freecad-power-user` selectively as a complementary parametric backend; `developer` is outside normal modeling scope. The supplied suite is knowledge guidance, not tested evidence that generated files meet requirements. Source links: `freecad-user/SKILL.md`, `freecad-power-user/SKILL.md`, `freecad-developer/SKILL.md`. Archived local files were inspected.

Evidence: existing_report_registered.

Documents: research/cad-and-skills.md.

<a id="src-ebf77b364ed5"></a>

## SRC-ebf77b364ed5 — OpenCV image processing feature detection

Original source: [https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html)

Summary: Official API documents probabilistic HoughLinesP on binary images and returns line-segment endpoint coordinates in pixel space.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-04-raster-drawings.md, research/action-audit/reviews/point-04-designer.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-04-visual.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/workflows/details/cad-r02.md, research/workflows/details/cad-r03.md, research/workflows/details/mix-r01.md, research/workflows/details/mix-r08.md.

<a id="src-ecc97be7318c"></a>

## SRC-ecc97be7318c — point-06-web-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-05/point-06-web-sources.json](/home/leo/projects/3dmodeling/research/sources/round-05/point-06-web-sources.json)

Summary: Existing local source cited by point 06 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-06-local-sources.json.

<a id="src-ece5f904e49d"></a>

## SRC-ece5f904e49d — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/glotoff/freecad-skills/git/trees/HEAD?recursive=1](https://api.github.com/repos/glotoff/freecad-skills/git/trees/HEAD?recursive=1)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API recursive tree response. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ed09b653131a"></a>

## SRC-ed09b653131a — openscad — mitsuhiko/agent-stuff

Original source: [https://www.skills.sh/mitsuhiko/agent-stuff/openscad](https://www.skills.sh/mitsuhiko/agent-stuff/openscad)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: openscad — mitsuhiko/agent-stuff. Source class: skills.sh skill directory page. Original reuse terms: No separate reuse license was identified in the saved page; retain for provenance and do not reproduce page content.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ede9c64cd596"></a>

## SRC-ede9c64cd596 — rec-r09.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r09.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r09.md)

Summary: Existing local source cited by point 05 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-05-local-sources.json.

<a id="src-ee88cef821b6"></a>

## SRC-ee88cef821b6 — GitHub repository metadata or tree response

Original source: [https://api.github.com/repos/earthtojake/text-to-cad](https://api.github.com/repos/earthtojake/text-to-cad)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: GitHub repository metadata or tree response. Source class: GitHub REST API repository metadata. Original reuse terms: GitHub API response retained as a provenance record; no separate reuse claim made.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-ef7f25d50b37"></a>

## SRC-ef7f25d50b37 — item-profile-02633-segment-100mm.md — recorded_execution_report

Original source: [/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md](/home/leo/projects/ferme/engineering/module-development/cad/checks/item-profile-02633-segment-100mm.md)

Summary: Component-specific native checks, save/reopen observations and source paths for OCS 2026.42. Applicability:

Evidence: local_source_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-f06d3b316cfc"></a>

## SRC-f06d3b316cfc — rec-r04.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/rec-r04.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r04.md)

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

Original source: [/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/assets.json](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/assets.json)

Summary: Authoritative existing action/route record or authored implementation-queue record: individual action boundaries, original input contracts, source/code evidence, qualitative order or first-task implementation proposal. Revision scope is this batch.

Evidence: authored_document_inspected.

Documents: research/sources/round-06/implementation-queue-sources.json.

<a id="src-f5b26686d5af"></a>

## SRC-f5b26686d5af — Cargo.toml

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/Cargo.toml](/home/leo/projects/3rdparty/OpenCADStudio/Cargo.toml)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

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

<a id="src-f77f55667d7d"></a>

## SRC-f77f55667d7d — domain-sources.json

Original source: [/home/leo/projects/3dmodeling/research/sources/round-02/domain-sources.json](/home/leo/projects/3dmodeling/research/sources/round-02/domain-sources.json)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-f7e7cce18547"></a>

## SRC-f7e7cce18547 — Blender Object API RNA source (main branch)

Original source: [https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_object_api.cc](https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_object_api.cc)

Summary: Official Blender RNA source defines Object.ray_cast with object-space origin/direction, maximum distance and optional depsgraph for evaluated mesh access. It returns hit boolean, location, normal and face index. This query is against evaluated object geometry in object-space, not a physical measurement; the mutable main-branch source does not pin an installed release.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/point-05-alignment-and-remodeling.md, research/action-audit/reviews/point-05-designer.md, research/action-audit/reviews/point-05-sources.md, research/sources/round-05/point-05-web-sources.json.

<a id="src-f828b291cc6f"></a>

## SRC-f828b291cc6f — OpenCADStudio MCP automation guide

Original source: [/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md)

Summary: Local OCS guide describes stdio MCP and drawing inspection, mutation, measurements, audits and verified save. It supports application-level drawing workflow claims.

Evidence: local_source_inspected, local_reference_registered.

Documents: research/sources/round-02/cad-sources.json, research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-03-local-sources.json, research/sources/round-05/point-04-local-sources.json.

<a id="src-f954ab80c148"></a>

## SRC-f954ab80c148 — Agent skill: cad

Original source: [https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/SKILL.md](https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/SKILL.md)

Summary: Existing archived source for CAD skill source instructions, references, marketplace discovery and repository metadata: Agent skill: cad. Source class: agent skill instructions. Original reuse terms: MIT; attribution and notice retained locally.

Evidence: archived_original_referenced.

Documents: research/sources/round-02/archive-sources.json.

<a id="src-f9e1dbc024e2"></a>

## SRC-f9e1dbc024e2 — dom-r02.md

Original source: [/home/leo/projects/3dmodeling/research/workflows/details/dom-r02.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r02.md)

Summary: Existing local source cited by point 02 procedure/reviews; its concrete claim and operation relationship are preserved in those referring documents. This record captures source bytes at integration.

Evidence: local_reference_registered.

Documents: research/sources/round-05/point-02-local-sources.json, research/sources/round-05/point-06-local-sources.json.

<a id="src-fa8c58e8c7a1"></a>

## SRC-fa8c58e8c7a1 — Open3D licence

Original source: [https://github.com/isl-org/Open3D/blob/main/LICENSE](https://github.com/isl-org/Open3D/blob/main/LICENSE)

Summary: Primary source gives Open3D MIT licence; third-party dependencies remain separately governed.

Evidence: existing_report_registered, web_inspected.

Documents: research/sources/round-03/domain-detail-sources.json, research/workflows/details/dom-r01.md.

<a id="src-fbf7ed489d76"></a>

## SRC-fbf7ed489d76 — https://arxiv.org/abs/2403.02151

Original source: [https://arxiv.org/abs/2403.02151](https://arxiv.org/abs/2403.02151)

Summary: - TripoSR research paper: https://arxiv.org/abs/2403.02151

Evidence: existing_report_registered.

Documents: research/reconstruction.md.

<a id="src-fcdc74aed22e"></a>

## SRC-fcdc74aed22e — FreeCAD Sketcher scripting documentation

Original source: [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)

Summary: The FreeCAD scripting page shows `Sketcher::SketchObject`, `addGeometry`, `addConstraint` with a Coincident constraint, and `doc.recompute()`. The example adds three line segments and one coincidence relation; it demonstrates API construction, not a closed or fully constrained profile or solver-status check. The page is in the FreeCAD documentation repository, which GitHub reports was archived on 2026-04-01.

Evidence: existing_report_registered, web_inspected.

Documents: research/action-audit/implementation-queue/queue.md, research/action-audit/point-03-vector-and-solid.md, research/action-audit/reviews/point-03-designer.md, research/action-audit/reviews/point-03-software.md, research/action-audit/reviews/point-03-sources.md, research/action-audit/reviews/point-03-visual.md, research/action-audit/reviews/point-04-software.md, research/action-audit/reviews/point-05-software.md, research/action-audit/reviews/visual-review.md, research/cad-and-skills.md, research/sources/round-02/cad-sources.json, research/sources/round-03/cad-detail-sources.json, research/sources/round-05/point-03-web-sources.json, research/workflows/details/cad-r01.md, research/workflows/details/cad-r02.md, research/workflows/details/cad-r04.md, research/workflows/details/cad-r05.md, research/workflows/details/cad-r09.md, research/workflows/details/mix-r02.md.

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

<a id="src-fe980d416f56"></a>

## SRC-fe980d416f56 — sequence

Original source: [/home/leo/projects/3dmodeling/research/action-audit/sequence.json](/home/leo/projects/3dmodeling/research/action-audit/sequence.json)

Summary: Full sequential audit integration record: exact operation/action, workflow/skill relationships, original-contract findings, current execution state or observed documentary review. Readable content and evidence scope are preserved in this original local record.

Evidence: authored_document_inspected.

Documents: research/sources/round-05/audit-index-sources.json.

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
