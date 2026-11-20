"""Check a catalogue search result for an NSK single-row deep-groove bearing closure."""
import argparse
import json
import re
from pathlib import Path

from catalogue_candidates import variant_check


SOURCE = "https://www.nsk.com/content/dam/nsk/am/en_us/documents/bearings-americas/Rolling-Bearings-for-Industrial-Machinery.pdf"
FAMILY = "single-row-deep-groove-ball-bearing"
SUFFIX = {
    ("shield", 1): "Z", ("shield", 2): "ZZ",
    ("contact-seal", 1): "DU", ("contact-seal", 2): "DDU",
    ("non-contact-seal", 1): "V", ("non-contact-seal", 2): "VV",
}
# Limit the parser to ordinary metric 60, 62 and 63 series used in this procedure.
BASE = r"6[023][0-9]{2}"


def evaluate(candidate, base, closure, sides):
    if not re.fullmatch(BASE, base) or (closure, sides) not in SUFFIX:
        raise ValueError("Supply a four-digit 60, 62 or 63 series base and a supported closure")
    required_suffix = SUFFIX[closure, sides]
    required = {"manufacturer": "NSK", "family": FAMILY}
    source = candidate.get("private_source") or {}
    fields = source.get("variant") or {}
    check = variant_check(candidate, required)
    actual = fields.get("designation")
    parsed = re.fullmatch(f"({BASE})[ -]?(ZZ|DDU|VV|Z|DU|V)", actual or "")
    reason = "manufacturer and family must match sourced fields"
    status = check["status"]
    if status == "different-variant" and all(value is None for value in check["mismatches"].values()):
        status = "needs-evidence"
    if status == "fields-match":
        if parsed is None:
            status, reason = "needs-evidence", "full supported designation required"
        elif fields.get("suffix") is not None and fields["suffix"] != parsed[2]:
            status, reason = "needs-evidence", "suffix field conflicts with full designation"
        elif (parsed[1], parsed[2]) == (base, required_suffix):
            reason = "base and closure suffix match"
        else:
            status, reason = "different-variant", "base or closure suffix differs"
    return dict(id=candidate["id"], file=candidate.get("file"), sha256=candidate.get("sha256"),
                evidence=source.get("evidence"), designation=actual,
                required_designation=base + required_suffix, status=status, reason=reason)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalogue_result", type=Path, help="JSON from catalogue_candidates.py")
    parser.add_argument("--base", required=True, help="NSK four-digit 60, 62 or 63 series, e.g. 6205")
    parser.add_argument("--closure", required=True, choices=sorted({key[0] for key in SUFFIX}))
    parser.add_argument("--sides", required=True, type=int, choices=(1, 2))
    args = parser.parse_args()
    try:
        rows = {}
        receipt = json.loads(args.catalogue_result.read_bytes())
        for name, snapshot in receipt["sources"].items():
            if "error" in snapshot:
                raise ValueError(f"Catalogue {name}: {snapshot['error']}")
            rows[name] = [evaluate(row, args.base, args.closure, args.sides)
                          for row in snapshot["candidates"]]
        if not re.fullmatch(BASE, args.base):
            raise ValueError("Unsupported bearing base")
    except (OSError, KeyError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(dict(manufacturer="NSK", family=FAMILY, base=args.base,
                          closure=args.closure, sides=args.sides, rule_source=SOURCE,
                          required_suffix=SUFFIX[args.closure, args.sides], sources=rows), indent=2))


if __name__ == "__main__":
    main()
