# Cleanup of newly authored examples

Date: 12 November 2026.

1. User instruction: “do apply the cleanup”, referring to removal of newly authored examples and references presenting them as project capabilities.
2. Starting checkpoint: `2b32e72`. All 13 removed files were verified byte-for-byte against committed revision `0a0babb` before deletion.
3. Finding: executable examples and custom input formats were created outside the research/documentation scope. The six modeling/reconstruction programs received static review and syntax checks; the distance helper received six synthetic tests.
4. Cleanup: remove the examples directory; replace active example references with documented third-party tool/API procedures; retain the 38 workflow dossiers, classifications, original sources, graphs and implementation plan.
5. Actual coordinating model identity is unavailable. The earlier CAD agent reported GPT-6 Luna; the earlier reconstruction/domain runtime identities are unavailable.

## Removed files preserved in Git

Each path below identifies the committed original in revision `0a0babb`. SHA-256 values were verified before removal.

| Committed path | SHA-256 |
| --- | --- |
| `examples/workflows/README.md` | `dc0ecc1fd72e58e7c3f7fb3852aeabe5890dc81e1cf9d4b5c00c2ba2e1c6af5e` |
| `examples/workflows/cad/README.md` | `e3b55e6f14bddee987498c0508fe5d1eef6d9331c5aa7a343eb16e0b7166115d` |
| `examples/workflows/cad/build_part.py` | `bebec6f7c34721490d7e2a0b5e305736b4bc2ed3ec0f8ba428849c08f9fbe02c` |
| `examples/workflows/cad/import_profile.py` | `4be566f7240f1b77a6d52a4e85537e4e974eaa6b1bfd117a4dcaaab51e8affa2` |
| `examples/workflows/common/README.md` | `ec6432a25c2feecc194e86bc2697c5fbed73ec2d7a0c53e23aa4e99c0d01e5ea` |
| `examples/workflows/common/check_control_distances.py` | `449442c3cd0852dafb46930ae11e019002a4e3aa48b988a496e10d9d68c8eef4` |
| `examples/workflows/common/test_control_distances.py` | `d6199099c8875df335bdbbd4aed87f2cdab65b8b3c02b4ecccf11c33d13045df` |
| `examples/workflows/domains/README.md` | `76ce753eb4562db2ea102f9e60afdc3f97668366b802acaeeacf5904ab5bb34f` |
| `examples/workflows/domains/ifc_model.py` | `672a3c834ca14216a37dfa30d4c02bafa97156a7f7bfe8668ffb1cac90dcebb4` |
| `examples/workflows/domains/robot_model.py` | `91b402c896cbbb42e5f75f7367b15fa493402fc5a158b3ce56c8745cebf88391` |
| `examples/workflows/reconstruction/README.md` | `59b7d9c9d6e95eb88ced41ce71ca6899891a0364a73fe19be9f3fe24a108be02` |
| `examples/workflows/reconstruction/calibrate_camera.py` | `f5937a811a3a36d98b6dc4d60fcd03e3d5a6f4cd7c9fa1d1648abc7f6808f61d` |
| `examples/workflows/reconstruction/register_clouds.py` | `02b41b9977009ec75c63770d3b7fe6d010ae3f02b01911c1151fb252dbae2a06` |
