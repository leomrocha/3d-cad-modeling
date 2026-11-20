"""Check the dependencies of one OpenCV operation in this interpreter."""

import argparse
import importlib.metadata as metadata
import json
import platform
import sys

FAMILIES = (
    "opencv-python-headless",
    "opencv-contrib-python-headless",
    "opencv-python",
    "opencv-contrib-python",
)
OPERATIONS = ("contours", "plane", "thinning")


def probe(operation):
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
        required = {
            "contours": ("findContours", "fitEllipseAMS"),
            "plane": ("findHomography", "perspectiveTransform"),
            "thinning": ("ximgproc.thinning",),
        }
        for name in required[operation]:
            value = cv2
            for part in name.split("."):
                value = getattr(value, part)
            if not callable(value):
                raise AttributeError(f"Missing OpenCV function: {name}")
        result["status"] = "available"
    except AttributeError as exc:
        result.update(status="missing-operation", error=str(exc))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=OPERATIONS)
    result = probe(parser.parse_args().operation)
    print(json.dumps(result))
    sys.exit(result["status"] != "available")
