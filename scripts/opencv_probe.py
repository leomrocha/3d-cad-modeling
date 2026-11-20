"""Exercise one OpenCV operation in this interpreter."""

import argparse
import importlib.metadata as metadata
import json
import platform
import sys
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=OPERATIONS)
    result = probe(parser.parse_args().operation)
    print(json.dumps(result))
    sys.exit(result["status"] != "tested")
