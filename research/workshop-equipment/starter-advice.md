# Proposed metalworking starter setup — 2026-11-13

## Discussion target and evidence

Advice requested for restarting welding after 25 years, occasional full workdays, new low-cost 230 V single-phase equipment, existing woodworking equipment, and explicit priority for MMA/stick alongside gas and self-shielded wire welding. Plasma target remains steel/stainless steel 5–10 mm. This document records proposals, with author decisions retained separately in ideas.json.

Existing machine evidence: [findings](findings.md) and [source records](../sources/workshop-equipment-2026-11-13.json). New practical guidance sources are registered in [starter sources](../sources/workshop-starter-2026-11-13.json). Primary-source web inspection is delegated to the previously launched agent with gpt-6-luna requested; actual runtime model identity is unavailable. Advice is synthesis, not a locally exercised welding procedure.

## Proposed buying order

1. One MIG/MAG + self-shielded flux + MMA machine. Use MMA immediately and add gas MIG for thin steel sheet. The previously recorded 160 M offers a lower purchase price; the 200 ST offers 1–5 kg spools and spot function. Choose operating current/duty against the actual electrical circuit. Separate MMA is an alternative when portability or leaving the wire setup connected has value. Optional TIG is a later addition.
2. Welding PPE and fume control, a dedicated noncombustible work area, steel bench, vice and clamps.
3. One 125 mm angle grinder with material-rated cutting discs, grinding discs and flap discs, each used for its intended operation. A second grinder is an optional convenience for avoiding disc changes.
4. Metal bandsaw for repeated straight tube/section cuts; choose throat and vice capacity from the actual stock. A carbide dry-cut metal saw is an alternative for fast repetitive cuts, subject to machine and blade material approval. Abrasive chop saw is another category to compare, with abrasive consumables, sparks and burrs. Existing reciprocating saw with a metal blade is useful for dismantling; a hacksaw handles small quantities.
5. Plasma and matched compressed-air system for plate shapes and openings. Pair measured/published delivered flow at operating pressure, duty, hose size and filtration with the exact cutter manual. Tank volume supplies a buffer; delivered flow determines replenishment.

## MMA/stick starter kit

Electrode holder and work-return clamp with cables, normally supplied with a multiprocess machine; E6013 mild-steel electrodes in 2.5 and 3.2 mm; chipping hammer; steel wire brush; electrode storage according to maker instructions. Proposed starter sizes are practice choices. Lincoln START-01 specifies 60–85 A for its 2.5 mm E6013 and 100–125 A for its 3.2 mm E6013, with AC/DC−/DC+ permitted. Apply the exact purchased electrode sheet for current and polarity, and the machine manual for operation. E7018 is a later procedure-specific alternative with its own storage requirements. Use suitable stainless electrodes for known stainless grades and joint procedures.

## Gas and self-shielded wire kits

For mild-steel gas MIG/MAG: compatible solid steel wire, argon/CO2 mixture approved by the wire manufacturer, regulator/flowmeter, gas hose, secured cylinder, matching contact tips/drive rolls, spare nozzle and liner. Proposed wire sizes: 0.6 mm for thin sheet when supported, and 0.8 mm as a general starting size. Keep refill availability in the cylinder buying decision.

For self-shielded flux: compatible flux wire, matching feed rolls/tips and the polarity required by the exact wire. Chip and brush slag between passes. Keep thin automotive sheet practice with gas MIG separate from thicker MMA/flux exercises. Existing WELD-01 and WELD-02 records support both gas and flux modes.

## Holding, measurement and drilling

Proposed initial set: bench vice, four metalworking clamps, two locking pliers, engineer square, steel rule, scriber, centre punch, deburring file and hammer. Reuse a compatible drill/drill press with metal-rated HSS bits, a clamped workpiece and cutting fluid selected for the material. Support long stock. Use dedicated stainless brushes/abrasives when preserving stainless surfaces.

Use an existing woodworking saw for aluminium only where its manufacturer permits the exact nonferrous material and blade arrangement; follow speed, blade, section and clamping limits. Steel cutting uses a saw explicitly rated for steel.

## Work area and practice sequence

Provide an automatic welding helmet suitable for welding/plasma current, safety glasses, grinding face shield, leather gloves, flame-resistant clothing, enclosed protective footwear and hearing protection. Capture welding fumes at source; follow the risk assessment for respiratory protection. Separate hot work from wood dust, dust extraction and combustibles; protect adjacent people from arc radiation. Secure the gas cylinder upright.

Prepare known uncoated mild-steel practice coupons, proposed thickness around 3 mm for initial MMA. Clean contact and joint areas, clamp, set current from the electrode maker, practise striking/restarting, straight beads and fillet joints, remove slag and inspect after each pass. Tack a small bracket or frame, check squareness and distortion, then weld in a balanced sequence. Compare gas MIG and self-shielded flux on suitable separate coupons. Practice fracture/cut inspection is learning evidence; safety-critical axles, chassis and load-bearing joints require material-specific repair/fabrication procedures and qualified work.

## Workflow handoffs

All dimensions in mm, electrical current in A and air delivery in L/min at stated bar. Source IDs are defined in the linked registers.

| Operation | Input and prerequisite | Output and checks | Supporting sources |
| --- | --- | --- | --- |
| Saw and deburr | Stock dimensions, material, rated machine/blade, supported clamping | Cut stock; length, squareness, burrs; kerf removes material | START-08/START-13/START-15/START-16 |
| Prepare and tack | Clean identified material, joint fit, clamps, work-return connection | Tacked assembly; square and fit checks; local heat distortion | START-03/START-05; WELD-01/WELD-02 |
| MMA weld | Selected electrode/current/polarity, clean joint, fume control | Weld plus slag; remove slag and inspect before later passes | START-03/START-05; WELD-01/WELD-02 |
| Gas MIG / flux weld | Compatible wire/feed/polarity; shielding system for gas mode | Weld, spatter and flux slag where applicable; inspect joint and distortion | WELD-01/WELD-02; START-09/START-10/START-11 |
| Plasma cut | Rated material/thickness, cutter input circuit and air system | Plate cut; kerf, heat-affected edge and dross; dimensions checked | PLASMA-01/PLASMA-03; START-05/START-06 |

Compatible proposed combination: saw straight stock, deburr, fit/clamp, tack, check square, weld, inspect; use plasma for shaped plate parts joining that assembly. No manufacturing geometry or simulation is produced.

## Practical source summaries

1. **START-01 — Lincoln E6013 electrode sheet**: E6013: 2.5x350 mm 60–85 A; 3.2x350 mm 100–125 A; AC/DC−/DC+. Values apply to this electrode sheet. [Original source](https://ch-delivery.lincolnelectric.com/api/public/content/0a466bf3e2b44d0395103d46fd69a940?v=778bc671).
1. **START-02 — Lincoln electrode storage guidance**: Storage and redrying instructions; specific product label takes precedence. [Original source](https://ch-delivery.lincolnelectric.com/api/public/content/8f62b7daa7104f118facf6c320f497f0?v=2fd828e3).
1. **START-03 — Lincoln stick welding setup guide**: Electrode holder, electrode lead, work-return clamp/lead; clean return contact near work. [Original source](https://ch-delivery.lincolnelectric.com/api/public/content/0f1ee250caf14f8abd252f612b628b18?v=153dd1b8).
1. **START-04 — Lincoln training equipment listing**: Training list includes chipping hammer and wire brush. [Original source](https://classes.lincolnelectric.com/search/publicCourseSearchDetails.do?courseId=1055475&method=load&selectedProgramAreaId=1050137).
1. **START-05 — INRS welding fumes**: Source capture with supplementary general ventilation; emissions depend on process and material. [Original source](https://www.inrs.fr/risques/fumees-soudage/ce-qu-il-faut-retenir).
1. **START-06 — INRS wood dust fire and explosion**: Wood dust deposits/clouds can ignite with heat and welding sparks. [Original source](https://ftweb.inrs.fr/metiers/metiers-du-bois/transformation-du-bois/poussiere/incendie-explosion.html).
1. **START-07 — HSE welding in vehicle repair**: Fume control in repair: paint, underseal, galvanizing, stainless and confined spaces. [Original source](https://www.hse.gov.uk/mvr/mechanical-repair/welding.htm).
1. **START-08 — DEWALT aluminium cutting permissions**: Only approved saw models with appropriate nonferrous blade; consult exact manual. [Original source](https://support.dewalt.com/hc/en-ae/articles/360016679337-Can-I-use-my-saw-to-cut-sheet-Aluminium).
1. **START-09 — Lincoln Steelcore 71T-GS**: Self-shielded wire 0.8/0.9 mm with DC− product instructions; exact wire governs polarity. [Original source](https://ch-delivery.lincolnelectric.com/api/public/content/4b116c2b3b5f46fdaa024bac101c8e4b?v=e32391fd).
1. **START-10 — ESAB Coreshield11**: Self-shielded mild-steel wire; DCEN. [Original source](https://esab.com/us/nam_en/products-solutions/product/filler-metals/mild-steel/self-shielded-flux-cored-wires-fcaw/coreshield-11/).
1. **START-11 — Lincoln MIG and flux polarity guide**: Guide illustrates gas MIG DC+ and its gasless flux DC−. [Original source](https://ch-delivery.lincolnelectric.com/api/public/content/87cc0123c9014e23ad25f0d8721ef755?v=5266f7fb).
1. **START-12 — Lincoln constant current and constant voltage outputs**: Constant current appropriate to manual SMAW. [Original source](https://qacd10.lincolnelectric.com/en/Welding-and-Cutting-Resource-Center/Process-and-Theory/Constant-Current-vs-Constant-Voltage-Output).
1. **START-13 — Bosch GCB127 metal bandsaw application**: Portable18 V example for metal profiles/pipes; application evidence, not a230 V product recommendation. [Original source](https://www.bosch-professional.com/gb/en/products/gcb-18v-127-06012B7000).
1. **START-14 — Evolution metal-cutting saw range**: Carbide blade applications material-dependent; range page. [Original source](https://sklep.evolutionpowertools.com/pages/metal-cutting-chop-saws).
1. **START-15 — Evolution saw manual084**: Material applications with corresponding approved blade. [Original source](https://www.evolutionpowertools.com/downloads/manuals/2025/084.pdf?ref=reachdog&sub_id=).
1. **START-16 — Bosch abrasive metal saw category**: GCO240 abrasive355 mm,3800 rpm; category page supports tool type. [Original source](https://www.bosch-professional.com/om/en/metal-cut-off-saws-131477-ocs-c/).
1. **START-17 — DEWALT DW716 manual**: Specific saw manual prohibits ferrous cutting. [Original source](https://www.dewalt.com/GLOBALBOM/QU/DW716/3/Instruction_Manual/EN/N039235_DW716_EN.pdf).
