# 3D CAD Modeling

Reusable tools and agent instructions for creating, inspecting and modifying 3D models from descriptions, dimensions, drawings, photographs and existing geometry.

The current repo has been used and implemented to generate CAD models using the [OpenCADStudio](https://www.opencadstudio.com/) MCP Server. 

This is an ONGOING WORK, for now is the first pre-pre-pre-alpha release, I'll be updating it, do please collaborate, copy it, share it, that is why the license is MIT

## License

[MIT](LICENSE) for project code and documentation. 
All external sources and assets have their own. IF I have accidentally left some thigns without the real check please do contact me and I'll be really pleased to take that out.

## Introduction

If you do not want to read this and directly check the [Examples](TODO LINK TO EXMAPLES)

I've been working for some time on some cad modeling. As the last time I really touched cad was OpenSCAD (cause I've done software for 20+ years now), the last time I really did something manually in a CAD thign was Autocad 2000 some 25+ years ago AND that I'm too lazy now to learn again to use another CAD  software now I decided I'd make AI agents model things for me. I draw as I learnt 3 decades ago in paper then take pictures and show the things to the model, I have my computer running while sometimes I manage things from my phone.

This adventure has not been without problems, blockers, often cursing and of course AI SLOPE that I try to keep to a minimum, so after so much work and learnings and improving my processes I've started to consolidate all thigns into a single Skills and Scripts repository that takes learnings from all those "adventures".

This time, this repo is now a bed for my recursive self improving skill (RSI - yes this is an exageration) that I'm using for yet another project to make it better. This skill set is far from done, It is thouth already in use by me and I'll keep improving it (it is already improving with each new model and I have 100+ models queued for the automated workflow)

The idea is to share and see if somebody can use it learn new things and make things faster and simpler.

I'll share also the things that I've been working on in other repositories when I consider they are ready enough, although here you'll get some example screenshots from those projects.

## Project

The project develops a common workflow for mechanical parts, assemblies, buildings and model handoffs to physics simulation. 

The main pipeline done for a 3D recreation from known things is:

1. Give the agent the part name, drawings, pictures and known measurements.
2. The agent checks whether a matching 3D model already exists.
3. It reads the dimensions and identifies the separate pieces, holes and mounting points.
4. It builds the missing shapes in CAD, or updates the existing model.
5. It measures the result, compares it with the references, saves it and opens it again to check the saved file.
6. It records the result and improves the reusable instructions or code for the next part.

And the main pipeline that I use for NEW things is:

1. I create some hand sketches and descriptions
2. Send those to an agent
3. Make the agent spawn a swarm of research light agents online for similar things, ideas, concepts and so on
4. Review those results
5. Select a few things ideas drop others rephrase, rewrite, restate and review the definitions, references and so on
6. Get pissed off cause AI changed somethign withotu permission and without instruction
7. write down all findings and ideas git commit changes to keep those
8. Make AI use the skills for 3d modeling till it blocks (it can not create things from nothing)
9. review thigns and get pissed off again
10. iterate  

When I see things are ready enough I send then the automated 3D modeling pipeline to work.

## Repository

1. `docs/` — linked documentation, selected example copies and images.
2. `skills/` — agent task instructions.
3. `scripts/` and `tests/` — reusable helpers and their checks.
4. `research/` — method assessments, workflow definitions and sources.
5. `execution/` — recorded execution reports.

## Examples

## House modeling

This is the first thign I did at this complexity level with AI + drawing + pictures + a lot of iterations, is kind of a model house that I sent to a 3D model that was interpreted with a custom three.js library for 3D many nice things there, output was finally done in  [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) and displayed in the browser  

### Mast physics for a wind generator

I'm working on a wind generator idea, so I started to check how to model and see how a mast support would behave for the particular geometry I'm trying to get on the top part, many of the thigns I did there for the 3d modeling came ata good port so I add them here as examples of what the predating things allowed me to do (with a lot of interaction and effort)

A square mast model and recorded Code_Aster wind cases. [Mast model and simulation pictures](docs/examples/wind-generator.md).

![Mast displacement for 15 m/s wind from 0 and 45 degrees](docs/images/mast/mast-displacement.png)

### Mechanical component models

Another current project is about making a remote controlled 2 wheel tractor, but I do not have time to work on it really so I'm automating all that I can this includes a (mostly) automated pipeline that gets available components from standards and pictures and manufacturer details that kind of fit int eh base idea I have, 

![SKF SY20TF component geometry](./docs/images/mechanical_components/bearing.png)

Selected frame, motor, bearing and battery examples show source-based construction, component boundaries and saved-model checks. [Mechanical component examples](docs/examples/mechanical_components.md).


## Installing and Using it

### How to install the skills

I would directly ASK the AI agent you are using to install this and make it available as skill and scripts, that should do the job. But if you want to do it manually here some pointers.

For Codex on Linux or macOS, complete the [Python helper setup](#set-up-the-python-helpers) below, then run these commands from the repository directory:

```sh
export MODELING_ROOT="$(pwd -P)"
mkdir -p "$HOME/.agents/skills"
for skill in component-cad drawing-inspection source-intake; do
  target="$HOME/.agents/skills/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    printf 'Already exists: %s\n' "$target"
  else
    ln -s "$MODELING_ROOT/skills/$skill" "$target"
  fi
done
```

This registers the three skills for your Codex projects. Existing entries are preserved. Keep this checkout: the skills use its shared scripts and reference files. When working in another project, tell the agent to set `MODELING_ROOT` to this checkout before running the helpers.

In Codex CLI or the IDE extension, use `/skills` to list the installed skills. Invoke one by name, for example:
```text
Use $component-cad to model this component from the supplied drawing.
```

Codex detects skill changes automatically. Restart Codex if a newly linked skill does not appear. See the official [Codex skill installation and discovery documentation](https://developers.openai.com/codex/skills).


### Set up the Python helpers

The current status is with Python 3.12. 
From a terminal:
```sh
git clone https://github.com/leomrocha/3d-cad-modeling.git
cd 3d-cad-modeling
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-native.txt
```

Python dependencies are listed in [requirements-native.txt](requirements-native.txt). 
CAD construction uses an existing [OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio) installation, the OCS engineering skill and the `cadtools` runtime described in the [component CAD skill](skills/component-cad/SKILL.md).

### Use the skills with your agent

1. Give the agent the drawing, pictures or dimensions and describe the model you need.
2. Ask it to read [component-cad](skills/component-cad/SKILL.md) for a component job, [drawing-inspection](skills/drawing-inspection/SKILL.md) for a DXF, or [source-intake](skills/source-intake/SKILL.md) to record the inputs.
3. Specify the component project's input and output locations and the CAD session it should use.
4. Review the resulting model and the changes recorded for that iteration.

### Run a helper directly

For a DXF file named `drawing.dxf`:
```sh
python scripts/dxf_inspect.py drawing.dxf --output drawing-inventory.json
```

Command-line options:
```s
python scripts/part_index.py --help
python scripts/model_inventory.py --help
python scripts/source_intake.py --help
```

### Tools
To get a list of all skills and python helpers do go read the  [tools page](docs/tools.md).

### DISCLAIMER
AI use:
* code and skills are all Written with ai I instruct, reinstruct and review things then I tell it to modify and update things. But as this is for AI use the parts that are only dedicated to it I do not correct the phrasing for humans.
* README and main HUMAN targetted documentations files were sketched by me, written by AI then I drop almost everything cause I do not like it and rewrite things, then I send AI agents to fix some small things and details.
* For the AI documentation I let AI do the writing and try not to get too angry about that cause they are instructions for AI so ...
