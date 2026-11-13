# 3D CAD Modeling

Reusable tools and agent instructions for creating, inspecting and modifying 3D models from descriptions, dimensions, drawings, photographs and existing geometry.

This is an ONGOING WORK, for now is the first pre-pre-pre-alpha release, I'll be updating it, do please collaborate, copy it, share it, that is why the license is MIT

AI use:
* code and skills are all Written with ai I instruct, reinstruct and review things then I tell it to modify and update things. But as this is for AI use the parts that are only dedicated to it I do not correct the phrasing for humans.
* README and main HUMAN targetted documentations files were sketched by me, written by AI then I drop almost everything cause I do not like it and rewrite things, then I send AI agents to fix some small things and details.
* For the AI documentation you'll notice the files and docs are really really ugly like every AI written thing.

## Introduction

I've been working for some time on some cad modeling. As the last time I really touched cad was OpenSCAD (cause I've done software for 20+ years now), the last time I really did something manually in a CAD thign was Autocad 2000 some 25+ years ago AND that I'm too lazy now to learn again to use another CAD  software now I decided I'd make AI agents model things for me. I draw as I learnt 3 decades ago in paper then take pictures and show the things to the model, I have my computer running while sometimes I manage things from my phone.

This adventure has not been without problems, blockers, often cursing and of course AI SLOPE that I try to keep to a minimum, so after so much work and learnings and improving my processes I've started to consolidate all thigns into a single Skills and Scripts repository that takes learnings from all those "adventures".

This time, this repo is now a bed for my recursive self improving skill (RSI - yes this is an exageration) that I'm using for yet another project to make it better. This skill set is far from done, It is thouth already in use by me and I'll keep improving it (it is already improving with each new model and I have 100+ models queued for the automated workflow)

The idea is to share and see if somebody can use it learn new things and make things faster and simpler.

I'll share also the things that I've been working on in other repositories when I consider they are ready enough, although here you'll get some example screenshots from those projects.

## Project

The project develops a common workflow for mechanical parts, assemblies, buildings and model handoffs to physics simulation. 

The main pipeline done for a 3D recreation from known things is:

TODO MAKE THE WORKFLOW CLEAR AND ELI 5 NOT FUCKGIN BLABBERY
1. **Record the request and sources.** Identify the model, required features, output representation and source revisions. 
2. **Inspect existing models.** Find matching geometry and recorded checks before starting construction. 
3. **Interpret the inputs.** Bind dimensions and units from text, vector drawings or measured image points. 
4. **Construct or modify geometry.** Create source-bound profiles and solids, retaining part identity and native geometry. 
5. **Verification.** Compare required features with source expectations, save, reopen and inspect the actual revision. 
6. Iterate

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


## Installing and Using it

TODO HERE ADD THAT PART on how to do this install use and so on


## Documentation

1. [Documentation home](docs/README.md) — guide to the pages.
2. [Workflow](docs/workflow.md) — inputs, modeling, checking and handoffs.
3. [Tools](docs/tools.md) — software roles, agent responsibilities and implementation status.
4. [Example gallery](docs/examples/README.md) — wind-generator, FERME and building applications.

## Repository

1. `docs/` — linked documentation, selected example copies and images.
2. `skills/` — agent task instructions.
3. `scripts/` and `tests/` — reusable helpers and their checks.
4. `research/` — method assessments, workflow definitions and sources.
5. `execution/` — recorded execution reports.

## License

[MIT](LICENSE) for project code and documentation. 
All external sources and assets have their own. IF I have accidentally left some thigns without the real check please do contact me and I'll be really pleased to take that out.


## Examples

## House modeling

This is the first thign I did at this complexity level with AI + drawing + pictures + a lot of iterations, is kind of a model house that I sent to a 3D model that was interpreted with a custom three.js library for 3D many nice things there, output was finally done in  [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) and displayed in the browser  

### Mast physics for a wind generator

I'm working on a wind generator idea, so I started to check how to model and see how a mast support would behave for the particular geometry I'm trying to get on the top part, many of the thigns I did there for the 3d modeling came ata good port so I add them here as examples of what the predating things allowed me to do (with a lot of interaction and effort)

A square mast model and recorded Code_Aster wind cases. [Models, simulation inputs and results](docs/examples/wind-generator.md).

![Mast displacement for 15 m/s wind from 0 and 45 degrees](docs/images/wind-generator/mast-displacement.png)

### Mechanical component models

Another current project is about making a remote controlled 2 wheel tractor, but I do not have time to work on it really so I'm automating all that I can this includes a (mostly) automated pipeline that gets available components from standards and pictures and manufacturer details that kind of fit int eh base idea I have, 

![SKF SY20TF component geometry](./docs/images/ferme/bearing.png)

Selected frame, motor, bearing and battery examples show source-based construction, component boundaries and saved-model checks. [FERME examples](docs/examples/ferme.md).

### Buildings

The proposed building route combines plans, dimensions and component geometry into walls, floors, openings and semantic IFC models. [Building workflow](docs/examples/buildings.md).
