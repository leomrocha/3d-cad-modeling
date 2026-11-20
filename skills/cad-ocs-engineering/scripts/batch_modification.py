"""Modify reviewed dimensions of existing STEP bores or XCAF bar occurrences."""

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path
import tempfile

from batch_creation import TOL, load_solid, measure_cut, required_number
from batch_dxf_lines import publish_directory
from batch_dxf_placement import sync_path
from batch_request import prepare
from operation_catalogue import file_digest, read


def reviewed_values(spec, targets, field):
    rows = prepare(
        dict(
            model=spec["model"],
            revision=spec["revision"],
            action="modify",
            entity=spec["operation"],
            output="saved solid geometry",
            model_unit="mm",
            targets=targets,
            **{k: spec[k] for k in ("value", "values") if k in spec},
        ),
        {"operations": []},
    ).read()["rows"]
    return {
        row["target"]: required_number(row["requested"][field]["value"]) for row in rows
    }


def dimension_target(key, anchor, field, number):
    return dict(
        id=key, reference=anchor, current={field: dict(value=number, unit="mm")}
    )


def solid_difference(a, b):
    """Symmetric material difference in cubic millimetres."""
    return a.cut(b).Volume() + b.cut(a).Volume()


def modify_bores(spec, output):
    import cadquery as cq

    source = load_solid(spec["model"])
    shape = source
    targets, checked = [], []
    for bore in spec["targets"]:
        key = bore["id"]
        if bore["anchor"] != "entry centre" or bore["end"] not in ("through", "blind"):
            raise ValueError(
                "Select a blind or through bore and its fixed entry centre"
            )
        axis = cq.Vector(*bore["direction"])
        if not math.isclose(axis.Length, 1, abs_tol=TOL):
            raise ValueError("The inward bore direction must be a unit vector")
        axis = axis.normalized()
        row = dict(
            id=key,
            xyz=bore["entry"],
            value=dict(
                diameter=required_number(bore["diameter"]),
                depth=required_number(bore["depth"]),
                end=bore["end"],
            ),
        )
        before = measure_cut(source, row, axis)
        if any(
            math.dist(before["entry"], other[2]["entry"]) < TOL for other in checked
        ):
            raise ValueError("Duplicate bore entry")
        checked.append((row, axis, before))
        targets.append(
            dimension_target(key, bore["anchor"], "diameter", before["diameter"])
        )
    values = reviewed_values(spec, targets, "diameter")
    for row, axis, before in checked:
        diameter = values[row["id"]]
        old = before["diameter"]
        depth = before["depth"]
        if diameter < old:
            raise ValueError(
                "Use the native feature or a qualified face-offset provider for bore reduction"
            )
        if diameter > old:
            cutter = cq.Solid.makeCylinder(
                diameter / 2, depth, cq.Vector(*before["entry"]), axis
            )
            modified = shape.cut(cutter)
            removed = math.pi * (diameter**2 - old**2) * depth / 4
            if (
                len(modified.Solids()) != 1
                or not modified.isValid()
                or not math.isclose(
                    shape.Volume() - modified.Volume(),
                    removed,
                    rel_tol=1e-7,
                    abs_tol=1e-9,
                )
            ):
                raise ValueError(
                    "Requested bore crosses another feature or host boundary"
                )
            shape = modified.Solids()[0]
        row["value"]["diameter"] = diameter
    cq.exporters.export(shape, str(output))
    saved = load_solid(output)
    if solid_difference(saved, shape) > TOL:
        raise ValueError("Reopened host material differs from the reviewed cuts")
    return [
        dict(before=before, after=measure_cut(saved, row, axis), anchor="entry centre")
        for row, axis, before in checked
    ]


def execute(request, directory):
    request_bytes = request.read_bytes()
    contract = sha256(request_bytes).hexdigest()
    spec = json.loads(request_bytes)
    source = (request.parent / spec["model"]).resolve()
    spec["model"] = str(source)
    if spec["unit"] != "mm" or file_digest(source) != spec["revision"]:
        raise ValueError("Expected millimetres and the reviewed source revision")
    if spec["operation"] == "bore diameter":
        suffix, writer = "step", modify_bores
    elif spec["operation"] == "bar length":
        from batch_xcaf_bars import modify_bars

        suffix, writer = "xbf", modify_bars
    elif spec["operation"] == "occurrence name":
        from batch_xcaf_bars import rename_occurrences

        suffix, writer = "xbf", rename_occurrences
    else:
        raise ValueError("Use the native provider for this property or constraint")
    name = "result." + suffix
    files = ("request.json", name, "readback.json")
    if directory.exists():
        if (
            read(directory / "manifest.json")
            != {k: file_digest(directory / k) for k in files}
            or (directory / "request.json").read_bytes() != request_bytes
        ):
            raise ValueError("Published result, readback or request differs")
        sync_path(directory.parent)
        return read(directory / "readback.json")
    with tempfile.TemporaryDirectory(dir=directory.parent) as tmp:
        job = Path(tmp) / "job"
        job.mkdir()
        result = writer(spec, job / name)
        if file_digest(request) != contract or file_digest(source) != spec["revision"]:
            raise ValueError("Request or source changed during modification")
        receipt = dict(
            operation=spec["operation"],
            unit="mm",
            request_sha256=contract,
            source_sha256=spec["revision"],
            result_sha256=file_digest(job / name),
            elements=result,
        )
        (job / "request.json").write_bytes(request_bytes)
        (job / "readback.json").write_text(
            json.dumps(receipt, indent=2, allow_nan=False)
        )
        (job / "manifest.json").write_text(
            json.dumps({k: file_digest(job / k) for k in files}, indent=2)
        )
        for filename in (*files, "manifest.json"):
            sync_path(job / filename)
        sync_path(job)
        sync_path(job.parent)
        publish_directory(job, directory)
        sync_path(directory.parent)
        sync_path(job.parent)
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
        TypeError,
        ValueError,
        RuntimeError,
    ) as error:
        parser.exit(2, f"{error}\n")
