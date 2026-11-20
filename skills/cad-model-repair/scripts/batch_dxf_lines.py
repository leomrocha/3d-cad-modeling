"""Apply reviewed DXF LINE lengths to a new drawing, preserving each selected start and direction."""
import hashlib
import json
import math
import ctypes
import os
import sys
import tempfile
from pathlib import Path
from uuid import uuid4

from batch_request import execution_rows
from operation_catalogue import file_digest

INPUT = "DXF LINE"
OUTPUT = "line length from fixed start"
METHOD = "resize-line"
REFERENCE = "fixed LINE start"
UNIT_CODES = {"in": 1, "ft": 2, "mm": 4, "cm": 5, "m": 6}


def backend():
    import ezdxf
    return "ezdxf/" + ezdxf.__version__


def drawing(path, unit):
    import ezdxf
    doc = ezdxf.readfile(path)
    if doc.units not in (0, UNIT_CODES[unit]):
        raise ValueError("DXF declared unit differs from request model unit")
    return doc


def line(doc, handle):
    entity = doc.entitydb.get(handle)
    if entity is None or entity.dxftype() != "LINE" or entity.dxf.owner != doc.modelspace().block_record_handle:
        raise ValueError(f"Expected a modelspace LINE at {handle}")
    return entity


def measured(entity):
    return entity.dxf.start, entity.dxf.end, (entity.dxf.end - entity.dxf.start).magnitude


def unselected_lines(doc, selected):
    return {e.dxf.handle: (e.dxf.owner, e.dxf.start, e.dxf.end, e.dxf.thickness, e.dxf.extrusion)
            for e in doc.entitydb.values() if e.dxftype() == "LINE" and e.dxf.handle not in selected}


def verify_sample(source, result, receipt, expected, *, require_change=True):
    if (receipt["backend"], receipt["action"], receipt["input"], receipt["output"], receipt["name"]) != (
            backend(), "modify", INPUT, OUTPUT, METHOD):
        raise ValueError("DXF operation identity differs from installed backend")
    unit = receipt["unit"]
    before = drawing(source, unit)
    after = drawing(result, unit)
    if unselected_lines(before, expected) != unselected_lines(after, expected):
        raise ValueError("Unselected LINE geometry changed")
    changed = False
    for target, props in expected.items():
        start, end, original = measured(line(before, target))
        new_start, new_end, actual = measured(line(after, target))
        length = props["length"]
        if type(length) not in (int, float) or not (0 < length < math.inf) or original <= 0:
            raise ValueError(f"Expected positive LINE lengths for {target}")
        if list(start) != props["start"] or start != new_start:
            raise ValueError(f"LINE start differs for {target}")
        if not math.isclose(actual, length, rel_tol=1e-12, abs_tol=1e-10):
            raise ValueError(f"LINE length differs for {target}")
        destination = start + (end - start).normalize(length)
        if (new_end - destination).magnitude > 1e-10 + 1e-12 * length:
            raise ValueError(f"LINE endpoint differs for {target}")
        changed |= not math.isclose(original, length, rel_tol=1e-12, abs_tol=1e-10)
    if require_change and not changed:
        raise ValueError("Qualification must demonstrate a measured LINE length change")


def publish_directory(staged, destination):
    """Publish on the supported platforms without replacing even an empty directory."""
    libc = ctypes.CDLL(None, use_errno=True)
    old, new = os.fsencode(staged), os.fsencode(destination)
    if sys.platform.startswith("linux") and hasattr(libc, "renameat2"):
        # AT_FDCWD, RENAME_NOREPLACE
        status = libc.renameat2(-100, old, -100, new, 1)
    elif sys.platform == "darwin" and hasattr(libc, "renamex_np"):
        # RENAME_EXCL
        status = libc.renamex_np(old, new, 4)
    else:
        raise OSError("Atomic no-replace directory rename is unavailable")
    if status:
        error = ctypes.get_errno()
        raise OSError(error, os.strerror(error), str(destination))


def apply(preview, directory, *, resource, catalogue_path=None, sample=False):
    """Create a new job directory. Sample mode qualifies the writer on a separate owned output."""
    data = preview.read()
    if (data["action"], data["entity"], data["output"]) != ("modify", INPUT, OUTPUT):
        raise ValueError("This operation modifies DXF LINE lengths from their fixed start")
    source = Path(data["model"]).resolve()
    if file_digest(source) != data["revision"]:
        raise ValueError("Source revision changed")
    unit = data["model_unit"]
    doc = drawing(source, unit)
    from batch_dxf_inventory import read_inventory
    if sample:
        rows = data["rows"]
        if any("selection" in row for row in rows):
            from batch_selection import verify_reopened
            paths = verify_reopened(preview, read_inventory(data["model"], unit))
            for row, path in zip(rows, paths):
                row["target"] = "/".join(path)
    else:
        if not any(route.get("backend") == backend() and route["name"] == METHOD and route["resource"] == resource
                   for route in data["routes"]):
            raise ValueError("No matching DXF operation with verified readback for this backend")
        rows = execution_rows(preview, resource, METHOD, catalogue_path=catalogue_path,
                              read_revision=file_digest, read_inventory=read_inventory)
    expected = {}
    for row in rows:
        handle = row["target"]
        if row["reference"] != REFERENCE:
            raise ValueError(f"DXF LINE {handle} requires reference {REFERENCE!r}")
        entity = line(doc, handle)
        start, end, current = measured(entity)
        old, new = row["current"], row["requested"]
        if old.get("unit") != unit or new.get("unit") != unit:
            raise ValueError(f"Specify a length for {handle}")
        if not math.isclose(current, old["value"], rel_tol=1e-12, abs_tol=1e-10):
            raise ValueError(f"Starting LINE length changed for {handle}")
        length = new["value"]
        if length <= 0 or current <= 0:
            raise ValueError(f"Specify positive LINE lengths for {handle}")
        expected[handle] = {"start": list(start), "length": length}
        entity.dxf.end = start + (end - start).normalize(length)
    if file_digest(source) != data["revision"]:
        raise ValueError("Source revision changed during preparation")
    directory = Path(directory).absolute()
    with tempfile.TemporaryDirectory(dir=directory.parent, prefix=".batch-lines-") as temp:
        staged = Path(temp) / "job"
        staged.mkdir()
        save_result(doc, staged, source, data["revision"], unit, resource, expected, sample, hashlib.sha256(preview.document.encode()).hexdigest())
        publish_directory(staged, directory)
    return directory / "evidence.json"


def save_result(doc, directory, source, source_revision, unit, resource, expected, sample, preview_sha256):
    result = directory / "result.dxf"
    doc.saveas(result)
    context = dict(resource=resource, name=METHOD, input=INPUT, output=OUTPUT, action="modify",
                   backend=backend(), status="completed", operation_id=uuid4().hex,
                   result=result.name, result_sha256=file_digest(result))
    writer = dict(**context, preview_sha256=preview_sha256, source=str(source), source_sha256=source_revision, unit=unit, expected=expected)
    reopened = drawing(result, unit)
    observed = {}
    for handle, properties in expected.items():
        start, _, length = measured(line(reopened, handle))
        # Length comparison uses the stated tolerance, retaining the raw measured value.
        observed[handle] = {"start": list(start), "length": length}
    reader = dict(**context, readback_id=uuid4().hex, observed=observed)
    verify_sample(source, result, writer, expected, require_change=sample)
    if file_digest(source) != source_revision:
        raise ValueError("Source revision changed during verification")
    evidence = {}
    for name, record in (("operation", writer), ("readback", reader)):
        path = directory / (name + ".json")
        path.write_text(json.dumps(record, allow_nan=False, indent=2) + "\n")
        evidence[name] = path.name
        evidence[name + "_sha256"] = file_digest(path)
    path = directory / "evidence.json"
    path.write_text(json.dumps(evidence, indent=2) + "\n")


def main():
    import argparse
    from batch_request import Preview
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["sample", "execute"])
    parser.add_argument("preview", type=Path)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--preview-sha256", required=True)
    parser.add_argument("--resource", required=True)
    parser.add_argument("--catalogue", type=Path)
    args = parser.parse_args()
    if args.mode == "execute" and args.catalogue is None:
        parser.error("execute requires --catalogue")
    try:
        import hashlib
        payload = args.preview.read_bytes()
        if hashlib.sha256(payload).hexdigest() != args.preview_sha256:
            raise ValueError("Reviewed preview digest differs")
        evidence = apply(Preview(payload.decode()), args.directory, resource=args.resource,
                         catalogue_path=args.catalogue, sample=args.mode == "sample")
        print(evidence)
    except (OSError, TypeError, KeyError, ValueError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
