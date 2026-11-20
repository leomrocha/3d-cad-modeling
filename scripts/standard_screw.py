"""Generate and check a cosmetic ISO 4017 screw using an installed FastenerCAD source tree."""

import argparse
import hashlib
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

from batch_dxf_lines import publish_directory
from catalogue_candidates import search_saved
from operation_catalogue import location


def positive(value):
    return type(value) in (int, float) and math.isfinite(value) and value > 0


def measured_match(review, fields, row, diameter):
    geometry = review.get("geometry") or {}
    if geometry.get("one_valid_solid") is not True or geometry.get("coaxial") is not True:
        return False
    if not geometry.get("evidence") or not positive(diameter):
        return False
    for key in ("underhead_mm", "shaft_diameter_mm", "head_height_mm", "across_flats_mm",
                "across_corners_mm"):
        if not positive(geometry.get(key)):
            return False
    return (abs(geometry["underhead_mm"] - fields["length_mm"]) <= 1e-5
            and abs(geometry["shaft_diameter_mm"] - diameter) <= 1e-5
            and row["head_height_mm"][0] <= geometry["head_height_mm"] <= row["head_height_mm"][1]
            and row["across_flats_mm"][0] <= geometry["across_flats_mm"] <= row["across_flats_mm"][1]
            and geometry["across_corners_mm"] >= row["min_across_corners_mm"])


def catalogue_route(catalogue, required, reviews, row, shaft_diameter, failures):
    """Use the configured snapshots and qualify assets against reviewed specifications."""
    def related(record):
        private = record.get("private_source") or {}
        if (private.get("variant") or {}).get("standard") == required["standard"]:
            return True
        return any(isinstance(item, dict) and item.get("designation") == required["standard"]
                   for item in record.get("standards") or [])

    query = f'iso-4017-{required["size"].lower()}x{required["length_mm"]:g}'
    sources = search_saved(catalogue, query, include_record=related)
    for name, source in sources.items():
        if source.get("method_errors"):
            failures[name] = "; ".join(source["method_errors"])
        if source.get("error") or source.get("reached_search_limit"):
            failures[name] = source.get("error", "search limit")
    parameter = None
    for source in sources.values():
        for candidate in source.get("candidates", []):
            digest = candidate.get("sha256")
            if not digest:
                continue
            private = candidate.get("private_source") or {}
            review = reviews.get(digest) or private
            fields = review.get("variant") or {}
            if not review.get("evidence") or not all(
                fields.get(key) == value for key, value in required.items() if key != "length_mm"
            ):
                continue
            expected_shaft = shaft_diameter
            if expected_shaft is None and required["representation"] == "cosmetic":
                expected_shaft = fields.get("cosmetic_shaft_diameter_mm")
            if not positive(fields.get("length_mm")) or not measured_match(review, fields, row, expected_shaft):
                continue
            receipt = dict(geometry=review["geometry"], asset=candidate["locator"], sha256=digest, evidence=review["evidence"])
            if fields.get("length_mm") == required["length_mm"]:
                return dict(route="reuse", **receipt)
            control = review.get("length_parameter")
            if fields.get("length_mm") and isinstance(control, dict) and control.get("name") and (
                required["length_mm"] in control.get("lengths_mm", [])
            ):
                parameter = dict(route="modify-length-parameter", parameter=control["name"],
                                 requested_mm=required["length_mm"], **receipt)
    return parameter


def prepare(tree, spec, out, catalogue, pins, *, published=False):
    def read(path):
        raw = path.read_bytes()
        pins[path] = hashlib.sha256(raw).hexdigest()
        return raw

    data = json.loads(read(spec))
    if data["standard"] != "ISO 4017" or data["thread_series"] != "coarse":
        raise ValueError("This route supports ISO 4017 coarse threads")
    size = data["size"]
    if (
        not isinstance(size, str)
        or not size.startswith("M")
        or not size[1:].replace(".", "", 1).isdigit()
    ):
        raise ValueError("Expected metric size designation")
    head = data.get("head_form", "external-hex")
    if head != "external-hex":
        raise ValueError("ISO 4017 requires an external hexagon head")
    expected = data["reference"]
    row_hash = None
    identity = dict(size=size, standard=data["standard"], thread_series="coarse", head_form=head)
    if "row_file" in expected:
        raw = read(spec.parent / expected["row_file"])
        row_hash = hashlib.sha256(raw).hexdigest()
        if row_hash != expected["sha256"]:
            raise ValueError("Independent reference file hash differs")
        row = json.loads(raw)
        if not identity.keys() <= row.keys():
            raise ValueError("Independent reference row must identify the screw designation and head")
        if row.get("grade") != "A" or str(row.get("edition")) != "2022":
            raise ValueError("Independent row must identify ISO 4017:2022 grade A")
        if "pitch_mm" not in row:
            raise ValueError("Independent reference row must identify pitch")
        if "pitch_mm" in expected and expected["pitch_mm"] != row["pitch_mm"]:
            raise ValueError("Legacy pitch differs from independent row")
        expected = row
    for key, value in identity.items():
        if key in expected and expected[key] != value:
            raise ValueError(f"Reference row mismatch: {key}")
    if "pitch_mm" in expected and (
        type(expected["pitch_mm"]) not in (int, float)
        or not math.isfinite(expected["pitch_mm"]) or expected["pitch_mm"] <= 0
    ):
        raise ValueError("Invalid reference pitch")
    if not isinstance(expected.get("source"), str) or not expected["source"].strip() or not expected.get("edition"):
        raise ValueError("Identify the source table and edition")
    if data.get("grade", "A") != "A" or expected.get("grade", "A") != "A":
        raise ValueError("Unsupported product grade")
    if ("edition" in data and str(data["edition"]) not in ("2022", "ISO 4017:2022")) or (
        str(expected["edition"]) not in ("2022", "ISO 4017:2022")
    ):
        raise ValueError("Unsupported ISO 4017 edition")
    for key in ("head_height_mm", "across_flats_mm"):
        limits = expected.get(key)
        if not isinstance(limits, list) or len(limits) != 2 or not all(map(positive, limits)) or limits[0] > limits[1]:
            raise ValueError("Invalid reference limits: " + key)
    if not positive(expected.get("min_across_corners_mm")):
        raise ValueError("Missing minimum across corners")
    length = data["length_mm"]
    diameter = float(size[1:])
    if not positive(length) or not positive(diameter) or diameter > 24 or length > min(150, 10 * diameter):
        raise ValueError("Request outside supported grade A size and length range")
    lengths = expected.get("lengths_mm")
    if not isinstance(lengths, list) or not all(map(positive, lengths)) or length not in lengths:
        raise ValueError("Length is outside the supplied reference row")
    representation = data.get("representation", "cosmetic")
    if representation not in ("nominal-envelope", "cosmetic"):
        raise ValueError("Unsupported screw representation")
    failures = {}
    metadata = dict(source=expected["source"], edition=expected["edition"],
                    independent_row_sha256=row_hash, spec_sha256=pins[spec],
                    reference_kind="independent-row" if row_hash else "caller-supplied limits",
                    catalogue_failures=failures)

    def select(pitch, shaft_diameter):
        required = dict(**identity, pitch_mm=pitch, length_mm=length, representation=representation,
                        grade="A", edition="2022")
        selection = catalogue_route(catalogue or location(), required, data.get("asset_reviews", {}),
                                    expected, shaft_diameter, failures)
        if selection:
            return dict(**selection, **metadata)
        return None

    independent_shaft = diameter if representation == "nominal-envelope" else expected.get("cosmetic_shaft_diameter_mm")
    if positive(expected.get("pitch_mm")):
        selection = select(expected["pitch_mm"], independent_shaft)
        if selection:
            return selection
    if representation == "nominal-envelope" and row_hash:
        raise ValueError(f"No qualified nominal-envelope asset or exposed parameter. Parts source errors: {failures}")
    table = tree / "catalog" / (size + ".json")
    if not table.is_file():
        raise ValueError("Designation outside the installed ISO 4017 size table")
    original = json.loads(read(table))
    if original["designation"] != size or original["nominal_diameter"] != diameter:
        raise ValueError("Generator table designation or nominal diameter differs")
    coarse = original["thread"]["coarse"]
    pitch = coarse["pitch"]
    if not positive(pitch) or not positive(coarse["pitch_dia"]) or coarse["pitch_dia"] >= diameter:
        raise ValueError("Invalid generator pitch or pitch diameter")
    if "pitch_mm" in expected and pitch != expected["pitch_mm"]:
        raise ValueError("Source and generator thread pitches differ")
    selection = select(pitch, diameter if representation == "nominal-envelope" else coarse["pitch_dia"])
    if selection:
        return selection
    if representation != "cosmetic":
        raise ValueError(f"No qualified nominal-envelope asset or exposed parameter. Parts source errors: {failures}")
    import cadquery as cq

    step = out / "reference.step"
    provider_files = [file for folder in ("standards", "threads", "common", "catalog", "export")
                      for file in sorted((tree / folder).rglob("*.py"))]
    for file in provider_files:
        read(file)
    if not published:
        subprocess.run([sys.executable, "-I", "-B", "-c",
                        "import sys; sys.path.insert(0,sys.argv[1]); "
                        "from standards.ISO4017 import HexScrewISO4017; "
                        "from pathlib import Path; "
                        "HexScrewISO4017(size=sys.argv[2],length=float(sys.argv[3]),"
                        "thread='cosmetic',thread_series='coarse').to_step(Path(sys.argv[4]))",
                        str(tree.resolve()), size, str(length), str(step.resolve())], check=True)
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

    surface = cylinder._geomAdaptor().Cylinder()
    axis = surface.Axis()
    direction = axis.Direction()
    center = axis.Location()
    shaft_bounds = cylinder.BoundingBox()
    checks = dict(
        shaft_pitch_diameter=abs(2 * surface.Radius() - coarse["pitch_dia"]) <= eps,
        shaft_coaxial=math.hypot(direction.X(), direction.Y()) <= eps and math.hypot(center.X(), center.Y()) <= eps,
        shaft_meets_bearing=abs(shaft_bounds.zmax - z) <= eps and shaft_bounds.zmin < z,
        bearing_centered=math.hypot(bearing.Center().x, bearing.Center().y) <= eps,
        length=abs(length - underhead) <= eps,
        height=in_range(head_height, expected["head_height_mm"]),
        flats=all(in_range(v, expected["across_flats_mm"]) for v in flat_spans),
        corners=corners >= expected["min_across_corners_mm"] - eps,
    )
    result = dict(
        checks=checks,
        route="generate",
        pitch_mm=pitch,
        pitch_cross_checked="pitch_mm" in expected,
        nominal_thread_envelope_mm=float(size[1:]),
        represented_thread_diameter_mm=cylinder.BoundingBox().xlen,
        units="mm",
        underhead_mm=underhead,
        head_height_mm=head_height,
        across_flats_mm=flat_spans,
        across_corners_mm=corners,
        **metadata,
        generator_table_sha256=pins[table],
        provider_code_sha256={file.relative_to(tree).as_posix(): pins[file] for file in provider_files},
        step_sha256=hashlib.sha256(step.read_bytes()).hexdigest(),
    )
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise ValueError("STEP outside reference limits: " + ", ".join(failed))
    return result


def check_pins(pins):
    for path, digest in pins.items():
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("Input changed during screw selection or generation: " + path.name)


def recover_published(tree, spec, out, catalogue):
    """Validate the request and reopen the already published STEP without exporting."""
    receipt = out / "receipt.json"
    if out.is_symlink() or not out.is_dir() or receipt.is_symlink() or not receipt.is_file():
        raise ValueError("Existing screw output has no regular receipt")
    receipt_bytes = receipt.read_bytes()
    stored = json.loads(receipt_bytes)
    pins = {receipt: hashlib.sha256(receipt_bytes).hexdigest()}
    if stored.get("spec_sha256") != hashlib.sha256(spec.read_bytes()).hexdigest():
        raise ValueError("Published screw request differs")
    names = {"receipt.json"}
    if stored.get("route") == "generate":
        names.add("reference.step")
        step = out / "reference.step"
        if step.is_symlink() or not step.is_file():
            raise ValueError("Existing screw output has no regular STEP")
        pins[step] = hashlib.sha256(step.read_bytes()).hexdigest()
        if pins[step] != stored.get("step_sha256"):
            raise ValueError("Published STEP differs from recorded hash")
    if {entry.name for entry in out.iterdir()} != names:
        raise ValueError("Published screw output differs from recorded files")
    result = prepare(tree, spec, out, catalogue, pins, published=True)
    check_pins(pins)
    if stored != result:
        raise ValueError("Published screw receipt differs from qualified request")
    return stored


def generate(tree, spec, out, catalogue=None):
    if out.exists() or out.is_symlink():
        return recover_published(tree, spec, out, catalogue)
    out.parent.mkdir(parents=True, exist_ok=True)
    pins = {}
    with tempfile.TemporaryDirectory(prefix=".screw-", dir=out.parent) as temp:
        staged = Path(temp) / "result"
        staged.mkdir()
        result = prepare(tree, spec, staged, catalogue, pins)
        check_pins(pins)
        (staged / "receipt.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        try:
            publish_directory(staged, out)
        except FileExistsError:
            return recover_published(tree, spec, out, catalogue)
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("tree", "spec", "new_output"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--catalogue", type=Path, help="Saved operation catalogue")
    args = parser.parse_args()
    generate(args.tree, args.spec, args.new_output, args.catalogue)
