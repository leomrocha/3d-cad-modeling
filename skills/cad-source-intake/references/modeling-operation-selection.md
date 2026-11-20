# Choose the route for one modeling operation

Start with the requested result, known part identity, required geometry or output type, and checks. Respect a caller-selected operation or provider. Use this order when there is a choice.

1. Reuse an existing suitable component unchanged. Check project models and each user-supplied parts source through the CAD Models indexing method. Confirm the actual asset, variant, representation and mating features. A matching alias can identify several sizes.
2. Reuse an editable member of the correct family. Identify the exposed parameter, supported range or configuration, units and affected interfaces. Save a derivative, change only the intended parameter, rebuild, then check the requested dimension and one independent datum or interface. Preserve the original.
3. Run an existing script, generator, algorithm or service that delivers the required output with repeatable checks.
4. Use an available sub-skill or skill when interpretation, correction or user judgment is needed. Give it the relevant source, the unresolved feature and a concrete output to return.
5. Carry out only the uncovered operation. Preserve useful scripts, prompts, procedures, outputs and checks in the job so a later skill improvement can reuse them.

Choose the first suitable level. Within that level consider total setup time, compute or service cost, correction effort and verification effort. Reuse an earlier verified lookup or intermediate result for the same inputs. After identifying a component from an image, return to component lookup for that component. A drawing-inspection, translation or repair request with a supplied file starts at its requested operation.

## Choose a provider by its actual capability

Identify the available local algorithms, scripts, models and user-supplied servers relevant to the operation. Inspect the selected deployment's tool schema, model/task metadata or API documentation. Match its inputs and actual outputs to the job. Use its declared API and configured client; do not assume a common endpoint format. Use a small job-relevant sample if capability or coordinate conventions need confirmation.

For an image operation, distinguish descriptions, class labels, boxes, point prompts, raster masks and polygons. A YOLO detection deployment can propose boxes. A segmentation deployment may return masks or polygons. A VLM may read markings, ground an object or emit a mask when its interface supports that output. Record original image dimensions, crop/resize/padding transforms, coordinate convention and instance IDs. Map the result back to source pixels and check the target boundary or feature. Forward a box to a compatible segmenter when a mask is required. Use an agent or user to correct the specific ambiguous instance or boundary when needed. Metric dimensions require separate scale evidence.

## Record the route in the existing job log

For direct reuse, record source/index revision, asset ID and hash and the match check. For a derivative, add the parent hash, parameter edit, output and readback. For a tool call, record the script or provider, model/version if exposed, inputs, settings, returned artifact and check. For guided or new work, also keep the useful prompt, correction and reusable script or procedure. Record why a higher-priority route was unsuitable when that affects the decision. Keep credentials outside logs. Retain evidence locally under the owning project's rules.
