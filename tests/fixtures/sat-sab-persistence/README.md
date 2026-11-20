# SAT and SAB vertex persistence fixture

The fixture is an octagonal prism authored for this test. The XY profile vertices in millimetres are `(-3, -2)`, `(-2, -3)`, `(2, -3)`, `(3, -2)`, `(3, 2)`, `(2, 3)`, `(-2, 3)`, and `(-3, 2)`. The end faces are at Z = −1 mm and Z = 1 mm. The closed body has 16 distinct vertices, planar surfaces and an identity transform. The SAT records that transform explicitly.

ezdxf 1.4.5 generated the ACIS700 SAT body before saving it in an R2010 DXF with millimetre units. The reopened DXF contained the same SAT records after trimming trailing whitespace. ezdxf decoded those records, confirmed the transform is identity, and exported the ACIS700 SAB with the redundant transform omitted. This pair exercises the SAT-to-SAB comparator through a DXF round trip.

The authored fixture geometry uses the [repository MIT licence](../../../LICENSE). The format writer was [ezdxf](https://github.com/mozman/ezdxf) by Manfred Moitzi.

| File | SHA-256 |
| --- | --- |
| `before-save.sat` | `e81335a17b2aa940e86599790b4f128382b7dc72acf1ce797b00259152a2b4a6` |
| `after-reopen.sab` | `25cef7a31ed37226f8127622999230bfef2218d833e9d363209a6732ed45784b` |
