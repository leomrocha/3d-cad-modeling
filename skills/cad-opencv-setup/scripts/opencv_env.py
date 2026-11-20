"""Probe this interpreter or prepare a verified, job-owned OpenCV environment."""

import argparse
import hashlib
import importlib.metadata as metadata
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time

FAMILIES = (
    "opencv-python-headless",
    "opencv-contrib-python-headless",
    "opencv-python",
    "opencv-contrib-python",
)
OPERATIONS = ("contours", "plane", "thinning")


def probe(operation):
    started = time.monotonic()
    wheels = {}
    for name in FAMILIES:
        try:
            wheels[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            pass
    result = dict(
        operation=operation,
        python=platform.python_version(),
        platform=platform.platform(),
        architecture=platform.machine(),
        interpreter=sys.executable,
        distributions=wheels,
        mixed=len(wheels) > 1,
    )
    try:
        import cv2
        import numpy as np
    except Exception as exc:
        result.update(
            status="absent"
            if isinstance(exc, ModuleNotFoundError) and exc.name == "cv2"
            else "import-failure",
            error=str(exc),
        )
        return result
    result.update(cv2=cv2.__version__, numpy=np.__version__)
    try:
        if operation == "contours":
            mask = np.zeros((80, 100), np.uint8)
            mask[10:70, 10:90] = 255
            cv2.circle(mask, (31, 44), 8, 0, -1)
            loops, tree = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            child = next(i for i, row in enumerate(tree[0]) if row[3] >= 0)
            center = cv2.fitEllipseAMS(loops[child])[0]
            result.update(loops=len(loops), center_px=center)
            ok = len(loops) == 2 and np.allclose(center, [31, 44], atol=0.01)
        elif operation == "plane":
            points = np.float64([[0, 0], [20, 0], [20, 10], [0, 10]])
            h, _ = cv2.findHomography(points, points * 2 + [3, 4])
            actual = cv2.perspectiveTransform(np.float64([[[7, 3]]]), h)[0, 0]
            result["held_out"] = actual.tolist()
            ok = np.allclose(actual, [17, 10])
        else:
            src = np.zeros((15, 15), np.uint8)
            src[2:13, 6:9] = 255
            dst = cv2.ximgproc.thinning(src)
            ok = np.count_nonzero(dst[7]) == 1 and dst[7, 7] == 255
        result["status"] = "tested" if ok else "incorrect-result"
    except AttributeError as exc:
        result.update(status="missing-operation", error=str(exc))
    except Exception as exc:
        result.update(status="operation-failed", error=str(exc))
    result["elapsed_s"] = time.monotonic() - started
    return result


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
                current.get("status") == "tested"
                and current["distributions"] == saved["distributions"]
                and current["numpy"] == saved["numpy"]
            ):
                return saved
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
        if result["status"] == "tested" and list(result["distributions"]) != [family]:
            result.update(status="wrong-distribution", expected=family)
        if result["status"] == "tested":
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
    report = probe(args.operation) if args.command == "probe" else prepare(args)
    print(json.dumps(report, indent=2))
    sys.exit(report["status"] != "tested")
