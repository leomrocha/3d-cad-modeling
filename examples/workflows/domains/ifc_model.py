#!/usr/bin/env python3
"""Create a small IFC4 model from explicit SI-unit building data.

Input JSON contract (all engineering values are mandatory):
{
  "units": "m",
  "project": {"name": "..."},
  "site": {"name": "..."},
  "building": {"name": "..."},
  "frame": {"name": "project-local-ENU", "x_axis": "east", "y_axis": "north", "z_axis": "up"},
  "storeys": [{"name": "...", "elevation_m": 0.0, "walls": [{
    "name": "...", "p1_m": [0, 0], "p2_m": [1, 0],
    "base_elevation_m": 0.0, "height_m": 2.5, "thickness_m": 0.2,
    "openings": [{"name": "...", "station_m": 0.2, "sill_m": 0.0,
      "width_m": 0.8, "height_m": 2.0, "opening_depth_m": 0.3}]
  }]}],
  "georeference": null
}

This example supports straight, constant-thickness walls and rectangular openings.
It creates a new IFC file and refuses to overwrite an existing target. It does not
interpret plan pixels, assign building code classifications, generate doors or
windows, or infer survey/georeference values. Georeference fields are passed only
when a complete, reviewed CRS/map conversion is present in the input JSON.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import ifcopenshell.api.aggregate
import ifcopenshell.api.context
import ifcopenshell.api.feature
import ifcopenshell.api.geometry
import ifcopenshell.api.georeference
import ifcopenshell.api.project
import ifcopenshell.api.root
import ifcopenshell.api.spatial
import ifcopenshell.api.unit
import numpy as np


def require_number(value: Any, label: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be an explicit number")
    result = float(value)
    if not math.isfinite(result) or (positive and result <= 0.0):
        raise ValueError(f"{label} must be finite" + (" and > 0" if positive else ""))
    return result


def xy(value: Any, label: str) -> tuple[float, float]:
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{label} must contain [x_m, y_m]")
    return require_number(value[0], f"{label}[0]"), require_number(value[1], f"{label}[1]")


def make_model(data: dict[str, Any]):
    if data.get("units") != "m":
        raise ValueError('units must explicitly be "m"')
    frame = data.get("frame", {})
    if frame.get("x_axis") != "east" or frame.get("y_axis") != "north" or frame.get("z_axis") != "up":
        raise ValueError("frame must explicitly declare x=east, y=north, z=up")
    for key in ("project", "site", "building"):
        if not isinstance(data.get(key), dict) or not data[key].get("name"):
            raise ValueError(f"{key}.name is required")

    model = ifcopenshell.api.project.create_file(version="IFC4")
    project = ifcopenshell.api.root.create_entity(
        model, ifc_class="IfcProject", name=data["project"]["name"]
    )
    # Explicit project units: all dimensions in this input are metres.
    metre = ifcopenshell.api.unit.add_si_unit(model, unit_type="LENGTHUNIT")
    square_metre = ifcopenshell.api.unit.add_si_unit(model, unit_type="AREAUNIT")
    cubic_metre = ifcopenshell.api.unit.add_si_unit(model, unit_type="VOLUMEUNIT")
    ifcopenshell.api.unit.assign_unit(model, units=[metre, square_metre, cubic_metre])

    model_context = ifcopenshell.api.context.add_context(model, context_type="Model")
    body_context = ifcopenshell.api.context.add_context(
        model,
        context_type="Model",
        context_identifier="Body",
        target_view="MODEL_VIEW",
        parent=model_context,
    )
    site = ifcopenshell.api.root.create_entity(
        model, ifc_class="IfcSite", name=data["site"]["name"]
    )
    building = ifcopenshell.api.root.create_entity(
        model, ifc_class="IfcBuilding", name=data["building"]["name"]
    )
    ifcopenshell.api.aggregate.assign_object(model, products=[site], relating_object=project)
    ifcopenshell.api.aggregate.assign_object(model, products=[building], relating_object=site)

    for storey_data in data.get("storeys", []):
        name = storey_data.get("name")
        if not name:
            raise ValueError("every storey needs a name")
        elevation = require_number(storey_data.get("elevation_m"), f"{name}.elevation_m")
        storey = ifcopenshell.api.root.create_entity(
            model, ifc_class="IfcBuildingStorey", name=name
        )
        storey.Elevation = elevation
        ifcopenshell.api.aggregate.assign_object(
            model, products=[storey], relating_object=building
        )

        for wall_data in storey_data.get("walls", []):
            wall_name = wall_data.get("name")
            if not wall_name:
                raise ValueError(f"wall in {name} needs a name")
            p1 = xy(wall_data.get("p1_m"), f"{wall_name}.p1_m")
            p2 = xy(wall_data.get("p2_m"), f"{wall_name}.p2_m")
            length = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            if length <= 0.0:
                raise ValueError(f"{wall_name}: p1_m and p2_m must differ")
            base_z = require_number(
                wall_data.get("base_elevation_m"), f"{wall_name}.base_elevation_m"
            )
            height = require_number(wall_data.get("height_m"), f"{wall_name}.height_m", positive=True)
            thickness = require_number(
                wall_data.get("thickness_m"), f"{wall_name}.thickness_m", positive=True
            )
            wall = ifcopenshell.api.root.create_entity(
                model, ifc_class="IfcWall", name=wall_name
            )
            ifcopenshell.api.geometry.create_2pt_wall(
                model,
                element=wall,
                context=body_context,
                p1=p1,
                p2=p2,
                elevation=base_z,
                height=height,
                thickness=thickness,
                is_si=True,
            )
            ifcopenshell.api.spatial.assign_container(
                model, products=[wall], relating_structure=storey
            )

            dx, dy = (p2[0] - p1[0]) / length, (p2[1] - p1[1]) / length
            angle = math.atan2(dy, dx)
            for opening_data in wall_data.get("openings", []):
                opening_name = opening_data.get("name")
                if not opening_name:
                    raise ValueError(f"opening in {wall_name} needs a name")
                station = require_number(opening_data.get("station_m"), f"{opening_name}.station_m")
                sill = require_number(opening_data.get("sill_m"), f"{opening_name}.sill_m")
                width = require_number(opening_data.get("width_m"), f"{opening_name}.width_m", positive=True)
                opening_height = require_number(
                    opening_data.get("height_m"), f"{opening_name}.height_m", positive=True
                )
                depth = require_number(
                    opening_data.get("opening_depth_m"),
                    f"{opening_name}.opening_depth_m",
                    positive=True,
                )
                if depth <= thickness:
                    raise ValueError(f"{opening_name}: opening_depth_m must exceed host wall thickness")
                if station < 0.0 or station + width > length:
                    raise ValueError(f"{opening_name}: opening station/width must fit along the wall")
                if sill < 0.0 or sill + opening_height > height:
                    raise ValueError(f"{opening_name}: sill and height must fit within the wall")

                opening = ifcopenshell.api.root.create_entity(
                    model, ifc_class="IfcOpeningElement", name=opening_name
                )
                representation = ifcopenshell.api.geometry.add_wall_representation(
                    model,
                    context=body_context,
                    length=width,
                    height=opening_height,
                    thickness=depth,
                )
                ifcopenshell.api.geometry.assign_representation(
                    model, product=opening, representation=representation
                )
                # API wall solids extend in local +Y; center an over-depth void on the host thickness.
                cx = p1[0] + station * dx
                cy = p1[1] + station * dy
                lateral = (thickness - depth) / 2.0
                tx = cx - lateral * dy
                ty = cy + lateral * dx
                matrix = np.asarray([
                    [math.cos(angle), -math.sin(angle), 0.0, tx],
                    [math.sin(angle), math.cos(angle), 0.0, ty],
                    [0.0, 0.0, 1.0, base_z + sill],
                    [0.0, 0.0, 0.0, 1.0],
                ], dtype=float)
                ifcopenshell.api.geometry.edit_object_placement(
                    model, product=opening, matrix=matrix, is_si=True
                )
                ifcopenshell.api.feature.add_feature(
                    model, feature=opening, element=wall
                )

    georef = data.get("georeference")
    if georef is not None:
        crs = georef.get("projected_crs")
        operation = georef.get("coordinate_operation")
        required = {
            "Eastings", "Northings", "OrthogonalHeight",
            "XAxisAbscissa", "XAxisOrdinate", "Scale",
        }
        if not crs or not required.issubset(operation or {}):
            raise ValueError("georeference needs a CRS name and all map-conversion values")
        ifcopenshell.api.georeference.add_georeferencing(model, name=crs)
        ifcopenshell.api.georeference.edit_georeferencing(
            model,
            projected_crs={"Name": crs},
            coordinate_operation=operation,
        )
    return model


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_ifc", type=Path)
    args = parser.parse_args()
    if args.output_ifc.exists():
        raise FileExistsError(f"Refusing to overwrite existing IFC: {args.output_ifc}")
    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    model = make_model(data)
    args.output_ifc.parent.mkdir(parents=True, exist_ok=True)
    model.write(str(args.output_ifc))


if __name__ == "__main__":
    main()
