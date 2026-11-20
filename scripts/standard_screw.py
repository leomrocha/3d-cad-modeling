"""Generate and check a cosmetic ISO 4017 screw using an installed FastenerCAD source tree."""

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path


def generate(tree, spec, out):
    import cadquery as cq

    data = json.loads(spec.read_bytes())
    if data["standard"] != "ISO 4017" or data["thread_series"] != "coarse":
        raise ValueError("This route supports ISO 4017 coarse threads")
    size = data["size"]
    if (
        not isinstance(size, str)
        or not size.startswith("M")
        or not size[1:].replace(".", "", 1).isdigit()
    ):
        raise ValueError("Expected metric size designation")
    expected = data["reference"]
    if not expected["source"] or not expected["edition"]:
        raise ValueError("Identify the source table and edition")
    length = data["length_mm"]
    if not math.isfinite(length) or length <= 0 or length not in expected["lengths_mm"]:
        raise ValueError("Length is outside the supplied reference row")
    table = tree / "catalog" / (size + ".json")
    original = json.loads(table.read_bytes())
    if original["thread"]["coarse"]["pitch"] != expected["pitch_mm"]:
        raise ValueError("Source and generator thread pitches differ")
    sys.path.insert(0, str(tree.resolve()))
    from standards.ISO4017 import HexScrewISO4017

    out.mkdir(parents=True, exist_ok=False)
    step = out / "reference.step"
    HexScrewISO4017(
        size=size, length=length, thread="cosmetic", thread_series="coarse"
    ).to_step(step)
    shape = cq.importers.importStep(str(step)).val()
    if len(shape.Solids()) != 1 or not shape.isValid():
        raise ValueError("Generated STEP must reopen as one valid solid")
    (bearing,) = [
        f for f in shape.Faces() if f.geomType() == "PLANE" and len(f.Wires()) == 2
    ]
    (cylinder,) = [f for f in shape.Faces() if f.geomType() == "CYLINDER"]
    flat_spans = [
        2 * math.hypot(e.Center().x, e.Center().y) for e in bearing.outerWire().Edges()
    ]
    if len(flat_spans) != 6:
        raise ValueError("Expected six flats on the screw head")
    z = bearing.Center().z
    bounds = shape.BoundingBox()
    head_height = bounds.zmax - z
    underhead = z - bounds.zmin
    corners = max(
        math.dist(a.toTuple(), b.toTuple())
        for a in bearing.outerWire().Vertices()
        for b in bearing.outerWire().Vertices()
    )
    eps = 1e-5

    def in_range(value, limits):
        low, high = limits
        return low - eps <= value <= high + eps

    checks = dict(
        length=abs(length - underhead) <= eps,
        height=in_range(head_height, expected["head_height_mm"]),
        flats=all(in_range(v, expected["across_flats_mm"]) for v in flat_spans),
        corners=corners >= expected["min_across_corners_mm"] - eps,
    )
    result = dict(
        checks=checks,
        nominal_thread_envelope_mm=float(size[1:]),
        represented_thread_diameter_mm=cylinder.BoundingBox().xlen,
        units="mm",
        underhead_mm=underhead,
        head_height_mm=head_height,
        across_flats_mm=flat_spans,
        across_corners_mm=corners,
        source=expected["source"],
        edition=expected["edition"],
        generator_table_sha256=hashlib.sha256(table.read_bytes()).hexdigest(),
        spec_sha256=hashlib.sha256(spec.read_bytes()).hexdigest(),
        step_sha256=hashlib.sha256(step.read_bytes()).hexdigest(),
    )
    (out / "receipt.json").write_text(
        json.dumps(result, indent=2, allow_nan=False) + "\n"
    )
    if not all(checks.values()):
        raise ValueError("STEP outside reference limits; see receipt.json")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("tree", "spec", "new_output"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    generate(args.tree, args.spec, args.new_output)
