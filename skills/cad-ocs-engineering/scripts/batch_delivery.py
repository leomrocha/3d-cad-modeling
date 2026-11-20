"""Route a reviewed batch to locally qualified CAD methods and report its saved result."""

import argparse
import json
import math
from pathlib import Path
from batch_request import Preview
import sys
import hashlib
from batch_sample_readback import target_ids, measured_ids, verify_native
import subprocess

from operation_catalogue import file_digest, load, read


# Each tuple identifies the action, native input and saved result the writer verifies.
CONTRACTS = {
    "circle": ("create", "planar positions", "DXF circles"),
    "cut": ("create", "solid host", "STEP cylindrical cuts"),
    "occurrence": ("create", "catalogue part", "XCAF shared occurrences"),
    "bar length": ("modify", "rectangular XCAF bar", "anchored bar length"),
    "bore diameter": ("modify", "reviewed cylindrical bore", "anchored bore diameter"),
    "occurrence name": ("modify", "XCAF occurrence", "occurrence name"),
    "replace occurrence": (
        "replace",
        "keyed XCAF occurrence",
        "seated catalogue occurrence",
    ),
}


def writer(operation):
    if CONTRACTS[operation][0] == "create":
        from batch_creation import execute
    else:
        from batch_modification import execute
    return execute


def provider(operation):
    from importlib.metadata import version

    package = "ezdxf" if operation == "circle" else "cadquery"
    return f"{package}/{version(package)}"


def verify_job_sample(row, resource, sample, *, replay):
    """Bind a local writer's published sample to its original contract and measured results."""
    method = next(m for m in resource["methods"] if m["name"] == row["name"])
    request = Path(method["sample_request"]).resolve()
    operation = read(request)["operation"]
    if (
        Path(resource["location"]).resolve()
        != Path(writer(operation).__code__.co_filename).resolve()
    ):
        raise ValueError("Catalogue resource differs from the installed batch writer")
    if CONTRACTS[operation] != (row["action"], row["input"], row["output"]):
        raise ValueError("Sample operation differs from the catalogue method")
    if resource["backend"] != provider(operation):
        raise ValueError("Installed sample backend differs")
    if sample.name != "manifest.json" or not sample.is_file():
        raise ValueError("Specify the published batch sample manifest")
    spec = read(request)
    source = (request.parent / spec["model"]).resolve()
    job = sample.parent
    manifest = read(sample)
    suffix = {"circle": "dxf", "cut": "step", "bore diameter": "step"}.get(
        operation, "xbf"
    )
    result = job / ("result." + suffix)
    if set(manifest) != {"request.json", "readback.json", result.name} or any(
        file_digest(job / name) != digest for name, digest in manifest.items()
    ):
        raise ValueError("Sample manifest differs from its saved artifacts")
    receipt = read(job / "readback.json")
    if (
        file_digest(request) != manifest["request.json"]
        or receipt["request_sha256"] != manifest["request.json"]
        or receipt["source_sha256"] != spec["revision"]
        or file_digest(source) != spec["revision"]
        or receipt["result_sha256"] != manifest[result.name]
        or receipt["operation"] != operation
    ):
        raise ValueError("Sample request, source or result changed")
    verify_native(spec, request.parent, source, result, receipt["elements"])
    return file_digest(sample)


def measure_row(spec, doc, *, planned):
    """Project straight-edged occurrences on a measured modelspace LINE."""
    from batch_dxf_frames import TOL, resolve_frame
    from step_placements import apply, dot, unit

    check = spec["row_check"]
    edge = doc.entitydb[check["line"]]
    if (
        edge.dxftype() != "LINE"
        or edge.dxf.get("thickness", 0)
        or edge.dxf.owner != doc.modelspace().block_record_handle
    ):
        raise ValueError("Row reference must be a modelspace LINE")
    start, end = edge.dxf.start, edge.dxf.end
    axis = unit(list(end - start))

    def station(point):
        return dot(axis, [v - o for v, o in zip(point, start)])

    intervals = []
    stations = []
    for row in sorted(spec["rows"], key=lambda r: r["position_index"]):
        insert, _, matrix = resolve_frame(doc, row["target"])
        if planned:
            matrix = row["requested"]["world_frame"]
        stations.append(station([line[3] for line in matrix[:3]]))
        block = doc.blocks[insert.dxf.name]
        limits = []
        for entity in block:
            if entity.dxftype() == "LINE" and not entity.dxf.get("thickness", 0):
                points = (entity.dxf.start, entity.dxf.end)
            elif (
                entity.dxftype() == "LWPOLYLINE"
                and not entity.has_arc
                and not entity.has_width
                and not entity.dxf.get("thickness", 0)
            ):
                points = entity.vertices_in_wcs()
            else:
                raise ValueError(
                    "Row edge offsets require straight LINE or zero-width polyline geometry"
                )
            for point in points:
                limits.append(
                    station(apply(matrix, point - block.block.dxf.base_point))
                )
        if not limits:
            raise ValueError("Empty bar definition")
        intervals.append((min(limits), max(limits)))
    measured = dict(
        first_offset=intervals[0][0],
        last_offset=station(end) - intervals[-1][1],
        pitches=[b - a for a, b in zip(stations, stations[1:])],
        clear_gaps=[b[0] - a[1] for a, b in zip(intervals, intervals[1:])],
    )
    for key in ("first_offset", "last_offset", "pitches", "clear_gaps"):
        if key not in check:
            continue
        expected, actual = check[key], measured[key]
        if key in ("first_offset", "last_offset"):
            expected, actual = [expected], [actual]
        if len(actual) != len(expected) or any(
            not math.isclose(x, y, abs_tol=TOL, rel_tol=0)
            for x, y in zip(actual, expected)
        ):
            raise ValueError(f"Row {key}: measured {actual}, requested {expected}")
    return measured


def place_existing(
    preview, spec, targets, row, resource, directory, catalogue, report, entry
):
    from batch_dxf_frames import METHOD
    from batch_dxf_placement import resume, start

    if row["name"] != METHOD or row not in spec["routes"]:
        raise ValueError("No reviewed individual occurrence move adapter")
    if "row_check" in spec:
        from batch_dxf_lines import drawing

        measure_row(spec, drawing(spec["model"], spec["model_unit"]), planned=True)
    if directory.exists():
        plan = read(directory / "plan.json")
        if (
            plan.get("row_check") != spec.get("row_check")
            or plan["unit"] != spec["model_unit"]
            or plan["resource"] != resource["id"]
            or plan["source_sha256"] != spec["revision"]
            or plan["source"] != str(Path(spec["model"]).resolve())
            or set(plan["expected"]) != set(targets)
            or plan["sample"]
            or any(
                plan["expected"][r["target"]]["world_frame"]
                != r["requested"]["world_frame"]
                or plan["expected"][r["target"]]["before"]
                != r["current"]["world_frame"]
                or plan["expected"][r["target"]]["reference"] != r["reference"]
                or plan["expected"][r["target"]]["position_id"] != r["position_id"]
                or plan["expected"][r["target"]]["position_index"]
                != r["position_index"]
                for r in spec["rows"]
            )
        ):
            raise ValueError("Existing placement job differs from the reviewed targets")
    else:
        start(preview, directory, resource["id"], catalogue)
    results = resume(directory)
    if set(results) != set(targets):
        raise ValueError("Placement result identities differ from the reviewed targets")
    if "row_check" in spec and all(
        r["status"] == "completed" for r in results.values()
    ):
        report["row_measurements"] = measure_row(
            spec, drawing(directory / "result.dxf", spec["model_unit"]), planned=False
        )
    report["readback"] = (
        read(directory / "readback.json")
        if (directory / "readback.json").is_file()
        else None
    )
    report["completed"] = [k for k, v in results.items() if v["status"] == "completed"]
    report["remaining"] = [k for k in targets if k not in report["completed"]]
    if report["remaining"]:
        entry["results"] = results
        raise ValueError(
            "Inspect the recorded move effects and resume the owned drawing"
        )


def deliver(request, catalogue, directory, *, request_sha256=None):
    payload = request.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if request_sha256 is not None and digest != request_sha256:
        raise ValueError("Reviewed request digest differs")
    preview = Preview(payload.decode())
    spec = preview.read()
    data = load(catalogue)
    placement = spec.get("action") == "place"
    targets = target_ids(spec)
    if "rows" in spec:
        contract = (spec["action"], spec["entity"], spec["output"])
    else:
        operation = spec["operation"]
        contract = CONTRACTS[operation]
    attempts = []
    report = dict(attempts=attempts, completed=[], remaining=targets)
    # Registration order breaks ties within the user's reuse preference.
    order = {"unchanged": 0, "parameter": 1, "script": 2, "guided": 3}
    resources = {resource["id"]: resource for resource in data["resources"]}

    def priority(row):
        definitions = resources[row["resource"]].get("methods", [])
        method = next((m for m in definitions if m["name"] == row["name"]), {})
        return order.get(method.get("reuse", "script"), len(order))

    candidates = sorted(data["operations"], key=priority)
    if placement and directory.exists():
        owner = read(directory / "plan.json")["resource"]
        candidates = [row for row in candidates if row["resource"] == owner]
        if not candidates:
            report["blocker"] = (
                f"Existing placement job needs its owning resource {owner}"
            )
            return report
    for row in candidates:
        if (row.get("action"), row["input"], row["output"]) != contract:
            continue
        entry = dict(resource=row["resource"], method=row["name"])
        attempts.append(entry)
        owns_result = False
        try:
            if spec.get("relationship", "individual") != "individual":
                raise ValueError("An editable native pattern provider is required")
            if not row.get("usable") or not row.get("readback_verified"):
                raise ValueError(row.get("reason", "Method lacks a verified sample"))
            resource = next(r for r in data["resources"] if r["id"] == row["resource"])
            method = next(m for m in resource["methods"] if m["name"] == row["name"])
            if placement:
                owns_result = True
                place_existing(
                    preview,
                    spec,
                    targets,
                    row,
                    resource,
                    directory,
                    catalogue,
                    report,
                    entry,
                )
            elif spec.get("action") == "modify" and "rows" in spec:
                from batch_dxf_lines import (
                    apply as resize_lines,
                    METHOD as resize_method,
                )

                if row["name"] != resize_method or row not in spec["routes"]:
                    raise ValueError("No reviewed DXF line-length adapter")
                owns_result = True
                if directory.exists():
                    from operation_catalogue import verify_receipts

                    evidence = read(directory / "evidence.json")
                    if (
                        evidence.get("operation") != "operation.json"
                        or evidence.get("readback") != "readback.json"
                    ):
                        raise ValueError(
                            "Published LINE receipts must name this job's files"
                        )
                    prior = read(directory / "operation.json")
                    if (
                        prior.get("preview_sha256") != digest
                        or prior["result"] != "result.dxf"
                        or prior["source_sha256"] != spec["revision"]
                        or Path(prior["source"]).resolve()
                        != Path(spec["model"]).resolve()
                        or prior["unit"] != spec["model_unit"]
                        or set(prior["expected"]) != set(targets)
                    ):
                        raise ValueError(
                            "Published LINE operation differs from the reviewed request"
                        )
                    verify_receipts(
                        row, resource, directory / "evidence.json", require_change=False
                    )
                else:
                    resize_lines(
                        preview,
                        directory,
                        resource=resource["id"],
                        catalogue_path=catalogue,
                    )
                report.update(
                    completed=targets,
                    remaining=[],
                    readback=read(directory / "readback.json"),
                )
            else:
                if not method.get("sample_request") or "operation" not in spec:
                    raise ValueError("No installed adapter for this method")
                if read(Path(method["sample_request"]))["operation"] != operation:
                    raise ValueError("Sample uses a different writer")
                digest = verify_job_sample(
                    row, resource, Path(row["readback_file"]), replay=False
                )
                if digest != row["evidence_sha256"]:
                    raise ValueError("Qualification changed")
                owns_result = True
                receipt = writer(operation)(request, directory, reviewed_bytes=payload)
                if set(measured_ids(receipt["elements"])) != set(targets):
                    raise ValueError(
                        "Readback target IDs differ from the reviewed targets"
                    )
                report.update(completed=targets, remaining=[], readback=receipt)
            entry["outcome"] = "completed"
            return report
        except (
            OSError,
            ValueError,
            KeyError,
            TypeError,
            ImportError,
            RuntimeError,
            subprocess.SubprocessError,
        ) as exc:
            entry["outcome"] = str(exc)
            if owns_result and directory.exists():
                break  # Preserve the published job for reconciliation by its owning writer.
    report["blocker"] = (
        attempts[-1]["outcome"]
        if attempts
        else "No catalogue method matches " + ", ".join(contract)
    )
    return report


if __name__ == "__main__":
    if sys.argv[1:] == ["verify-sample"]:
        try:
            row, resource, path = json.load(sys.stdin)
            print(
                json.dumps(
                    {
                        "sha256": verify_job_sample(
                            row, resource, Path(path), replay=False
                        )
                    }
                )
            )
        except (
            KeyError,
            ValueError,
            TypeError,
            OSError,
            ImportError,
            RuntimeError,
        ) as error:
            sys.exit(str(error))
        sys.exit(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--catalogue", required=True, type=Path)
    parser.add_argument("--request-sha256", required=True)
    args = parser.parse_args()
    try:
        result = deliver(
            args.request,
            args.catalogue,
            args.directory,
            request_sha256=args.request_sha256,
        )
    except (KeyError, ValueError, TypeError, OSError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(2 if "blocker" in result or result["remaining"] else 0)
