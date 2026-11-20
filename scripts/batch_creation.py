"""Create a reviewed pattern of circles, solid cuts or shared component occurrences."""

import argparse
from collections import defaultdict
from itertools import product
import json
import math
from pathlib import Path
import subprocess
import tempfile

from batch_dxf_lines import publish_directory
from batch_request import prepare
from cadtools.runtime import CadError
from catalogue_candidates import lookup
from operation_catalogue import file_digest, read
from hashlib import sha256
from planar_positions import generate
from spatial_positions import frame
from step_placements import cross

TOL = 1e-6  # millimetres for solid results; drawing units for DXF readback


def required_number(value):
    if type(value) not in (float, int) or not math.isfinite(value) or value <= 0:
        raise ValueError("Expected a positive finite dimension")
    return value


def patterns(spec):
    if spec["relationship"] != "individual":
        raise ValueError(
            "Select a native pattern provider to retain driving relationships"
        )
    pattern = spec["pattern"]
    positions = generate(pattern)
    rows = positions["positions"]
    if not rows or len({tuple(r["xyz"]) for r in rows}) != len(rows):
        raise ValueError("Expected distinct, nonempty positions")
    plane = positions["frame"]
    normal = cross(plane["x"], plane["y"])
    for row in rows:
        row["matrix"] = frame(row["xyz"], normal, row.get("direction_xyz", plane["x"]))
    return positions, rows, normal


def check_centre(spec, centre, row):
    if math.dist(centre, row["xyz"]) > TOL:
        raise ValueError(f"Reopened centre differs at {row['id']}")
    pattern = spec["pattern"]
    if pattern["kind"] != "circle":
        return {}
    plane = pattern["frame"]
    origin = [
        o + a * pattern["centre"][0] + b * pattern["centre"][1]
        for o, a, b in zip(plane["origin"], plane["x"], plane["y"])
    ]
    radial = math.dist(centre, origin)
    if abs(radial - pattern["radius"]) > TOL:
        raise ValueError(f"Pitch radius differs at {row['id']}")
    return {"axis_reference": pattern["reference"], "pitch_radius": radial}


def circles(spec, rows, normal, path):
    from ezdxf.math import OCS
    from batch_dxf_frames import check_document
    from batch_dxf_lines import drawing
    from batch_insert_recovery import baseline

    unit = spec["pattern"]["unit"]
    doc = drawing(spec["model"], unit)
    check_document(doc, unit, doc.dxfversion)
    before = baseline(doc)
    retained_groups = {g.dxf.handle: list(g.handles()) for _, g in doc.groups}
    if doc.layers.get("0").is_locked():
        raise ValueError("Creation layer 0 is locked")
    group = doc.groups.new()
    ocs = OCS(normal)
    entities = []
    # Only parallel circles can duplicate an element of this pattern. Index centre
    # and radius together so concentric circles with other radii stay independent.
    buckets = defaultdict(list)

    def cell(coordinates):
        return tuple(math.floor(value / TOL) for value in coordinates)

    for other in doc.modelspace().query("CIRCLE"):
        if abs(abs(other.dxf.extrusion.normalize().dot(normal)) - 1) <= TOL:
            centre = tuple(other.ocs().to_wcs(other.dxf.center))
            buckets[cell((*centre, other.dxf.radius))].append(
                (centre, other.dxf.radius)
            )
    comparisons = 0
    offsets = list(product((-1, 0, 1), repeat=4))
    for row in rows:
        radius = required_number(row["value"]["diameter"]) / 2
        centre = row["xyz"]
        key = cell((*centre, radius))
        for offset in offsets:
            bucket = buckets.get(tuple(i + j for i, j in zip(key, offset)), ())
            comparisons += len(bucket)
            if comparisons > 1_000_000:
                raise ValueError("Circle proximity comparison limit exceeded")
            if any(
                math.dist(centre, xyz) <= TOL and abs(radius - r) <= TOL
                for xyz, r in bucket
            ):
                raise ValueError(f"Circle already exists at {row['id']}")
        buckets[key].append((centre, radius))
        entities.append(
            doc.modelspace().add_circle(
                ocs.from_wcs(row["xyz"]), radius, dxfattribs={"extrusion": normal}
            )
        )
    group.set_data(entities)
    handles = [entity.dxf.handle for entity in entities]
    doc.saveas(path)
    saved = drawing(path, unit)
    if baseline(saved, handles) != before or set(
        saved.entitydb[group.dxf.handle].handles()
    ) != set(handles):
        raise ValueError("Saved circle group or retained drawing geometry differs")
    if any(
        list(saved.entitydb[h].handles()) != members
        for h, members in retained_groups.items()
    ):
        raise ValueError("Independent group membership changed")
    results = []
    for row, handle in zip(rows, handles):
        entity = saved.entitydb[handle]
        centre = list(entity.ocs().to_wcs(entity.dxf.center))
        diameter = 2 * entity.dxf.radius
        if (
            entity.dxftype() != "CIRCLE"
            or math.dist(entity.dxf.extrusion, normal) > TOL
            or abs(diameter - row["value"]["diameter"]) > TOL
        ):
            raise ValueError("Saved circle geometry differs")
        results.append(
            dict(
                id=row["id"],
                handle=handle,
                centre=centre,
                diameter=diameter,
                normal=normal,
                **check_centre(spec, centre, row),
            )
        )
    return results


def load_solid(path):
    import cadquery as cq

    if Path(path).suffix.lower() not in (".stp", ".step"):
        raise ValueError("This solid operation requires a STEP model")
    from OCP.IFSelect import IFSelect_RetDone
    from OCP.STEPControl import STEPControl_Reader

    reader = STEPControl_Reader()
    if reader.ReadFile(str(path)) != IFSelect_RetDone:
        raise ValueError("STEP file could not be loaded")
    reader.SetSystemLengthUnit(1.0)  # OCCT working coordinates in mm
    roots = reader.NbRootsForTransfer()
    if not roots or not all(reader.TransferRoot(i) for i in range(1, roots + 1)):
        raise ValueError("STEP root transfer incomplete")
    shapes = [cq.Shape.cast(reader.Shape(i)) for i in range(1, reader.NbShapes() + 1)]
    solids = []
    while shapes:
        shape = shapes.pop()
        if shape.ShapeType() == "Compound":
            children = list(shape)
            if not children:
                raise ValueError("STEP contains an independent empty compound")
            shapes.extend(children)
        elif shape.ShapeType() == "Solid" and shape.isValid():
            solids.append(shape)
        else:
            raise ValueError(
                "STEP contains independent geometry outside the selected solid"
            )
    if len(solids) != 1:
        raise ValueError("Select a STEP containing exactly one valid solid")
    return solids[0]


def check_rim(shape, ring, direction, floor):
    """Require the wall edge to bound the actual opening or complete end disk."""
    import cadquery as cq

    neighbours = [
        face
        for face in shape.Faces()
        if face.geomType() == "PLANE"
        and any(edge.isSame(ring) for edge in face.Edges())
    ]
    if len(neighbours) != 1 or neighbours[0].normalAt().dot(direction) < 1 - TOL:
        raise ValueError("Expected a planar host face incident to the bore rim")
    face = neighbours[0]
    wires = [face.outerWire()] if floor else face.innerWires()
    if not any(len(w.Edges()) == 1 and w.Edges()[0].isSame(ring) for w in wires):
        raise ValueError("Bore endpoint material or opening differs")
    disk = cq.Face.makeFromWires(cq.Wire.assembleEdges([ring]))
    area = disk.intersect(shape).Area()
    if floor:
        if face.innerWires() or not math.isclose(area, disk.Area(), rel_tol=1e-8):
            raise ValueError("Expected a complete flat blind-bore bottom")
    elif area > TOL**2:
        raise ValueError("The bore opening disk contains material")


def measure_cut(shape, row, axis):
    import cadquery as cq

    val = row["value"]
    start = cq.Vector(*row["xyz"])
    end = start + axis * val["depth"]
    found = []
    for face in shape.Faces():
        if face.geomType() != "CYLINDER":
            continue
        rings = [
            e
            for e in face.Edges()
            if e.geomType() == "CIRCLE"
            and e.IsClosed()
            and abs(2 * e.radius() - val["diameter"]) <= TOL
        ]
        if len(rings) != 2:
            continue
        rings.sort(key=lambda e: (e.arcCenter() - start).Length)
        a, b = [e.arcCenter() for e in rings]
        if (a - start).Length <= TOL and (b - end).Length <= TOL:
            found.append(rings)
    if len(found) != 1:
        raise ValueError(
            f"Expected one complete cylindrical wall and two edge circles at {row['id']}"
        )
    entry, ends = found[0]
    a, b, radius = entry.arcCenter(), ends.arcCenter(), entry.radius()
    check_rim(shape, entry, axis * -1, floor=False)
    blind = val["end"] == "blind"
    check_rim(shape, ends, axis * (-1 if blind else 1), floor=blind)
    return dict(
        id=row["id"],
        entry=list(a.toTuple()),
        diameter=2 * radius,
        depth=(b - a).Length,
        direction=list(axis.toTuple()),
        **{("bottom" if val["end"] == "blind" else "exit"): list(b.toTuple())},
    )


def cuts(spec, rows, normal, path):
    import cadquery as cq

    if spec["pattern"]["unit"] != "mm" or spec["direction"] not in (
        "+normal",
        "-normal",
    ):
        raise ValueError("Specify mm and the inward signed plane normal")
    shape = load_solid(spec["model"])
    axis = cq.Vector(*normal) * (1 if spec["direction"] == "+normal" else -1)
    for row in rows:
        v = row["value"]
        radius = required_number(v["diameter"]) / 2
        depth = required_number(v["depth"])
        if v["end"] not in ("blind", "through"):
            raise ValueError("Specify blind or through and the measured cut depth")
        start = cq.Vector(*row["xyz"])
        cutter = cq.Solid.makeCylinder(radius, depth, start, axis)
        result = shape.cut(cutter)
        expected = math.pi * radius**2 * depth
        if (
            not result.isValid()
            or len(result.Solids()) != 1
            or not math.isclose(
                shape.Volume() - result.Volume(), expected, rel_tol=1e-7, abs_tol=1e-9
            )
        ):
            raise ValueError(
                f"Cut crosses a boundary, void or previous feature at {row['id']}"
            )
        shape = result.Solids()[0]
    cq.exporters.export(shape, str(path))
    saved = load_solid(path)
    if not math.isclose(saved.Volume(), shape.Volume(), rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError("Reopened host volume differs")
    results = []
    for row in rows:
        measured = measure_cut(saved, row, axis)
        measured.update(check_centre(spec, measured["entry"], row))
        results.append(measured)
    return results


def selected_part(spec):
    part = spec["part"]
    data = Path(part["data"])
    hits = lookup(Path(part["search_cli"]), data, part["query"])["candidates"]
    candidates = [
        c for c in hits if c["id"] == part["id"] and c.get("sha256") == spec["revision"]
    ]
    if len(candidates) != 1:
        raise ValueError("Selected catalogue part or asset revision differs")
    source = data / candidates[0]["file"]
    if source.resolve() != Path(spec["model"]).resolve():
        raise ValueError("Selected model differs from the reviewed catalogue asset")
    return source


def occurrences(spec, rows, normal, path):
    import cadquery as cq
    from OCP.gp import gp_Trsf
    from OCP.TopLoc import TopLoc_Location

    if spec["pattern"]["unit"] != "mm":
        raise ValueError("Assembly positions require millimetres")
    part = load_solid(selected_part(spec))
    assembly = cq.Assembly(name="Pattern")
    for row in rows:
        transform = gp_Trsf()
        transform.SetValues(*(v for r in row["matrix"][:3] for v in r))
        assembly.add(part, name=row["id"], loc=cq.Location(TopLoc_Location(transform)))
    assembly.export(str(path))
    saved = cq.Assembly.load(str(path))
    by_name = {child.name: child for child in saved.children}
    if len(saved.children) != len(rows) or set(by_name) != {row["id"] for row in rows}:
        raise ValueError("Occurrence count or names differ")
    shared = saved.children[0].obj
    if (
        not shared.isValid()
        or len(shared.Solids()) != 1
        or not math.isclose(shared.Volume(), part.Volume(), rel_tol=1e-9)
    ):
        raise ValueError("Saved part geometry differs")
    results = []
    for row in rows:
        child = by_name[row["id"]]
        trsf = child.loc.wrapped.Transformation()
        actual = [[trsf.Value(i, j) for j in range(1, 5)] for i in range(1, 4)]
        if not shared.wrapped.IsPartner(child.obj.wrapped) or any(
            abs(a - b) > TOL
            for u, v in zip(actual, row["matrix"])
            for a, b in zip(u, v)
        ):
            raise ValueError(f"Occurrence definition or frame differs at {row['id']}")
        results.append(
            dict(
                id=row["id"],
                definition=spec["part"]["id"],
                frame=actual,
                **check_centre(spec, [r[3] for r in actual], row),
            )
        )
    return results


def execute(request, directory):
    request_bytes = request.read_bytes()
    contract = sha256(request_bytes).hexdigest()
    spec = json.loads(request_bytes)
    source = (request.parent / spec["model"]).resolve()
    spec["model"] = str(source)
    if spec["operation"] == "occurrence":
        for key in ("data", "search_cli"):
            spec["part"][key] = str((request.parent / spec["part"][key]).resolve())
    if file_digest(source) != spec["revision"]:
        raise ValueError("Source revision changed")
    positions, rows, normal = patterns(spec)
    kind = spec["operation"]
    writer, suffix = {
        "circle": (circles, "dxf"),
        "cut": (cuts, "step"),
        "occurrence": (occurrences, "xbf"),
    }[kind]
    request_values = {k: spec[k] for k in ("value", "values") if k in spec}
    if kind == "occurrence":
        if request_values:
            raise ValueError("Shared occurrences use the selected part definition")
        request_values = {"value": {"definition": spec["part"]["id"]}}
    reviewed = prepare(
        dict(
            model=str(source),
            revision=spec["revision"],
            action="create",
            entity=kind,
            output=suffix,
            model_unit=positions["unit"],
            targets=[dict(id=r["id"], reference=r["reference"]) for r in rows],
            **request_values,
        ),
        {"operations": []},
    ).read()
    fields = {
        "circle": {"diameter"},
        "cut": {"diameter", "end", "depth"},
        "occurrence": {"definition"},
    }[kind]
    for row, review in zip(rows, reviewed["rows"]):
        if set(review["requested"]) != fields:
            raise ValueError(f"Expected {sorted(fields)} at {row['id']}")
        row["value"] = dict(review["requested"])
        for field in fields & {"depth", "diameter"}:
            value = row["value"][field]
            if isinstance(value, dict):
                if value["unit"] != positions["unit"]:
                    raise ValueError(f"Expected a length for {field}")
                value = value["value"]
            row["value"][field] = required_number(value)
    name = "result." + suffix
    if directory.exists():
        manifest = read(directory / "manifest.json")
        if manifest != {
            filename: file_digest(directory / filename)
            for filename in ("request.json", name, "readback.json")
        }:
            raise ValueError("Published result or readback changed")
        receipt = read(directory / "readback.json")
        if (
            (directory / "request.json").read_bytes() != request_bytes
            or receipt["request_sha256"] != contract
            or receipt["result_sha256"] != file_digest(directory / name)
        ):
            raise ValueError("Existing result differs from this request")
        return receipt
    with tempfile.TemporaryDirectory(dir=directory.parent) as tmp:
        job = Path(tmp) / "job"
        job.mkdir()
        path = job / name
        result = writer(spec, rows, normal, path)
        if contract != file_digest(request) or spec["revision"] != file_digest(source):
            raise ValueError("Request or source changed during creation")
        receipt = dict(
            request_sha256=contract,
            source_sha256=spec["revision"],
            unit=positions["unit"],
            result_sha256=file_digest(path),
            operation=kind,
            reference=positions["reference"],
            elements=result,
        )
        (job / "readback.json").write_text(json.dumps(receipt, indent=2))
        (job / "request.json").write_bytes(request_bytes)
        manifest = {
            filename: file_digest(job / filename)
            for filename in ("request.json", name, "readback.json")
        }
        (job / "manifest.json").write_text(json.dumps(manifest, indent=2))
        publish_directory(job, directory)
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("job", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(execute(args.request, args.job), indent=2))
    except (
        ImportError,
        KeyError,
        OSError,
        subprocess.CalledProcessError,
        TypeError,
        ValueError,
        RuntimeError,
        CadError,
    ) as error:
        parser.exit(2, f"{error}\n")
