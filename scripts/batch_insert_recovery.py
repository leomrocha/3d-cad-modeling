"""Start or resume journalled modelspace INSERTs into a job-owned DXF drawing."""
import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import tempfile
from uuid import uuid4

from assembly_occurrences import placement
from batch_dxf_lines import drawing, publish_directory, UNIT_CODES
from cadtools.checkpoints import atomic_json
from cadtools.runtime import Journal
from operation_catalogue import file_digest

APP = "CAD_BATCH_INSERT"
JOB_APP = "CAD_BATCH_JOB"
SEAT_TOLERANCE = 1e-10


def digest_tags(doc, entities):
    from ezdxf.lldxf.tagwriter import TagCollector
    digest = hashlib.sha256()
    for entity in entities:
        writer = TagCollector(dxfversion=doc.dxfversion, optional=False)
        entity.export_dxf(writer)
        digest.update(repr(writer.tags).encode())
    return digest.hexdigest()


def definition(doc, name):
    block = doc.blocks.get(name)
    if (block is None or name.startswith("*") or not len(block)
            or block.block.dxf.flags or any(e.dxftype() not in
                {"LINE", "CIRCLE", "ARC", "LWPOLYLINE", "TEXT", "SOLID", "POINT"}
                for e in block)):
        raise ValueError("Select a local named block containing supported primitive entities")
    return digest_tags(doc, [block.block, *block])


def contract(doc, plan):
    rows = plan["targets"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("Expected an ordered list of insertion targets")
    names, seats, targets = set(), set(), []
    for row in rows:
        name, point, block = row["id"], row["point"], row["block"]
        deps = row.get("depends_on", [])
        if (not isinstance(name, str) or not name.strip() or name in names
                or not isinstance(deps, list) or not set(deps).issubset(names)):
            raise ValueError("Target IDs must be unique and dependencies must precede the target")
        if (not isinstance(point, list) or len(point) != 3
                or any(type(n) not in (int, float) or not math.isfinite(n) for n in point)
                or any(all(abs(a-b) <= SEAT_TOLERANCE for a,b in zip(point, seat)) for seat in seats)):
            raise ValueError("Expected distinct finite modelspace WCS insertion points")
        if occupants(doc, point):
            raise ValueError(f"Starting seat occupied for {name}")
        targets.append(dict(id=name, point=point, block=block, depends_on=deps,
                            matrix=placement({"point": point}), definition=definition(doc, block),
                            request_id=uuid4().hex))
        seats.add(tuple(point))
        names.add(name)
    return targets


def occupants(doc, point):
    from ezdxf.math import Vec3
    matches = []
    for entity in doc.modelspace().query("INSERT"):
        dxf = entity.dxf
        rows, columns = dxf.row_count, dxf.column_count
        if rows < 1 or columns < 1 or rows * columns > 100000:
            raise ValueError("Unsupported INSERT array dimensions")
        ocs = entity.ocs()
        for row in range(rows):
            for col in range(columns):
                offset = Vec3(col * dxf.column_spacing, row * dxf.row_spacing, 0)
                seat = ocs.to_wcs(dxf.insert + offset.rotate_deg(dxf.rotation))
                if seat.isclose(point, rel_tol=0, abs_tol=SEAT_TOLERANCE):
                    matches.append(entity)
    return matches


def marker(entity):
    if entity.has_xdata(APP):
        return list(entity.get_xdata(APP))
    return []


def observe(doc, target):
    from ezdxf.math import Vec3
    rows = occupants(doc, target["point"])
    marked = [e for e in doc.modelspace().query("INSERT")
              if marker(e) == [(1000, target["request_id"])]]
    try:
        same_definition = definition(doc, target["block"]) == target["definition"]
    except ValueError:
        same_definition = False
    state = "unknown"
    if same_definition and not rows and not marked:
        state = "not_applied"
    elif same_definition and len(rows) == len(marked) == 1 and rows[0] is marked[0]:
        entity = rows[0]
        block = doc.blocks.get(target["block"])
        matrix = entity.matrix44()
        # The native DXF matrix maps the block's own base to the requested WCS seat.
        base = block.block.dxf.base_point
        desired = target["matrix"]
        axes = [Vec3(desired[0][i], desired[1][i], desired[2][i]) for i in range(3)]
        if (entity.dxf.name == target["block"] and entity.mcount == 1 and
                matrix.transform(base).isclose(target["point"], rel_tol=0, abs_tol=1e-10)
                and all(matrix.transform_direction(axis).isclose(expected, rel_tol=0, abs_tol=1e-12)
                        for axis, expected in zip(((1,0,0),(0,1,0),(0,0,1)), axes))):
            state = "applied"
    return dict(effect=state, count=len(rows), handles=[e.dxf.handle for e in rows],
                request_id=target["request_id"])


@contextmanager
def writer_interval(directory):
    with (directory / "writer.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def baseline(doc, excluded=()):
    ignored = set(excluded)
    return {b.name: {"entities": [e.dxf.handle for e in b if e.dxf.handle not in ignored],
                     "digest": digest_tags(doc, [b.block, *(e for e in b if e.dxf.handle not in ignored)])}
            for b in doc.blocks}


def read_owned(directory, plan):
    path = directory / "model.dxf"
    revision = file_digest(path)
    doc = drawing(path, plan["unit"])
    if (doc.dxfversion != plan["version"] or doc.units != UNIT_CODES[plan["unit"]]
            or not doc.modelspace().block_record.has_xdata(JOB_APP)
            or list(doc.modelspace().block_record.get_xdata(JOB_APP)) != [(1000, plan["job_id"])]):
        raise ValueError("Owned drawing identity, version or declared units differ")
    originals = set(plan["baseline"][doc.modelspace().block_record.dxf.name]["entities"])
    # New occurrences at selected seats receive a target-local classification.
    # Every original occurrence remains part of the independent comparison.
    excluded = {e.dxf.handle for t in plan["targets"] for e in occupants(doc, t["point"])
                if e.dxf.handle not in originals}
    intents = Journal(directory / "requests.jsonl").requests
    context = {"job_id": plan["job_id"], "source_sha256": plan["source_sha256"]}
    marked = {}
    for entity in doc.modelspace().query("INSERT"):
        tags = marker(entity)
        if len(tags) == 1 and tags[0][0] == 1000:
            marked.setdefault(tags[0][1], []).append(entity.dxf.handle)
    for target in plan["targets"]:
        key = target["request_id"]
        intent = intents.get(key, {})
        handles = marked.get(key, [])
        if (intent.get("context") == context and intent.get("request") == dict(op="insert", **target)
                and len(handles) == 1 and handles[0] not in originals):
            excluded.add(handles[0])
    actual = baseline(doc, excluded)
    selected_definitions = {t["block"].casefold() for t in plan["targets"]}
    def independent(blocks):
        return {name: signature for name, signature in blocks.items()
                if name.casefold() not in selected_definitions}
    if independent(actual) != independent(plan["baseline"]):
        raise ValueError("Independent drawing geometry differs from job baseline")
    if file_digest(path) != revision:
        raise ValueError("Owned drawing revision changed during readback")
    return doc, revision


def start(source, directory, plan):
    source, directory = Path(source), Path(directory)
    with tempfile.TemporaryDirectory(dir=directory.parent) as tmp:
        job = Path(tmp) / "job"
        job.mkdir()
        model = job / "model.dxf"
        shutil.copyfile(source, model)
        if file_digest(model) != plan["source_sha256"] or file_digest(source) != plan["source_sha256"]:
            raise ValueError("Source revision differs")
        doc = drawing(model, plan["unit"])
        if doc.units != UNIT_CODES[plan["unit"]] or doc.dxfversion < "AC1015":
            raise ValueError("DXF R2000 or later with declared matching units required")
        targets = contract(doc, plan)
        original = baseline(doc)
        job_id = uuid4().hex
        if JOB_APP not in doc.appids:
            doc.appids.new(JOB_APP)
        doc.modelspace().block_record.set_xdata(JOB_APP, [(1000, job_id)])
        doc.saveas(model)
        if baseline(drawing(model, plan["unit"])) != original:
            raise ValueError("Owned DXF initialization changed independent geometry")
        (job / "receipts").mkdir()
        atomic_json(job / "results.json", {t["id"]: dict(status="pending", request_id=t["request_id"])
                                          for t in targets})
        atomic_json(job / "plan.json", dict(unit=plan["unit"], targets=targets,
                    source_sha256=plan["source_sha256"], job_id=job_id, baseline=original, version=doc.dxfversion))
        publish_directory(job, directory)


def insert_one(directory, doc, target, unit, revision):
    # Preserve all independent block/layout entities through this format round trip.
    def retained(drawing, exclude=None):
        return {b.name: digest_tags(drawing, [e for e in b if e.dxf.handle != exclude])
                for b in drawing.blocks}

    before = retained(doc)
    if APP not in doc.appids:
        doc.appids.new(APP)
    entity = doc.modelspace().add_blockref(target["block"], target["point"])
    entity.set_xdata(APP, [(1000, target["request_id"])])
    with tempfile.TemporaryDirectory(dir=directory) as tmp:
        staged = Path(tmp) / "model.dxf"
        doc.saveas(staged)
        reopened = drawing(staged, unit)
        if observe(reopened, target)["effect"] != "applied" or retained(reopened, entity.dxf.handle) != before:
            raise ValueError("Saved insertion or independent geometry differs")
        if file_digest(directory / "model.dxf") != revision:
            raise ValueError("Owned drawing changed during insertion")
        with staged.open("rb") as stream:
            os.fsync(stream.fileno())
        os.replace(staged, directory / "model.dxf")
        descriptor = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def inspect_target(directory, doc, target, journal, plan):
    observation = observe(doc, target)
    key = target["request_id"]
    intent = journal.requests.get(key)
    request = dict(op="insert", **target)
    context = {"job_id": plan["job_id"], "source_sha256": plan["source_sha256"]}
    if intent and (intent["request"] != request or intent["context"] != context):
        raise ValueError("Journal intent differs from insertion contract")
    receipt = directory / "receipts" / (key + ".json")
    if ((receipt.is_file() and observation != json.loads(receipt.read_text()))
            or (observation["effect"] == "applied" and not intent)):
        observation["effect"] = "unknown"
    return observation, receipt, intent, request, context


def resume(directory, *, after_save=None):
    from ezdxf.lldxf.const import DXFError
    directory = Path(directory)
    with writer_interval(directory):
        plan = json.loads((directory / "plan.json").read_text())
        if "baseline" not in plan:
            raise ValueError("Job predates persisted drawing identity and independent baseline")
        journal = Journal(directory / "requests.jsonl")
        results = json.loads((directory / "results.json").read_text())

        def checked_read():
            try:
                return read_owned(directory, plan)
            except (ValueError, OSError, DXFError) as error:
                atomic_json(directory / "drawing-check.json", dict(status="failed", detail=str(error)))
                raise

        for target in plan["targets"]:
            doc, revision = checked_read()
            obs, receipt, intent, request, context = inspect_target(directory, doc, target, journal, plan)
            detail = {}
            blocked = any(results[key]["status"] != "completed" for key in target["depends_on"])
            if obs["effect"] == "not_applied" and not blocked:
                if intent is None:
                    journal.intent(request, context)
                try:
                    insert_one(directory, doc, target, plan["unit"], revision)
                except InterruptedError:
                    raise
                except (OSError, ValueError, DXFError) as error:
                    detail = {"detail": str(error)}
                else:
                    if after_save:
                        after_save(target["id"])
                doc, _ = checked_read()
                obs, *_ = inspect_target(directory, doc, target, journal, plan)
            if obs["effect"] == "applied":
                status = "completed"
                if not receipt.exists():
                    atomic_json(receipt, obs)
            elif obs["effect"] == "not_applied" and blocked:
                status = "pending"
            else:
                status = "failed"
            results[target["id"]] = dict(status=status, **obs, **detail)
            atomic_json(directory / "results.json", results)
        doc, revision = checked_read()
        for target in plan["targets"]:
            obs, *_ = inspect_target(directory, doc, target, journal, plan)
            row = results[target["id"]]
            if any(row[k] != v for k, v in obs.items()):
                row.update(obs, status="failed", detail="Target changed before final verification")
        atomic_json(directory / "results.json", results)
        atomic_json(directory / "drawing-check.json", dict(status="completed", revision=revision))
        return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--plan", type=Path)
    args = parser.parse_args()
    if bool(args.source) != bool(args.plan):
        parser.error("Supply --source and --plan together for a new job")
    try:
        if args.plan:
            start(args.source, args.directory, json.loads(args.plan.read_text()))
        results = resume(args.directory)
    except ModuleNotFoundError as error:
        parser.exit(2, f"Required installed Python module: {error.name}\n")
    except (ValueError, OSError, KeyError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(results, indent=2))
    return int(any(r["status"] != "completed" for r in results.values()))


if __name__ == "__main__":
    raise SystemExit(main())
