# Shared parts catalogue — discussion proposal

Date: 12 November 2026. Evidence: **user proposal and proposed design alternatives**. Documentation model: **gpt-6.1-sol**. Checkpoint: `9c3f38c`.

## 1. Requested catalogue and current scope

1. User proposal: a third connected record for parts, containing ID, code, location, description, formal industry name where applicable, ISO/IEC/ANSI/EU standard code and name, and search. Initial storage preference: Markdown, CSV or a similar text file. A possible later database/search implementation was mentioned with DuckDB or SQLite.
2. Component records describe individual CAD jobs and their outputs. Action records describe modeling operations and tooling improvements. The proposed shared parts catalogue identifies reusable items and links each item to those component and action records.
3. Current proposed catalogue scope: identity, names/descriptions, manufacturer/supplier/project codes, source and model locations, attributed standards and text/field search. Formal names and standards retain original evidence links and applicability.
4. Catalogue data files and search software remain proposed implementation work. This batch registers the discussion, alternatives and future-work boundary. Acceptance remains a separate project decision.

## 2. Proposed identity and relationships

1. Use a permanent catalogue ID and a readable item name. Preserve manufacturer part numbers, supplier codes and project references as separate fields. Existing identifiers such as **Trelleborg T539 tyre (C001)** and **Main frame longitudinal rail (P01)** remain ferme project references.
2. Keep source file location, native CAD location and physical storage location distinguishable. File records carry representation, revision and source identity. Physical stock and installed assembly occurrences can reference the reusable part identity.
3. Classify purchased components, custom part designs, material/stock specifications and particular cut pieces explicitly. A cut rail can reference its tube/stock specification; an assembly occurrence references the exact part revision.
4. Record a standard's designation, formal title, edition, applicable component/feature and supporting source. Distinguish a standard for a thread/material/dimensional series from a standard applying to an entire component. Keep conformity statements attributed to their source.
5. Link a catalogue part revision to its CAD artifact/check records, component input sheet, construction action occurrences and tool revision used. The action registry retains individual workflow boundaries and its own execution evidence.

## 3. Proposed storage alternatives

1. **Single CSV with Markdown part descriptions:** one searchable identity table plus linked descriptive pages. A part with several codes, standards or files needs an explicit convention for those repeated relationships.
2. **Linked CSV files with generated Markdown catalogue:** proposed recommendation from the discussion. `parts.csv` contains core identities; `part-standards.csv` contains attributed standards and applicability; `part-files.csv` contains artifact/source/revision locations; `part-aliases.csv` contains alternate names and project/supplier references. A generated Markdown index supports browsing. Physical stock locations can have a linked file when that work is introduced.
3. **Markdown-first catalogue:** readable per-part pages and an index. Structured fields and reference checks would support later export and search.
4. **Later database and similarity search:** retain stable IDs and explicit relationships so a future SQLite/DuckDB-based design can import them. Field/text search and possible vector similarity indexing remain separate proposed capabilities; engine/extension selection belongs to that future implementation.
5. These alternatives are registered as proposals. The listed filenames describe possible interfaces and organisation.

## 4. Proposed initial fields and search

1. Core fields: catalogue ID, readable name, formal industry name where evidenced, description, item category, manufacturer, manufacturer part number, variant/revision, source reference and evidence status.
2. Relationship fields: project reference/alias, supplier code, standard designation/title/edition and applicability, CAD/source/check file location and revision, optional physical stock location.
3. Proposed initial search: readable name, description, manufacturer code, alias/project reference, standard and item category. A future Python command can filter text files and return readable item names with artifact links.
4. Seed candidates come from the existing ferme manifest, preserving its exact IDs, source references, dependencies and existing CAD paths. Each component iteration adds its actual artifact/check links and action/tool revision. Repeated part records require identity/variant comparison before merging.

## 5. Future work explicitly recorded by the user

1. User instruction: “we can add mroe information later like material an dresistance to each part, this should be separated by kind of work wood, metal, architecture, mechanical, industrial, etc but this is a point for later I htink we need to leave this there as a FUTURE work”.
2. **Future work:** add material information and resistance properties per part. Property values will retain units, source, evidence status and applicable measurement/operating conditions when this extension is defined.
3. **Future work:** classify by kind of work, including wood, metal, architecture, mechanical and industrial. The category structure and treatment of items spanning several kinds of work belong to that extension.
4. The current proposal records these extensions and their future status. Their detailed schemas, values and classification implementation form later work.

## 6. Existing local sources and relationships

1. [Ferme CAD input index](/home/leo/projects/ferme/engineering/module-development/cad-inputs/README.md): source-based component/custom-part sheets, model references and geometric dependency rules.
2. [Ferme part manifest](/home/leo/projects/ferme/engineering/module-development/cad-inputs/parts.json): 103 records with ID, readable name, group, route, quantity, kind, input sheet, dependencies, sources and existing CAD path. Existing project catalogue seed material.
3. [Evidence-based CAD construction skill](/home/leo/projects/ferme/skills/cad-construction/SKILL.md): component/source identity, variants, revisions, representation, provenance and reproduction records.
4. [Implementation queue and existing-code map](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/README.md): existing action-level implementation records and evidence categories.
5. [Structured implementation queue](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/queue.json): individual action references and operation contracts. The proposed catalogue links to action occurrences while retaining those definitions.
6. [First source-record implementation proposal](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md): source locators, revision identities, hashes and correction relationships that can support catalogue evidence.
7. [Project idea register](/home/leo/projects/3dmodeling/research/ideas-register.md): catalogue/storage/search and future materials/work-domain ideas, each with proposal status and links to this discussion record.

## 7. Batch execution record

1. Authorisation: standing instruction to register every idea/source/alternative, the correction requesting repository registration and the subsequent instruction to leave material/resistance/work-domain extensions as future work.
2. Executed work: local document/manifest inspection, discussion registration, source snapshots and documentation consistency checks. Existing operation/action definitions and the implementation plan are preserved.
3. Evidence classifications: user proposal; proposed design alternative; future work; inspected local source; authored discussion document. Catalogue implementation and new part-property assertions retain their proposed status.
