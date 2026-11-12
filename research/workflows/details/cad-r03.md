# CAD-R03 — Raster floor plan to semantic layout and 3D building

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 4/5; computing 3/5.**

Output: ifc / cad-solid

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. raster-plan
2. dimensions
3. text

## Detailed source and preparation artifacts

1. Artifact: raster-plan; Format: PNG/TIFF/JPEG or raster PDF page; Requirement: reviewed wall/opening graph + vertical dimensions; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** reviewed wall/opening graph + vertical dimensions
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: CVPR2021; Role: CVPR2021 floorplan; License: Paper only; no software licence implied.; Apis: Published algorithm: blueprint semantic/geometry inference in paper; manual graph interpretation; no CLI claim; Dependencies: Paper has no asserted installable dependency; reproducing method requires research implementation/dataset.; Source urls: https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf
2. Name: ACCV2022; Role: ACCV2022 vectorization; License: Paper only; no software licence implied.; Apis: Published vectorization method: raster blueprint to vector structure; no CLI claim; Dependencies: Paper has no asserted installable dependency; reproducing method requires research implementation/dataset.; Source urls: https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf
3. Name: FreeCAD; Role: FreeCAD Draft/Part; License: LGPL-2.1-or-later per project licensing page.; Apis: FreeCAD Python console/macros; App.newDocument; Sketcher::SketchObject.addGeometry/addConstraint; Part::Feature.Shape or PartDesign::Body/Feature for solids; ViewPart/TechDraw orthographic projection; import/export via Draft/Part; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf

## Procedure

1. Order: 1; Action: OpenCV rectification; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: human wall/opening topology and storey heights; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: construct walls/openings in FreeCAD/OCS; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: validate dimensions and IFC/STEP handoff.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-02; Name: Rectify a raster drawing plane from known dimensions; Inputs: ; Outputs: measurement-set; Tools: OpenCV point correspondences; planar homography; Source urls: https://docs.opencv.org/5.0/main_modules/calib.html; Prerequisites: For scale, provide known dimensions on the same plane.; A planar homography rectifies that plane and does not recover object depth.; Preserves: Original image coordinates; Known control lengths; Image-to-plane transform; Changes or infers: Calculates a plane transform and metric image coordinates from matched points.; Checks: Check independent in-plane lengths after rectification.; Record controls, units and transformation.; Alternatives: Manual scale using a known dimension on a front-parallel scan; Automation: scripted; Evidence status: documented_capability; Summary: Rectify a single drawing plane using matched control coordinates; this route does not calibrate a general 3D camera or infer depth.; Input alternatives: raster-sketch; dimensions; raster-plan; dimensions
2. Id: CAD-03; Name: Recognize dimension text with OCR; Inputs: ; Outputs: text; Tools: Tesseract OCR TSV output; image crop/deskew; human transcription review; Source urls: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html; Prerequisites: Retain original pixels and page transform.; Use OCR output as candidates; resolve glyphs, units, tolerance symbols and feature association against the source image.; Preserves: Text bounding boxes; OCR confidence values; Original image and crop coordinates; Changes or infers: Produces candidate text strings and numeric dimension values from pixels.; Checks: Verify every dimension against the source crop.; Check decimal separator, diameter/radius symbols, tolerance, units and view association.; Alternatives: Manual dimension transcription; Vector drawing dimension records when available; Automation: assisted; Evidence status: documented_capability; Summary: Tesseract TSV can return text and word bounding boxes with confidence; engineering interpretation and dimension association remain review steps.; Input alternatives: raster-sketch; raster-plan
3. Id: CAD-04; Name: Extract raster edges, lines and contours; Inputs: ; Outputs: vector-drawing; Tools: OpenCV thresholding; HoughLinesP; findContours; approxPolyDP; Source urls: https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html; https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html; https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; Prerequisites: Rectify or record the image transform before measuring extracted pixels.; Separate dimension lines, extension lines, text and object contours by layers or masks.; Preserves: Pixel coordinates and candidate segment endpoints; Source image identity; Changes or infers: Approximates raster strokes as candidate vectors; line/contour algorithms do not classify engineering intent by themselves.; Checks: Overlay candidates on source raster.; Measure endpoint gaps and edge displacement in calibrated coordinates.; Retain uncertain or intersecting candidates for review.; Alternatives: Manual trace in OCS or FreeCAD; Learned wall/opening segmentation followed by vectorization; Automation: scripted; Evidence status: proposed_composition; Summary: Image-processing primitives and floor-plan reconstruction research support candidate line extraction, while symbol and feature meaning require separate interpretation.; Input alternatives: raster-sketch; raster-plan
4. Id: CAD-01; Name: Extract a model brief from text and dimensions; Inputs: ; Outputs: model-brief; Tools: model brief schema; human review; OCS engineering skill; Source urls: [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); Prerequisites: Identify each value as supplied, measured, inferred, assumed, or calculated.; Declare units, origin, axes, component boundaries, intended output and source links.; Preserves: Original text; Value-to-source associations; Author's unresolved choices; Changes or infers: Groups explicit requirements into named parameters and geometry constraints.; Does not infer hidden geometry from prose alone.; Checks: Every numerical parameter has units and provenance.; Ambiguities affecting geometry are listed separately.; Alternatives: Direct interactive OCS modeling after brief readback; Code-CAD generation from a validated brief; Automation: assisted; Evidence status: proposed_composition; Summary: Create a source-linked brief before changing geometry; keep source claims separate from constraints and design choices.; Input alternatives: text; dimensions; text; dimensions
5. Id: CAD-05; Name: Convert raster floor-plan candidates into a wall and opening graph; Inputs: raster-plan; measurement-set; Outputs: vector-drawing; Tools: floor-plan segmentation/vectorization model or manual trace; graph consistency checks; OCS or FreeCAD Draft; Source urls: https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf; https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf; Prerequisites: Establish plan scale and origin from a known control or explicit drawing dimensions.; Define wall centerline/edge convention and distinguish walls, openings, room labels and annotation.; Preserves: Raster source; Candidate pixel/vector locations; Wall/opening graph and confidence/status; Changes or infers: Classifies walls/openings/rooms and infers graph connections from image patterns.; Checks: Room/wall graph connectivity; Opening endpoints attach to wall segments; Known lengths and orthogonality; Manual confirmation of ambiguous symbols; Alternatives: Trace wall centerlines and openings manually; Use a learned detector to propose vector geometry; Automation: mixed; Evidence status: proposed_composition; Summary: Research papers demonstrate floor-plan segmentation, vectorization and structural graph reconstruction; exact measurements and semantics still need source-linked confirmation.
6. Id: CAD-17; Name: Build wall and opening solids from a confirmed floor-plan graph; Inputs: vector-drawing; measurement-set; model-brief; Outputs: cad-assembly; Tools: FreeCAD Part/Sketcher or OCS native geometry; wall/opening graph interpretation; human confirmation; Source urls: https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf; https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf; [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); Prerequisites: vector-drawing contains the reviewed plan wall/opening graph from CAD-05.; measurement-set contains known in-plane controls; model-brief contains confirmed wall height, thickness convention, opening dimensions/heights, floor datum and units.; Represent unknown elevations or wall build-ups as explicit parameters and do not fill them from plan pixels.; Preserves: Wall/opening graph and source-vector references; Confirmed plan dimensions and model-brief parameter provenance; Separate wall/opening component identities; Changes or infers: Extrudes confirmed plan graph into separate candidate wall/opening solids and groups them as a CAD assembly.; Does not assign IFC classifications or unobserved construction layers.; Checks: Check every generated opening attaches to its intended wall segment.; Check room graph/connectivity, wall lengths/thicknesses, opening positions and elevations.; Verify generated top/plan projections against the source plan and compare all known controls.; Alternatives: Manual wall/opening construction from the reviewed graph in OCS or FreeCAD.; Automation: mixed; Evidence status: proposed_composition; Summary: Compose a confirmed plan graph and explicit elevation/opening parameters into separate CAD wall/opening solids. Floor-plan papers describe research recognition/reconstruction methods; this operation proposes an editable CAD handoff and does not claim BIM/IFC semantics.
7. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); [step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `cv2.getPerspectiveTransform(src_pts,dst_pts); cv2.warpPerspective(plan,H,size); human trace wall/opening graph; FreeCAD PartDesign/Sketcher model from reviewed graph`; Status: existing_tool_entrypoint; Source urls: https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md; Notes: Paper methods inform interpretation but provide no claimed general-purpose CLI; OpenCV rectification and FreeCAD feature creation are documented tools. Paper code not installed or run.

## Output artifacts

1. **Representations:** ifc / cad-solid
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: floor layout; Quantity: wall/opening lengths and opening positions; Unit: mm; Acceptance: reviewed graph closes and supplied dimensions agree; Method: Compare traced vector graph and CAD walls/openings against calibrated plan and source dimensions.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 4
3. **Compute:** 3
4. **Human reason:** Topology and labels need review; vertical dimensions usually need separate evidence.
5. **Setup reason:** OpenCV, OCR and CAD application integration.
6. **Compute reason:** CPU image processing plus moderate geometry; larger plans and semantic extraction increase cost.

## Resources and scaling

1. **Cpu:** CPU image processing plus moderate geometry; larger plans and semantic extraction increase cost.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with plan pixels, walls, openings and floors.
4. **Storage:** Preserve plan originals, rectified plan, reviewed graph and building CAD.
5. **Scaling drivers:** plan pixels, walls, openings and floors
6. **Variants:** Manual/CPU baseline; learned plan parser requires its documented model environment.

## Detailed branch procedures

1. [dom-r01.md](/home/leo/projects/3dmodeling/research/workflows/details/dom-r01.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html)
2. [https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf)
3. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
