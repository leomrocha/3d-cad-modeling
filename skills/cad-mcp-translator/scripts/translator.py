"""Offline mapper for one explicitly selected CAD application, bridge and operation."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def text_field(record, name):
    value = record.get(name)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Expected nonempty {name}")
    return value


def check_mapping(mapping):
    if mapping.get("format") != 1 or not isinstance(mapping.get("steps"), list):
        raise ValueError("Unsupported operation mapping")
    for key in ("application", "bridge", "operation", "quantity", "unit", "source", "readback"):
        text_field(mapping, key)
    for step in mapping["steps"]:
        text_field(step, "action")
        text_field(step, "tool")


def inventory(snapshot):
    """Pages retain request cursor, raw tool list and nextCursor. Reject mixed epochs."""
    pages = snapshot.get("pages")
    generation = text_field(snapshot, "generation")
    if not isinstance(pages, list) or not pages:
        raise ValueError("Missing discovery pages")
    cursor = None
    seen = set()
    tools = {}
    for index, page in enumerate(pages):
        if page.get("generation") != generation or "cursor" not in page or page["cursor"] != cursor:
            raise ValueError("Stale or discontinuous discovery pages")
        if not isinstance(page.get("tools"), list):
            raise ValueError("Invalid tool list")
        for tool in page["tools"]:
            name = text_field(tool, "name")
            if name in tools or not isinstance(tool.get("inputSchema"), dict):
                raise ValueError(f"Duplicate or incomplete tool: {name}")
            tools[name] = tool
        cursor = page.get("nextCursor")
        if cursor is None:
            if index != len(pages) - 1:
                raise ValueError("Pages follow inventory completion")
        elif not isinstance(cursor, str) or not cursor or cursor in seen:
            raise ValueError("Invalid or repeated cursor")
        seen.add(cursor)
    if cursor is not None or snapshot.get("changed") is not False:
        raise ValueError("Discovery incomplete or changed; rediscover")
    return tools


def plan(mapping, application, bridge, operation, snapshot=None, previous=None, connection=None):
    check_mapping(mapping)
    requested = (application, bridge, operation)
    if requested != tuple(mapping[key] for key in ("application", "bridge", "operation")):
        raise ValueError("Mapping belongs to a different application, bridge or operation")
    result = dict(application=application, bridge=bridge, operation=operation,
                  mapping_sha256=digest(mapping), source=mapping["source"],
                  steps=mapping["steps"], readback=mapping["readback"],
                  status="DOCUMENTED" if mapping["steps"] else "DISCOVERY_REQUIRED")
    if snapshot is None:
        return result
    if (snapshot.get("application"), snapshot.get("bridge")) != requested[:2]:
        raise ValueError("Snapshot belongs to a different target")
    if not connection or connection != snapshot.get("connection"):
        raise ValueError("Snapshot must match the explicitly selected connection")
    binding = {key: text_field(snapshot, key) for key in (
        "connection", "workspace", "session", "document", "privileges", "settings",
        "protocol", "transport", "generation")}
    for key in ("host_version", "bridge_version"):
        binding[key] = snapshot.get(key) or "unknown"
    tools = inventory(snapshot)
    names = [step["tool"] for step in mapping["steps"]]
    schemas = {name: tools[name] for name in names if name in tools}
    result["missing_tools"] = sorted(set(names) - schemas.keys())
    result["schemas"] = schemas
    result["binding_sha256"] = digest([requested, result["mapping_sha256"], binding, schemas])
    result["session_only"] = "unknown" in (binding["host_version"], binding["bridge_version"])
    result["status"] = "SCHEMA_OBSERVED" if names and not result["missing_tools"] else "DISCOVERY_REQUIRED"
    if previous is not None and previous != result["binding_sha256"]:
        result["status"] = "STALE_BINDING"
    return result


def contribution_step(preview_choice, current_scope, approved_scope=None):
    """Choose a local workflow step. The caller collects the actual user's decisions."""
    if preview_choice is not True:
        return "KEEP_LOCAL"
    if current_scope is None:
        return "PREPARE_PREVIEW"
    for field in ("commit", "diff_sha256", "destination", "source_branch", "target_branch"):
        text_field(current_scope, field)
    if approved_scope != current_scope:
        return "SHOW_FINAL_SCOPE"
    return "SUBMIT_APPROVED_REVISION"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--application", required=True)
    parser.add_argument("--bridge", required=True)
    parser.add_argument("--operation", required=True)
    parser.add_argument("--mapping", type=Path, help="Explicit job-local candidate mapping")
    parser.add_argument("--snapshot", type=Path, help="Locally captured, sanitized MCP inventory")
    parser.add_argument("--connection", help="Selected local connection ID, required with an inventory")
    parser.add_argument("--previous-binding", help="Check against an earlier local binding digest")
    args = parser.parse_args()
    try:
        if args.mapping:
            mapping = read_json(args.mapping)
        else:
            shipped = Path(__file__).resolve().parents[1] / "mappings"
            bundled = {p.stem: p for p in shipped.glob("*.json")}
            if args.application not in bundled:
                parser.error("Supply a job-local --mapping for the selected application")
            mapping = read_json(bundled[args.application])
        result = plan(mapping, args.application, args.bridge, args.operation,
                      read_json(args.snapshot) if args.snapshot else None, args.previous_binding, args.connection)
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as error:
        parser.exit(2, f"Mapping error: {error}\n")


if __name__ == "__main__":
    main()
