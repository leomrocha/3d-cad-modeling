# Computational geometry and solver handoff

1. Record requirements, source geometry, units, coordinate frames, named parts, material inputs, operating conditions and the required result before calculation.
2. Reuse native solids and supported analytic readers. Give equations and numerical methods their supplied inputs, operating range, discretization and convergence checks. Preserve assumptions and computed values with their own evidence labels.
3. Keep schematic/reference envelopes distinct from detailed component geometry. Mesh appearance, colors and screenshots carry their display meaning; material behavior and physical results require their supplied properties and methods.
4. Save intermediate geometry, input files and calculation state incrementally. Export a derivative only within the requested source/target format, tool and information-change scope; preserve the original.
5. A solver handoff records exact geometry revision/hash, frame, units, representations, parts/interfaces, material/load/boundary inputs and convergence requirements. Report concrete unsupported checks and actual execution results.
