"""Inventory STEP solid-definition entities without counting nested shells.

This is a narrow Part 21 DATA-section reader for entity identity and type only.
It does not parse geometry, placements, topology, units, or product structure.
"""
import re


SUPPORTED_SOLID_TYPES = ("MANIFOLD_SOLID_BREP", "BREP_WITH_VOIDS", "FACETED_BREP")
_TYPE = re.compile(r"\b([A-Z][A-Z0-9_]*)\s*\(")
_SIMPLE = re.compile(r"#(\d+)\s*=\s*([A-Z][A-Z0-9_]*)\s*\(")
_COMPLEX = re.compile(r"#(\d+)\s*=\s*\((.*?)\)\s*;", re.S)


def _without_comments_and_strings(text):
    """Blank comments and quoted strings while preserving separators."""
    out = []
    i = 0
    while i < len(text):
        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            if end < 0:
                raise ValueError("Unterminated STEP comment")
            out.append(" " * (end + 2 - i))
            i = end + 2
        elif text[i] == "'":
            start = i
            i += 1
            while i < len(text):
                if text[i] == "'":
                    if i + 1 < len(text) and text[i + 1] == "'":
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            else:
                raise ValueError("Unterminated STEP string")
            out.append(" " * (i - start))
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def inventory_step_solids(source):
    """Return distinct supported BREP solid definitions in a STEP Part 21 file.

    ``source`` may be UTF-8/ASCII text or bytes. Simple definitions of the
    three supported types are counted once by entity ID. Complex entity
    instances are reported separately and never included in that count.
    Shells and faces are not solid definitions.
    """
    if isinstance(source, bytes):
        text = source.decode("latin-1")
    elif isinstance(source, str):
        text = source
    else:
        raise TypeError("STEP source must be str or bytes")
    cleaned = _without_comments_and_strings(text)
    data = re.search(r"\bDATA\s*;(.*?)\bENDSEC\s*;", cleaned, re.S | re.I)
    if not data:
        raise ValueError("STEP DATA section required")
    body = data.group(1)

    definitions = {}
    for match in _SIMPLE.finditer(body):
        entity_id, kind = match.group(1), match.group(2).upper()
        if entity_id in definitions:
            raise ValueError("Duplicate STEP entity identifier #" + entity_id)
        definitions[entity_id] = {"form": "simple", "types": [kind]}

    complex_spans = []
    for match in _COMPLEX.finditer(body):
        entity_id = match.group(1)
        if entity_id in definitions:
            raise ValueError("Duplicate STEP entity identifier #" + entity_id)
        types = [m.group(1).upper() for m in _TYPE.finditer(match.group(2))]
        if not types:
            raise ValueError("Complex STEP entity has no typed components #" + entity_id)
        definitions[entity_id] = {"form": "complex", "types": sorted(set(types))}
        complex_spans.append(entity_id)

    ids_by_type = {kind: [] for kind in SUPPORTED_SOLID_TYPES}
    for entity_id, definition in definitions.items():
        if definition["form"] == "simple" and definition["types"][0] in ids_by_type:
            ids_by_type[definition["types"][0]].append(int(entity_id))
    for values in ids_by_type.values():
        values.sort()

    complex_entities = []
    for entity_id in complex_spans:
        types = definitions[entity_id]["types"]
        complex_entities.append({
            "entity_id": int(entity_id),
            "component_types": types,
            "solid_related": any(name.endswith("SOLID") or name.endswith("BREP") for name in types),
        })
    complex_entities.sort(key=lambda row: row["entity_id"])
    counts = {kind: len(values) for kind, values in ids_by_type.items()}
    return {
        "supported_solid_entity_ids": ids_by_type,
        "supported_solid_entity_counts": counts,
        "supported_solid_definition_count": sum(counts.values()),
        "complex_entities": complex_entities,
        "complex_solid_related_entities": [row for row in complex_entities if row["solid_related"]],
        "simple_non_solid_definition_count": sum(
            1 for row in definitions.values()
            if row["form"] == "simple" and row["types"][0] not in ids_by_type
        ),
    }
