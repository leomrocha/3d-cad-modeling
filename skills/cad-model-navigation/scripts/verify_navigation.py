"""Compare an intended occurrence inventory with an independently reopened one."""
import argparse
import json
import math
from pathlib import Path


def index(document):
    rows = document["objects"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("objects must be a nonempty list")
    indexed = {}
    for row in rows:
        for field in ("id", "definition", "label", "role", "layer"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"{row.get('id')}: missing {field}")
        key = row["id"]
        if key in indexed:
            raise ValueError(f"{key}: duplicate occurrence ID")
        indexed[key] = row
    for key in indexed:
        current, seen = key, set()
        while current is not None:
            if current not in indexed or current in seen:
                raise ValueError(f"{key}: unresolved or cyclic parent {current}")
            seen.add(current)
            current = indexed[current]["parent"]
    return indexed


def equal(left, right):
    """JSON values with exact numeric equality, keeping booleans distinct."""
    if type(left) in (float, int) and type(right) in (float, int):
        return left == right and all(type(x) is int or math.isfinite(x) for x in (left, right))
    if type(left) is not type(right):
        return False
    if isinstance(left, list):
        return len(left) == len(right) and all(equal(x, y) for x, y in zip(left, right))
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(equal(left[k], right[k]) for k in left)
    return left == right


def compare(expected, observed):
    before, after = index(expected), index(observed)
    errors = []
    for key in sorted(before.keys() | after.keys()):
        if key not in before or key not in after:
            errors.append({"id": key, "error": "unexpected" if key in after else "missing"})
            continue
        for field, value in before[key].items():
            if field not in after[key] or not equal(value, after[key][field]):
                errors.append({"id": key, "field": field, "expected": value,
                               "observed": after[key].get(field), "present": field in after[key]})
    return {"result": "FAIL" if errors else "PASS", "objects": len(after), "differences": errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", type=Path)
    parser.add_argument("reopened", type=Path)
    args = parser.parse_args()
    try:
        result = compare(json.loads(args.expected.read_text()), json.loads(args.reopened.read_text()))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        result = {"result": "FAIL", "error": str(error)}
    print(json.dumps(result, indent=2))
    raise SystemExit(result["result"] != "PASS")
