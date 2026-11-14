# Rectangular mounting-envelope references

1. The legacy [pixhawk.py](../scripts/pixhawk.py) module accepts any caller-supplied source-bound rectangular case and nominal metric mounting pattern. Supply units mm and required feature values for case XYZ, hole XY pitches, nominal thread designation and blind depth.
2. Supply construction_overrun_mm explicitly. The nominal reference cylinder must fit within the envelope and the cut depth/overrun must preserve the opposite face. A nominal designation represents a mechanical reference diameter.
3. build_envelope constructs a rectangular clearance body and four nominal mounting references. This representation is a clearance envelope. Detailed outer surfaces require their own source geometry.
4. verify compares observed vertex extrema, projected axes, blind bottom faces and available body closure. Numerical readback tolerance and caller source-dimensional tolerances remain separate. inspect reads the saved native solid.
5. Save IN_PROGRESS models incrementally and retain final save/reopen, source metadata and observed representation in caller-owned job records.
