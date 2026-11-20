"""Build a source-bound agent CAD sequence using CadQuery. Reopen and measure its STEP solid."""

import argparse
import hashlib
from importlib.metadata import version
import json
import math
import re
from pathlib import Path
import tempfile


def finite(value):
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        raise ValueError("Finite numeric CAD input required")
    return float(value)


def measured(shape):
    bounds = shape.BoundingBox()
    return dict(
        solids=len(shape.Solids()),
        faces=len(shape.Faces()),
        valid=shape.isValid(),
        volume_mm3=shape.Volume(),
        bounds_mm=[
            bounds.xmin,
            bounds.ymin,
            bounds.zmin,
            bounds.xmax,
            bounds.ymax,
            bounds.zmax,
        ],
    )


def build(sequence):
    import cadquery as cq

    if sequence["units"] != "mm" or not sequence["features"]:
        raise ValueError("Supply a nonempty feature sequence in millimetres")
    if not sequence.get("model") or not sequence.get("sources"):
        raise ValueError("Record the producing model and its input source identities")
    parameters = sequence["parameters"]
    for name, parameter in parameters.items():
        finite(parameter["value_mm"])
        if not name or parameter["basis"] not in {"explicit", "measured", "inferred"}:
            raise ValueError("Identify each parameter and its basis")
        if parameter.get("source") not in sequence["sources"]:
            raise ValueError("Parameter requires a known source")

    def val(name):
        return finite(parameters[name]["value_mm"])

    previous, seen = None, set()
    for item in sequence["features"]:
        name = item["id"]
        if not name or name in seen:
            raise ValueError("Each feature needs a unique name")
        seen.add(name)
        plane = item["plane"]
        if plane not in ("XY", "YZ", "XZ"):
            raise ValueError("Use a named local plane")
        work = cq.Workplane(plane, origin=tuple(val(n) for n in item["origin_xyz"]))
        profile = item["profile"]
        if profile["kind"] == "rectangle":
            w, h = val(profile["width"]), val(profile["height"])
            if min(w, h) <= 0:
                raise ValueError("Positive rectangle size required")
            work = work.rect(w, h)
        elif profile["kind"] == "circle":
            diameter = val(profile["diameter"])
            if diameter <= 0:
                raise ValueError("Positive circle diameter required")
            work = work.circle(diameter / 2)
        elif profile["kind"] == "polygon":
            vertices = [(val(x), val(y)) for x, y in profile["vertices"]]
            if len(set(vertices)) < 3:
                raise ValueError("Three distinct polygon vertices required")
            work = work.polyline(vertices).close()
        else:
            raise ValueError("Unsupported profile")
        depth = val(item["depth"])
        if depth == 0:
            raise ValueError("A zero-depth extrusion cannot form a solid")
        tool = work.extrude(depth)
        op = item["operation"]
        if op == "add":
            previous = tool if previous is None else previous.union(tool)
        elif op in ("cut", "intersect") and previous is not None:
            prior = previous.val().Volume()
            previous = previous.cut(tool) if op == "cut" else previous.intersect(tool)
            if op == "cut" and previous.val().Volume() >= prior:
                raise ValueError("Cut removed no material: " + name)
        else:
            raise ValueError(
                "First feature must add a solid; subsequent operations are add, cut, intersect"
            )
        if not previous.val().isValid() or len(previous.val().Solids()) != 1:
            raise ValueError(
                "Feature produced an invalid or disconnected solid: " + name
            )
    return previous


def run(sequence_file, output, source_paths=None):
    import cadquery as cq

    raw = sequence_file.read_bytes()
    sequence = json.loads(raw)
    output = output.resolve()
    if output.exists():
        raise FileExistsError(output)
    for name, item in sequence["sources"].items():
        if not re.fullmatch("[0-9a-f]{64}", item.get("sha256", "")):
            raise ValueError("Source digest missing or malformed: " + name)
    if source_paths is not None:
        if set(source_paths) != set(sequence["sources"]):
            raise ValueError("Supply paths for every source in the sequence")
        for name, path in source_paths.items():
            with Path(path).open("rb") as stream:
                if (
                    hashlib.file_digest(stream, "sha256").hexdigest()
                    != sequence["sources"][name]["sha256"]
                ):
                    raise ValueError("Source revision mismatch: " + name)
    datum = build(sequence)
    with tempfile.TemporaryDirectory(dir=output.parent) as directory:
        job = Path(directory)
        path = job / "solid.step"
        cq.exporters.export(datum, str(path))
        imported = cq.importers.importStep(str(path)).val()
        evidence = measured(imported)
        original = measured(datum.val())
        if (
            not evidence["valid"]
            or evidence["solids"] != 1
            or not math.isclose(
                original["volume_mm3"],
                evidence["volume_mm3"],
                abs_tol=1e-6,
                rel_tol=1e-8,
            )
        ):
            raise ValueError("STEP solid failed independent reopen checks")
        result = dict(
            model=sequence["model"],
            cadquery=version("cadquery"),
            sequence_sha256=hashlib.sha256(raw).hexdigest(),
            step_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            inferred_parameters=[
                key
                for key, row in sequence["parameters"].items()
                if row["basis"] == "inferred"
            ],
            source_bytes_checked=source_paths is not None,
            geometry=evidence,
        )
        (job / "sequence.json").write_bytes(raw)
        (job / "receipt.json").write_text(
            json.dumps(result, indent=2, allow_nan=False) + "\n"
        )
        # Only the exclusive output reservation is visible to other calls.
        output.mkdir()
        # Publish the completion receipt last so a partial job cannot appear complete.
        for name in ("solid.step", "sequence.json", "receipt.json"):
            (job / name).replace(output / name)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sequence", type=Path)
    parser.add_argument("new_directory", type=Path)
    parser.add_argument("--source", nargs=2, action="append", metavar=("ID", "FILE"))
    args = parser.parse_args()
    try:
        run(
            args.sequence,
            args.new_directory,
            dict(args.source) if args.source else None,
        )
    except ImportError as exc:
        parser.exit(2, f"Select an interpreter with CadQuery and OCP: {exc}\n")
