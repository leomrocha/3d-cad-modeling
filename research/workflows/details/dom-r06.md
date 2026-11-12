# DOM-R06 — Photo set to measured reusable component

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 4/5.**

Output: Metric mesh plus a reusable component record with source images, frame, dimensions, rights and uncertainty; editable CAD remodel remains a separate stage.

## Comparison conditions

Overlapping calibrated photos of a static object, scales or measured controls, visible interfaces, neutral background; reconstruction route has no guaranteed feature tree.

## Registered starting artifact types

1. photo-set
2. measurement-set
3. model-brief
4. source-library

## Detailed source and preparation artifacts

1. Type: photo-set; Formats: JPG/PNG/HEIC with metadata; Minimum quality: Many overlapping viewpoints, sharp detail and known lens calibration where possible.; Required evidence: image IDs; camera model; rights; capture sequence; Handling: Preserve originals.
2. Type: measurement-set; Formats: CSV/JSON/drawing; Minimum quality: Scale bars and interface measurements in named frame.; Required evidence: point IDs; units; method; uncertainty; Handling: Metric scale tied to measured controls.
3. Type: source-library; Formats: per-file record; Minimum quality: Photo and resulting model storage/distribution rights explicitly recorded.; Required evidence: license/terms; source attribution; Handling: Separate code/model rights.

## Reference points, datums and coordinate frames

1. Kind: camera solution; Fields: camera intrinsics/extrinsics; reprojection error; Frame: camera → object frame; Source status: COLMAP output
2. Kind: scale controls; Fields: control lengths/points; Frame: object local → metric frame; Source status: measured scale/targets
3. Kind: component interfaces; Fields: mount faces/axes/holes; Frame: mesh frame → component frame; Source status: measurement set

## Software, libraries and dependencies

1. Name: COLMAP; Role: multi-view camera solve and dense cloud; Software license: BSD-3-Clause software; input photo/model rights separate; Api or entrypoint: `colmap feature_extractor`, `exhaustive_matcher`, `mapper`, `image_undistorter`, `patch_match_stereo`, `stereo_fusion`; Environment dependencies: COLMAP; dense GPU recommended; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Reconstruction is surface evidence; scale requires measured controls.; Source urls: https://colmap.github.io/cli.html; https://colmap.github.io/faq.html
2. Name: Open3D; Role: cloud cleanup and surface reconstruction; Software license: MIT code; input rights separate; Api or entrypoint: point cloud normals; Poisson or ball pivoting `TriangleMesh` APIs; Environment dependencies: Open3D Python; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Poisson is inferred surface and requires oriented normals.; Source urls: https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html
3. Name: TripoSR optional; Role: single-image appearance mesh route; Software license: MIT code and model card; image/output rights independent; Api or entrypoint: `python run.py <image> --output-dir <dir>` per pinned README; Environment dependencies: PyTorch; source says default ~6 GB VRAM and CPU fallback; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Single image does not establish dimensions, back faces, interfaces or mechanical fit.; Source urls: https://github.com/VAST-AI-Research/TripoSR; https://huggingface.co/stabilityai/TripoSR

## Procedure

1. Action: Capture/curate overlapping viewpoints and scale controls.; Tool: Camera/photo acquisition; Command or api: Record camera/lens, frame order, control dimensions and object orientation.; Preserves: Original object and photos; Changes or infers: Evidence dataset.; Check: Coverage, blur, repeated texture and control visibility.; Code status: manual
2. Action: Solve camera poses and dense surface.; Tool: COLMAP CLI; Command or api: Run `feature_extractor`, `exhaustive_matcher`, `mapper`; then `image_undistorter`, `patch_match_stereo`, `stereo_fusion`.; Preserves: Source photos; Changes or infers: Sparse cameras and fused cloud.; Check: Reprojection error, connected camera graph and control residuals.; Code status: existing_tool_entrypoint
3. Action: Scale and inspect cloud; reconstruct mesh if needed.; Tool: Open3D; Command or api: Apply control scale/registration; estimate normals and create a documented mesh.; Preserves: Cloud + controls; Changes or infers: Metric mesh; holes/invisible underside remain inferred.; Check: Independent dimensions and surface coverage.; Code status: assisted
4. Action: Author native reusable record or remodel measured interfaces.; Tool: FreeCAD/OCS; Command or api: Build a component record and optional clean parametric CAD around measured datums.; Preserves: Mesh, controls and interface measurements; Changes or infers: Native remodel is new authored geometry.; Check: Interface dimensions and fit checks against measurements.; Code status: manual

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-06; Name: Library asset intake and rights record; Inputs: source-library; Outputs: component-record; Tools: component registry/schema proposal; source license review; Source urls: https://www.freecad.org/addons.php?lang=eng_EN; https://www.kicad.org/libraries/license/; https://github.com/google-deepmind/mujoco_menagerie; https://polyhaven.com/license; https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280; Prerequisites: Original source identity and item-level license/terms available or explicitly unknown.; Preserves: Original file, URL, retrieved date, hash, attribution, license text/terms and source claims.; Changes or infers: Normalize metadata; derived conversions become separate assets with lineage.; Checks: License status per file; duplicate hash; units/frame; source part number and revision when stated.; Alternatives: Keep external link only where local caching/redistribution terms are unclear.; Automation: mixed; Evidence status: proposed_composition; Summary: Create immutable, rights-aware component records instead of treating catalogs as a common license.; Source ids: DSRC-07; DSRC-08; DSRC-09; DSRC-10; DSRC-11
2. Id: DOM-20; Name: Photos/video to camera solution, point cloud and mesh; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG/OpenMVS; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Overlapping sharp views, camera metadata/calibration where available, scene motion/lighting assessed and scale controls identified.; Preserves: Original frames, camera solution, control points, reconstruction settings, sparse/dense outputs.; Changes or infers: Videos sampled into images; camera poses and dense surfaces are estimated from image correspondences.; Checks: Registered-view coverage, reprojection residuals, independent scale distances, surface holes and withheld checks.; Alternatives: RGB-D/LiDAR for metric depth; single-image learned mesh only for visual proposal.; Automation: scripted; Evidence status: documented_capability; Summary: Reconstruct visible geometry and camera poses from image sequences; monocular scale requires external controls.; Source ids: DSRC-33
3. Id: DOM-28; Name: Dense multi-view stereo to point cloud and mesh; Inputs: photo-set; camera-solution; Outputs: point-cloud; mesh; Tools: COLMAP dense reconstruction; AliceVision/Meshroom; OpenMVS; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); Prerequisites: Camera solution and image set correspond; scale/control transform is available for metric results.; Preserves: Sparse camera solution, source images, dense settings and intermediate depth maps where available.; Changes or infers: Estimates visible depth/surfaces and fuses points; mesh topology and texture are derived.; Checks: Coverage, holes, reprojection, independent dimensions and surface residuals.; Alternatives: Depth sensor integration via DOM-21; visual scene via DOM-22/30.; Automation: scripted; Evidence status: documented_capability; Summary: Compute dense surfaces from a previously estimated camera solution.; Source ids: DSRC-33
4. Id: DOM-23; Name: Scan or mesh to parametric CAD remodeling; Inputs: point-cloud; measurement-set; model-brief; Outputs: parametric-source; cad-solid; Tools: Open3D/CloudCompare measurement; OCS baseline; FreeCAD/OCCT solid modeling; Source urls: [reconstruction.md](/home/leo/projects/3dmodeling/research/reconstruction.md); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); Prerequisites: Source scan frame/scale calibrated; independent interface dimensions and target function stated.; Preserves: Source point cloud/mesh, control measurements, fits, residual map and authored feature dimensions.; Changes or infers: Selected observed regions are approximated by constrained planes/cylinders/features; hidden geometry is a proposal unless measured.; Checks: Held-out scan-to-CAD distances; functional interfaces; solid validity and saved-file reopen.; Alternatives: Retain mesh when only appearance/clearance context is needed; direct reverse-engineered surface B-rep if warranted.; Automation: mixed; Evidence status: documented_capability; Summary: Convert observed geometry into editable CAD features without promoting inferred regions to measured facts.; Source ids: DSRC-33; DSRC-02; Input alternatives: mesh
5. Id: DOM-40; Name: Script-parametric CAD authoring; Inputs: model-brief; Outputs: parametric-source; cad-solid; Tools: CadQuery; build123d; OpenSCAD; FreeCAD Python; Source urls: [cad-and-skills.md](/home/leo/projects/3dmodeling/research/cad-and-skills.md); [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); Prerequisites: Parameters, units, datum and solid design intent are explicit.; Preserves: Executable source, package/version, parameter names and input provenance.; Changes or infers: Script defines feature/CSG operations; generated B-rep may differ by kernel/version.; Checks: Run source in declared environment; validate solid topology and controlling dimensions; compare saved export and source.; Alternatives: Use DOM-04 application-native solid authoring when feature/script history is not required.; Automation: scripted; Evidence status: documented_capability; Summary: Generate a CAD solid from a reviewed, editable parametric script; code source is retained as a separate product.; Source ids: DSRC-03; DSRC-01
6. Id: DOM-12; Name: Export mesh assets for MuJoCo; Inputs: ; Outputs: mesh; Tools: CAD mesh exporter; Blender; Open CASCADE tessellation; Source urls: https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; https://github.com/google-deepmind/mujoco/blob/main/doc/programming/extension.rst; [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); Prerequisites: Tessellation settings and mesh local frame/units chosen.; Preserves: Source CAD/B-rep and conversion parameters.; Changes or infers: Surface geometry becomes triangles; MuJoCo supports OBJ and binary STL; material assignment is separate.; Checks: Bounds, scale, normals, topology, source/mesh overlay and referenced geom role.; Alternatives: MuJoCo primitives for simple geometry; custom decoder plugin for other asset formats.; Automation: scripted; Evidence status: documented_capability; Summary: Create simulation mesh files and retain their source frame and approximation settings.; Input alternatives: cad-solid; b-rep; visual-scene; robot-assembly; Source ids: DSRC-20; DSRC-22; DSRC-13
7. Id: DOM-13; Name: Generate convex collision set; Inputs: mesh; Outputs: collision-set; Tools: CoACD; V-HACD; primitive fitting; Source urls: https://raw.githubusercontent.com/SarahWeiii/CoACD/main/LICENSE; https://github.com/kmammou/v-hacd/blob/master/LICENSE; https://github.com/google-deepmind/mujoco/blob/main/doc/overview.rst; Prerequisites: Input mesh local frame and scale known; collision features/contact regions identified.; Preserves: Input visual mesh, source hash, license, decomposition parameters and derived hull set.; Changes or infers: Nonconvex surface approximated by convex pieces; holes/passages may be filled or altered.; Checks: Hull finite bounds; compare envelope/volume; inspect missing passages; simulator contact fixtures.; Alternatives: Primitive colliders; single convex hull for coarse bounding; use original mesh only where supported and semantics understood.; Automation: scripted; Evidence status: documented_capability; Summary: Derive a collision-specific approximation and review topology-sensitive errors.; Source ids: DSRC-23; DSRC-24; DSRC-20
8. Id: DOM-26; Name: Version and reuse component revision; Inputs: component-record; Outputs: component-record; Tools: content-addressed files; Git metadata; source/license registry; Source urls: [domains-and-components.md](/home/leo/projects/3dmodeling/research/domains-and-components.md); [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); Prerequisites: Stable component ID, exact source bytes, item terms and conversion lineage recorded.; Preserves: Existing revisions and assemblies pinning them; original files are immutable.; Changes or infers: New source content or license produces a new revision/digest; derived files link to input/tool versions.; Checks: Hash consistency, dependency/license closure, revision pinning and reproducible export manifests.; Alternatives: Git for small source assets; LFS/content-addressed storage for large licensed assets after policy check.; Automation: scripted; Evidence status: proposed_composition; Summary: Keep reusable assets immutable and project assemblies reproducible against pinned revisions.; Source ids: DSRC-13; DSRC-01

## Code and tool entry points

1. Status: existing_tool_entrypoint; Path: See the selected tool/variant contract.; Summary: Use the software/API entry points below in the recorded procedure; manual CAD, joint and semantic authoring steps use the explicit frames and source data recorded for that step.; Related entrypoints: ; Source urls: https://colmap.github.io/cli.html; https://colmap.github.io/faq.html; https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html; https://github.com/VAST-AI-Research/TripoSR; https://huggingface.co/stabilityai/TripoSR; Entrypoints: `colmap feature_extractor`, `exhaustive_matcher`, `mapper`, `image_undistorter`, `patch_match_stereo`, `stereo_fusion`; point cloud normals; Poisson or ball pivoting `TriangleMesh` APIs; `python run.py <image> --output-dir <dir>` per pinned README

## Output artifacts

1. Type: mesh; Format: PLY/OBJ/GLB; Retained: Observed surface triangles with scale/transform manifest.; Loss or inference: Hidden surfaces, exact analytic features, tolerances and semantics are absent/inferred.
2. Type: native-model-document; Format: FCStd/OCS source if remodeled; Retained: Editable parametric or native representation as authored.; Loss or inference: Remodel is a derivative, not the photo reconstruction itself.
3. Type: source-library; Format: Manifest + asset files; Retained: Per-file source, license, hash, revision, frame and units.; Loss or inference: Rights depend on source and derivative terms.

## Checks

1. Camera graph connected; controls constrain scale; held-out dimensions recorded.
2. Surface coverage and mesh holes inspected.
3. Metric dimensions match independent measurements within stated uncertainty.
4. Source/hash/license and transforms attach to each asset.
5. Native remodel opens and features reference stable datums.

## Failure recovery

1. Low overlap/disconnected solve: capture bridge images or split views.
2. Specular/textureless surface: add coded targets/measurement-led CAD.
3. No scale control: mark mesh arbitrary scale and do not call it measured.
4. Image model looks plausible but interface unknown: retain only visual role.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Capture coverage, scale and mechanical interpretation need review.
5. **Setup reason:** Calibration, SfM and geometry tools plus asset registry.
6. **Compute reason:** Dense reconstruction uses substantial CPU/RAM and GPU acceleration when enabled.

## Resources and scaling

1. **Cpu:** CPU feature and mesh stages; multithreaded.
2. **Gpu:** COLMAP dense route GPU-accelerated; TripoSR source quotes ~6 GB VRAM default.
3. **Ram:** Image count/resolution and dense depth maps dominate.
4. **Storage:** Original photos, sparse model, depth maps, point cloud, mesh and manifests.
5. **Scaling drivers:** image count/resolution; surface texture; camera graph; mesh triangles
6. **Variants:** TripoSR is faster-to-author visual route but not metric component CAD.; Measured multi-view route supports dimensions with controls.

## Detailed branch procedures

1. [rec-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/rec-r01.md)
2. [cad-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/cad-r01.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://colmap.github.io/cli.html](https://colmap.github.io/cli.html)
2. [https://colmap.github.io/faq.html](https://colmap.github.io/faq.html)
3. [https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html](https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html)
4. [https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR)
5. [https://huggingface.co/stabilityai/TripoSR](https://huggingface.co/stabilityai/TripoSR)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
