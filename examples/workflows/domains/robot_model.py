#!/usr/bin/env python3
"""Write a deliberately bounded MJCF robot tree from explicit model data.

Input JSON declares SI units, radians, a root body tree, source-linked joint and
inertial values, and separately identified visual/collision mesh assets. This
writer supports fixed, hinge and slide joints, one nested tree and mesh geoms.
It does not infer joints, calculate mass/inertia, synthesize actuators/controllers,
create closed-loop constraints, convert CAD assemblies or validate physical
accuracy. Collision meshes should already be simplified convex pieces where
needed. Mesh files remain external references; the adjacent manifest records the
exact file hashes and per-asset terms.

Each inertial record uses `frame: "body"` and a six-value `fullinertia_kg_m2`
tensor in MJCF order (ixx, iyy, izz, ixy, ixz, iyz). Do not supply an inertial
quaternion with this tensor; MJCF treats those attributes as mutually exclusive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def finite_vector(value: Any, size: int, label: str) -> list[float]:
    if not isinstance(value, list) or len(value) != size:
        raise ValueError(f"{label} must contain {size} explicit values")
    result = []
    for i, item in enumerate(value):
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            raise ValueError(f"{label}[{i}] must be numeric")
        item = float(item)
        if not math.isfinite(item):
            raise ValueError(f"{label}[{i}] must be finite")
        result.append(item)
    return result


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_inertia(values: list[float], name: str) -> None:
    ixx, iyy, izz, ixy, ixz, iyz = values
    minor2 = ixx * iyy - ixy * ixy
    determinant = (
        ixx * (iyy * izz - iyz * iyz)
        - ixy * (ixy * izz - iyz * ixz)
        + ixz * (ixy * iyz - iyy * ixz)
    )
    if ixx <= 0.0 or minor2 <= 0.0 or determinant <= 0.0:
        raise ValueError(f"{name}: full inertia matrix must be positive definite")


def vec_text(values: list[float]) -> str:
    return " ".join(format(x, ".17g") for x in values)


def build(data: dict[str, Any], input_dir: Path, output_xml: Path) -> tuple[ET.ElementTree, dict[str, Any]]:
    expected_units = {"length": "m", "angle": "rad", "mass": "kg", "inertia": "kg*m^2"}
    if data.get("units") != expected_units:
        raise ValueError(f"units must explicitly equal {expected_units}")
    model_data = data.get("model", {})
    name = model_data.get("name")
    if not name:
        raise ValueError("model.name is required")
    physics = model_data.get("physics", {})
    timestep = physics.get("timestep_s")
    if not isinstance(timestep, (int, float)) or isinstance(timestep, bool) or not math.isfinite(timestep) or timestep <= 0:
        raise ValueError("model.physics.timestep_s must be an explicit positive number")
    gravity = finite_vector(physics.get("gravity_m_s2"), 3, "model.physics.gravity_m_s2")

    assets = {}
    manifest_assets = []
    for asset in data.get("meshes", []):
        asset_id = asset.get("id")
        if not asset_id or asset_id in assets:
            raise ValueError("mesh asset IDs must be present and unique")
        if not asset.get("license") or not asset.get("license_url") or not asset.get("source_url"):
            raise ValueError(f"{asset_id}: license, license_url and source_url are required")
        expected_hash = asset.get("sha256")
        if not isinstance(expected_hash, str) or len(expected_hash) != 64:
            raise ValueError(f"{asset_id}: sha256 must be a 64-character source digest")
        source_path = Path(asset.get("file", ""))
        if not source_path.is_absolute():
            source_path = input_dir / source_path
        source_path = source_path.resolve(strict=True)
        actual_hash = sha256_file(source_path)
        if actual_hash.lower() != expected_hash.lower():
            raise ValueError(f"{asset_id}: mesh file SHA-256 does not match input record")
        scale = finite_vector(asset.get("scale"), 3, f"{asset_id}.scale")
        if any(v <= 0.0 for v in scale):
            raise ValueError(f"{asset_id}.scale values must be positive")
        role = asset.get("role")
        if role not in {"visual", "collision", "both"}:
            raise ValueError(f"{asset_id}.role must be visual or collision")
        assets[asset_id] = {**asset, "path": source_path, "scale_values": scale}
        manifest_assets.append({
            "id": asset_id,
            "source_url": asset["source_url"],
            "license": asset["license"],
            "license_url": asset["license_url"],
            "path": str(source_path),
            "sha256": actual_hash,
            "role": role,
        })

    root = ET.Element("mujoco", {"model": name})
    compiler = ET.SubElement(root, "compiler", {"angle": "radian", "inertiafromgeom": "false"})
    del compiler
    ET.SubElement(root, "option", {"timestep": format(float(timestep), ".17g"), "gravity": vec_text(gravity)})
    asset_el = ET.SubElement(root, "asset")
    for asset_id, asset in assets.items():
        # Absolute path keeps this reference exact; package relocation needs a reviewed relative-path rewrite.
        ET.SubElement(asset_el, "mesh", {
            "name": asset_id,
            "file": str(asset["path"]),
            "scale": vec_text(asset["scale_values"]),
        })
    worldbody = ET.SubElement(root, "worldbody")
    bodies = data.get("bodies")
    if not isinstance(bodies, list) or not bodies:
        raise ValueError("bodies must contain at least one explicit root body")
    seen = set()

    def append_body(parent_xml: ET.Element, body: dict[str, Any], root_body: bool = False) -> None:
        body_name = body.get("name")
        if not body_name or body_name in seen:
            raise ValueError("body names must be present and unique")
        seen.add(body_name)
        pos = finite_vector(body.get("pos_m"), 3, f"{body_name}.pos_m")
        quat = finite_vector(body.get("quat_wxyz"), 4, f"{body_name}.quat_wxyz")
        quat_norm = math.sqrt(sum(v * v for v in quat))
        if abs(quat_norm - 1.0) > 1e-6:
            raise ValueError(f"{body_name}.quat_wxyz must be unit length")
        body_el = ET.SubElement(parent_xml, "body", {
            "name": body_name,
            "pos": vec_text(pos),
            "quat": vec_text(quat),
        })
        joint = body.get("joint")
        if not isinstance(joint, dict) or joint.get("type") not in {"fixed", "hinge", "slide", "free"}:
            raise ValueError(f"{body_name}.joint must explicitly declare fixed, hinge, slide or free")
        joint_type = joint["type"]
        if root_body and joint_type not in {"fixed", "free"}:
            raise ValueError("root body joint must be fixed or free")
        if not root_body and joint_type == "free":
            raise ValueError("free joints are supported only on the root body")
        if not joint.get("source") or not joint.get("evidence_status"):
            raise ValueError(f"{body_name}.joint needs source and evidence_status")
        if joint_type not in {"fixed", "free"}:
            jname = joint.get("name")
            if not jname:
                raise ValueError(f"{body_name}: movable joint needs a name")
            jpos = finite_vector(joint.get("pos_m"), 3, f"{body_name}.joint.pos_m")
            axis = finite_vector(joint.get("axis"), 3, f"{body_name}.joint.axis")
            norm = math.sqrt(sum(v * v for v in axis))
            if norm == 0.0 or abs(norm - 1.0) > 1e-6:
                raise ValueError(f"{body_name}.joint.axis must be unit length")
            rng = finite_vector(joint.get("range"), 2, f"{body_name}.joint.range")
            if rng[0] >= rng[1]:
                raise ValueError(f"{body_name}.joint.range must increase")
            attrs = {"name": jname, "type": joint_type, "pos": vec_text(jpos), "axis": vec_text(axis),
                     "range": vec_text(rng), "limited": "true"}
            ET.SubElement(body_el, "joint", attrs)
        elif joint_type == "free":
            if not joint.get("name"):
                raise ValueError(f"{body_name}: free joint needs a name")
            ET.SubElement(body_el, "freejoint", {"name": joint["name"]})

        inertial = body.get("inertial")
        if not isinstance(inertial, dict):
            raise ValueError(f"{body_name}.inertial is required")
        for key in ("mass_source", "inertia_source", "evidence_status"):
            if not inertial.get(key):
                raise ValueError(f"{body_name}.inertial.{key} is required")
        mass = inertial.get("mass_kg")
        if not isinstance(mass, (int, float)) or isinstance(mass, bool) or not math.isfinite(mass) or mass <= 0:
            raise ValueError(f"{body_name}.inertial.mass_kg must be sourced and positive")
        ipos = finite_vector(inertial.get("pos_m"), 3, f"{body_name}.inertial.pos_m")
        # MJCF prohibits combining `fullinertia` with an inertial-frame quaternion.
        # This bounded writer accepts the full tensor in body axes only.
        if inertial.get("frame") != "body":
            raise ValueError(f"{body_name}.inertial.frame must be 'body' for fullinertia")
        inertia = finite_vector(inertial.get("fullinertia_kg_m2"), 6,
                                f"{body_name}.inertial.fullinertia_kg_m2")
        validate_inertia(inertia, body_name)
        ET.SubElement(body_el, "inertial", {
            "pos": vec_text(ipos), "mass": format(float(mass), ".17g"),
            "fullinertia": vec_text(inertia),
        })

        geometries = body.get("geometries", [])
        if not geometries:
            raise ValueError(f"{body_name}.geometries must reference visual and/or collision mesh assets")
        for index, geom in enumerate(geometries):
            asset_id = geom.get("mesh")
            if asset_id not in assets:
                raise ValueError(f"{body_name}: unknown mesh asset {asset_id!r}")
            role = geom.get("role")
            if role not in {"visual", "collision", "both"}:
                raise ValueError(f"{body_name}.geometries[{index}].role must be visual or collision")
            geom_pos = finite_vector(geom.get("pos_m"), 3,
                                    f"{body_name}.geometries[{index}].pos_m")
            geom_quat = finite_vector(geom.get("quat_wxyz"), 4,
                                      f"{body_name}.geometries[{index}].quat_wxyz")
            if abs(math.sqrt(sum(v * v for v in geom_quat)) - 1.0) > 1e-6:
                raise ValueError(f"{body_name}.geometries[{index}].quat_wxyz must be unit length")
            attrs = {"name": f"{body_name}_{index}_{role}", "type": "mesh", "mesh": asset_id,
                     "pos": vec_text(geom_pos), "quat": vec_text(geom_quat)}
            if role == "visual":
                attrs.update({"contype": "0", "conaffinity": "0", "group": "2"})
            ET.SubElement(body_el, "geom", attrs)
        for child in body.get("children", []):
            append_body(body_el, child)

    for body in bodies:
        append_body(worldbody, body, root_body=True)

    manifest = {
        "model": name,
        "units": expected_units,
        "source_json": None,
        "assets": manifest_assets,
        "validation": "XML well-formedness and input checks only; compile with MuJoCo and verify against physical evidence separately",
    }
    ET.indent(root, space="  ")
    return ET.ElementTree(root), manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_xml", type=Path)
    args = parser.parse_args()
    manifest_path = args.output_xml.with_suffix(args.output_xml.suffix + ".manifest.json")
    if args.output_xml.exists() or manifest_path.exists():
        raise FileExistsError("Refusing to overwrite MJCF XML or its asset manifest")
    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    tree, manifest = build(data, args.input_json.resolve().parent, args.output_xml)
    manifest["source_json"] = {
        "path": str(args.input_json.resolve()),
        "sha256": sha256_file(args.input_json.resolve()),
    }
    # Serialize in memory and parse it again for XML well-formedness before writing.
    xml_bytes = ET.tostring(tree.getroot(), encoding="utf-8", xml_declaration=True)
    ET.fromstring(xml_bytes)
    args.output_xml.parent.mkdir(parents=True, exist_ok=True)
    args.output_xml.write_bytes(xml_bytes)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
