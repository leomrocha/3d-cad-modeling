"""Request an editable CAD sequence from a user-selected chat-completions endpoint."""

import argparse
import base64
import hashlib
import http.client
import json
import math
import os
from pathlib import Path
from urllib.parse import urlsplit

SYSTEM = """Translate the user's engineering description into geometry. Return a JSON array of extrusion operations in order. Begin by adding the body, then cut holes. Units are millimetres. Use exactly these keys and formats:
rectangle: {"op":"add","shape":"rectangle","center":[x,y,z],"width":number,"height":number,"depth":number}
circle: {"op":"cut","shape":"circle","center":[x,y,z],"diameter":number,"depth":number}
Each op may be add, cut or intersect. Each profile is centered at the specified XYZ and extruded along +Z from there. Use negative depth for the opposite direction. A through-hole in a plate starting at z=0 has positive depth equal to the plate thickness. Return JSON only. Produce an empty array when this vocabulary cannot describe the requested shape."""


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def chat(endpoint, request, key, timeout):
    url = urlsplit(endpoint)
    if (
        url.scheme not in ("http", "https")
        or not url.hostname
        or url.username
        or url.password
        or url.query
        or url.fragment
    ):
        raise ValueError(
            "Supply a full HTTP(S) chat-completions URL without credentials, query or fragment"
        )
    if (
        key
        and url.scheme != "https"
        and url.hostname not in ("localhost", "127.0.0.1", "::1")
    ):
        raise ValueError("A bearer token requires HTTPS or a loopback address")
    cls = (
        http.client.HTTPSConnection
        if url.scheme == "https"
        else http.client.HTTPConnection
    )
    conn = cls(url.hostname, url.port, timeout=timeout)
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = "Bearer " + key
    try:
        conn.request("POST", url.path or "/", json.dumps(request).encode(), headers)
        response = conn.getresponse()
        raw = response.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError("Response exceeds 8 MiB")
        return response.status, raw
    finally:
        conn.close()


def expand(content, model, sources):
    if not isinstance(content, str):
        raise ValueError("Expected a text response containing the feature array")
    text = content.strip()
    if text.startswith("```json\n") and text.endswith("\n```"):
        text = text[8:-4]
    items = json.loads(text)
    if not isinstance(items, list) or not 1 <= len(items) <= 256:
        raise ValueError(
            "Model must provide a nonempty array with at most 256 operations"
        )
    params, features = {}, []
    for i, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError("Expected one object per feature")
        name = f"feature{i}"

        def parameter(field, value):
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError(f"Expected a finite number for {name}.{field}")
            pid = name + "_" + field
            params[pid] = dict(value_mm=value, basis="inferred", source="response")
            return pid

        shape = item["shape"]
        profile = {"kind": shape}
        if shape == "rectangle":
            fields = ["width", "height"]
        elif shape == "circle":
            fields = ["diameter"]
        else:
            raise ValueError("Unsupported generated profile: " + str(shape))
        if set(item) != {"op", "shape", "center", "depth", *fields}:
            raise ValueError("Unexpected or missing fields on " + name)
        x, y, z = item["center"]
        for field in fields:
            profile[field] = parameter(field, item[field])
            if item[field] <= 0:
                raise ValueError("Expected positive " + field)
        if item["op"] not in ("add", "cut", "intersect") or (
            i == 1 and item["op"] != "add"
        ):
            raise ValueError("First feature must add one solid")
        features.append(
            dict(
                id=name,
                plane="XY",
                origin_xyz=[parameter("x", x), parameter("y", y), parameter("z", z)],
                profile=profile,
                depth=parameter("depth", item["depth"]),
                operation=item["op"],
            )
        )
    return dict(
        model=model, units="mm", sources=sources, parameters=params, features=features
    )


def run(args):
    key = os.environ[args.key_env] if args.key_env else None
    prompt = args.prompt.read_bytes()
    sources = {"prompt": {"sha256": sha(prompt)}}
    text = prompt.decode().strip()
    if not text:
        raise ValueError("The engineering prompt is empty")
    content = [{"type": "text", "text": text}]
    for index, path in enumerate(args.image, 1):
        raw = path.read_bytes()
        if raw.startswith(b"\x89PNG\r\n\x1a\n"):
            mime = "image/png"
        elif raw.startswith(b"\xff\xd8\xff"):
            mime = "image/jpeg"
        else:
            raise ValueError("Supply original PNG or JPEG views")
        sources[f"view{index}"] = {"sha256": sha(raw)}
        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": "data:" + mime + ";base64," + base64.b64encode(raw).decode()
                },
            }
        )
    payload = dict(
        model=args.model,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": content if args.image else text},
        ],
    )
    args.output.mkdir()
    (args.output / "inputs.json").write_text(
        json.dumps(
            dict(requested_model=args.model, sources=sources, instruction=SYSTEM),
            indent=2,
        )
        + "\n"
    )
    status, raw = chat(args.endpoint, payload, key, args.timeout)
    (args.output / "response.json").write_bytes(raw)
    if status != 200:
        raise ValueError(f"Provider returned HTTP {status}; response retained")
    envelope = json.loads(raw)
    if (
        not isinstance(envelope, dict)
        or not isinstance(envelope.get("choices"), list)
        or not envelope["choices"]
    ):
        raise ValueError("No chat completion was returned")
    model = envelope.get("model") or args.model
    sources["response"] = {"sha256": sha(raw)}
    sequence = expand(envelope["choices"][0]["message"]["content"], model, sources)
    (args.output / "sequence.json").write_text(
        json.dumps(sequence, indent=2, allow_nan=False) + "\n"
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("endpoint")
    p.add_argument("model")
    p.add_argument("prompt", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--image", action="append", type=Path, default=[])
    p.add_argument(
        "--key-env", help="Read a bearer token from this environment variable"
    )
    p.add_argument("--timeout", type=float, default=180)
    try:
        run(p.parse_args())
    except (OSError, KeyError, ValueError, TypeError, http.client.HTTPException) as exc:
        p.exit(2, str(exc) + "\n")
