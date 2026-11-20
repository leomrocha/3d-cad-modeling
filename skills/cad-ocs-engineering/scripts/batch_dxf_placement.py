"""Review, apply and resume individual existing DXF INSERT placements."""
import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import tempfile
from uuid import uuid4

from batch_dxf_frames import INPUT, METHOD, OUTPUT, TOL, check_document, check_editable, resolve_frame, signatures, verify_result
from batch_dxf_inventory import read_inventory
from batch_dxf_lines import backend, drawing, publish_directory
from batch_insert_recovery import writer_interval
from batch_request import Preview, execution_rows, prepare
from batch_selection import resolve as resolve_selection, verify_reopened
from cadtools.checkpoints import atomic_json
from cadtools.runtime import Journal
from operation_catalogue import file_digest, load, read
from spatial_positions import frame
from step_placements import classify_hand, cross, inverse, multiply, native_fields, near


def review(request, positions, catalogue):
    if positions["unit"] != request["model_unit"]:
        raise ValueError("Position and model length units differ")
    selection = dict(request["selection"], operation_reference=positions["reference"])
    request = dict(request, entity=INPUT, output=OUTPUT, action="place", selection=selection)
    if ("assignments" in request) == ("order_by" in request):
        raise ValueError("Specify explicit assignments or order_by")
    if "order_by" in request:
        order = request["order_by"]
        if order not in ("increasing measured distance", "decreasing measured distance") or "measurement" not in selection:
            raise ValueError("Ordered placement requires a selected native reference and measured distance")
        snapshot = read_inventory(request["model"], request["model_unit"])
        targets = resolve_selection(request, snapshot)
        ranked = sorted((t["selection"]["measurement"]["distance"], t["id"]) for t in targets)
        if any(b[0] - a[0] <= TOL for a, b in zip(ranked, ranked[1:])):
            raise ValueError("Tied reference distances require explicit position assignments")
        if order == "decreasing measured distance":
            ranked.reverse()
        assignments = {t[1]: p["id"] for t, p in zip(ranked, positions["positions"], strict=True)}
    else:
        assignments = request["assignments"]
    destinations = {row["id"]: row for row in positions["positions"]}
    if (len(destinations) != len(positions["positions"]) or len(assignments) != len(destinations)
            or set(assignments.values()) != set(destinations)):
        raise ValueError("Assign each selected target and each position ID exactly once")
    indices = {position: i for i, position in enumerate(destinations)}
    values = {}
    for target, position_id in assignments.items():
        row = destinations[position_id]
        if row.get("reference", positions["reference"]) != positions["reference"]:
            raise ValueError(f"Position {position_id} names a different reference from its group")
        if "world_transform" in row:
            matrix = row["world_transform"]
        else:
            plane = positions["frame"]
            matrix = frame(row["xyz"], cross(plane["x"], plane["y"]),
                           row.get("direction_xyz", plane["x"]))
        classify_hand(matrix)
        if [matrix[i][3] for i in range(3)] != row["xyz"]:
            raise ValueError(f"Position and frame origins differ for {position_id}")
        values[target] = {"world_frame": matrix}
    data = prepare(dict(request, values=values), catalogue).read()
    if "order_by" in request:
        data["order_by"] = request["order_by"]
    for row in data["rows"]:
        row["position_id"] = assignments[row["target"]]
        row["position_index"] = indices[row["position_id"]]
    return Preview(json.dumps(data, indent=2, allow_nan=False))


def preflight(doc, rows):
    uses = Counter(e.dxf.name.casefold() for e in doc.entitydb.values() if e.dxftype() == "INSERT")
    paths = {row["target"] for row in rows}
    if not paths or len(paths) != len(rows) or len({r["position_id"] for r in rows}) != len(rows):
        raise ValueError("Expected unique existing occurrence paths")
    for row in rows:
        target = row["target"]
        parts = target.split("/")
        for i, handle in enumerate(parts):
            ancestor = doc.entitydb[handle]
            if ancestor.dxftype() != "INSERT" or doc.blocks[ancestor.dxf.name].block.dxf.flags:
                raise ValueError(f"{target} requires local named block references")
            if i < len(parts) - 1 and (uses[ancestor.dxf.name.casefold()] != 1
                                      or "/".join(parts[:i+1]) in paths):
                raise ValueError(f"Moving {target} would edit other occurrences or a selected ancestor")
        current = resolve_frame(doc, target)[2]
        check_editable(doc, target)
        desired = row["requested"]["world_frame"]
        classify_hand(desired)
        if not near(current, row["current"]["world_frame"], TOL):
            raise ValueError(f"Starting placement differs at {target}")
        if classify_hand(desired) != classify_hand(current):
            raise ValueError(f"Requested placement changes the handedness of {target}")


def start(preview, directory, resource, catalogue=None, *, sample=False):
    data = preview.read()
    if (data["action"], data["entity"], data["output"]) != ("place", INPUT, OUTPUT):
        raise ValueError("Expected an existing-occurrence placement review")
    source = Path(data["model"]).resolve()
    if file_digest(source) != data["revision"]:
        raise ValueError("Source revision changed")
    if sample:
        rows = data["rows"]
        paths = verify_reopened(preview, read_inventory(data["model"], data["model_unit"]))
        if ["/".join(p) for p in paths] != [r["target"] for r in rows]:
            raise ValueError("Selected paths changed")
    else:
        if not any(r["name"] == METHOD and r.get("backend") == backend() and r["resource"] == resource
                   for r in data["routes"]):
            raise ValueError("Reviewed catalogue route differs from installed placement backend")
        rows = execution_rows(preview, resource, METHOD, catalogue_path=catalogue,
                              read_revision=file_digest, read_inventory=read_inventory)
    unit = data["model_unit"]
    doc = drawing(source, unit)
    check_document(doc, unit, doc.dxfversion)
    preflight(doc, rows)
    directory = Path(directory).absolute()
    with tempfile.TemporaryDirectory(dir=directory.parent) as tmp:
        job = Path(tmp) / "job"
        job.mkdir()
        shutil.copyfile(source, job / "result.dxf")
        if file_digest(job / "result.dxf") != data["revision"]:
            raise ValueError("Source changed while initializing the batch")
        namespace = uuid4().hex
        targets = {r["target"]: dict(before=r["current"]["world_frame"], **r["requested"],
                                     reference=r["reference"], position_id=r["position_id"],
                                     position_index=r["position_index"],
                                     request_id=namespace + ":" + r["target"]) for r in rows}
        plan = dict(source=str(source), source_sha256=data["revision"], unit=unit, version=doc.dxfversion, job_id=namespace,
                    sample=sample, resource=resource, expected=targets)
        atomic_json(job / "plan.json", plan)
        atomic_json(job / "review.json", {"plan_sha256": file_digest(job / "plan.json")})
        atomic_json(job / "results.json", {k: {"status": "pending"} for k in targets})
        publish_directory(job, directory)


def set_frame(entity, parent, desired):
    local = multiply(inverse(parent), desired)
    fields = native_fields(local)
    entity.dxf.insert = tuple(fields["insert_point"].values())
    entity.dxf.extrusion = tuple(fields["normal"].values())
    entity.dxf.rotation = math.degrees(fields["rotation"])
    entity.dxf.xscale = entity.dxf.zscale = 1
    entity.dxf.yscale = -1 if classify_hand(local) == "MIRRORED" else 1


def sync_path(path):
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_one(directory, doc, target, parent, row, rev, checked):
    result = directory / "result.dxf"
    entity = doc.entitydb[target.split("/")[-1]]
    set_frame(entity, parent, row["world_frame"])
    with tempfile.TemporaryDirectory(dir=directory) as tmp:
        staged = Path(tmp) / "result.dxf"
        doc.saveas(staged)
        sync_path(staged)
        saved = checked(staged)
        check_editable(saved, target)
        current = resolve_frame(saved, target)[2]
        if not near(current, row["world_frame"], TOL):
            raise ValueError(f"Persisted world frame differs at {target}")
        if file_digest(result) != rev:
            raise ValueError("Drawing changed during placement")
        os.replace(staged, result)
        sync_path(directory)


def effect(current, row, intent):
    original = near(current, row["before"], TOL)
    if near(current, row["world_frame"], TOL) and (original or intent):
        return "applied"
    return "not_applied" if original else "unknown"


def resume(directory, *, after_save=None):
    directory = Path(directory)
    from ezdxf.lldxf.const import DXFError
    with writer_interval(directory):
        # Withdraw completed receipts while checking the current job drawing.
        for name in ("evidence.json", "operation.json", "readback.json"):
            (directory / name).unlink(missing_ok=True)
        sync_path(directory)
        if file_digest(directory / "plan.json") != read(directory / "review.json")["plan_sha256"]:
            raise ValueError("Placement contract changed since the job started")
        plan = read(directory / "plan.json")
        source, result = Path(plan["source"]), directory / "result.dxf"
        if file_digest(source) != plan["source_sha256"]:
            raise ValueError("Source drawing changed after placement review")
        targets = plan["expected"]
        unit = plan["unit"]
        base = signatures(drawing(source, unit), targets)
        journal = Journal(directory / "requests.jsonl")
        results = read(directory / "results.json")
        context = {"job_id": plan["job_id"], "source_sha256": plan["source_sha256"]}

        def checked(path):
            try:
                doc = drawing(path, unit)
                check_document(doc, unit, plan["version"])
                if signatures(doc, targets) != base:
                    raise ValueError("Drawing definitions, occurrence identities or independent geometry changed")
                return doc
            except (KeyError, TypeError, OSError, ValueError, DXFError) as error:
                if path == result:
                    for key, entry in results.items():
                        entry.update(confirmed=entry.get("confirmed", False) or entry["status"] == "completed",
                                     status="failed", effect="unknown", detail=str(error),
                                     request_id=targets[key]["request_id"])
                    atomic_json(directory / "results.json", results)
                raise

        for target, row in targets.items():
            rev = file_digest(result)
            doc = checked(result)
            key = row["request_id"]
            request = dict(op="place", target=target, **row)
            intent = journal.requests.get(key)
            confirmed = results[target].get("confirmed", False) or results[target]["status"] == "completed"
            detail = {}
            state = "unknown"
            status = "failed"
            try:
                if intent and (intent["request"] != request or intent["context"] != context):
                    raise ValueError(f"Saved intent differs for {target}")
                _, parent, current = resolve_frame(doc, target)
                state = effect(current, row, intent)
                check_editable(doc, target)
                if state == "not_applied" and not confirmed:
                    if not intent:
                        journal.intent(request, context)
                    write_one(directory, doc, target, parent, row, rev, checked)
                    if after_save:
                        after_save(target)
                    # Acknowledge the actual published drawing.
                    saved = checked(result)
                    check_editable(saved, target)
                    state = effect(resolve_frame(saved, target)[2], row, journal.requests.get(key))
                if state == "applied":
                    status = "completed"
                else:
                    detail["detail"] = "Published frame differs from the confirmed or requested placement"
            except InterruptedError:
                raise
            except (KeyError, TypeError, OSError, ValueError, DXFError) as error:
                detail["detail"] = str(error)
                # The staged save or its acknowledgement may fail on either side of publication.
                # Recover from the owned drawing before touching the next independent target.
                try:
                    saved = checked(result)
                    state = effect(resolve_frame(saved, target)[2], row, journal.requests.get(key))
                    check_editable(saved, target)
                    recorded = journal.requests.get(key, {})
                    if state == "applied" and recorded.get("request") == request and recorded.get("context") == context:
                        sync_path(result)
                        sync_path(directory)
                        status = "completed"
                except (KeyError, TypeError, OSError, ValueError, DXFError) as reconcile_error:
                    detail["readback_error"] = str(reconcile_error)
            results[target] = dict(status=status, effect=state, request_id=key,
                                   confirmed=confirmed or status == "completed", **detail)
            atomic_json(directory / "results.json", results)
        if all(row["status"] == "completed" for row in results.values()):
            if file_digest(source) != plan["source_sha256"]:
                raise ValueError("Source revision changed during verification")
            receipt = dict(resource=plan["resource"], name=METHOD, action="place", input=INPUT,
                           output=OUTPUT, backend=backend(), status="completed", operation_id=plan["job_id"],
                           result=result.name, result_sha256=file_digest(result))
            writer = dict(receipt, expected=targets, unit=unit, version=plan["version"], source=str(source), source_sha256=plan["source_sha256"])
            observed = verify_result(source, result, writer, require_change=plan["sample"])
            if file_digest(result) != receipt["result_sha256"] or file_digest(source) != plan["source_sha256"]:
                raise ValueError("Placement drawing changed during final readback")
            reader = dict(receipt, observed=observed, readback_id=plan["job_id"] + ":reopen")
            evidence = {}
            for name, record in (("operation", writer), ("readback", reader)):
                path = directory / (name + ".json")
                atomic_json(path, record)
                evidence[name], evidence[name + "_sha256"] = path.name, file_digest(path)
            atomic_json(directory / "evidence.json", evidence)
        return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="mode", required=True)
    prep = commands.add_parser("prepare")
    prep.add_argument("request", type=Path)
    prep.add_argument("positions", type=Path)
    prep.add_argument("--catalogue", type=Path, required=True)
    for mode in ("sample", "execute", "resume"):
        cmd = commands.add_parser(mode)
        if mode != "resume":
            cmd.add_argument("preview", type=Path)
            cmd.add_argument("--preview-sha256", required=True)
            cmd.add_argument("--resource", required=True)
            if mode == "execute":
                cmd.add_argument("--catalogue", required=True, type=Path)
        cmd.add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        try:
            backend()
        except ModuleNotFoundError as error:
            if error.name != "ezdxf":
                raise
            raise ValueError("DXF placement requires locally available ezdxf. Use the guided native "
                             "placement procedure in references/existing-batch-placement.md.") from error
        if args.mode == "prepare":
            print(review(read(args.request), read(args.positions), load(args.catalogue)).document)
            return
        if args.mode != "resume":
            payload = args.preview.read_bytes()
            if hashlib.sha256(payload).hexdigest() != args.preview_sha256:
                raise ValueError("Reviewed preview digest differs")
            start(Preview(payload.decode()), args.directory, args.resource, getattr(args, "catalogue", None),
                  sample=args.mode == "sample")
        results = resume(args.directory)
        print(json.dumps(results, indent=2))
        if any(row["status"] != "completed" for row in results.values()):
            raise SystemExit(1)
    except (KeyError, TypeError, OSError, ValueError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
