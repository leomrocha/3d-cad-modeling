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
