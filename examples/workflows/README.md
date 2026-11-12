# Input-to-3D reference code

Date: 12 November 2026.

| Procedure | Code and input contract | Libraries | Output |
| --- | --- | --- | --- |
| Explicit dimensions to a drilled CAD plate | [CAD examples](/home/leo/projects/3dmodeling/examples/workflows/cad/README.md), [build_part.py](/home/leo/projects/3dmodeling/examples/workflows/cad/build_part.py) | CadQuery / OCCT | STEP solid |
| Closed DXF profile to an extrusion | [import_profile.py](/home/leo/projects/3dmodeling/examples/workflows/cad/import_profile.py) | CadQuery, ezdxf | STEP solid |
| Known checkerboard observations to camera calibration | [reconstruction examples](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/README.md), [calibrate_camera.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/calibrate_camera.py) | OpenCV, NumPy | Intrinsics, distortion, poses and pixel residuals |
| Source cloud and target cloud to refined alignment | [register_clouds.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/register_clouds.py) | Open3D, NumPy | Transform, aligned derivative and correspondence statistics |
| Explicit wall and opening data to building entities | [domain examples](/home/leo/projects/3dmodeling/examples/workflows/domains/README.md), [ifc_model.py](/home/leo/projects/3dmodeling/examples/workflows/domains/ifc_model.py) | IfcOpenShell, NumPy | IFC4 project, storeys, walls and opening relationships |
| Explicit bodies, joints, mesh assets and inertial data to robot description | [robot_model.py](/home/leo/projects/3dmodeling/examples/workflows/domains/robot_model.py) | Python standard library; MuJoCo for model compilation | MJCF XML and asset provenance manifest |
| Extracted model points compared with source lengths | [common helper contract](/home/leo/projects/3dmodeling/examples/workflows/common/README.md), [check_control_distances.py](/home/leo/projects/3dmodeling/examples/workflows/common/check_control_distances.py) | Python standard library | Separate fit/check distance residuals |

The six modeling/reconstruction scripts are reference implementations reviewed statically and syntax checked. Their READMEs supply invocation and input contracts. The common distance helper has synthetic unit tests. Workflow dossiers link these scripts to applicable operations and supply native tool/API entry points for the remaining operations.

Original tool documentation and evidence summaries are registered in the [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md). Workflow-specific prerequisites, source points, units, failure recovery and classifications are in the [38 dossiers](/home/leo/projects/3dmodeling/research/workflows/details/README.md).
