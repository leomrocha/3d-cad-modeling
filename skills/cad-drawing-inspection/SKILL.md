---
name: cad-drawing-inspection
description: Inspect a DXF drawing's original entities, declared units, spaces, layers, nested blocks and source coordinate systems before selecting geometry for CAD construction.
---

# Inspect a DXF drawing before selecting a profile

Use the [operation selection procedure](references/modeling-operation-selection.md) for component reuse, provider capability checks and job evidence. Apply it to the requested operation.

Implements the DXF branch of **Inspect source entities, units and drawing contexts (CAD-08-A01)**. Read the existing inspection for the same source hash, space, layer selection and options before executing another inspection.

## Package setup

Set `SKILL_ROOT` to this installed skill directory and `SOURCE_ROOT` to the caller-owned drawing directory. Use Python 3.12 on Linux or macOS:

```sh
python3 -m venv "$SOURCE_ROOT/drawing-env"
. "$SOURCE_ROOT/drawing-env/bin/activate"
python -m pip install -r "$SKILL_ROOT/requirements.txt"
python "$SKILL_ROOT/scripts/package_check.py"
```

## Inputs and command

1. Preserve the exact original DXF path and source identity. Select the required layout explicitly; `Model` is the default. Select layers when the job identifies them. The inspection returns all encountered occurrence IDs with an explicit selection flag.
2. Use the pinned [native-reader dependencies](requirements.txt), including ezdxf1.4.5. Install them in the selected Python environment. The tool uses ezdxf directly and the existing `component_records.observe_file` helper.

```sh
python3 \
  ${SKILL_ROOT}/scripts/dxf_inspect.py \
  ${SOURCE_ROOT}/source.dxf --space Model \
  --output ${SOURCE_ROOT}/new-inventory.json
```

3. Add repeated `--layer NAME` arguments for explicit layer selection. Optional bounds: `--max-entities`, `--max-depth`, `--max-bytes`. Defaults are 10000 occurrences, 32 nested block levels and 64 MiB of source bytes. A source over a bound fails with the affected limit.
4. Existing output paths are protected. The original file is read and its hash compared before and after parsing. No source repair or unit conversion is performed by this command. Exit0 means the inventory was written; exit2 reports invalid input, an exceeded bound or an I/O/parser failure.

## Read the inventory

1. `source` gives the original path, hash and byte count. `reader` records ezdxf version and options. `space`, available layouts/layers, selected layers and counts retain the drawing context.
2. `units` records the actual `$INSUNITS` code and decoded unit. A unitless header yields `NEEDS_UNIT_EVIDENCE`; retain that result beside the affected profile before supplying a dimensional interpretation.
3. Every entity has its source handle, occurrence path, original/effective layer, selected flag, type and retained DXF attributes. Layer0 inherits the containing INSERT layer. Annotation and unclassified roles remain explicit. A profile candidate is a software type classification; the agent identifies the intended physical contour.
4. Block occurrences retain original block base points, units and transforms. `world_from_block_rows` is an ezdxf row-vector matrix mapping containing-block coordinates to drawing WCS. Parent transforms compose after child transforms. MINSERT cells get distinct occurrence paths and transformed positions. Cyclic or missing blocks are recorded as issues.
5. Source entity OCS means its own object coordinate system. ARC/CIRCLE/LWPOLYLINE and2D POLYLINE retain that label, extrusion normal and original attributes. Their source coordinates and bulges remain unchanged. The selected geometry adapter applies the entity OCS transform before the recorded containing-block transform.
6. Attached attributes retain their source occurrence. An array with attributes records the specific expansion issue for review. Geometry occurrence expansion is bounded before allocating a large array.

## Agent review and downstream action

1. Identify source profile, annotations and construction geometry using the actual source/context. Review units, source dimensions, selected occurrence IDs, plane and any cyclic/missing-block issues.
2. Pass the original source hash, chosen occurrence paths, units and target-plane decision to **Create a mapped and explicitly cleaned derivative (CAD-08-A02)**. The source-to-profile transformation belongs to that action.
3. Retain the actual inventory and its source hash in caller-owned job storage. Verify nested transforms against independently supplied points before selecting geometry for construction.
4. For a multi-view DXF, identify the projection and physical datum in each view before combining entities. Keep drawing-sheet positions separate from part coordinates. For each shared landmark, pass its occurrence IDs, view-to-part axis directions, physical coordinates, units and their evidence to the builder. Resolve conflicting values against the source revision. Preserve hidden lines, dimensions and keep-outs as distinct roles when selecting the profile.

## Raster profiles and dimension leaders

Use the original DXF entities for a vector profile. For a raster or mask, select an interpreter using the optional cad-opencv-setup contours probe. Run [raster_features.py](scripts/raster_features.py) SOURCE NEW_OUTPUT --threshold N. Add --dark for dark foreground. Inspect the numbered overlay and hierarchy at source resolution. A stroke has two edges. An occlusion or crossing annotation can join regions or open a hole. Preserve affected samples and request a corrected mask or original vector. Use fit_samples on picked pixels for an open arc or straight edge. Compare line RMS error in pixels against pick uncertainty. The ellipse candidate includes sampled angular span and normalized radial error. Verify residuals, visibility and design evidence before naming a bore.

For one evidenced plane add --controls JSON with source_sha256, pixels, plane_mm, held_pixels, held_mm and limit_mm. Keep a signed part frame, source hash and separately identified control points. Check that held-out points cover the work region. Inspect hole orientation and nominal dimensions against the source. For OCR keep the text region, view and leader endpoint. Use leader_candidates in [image_observations.py](scripts/image_observations.py) with the endpoint and pick tolerance in pixels. Resolve multiple or wrong candidates against the dimension extension lines and name the selected feature in the revision.

For a dimension crop and an available local PaddleOCR recognizer, run the provider interpreter with [raster_text.py](scripts/raster_text.py) ORIGINAL MODEL_DIRECTORY --crop LEFT TOP RIGHT BOTTOM. Right and bottom are exclusive pixel indices. Use the returned text receipt with image_observations.py. The recorded model hash, source crop and recognition score accompany the proposed text. Check the leader and decimal point against the original drawing before using the value.
