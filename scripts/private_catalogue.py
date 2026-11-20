"""Build a versioned private CAD Models snapshot with its original build.py."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

FORMATS = set(
    ".dwg .dxf .step .stp .iges .igs .stl .obj .3mf .blend .fcstd .brep .ifc .glb .gltf".split()
)


def prepare(source, destination, builder, python, metadata):
    source, destination = source.resolve(), destination.resolve()
    if destination.is_relative_to(source):
        raise ValueError("Store snapshots outside the input tree")
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination) as temporary:
        stage = Path(temporary)
        data = stage / "data"
        packages = data / "packages"
        packages.mkdir(parents=True)
        rows, used, observed = [], set(), set()
        for asset in sorted(source.rglob("*")):
            if asset.suffix.lower() not in FORMATS or not asset.is_file():
                continue
            if asset.resolve() != asset or not asset.stat().st_size:
                raise ValueError(f"Redirected or empty asset: {asset.name}")
            relative = asset.relative_to(source)
            observed.add(relative.as_posix())
            extra = metadata.get(relative.as_posix(), {})
            key = extra.get("id") or re.sub(
                "[^a-z0-9]+", "-", relative.as_posix().lower()
            ).strip("-")
            if key in used or not re.fullmatch("[a-z0-9-]+", key):
                raise ValueError(f"Ambiguous or invalid catalogue ID: {key}")
            used.add(key)
            target = Path("models", key, asset.name)
            folder = packages / target.parent
            folder.mkdir(parents=True)
            shutil.copyfile(asset, packages / target)
            with (packages / target).open("rb") as stream:
                sha = hashlib.file_digest(stream, "sha256").hexdigest()
            with asset.open("rb") as stream:
                if hashlib.file_digest(stream, "sha256").hexdigest() != sha:
                    raise ValueError(f"Source changed during snapshot: {relative}")
            role = extra.get(
                "role", "drawing" if asset.suffix.lower() == ".dxf" else "candidate"
            )
            source_info = dict(
                path=relative.as_posix(),
                sha256=sha,
                role=role,
                units=extra.get("units"),
                variant=extra.get("variant", {}),
                evidence=extra.get("evidence"),
            )
            (packages / target.with_suffix(".md")).write_text(
                json.dumps(source_info, indent=2)
            )
            rows.append(
                dict(
                    id=key,
                    name=extra.get("name", asset.stem),
                    subject="local parts",
                    kind=role,
                    description=extra.get("description", relative.as_posix()),
                    private_source=source_info,
                    needs_information=role == "candidate" or not extra.get("units"),
                    tags=extra.get("tags", []),
                    aliases=extra.get("aliases", []),
                    materials=None,
                    standards=extra.get("standards"),
                    dimensions=extra.get("dimensions"),
                    file=target.as_posix(),
                    package_assets=[
                        target.as_posix(),
                        target.with_suffix(".md").as_posix(),
                    ],
                )
            )
        missing = set(metadata) - observed
        if missing or not rows:
            raise ValueError(
                f"Missing listed assets or empty source: {sorted(missing)}"
            )
        pilot = data / "pilot.json"
        pilot.write_text(json.dumps(rows, sort_keys=True))
        subprocess.run([python, builder.resolve()], cwd=stage, check=True)
        catalogue = data / "catalogue.json"
        indexed = json.loads(catalogue.read_text())
        for row in indexed:
            row.update(download=None, companion=None, repo_folder=None)
        catalogue.write_text(json.dumps(indexed, ensure_ascii=False))
        snapshot = (
            destination
            / hashlib.sha256((data / "catalogue.json").read_bytes()).hexdigest()
        )
        try:
            data.rename(snapshot)
        except OSError:
            if (
                not snapshot.is_dir()
                or (data / "catalogue.json").read_bytes()
                != (snapshot / "catalogue.json").read_bytes()
            ):
                raise
        return snapshot


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "destination", "builder"):
        p.add_argument(name, type=Path)
    p.add_argument(
        "--python",
        default=sys.executable,
        help="Interpreter with the upstream builder dependencies",
    )
    p.add_argument(
        "--metadata", type=Path, help="Object keyed by source-relative CAD filename"
    )
    args = p.parse_args()
    print(
        prepare(
            args.source,
            args.destination,
            args.builder,
            args.python,
            json.loads(args.metadata.read_text()) if args.metadata else {},
        )
    )
