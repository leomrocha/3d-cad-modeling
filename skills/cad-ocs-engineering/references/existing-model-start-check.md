# Reconcile existing models before construction

1. Inspect actual matching component models and all manifest, work-record, input-sheet and CAD-index references, including entries marked NOT_STARTED. Read readable component name, exact variant/configuration and required representation.
2. Mark a matching completed component DONE with its actual model path and recorded checks. Reuse its geometry and checks, then select an unfinished component. Begin construction only after reconciliation establishes that the required matching model is absent.
3. [model_inventory.py](../scripts/model_inventory.py) reads caller-supplied index, work index, CAD root and project root. The selected inputs define the [path origins](paths.md). An unresolved origin blocks a construction decision.
4. SKIP_EXISTING_MODEL identifies an attributed existing nonempty model. LOCATE_COMPLETED_MODEL preserves DONE while locating an absent recorded output. REVIEW_EXISTING_CANDIDATES requires component-identity review of unscoped links or filename candidates. NEW_MODEL_REQUIRED is the tool's result within the full reconciliation.
5. Distinguish 2D drawings, another component's reference model and matching 3D geometry. Preserve original source/representation labels. IGES may supply surfaces or solids; establish actual topology after inspection.
6. For separately declared configurations pass an exact configuration selector. Other configurations retain their own paths/status; unscoped candidates require review. Reject duplicate/empty configuration names.
7. A candidate_reviews entry identifies one exact candidate_path, lowercase SHA-256, different_component decision, concrete reason and evidence_locator. Apply it only when current path/hash match. Keep stale reviews and unresolved candidates visible. An attributed matching model retains its reuse action.

## Retrieve reusable parts before constructing geometry

Use the [operation selection procedure](modeling-operation-selection.md). Alongside the project reconciliation above, query the available CAD Models snapshot and every compatible user-supplied local parts snapshot. Reuse the trusted CAD Models search implementation. For example:

```sh
python "$SKILL_ROOT/scripts/catalogue_candidates.py" "$PART_SEARCH_TERM"
```

The command searches the parts sources selected during catalogue setup or refresh. Search full identifiers and variant-defining dimensions, then aliases or family terms as needed. A returned file path is relative to that source's data directory. Use the record and its companion to establish variant, geometry scope and mating interfaces. Keep uncovered sources, missing files and search-limit results visible. For a supplied unindexed folder, retain the existing project inventory and identify the folder for preparation with the CAD Models indexing method. An unavailable catalogue is not a verified miss.

Inspect all relevant matches for an unchanged part before choosing a family derivative. An existing screw of a different length is eligible for a parameter edit only with evidence of a compatible editable family and length control. For a verified match, reuse the actual file. For a family edit, record parameter name and units, preserve the family source and check the derivative before recording DONE. For a different variant without a suitable parameter, record the mismatch and continue to the existing script or guided route.

Catalogue results retain the stated configuration (`variant`), revision, construction status (`state`) and incomplete-information flag (`needs_information`) when supplied. Use these fields to select the configuration for inspection. Qualify a requested dimension from its evidence or by measuring the selected revision.
