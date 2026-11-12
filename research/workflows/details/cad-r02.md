# CAD-R02 — Raster sketch and measured scale to constrained profile and solid

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 2/5.**

Output: A reviewed dimensioned 2D profile and an extruded/revolved B-rep solid with native CAD source.

## Comparison conditions

One legible planar hand sketch with known in-plane control and enough dimensions for one part. Compare with clean DXF profile in CAD-R04.

## Registered starting artifact types

1. raster-sketch
2. dimensions

## Detailed source and preparation artifacts

1. Artifact: raster-sketch; Format: PNG/TIFF/JPEG or raster PDF page; Requirement: One planar view.; Quality: Sharp, high contrast, no folds over dimensions or profile.; Provenance: Original image retained.
2. Artifact: dimensions; Format: dimension list with units; Requirement: Known coplanar scale control plus all dimensions for selected feature.; Quality: Every value anchored to feature.; Provenance: Measured/annotated source.

## Reference points, datums and coordinate frames

1. **Plane:** drawing mapped to model XY
2. **Origin:** chosen corner/centre with image pixel coordinate stored
3. **Axes:** image y-down mapped to model Y by recorded transform; Z is extrusion axis
4. **Controls:** four corresponding non-collinear points for perspective rectification or known in-plane distances with view controlled
5. **Unit:** mm

## Software, libraries and dependencies

1. Name: OpenCV; Role: Planar image rectification and raster line candidates.; License: Apache-2.0 upstream.; Apis: cv2.getPerspectiveTransform(4 point pairs); cv2.warpPerspective; cv2.HoughLinesP; cv2.findContours/cv2.approxPolyDP; Dependencies: Python 3, OpenCV Python bindings (opencv-python or system package), NumPy; image file raster source.; Source urls: https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html; https://github.com/opencv/opencv/blob/4.x/LICENSE
2. Name: Tesseract; Role: Dimension text candidates with boxes/confidence; humans verify engineering notation.; License: Apache-2.0 upstream.; Apis: tesseract image outputbase -l eng tsv; TSV bbox/confidence review; Dependencies: Tesseract OCR binary plus eng traineddata; TSV output is text candidates only.; Source urls: https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md; https://github.com/tesseract-ocr/tesseract
3. Name: FreeCAD; Role: Complementary native feature-history and constrained-sketch backend.; License: LGPL-2.1-or-later per project licensing page.; Apis: FreeCAD Python console/macros; App.newDocument; Sketcher::SketchObject.addGeometry/addConstraint; Part::Feature.Shape or PartDesign::Body/Feature for solids; ViewPart/TechDraw orthographic projection; import/export via Draft/Part; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md; https://www.freecad.org/contributing.php?lang=eng
4. Name: OpenCADStudio; Role: Project baseline: native drawing/solid geometry controlled through editor/MCP; installed skill supplies geometry contract, readback and save rules. Inspected sources establish Solid3D/ACIS and mesh schemas, not general parametric feature history.; License: GPL-3.0 (local LICENSE file).; Apis: OpenCADStudio --mcp; ocs_control.py discover/read; ocs_execute after inspecting command schema; ocs_read geometry/entity records; Dependencies: OpenCADStudio desktop build with MCP enabled; Python 3 helper plus local session credentials/config.; Source urls: [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); [API-SPEC.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md); [LICENSE](/home/leo/projects/3rdparty/OpenCADStudio/LICENSE)

## Procedure

1. Order: 1; Action: Retain pixels and record view orientation, control points and dimensions.; Tool or command: image/source ledger; Human review: Classify object vs dimension/construction strokes.; Status: proposed_composition
2. Order: 2; Action: Rectify planar scan from controls; retain transform.; Tool or command: OpenCV getPerspectiveTransform/warpPerspective; Human review: Check an independent known length.; Status: proposed_composition
3. Order: 3; Action: OCR dimensions to TSV and manually confirm glyphs, units and feature anchors.; Tool or command: Tesseract CLI; Human review: Confidence is a candidate indicator, not acceptance.; Status: proposed_composition
4. Order: 4; Action: Extract line/contour candidates and overlay them on original.; Tool or command: OpenCV HoughLinesP/findContours/approxPolyDP; Human review: Manually distinguish profile from annotations.; Status: proposed_composition
5. Order: 5; Action: Trace/import profile; constrain against source-linked measurements.; Tool or command: FreeCAD Sketcher or OCS native geometry; Human review: Review solver state and changes.; Status: proposed_composition
6. Order: 6; Action: Create thickness/feature and verify B-rep.; Tool or command: FreeCAD/OCS/CadQuery; Human review: Extrusion or revolution values explicit.; Status: proposed_composition
7. Order: 7; Action: Save native model and separately requested STEP; reopen.; Tool or command: Owning CAD application; Human review: Compare dimensions and projection.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-02; Name: Rectify a raster drawing plane from known dimensions; Inputs: ; Outputs: measurement-set; Tools: OpenCV point correspondences; planar homography; Source urls: https://docs.opencv.org/5.0/main_modules/calib.html; Prerequisites: For scale, provide known dimensions on the same plane.; A planar homography rectifies that plane and does not recover object depth.; Preserves: Original image coordinates; Known control lengths; Image-to-plane transform; Changes or infers: Calculates a plane transform and metric image coordinates from matched points.; Checks: Check independent in-plane lengths after rectification.; Record controls, units and transformation.; Alternatives: Manual scale using a known dimension on a front-parallel scan; Automation: scripted; Evidence status: documented_capability; Summary: Rectify a single drawing plane using matched control coordinates; this route does not calibrate a general 3D camera or infer depth.; Input alternatives: raster-sketch; dimensions; raster-plan; dimensions
2. Id: CAD-03; Name: Recognize dimension text with OCR; Inputs: ; Outputs: text; Tools: Tesseract OCR TSV output; image crop/deskew; human transcription review; Source urls: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html; Prerequisites: Retain original pixels and page transform.; Use OCR output as candidates; resolve glyphs, units, tolerance symbols and feature association against the source image.; Preserves: Text bounding boxes; OCR confidence values; Original image and crop coordinates; Changes or infers: Produces candidate text strings and numeric dimension values from pixels.; Checks: Verify every dimension against the source crop.; Check decimal separator, diameter/radius symbols, tolerance, units and view association.; Alternatives: Manual dimension transcription; Vector drawing dimension records when available; Automation: assisted; Evidence status: documented_capability; Summary: Tesseract TSV can return text and word bounding boxes with confidence; engineering interpretation and dimension association remain review steps.; Input alternatives: raster-sketch; raster-plan
3. Id: CAD-04; Name: Extract raster edges, lines and contours; Inputs: ; Outputs: vector-drawing; Tools: OpenCV thresholding; HoughLinesP; findContours; approxPolyDP; Source urls: https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html; https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html; https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html; Prerequisites: Rectify or record the image transform before measuring extracted pixels.; Separate dimension lines, extension lines, text and object contours by layers or masks.; Preserves: Pixel coordinates and candidate segment endpoints; Source image identity; Changes or infers: Approximates raster strokes as candidate vectors; line/contour algorithms do not classify engineering intent by themselves.; Checks: Overlay candidates on source raster.; Measure endpoint gaps and edge displacement in calibrated coordinates.; Retain uncertain or intersecting candidates for review.; Alternatives: Manual trace in OCS or FreeCAD; Learned wall/opening segmentation followed by vectorization; Automation: scripted; Evidence status: proposed_composition; Summary: Image-processing primitives and floor-plan reconstruction research support candidate line extraction, while symbol and feature meaning require separate interpretation.; Input alternatives: raster-sketch; raster-plan
4. Id: CAD-01; Name: Extract a model brief from text and dimensions; Inputs: ; Outputs: model-brief; Tools: model brief schema; human review; OCS engineering skill; Source urls: [implementation-plan.md](/home/leo/projects/3dmodeling/research/implementation-plan.md); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); Prerequisites: Identify each value as supplied, measured, inferred, assumed, or calculated.; Declare units, origin, axes, component boundaries, intended output and source links.; Preserves: Original text; Value-to-source associations; Author's unresolved choices; Changes or infers: Groups explicit requirements into named parameters and geometry constraints.; Does not infer hidden geometry from prose alone.; Checks: Every numerical parameter has units and provenance.; Ambiguities affecting geometry are listed separately.; Alternatives: Direct interactive OCS modeling after brief readback; Code-CAD generation from a validated brief; Automation: assisted; Evidence status: proposed_composition; Summary: Create a source-linked brief before changing geometry; keep source claims separate from constraints and design choices.; Input alternatives: text; dimensions; text; dimensions
5. Id: CAD-08; Name: Read and clean vector drawing geometry; Inputs: vector-drawing; Outputs: vector-drawing; Tools: OpenCADStudio DWG/DXF/MCP; FreeCAD Draft DXF/SVG import; ezdxf; geometry audit; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_SVG.md; https://ezdxf.readthedocs.io/en/stable/; [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); [README.md](/home/leo/projects/3rdparty/OpenCADStudio/README.md); Prerequisites: Preserve source file and hash.; Determine drawing units, model/paper space, layer selection, block transforms, origin and target sketch plane.; Read DXF/SVG import option and unsupported entity behavior.; Preserves: Original file; Entity types, layers, blocks, annotations and source coordinates where supported; Changes or infers: Selects profile entities, normalizes transforms and may join, discretize, or repair curves.; Checks: Count input/output entities by type and layer.; Find duplicate/open/self-intersecting edges.; Compare profile bounds, area and source dimensions.; For SVG, verify viewBox and physical scale; FreeCAD importer flattens Z.; Alternatives: Use the source DXF unchanged in OCS; Use FreeCAD native DXF or legacy importer; Parse DXF with ezdxf and build clean geometry separately; Automation: mixed; Evidence status: documented_capability; Summary: FreeCAD documents DXF/SVG entity coverage and import modes; ezdxf reads and writes DXF. Entity preservation and scale depend on the specific importer/settings.
6. Id: CAD-09; Name: Build and constrain an editable planar sketch; Inputs: vector-drawing; Outputs: constrained-sketch; Tools: FreeCAD Sketcher scripting; FreeCAD Draft-to-Sketch; OpenCADStudio sketch/constraint capability as discovered in session; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md; [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); Prerequisites: Specify units, support plane and datum.; Resolve profile closure/repair and record which source curves changed.; Associate each dimensional constraint with measured/source/inferred status.; Preserves: 2D profile geometry; Named dimensions and geometric constraints; Constraint provenance in the project evidence ledger; Changes or infers: Adds constraints and may alter underconstrained geometry to satisfy them.; Checks: Solver state/degrees of freedom; Residuals and overconstraints; Source-to-constraint numeric comparison; Profile closedness and intersections; Alternatives: Keep vector geometry as non-parametric Draft/OCS drawing entities; Generate sketch geometry from code-CAD source; Automation: mixed; Evidence status: documented_capability; Summary: FreeCAD documents Python creation of Sketcher geometry and constraints. Solver success tests consistency, not the truth of supplied or inferred measurements.; Input alternatives: model-brief; dimensions; measurement-set
7. Id: CAD-10; Name: Create a kernel solid and native model document from confirmed parameters; Inputs: ; Outputs: cad-solid; native-model-document; Tools: OpenCADStudio kernel tools; FreeCAD PartDesign/Part; build123d; CadQuery; Source urls: https://build123d.readthedocs.io/en/latest/operations.html; https://cadquery.readthedocs.io/en/stable/; https://openscad.org/documentation; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md; [cadkernel-body-path.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/cadkernel-body-path.md); Prerequisites: Declare units, feature parameters, direction/axis and part boundary.; Use exact B-rep backend if exact surfaces/export are required.; Preserve native feature document or code source.; Preserves: Input dimensions and feature parameters; Native feature tree or executable parametric source; Part names and component boundaries; Editable native model document; feature history depends on the selected CAD application; Changes or infers: Creates exact kernel geometry from the confirmed profile/feature instructions; unsupported features may require alternatives.; Checks: Kernel shape validity and solid count; Bounds, volume, hole/shaft dimensions and units; Recompute or regenerate after one parameter change; Save/reopen and independent import; Alternatives: FreeCAD feature-history model; build123d/CadQuery Python source; OCS native body; separate exact STEP exporter if needed; Automation: scripted; Evidence status: documented_capability; Summary: Build kernel CAD solids from a confirmed constrained sketch, parametric source, or explicit model brief plus dimensions. FreeCAD/build123d/CadQuery provide documented B-rep routes; OCS creates native geometry but its inspected STEP writer emits mesh-derived faceted STEP.; Input alternatives: constrained-sketch; parametric-source; model-brief; dimensions
8. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: [README.md](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/README.md); [step.rs](/home/leo/projects/3rdparty/OpenCADStudio/src/io/step.rs); [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Code and tool entry points

1. Entrypoint: `cv2.getPerspectiveTransform(src_pts,dst_pts); cv2.warpPerspective(image,H,size)`; Status: existing_tool_entrypoint; Source urls: https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html; Notes: API example only; no image processed.
2. Entrypoint: `tesseract calibrated.png - -l eng tsv > dimensions.tsv`; Status: existing_tool_entrypoint; Source urls: https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md; Notes: TSV includes word boxes and confidence; review each engineering value.
3. Entrypoint: `cv2.HoughLinesP(...); cv2.findContours(...); cv2.approxPolyDP(...)`; Status: existing_tool_entrypoint; Source urls: https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html; https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html; Notes: Candidate vectors only; no engineering-meaning classifier.

## Output artifacts

1. **Representations:** raster-sketch; measurement-set; text; vector-drawing; constrained-sketch; cad-solid; native-model-document
2. **Editable source:** Original image, transform/OCR/vector ledger and native constrained sketch/features.
3. **Preserves:** source pixels and control transform; OCR candidates/boxes; human-confirmed feature-to-dimension links
4. **Loss or inference:** stroke centerlines approximate raster geometry; OCR may confuse glyphs; single sketch does not encode depth/thickness/hidden surfaces

## Checks

1. Object: scale; Quantity: withheld in-plane length; Unit: mm; Acceptance: within source tolerance; Method: Transform then measure independent length.
2. Object: OCR; Quantity: dimension transcription and feature association; Unit: text/mm; Acceptance: every value manually checked; Method: Overlay TSV boxes on pixels.
3. Object: profile; Quantity: closure/self-intersection; Unit: boolean/count; Acceptance: intended closed loops only; Method: CAD wire/Sketcher checks.
4. Object: constraints; Quantity: residual/degrees of freedom; Unit: mm/count; Acceptance: consistent with explicit constraints and source values; Method: Sketcher solver plus independent comparison.
5. Object: solid; Quantity: validity/bounds/count; Unit: boolean/mm/count; Acceptance: matches explicit features and units; Method: Kernel validity and STEP readback.

## Failure recovery

1. Failure: Bad/collinear rectification controls; Recovery: Rescan front-parallel or add planar control; do not infer scale from zoom.
2. Failure: Ambiguous OCR symbol; Recovery: Crop and transcribe manually; keep original pixel reference.
3. Failure: Open/merged vector profile; Recovery: Repair a copy under change log or trace manually; preserve original raster.
4. Failure: Solver conflict; Recovery: Inspect units, duplicate edges and constraint provenance; change only documented constraints.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 2
4. **Human reason:** Stroke classification, text confirmation and dimension/feature association require review.
5. **Setup reason:** OpenCV, Tesseract traineddata and CAD app; no model training.
6. **Compute reason:** One page is CPU image processing and small CAD; no GPU.

## Resources and scaling

1. **Cpu:** Low to moderate for one high-resolution page and contours.
2. **Gpu:** None.
3. **Ram:** Low to moderate; scales with raster dimensions.
4. **Storage:** Original/corrected raster, TSV, vector and CAD artifacts.
5. **Scaling drivers:** image pixels; number of pages; contour density; number of manual loops
6. **Variants:** front-parallel rescan reduces setup; tilted photo needs rectification; damaged/ambiguous scan increases human effort

## Original sources

1. [https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html](https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html)
2. [https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html)
3. [https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html)
4. [https://github.com/opencv/opencv/blob/4.x/LICENSE](https://github.com/opencv/opencv/blob/4.x/LICENSE)
5. [https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md](https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md)
6. [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
7. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)
8. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md)
9. [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
