# Inspect and revise an existing bearing assembly

1. Reconcile existing models before construction. Bind the source revision, required configuration, named solids, units/frame and interface expectations.
2. Read actual native records with [stable entity reads](../scripts/cadtools/records.py). Use [native_acis.py](../scripts/native_acis.py) for reachable body geometry and enable supported rigid transformations explicitly.
3. [pillow_block.py](../scripts/pillow_block.py) checks caller-supplied bearing/housing features. Coplanar Boolean fragments can divide a mounting boundary; use the decoded boundary components and independent expected spans.
4. Record source-dimension discrepancies against the exact measured feature. A requested revision changes only named owned solids and preserves unrelated components and source originals.
5. Save a versioned derivative incrementally, then compare saved geometry and metadata with the source expectations. Retain source and result hashes, actual representation and [cleanup](document-cleanup.md) evidence.
