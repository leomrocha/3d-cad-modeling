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

from operation_catalogue import file_digest, load, read, provider_call, provider_python


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
    if "row_check" in spec:
        results = resume(
            directory, read_row=lambda doc: measure_row(spec, doc, planned=False)
        )
    else:
        results = resume(directory)
    if set(results) != set(targets):
        raise ValueError("Placement result identities differ from the reviewed targets")
    report["readback"] = (
        read(directory / "readback.json")
        if (directory / "readback.json").is_file()
        else None
    )
    if "row_check" in spec and report["readback"]:
        report["row_measurements"] = report["readback"]["row_measurements"]
    report["completed"] = [k for k, v in results.items() if v["status"] == "completed"]
    report["remaining"] = [k for k in targets if k not in report["completed"]]
    if report["remaining"]:
        entry["results"] = results
        raise ValueError(
            "Inspect the recorded move effects and resume the owned drawing"
        )


def provider_runner(resource, row, method):
    """Use the approved writer installation; standalone DXF packages share the same writer source."""
    here = Path(__file__).resolve()
    if "location" not in resource:
        return here
    location = Path(resource["location"])
    if method.get("sample_request"):
        filename = (
            "batch_creation.py"
            if row["action"] == "create"
            else "batch_modification.py"
        )
    elif row["action"] == "place":
        filename = "batch_dxf_placement.py"
    else:
        filename = "batch_dxf_lines.py"
    if (
        not location.is_absolute()
        or location.name != filename
        or not location.is_file()
    ):
        raise ValueError("Selected resource must identify its installed batch writer")
    destination = location.resolve().parent / here.name
    if (
        destination.is_file()
        and destination.resolve().parent == location.resolve().parent
    ):
        return destination
    if not method.get("sample_request") and file_digest(location) == file_digest(
        here.with_name(filename)
    ):
        return here
    raise ValueError("Selected writer installation lacks the matching batch runner")


def published_readback(directory, request, spec, digest, targets, row):
    """Check the worker's result and receipt against the job actually published."""
    receipt = read(directory / "readback.json")
    if not isinstance(receipt, dict) or not receipt:
        raise ValueError("Published readback must contain measured target properties")
    source = (
        (request.parent / spec["model"]).resolve()
        if "operation" in spec
        else Path(spec["model"]).resolve()
    )
    if file_digest(source) != spec["revision"]:
        raise ValueError("Published batch source revision differs")
    if "operation" in spec:
        operation = spec["operation"]
        suffix = {"circle": "dxf", "cut": "step", "bore diameter": "step"}.get(
            operation, "xbf"
        )
        result = directory / ("result." + suffix)
        manifest = read(directory / "manifest.json")
        expected = {
            name: file_digest(directory / name)
            for name in ("request.json", "readback.json", result.name)
        }
        if (
            manifest != expected
            or manifest["request.json"] != digest
            or receipt["request_sha256"] != digest
            or receipt["operation"] != operation
            or receipt["source_sha256"] != spec["revision"]
            or receipt["result_sha256"] != manifest[result.name]
            or set(measured_ids(receipt["elements"])) != set(targets)
        ):
            raise ValueError(
                "Published batch artifacts differ from the reviewed request or targets"
            )
    else:
        evidence = read(directory / "evidence.json")
        for key in ("operation", "readback"):
            name = key + ".json"
            if evidence[key] != name or evidence[key + "_sha256"] != file_digest(
                directory / name
            ):
                raise ValueError("Published DXF evidence differs from its receipts")
        operation = read(directory / "operation.json")
        for item in (receipt, operation):
            if (
                item["status"] != "completed"
                or item["result"] != "result.dxf"
                or item["result_sha256"] != file_digest(directory / "result.dxf")
                or any(
                    item[k] != row[k]
                    for k in (
                        "resource",
                        "name",
                        "action",
                        "input",
                        "output",
                        "backend",
                    )
                )
            ):
                raise ValueError(
                    "Published DXF result differs from its selected method or model"
                )
        if (
            receipt["operation_id"] != operation["operation_id"]
            or operation["source_sha256"] != spec["revision"]
            or Path(operation["source"]).resolve() != source
            or set(receipt["observed"]) != set(targets)
            or set(operation["expected"]) != set(targets)
        ):
            raise ValueError("Published DXF receipts differ from the reviewed targets")
        if spec["action"] == "place":
            plan = read(directory / "plan.json")
            if (
                read(directory / "review.json")["plan_sha256"]
                != file_digest(directory / "plan.json")
                or plan["job_id"] != operation["operation_id"]
                or plan["expected"] != operation["expected"]
                or plan["resource"] != row["resource"]
                or plan["sample"]
                or plan.get("row_check") != spec.get("row_check")
                or plan["unit"] != spec["model_unit"]
            ):
                raise ValueError(
                    "Published placement plan differs from reviewed ownership or layout"
                )
            for r in spec["rows"]:
                dest = plan["expected"][r["target"]]
                if (
                    dest["before"] != r["current"]["world_frame"]
                    or dest["world_frame"] != r["requested"]["world_frame"]
                    or any(
                        dest[k] != r[k]
                        for k in ("reference", "position_id", "position_index")
                    )
                ):
                    raise ValueError(
                        "Published placement differs from the reviewed destination"
                    )
        elif operation.get("preview_sha256") != digest:
            raise ValueError("Published LINE job differs from its reviewed preview")
    return receipt


def lacks_dependency(error):
    return isinstance(error, ImportError) or isinstance(error.__cause__, ImportError)


def deliver(
    request, catalogue, directory, *, request_sha256=None, payload=None, selected=None
):
    if payload is None:
        payload = request.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if request_sha256 is not None and digest != request_sha256:
        raise ValueError("Reviewed request digest differs")
    preview = Preview(payload.decode())
    spec = preview.read()
    data = load(catalogue)
    placement = spec.get("action") == "place"
    # Pattern target enumeration can require the provider's geometry libraries.
    targets = None if "pattern" in spec else target_ids(spec)
    if "rows" in spec:
        contract = (spec["action"], spec["entity"], spec["output"])
    else:
        operation = spec["operation"]
        contract = CONTRACTS[operation]
    attempts = []
    report = dict(attempts=attempts, completed=[], remaining=targets or [])
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
    if selected is not None:
        row, approved = selected
        if (
            resources.get(row["resource"]) != approved
            or row not in candidates
            or provider_python(approved) != Path(sys.executable)
        ):
            raise ValueError(
                "Selected resource or interpreter changed before batch execution"
            )
        candidates = [row]
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
            runner = provider_runner(resource, row, method)
            if selected is None and (
                provider_python(resource) != Path(sys.executable)
                or runner != Path(__file__).resolve()
            ):
                owns_result = True
                response = provider_call(
                    resource,
                    runner,
                    "execute-method",
                    dict(
                        request=str(request.absolute()),
                        catalogue=str(catalogue.absolute()),
                        directory=str(directory.absolute()),
                        payload=preview.document,
                        digest=digest,
                        selected=[row, resource],
                    ),
                )
                completed = response.get("completed")
                remaining = response.get("remaining")
                if not isinstance(completed, list) or not isinstance(remaining, list):
                    raise ValueError("Provider returned no batch target readback")
                returned = completed + remaining
                if (
                    any(not isinstance(k, str) or not k for k in returned)
                    or len(set(returned)) != len(returned)
                    or (targets is not None and set(returned) != set(targets))
                ):
                    raise ValueError("Provider returned inconsistent target IDs")
                if "blocker" in response:
                    if placement and (directory / "results.json").is_file():
                        effects = read(directory / "results.json")
                        if set(effects) == set(targets):
                            report["completed"] = [
                                k
                                for k in targets
                                if effects[k]["status"] == "completed"
                            ]
                            report["remaining"] = [
                                k for k in targets if k not in report["completed"]
                            ]
                    raise ValueError(response["blocker"])
                record = response.get("readback")
                if (
                    remaining
                    or not completed
                    or not isinstance(record, dict)
                    or not record
                ):
                    raise ValueError("Provider returned no completed batch readback")
                if targets is None:
                    try:
                        targets = target_ids(spec)
                    except (ImportError, ValueError) as exc:
                        if not lacks_dependency(exc):
                            raise
                        identity = provider_call(
                            resource, runner, "pattern-targets", spec
                        )
                        targets = identity["targets"]
                        if (
                            not isinstance(targets, list)
                            or not targets
                            or any(not isinstance(k, str) or not k for k in targets)
                            or len(set(targets)) != len(targets)
                        ):
                            raise ValueError(
                                "Provider could not identify reviewed pattern members"
                            )
                    report["remaining"] = targets
                if set(completed) != set(targets) or record != published_readback(
                    directory, request, spec, digest, targets, row
                ):
                    raise ValueError(
                        "Provider readback differs from its published job or reviewed targets"
                    )
                report.update(completed=completed, remaining=[], readback=record)
                if "row_check" in spec:
                    report["row_measurements"] = record["row_measurements"]
                entry["outcome"] = "completed"
                return report
            if targets is None:
                targets = target_ids(spec)
                report["remaining"] = targets
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
    if targets is None and not report["remaining"]:
        try:
            report["remaining"] = target_ids(spec)
        except (ImportError, ValueError, KeyError, TypeError, RuntimeError) as exc:
            report["target_error"] = str(exc)
            report["unresolved_pattern"] = spec["pattern"]
            report["blocker"] += f"; target enumeration: {exc}"
    return report


if __name__ == "__main__":
    if sys.argv[1:] == ["pattern-targets"]:
        try:
            print(json.dumps({"targets": target_ids(json.load(sys.stdin))}))
        except (ImportError, ValueError, TypeError, KeyError) as error:
            sys.exit(str(error))
        sys.exit(0)
    if sys.argv[1:] == ["execute-method"]:
        try:
            job = json.load(sys.stdin)
            result = deliver(
                Path(job["request"]),
                Path(job["catalogue"]),
                Path(job["directory"]),
                request_sha256=job["digest"],
                payload=job["payload"].encode(),
                selected=job["selected"],
            )
            print(json.dumps(result))
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
