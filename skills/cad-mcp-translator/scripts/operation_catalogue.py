"""Check approved modeling methods with operation fixtures and save their local availability."""

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

VERSION = 1
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
    if catalogue.get("version") != VERSION:
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


def digest(path):
    with Path(path).open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def run_checked(command, server=False):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=180,
            stdin=subprocess.DEVNULL,
            check=False,
        )
    except subprocess.TimeoutExpired:
        raise ValueError("Operation fixture timed out after 180 seconds") from None
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        # Server error bodies, URLs and request arguments can contain credentials.
        if server:
            missing = re.search(r"No module named '([A-Za-z0-9_.]+)'", detail)
            status = re.search(r"returned HTTP (\d{3})", detail)
            if missing:
                raise ValueError(f"Missing Python module {missing[1]}")
            if status:
                raise ValueError(f"Inference server returned HTTP {status[1]}")
            if "Connection refused" in detail:
                raise ValueError("Connection refused by the selected inference server")
            raise ValueError("Inference fixture failed to return the requested output")
        raise ValueError(
            detail.splitlines()[-1][:500]
            if detail
            else f"Fixture exited with status {result.returncode}"
        )
    return result.stdout


def qualify(resource, method):
    kind = method["probe"]
    expected = {
        "sam": "mask",
        "sam2": "mask",
        "cad-sequence": "editable sequence",
        "dxf": "entity inventory",
        "parts": "part candidates",
        "intake": "source revision",
        **{k: v[1] for k, v in OPENCV.items()},
    }
    if kind in expected and method["output"] != expected[kind]:
        raise ValueError(f"{kind} produces {expected[kind]}")
    if kind == "guided":
        if not Path(resource["location"]).exists():
            raise ValueError("Selected guided tool or skill path is missing")
        raise ValueError(
            "Exercise the selected skill or tool with its input and check the output"
        )
    python = resource["python"]
    if not Path(python).is_absolute():
        raise ValueError("Specify the absolute path of the selected interpreter")
    if kind in OPENCV:
        command = [python, "-I", str(HERE / "opencv_probe.py"), kind]
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if not result.stdout:
            raise ValueError(result.stderr.strip() or "OpenCV probe returned no output")
        outcome = json.loads(result.stdout)
        if result.returncode or outcome["status"] != "tested":
            raise ValueError(outcome.get("error") or outcome["status"])
        return
    with tempfile.TemporaryDirectory(prefix="cad-operation-") as temporary:
        output = Path(temporary) / "result"
        if kind == "vision":
            config = read(method["config"])
            # Bind live qualification to the listed server or local checkpoint.
            if (config.get("url") or config.get("local_checkpoint")) != resource[
                "location"
            ]:
                raise ValueError("Vision configuration selects a different resource")
            run_checked(
                [
                    python,
                    selected_script(resource, "vision_provider.py"),
                    method["sample"],
                    method["config"],
                    output,
                ],
                server="url" in config,
            )
            observations = read(output / "observations.json")["instances"]
            if not any(
                row["kind"] == method["output"]
                and (row["kind"] != "mask" or any(any(line) for line in row["mask"]))
                for row in observations
            ):
                raise ValueError(f"Fixture returned no {method['output']} instance")
        elif kind in ("sam", "sam2"):
            script = "sam_mask.py" if kind == "sam" else "vision_provider_sam2.py"
            run_checked(
                [
                    python,
                    selected_script(resource, script),
                    method["sample"],
                    resource["location"],
                    method["prompt"],
                    output,
                ]
            )
            instances = read(output)["instances"]
            if not any(
                i["kind"] == "mask" and any(any(row) for row in i["mask"])
                for i in instances
            ):
                raise ValueError("Fixture returned no foreground mask")
        elif kind == "cad-sequence":
            command = [
                python,
                selected_script(resource, "learned_cad_provider.py"),
                resource["location"],
                method["model"],
                method["sample"],
                output,
            ]
            for image in method.get("images", []):
                command.extend(["--image", image])
            if method.get("key_env"):
                command.extend(["--key-env", method["key_env"]])
            run_checked(command, server=True)
            if not read(output / "sequence.json")["features"]:
                raise ValueError("CAD fixture returned no features")
        elif kind == "intake":
            run_checked(
                [
                    python,
                    selected_script(resource, "source_intake.py"),
                    "--input",
                    method["sample"],
                    "--output",
                    output,
                ]
            )
            if not (output / "revision/source-index.json").is_file():
                raise ValueError("Source intake fixture returned no revision index")
        elif kind == "dxf":
            run_checked(
                [
                    python,
                    selected_script(resource, "dxf_inspect.py"),
                    method["sample"],
                    "--output",
                    output,
                ]
            )
            if not read(output)["counts"]["selected_occurrences"]:
                raise ValueError("DXF fixture returned no selected entities")
        elif kind == "parts":
            raw = run_checked(
                [
                    python,
                    selected_script(resource, "catalogue_candidates.py"),
                    "--search-cli",
                    method["search_cli"],
                    "--source",
                    "parts",
                    resource["location"],
                    method["query"],
                ]
            )
            candidates = json.loads(raw)["sources"]["parts"]["candidates"]
            if not any(row.get("sha256") for row in candidates):
                raise ValueError("Parts lookup returned no matching local asset")
        else:
            raise ValueError(f"No operation fixture configured for {kind}")


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


def approved_files(method):
    # Confirm these exact bytes before a server fixture transmits user input.
    if method["probe"] in ("vision", "cad-sequence"):
        paths = [method["sample"], *method.get("images", [])]
        if method["probe"] == "vision":
            paths.append(method["config"])
        return {name: digest(name) for name in paths}
    return {}


def refresh(path, resources, *, confirm_files=True):
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
                hashes = approved_files(method)
                if confirm_files:
                    method["approved_files"] = hashes
                elif hashes != method.get("approved_files", {}):
                    raise ValueError(
                        "Fixture input or server configuration changed; confirm the new revision"
                    )
                qualify(resource, method)
                row["usable"] = True
            except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
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
        if args.action == "failed":
            row.pop("check", None)
            row.pop("evidence", None)
            row.pop("evidence_sha256", None)
            row.update(usable=False, reason=args.reason)
        else:
            resource = next(
                item for item in catalogue["resources"] if item["id"] == args.resource
            )
            method = next(
                item for item in methods(resource) if item["name"] == args.method
            )
            if method["probe"] != "guided":
                raise ValueError("Use the selected automatic operation fixture")
            if not Path(resource["location"]).exists():
                raise ValueError("Selected guided tool or skill path is missing")
            if not args.evidence.is_file() or not args.evidence.stat().st_size:
                raise ValueError(
                    "Supply the existing local evidence from the operation check"
                )
            row.pop("reason", None)
            row.update(
                usable=True,
                check=args.check,
                evidence=str(args.evidence.resolve()),
                evidence_sha256=digest(args.evidence),
            )
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
    passed = sub.add_parser("observed", help="Record an exercised guided operation")
    passed.add_argument("resource")
    passed.add_argument("method")
    passed.add_argument("evidence", type=Path)
    passed.add_argument(
        "check", help="Actual input, observed output and checked property"
    )
    args = parser.parse_args()
    try:
        catalogue = load(args.catalogue)
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
                result = refresh(
                    args.catalogue, resources, confirm_files=args.resources is not None
                )
        elif args.action == "routes":
            result = [
                row
                for row in catalogue["operations"]
                if row["usable"] and row["output"] == args.output
            ]
        else:
            result = record_result(args.catalogue, args)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
