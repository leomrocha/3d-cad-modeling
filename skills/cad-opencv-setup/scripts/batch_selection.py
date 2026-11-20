"""Resolve measured CAD inventory against an immutable batch selection."""
import math
import json
from collections import Counter

from step_placements import apply, classify_hand, dot, eye, multiply, unit

REFERENCE_KINDS = {"vertex", "edge", "outside border", "inside border", "centreline",
                   "axis", "plane", "face", "existing feature"}


def vector(value):
    if len(value) != 3 or any(type(n) not in (float, int) or not math.isfinite(n) for n in value):
        raise ValueError("Expected a finite 3-vector")
    return list(value)


def inventory(snapshot):
    """Expand reached definitions into unique occurrence paths, with local identity at every level."""
    result = {}

    def visit(owner, path, chain, transform, active):
        if owner in active or len(active) >= 128:
            raise ValueError("Cyclic or excessively deep assembly")
        children = snapshot["definitions"][owner]
        def signature(child):
            return json.dumps([child.get(k) for k in ("name", "kind", "definition", "geometry")]
                              + [child.get("matrix", eye())], sort_keys=True, allow_nan=False)
        counts = Counter(signature(child) for child in children)
        for child in children:
            handle = child["id"]
            if not isinstance(handle, str) or not handle or "/" in handle:
                raise ValueError("Expected a native ID without slash")
            key = path + (handle,)
            if key in result or len(result) >= 100000:
                raise ValueError("Duplicate native sibling ID or occurrence limit exceeded")
            matrix = child.get("matrix", eye())
            classify_hand(matrix)
            world = multiply(transform, matrix)
            geometry = child["geometry"]
            if not isinstance(geometry, dict) or not geometry:
                raise ValueError("Local geometry evidence required")
            segment = dict(id=handle, owner=owner, name=child["name"], kind=child["kind"],
                           definition=child.get("definition"), geometry=geometry, matrix=matrix,
                           unique_in_owner=counts[signature(child)] == 1)
            identity = chain + [segment]
            result[key] = dict(path=list(key), chain=identity, matrix=world, element=child)
            if segment["definition"] is not None:
                visit(segment["definition"], key, identity, world, active | {owner})
    visit(snapshot["root"], (), [], eye(), set())
    return result


def rebound(record, candidates):
    """Resolve one level at a time, checking owner, definition, transform and local geometry."""
    path = ()
    for recorded in record["chain"]:
        same = path + (recorded["id"],)
        siblings = [key for key in candidates if key[:-1] == path]
        def matches(key):
            current = candidates[key]["chain"][-1]
            return all(current[field] == value for field, value in recorded.items() if field not in ("id", "unique_in_owner"))
        if same in candidates and matches(same):
            path = same
        else:
            matches_found = [key for key in siblings if matches(key)]
            if len(matches_found) != 1 or not recorded["unique_in_owner"]:
                raise ValueError("Missing or ambiguous reopened occurrence")
            path = matches_found[0]
    return candidates[path]


def measured(target, reference, rule):
    anchor = rule["target_anchor"]
    target_point = apply(target["matrix"], vector(target["element"]["anchors"][anchor]))
    ref = reference["element"]
    if rule["reference_kind"] not in REFERENCE_KINDS or rule["reference_kind"] not in ref["reference_kinds"]:
        raise ValueError("Reference geometry kind differs")
    origin = apply(reference["matrix"], vector(ref["anchors"][rule["reference_anchor"]]))
    local_direction = unit(ref["directions"][rule["direction"]])
    direction = unit([dot(row[:3], local_direction) for row in reference["matrix"][:3]])
    side = rule["side"]
    if side not in ("positive", "negative"):
        raise ValueError("Specify positive or negative side")
    signed = dot([a-b for a, b in zip(target_point, origin)], direction)
    direction = direction if side == "positive" else [-n for n in direction]
    centre_distance = signed if side == "positive" else -signed
    distance = centre_distance
    centre = target_point
    foot = [v - centre_distance * n for v, n in zip(centre, direction)]
    if rule["measure_to"] == "wall":
        if anchor != "centre":
            raise ValueError("A circular wall needs the centre anchor")
        geom = target["element"]["geometry"]
        radius = geom["radius"]
        normal = unit(geom["normal"])
        normal = unit([dot(row[:3], normal) for row in target["matrix"][:3]])
        if type(radius) not in (int, float) or not math.isfinite(radius) or radius <= 0 or abs(dot(normal, direction)) > 1e-8:
            raise ValueError("A circular wall needs positive radius and an in-plane direction")
        distance -= radius
        target_point = [v - radius * n for v, n in zip(centre, direction)]
    elif rule["measure_to"] != "anchor":
        raise ValueError("Specify anchor or wall")
    return dict(distance=distance, centre_side_distance=centre_distance,
                reference_point=foot, target_point=target_point, direction=direction,
                reference_anchor_point=origin, target_anchor_point=centre)


def path_key(value):
    if not isinstance(value, list) or not all(isinstance(key, str) and key for key in value):
        raise ValueError("Specify a list of native IDs")
    return tuple(value)


def resolve(request, snapshot):
    for field in ("model", "model_unit", "revision"):
        if type(snapshot[field]) != type(request[field]) or snapshot[field] != request[field]:
            raise ValueError("Selection inventory differs for " + field)
    records = inventory(snapshot)
    spec = request["selection"]
    scope = path_key(spec["scope"])
    if scope and scope not in records:
        raise ValueError("Missing selection scope")
    modes = set(spec) & {"paths", "named", "condition"}
    if len(modes) != 1:
        raise ValueError("Specify one selection method")
    measure = spec.get("measurement")
    reference = records[path_key(measure["reference_path"])] if measure is not None else None
    if reference and reference["element"].get("unsupported"):
        raise ValueError("Unsupported reference occurrence")
    if "condition" in modes:
        if any(rec["element"].get("unsupported") for key, rec in records.items() if key[:len(scope)] == scope):
            raise ValueError("Unsupported occurrence in measured selection scope")
        if reference is None:
            raise ValueError("Measured condition requires a reference")
        condition = spec["condition"]
        low, high = condition["range"]
        if any(type(v) not in (int, float) or not math.isfinite(v) for v in (low, high)) or low > high:
            raise ValueError("Expected an ordered finite range in model units")
        keys = [key for key, rec in records.items() if key[:len(scope)] == scope
                and rec["element"]["kind"] == condition["kind"]]
    else:
        paths = snapshot["named"][spec["named"]] if "named" in modes else spec["paths"]
        keys = [path_key(path) for path in paths]
    if len(set(keys)) != len(keys):
        raise ValueError("Repeated selected occurrence")
    targets = []
    for key in keys:
        if key[:len(scope)] != scope:
            raise ValueError("Target outside selection scope")
        record = records[key]
        if record["element"].get("unsupported"):
            raise ValueError("Unsupported target occurrence")
        evidence = {"target": {k: record[k] for k in ("path", "chain", "matrix")}}
        if measure is not None:
            m = measured(record, reference, measure)
            if "condition" in modes and (m["centre_side_distance"] < 0 or not low <= m["distance"] <= high):
                continue
            if m["centre_side_distance"] < 0:
                raise ValueError("Target lies on the opposite reference side")
            evidence.update(reference={k: reference[k] for k in ("path", "chain", "matrix")},
                            measurement=m, rule=measure)
        element = record["element"]
        targets.append(dict(id="/".join(key), reference=spec["operation_reference"],
                            current=element.get("current"), selection=evidence))
    if not targets:
        raise ValueError("Selection matched no elements")
    return targets


def verify_reopened(preview, snapshot):
    """Read back the recorded targets and references for the same logical model and revision."""
    data = preview.read()
    for field in ("model", "model_unit", "revision"):
        if type(data[field]) != type(snapshot[field]) or data[field] != snapshot[field]:
            raise ValueError("Reopened selection differs for " + field)
    records = inventory(snapshot)
    paths = []
    for row in data["rows"]:
        evidence = row["selection"]
        target = rebound(evidence["target"], records)
        if "reference" in evidence:
            ref = rebound(evidence["reference"], records)
            if measured(target, ref, evidence["rule"]) != evidence["measurement"]:
                raise ValueError("Reopened reference measurement changed")
        if target["path"] in paths:
            raise ValueError("Reopened selections alias")
        paths.append(target["path"])
    spec = dict(data["selection"])
    if spec["scope"]:
        depth = len(spec["scope"])
        spec["scope"] = paths[0][:depth]
    if "paths" in spec:
        spec["paths"] = paths
    if spec.get("measurement") is not None:
        spec["measurement"] = dict(spec["measurement"], reference_path=ref["path"])
    reread = resolve(dict(data, selection=spec), snapshot)
    actual = [item["selection"]["target"]["path"] for item in reread]
    if sorted(actual) != sorted(paths) or ("named" in spec and actual != paths):
        raise ValueError("Reopened selection membership changed")
    return paths
