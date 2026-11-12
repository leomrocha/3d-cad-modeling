# Combined workflows

Research date: 12 November 2026. Status: proposed cross-domain compositions.

These recipes combine the CAD, reconstruction and domain operations. Each operation has its own source evidence; the composed routes retain proposal status. Full records: [combined-paths.json](combined-paths.json). The [operation catalogue](operation-catalogue.md) and [source register](../sources/source-register.md) provide the transformation details and original source summaries.

## 1. MIX-R01 — Raster plan + site photographs + controls + library → IFC and registered context

Goal: Semantic building with sourced components, registered observed surfaces and visual scene.

Combine plan interpretation with measured site surfaces and identified library components; preserve the IFC model, photo solution and conversion map.

Inputs: text, dimensions, raster-plan, photo-set, measurement-set, source-library.

Operations: CAD-02 → CAD-03 → CAD-04 → CAD-01 → CAD-05 → DOM-18 → DOM-06 → DOM-35 → REC-03 → REC-17 → DOM-19 → DOM-17.

Artifact roles:

1. **drawing:** original raster plan and extracted topology.
2. **site:** dense cloud from photographs.
3. **controls:** shared frame/scale and separate assessment controls.
4. **authority:** IFC building plus retained source evidence.

Handoff conditions:

1. Plan scale and heights are explicit inputs to semantic building creation.
2. OCR labels are reconciled with plan features before wall/opening creation.
3. Control correspondences align the observed cloud with IFC placements; independent controls evaluate the alignment.
4. Library components retain source identity and instance transforms.

## 2. MIX-R02 — Vector profile + dimensions + library parts → articulated CAD, MJCF and URDF

Goal: Editable part/assembly with separate visual/collision derivatives and source-linked robot descriptions.

Use a dimensioned part as one assembly component, place identified library parts, author explicit joints and physical data, and derive robot packages.

Inputs: text, dimensions, vector-drawing, measurement-set, source-library, material-set.

Operations: CAD-01 → CAD-08 → CAD-09 → CAD-10 → DOM-06 → DOM-37 → DOM-07 → DOM-31 → DOM-08 → DOM-12 → DOM-13 → DOM-14 → DOM-11 → DOM-09.

Artifact roles:

1. **part:** dimensioned native CAD.
2. **library:** identified component assets.
3. **kinematics:** authored joint and assembly graph.
4. **dynamics:** per-body mass, centre of mass and inertia with sources.

Handoff conditions:

1. The brief defines rigid links and joint intent; geometry alone supplies no motion definition.
2. Interface frames bind component placement to named datums.
3. Mass properties are assigned per rigid body from recorded data or stated density/volume calculations.
4. URDF and MJCF are separate named derivatives of the same assembly revision.

## 3. MIX-R03 — Photographs + measured controls + component library → CAD assembly and MuJoCo model

Goal: Measured-reference CAD assembly with explicit robot structure and collision derivatives.

Reconstruct visible surfaces, fit candidate features, remodel selected parts, combine them with identified hardware and author the robot model.

Inputs: text, dimensions, photo-set, measurement-set, source-library, material-set.

Operations: CAD-01 → REC-01 → REC-03 → REC-17 → REC-09 → REC-14 → DOM-06 → CAD-12 → CAD-13 → DOM-31 → DOM-08 → DOM-12 → DOM-13 → DOM-14 → DOM-11.

Artifact roles:

1. **observed:** photographic reconstruction.
2. **modeled:** remodeled CAD features.
3. **reused:** library components.
4. **checks:** source dimensions, regional deviations and body/joint transforms.

Handoff conditions:

1. Calibration/control images and reconstruction images retain distinct roles.
2. Fit controls and independent measurement controls are identified separately.
3. A library match is an identified component decision supported by interfaces and provenance.
4. Hidden surfaces retain inference labels through CAD and simulation export.

## 4. MIX-R04 — Existing housing CAD + depth scan + drawing → revised interface and reusable component

Goal: Revisioned replacement component fitted to the retained housing and registered scan.

Use the housing as a stable reference, drawing dimensions as constraints and scan surfaces as local evidence for the scoped replacement.

Inputs: cad-solid, depth-frames, vector-drawing, measurement-set, model-brief, source-library.

Operations: REC-05 → REC-06 → REC-12 → REC-15 → REC-14 → CAD-12 → CAD-13 → DOM-06 → DOM-26.

Artifact roles:

1. **fixed_reference:** original housing CAD.
2. **observed:** calibrated depth surface.
3. **dimension_source:** drawing and direct controls.
4. **revision:** replacement interface CAD and updated component metadata.

Handoff conditions:

1. Source housing and replacement CAD have separate artifact IDs.
2. Depth calibration, shared datums and transforms connect the cloud to the housing.
3. Drawing constraints and fit residuals remain attributable to their respective sources.
4. Catalogue registration pins the revised component assets and their source licences.

## 5. MIX-R05 — Robot CAD + Menagerie MJCF + depth environment → combined simulation scene

Goal: MuJoCo scene with explicit CAD-link mapping and scanned-environment collision geometry.

Reuse a specifically licensed simulation package, map CAD occurrences to its bodies and add a registered scanned environment.

Inputs: mjcf, cad-assembly, joint-set, measurement-set, depth-frames, source-library.

Operations: DOM-06 → REC-05 → REC-06 → DOM-13 → DOM-32 → DOM-33 → DOM-24.

Artifact roles:

1. **robot:** supplied MJCF and joint records.
2. **geometry:** CAD assembly occurrences.
3. **environment:** depth-derived mesh and colliders.
4. **display:** Blender inspection scene.

Handoff conditions:

1. The supplied MJCF is a named model revision with its own licence record.
2. CAD-to-body mapping checks transforms and joints before modifying a derivative.
3. Environment mesh and colliders have separate assets and aligned frames.
4. Source robot dynamics retain their recorded source/model-fidelity status.

## 6. MIX-R06 — IFC building + existing robot MJCF → building collision environment and semantic display

Goal: Robot scene with building colliders and a retained IFC/GLB identity map.

Derive colliders from selected building elements while preserving semantic IFC as the building source.

Inputs: ifc, mjcf, measurement-set.

Operations: DOM-16 → DOM-13 → DOM-33 → DOM-17.

Artifact roles:

1. **semantic_source:** IFC graph.
2. **simulation_source:** existing MJCF.
3. **collision:** selected building surfaces.
4. **display:** IFC-derived visual scene.

Handoff conditions:

1. Select the building surfaces used as simulation environment.
2. Preserve IFC-to-mesh element mapping and unit/frame conversion.
3. Inspect doorway/contact channels after convex decomposition.
4. The supplied MJCF and the environment-augmented derivative have distinct revision IDs.

## 7. MIX-R07 — Sketch over registered 3D + dimensions → revised CAD and fabrication package

Goal: Source-linked native CAD revision, comparison record and fabrication derivatives.

Anchor screen annotations to the selected surface, interpret feature intent and construct a dimensioned CAD revision.

Inputs: raster-sketch, camera-solution, mesh, measurement-set, text, dimensions, material-set.

Operations: CAD-01 → REC-13 → REC-14 → REC-16 → CAD-13 → DOM-25.

Artifact roles:

1. **annotation:** screen stroke and surface anchors.
2. **reference:** registered mesh.
3. **intent:** dimensioned brief.
4. **output:** native model revision and its requested fabrication derivatives.

Handoff conditions:

1. Store stroke pixels, camera pose/intrinsics and hit component/triangle IDs.
2. Ray hits are calculated anchors; their evidence follows the hit surface and camera calibration.
3. Sketch-plane, feature meaning and governing dimensions are explicit before CAD construction.
4. Fabrication output uses the checked CAD revision and stated material/process information.

## 8. MIX-R08 — Orthographic rasters + dimensions → candidate geometry and component record

Goal: Multi-view reconstruction hypothesis with checked projections and provenance.

Use multiple orthographic views and dimension evidence to propose a consistent 3D model and record the result as a source-linked candidate component.

Inputs: raster-sketch, dimensions, measurement-set, source-library, text.

Operations: CAD-02 → CAD-04 → CAD-06 → CAD-07 → CAD-13 → DOM-06 → DOM-26.

Artifact roles:

1. **views:** registered orthographic source images.
2. **controls:** printed/direct dimension evidence.
3. **candidate:** reconstructed native or exchange geometry.
4. **catalogue:** revisioned component record with inference labels.

Handoff conditions:

1. The raster-sketch input contains distinct front/top/side views with recorded projection convention.
2. Dimension and correspondence alternatives remain attributed to source views.
3. Reproject the candidate into every supplied view and compare independent dimensions.
4. The library record retains candidate/inferred status for hidden geometry.

## 9. MIX-R09 — One photo capture → Gaussian context + independent MVS mesh + CAD

Goal: Aligned visual scene, independently reconstructed measured surface and remodeled CAD.

Fork the capture into a view-synthesis branch and dense geometry branch, then retain their alignment with the CAD interpretation.

Inputs: photo-set, measurement-set.

Operations: REC-01 → REC-03 → REC-19 → REC-17 → REC-09 → REC-14 → CAD-13 → DOM-24.

Artifact roles:

1. **appearance:** Gaussian reconstruction.
2. **surface:** MVS mesh/cloud.
3. **engineering:** remodeled CAD.
4. **alignment:** camera solution, scale and control transform.

Handoff conditions:

1. Both branches preserve the same camera/image lineage.
2. Gaussian output remains a visual scene representation.
3. Dense MVS and measured controls supply the surface evidence used for remodeling.
4. Regional deviations and source dimensions evaluate the CAD derivative.

## 10. MIX-R10 — IFC + reusable library components → exact geometry branch and static MuJoCo environment

Goal: Semantic building revision with geometry derivatives and reusable source metadata.

Place identified library elements into IFC, retain an explicit B-rep extraction branch and derive a static simulation environment.

Inputs: ifc, source-library, measurement-set.

Operations: DOM-06 → DOM-35 → DOM-27 → DOM-12 → DOM-13 → DOM-34 → DOM-26.

Artifact roles:

1. **source:** IFC and identified library assets.
2. **exact_geometry:** supported OpenCASCADE B-rep extraction.
3. **collision:** derived convex/primitives set.
4. **simulation:** static environment MJCF.

Handoff conditions:

1. Geometry extraction keeps the source IFC graph and object identity mapping.
2. B-rep extraction and tessellation are separately recorded representation changes.
3. Static environment MJCF uses colliders derived from the selected mesh and stated frame.
4. Component versioning records the native source and intended derivative roles.

## Additional registered ideas

1. **Shared frame and anchor record** — Use one versioned record to relate pixels, camera rays, scan coordinates, CAD datums and component IDs. Next check: Compare transform direction, units and anchor round trips in the selected tools.

1. **Source-to-feature association** — Retain each fitted or interpreted surface region and the exact CAD feature it supports. Next check: Compare fitted-plane/cylinder evidence with saved feature and dimension readback.

1. **Importer/exporter field mapping** — Maintain actual preserved/transformed/discarded field mappings per tool/version. Next check: Run the same component and assembly fixtures through the intended consumers.

1. **Ambiguous-view comparison** — Retain several geometrically consistent interpretations until source evidence distinguishes them. Next check: Compare projected views and independent dimensions, with inference labels by feature.

1. **Dependency-driven revision updates** — Record which branch depends on each measurement, component revision and interpretation. Next check: Trace a single input change through affected recipes and derivative revisions.

1. **Text-to-concept-image-to-mesh route** — Register a possible branch from text or sketch through a concept image to an image-conditioned mesh, then measured CAD remodeling. Next check: Research an open image-generation backend and its exact weight/output terms before defining the first transition.

1. **Procedural field geometry supplement** — Evaluate PicoGK/ShapeKernel as a separate source-driven geometry branch with explicit field/mesh resolution and OCS interchange checks. Next check: Use the existing archived sources to define runtime/platform, output representation and comparison experiments.
