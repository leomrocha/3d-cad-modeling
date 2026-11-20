"""Map decoded provider instances into a source image using its recorded pixel transform."""

import argparse
import hashlib
import io
import json
from pathlib import Path


def _warp_mask_numpy(mask, h, width, height):
    """Nearest-neighbour sampling in source pixel coordinates, with zero background."""
    import numpy as np

    inverse = np.linalg.inv(h)
    mapped = np.zeros((height, width), dtype=np.uint8)
    xs = np.arange(width)
    for top in range(0, height, 128):
        ys = np.arange(top, min(top + 128, height))[:, None]
        w = inverse[2, 0] * xs + inverse[2, 1] * ys + inverse[2, 2]
        with np.errstate(divide="ignore", invalid="ignore"):
            mx = np.rint((inverse[0, 0] * xs + inverse[0, 1] * ys + inverse[0, 2]) / w)
            my = np.rint((inverse[1, 0] * xs + inverse[1, 1] * ys + inverse[1, 2]) / w)
        inside = (mx >= 0) & (my >= 0) & (mx < mask.shape[1]) & (my < mask.shape[0])
        mapped[top:top + len(ys)][inside] = mask[my[inside].astype(int), mx[inside].astype(int)]
    return mapped


def normalize(raw, receipt):
    try:
        import cv2
    except (ImportError, OSError):
        cv2 = None
        from PIL import Image, ImageDraw

    import numpy as np
    from raster_features import projection

    sha = hashlib.sha256(raw).hexdigest()
    if receipt["source_sha256"] != sha:
        raise ValueError("Response references another image revision")
    if cv2 is None:
        with Image.open(io.BytesIO(raw)) as image:
            overlay = image.convert("L").convert("RGB")
        width, height = overlay.size
    else:
        gray = cv2.imdecode(np.frombuffer(raw, np.uint8),
                            cv2.IMREAD_GRAYSCALE | cv2.IMREAD_IGNORE_ORIENTATION)
        if gray is None:
            raise ValueError("Invalid original image")
        height, width = gray.shape
        overlay = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    h = np.array(receipt["source_from_provider"], dtype=float)
    if h.shape != (3, 3) or not np.isfinite(h).all() or np.linalg.matrix_rank(h) != 3:
        raise ValueError("Invalid provider frame")
    size = receipt["provider_size_px"]
    if len(size) != 2 or any(type(i) != int or i < 1 for i in size):
        raise ValueError("Invalid provider size")
    items, ids = [], set()
    for instance in receipt["instances"]:
        key, kind = instance["id"], instance["kind"]
        if not isinstance(key, str) or not key or key in ids:
            raise ValueError("Unique instance identity required")
        ids.add(key)
        row = dict(id=key, kind=kind)
        if kind == "mask":
            mask = np.asarray(instance["mask"])
            if mask.shape != tuple(reversed(size)) or not np.isin(mask, [0, 1]).all():
                raise ValueError("Expected binary mask in declared provider frame")
            if cv2 is None:
                mapped = _warp_mask_numpy(mask, h, width, height)
                overlay.paste((0, 170, 0), mask=Image.fromarray(mapped * 255))
            else:
                mapped = cv2.warpPerspective(
                    mask.astype(np.uint8), h, (width, height), flags=cv2.INTER_NEAREST
                )
                overlay[mapped != 0] = (0, 170, 0)
            row["mask"] = mapped.tolist()
        elif kind in ("box", "polygon", "point", "text"):
            points = np.asarray(instance["points"], dtype=float)
            if (
                points.ndim != 2
                or points.shape[1] != 2
                or (kind in ("box", "text") and len(points) != 4)
                or (kind == "point" and len(points) != 1)
                or (kind == "polygon" and len(points) < 3)
            ):
                raise ValueError("Invalid pixel coordinates for " + kind)
            mapped = projection(points, h)
            row["points_px"] = mapped.tolist()
            if kind == "text":
                row["text"] = instance["text"]
            pixels = np.int32(np.rint(mapped))
            if cv2 is None:
                draw = ImageDraw.Draw(overlay)
                points = [tuple(point) for point in pixels.tolist()]
                if kind != "point":
                    draw.line([*points, points[0]], fill=(255, 0, 0))
                draw.point(points[0], fill=(0, 0, 255))
            else:
                cv2.polylines(overlay, [pixels], kind != "point", (0, 0, 255), 1)
                cv2.circle(overlay, tuple(pixels[0]), 1, (255, 0, 0), -1)
        else:
            raise ValueError("Unsupported observation: " + kind)
        items.append(row)
    if cv2 is None:
        stream = io.BytesIO()
        overlay.save(stream, format="PNG")
        overlay_bytes = stream.getvalue()
    else:
        overlay_bytes = cv2.imencode(".png", overlay)[1].tobytes()
    return dict(
        source_sha256=sha,
        size_px=[width, height],
        instances=items,
        provider=receipt["provider"],
        source_from_provider=h.tolist(),
        parent_response_sha256=receipt.get("parent_response_sha256"),
    ), overlay_bytes


def leader_candidates(end_px, features, tolerance_px):
    """Distance to contour segments in the source plane, including the closing edge."""
    import numpy as np

    end = np.array(end_px, dtype=float)
    if (
        end.shape != (2,)
        or not np.isfinite(end).all()
        or not np.isfinite(tolerance_px)
        or tolerance_px < 0
    ):
        raise ValueError("Finite endpoint and nonnegative pick tolerance required")
    result = []
    for row in features:
        a = np.asarray(row["samples_px"], dtype=float)
        v = np.roll(a, -1, axis=0) - a
        diff = end - a
        denom = (v * v).sum(axis=1)
        t = np.divide(
            (diff * v).sum(axis=1), denom, out=np.zeros_like(denom), where=denom > 0
        ).clip(0, 1)
        distance = np.linalg.norm(diff - v * t[:, None], axis=1).min()
        if distance <= tolerance_px:
            result.append(dict(id=row["id"], distance_px=float(distance)))
    return result


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    for field in ("source", "receipt", "output"):
        p.add_argument(field, type=Path)
    args = p.parse_args()
    receipt = args.receipt.read_bytes()
    result, overlay = normalize(args.source.read_bytes(), json.loads(receipt))
    result["receipt_sha256"] = hashlib.sha256(receipt).hexdigest()
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "observations.json").write_text(json.dumps(result, allow_nan=False))
    (args.output / "overlay.png").write_bytes(overlay)
