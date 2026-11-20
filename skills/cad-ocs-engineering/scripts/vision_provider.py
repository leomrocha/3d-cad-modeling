"""Call a selected JSON vision endpoint or decode its saved response for source intake."""

import argparse
import base64
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError
from urllib.parse import urlencode, urlunsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener
from local_model_runtime import inference_endpoint, offline_model_libraries
from xml.etree.ElementTree import Element, SubElement, tostring

IDENTITY = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def _box(values, size, units):
    limits = {"pixels": size, "normalized": (1, 1), "normalized1000": (1000, 1000)}[
        units
    ]
    x1, y1, x2, y2 = values
    if not (0 <= x1 < x2 <= limits[0] and 0 <= y1 < y2 <= limits[1]):
        raise ValueError("Box outside declared frame or corners unordered")
    x1, x2 = [x * size[0] / limits[0] for x in (x1, x2)]
    y1, y2 = [y * size[1] / limits[1] for y in (y1, y2)]
    return [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]


def _moondream(response, size):
    import cairosvg
    import numpy as np
    from PIL import Image

    box = response["bbox"]
    path = response["path"]
    if not isinstance(path, str) or not re.fullmatch(
        r"[MmLlHhVvCcSsQqTtAaZzEe0-9+.,\s-]+", path
    ):
        raise ValueError("Expected SVG path data")
    a, _, b, _ = _box(
        [box[k] for k in ("x_min", "y_min", "x_max", "y_max")], size, "normalized"
    )
    svg = Element(
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        width=str(size[0]),
        height=str(size[1]),
    )
    SubElement(
        svg,
        "path",
        d=path,
        fill="white",
        transform=f"translate({a[0]} {a[1]}) scale({b[0] - a[0]} {b[1] - a[1]})",
    )
    png = cairosvg.svg2png(bytestring=tostring(svg))
    alpha = np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"))[:, :, 3]
    return (alpha >= 128).astype("uint8").tolist()


def _select(response, keys):
    for key in keys:
        response = response[key]
    return response


def evaluate_lisa(
    model,
    image_clip,
    image_tensor,
    input_ids,
    resized_hw,
    original_hw,
    tokenizer,
    max_new_tokens=512,
):
    """Bridge an already loaded LISA runtime with upstream preprocessing and tokenizer."""
    import torch

    with torch.inference_mode():
        token_ids, batches = model.evaluate(
            image_clip,
            image_tensor,
            input_ids,
            [resized_hw],
            [original_hw],
            max_new_tokens=max_new_tokens,
            tokenizer=tokenizer,
        )
    if len(batches) != 1:
        raise ValueError("One source image per LISA receipt")
    masks = batches[0].detach().cpu()
    if masks.ndim != 3 or tuple(masks.shape[1:]) != tuple(original_hw):
        raise ValueError("Unexpected LISA mask frame")
    return {
        "token_ids": token_ids[0].detach().cpu().tolist(),
        "pred_masks": masks.tolist(),
    }


def decode(response, config, source_hash, source_size):
    import numpy as np

    model = config["model"]
    if not isinstance(model, str) or not model.strip():
        raise ValueError("Provide the deployed model identity")
    mode = config["format"]
    selected = _select(response, config.get("response_path", []))
    size = config.get("provider_size_px", list(source_size))
    if (
        not isinstance(size, list)
        or len(size) != 2
        or any(type(v) != int or v <= 0 for v in size)
        or math.prod(size) > 32000000
    ):
        raise ValueError("Invalid provider frame")
    if list(source_size) != size and "source_from_provider" not in config:
        raise ValueError("Provide the inverse resize or crop transform")
    matrix = np.asarray(config.get("source_from_provider", IDENTITY), dtype=float)
    if (
        matrix.shape != (3, 3)
        or not np.isfinite(matrix).all()
        or np.linalg.matrix_rank(matrix) != 3
    ):
        raise ValueError("Invalid provider-to-source transform")
    instances = []
    if mode == "instances":
        if not isinstance(selected, list):
            raise ValueError("Expected a list of named decoded instances")
        instances = selected
    elif mode == "moondream":
        instances.append(
            dict(id=config["instance_id"], kind="mask", mask=_moondream(selected, size))
        )
    elif mode == "lisa":
        # One source image per request. Select its N×H×W tensor by response_path.
        masks = np.asarray(selected)
        if masks.size:
            if (
                masks.ndim != 3
                or masks.shape[1:] != (size[1], size[0])
                or not np.isfinite(masks).all()
            ):
                raise ValueError(
                    "Expected one finite H×W logit plane per referenced instance"
                )
            for index, mask in enumerate(masks):
                instances.append(
                    dict(
                        id=f"segment-{index + 1}",
                        kind="mask",
                        mask=(mask > 0).astype("uint8").tolist(),
                    )
                )
    elif mode in ("qwen", "yolo"):
        if mode == "qwen" and isinstance(selected, str):
            content = selected.strip()
            if content.startswith("```"):
                match = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", content, re.S)
                if not match:
                    raise ValueError("Incomplete fenced JSON detections")
                content = match.group(1)
            selected = json.loads(content)
        if not isinstance(selected, list):
            raise ValueError("Expected an array of detections")
        units = config["coordinate_units"]
        for index, row in enumerate(selected):
            box = (
                row["bbox_2d"]
                if mode == "qwen"
                else [row["box"][key] for key in ("x1", "y1", "x2", "y2")]
            )
            points = _box(box, size, units)
            label = row["label" if mode == "qwen" else "name"]
            if not isinstance(label, str) or not label:
                raise ValueError("Expected a detection label")
            identifier = f"{label}-{index + 1}"
            instances.append(dict(id=identifier, kind="box", points=points))
            if mode == "yolo" and "segments" in row:
                xs, ys = row["segments"]["x"], row["segments"]["y"]
                polygon = np.asarray(list(zip(xs, ys, strict=True)), dtype=float)
                if (
                    polygon.ndim != 2
                    or len(polygon) < 3
                    or not np.isfinite(polygon).all()
                ):
                    raise ValueError("Invalid YOLO contour")
                if units != "pixels":
                    polygon = (
                        polygon
                        * np.asarray(size)
                        / (1000 if units == "normalized1000" else 1)
                    )
                if (polygon < 0).any() or (polygon > np.asarray(size)).any():
                    raise ValueError("Contour outside declared frame")
                instances.append(
                    dict(
                        id=identifier + "-outline",
                        kind="polygon",
                        points=polygon.tolist(),
                    )
                )
    else:
        raise ValueError("Choose instances, qwen, yolo, moondream or lisa")
    return dict(
        provider=model,
        source_sha256=source_hash,
        provider_size_px=size,
        source_from_provider=matrix.tolist(),
        instances=instances,
    )


def fill_payload(value, variables):
    if isinstance(value, dict):
        return {k: fill_payload(v, variables) for k, v in value.items()}
    if isinstance(value, list):
        return [fill_payload(v, variables) for v in value]
    return variables.get(value, value) if isinstance(value, str) else value


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Use the selected deployment's final endpoint URL")


def local_yolo_response(source, checkpoint):
    """Run an existing Ultralytics checkpoint and use the same rows as a YOLO server."""
    checkpoint = Path(checkpoint).resolve(strict=True)
    if not checkpoint.is_file() or checkpoint.suffix.lower() != ".pt":
        raise ValueError("Select an existing local YOLO .pt checkpoint")
    offline_model_libraries()
    os.environ.update(YOLO_OFFLINE="true", YOLO_AUTOINSTALL="false")
    from PIL import Image
    from ultralytics import YOLO
    from ultralytics.utils.checks import check_yolov5u_filename

    selected = check_yolov5u_filename(str(checkpoint), verbose=False)
    if selected != str(checkpoint):
        raise ValueError(
            "The YOLO runtime maps this filename to a different checkpoint"
        )
    model = YOLO(str(checkpoint))
    if model.task not in ("detect", "segment"):
        raise ValueError("Select a YOLO detection or segmentation checkpoint")
    with Image.open(source) as image:
        (result,) = model.predict(image.convert("RGB"), device="cpu", verbose=False)
    return json.dumps(result.summary(normalize=False, decimals=4)).encode()


def run(source, config, output, saved=None, timeout=120):
    import numpy  # Source-frame normalization uses NumPy.
    from PIL import Image
    from image_observations import normalize

    if config.get("format") == "moondream":
        import cairosvg

    if output.exists():
        raise FileExistsError(output)
    raw = source.read_bytes()
    source_hash = hashlib.sha256(raw).hexdigest()
    with Image.open(io.BytesIO(raw)) as image:
        source_size = image.size
        mime = Image.MIME[image.format]
    if saved:
        if config.get("source_sha256") != source_hash:
            raise ValueError(
                "Saved response requires a matching source_sha256 in its input contract"
            )
        output.mkdir(parents=True, exist_ok=False)
        original = saved.read_bytes()
        elapsed = None
    elif "local_checkpoint" in config:
        if (
            config.get("url")
            or config.get("format") != "yolo"
            or config.get("coordinate_units") != "pixels"
        ):
            raise ValueError("Local YOLO requires format yolo and pixel coordinates")
        if config.get("source_sha256", source_hash) != source_hash:
            raise ValueError("The configured image revision has changed")
        start = time.monotonic()
        original = local_yolo_response(io.BytesIO(raw), config["local_checkpoint"])
        elapsed = time.monotonic() - start
        output.mkdir(parents=True, exist_ok=False)
    else:
        if config.get("source_sha256", source_hash) != source_hash:
            raise ValueError("The configured image revision has changed")
        parsed = inference_endpoint(config["url"])
        url = urlunsplit(parsed)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if "auth" in config:
            auth = config["auth"]
            headers[auth["header"]] = auth.get("prefix", "") + os.environ[auth["env"]]
        query_secrets = config.get("query_from_env", {})
        if query_secrets:
            extra = urlencode({k: os.environ[env] for k, env in query_secrets.items()})
            query = parsed.query + "&" + extra if parsed.query else extra
            url = urlunsplit(parsed._replace(query=query))
        b64 = base64.b64encode(raw).decode("ascii")
        payload = fill_payload(
            config["payload"],
            {
                "$image_data_url": f"data:{mime};base64,{b64}",
                "$image_base64": b64,
                "$model": config["model"],
                "$prompt": config.get("prompt", ""),
            },
        )
        request = Request(
            url, data=json.dumps(payload).encode(), headers=headers, method="POST"
        )
        output.mkdir(parents=True, exist_ok=False)
        start = time.monotonic()
        try:
            with build_opener(ProxyHandler({}), _NoRedirect).open(
                request, timeout=timeout
            ) as connection:
                original = connection.read(64 * 1024 * 1024 + 1)
        except HTTPError as error:
            raise ValueError(f"Vision endpoint returned HTTP {error.code}") from None
        if len(original) > 64 * 1024 * 1024:
            raise ValueError("JSON response exceeds 64 MiB")
        elapsed = time.monotonic() - start
    (output / "response.json").write_bytes(original)
    try:
        receipt = decode(json.loads(original), config, source_hash, source_size)
        normalized, overlay = normalize(raw, receipt)
    except (ValueError, KeyError, TypeError, IndexError) as error:
        (output / "failure.json").write_text(
            json.dumps(
                {
                    "stage": "decode",
                    "error": str(error),
                    "source_sha256": source_hash,
                    "request_seconds": elapsed,
                }
            )
        )
        raise
    receipt["response_sha256"] = hashlib.sha256(original).hexdigest()
    receipt["request_seconds"] = elapsed
    receipt["mode"] = "response file" if saved else "HTTP POST"
    if not saved and "local_checkpoint" in config:
        receipt["mode"] = "local YOLO"
    receipt["format"] = config["format"]
    receipt["response_path"] = config.get("response_path", [])
    normalized["response_sha256"] = receipt["response_sha256"]
    for name, value in [("receipt.json", receipt), ("observations.json", normalized)]:
        (output / name).write_text(
            json.dumps(value, allow_nan=False, separators=(",", ":"))
        )
    (output / "overlay.png").write_bytes(overlay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "config", "new_output"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--response", type=Path)
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()
    run(
        args.source,
        json.loads(args.config.read_text()),
        args.new_output,
        args.response,
        args.timeout,
    )
