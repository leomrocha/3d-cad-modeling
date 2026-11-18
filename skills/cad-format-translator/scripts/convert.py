"""Create a new CAD derivative. Each command declares its source and target representation."""

import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import runpy
import sys
import subprocess
import tempfile

from scad_source import translate


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_stl(path):
    """Read oriented ASCII triangles, check watertight edges, extents and signed volume."""
    # OCCT's ASCII writer can use CRLF and whitespace; each facet has exactly three vertices.
    lines = iter(
        line.strip().split()
        for line in path.read_text(encoding="ascii").splitlines()
        if line.strip()
    )
    if next(lines, [])[:1] != ["solid"]:
        raise ValueError("Expected an ASCII STL solid")
    edges = Counter()
    low, high = [math.inf] * 3, [-math.inf] * 3
    count, volume = 0, 0.0
    while True:
        head = next(lines, [])
        if head[:1] == ["endsolid"]:
            break
        if head[:2] != ["facet", "normal"] or next(lines, []) != ["outer", "loop"]:
            raise ValueError("Malformed STL facet")
        points = []
        for _ in range(3):
            item = next(lines, [])
            if len(item) != 4 or item[0] != "vertex":
                raise ValueError("Missing STL vertex")
            point = tuple(map(float, item[1:]))
            if not all(map(math.isfinite, point)):
                raise ValueError("Nonfinite STL coordinates")
            points.append(point)
            low = list(map(min, low, point))
            high = list(map(max, high, point))
        if next(lines, []) != ["endloop"] or next(lines, []) != ["endfacet"]:
            raise ValueError("Incomplete STL facet")
        a, b, c = points
        u = [b[i] - a[i] for i in range(3)]
        v = [c[i] - a[i] for i in range(3)]
        cross = [
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0],
        ]
        if not any(cross):
            raise ValueError("Degenerate triangle")
        volume += sum(a[i] * cross[i] for i in range(3)) / 6
        edges.update(zip(points, points[1:] + points[:1]))
        count += 1
    if next(lines, None) is not None or not count or volume <= 0:
        raise ValueError("Expected one closed positive-volume STL")
    if any(n != 1 or edges[b, a] != 1 for (a, b), n in edges.items()):
        raise ValueError("Open, duplicated or nonmanifold mesh edges")
    return dict(triangles=count, bounds_mm=[low, high], signed_volume_mm3=volume)


def cq_shape(workplane):
    import cadquery as cq

    if isinstance(workplane, cq.Workplane):
        shapes = workplane.vals()
        if shapes and all(isinstance(s, cq.Shape) for s in shapes):
            return cq.Compound.makeCompound(shapes) if len(shapes) > 1 else shapes[0]
    if isinstance(workplane, cq.Shape):
        return workplane
    raise ValueError("Expected a CadQuery model Shape or Workplane of shapes")


def measures(shape):
    bb = shape.BoundingBox()
    if not shape.isValid() or not shape.Solids():
        raise ValueError("Expected valid solid geometry")
    return dict(
        solids=len(shape.Solids()),
        volume_mm3=shape.Volume(),
        bounds_mm=[[bb.xmin, bb.ymin, bb.zmin], [bb.xmax, bb.ymax, bb.zmax]],
        cylinder_radii_mm=sorted(
            face._geomAdaptor().Cylinder().Radius()
            for face in shape.Faces()
            if face.geomType() == "CYLINDER"
        ),
    )


def same_geometry(before, after):
    def values(row):
        return [
            row["volume_mm3"],
            *row["bounds_mm"][0],
            *row["bounds_mm"][1],
            *row["cylinder_radii_mm"],
        ]

    left, right = values(before), values(after)
    if (
        before["solids"] != after["solids"]
        or len(left) != len(right)
        or not all(
            math.isclose(a, b, abs_tol=1e-6, rel_tol=1e-7) for a, b in zip(left, right)
        )
    ):
        raise ValueError(
            "STEP round-trip bounds, cylinder radii, volume or solid count differ"
        )


def assembly_nodes(assembly):
    def visit(node, path):
        key = (*path, node.name)
        transform = node.loc.wrapped.Transformation()
        matrix = [transform.Value(i, j) for i in range(1, 4) for j in range(1, 5)]
        yield (
            key,
            (matrix, measures(cq_shape(node.obj)) if node.obj is not None else None),
        )
        for child in node.children:
            yield from visit(child, key)

    return dict(visit(assembly, ()))


def export_model(model, path, cq):
    if isinstance(model, cq.Assembly):
        before = assembly_nodes(model)
        model.export(str(path), exportType="STEP", mode="default")
        after = assembly_nodes(cq.Assembly.load(str(path), importType="STEP"))
        if before.keys() != after.keys():
            raise ValueError("STEP assembly hierarchy or labels differ")
        for key, (matrix, geometry) in before.items():
            observed, solid = after[key]
            if not all(
                math.isclose(a, b, abs_tol=1e-7) for a, b in zip(matrix, observed)
            ):
                raise ValueError(f"Assembly placement changed at {key}")
            if (geometry is None) != (solid is None):
                raise ValueError(f"Assembly shape ownership changed at {key}")
            if geometry is not None:
                same_geometry(geometry, solid)
        return dict(assembly_paths=[list(key) for key in after], placements="PASS")
    shape = cq_shape(model)
    original = measures(shape)
    cq.exporters.export(shape, str(path))
    checks = measures(cq_shape(cq.importers.importStep(str(path))))
    same_geometry(original, checks)
    return checks


def convert(
    mode, source, destination, *, trusted=False, analytic=False, dependencies=()
):
    source, destination = Path(source).resolve(), Path(destination).absolute()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Destination already exists: {destination}")
    extensions = {
        "scad-stl": ((".scad",), ".stl"),
        "scad-python": ((".scad",), ".py"),
        "python-step": ((".py",), ".step"),
        "step-stl": ((".step", ".stp"), ".stl"),
    }
    src_ext, dest_ext = extensions[mode]
    if source.suffix.lower() not in src_ext or destination.suffix.lower() not in (
        (".step", ".stp") if dest_ext == ".step" else (dest_ext,)
    ):
        raise ValueError("File extensions disagree with the selected route")
    if analytic and mode != "scad-python":
        raise ValueError("Analytic cylinders apply only to SCAD source translation")
    if mode in ("scad-stl", "python-step") and not trusted:
        raise ValueError(
            "Review the generator and its dependencies, then pass --trusted-source"
        )
    dependencies = [Path(p).resolve() for p in dependencies]
    pins = {p: sha(p) for p in dependencies}
    initial = sha(source)
    with tempfile.TemporaryDirectory(dir=destination.parent) as folder:
        out = Path(folder) / ("derivative" + dest_ext)
        if mode == "scad-python":
            program = translate(source.read_text(), source.name, analytic)
            compile(program, source.name, "exec")
            out.write_text(program)
            checks = dict(
                python_syntax="PASS", cylinders="analytic" if analytic else "polygonal"
            )
            version = "bounded SCAD grammar 1"
        elif mode == "scad-stl":
            version = subprocess.run(
                ["openscad", "--version"], capture_output=True, text=True, check=True
            )
            version = (version.stdout + version.stderr).strip()
            subprocess.run(
                [
                    "openscad",
                    "--hardwarnings",
                    "--export-format",
                    "asciistl",
                    "-o",
                    out,
                    source,
                ],
                check=True,
            )
            checks = inspect_stl(out)
        else:
            import cadquery as cq

            version = cq.__version__
            if mode == "python-step":
                original_path = sys.path[:]
                try:
                    sys.path.insert(0, str(source.parent))
                    module = runpy.run_path(str(source))
                finally:
                    sys.path[:] = original_path
                checks = export_model(module.get("model"), out, cq)
            else:
                shape = cq_shape(cq.importers.importStep(str(source)))
                original = measures(shape)
                if not shape.exportStl(
                    str(out), tolerance=0.01, angularTolerance=0.1, ascii=True
                ):
                    raise ValueError("STL writer failed")
                checks = inspect_stl(out)
                checks["input_geometry"] = original
                if not math.isclose(
                    original["volume_mm3"], checks["signed_volume_mm3"], rel_tol=0.01
                ):
                    raise ValueError("Mesh volume differs from input by more than 1%")
        if sha(source) != initial or any(sha(p) != value for p, value in pins.items()):
            raise ValueError("Source changed during conversion")
        result = dict(
            route=mode,
            source_sha256=initial,
            dependencies=[
                {"name": p.name, "sha256": value} for p, value in pins.items()
            ],
            output_sha256=sha(out),
            tool_version=version,
            units="mm convention",
            checks=checks,
        )
        os.link(out, destination)  # Atomic no-replace publication on this filesystem.
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "route", choices=("scad-stl", "scad-python", "python-step", "step-stl")
    )
    parser.add_argument("source")
    parser.add_argument("output")
    parser.add_argument(
        "--dependency",
        type=Path,
        action="append",
        default=[],
        help="Pin a reviewed input dependency; repeat for each file",
    )
    parser.add_argument("--trusted-source", action="store_true")
    parser.add_argument("--analytic-cylinders", action="store_true")
    args = parser.parse_args()
    try:
        print(
            json.dumps(
                convert(
                    args.route,
                    args.source,
                    args.output,
                    trusted=args.trusted_source,
                    analytic=args.analytic_cylinders,
                    dependencies=args.dependency,
                ),
                indent=2,
                allow_nan=False,
            )
        )
    except (
        KeyError,
        OSError,
        ValueError,
        ImportError,
        subprocess.SubprocessError,
    ) as exc:
        parser.exit(1, f"Conversion failed: {exc}\n")
