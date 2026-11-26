"""Plan differential off-flag writes against a complete native flag witness."""


def plan_isolation_transition(original, observed, hidden_before, hidden_after):
    """Return (layer, expected off, desired off) writes for one transition.

    Layer keys are the caller's stable native identities. The caller supplies
    complete flag records and a verified visibility target for each group.
    An empty target restores the baseline. This function sends no requests.
    """
    previous, target = set(hidden_before), set(hidden_after)
    for layer in previous | target:
        flags = original.get(layer)
        if flags is None or flags.get("off") is not False or flags.get("frozen") is not False:
            raise ValueError(f"Layer was not originally on and thawed: {layer}")

    expected = {
        layer: dict(flags, off=True) if layer in previous else flags
        for layer, flags in original.items()
    }
    if observed != expected:
        raise ValueError("Live layer flag table differs from the verified isolation state")

    # Hide first so enabling a layer cannot briefly expose an unrelated leaf.
    return (
        [(layer, False, True) for layer in sorted(target - previous)]
        + [(layer, True, False) for layer in sorted(previous - target)]
    )


def verify_ancestor_appearance(before, after, scope, edited_handles, expected_layers):
    """Check all reachable uses and compare (RGB, effective layer, blockers) by path.

    Paths are tuples of definition handles. Scope is the exact set of paths
    owned by the intended edit. Expected layers include any explicitly
    approved inherited changes. Compare topology, raw properties and world
    placements using the native model separately.
    """
    if before.keys() != after.keys():
        raise ValueError("Occurrence paths changed during the layer simulation")
    scope, edited_handles = set(scope), set(edited_handles)
    if not scope <= before.keys() or not expected_layers.keys() <= scope:
        raise ValueError("Expected layer changes must be within the occurrence scope")
    uses = {p for p in before if p[-1] in edited_handles}
    missing_handles = edited_handles - {p[-1] for p in uses}
    if missing_handles or uses - scope:
        raise ValueError(f"Edited uses outside scope: {sorted(uses - scope)}, missing handles: {sorted(missing_handles)}")
    mismatches = []
    for path, (rgb, layer, blockers) in before.items():
        if after[path] != (rgb, expected_layers.get(path, layer), blockers):
            mismatches.append(path)
    if mismatches:
        raise ValueError(f"Unexpected effective appearance changes: {sorted(mismatches)}")


def plan_exact_isolation_masks(flags, dependencies, groups):
    """Return hidden layer sets for predeclared exact groups of occurrence paths."""
    required = {path: set(layers) for path, layers in dependencies.items()}
    incomplete = [p for p, layers in required.items() if not layers]
    if incomplete:
        raise ValueError(f"Paths missing layer dependencies: {sorted(incomplete)}")
    relevant = set().union(*required.values())
    if not relevant <= flags.keys():
        raise ValueError(f"Missing dependency layers: {sorted(relevant - flags.keys())}")
    enabled = {name for name in relevant if not flags[name]["off"] and not flags[name]["frozen"]}
    masks = {}
    issues = {}
    for name, paths in groups.items():
        wanted = set(paths)
        if not wanted:
            raise ValueError(f"Empty isolation group: {name}")
        keep = set().union(*(required.get(path, set()) for path in wanted)) & enabled
        visible = {p for p, layers in required.items() if layers <= keep}
        missing, extra = wanted - visible, visible - wanted
        if missing or extra:
            issues[name] = {"missing": sorted(missing), "extra": sorted(extra)}
        else:
            masks[name] = enabled - keep
    if issues:
        raise ValueError(f"Isolation paths differ: {issues}")
    return masks
