# Workflow

[Documentation](README.md) · [Tools](tools.md) · [Examples](examples/README.md)

## Common modeling sequence

1. **Record the request and sources.** Identify the model, required features, output representation and source revisions. [Source intake](reference/operations.md#job-01).
2. **Inspect existing models.** Find matching geometry and recorded checks before starting construction. [Existing-model lookup](reference/operations.md#job-02).
3. **Interpret the inputs.** Bind dimensions and units from text, vector drawings or measured image points. [Model brief](reference/operations.md#cad-01), [drawing inspection](reference/operations.md#cad-08) and [image-point calibration](reference/operations.md#job-03).
4. **Construct or modify geometry.** Create source-bound profiles and solids, retaining part identity and native geometry. [Sketches](reference/operations.md#cad-09), [solid construction](reference/operations.md#cad-10) and [assembly](reference/operations.md#cad-12).
5. **Check the saved model.** Compare required features with source expectations, save, reopen and inspect the actual revision. [Verification](reference/operations.md#cad-13).
6. **Prepare the consuming representation.** Carry the required geometry, relationships and physical inputs into the particular building or simulation model. [Building IFC](reference/operations.md#dom-18) and [mast simulation](reference/operations.md#sim-01).

## Photographs and scans

I'd like to implement many things like these in the future btu they'll be done when I need them or if there is enough demand, or if somebody wants to add it OR if I get paid to do it (hey! I also have to earn my living I'd gladly leave where I'm today to make these kind of work full time though)

1. [Calibrate the camera](reference/operations.md#rec-01) from known target coordinates and images.
2. [Recover camera poses and sparse points](reference/operations.md#rec-03) from overlapping photographs.
3. [Reconstruct a dense surface](reference/operations.md#rec-17) using the retained camera solution.
4. [Register and compare surfaces](reference/operations.md#rec-08) in an explicitly scaled frame.
5. [Remodel selected features as CAD](reference/operations.md#rec-14), then [compare revisions](reference/operations.md#rec-16).
