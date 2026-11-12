#!/usr/bin/env python3
"""Reference CadQuery DXF-profile importer and STEP extruder.

The DXF remains unchanged. Exactly one closed wire on the requested layer is
accepted so the script does not silently guess nested contour semantics.
This file is reference code; it has not been run against CadQuery here.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import cadquery as cq
import ezdxf
from ezdxf import units as dxf_units


def positive_finite(value: float, name: str) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dxf", type=Path, required=True, help="source DXF; never modified")
    parser.add_argument("--layer", required=True, help="one profile layer to import")
    parser.add_argument("--scale-to-mm", type=float, required=True,
                        help="explicit source-coordinate multiplier into millimetres")
    parser.add_argument("--extrusion-mm", type=float, required=True,
                        help="confirmed extrusion length in millimetres")
    parser.add_argument("--merge-tolerance-source-units", type=float, required=True,
                        help="CadQuery wire-merge tolerance in original DXF coordinate units")
    parser.add_argument("--step", type=Path, required=True, help="new .step output path")
    parser.add_argument("--allow-header-scale-mismatch", action="store_true",
                        help="allow explicit scale to override a conflicting DXF $INSUNITS value")
    parser.add_argument("--overwrite", action="store_true", help="allow replacing existing STEP output")
    args = parser.parse_args()

    source_path = args.dxf.resolve(strict=True)
    output_path = args.step.resolve()
    if source_path == output_path:
        raise SystemExit("source DXF and STEP output must be separate files")
    if output_path.suffix.lower() != ".step":
        raise SystemExit("output path must use the .step extension")
    if output_path.exists() and not args.overwrite:
        raise SystemExit(f"output exists; pass --overwrite to replace it: {output_path}")

    scale = positive_finite(args.scale_to_mm, "scale-to-mm")
    height = positive_finite(args.extrusion_mm, "extrusion-mm")
    merge_tolerance = positive_finite(
        args.merge_tolerance_source_units, "merge-tolerance-source-units"
    )

    document = ezdxf.readfile(source_path)
    matching_layers = [layer.dxf.name for layer in document.layers
                       if layer.dxf.name.casefold() == args.layer.casefold()]
    if not matching_layers:
        raise SystemExit(f"DXF layer does not exist: {args.layer}")
    layer = matching_layers[0]
    insunits = int(document.header.get("$INSUNITS", 0))
    header_scale_mm = None
    if insunits:
        try:
            header_scale_mm = dxf_units.conversion_factor(insunits, dxf_units.MM)
        except (ValueError, TypeError) as error:
            raise SystemExit(f"unsupported DXF $INSUNITS value {insunits}: {error}") from error
        if (not math.isclose(scale, header_scale_mm, rel_tol=1e-9, abs_tol=1e-12)
                and not args.allow_header_scale_mismatch):
            raise SystemExit(
                f"explicit scale {scale} mm/unit disagrees with DXF $INSUNITS "
                f"conversion {header_scale_mm} mm/unit; inspect source or pass "
                "--allow-header-scale-mismatch after confirming the drawing scale"
            )

    # Read only the selected layer. The importer's tolerance is expressed in
    # source drawing coordinates; scaling is applied after wire construction.
    imported = cq.importers.importDXF(
        str(source_path), tol=merge_tolerance, include=[layer]
    )
    source_wires = imported.wires().vals()
    if len(source_wires) != 1:
        raise SystemExit(
            f"expected exactly one imported wire on {layer!r}; found {len(source_wires)}. "
            "Separate contours or resolve inner/outer wire roles before using this reference script."
        )
    wire = source_wires[0]
    if not wire.Closed():
        raise SystemExit("selected DXF profile wire is open")
    if not wire.isValid():
        raise SystemExit("selected DXF profile wire is invalid")

    factor_matrix = cq.Matrix([
        [scale, 0.0, 0.0, 0.0],
        [0.0, scale, 0.0, 0.0],
        [0.0, 0.0, scale, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    scaled_wire = wire.transformGeometry(factor_matrix)
    profile = cq.Workplane("XY").newObject([scaled_wire]).wires().toPending()
    result = profile.extrude(height)
    shape = result.val()
    if not shape.isValid():
        raise SystemExit("extruded result failed CadQuery/OCCT shape validity check")
    if result.solids().size() != 1:
        raise SystemExit("expected exactly one connected solid after extrusion")
    bounds = shape.BoundingBox()
    if not math.isclose(bounds.zlen, height, rel_tol=1e-8, abs_tol=1e-7):
        raise SystemExit(f"extrusion Z extent {bounds.zlen} mm differs from {height} mm")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.export(str(output_path), unit="MM", outputUnit="MM")
    reopened = cq.importers.importStep(str(output_path), unit="MM")
    if not reopened.val().isValid() or reopened.solids().size() != 1:
        raise SystemExit("STEP readback failed validity or single-solid check")
    print(json.dumps({
        "status": "reference-code-result",
        "source_dxf": str(source_path),
        "source_sha256": __import__("hashlib").sha256(source_path.read_bytes()).hexdigest(),
        "layer": layer,
        "dxf_insunits": insunits,
        "header_scale_mm_per_unit": header_scale_mm,
        "applied_scale_mm_per_unit": scale,
        "extrusion_mm": height,
        "step_file": str(output_path),
        "solid_count": reopened.solids().size(),
        "bounding_box_mm": {
            "x": reopened.val().BoundingBox().xlen,
            "y": reopened.val().BoundingBox().ylen,
            "z": reopened.val().BoundingBox().zlen,
        },
        "volume_mm3": reopened.val().Volume(),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
