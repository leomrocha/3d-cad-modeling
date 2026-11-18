"""Plan directional CAD operations from a user-selected connection's evidence."""

import argparse
import hashlib
import json
from pathlib import Path


def signature(value):
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode()
    ).hexdigest()


def strings(record, key):
    values = record[key]
    if not isinstance(values, list) or any(
        not isinstance(x, str) or not x for x in values
    ):
        raise ValueError(f"Expected list of names in {key}")
    return set(values)


def plan(data, connection, source, target, required, previous=None):
    """Format and scratch-document names are opaque, exact representation identifiers."""
    if not source or not target or source == target:
        raise ValueError("Specify distinct source and target representations")
    if not connection or data["connection"] != connection:
        raise ValueError("Selected connection does not match the supplied inventory")
    tools = {}
    for tool in data["tools"]:
        name = tool["name"]
        if (
            not isinstance(name, str)
            or not name
            or name in tools
            or not isinstance(tool["inputSchema"], dict)
        ):
            raise ValueError("Incomplete or duplicate tool schema")
        tools[name] = tool["inputSchema"]
    if data.get("complete") is not True:
        raise ValueError("Refresh the complete inventory before selecting tools")
    available = strings(data, "available_dependencies")
    edges, rejected = [], []
    for row in data["operations"]:
        name = row["tool"]
        if name not in tools:
            rejected.append(f"{name}: tool absent")
            continue
        fields = tools[name].get("properties", {})
        bindings = row["bindings"]
        if (
            not isinstance(bindings, dict)
            or not set(bindings) <= set(fields)
            or not set(tools[name].get("required", [])) <= set(bindings)
        ):
            rejected.append(f"{name}: argument binding differs from schema")
            continue
        if not all(
            isinstance(row[k], str) and row[k].strip()
            for k in ("from", "to", "evidence")
        ):
            raise ValueError("An operation needs representations and evidence")
        missing = strings(row, "dependencies") - available
        lost = set(required) - strings(row, "preserves")
        if missing or lost or row.get("accessible") is not True:
            rejected.append(
                f"{name}: missing dependencies {sorted(missing)}, "
                f"unpreserved properties {sorted(lost)}, accessible={row.get('accessible')}"
            )
            continue
        edges.append(row)
    # Prefer fewer documented losses, then fewer calls. Keep all equally good alternatives.
    pending = [(source, [], {source}, set())]
    candidates = []
    expansions = 0
    while pending:
        expansions += 1
        if expansions > 4096:
            raise ValueError("Inventory too broad; scope it to this conversion")
        current, steps, visited, losses = pending.pop()
        for edge in edges:
            destination = edge["to"]
            if edge["from"] != current or destination in visited:
                continue
            path = steps + [edge]
            path_losses = losses | strings(edge, "losses")
            if set(required) & path_losses:
                continue
            if destination == target:
                candidates.append(
                    (len(path_losses), len(path), path, sorted(path_losses))
                )
            else:
                if len(pending) + len(candidates) >= 4096:
                    raise ValueError("Inventory too broad; scope it to this conversion")
                pending.append(
                    (destination, path, visited | {destination}, path_losses)
                )
    candidates.sort(key=lambda entry: entry[:2])
    fingerprint = signature([data, connection, source, target, sorted(required)])
    routes = [
        dict(steps=c[2], losses=c[3]) for c in candidates if c[:2] == candidates[0][:2]
    ]
    status = "CANDIDATE" if routes else "GAP"
    if previous and previous != fingerprint:
        status = "STALE"
    if not routes:
        rejected.append(
            f"No verified declaration chain from {source} to {target}; "
            f"check a writer for {target} and its input representation"
        )
    return dict(
        status=status,
        connection=connection,
        binding=fingerprint,
        routes=routes,
        reasons=rejected,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path)
    for arg in ("connection", "source", "target"):
        parser.add_argument("--" + arg, required=True)
    parser.add_argument("--require", action="append", default=[])
    parser.add_argument("--previous")
    args = parser.parse_args()
    try:
        result = plan(
            json.loads(args.inventory.read_text()),
            args.connection,
            args.source,
            args.target,
            args.require,
            args.previous,
        )
        print(json.dumps(result, indent=2))
    except (KeyError, OSError, TypeError, ValueError) as exc:
        parser.exit(2, f"Invalid route inventory: {exc}\n")
