# Choose the route for one modeling operation

Start with the requested result, known part identity, required geometry or output type, and checks. Respect a caller-selected operation or provider. Use this order when there is a choice.

1. Reuse an existing suitable component unchanged. Check project models and each user-supplied parts source through the CAD Models indexing method. Confirm the actual asset, variant, representation and mating features. A matching alias can identify several sizes.
2. Reuse an editable member of the correct family. Identify the exposed parameter, supported range or configuration, units and affected interfaces. Save a derivative, change only the intended parameter, rebuild, then check the requested dimension and one independent datum or interface. Preserve the original.
3. Run an existing script, generator, algorithm or service that delivers the required output with repeatable checks.
4. Use an available sub-skill or skill when interpretation, correction or user judgment is needed. Give it the relevant source, the unresolved feature and a concrete output to return.
5. Carry out only the uncovered operation. Preserve useful scripts, prompts, procedures, outputs and checks in the job so a later skill improvement can reuse them.

Choose the first suitable level. Within that level consider total setup time, compute or service cost, correction effort and verification effort. Reuse an earlier verified lookup or intermediate result for the same inputs. After identifying a component from an image, return to component lookup for that component. A drawing-inspection, translation or repair request with a supplied file starts at its requested operation.

## Set up and refresh the local operation catalogue

During setup, or on first call after copying a skill, run `python3 "$SKILL_ROOT/scripts/operation_catalogue.py" show`. Ordinary jobs read this saved catalogue. It is shared across the modeling skills at `$XDG_CONFIG_HOME/cad-modeling/operations.json` (default `~/.config/cad-modeling/operations.json`). An explicit `--catalogue FILE` before the command selects another catalogue. The CAD Models parts index supplies reusable geometry.

Show the existing resources, the discovered interpreter and any tools, skills, environments, model files, servers and parts sources the user has already identified. Ask which resources may be used. Discovery alone grants no permission. For **“Refresh the available skills”**, show the saved selections and ask what to add, remove or change, including keeping the same list. Use already installed dependencies and existing model files. Refresh installs and downloads nothing.

Supply the complete confirmed list to `refresh --resources FILE`, or run `refresh` to repeat the saved checks. Each resource has a unique `id`, a `kind` and the selected paths or endpoint. Store absolute paths to the selected interpreter, owned helper directory. Include only credential references. For example, a confirmed OpenCV environment is a JSON list with one object:

```json
[{"id":"drawing-python","kind":"opencv","python":"/selected/environment/bin/python"}]
```

The OpenCV entry checks whether the selected interpreter provides the functions for contours, planar calibration and thinning. Other resources declare a `location`, a `python` interpreter when needed, an optional `scripts` directory and a `methods` list. Each method names its `name`, `input`, `output` and `probe`. Match inputs and outputs to the selected deployment. Use `modules` and `paths` for additional dependencies of that method.

| Probe | Dependencies to select |
| --- | --- |
| `vision` | Source-intake client, interpreter and `config` for the selected endpoint or local model at `location`. Record the deployment's supported prompts and outputs. Only local YOLO needs the local YOLO runtime. |
| `sam`, `sam2` | Local model directory and the selected segmentation runtime. |
| `cad-sequence` | CAD client, selected endpoint and deployed model. |
| `intake`, `dxf` | The corresponding installed helper and its Python dependencies. |
| `parts` | CAD Models data directory and its local `search_cli`. |
| `guided` | Selected tool or skill path and the dependencies of the named operation. |

Setup and refresh check dependencies without running modeling jobs or sending requests to a server. Report which methods became available or unavailable and name missing dependencies. Keep the selected resources in the local catalogue.

For a job, use `routes OUTPUT` to find methods with the required output. If a dependency is missing or a result falls short, tell the user which method was affected, what it returned and what is still needed. Immediately try the next applicable, authorized route in the reuse order. Carry useful partial results forward, for example a detection box can guide a segmenter or a trace. An empty search or detection applies to that input and leaves the method available. For a tool failure use `failed RESOURCE METHOD "specific error"` and bypass that method. Continue until the requested result is obtained or every applicable, authorized route has been tried. If those routes are exhausted, report the methods tried and the missing output.

## Choose a provider by its actual capability

Ordinary skill execution, including helpers and subprocesses, uses existing packages and model files. A missing dependency skips that method. Skill installation and execution must never download models, weights, tokenizers or processors. Use a model only when its required files already exist locally or the user supplies a running inference service with that model already loaded. Use inference operations only. Skip unavailable models and services that fetch files on demand. Apply the same rule to tests and examples.

Identify the available local algorithms, scripts, models and user-supplied servers relevant to the operation. Inspect the selected deployment's tool schema, model/task metadata or API documentation. Match its inputs and actual outputs to the job. Use its declared API and configured client; do not assume a common endpoint format. Use a small job-relevant sample if capability or coordinate conventions need confirmation.

For an image operation, distinguish descriptions, class labels, boxes, point prompts, raster masks and polygons. A YOLO detection deployment can propose boxes. A segmentation deployment may return masks or polygons. A VLM may read markings, ground an object or emit a mask when its interface supports that output. Record original image dimensions, crop/resize/padding transforms, coordinate convention and instance IDs. Map the result back to source pixels and check the target boundary or feature. Forward a box to a compatible segmenter when a mask is required. Use an agent or user to correct the specific ambiguous instance or boundary when needed. Metric dimensions require separate scale evidence.

## Record the route in the existing job log

For direct reuse, record source/index revision, asset ID and hash and the match check. For a derivative, add the parent hash, parameter edit, output and readback. For a tool call, record the script or provider, model/version if exposed, inputs, settings, returned artifact and check. For guided or new work, also keep the useful prompt, correction and reusable script or procedure. Record why a higher-priority route was unsuitable when that affects the decision. Keep credentials outside logs. Retain evidence locally under the owning project's rules.
