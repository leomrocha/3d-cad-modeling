---
name: drawing-inspection
description: Inspect a DXF drawing's original entities, declared units, spaces, layers, nested blocks and source coordinate systems before selecting geometry for CAD construction.
---

# Inspect a DXF drawing before selecting a profile

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
3. [Execution report](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/dxf-inspection.md) links two actual retained DXF runs and eight tests, including independent nested-transform controls.
