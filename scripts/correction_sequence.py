"""Run independent or sequential STEP and XCAF corrections with verified per-step reuse."""
import argparse
import fcntl
import hashlib
import json
from importlib.metadata import version
from pathlib import Path
import tempfile

from batch_modification import execute
from operation_catalogue import file_digest

# We read ideas for checking face references after edits, reusing earlier modeling steps,
# classifying imported bodies, and tracking mesh repairs in CadKit Kernel.
# Read 2026-11-24. Upstream licence: MIT OR Apache-2.0. https://github.com/civilkit/cadkit-kernel


def writer_identity():
    import sys
    modules = ("correction_sequence", "batch_modification", "batch_creation", "batch_request",
               "batch_xcaf_bars", "batch_dxf_lines", "batch_dxf_placement", "operation_catalogue")
    root = Path(__file__).parent
    return dict(cadquery=version("cadquery"), ocp=version("cadquery-ocp"),
                python=sys.version, code={name:file_digest(root / (name + ".py")) for name in modules})


def run(plan_path, store):
    plan = json.loads(plan_path.read_bytes())
    steps = plan["steps"]
    seen = set()
    for step in steps:
        name = step["id"]
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise ValueError("Use distinct readable step identifiers")
        if "after" in step and step["after"] not in seen:
            raise ValueError("Each predecessor must appear earlier in the plan")
        seen.add(name)
    store.mkdir(parents=True, exist_ok=True)
    provider = writer_identity()
    results = {}
    with (store / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        for step in steps:
            name = step["id"]
            parent = results.get(step.get("after"))
            if parent and parent["status"] != "PASS":
                results[name] = dict(status="BLOCKED", dependency=step["after"])
                continue
            try:
                spec = dict(step["edit"])
                suffix = {"bore diameter":"step", "bar length":"xbf", "occurrence name":"xbf"}.get(spec["operation"])
                if suffix is None:
                    raise ValueError("Use a STEP bore edit, XCAF bar edit or XCAF occurrence rename")
                if parent:
                    if "model" in spec or "revision" in spec:
                        raise ValueError("A dependent edit takes its model and revision from its predecessor")
                    spec.update(model=parent["output"], revision=parent["sha256"])
                else:
                    spec["model"] = str((plan_path.parent / spec["model"]).resolve())
                request = json.dumps(spec, sort_keys=True, allow_nan=False).encode()
                binding = [provider, spec, parent["key"] if parent else None]
                key = hashlib.sha256(json.dumps(binding, sort_keys=True).encode()).hexdigest()
                job = store / key
                cached = job.exists()
                with tempfile.TemporaryDirectory(dir=store) as temp:
                    path = Path(temp) / "request.json"
                    path.write_bytes(request)
                    receipt = execute(path, job)
                results[name] = dict(status="PASS", reused=cached, key=key,
                                     output=str((job / ("result." + suffix)).resolve()),
                                     sha256=receipt["result_sha256"])
            except (ValueError, OSError, RuntimeError, KeyError, TypeError) as error:
                results[name] = dict(status="FAILED", reason=str(error))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("store", type=Path)
    args = parser.parse_args()
    rows = run(args.plan, args.store)
    print(json.dumps(rows, indent=2))
    raise SystemExit(int(any(row["status"] != "PASS" for row in rows.values())))
