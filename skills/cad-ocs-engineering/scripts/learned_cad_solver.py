"""Solve a named 2D point sketch, optionally comparing a corrected revision (slvs 3.3)."""

import argparse
import hashlib
from importlib.metadata import version
import json
import math
from pathlib import Path


def identifier(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("A nonempty string identifier is required")
    return value


def finite(value):
    if (
        isinstance(value, bool)
        or not isinstance(value, (float, int))
        or not math.isfinite(value)
    ):
        raise ValueError("Expected a finite coordinate or dimension")
    return float(value)


def solve(sketch):
    import slvs

    if sketch["units"] != "mm" or not sketch["points"]:
        raise ValueError("Supply 2D points in mm")
    slvs.clear_sketch()
    try:
        plane = slvs.add_base_2d(1)
        points = {}
        for name, row in sketch["points"].items():
            identifier(name)
            if type(row.get("fixed", False)) is not bool:
                raise ValueError("fixed must be a boolean")
            x, y = map(finite, row["xy"])
            points[name] = slvs.add_point_2d(1 if row.get("fixed") else 2, x, y, plane)
        handles = {}
        for constraint in sketch["constraints"]:
            name = identifier(constraint["id"])
            if name in handles.values():
                raise ValueError("Duplicate constraint id " + name)
            left, right = constraint["points"]
            if left == right:
                raise ValueError("A constraint requires two distinct point IDs")
            a, b = points[left], points[right]
            kind = constraint["kind"]
            if kind == "distance":
                value = finite(constraint["mm"])
                if value <= 0:
                    raise ValueError("Use coincident for zero distance")
                item = slvs.distance(2, a, b, value, plane)
            elif kind == "coincident":
                item = slvs.coincident(2, a, b, plane)
            elif kind in ("horizontal", "vertical"):
                line = slvs.add_line_2d(2, a, b, plane)
                item = getattr(slvs, kind)(2, line, plane)
            else:
                raise ValueError("Unsupported point constraint: " + str(kind))
            handles[item["h"]] = name
        native, failed = slvs.solve_sketch(2, True)
        status = slvs.ResultFlag(native["result"]).name
        solved = status in {"OKAY", "REDUNDANT_OKAY"}
        return dict(
            status=status,
            degrees_of_freedom=native["dof"] if solved else None,
            failed_constraints=[handles[i] for i in failed],
            points_mm={
                key: [slvs.get_param_value(k) for k in pt["param"][:2]]
                for key, pt in points.items()
            }
            if solved
            else None,
        )
    finally:
        slvs.clear_sketch()


def read(path):
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def run(source, correction=None):
    before, sha = read(source)
    result = dict(
        solver="SolveSpace",
        version=version("slvs"),
        source_sha256=sha,
        before=solve(before),
    )
    if correction:
        after, new_sha = read(correction)
        if after.get("parent_sha256") != sha:
            raise ValueError("Corrected revision references another original")
        result.update(correction_sha256=new_sha, after=solve(after))
        previous = {item["id"]: item for item in before["constraints"]}
        revised = {item["id"]: item for item in after["constraints"]}
        result["changed_constraints"] = sorted(
            key
            for key in previous.keys() | revised.keys()
            if previous.get(key) != revised.get(key)
        )
        initial = result["before"]["points_mm"]
        result["displacement_reference"] = (
            "solved original" if initial is not None else "original input seeds"
        )
        if initial is None:
            initial = {key: row["xy"] for key, row in before["points"].items()}
        if result["after"]["points_mm"] is not None:
            result["displacement_mm"] = {
                key: math.dist(initial[key], xy)
                for key, xy in result["after"]["points_mm"].items()
                if key in initial
            }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("new_receipt", type=Path)
    parser.add_argument("--correction", type=Path)
    args = parser.parse_args()
    try:
        receipt = run(args.source, args.correction)
        with args.new_receipt.open("x") as f:
            json.dump(receipt, f, indent=2, allow_nan=False)
            f.write("\n")
    except ImportError as exc:
        parser.exit(
            2, f"Select an interpreter with the SolveSpace slvs binding: {exc}\n"
        )
