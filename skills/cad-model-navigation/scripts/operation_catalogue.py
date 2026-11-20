"""Check approved modeling methods by their dependencies and save their local availability."""

import argparse
import hashlib
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
from urllib.parse import urlsplit
import subprocess
import sys
import tempfile

ACTIONS = {'create', 'modify', 'replace', 'place'}
VERSION = 2
HERE = Path(__file__).resolve().parent
OPENCV = {
    "contours": ("binary image", "contours"),
    "plane": ("four point correspondences", "homography"),
    "thinning": ("binary image", "skeleton"),
}


def location():
    base = os.getenv("XDG_CONFIG_HOME") or Path.home() / ".config"
    return Path(base) / "cad-modeling" / "operations.json"


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load(path):
    if not path.exists():
        return {"version": VERSION, "resources": [], "operations": []}
    catalogue = read(path)
    if catalogue.get("version") not in (1, VERSION):
        raise ValueError("Unsupported operation catalogue version")
    return catalogue


@contextmanager
def update_lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.with_suffix(path.suffix + ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False, mode="w") as tmp:
        name = Path(tmp.name)
        try:
            json.dump(data, tmp, indent=2, allow_nan=False)
            tmp.write("\n")
            tmp.flush()
            os.fsync(tmp.fileno())
        except BaseException:
            name.unlink(missing_ok=True)
            raise
    try:
        name.replace(path)
    finally:
        name.unlink(missing_ok=True)


def selected_script(resource, name):
    # Other installed skills may own the selected helper.
    path = Path(resource.get("scripts", HERE)) / name
    if not path.is_absolute() or not path.is_file():
        raise ValueError(f"Missing operation helper: {path}")
    return path


def require_path(value, *, file=False):
    path = Path(value)
    if not value or not (path.is_file() if file else path.exists()):
        raise ValueError(f"Missing dependency: {value}")
    return path


def qualify(resource, method):
    kind = method["probe"]
    helpers = {
        "vision": "vision_provider.py",
        "sam": "sam_mask.py",
        "sam2": "vision_provider_sam2.py",
        "parts": "catalogue_candidates.py",
        "dxf": "dxf_inspect.py",
        "intake": "source_intake.py",
        "cad-sequence": "learned_cad_provider.py",
    }
    outputs = {
        "sam": "mask",
        "sam2": "mask",
        "cad-sequence": "editable sequence",
        "dxf": "entity inventory",
        "parts": "part candidates",
        "intake": "source revision",
        **{name: pair[1] for name, pair in OPENCV.items()},
    }
    if kind in outputs and method["output"] != outputs[kind]:
        raise ValueError(f"{kind} produces {outputs[kind]}")
    modules = list(method.get("modules", []))
    for dependency in method.get("paths", []):
        require_path(dependency)
    if kind == "guided":
        require_path(resource["location"])
        if not modules and "python" not in resource:
            return
    elif kind in helpers:
        helper = selected_script(resource, helpers[kind])
    elif kind not in OPENCV:
        raise ValueError(f"Unknown operation: {kind}")
    python = require_path(resource["python"], file=True)
    if not python.is_absolute():
        raise ValueError("Specify the absolute path of the selected interpreter")
    if kind in OPENCV:
        command = [python, "-I", str(HERE / "opencv_probe.py"), kind]
    else:
        if kind in ("vision", "cad-sequence"):
            location = resource["location"]
            if kind == "vision":
                modules.extend(["numpy", "PIL.Image", "image_observations"])
                config = read(method["config"])
                if (config.get("url") or config.get("local_checkpoint")) != location:
                    raise ValueError(
                        "Vision configuration selects a different resource"
                    )
                if config.get("format") == "moondream":
                    modules.append("cairosvg")
                if "local_checkpoint" in config:
                    require_path(location)
                    modules.extend(["torch", "ultralytics"])
            if kind == "cad-sequence" or "url" in config:
                endpoint = urlsplit(location)
                if (
                    endpoint.scheme not in ("http", "https")
                    or not endpoint.hostname
                    or endpoint.username is not None
                    or endpoint.password is not None
                    or endpoint.fragment
                ):
                    raise ValueError("Missing HTTP(S) inference endpoint")
        elif kind in ("sam", "sam2"):
            model = require_path(resource["location"])
            files = ["config.json", "model.safetensors", "preprocessor_config.json"]
            if kind == "sam2":
                files.append("processor_config.json")
            for filename in files:
                require_path(model / filename, file=True)
            modules.extend(
                ["torch", "transformers", "PIL.Image", "numpy", "safetensors"]
            )
        elif kind == "dxf":
            modules.append("ezdxf")
        elif kind == "parts":
            require_path(method["search_cli"], file=True)
            for filename in ("catalogue.json", "catalogue.sqlite"):
                require_path(Path(resource["location"]) / filename, file=True)
        # Import the client and its dependencies, without invoking the operation.
        directory = str(helper.parent) if kind in helpers else str(HERE)
        if kind in helpers:
            modules.append(helper.stem)
        code = (
            "import importlib, sys; sys.path.insert(0, sys.argv[1]); "
            "[importlib.import_module(name) for name in sys.argv[2:]]"
        )
        if kind in ("sam", "sam2"):
            prefix = "Sam2" if kind == "sam2" else "Sam"
            code += f"; from transformers import {prefix}Model, {prefix}Processor"
        command = [python, "-B", "-c", code, directory, *modules]
    env = dict(
        os.environ,
        YOLO_OFFLINE="true",
        YOLO_AUTOINSTALL="false",
        HF_HUB_OFFLINE="1",
        TRANSFORMERS_OFFLINE="1",
        PIP_NO_INDEX="1",
    )
    result = subprocess.run(command, capture_output=True, text=True, env=env)
    if result.returncode:
        if kind in OPENCV and result.stdout:
            outcome = json.loads(result.stdout)
            raise ValueError(outcome.get("error") or outcome["status"])
        raise ValueError(
            result.stderr.strip().splitlines()[-1]
            if result.stderr.strip()
            else f"Dependency check exited with status {result.returncode}"
        )


def methods(resource):
    if resource.get("kind") == "opencv":
        return [
            dict(name=name, probe=name, input=src, output=dst)
            for name, (src, dst) in OPENCV.items()
        ]
    if not resource.get("methods"):
        raise ValueError(
            f"Specify the modeling operations to check for {resource['id']}"
        )
    return resource["methods"]


def changes(before, after):
    old = {(row["resource"], row["name"]): row["usable"] for row in before}
    new = {(row["resource"], row["name"]): row["usable"] for row in after}
    return {
        label: [
            list(key)
            for key in sorted(old.keys() | new.keys())
            if new.get(key, False) == state and old.get(key, False) != state
        ]
        for label, state in (("became_available", True), ("became_unavailable", False))
    }


def file_digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def receipt_object(value, field):
    if not isinstance(value, dict) or not value:
        raise ValueError(f"Specify a nonempty {field} record")
    return value


def receipt_text(record, field):
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Specify {field} in receipt")
    return value


def bound_path(base, record, field):
    path = (base / receipt_text(record, field)).resolve()
    if file_digest(path) != receipt_text(record, field + "_sha256"):
        raise ValueError(f"Changed {field} file")
    return path


def verify_receipts(row, resource, path):
    """Validate the actual writer and independent readback records for one sample."""
    evidence = receipt_object(read(path), "evidence")
    base = path.parent
    writer_path = bound_path(base, evidence, "operation")
    reader_path = bound_path(base, evidence, "readback")
    if writer_path == reader_path:
        raise ValueError("Operation and readback receipts must be separate files")
    writer = receipt_object(read(writer_path), "operation")
    reader = receipt_object(read(reader_path), "readback")
    for record in (writer, reader):
        for field in ("resource", "name", "action", "input", "output"):
            if receipt_text(record, field) != row[field]:
                raise ValueError(f"Receipt describes a different {field}")
        if receipt_text(record, "backend") != receipt_text(resource, "backend"):
            raise ValueError("Receipt describes a different backend")
        if receipt_text(record, "status") != "completed":
            raise ValueError("Incomplete operation or readback")
    if receipt_text(reader, "operation_id") != receipt_text(writer, "operation_id"):
        raise ValueError("Readback belongs to another operation")
    if receipt_text(reader, "readback_id") == writer["operation_id"]:
        raise ValueError("Specify a separate readback ID")
    source = bound_path(writer_path.parent, writer, "source")
    result = bound_path(writer_path.parent, writer, "result")
    if writer["source_sha256"] == writer["result_sha256"]:
        raise ValueError("Sample edit must change the source revision")
    if bound_path(reader_path.parent, reader, "result") != result:
        raise ValueError("Readback belongs to another model")
    expected = receipt_object(writer.get("expected"), "expected target properties")
    observed = receipt_object(reader.get("observed"), "measured target properties")
    for target, properties in expected.items():
        if not isinstance(target, str) or not target.strip():
            raise ValueError("Specify a target ID")
        receipt_object(properties, "expected target properties")
    if set(expected) != set(observed):
        raise ValueError("Readback target set differs from the operation")
    if writer["backend"].startswith("ezdxf/") and row["input"] == "DXF LINE":
        from batch_dxf_lines import verify_sample
        verify_sample(source, result, writer, expected)
        from batch_dxf_lines import drawing, line, measured
        saved = drawing(result, writer["unit"])
        for target, props in observed.items():
            start, _, length = measured(line(saved, target))
            actual = {"start": list(start), "length": length}
            if json.dumps(actual, sort_keys=True) != json.dumps(props, sort_keys=True):
                raise ValueError("Readback differs from saved DXF geometry")
    elif writer["backend"].startswith("ezdxf/") and row["input"] == "DXF INSERT":
        from batch_dxf_frames import verify_result
        actual = verify_result(source, result, writer, require_change=True)
        if actual != observed:
            raise ValueError("Readback differs from reopened occurrence frames")
    else:
        raise ValueError("No backend artifact verification for this operation")
    return file_digest(path)


def refresh(path, resources, *, resource_base=None):
    previous = load(path)
    if not isinstance(resources, list):
        raise ValueError("Approved resources must be a JSON list")
    operations = []
    identifiers = set()
    for resource in resources:
        identifier = resource["id"]
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in identifiers
        ):
            raise ValueError("Each resource needs a unique nonempty id")
        identifiers.add(identifier)
        if not resource.get("kind"):
            raise ValueError(f"Specify the resource kind for {identifier}")
        names = set()
        for method in methods(resource):
            name = method["name"]
            if not name or name in names:
                raise ValueError(f"Duplicate or empty method in {identifier}")
            names.add(name)
            row = dict(
                resource=identifier,
                name=name,
                input=method["input"],
                output=method["output"],
                usable=False,
            )
            try:
                for obsolete in (
                    "approved_files",
                    "sample",
                    "images",
                    "query",
                    "prompt",
                ):
                    method.pop(obsolete, None)
                if "action" in method:
                    row.update(action=method["action"], readback_verified=False)
                    if method.get("readback_file"):
                        method["readback_file"] = str(((resource_base or path.parent) / method["readback_file"]).resolve())
                qualify(resource, method)
                if "action" in method:
                    if method["action"] not in ACTIONS:
                        raise ValueError("Unknown batch action")
                    if not method.get("readback_file"):
                        raise ValueError("Operation needs sample execution and readback")
                    evidence_path = Path(method["readback_file"])
                    digest = verify_receipts(row, resource, evidence_path)
                    row.update(readback_verified=True, readback_file=str(evidence_path), evidence_sha256=digest, backend=resource["backend"])
                row["usable"] = True
            except (OSError, ValueError, KeyError, TypeError, ImportError, subprocess.SubprocessError) as exc:
                row["reason"] = str(exc)
            operations.append(row)
    catalogue = dict(version=VERSION, resources=resources, operations=operations)
    write(path, catalogue)
    return {**catalogue, **changes(previous["operations"], operations)}


def record_result(path, args):
    with update_lock(path):
        catalogue = load(path)
        row = next(
            (
                item
                for item in catalogue["operations"]
                if (item["resource"], item["name"]) == (args.resource, args.method)
            ),
            None,
        )
        if row is None:
            raise ValueError("Unknown catalogued operation")
        row.update(usable=False, reason=args.reason)
        write(path, catalogue)
        return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalogue", type=Path, default=location())
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("show")
    update = sub.add_parser("refresh")
    update.add_argument(
        "--resources", type=Path, help="Complete user-confirmed resource list (JSON)"
    )
    routes = sub.add_parser("routes")
    routes.add_argument("output", help="Required operation output")
    failed = sub.add_parser("failed")
    failed.add_argument("resource")
    failed.add_argument("method")
    failed.add_argument("reason")
    args = parser.parse_args()
    try:
        catalogue = load(args.catalogue)
        if catalogue["version"] == 1 and args.action != "refresh":
            with update_lock(args.catalogue):
                catalogue = load(args.catalogue)
                if catalogue["version"] == 1:
                    catalogue = refresh(args.catalogue, catalogue["resources"])
        if args.action == "show":
            result = {
                **catalogue,
                "setup_required": not args.catalogue.is_file(),
                "discovered_python": sys.executable,
            }
        elif args.action == "refresh":
            with update_lock(args.catalogue):
                current = load(args.catalogue)
                if args.resources is None and not args.catalogue.is_file():
                    raise ValueError(
                        "Initial setup needs a user-confirmed resource list"
                    )
                resources = (
                    read(args.resources) if args.resources else current["resources"]
                )
                result = refresh(args.catalogue, resources, resource_base=args.resources.resolve().parent if args.resources else args.catalogue.parent)
        elif args.action == "routes":
            result = [
                row
                for row in catalogue["operations"]
                if row["usable"] and row["output"] == args.output
                and ("action" not in row or row.get("readback_verified") is True and row.get("evidence_sha256"))
            ]
        else:
            result = record_result(args.catalogue, args)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
