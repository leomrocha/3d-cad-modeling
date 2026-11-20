"""Find single-row deep-groove ball bearings with a sourced closure and side count."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from catalogue_candidates import lookup
from operation_catalogue import load, location

FAMILY = "single-row-deep-groove-ball-bearing"
CLOSURES = ("shield", "contact-seal", "non-contact-seal")


def designation_key(value):
    return re.sub(r"[ -]+", "", value.upper()) if isinstance(value, str) else ""


def base_matches_designation(base, designation):
    if not isinstance(designation, str):
        return False
    raw = designation.upper().strip()
    prefix = base.upper().strip()
    # A leading digit in the remainder could extend the base designation.
    remainder = raw[len(prefix):]
    return designation_key(raw) == designation_key(base) or (
        raw.startswith(prefix) and bool(remainder)
        and (remainder[0] in (" ", "-")
             or (bool(re.fullmatch(r"[0-9]{4}", prefix)) and remainder[0].isalpha()))
    )


def bearing_fields(candidate):
    source = candidate.get("private_source") or candidate
    variant = source.get("variant")
    return source, {**candidate, **variant} if isinstance(variant, dict) else candidate


def catalogue_record_may_match(row, base):
    source, fields = bearing_fields(row)
    documented = fields.get("designation_evidence") or source.get("designation_evidence") or {}
    return designation_key(fields.get("base") or documented.get("base")) == designation_key(base) or (
        base_matches_designation(base, fields.get("designation") or fields.get("part_number"))
    )


def evaluate(candidate, base, closure, sides):
    if not designation_key(base) or closure not in CLOSURES or type(sides) is not int or sides not in (1, 2):
        raise ValueError("Supply a bearing base designation, closure and side count")
    required = {"family": FAMILY}
    required.update(base=base, closure=closure, sides=sides)
    source, fields = bearing_fields(candidate)
    designation = fields.get("designation") or fields.get("part_number")
    result = dict(id=candidate["id"], file=candidate.get("file"),
                  sha256=candidate.get("sha256"), designation=designation)
    if fields.get("manufacturer"):
        result["manufacturer"] = fields["manufacturer"]

    record_evidence = source.get("evidence")
    if source is candidate and not record_evidence and candidate.get("catalogue_sha256"):
        record_evidence = {
            "catalogue_source": candidate["catalogue_source"],
            "catalogue_sha256": candidate["catalogue_sha256"],
            "record_id": candidate["id"],
        }
    documented = fields.get("designation_evidence") or source.get("designation_evidence") or {}
    actual_designation = designation_key(designation)
    suffix_source = documented.get("source") if actual_designation and designation_key(documented.get("designation")) == actual_designation else None

    missing, differences, conflicts, evidence = [], {}, [], {}
    for field, expected in required.items():
        explicit = fields.get(field)
        documented_value = documented.get(field) if suffix_source else None
        normalize = designation_key if field == "base" else lambda value: value
        if field == "sides":
            explicit = explicit if type(explicit) is int and explicit in (1, 2) else None
            documented_value = documented_value if type(documented_value) is int and documented_value in (1, 2) else None
        if explicit is not None and documented_value is not None and normalize(explicit) != normalize(documented_value):
            conflicts.append(field)
        if explicit is not None and record_evidence:
            actual, provenance = explicit, record_evidence
        else:
            actual, provenance = documented_value, suffix_source
        if field == "base" and actual is None and record_evidence and base_matches_designation(base, designation):
            actual, provenance = base, record_evidence
        if actual is None:
            missing.append(field)
        else:
            evidence[field] = provenance
            if normalize(actual) != normalize(expected):
                differences[field] = actual

    if conflicts:
        status, reason = "needs-evidence", "Conflicting evidence for " + ", ".join(conflicts)
    elif differences:
        status, reason = "different-variant", "Mismatched " + ", ".join(differences)
    elif missing:
        status, reason = "needs-evidence", "Missing evidence for " + ", ".join(missing)
    else:
        status, reason = "fields-match", "Bearing family, base, closure and side count match"
    return dict(result, status=status, reason=reason, missing=missing,
                mismatches=differences, evidence=evidence, required=required)


def search_saved(catalogue_path, query):
    """Read already selected parts sources and search each usable snapshot."""
    catalogue = load(catalogue_path)
    checked = {(row["resource"], row["name"]): row for row in catalogue["operations"]}
    sources = {}
    for resource in catalogue["resources"]:
        available = [method for method in resource.get("methods", ()) if method.get("probe") == "parts"]
        if not available:
            continue
        name = resource["id"]
        method = next((method for method in available
                       if checked.get((name, method["name"]), {}).get("usable")), None)
        if method is None:
            reasons = [checked.get((name, method["name"]), {}).get("reason") for method in available]
            sources[name] = {"error": "; ".join(filter(None, reasons)) or "Parts source has no usable search method"}
            continue
        try:
            sources[name] = lookup(
                Path(method["search_cli"]), Path(resource["location"]), query,
                include_record=lambda row: catalogue_record_may_match(row, query),
                interpreter=resource.get("python") or sys.executable,
            )
        except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
            sources[name] = {"error": str(error)}
    return sources


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalogue_result", nargs="?", type=Path, help="Existing JSON result from catalogue_candidates.py")
    parser.add_argument("--catalogue", type=Path, default=location(), help="Saved operation catalogue to search when no result is supplied")
    parser.add_argument("--base", required=True, help="Bearing base designation, e.g. 6205")
    parser.add_argument("--closure", required=True, choices=CLOSURES)
    parser.add_argument("--sides", required=True, type=int, choices=(1, 2))
    args = parser.parse_args()
    if not designation_key(args.base):
        parser.error("Supply a bearing base designation")
    try:
        sources = (json.loads(args.catalogue_result.read_bytes())["sources"] if args.catalogue_result
                   else search_saved(args.catalogue, args.base))
        rows = {
            name: snapshot if "error" in snapshot else [
                dict(evaluate(dict(row, catalogue_source=name,
                                   catalogue_sha256=snapshot.get("catalogue_sha256")),
                              args.base, args.closure, args.sides), catalogue_source=name)
                for row in snapshot["candidates"]
            ]
            for name, snapshot in sources.items()
        }
    except (OSError, KeyError, TypeError, ValueError) as error:
        parser.error(str(error))
    result = dict(family=FAMILY, base=args.base, closure=args.closure, sides=args.sides,
                  sources=rows, sources_at_search_limit=[name for name, snapshot in sources.items()
                                                          if snapshot.get("reached_search_limit")])
    if not sources:
        result["coverage"] = "No parts sources in the saved operation catalogue"
    print(json.dumps(result, indent=2))
    return int(not sources or any("error" in snapshot for snapshot in sources.values()))


if __name__ == "__main__":
    raise SystemExit(main())
