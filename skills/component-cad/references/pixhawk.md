# Holybro Pixhawk 6C source-dimension reference

Use this procedure for C052 when the currently retained source is the Holybro
Pixhawk 6C dimension drawing. The drawing is an original JPEG at
`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/source/holybro-pixhawk-6c-dimensions.jpg`.
Its exact URL, retrieval time, MIME type and SHA-256 are recorded in that job's
`source-records.json`. The official download page lists a “Pixhawk 6C Case CAD
3D File”, but its published attachment currently returns HTTP 404. The Pixhawk
6C Mini CAD files describe a different product and are excluded.

## Source-defined reference model

The manufacturer drawing specifies 84.8±0.1 mm length, 44±0.1 mm width,
12.4±0.1 mm thickness, a 32±0.1 × 60±0.1 mm four-hole mounting pattern, and
four M2 threaded holes with 6 mm thread depth. Holybro lists plastic and
aluminum case variants, with masses 34.6 g and 59.3 g respectively; the
dimension drawing does not identify which variant it depicts.

`scripts/pixhawk.py` builds a dimension envelope and four nominal M2 thread
reference cylinders. Its frame is a modeling proposal: origin at the center of
the rear mounting face, X along the 84.8 mm case length, Y along the 44 mm
width, and +Z through the 12.4 mm thickness toward the connector face. The
thread centers are (±30, ±16) mm and their 6 mm depth runs along +Z. The 2 mm
cylinders represent the M2 nominal designation; they do not represent thread
flanks or a tap-drill diameter.

The component job records a 0.01 mm cutter overrun outside the mounting face
as a CAD Boolean construction allowance. It is not a manufacturer dimension;
the bottom-plane check remains at the source-defined 6.00 mm thread depth.

Name this geometry a **dimension envelope** or **mechanical reference**. The
rectangular envelope does not represent the detailed case exterior. The
orthographic drawing can support a separate, attributed trace of bevels,
stepped side profiles and connector-window outlines. Keep each trace's source
pixel coordinates, image-scale calibration, coordinate mapping and measurement
uncertainty beside the reconstructed feature. Do not infer connector internals,
PCB geometry, wall thickness, case material, or connected shell construction
from this exterior drawing. Keep C055 Holybro PM02 V3 as a separate component.

## Construction and checks

1. Run `scripts/model_inventory.py` with the C052 component index and work index
   before construction. Preserve an existing matching model if one is found.
2. Run `python3 scripts/component_records.py ABSOLUTE_SOURCE_JOB.json` and
   require `SOURCE_READY`. The pinned C052 source job checks the downloaded
   drawing hash for each numeric feature.
3. Connect to the coordinator-authorized native OCS session. Build only the
   dimension envelope and four blind nominal M2 references using the installed
   `cadtools.geometry.Geometry` adapter and `SelectionCheckedClient`.
4. Read the created solid back through the existing SAT/SAB readers. Run
   `pixhawk.verify` against the source job. Its checks compare vertex extrema,
   all four thread-axis centers/diameters, and the four planar blind-hole
   bottoms. CAD numerical tolerance is separate from the drawing's ±0.1 mm
   source limits.
5. Save and reopen under the component job's authorized path. Repeat the same
   checks against the reopened native record and report the document identity,
   revision, geometry revision, native file hash and actual model identity.
6. Use `python3 -m unittest tests/test_pixhawk.py` for the offline checks of
   source-dimension logic. Passing tests do not establish a native OCS build or
   a manufacturer's detailed case model.

## Executed C052 reference — 13 November 2026

The current reference is `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/holybro-pixhawk-6c-mechanical-reference.dwg`.
The build used isolated document 93 and reopened document 94; active document
92 stayed unchanged. Saved SHA-256:
`1431c006fa758a4978533b52c398e6f4a9e5d52113d713fd14ebbd75e491de6f`.
The reopened file contains one closed connected 3D solid, and the audit reports
zero errors and zero warnings. Independent post-reopen checks pass for the
84.8 × 44 × 12.4 mm extrema, the four M2 reference axes at (±30, ±16) mm, and
all four bottom planes at z=6 mm. SAB parsing used the already available
`${NATIVE_READER_ROOT}` environment; no package was installed.

This result completes the **source-dimensioned mechanical reference**. The
rectangular solid is a clearance envelope with mounting references. It is not
the detailed Holybro case model. The detailed exterior/cutouts remain separate
because the published case CAD attachment returned HTTP 404 and the retained
drawing does not dimension all case contours or connector openings. Actual
model identity: `gpt-6-luna`.
