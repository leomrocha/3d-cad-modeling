"""Probe this interpreter or prepare a verified, job-owned OpenCV environment."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

# Isolated Python omits the script directory from its import path.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from opencv_probe import FAMILIES, OPERATIONS, probe


def wheel_hashes(folder):
    hashes = {}
    for wheel in sorted(folder.glob("*.whl")):
        with wheel.open("rb") as stream:
            hashes[wheel.name] = hashlib.file_digest(stream, "sha256").hexdigest()
    return hashes


def prepare(args):
    import fcntl

    root = args.root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    family = FAMILIES[
        (1 if args.operation == "thinning" else 0) + (2 if args.gui else 0)
    ]
    requirements = [family + ("==" + args.version if args.version else "")]
    if args.numpy_version:
        requirements.append("numpy==" + args.numpy_version)
    key = hashlib.sha256(
        json.dumps(
            [
                sys.executable,
                sys.version,
                requirements,
                args.operation,
                str(args.wheelhouse),
            ]
        ).encode()
    ).hexdigest()[:20]
    receipt = root / (key + ".json")
    with (root / (key + ".lock")).open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)

        def run_probe(python):
            run = subprocess.run(
                [python, "-I", __file__, "probe", args.operation],
                capture_output=True,
                text=True,
            )
            try:
                record = json.loads(run.stdout)
            except ValueError:
                return dict(
                    status="import-failure",
                    error=run.stderr[-2000:] or "Probe process returned no JSON",
                )
            return record

        if receipt.exists():
            saved = json.loads(receipt.read_text())
            current = (
                run_probe(root / saved["interpreter"])
                if (root / saved["interpreter"]).is_file()
                else {}
            )
            if (
                current.get("status") == "available"
                and current["distributions"] == saved["distributions"]
                and current["numpy"] == saved["numpy"]
            ):
                return {**saved, **current, "interpreter": saved["interpreter"]}
        start = time.monotonic()
        target = Path(tempfile.mkdtemp(prefix=key + "-", dir=root))
        python = target / "bin/python"
        wheels = target / "wheels"
        wheels.mkdir()
        download = [
            sys.executable,
            "-I",
            "-m",
            "pip",
            "download",
            "--only-binary=:all:",
            "--dest",
            str(wheels),
        ]
        if args.wheelhouse:
            download += ["--no-index", "--find-links", str(args.wheelhouse.resolve())]
        for command in (
            download + requirements,
            [sys.executable, "-I", "-m", "venv", str(target)],
            [
                str(python),
                "-I",
                "-m",
                "pip",
                "install",
                "--no-index",
                "--find-links",
                str(wheels),
                *requirements,
            ],
            [str(python), "-I", "-m", "pip", "check"],
        ):
            proc = subprocess.run(command, capture_output=True, text=True)
            if proc.returncode:
                failure = dict(
                    status="setup-failed",
                    command=command,
                    error=(proc.stderr or proc.stdout)[-4000:],
                    wheels=wheel_hashes(wheels),
                )
                (target / "failure.json").write_text(json.dumps(failure))
                return failure
        result = run_probe(python)
        result.update(
            interpreter=str(python.relative_to(root)),
            wheels=wheel_hashes(wheels),
            setup_s=time.monotonic() - start,
            disk_bytes=sum(p.stat().st_size for p in target.rglob("*") if p.is_file()),
        )
        if result["status"] == "available" and list(result["distributions"]) != [family]:
            result.update(status="wrong-distribution", expected=family)
        if result["status"] == "available":
            pending = receipt.with_suffix(".pending")
            pending.write_text(json.dumps(result, indent=2))
            pending.replace(receipt)
        else:
            (target / "failure.json").write_text(json.dumps(result, indent=2))
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("probe").add_argument("operation", choices=OPERATIONS)
    setup = commands.add_parser("setup")
    setup.add_argument("operation", choices=OPERATIONS)
    setup.add_argument("--root", required=True, type=Path)
    setup.add_argument("--wheelhouse", type=Path)
    setup.add_argument("--version")
    setup.add_argument("--numpy-version")
    setup.add_argument("--gui", action="store_true")
    args = parser.parse_args()
    if args.command == "setup":
        print("This installer will install OpenCV", file=sys.stderr, flush=True)
    report = probe(args.operation) if args.command == "probe" else prepare(args)
    print(json.dumps(report, indent=2))
    sys.exit(report["status"] != "available")
