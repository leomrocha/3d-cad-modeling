# Reversible conditioning and unchanged native transfer

## Condition exact profiles through an explicit working frame

Use [profile_conditioning.py](../scripts/profile_conditioning.py) when a caller has supplied a working frame for an authorized native trial. The map is `workingXY=(sourceXY-anchorXY)*scale+translationXY`. Coordinates and anchor/translation use the declared length unit; scale is positive and dimensionless. Supply the material pick through the same map. `conditioning_depth` applies the same uniform scale to the original positive depth. Region-normal-dependent signed extrusion remains a separate measured check.

1. Keep the original complete source profiles, source hashes, source frame and native failed-attempt receipts. Choose no factor, origin, material pick or geometric offset implicitly.
2. `condition_profiles` transforms Line endpoints, Arc endpoints/centers and every NURBS control. Roles, edge order, weights, degrees, knots and signed Arc sweeps remain unchanged. Positive uniform scaling preserves handedness. Reflection, shear, anisotropic scaling and general 3D restoration require a different explicit contract.
3. `conditioning_roundtrip` checks the supplied forward/inverse input map with the [strict source comparator](exact-source-checks.md). A passing input roundtrip establishes numerical reversibility of those inputs. Native acceptance and actual restored geometry require their own checks.
4. Save the created owned document immediately. Save every completed construction step and before switching frames, risky native commands and handoffs. A failed/uncertain save stops the next operation until original-request recovery establishes persistence.
5. After native construction, restore the complete original XYZ frame and original depth. Compare actual native vertices, source curves, control nets, knots, planar/curved supports, complete trim loops and provenance in the original source frame, then save/reopen. Record the actual native result beside the original failed result. A successful working-frame trial does not expose an internal kernel failure predicate.

## Explicit exact cubic-to-Line equivalence

`straight_bezier_certificate` in [exact_profiles.py](../scripts/exact_profiles.py) proves that a supplied clamped single-span degree-3 NURBS with four unit-weight controls has an exact straight-segment locus. It converts each supplied decimal number with `Fraction(str(value))`, checks exact collinearity and nondecreasing control parameters between distinct endpoints, and records rational parameters. No geometric tolerance admits a nearly straight curve. Backtracking control order, rational weights, multiple spans and other degrees fail this bounded certificate.

`compare_with_linear_cubics` requires an explicit unique list of source loop/edge indices. Every permitted edge must pass the certificate. All other source curves, loop roles and grouping retain the strict comparison. The result retains `strict_result`, `geometric_equivalence`, certificates and the encoding change. Preserve the original NURBS input and its strict encoding FAIL when the native kernel represents that edge by a Line.

Before adapting a native edge to Line, inspect its actual curve type, trim parameters and endpoint evaluation. A degree-1 control representation requires its own complete bounded-line proof. Matching endpoints alone does not establish the trim locus or its multiplicity. Use complete closed-loop matching after any explicitly permitted encoding change.

## Transfer complete existing native solid evidence

Use [verify_solid_transfer](../scripts/solid_transfer.py) to compare source/target readbacks after authorized copy operations or save/reopen. It sends no native request.

1. Pin source files and record receipts using [retained artifact relationships](retained-artifact-checks.md). Supply explicit `source_handle/target_handle` bindings, unique source/target records and exact document/revision identities from [stable reads](../scripts/cadtools/records.py). Equal entity counts alone supply no geometry match.
2. The comparison requires Solid3D types, record types, full ACIS payload equality and all noncommon properties. This includes the actual codec envelope, all SAT/SAB bytes and any body transform. A lost codec field or changed geometric property fails.
3. Original XDATA application records retain their values and multiplicity. Optional `added_metadata_apps` explicitly permits additional provenance applications and must be disjoint from original apps. Other common display properties retain separate verification scope.
4. Default coverage requires every source and target record to participate exactly once. Explicit `require_all_targets=false` supports checking one known group in a larger composite. Independently establish the complete composite mapping before claiming whole-output coverage.
5. Identical native payloads carry their existing geometry checks forward. Source material coverage, physical-part counts, placement changes and final persistence require their own evidence. Distinguish native construction domains from source physical bodies and installed component quantities. An altered SAT/SAB encoding or transformed intrinsic graph requires a separate source-bound graph comparison; it fails this exact-payload method.
6. Preserve complete native codec envelopes when a caller prepares an authorized payload change. Prefer targeted schema-declared field updates. A partial replacement object can omit required version/codec fields. Record original source bytes, requested representation change, actual updates and readback independently.

## Checkpoints and final file identity

[save_checkpoint](../scripts/cadtools/checkpoints.py) uses the existing `owned_audit` guard, checks the original document/geometry epoch before recovering a previous save, and refuses active operations. A successful checkpoint receipt binds the final on-disk hash. [save_reopen](../scripts/cadtools/verification.py) also checks the saved file hash after the reopened audit. Preserve an external file replacement as a failed persistence check.

For occurrence reconciliation, preserve source-qualified semantic uses, physical ownership, shared geometry identities and quantity factors independently. Required-work counts, saved recipes, source physical parts, construction domains and expanded occurrences describe different scopes. Retain original identities and source revisions when one saved geometry serves several documented uses. Use the existing [occurrence helpers](generic-integration.md) and [model reconciliation](existing-model-start-check.md).
