"""Prepare ordered CAD batch rows and bind them to reviewed inputs and an available route."""

import argparse
from dataclasses import dataclass
import json
import math
from pathlib import Path

from operation_catalogue import ACTIONS, load, location, read, verify_method

LENGTH_MM = {"mm": 1, "cm": 10, "m": 1000, "in": 25.4, "ft": 304.8}


def label(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Specify {field}")
    return value


def normalize(value, model_unit):
    """Normalize typed measurements, named properties, flags and definition IDs."""
    if isinstance(value, dict):
        if not value:
            raise ValueError("Empty property map")
        if "unit" in value or "value" in value:
            if set(value) != {"value", "unit"}:
                raise ValueError("A quantity needs exactly value and unit")
            number, unit = value["value"], label(value["unit"], "unit")
            if type(number) not in (float, int):
                raise ValueError("A quantity needs a numeric value")
            try:
                if unit in LENGTH_MM:
                    number *= LENGTH_MM[unit] / LENGTH_MM[model_unit]
                    unit = model_unit
                elif unit in ("deg", "rad"):
                    number = math.degrees(number) if unit == "rad" else float(number)
                    unit = "deg"
                else:
                    raise ValueError(f"Unsupported quantity unit: {unit}")
            except OverflowError as exc:
                raise ValueError("Quantity exceeds numeric range") from exc
            if not math.isfinite(number):
                raise ValueError("A quantity must be finite")
            return {"value": number, "unit": unit}
        return {label(k, "property name"): normalize(v, model_unit) for k, v in value.items()}
    if isinstance(value, list) and value:
        return [normalize(item, model_unit) for item in value]
    if isinstance(value, str):
        return label(value, "property value")
    if type(value) in (int, float, bool):
        try:
            if math.isfinite(value):
                return value
        except OverflowError:
            pass
    raise ValueError("Specify a finite property, a nonempty list or a named result")


def shape(value):
    if isinstance(value, dict):
        if "unit" in value:
            return ("quantity", value["unit"])
        return {k: shape(v) for k, v in value.items()}
    if isinstance(value, list):
        return [shape(v) for v in value]
    return "number" if type(value) in (int, float) else type(value).__name__


@dataclass(frozen=True)
class Preview:
    """Immutable serialized review. Reading rows returns an independent JSON value."""
    document: str

    def read(self):
        return json.loads(self.document)


def prepare(request, catalogue):
    action = label(request["action"], "action")
    if action not in ACTIONS:
        raise ValueError("Specify create, modify, replace or place")
    header = {key: label(request[key], key) for key in ("model", "entity", "output")}
    revision = request["revision"]
    if type(revision) is int:
        if revision < 0:
            raise ValueError("Revision must be nonnegative")
    else:
        label(revision, "revision")
    unit = label(request["model_unit"], "model length unit")
    if unit not in LENGTH_MM:
        raise ValueError("Specify a supported model length unit")
    if "selection" in request:
        from batch_selection import resolve
        if "targets" in request:
            raise ValueError("Specify targets or a selection")
        if "inventory" in request and (Path(header["model"]).suffix.lower() == ".dxf" or header["entity"].startswith("DXF ")):
            raise ValueError("DXF selection requires the saved drawing as its inventory")
        if "inventory" in request:
            snapshot = request["inventory"]
        else:
            from batch_dxf_inventory import read_inventory
            snapshot = read_inventory(request["model"], unit)
        targets = resolve(request, snapshot)
    else:
        targets = request["targets"]
    if not isinstance(targets, list) or not targets or not all(isinstance(t, dict) for t in targets):
        raise ValueError("Specify one or more target records")
    ids = [label(item["id"], "target ID") for item in targets]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate target ID")
    shared = "value" in request
    if shared == ("values" in request):
        raise ValueError("Specify one group value or values keyed by target ID")
    if not shared and (not isinstance(request["values"], dict) or set(request["values"]) != set(ids)):
        raise ValueError("Individual values must match every target ID exactly")
    rows = []
    for item in targets:
        target = item["id"]
        requested = normalize(request["value"] if shared else request["values"][target], unit)
        if not isinstance(requested, dict):
            raise ValueError(f"Specify a quantity or named result properties for {target}")
        current = item.get("current")
        if current is not None or action != "create":
            current = normalize(current, unit)
            if shape(current) != shape(requested):
                raise ValueError(f"Current and requested properties or dimensions differ for {target}")
        if rows and shape(rows[0]["requested"]) != shape(requested):
            raise ValueError(f"Inconsistent result properties for {target}")
        rows.append(dict(target=target, action=action, reference=label(item["reference"], "reference"),
                         current=current, requested=requested))
        if "selection" in request:
            rows[-1]["selection"] = item["selection"]
    routes = [row for row in catalogue["operations"]
              if row.get("action") == action and row["input"] == header["entity"]
              and row["output"] == header["output"]]
    result = dict(**header, action=action, revision=revision, model_unit=unit,
                  angle_convention="degrees, right-hand positive about the named axis",
                  rows=rows, routes=routes)
    if "selection" in request:
        result["selection"] = request["selection"]
    return Preview(json.dumps(result, indent=2, allow_nan=False))


def execution_rows(preview, resource, method, *, catalogue_path, read_revision, read_inventory=None):
    """Recheck the selected route and actual model revision before handing off reviewed rows."""
    data = preview.read()
    catalogue = load(Path(catalogue_path))
    for row in catalogue["operations"]:
        if (row["resource"], row["name"]) != (resource, method) or row not in data["routes"]:
            continue
        if row["usable"] and row.get("readback_verified") is True and row.get("evidence_sha256"):
            definition = next(r for r in catalogue["resources"] if r["id"] == resource)
            if verify_method(row, definition, Path(row["readback_file"])) != row["evidence_sha256"]:
                raise ValueError("Qualification evidence changed after review")
            actual = read_revision(data["model"])
            if type(actual) is not type(data["revision"]) or actual != data["revision"]:
                raise ValueError("Model revision changed after preview")
            if any("selection" in target for target in data["rows"]):
                from batch_selection import verify_reopened
                if read_inventory is None:
                    raise ValueError("Selected occurrences require a live inventory reader")
                paths = verify_reopened(preview, read_inventory(data["model"], data["model_unit"]))
                for target, path in zip(data["rows"], paths):
                    target["target"] = "/".join(path)
            return data["rows"]
    raise ValueError(f"No matching operation with verified readback: {resource}/{method}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request")
    parser.add_argument("--catalogue", type=Path, default=location())
    args = parser.parse_args()
    try:
        print(prepare(read(args.request), load(args.catalogue)).document)
    except (KeyError, ValueError, TypeError, OSError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
