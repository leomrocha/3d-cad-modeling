# Proposed implementation plan

Research date: 2026-11-12. Status: proposal. Repository foundation and research are the executed scope of this pass.

## 1. Proposed system

Build a reusable workflow toolkit around the existing OCS skill, a Python geometry pipeline, Blender inspection and reconstruction, and separate architecture and robotics exporters. Each job produces a native model, derivatives appropriate to the requested use, a source register and a verification report. A component library supplies reusable parts and assemblies.

The existing local OCS skill is the starting point for interactive CAD. The user reports partial success with that skill. Backend selection is per job: an engineering part needs dimensional constraints and solid checks; a site scan needs camera calibration and reconstruction checks; a robot needs component frames and joints; a building needs semantic building elements.

Detailed evidence is in [CAD and skills](cad-and-skills.md), [reconstruction](reconstruction.md), [domains and components](domains-and-components.md), and [local baseline](local-baseline.md).

## 2. Input-to-output routes

| Input | Processing route | Main deliverable | Verification |
| --- | --- | --- | --- |
| Text and dimensions | Extract dimensioned brief → resolve geometry constraints → OCS or scriptable solid backend | Native CAD, parameters, solid interchange | Dimensions, solid validity, feature/part count, saved-file reopen |
| Dimensioned sketch | Identify views/datums → transcribe dimensions → constrained sketches → features | CAD parts and assemblies | Each controlling dimension traced to its source, view consistency |
| Single photograph and measured references | Lens/perspective calibration where supported → reference measurements → explicit primitive/feature fitting | Dimensioned CAD hypothesis with evidence labels | Independent measured dimensions and view reprojection |
| Multiple photographs/video | Frame selection → calibration → camera poses → dense geometry → cleanup | Cameras, point cloud, textured mesh | Coverage, independent scale controls, reprojection and surface residuals |
| Depth/LiDAR scan | Calibration/extrinsics → registration → filtering → fusion | Metric point cloud or mesh | Sensor units, registration residuals, independent control distances |
| Scan/mesh of mechanical part | Segmentation → plane/cylinder/axis fits → feature constraints → remodel | Editable CAD plus retained scan | Held-out scan-to-CAD distances and functional interface dimensions |
| Raster floor plan | Scale/control lengths → wall/opening interpretation → component geometry | IFC building and editable source | Wall thickness, opening placement, elevations, room/element checks |
| DXF/SVG drawing | Units/layers/blocks → curve cleanup → closed profiles → extrusion/revolution/loft | Native CAD and solid export | Profile closure, curve fidelity, holes, dimensions, solid count |
| Appearance reference | Learned image-to-3D or Gaussian/NeRF reconstruction → mesh or scene refinement | Visual asset/reference scene | Multi-view appearance, geometry checks for its intended use |
| Existing CAD/library components | Licence/provenance intake → unit/frame mapping → assembly placement | Reusable components and assembly | Interface coordinates, part identity, transform and format fidelity |
| Robot assembly | Bodies and joints → visual/collision derivatives → mass properties → MJCF/URDF | Simulation package and native CAD | Units, joint frames/limits, inertia, compile, collision and motion checks |
| Building assembly | Building elements → materials/properties → placements/georeferencing → IFC | Semantic architecture model | IFC validation, element quantities, geometry, downstream importer check |

A perspective photograph supplies rays from a camera; measured references and stated geometry constraints supply dimensional evidence. Learned reconstruction fills occluded surfaces with inferred geometry. Store that inference status beside each affected component or feature.

## 3. Model representations and ownership

1. **Native editable source:** Preserve the OCS document, FreeCAD document, procedural Python/OpenSCAD source or IFC model used to create the geometry. Record backend and version.
2. **Analytic solid:** Use a supported boundary-representation route for exact planes, cylinders and topology. Record export settings and reopen measurements. STEP exchange preserves the content its exporter writes; feature history remains in the native source or generator.
3. **Polygon mesh:** Keep visual and collision meshes as separate derivatives. Record tessellation, simplification, normals, watertightness and unit conversion. Use GLB for packaged visual assets, with consumer-specific STL/OBJ/PLY where appropriate.
4. **Point cloud:** Preserve sample positions, coordinate frame, colour, normals and measurement provenance when available. Store filtering and registration transforms.
5. **Gaussian/NeRF scene:** Preserve cameras and reconstruction settings with the native representation. Extracted meshes become separately tracked derivatives with their own checks.
6. **Building model:** Use IFC classes, placements, property sets, material assignments, spatial hierarchy and stable element IDs for architecture.
7. **Robot model:** Preserve the kinematic tree, joint axes, limits, inertial properties, visual/collision mapping and source part IDs in MJCF/URDF packages.

For each job designate one authoritative model and derive the other formats from its recorded revision. An importer change creates a new derivative revision.

## 4. Proposed software layers

1. **Job brief and source intake.** A small Python CLI reads a structured model brief and reference files. It records units, frames, part IDs, required dimensions, intended use, input rights and output formats. Keep the original images, drawings and supplied measurements with hashes.
2. **Geometry adapters.** Reuse the local OCS session-control skill and revision-aware operations. Evaluate build123d and CadQuery on the same solid fixtures, then retain the one whose API and saved results fit the jobs. Use FreeCAD where an interactive feature tree and constrained sketches are required. Use OpenSCAD for concise CSG and suitable library components.
3. **Blender adapter.** Execute bounded Python scripts using Blender's native API for scene assembly, visual inspection, meshes, materials and rendering. Assess MCP bridges against direct scripts for session preservation and reproducibility.
4. **Reconstruction adapters.** Begin with a calibrated photogrammetry route and Open3D/CloudCompare processing. Add a separate GPU experiment for Gaussian scenes and learned object reconstruction after licence and hardware assessment.
5. **Domain exporters.** Use IfcOpenShell/Bonsai for building semantics and MuJoCo's native loader/compiler for simulation checks. Add URDF exchange when the robot consumer requires it.
6. **Component registry.** Store small metadata and procedural sources in Git; select binary storage after measuring fixture sizes and update frequency. Resolve components by stable ID, revision and content hash. Keep supplier models and scanned/generative assets traceable to their respective sources.
7. **Verification and reports.** Each adapter writes its actual execution state, logs, model revision, measured properties and output hashes. A readable report links dimensions and component names to the exact model being checked.

Candidate component sources include MuJoCo Menagerie for robot simulation descriptions, FreeCAD Parts Library and BIM Library for modeled components, KiCad for electronics, BOSL2/NopSCADlib for procedural geometry, and Poly Haven for visual assets. The [component assessment](domains-and-components.md) records the representation and licence of each source.

The repository provides reusable workflow contracts. Application-specific geometry and decisions remain in the consuming project or its model brief.

## 5. Proposed skill set

| Skill | Purpose | Reuse or implementation basis |
| --- | --- | --- |
| `model-brief` | Convert descriptions and reference files into explicit model inputs | Shared contract and source intake |
| `ocs-engineering` | Inspect and revise live OCS models | Existing local skill, controls and checks |
| `parametric-solid-modeling` | Build dimensioned parts from reproducible generators | Evaluate build123d/CadQuery and inspected CAD skills |
| `drawing-to-cad` | Interpret sketch/DXF/SVG profiles and dimensions | Existing drawing parsers plus constrained CAD operations |
| `blender-modeling` | Build and inspect scenes, meshes and visual derivatives | Native `bpy` workflows and assessed Blender skills |
| `capture-and-calibration` | Prepare photo/video/scan inputs and scale controls | Camera calibration and reconstruction prerequisites |
| `photogrammetry` | Produce cameras, clouds and textured surfaces | Selected SfM/MVS command-line pipeline |
| `point-cloud-and-mesh-processing` | Register, segment, clean, fit and compare geometry | Open3D/CloudCompare and mesh utilities |
| `scan-to-cad` | Remodel measured surfaces as constrained features | Fits, source measurements and CAD backend |
| `generative-3d-reference` | Produce appearance/reference geometry from images or text | Licence-assessed learned model adapter |
| `gaussian-scene-reference` | Reconstruct and inspect view-synthesis scenes | Licence-assessed Gaussian workflow |
| `architecture-ifc` | Create semantic buildings from plans and components | IfcOpenShell/Bonsai |
| `robot-model-handoff` | Export articulated assemblies and simulation packages | MJCF/URDF, collision and inertia checks |
| `component-library` | Find, import, version and reuse components | Provenance registry and per-asset licences |
| `model-verification` | Measure geometry and verify saved outputs | Backend checks, independent controls and readback |

Each future skill should contain a narrow `SKILL.md`, verified commands, supported version ranges, reference files and representative fixtures. Package reusable scripts with the skill that owns their workflow. Preserve upstream licences and attribution when adopting third-party content.

## 6. Component-library contract

Proposed component record fields:

1. **Identity:** `component_id`, readable name, family, revision, source revision, author/manufacturer and part number where applicable.
2. **Evidence:** source URL or file, retrieval date, source hash, licence identifier, licence text path, attribution, redistribution terms and provenance status.
3. **Representation:** native source, generator and parameters, analytic solid, visual mesh, collision mesh, point cloud and their hashes.
4. **Geometry:** length unit, local frame, origin, axes, bounding dimensions, interface frames, mounting features and declared tolerances with their sources.
5. **Assembly:** child component IDs, occurrence transforms, connection references and joint metadata where applicable.
6. **Physical properties:** mass, centre of mass, inertia tensor, material and density, each with units, frame and measured/manufacturer/calculated/assumed status.
7. **Verification:** backend/version, solid validity, mesh checks, dimensions, importer results and check date tied to the exact revision.
8. **Use and discovery:** tags, preview paths, permitted uses and consumer formats.

The catalogue should distinguish measured components, manufacturer geometry, procedural designs, scanned surfaces and generated reference assets. Interface frames make bearings, motors, wheels, fasteners, robot links, doors, windows and furniture reusable without reconstructing their placement rules.

Proposed layout during implementation:

```text
skills/<workflow>/SKILL.md
skills/<workflow>/scripts/
skills/<workflow>/references/
scripts/                         # shared CLI entrypoints only
schemas/                         # model brief, provenance, component, run result
library/catalog/                 # component metadata
library/components/<id>/         # native source and small licensed assets
examples/<workflow>/             # reproducible usage and input evidence
checks/fixtures/                 # deliberately small cross-tool fixtures
data/                            # local large captures and generated outputs
research/                        # assessments and source register
```

Choose large-file storage from measured data: Git LFS for versioned binary assets where repository hosting supports it, or content-addressed object storage with immutable manifests for large captures and reconstructions. Keep the retrieval path and hash in Git in either case.

## 7. Staged implementation

### Stage 1 — Existing OCS baseline and deterministic solids

1. Record the installed OCS build/session capabilities and retain the current local skill behaviour that already works.
2. Exercise one dimensioned bracket with a bore and multiple named parts using the authorized CAD route.
3. Compare a curved solid from build123d and CadQuery using identical declared dimensions; assess edits, export, analytic surfaces and saved-file readback.
4. Reopen derivatives in an independent supported importer and inspect part count, bounds, bore size and volume.
5. Deliver the existing-skill capability receipt, one selected procedural-solid adapter, model brief schema and an example with measured checks.

The comparison addresses the OCS source exporter finding: its current STEP route consumes triangles. The test must determine the usable solid-interchange route for the selected backend and consumer.

### Stage 2 — Drawings, Blender and the first component catalogue

1. Run a dimensioned DXF profile with a hole, a dimensioned raster sketch and a text brief through the intake contract.
2. Create a corresponding part and a simple room with a wall opening; validate the supplied dimensions and geometry features.
3. Derive Blender visual assets from those same revisions and verify unit/axis mapping numerically.
4. Add a small pilot catalogue spanning a mechanical part, an assembly, and an architectural element. Preserve licences, interfaces and source dimensions.
5. Deliver `drawing-to-cad`, `blender-modeling` and `component-library` skills backed by exercised scripts.

### Stage 3 — Metric reconstruction and CAD remodeling

1. Capture or reuse an authorized photo set with calibration evidence and measured control distances.
2. Reconstruct cameras and surfaces, then align scale/frame using a subset of controls.
3. Reserve independent measurements for error evaluation. Report per-control residuals in millimetres and surface-fit residuals over defined regions.
4. Fit relevant planes/cylinders and rebuild a selected part as CAD. Inspect functional dimensions and scan-to-CAD distances.
5. Deliver the capture, photogrammetry, cloud/mesh and scan-to-CAD skills with original images, transformations and measurements.

### Stage 4 — Architecture and robotics consumers

1. Create an IFC example with a wall, opening, door/window and storey placement. Check semantic classes, geometric dimensions and a consumer import.
2. Create an articulated robot example with separate links, defined joints and known physical-property inputs.
3. Export visual and collision geometry, compile the MJCF model and check frame transforms, joint ranges and intended contacts.
4. Export URDF if the selected robot consumer uses it; compare the imported kinematics and inertial metadata against the source.
5. Deliver `architecture-ifc` and `robot-model-handoff` skills with source-linked verification reports.

### Stage 5 — Gaussian and learned reconstruction extensions

1. Select a specific tool/model from the licence assessment and record compatible hardware, dependencies and weights.
2. Benchmark Gaussian scene reconstruction on the metric photo fixture, retaining cameras and transforms.
3. Benchmark learned image-to-3D on an object with known independent dimensions and multi-view references.
4. Compare runtime, peak memory, output representation, appearance and measured geometry errors. Keep inferred surfaces tagged through remodeling.
5. Deliver optional reference-generation skills whose outputs enter the same asset registry and verification process.

### Stage 6 — Workflow integration

1. Provide one CLI entrypoint for intake, adapter execution, inspection and export.
2. Add capability discovery per installed tool and versioned adapter configuration.
3. Record job state, partial outputs and restart points for long reconstruction operations.
4. Package exercised skills and pinned environment definitions by workflow family.
5. Document examples from each supported input type through its native source and downstream consumer.

## 8. Verification specification

1. **Geometry:** Controlling dimensions and allowed errors come from the task brief and intended use. Measure the actual saved geometry. For solids, inspect validity, count, topology, volume, surface types and interfaces. For meshes, inspect scale, normals, disconnected components, degeneracy and watertightness where required.
2. **Reconstruction:** Separate controls used to estimate the transformation from controls used to assess error. Record camera/image coverage, calibrated parameters, registration residuals, point/mesh coverage and local error distributions. Compare inferred and observed regions separately.
3. **Interchange:** Reopen each supported output using its actual consumer and compare IDs/counts, placements, dimensions and available properties. Retain a numerical conversion factor and explicit source/target frames.
4. **Robot dynamics:** Record the source of mass and inertia. Test loader compilation, joint-axis direction, limits and defined contact cases. A numerical simulation report describes that specified model and operating conditions.
5. **Architecture:** Check IFC schema validity, class/property assignments, placements, openings and quantities against the example brief. Exercise the selected architecture consumer.
6. **Reproducibility:** Record tool versions, dependency locks, model-weight revisions, parameters, seeds where relevant, original input hashes, execution logs and output hashes.

## 9. Implementation priorities

1. Start with existing OCS use, dimensioned text/sketch modeling and Blender derivatives: these provide a direct route to CAD on the observed local setup.
2. Add source-backed component reuse and drawing intake: these reduce repeated modeling and support architecture and robotics together.
3. Establish metric reconstruction and scan-to-CAD with independent controls: this connects photographic evidence to dimensional geometry.
4. Add IFC and MJCF consumers: these demonstrate the two named application domains.
5. Add GPU reference-generation options against the same fixtures: this provides a measured comparison of appearance and geometry for the additional methods.
