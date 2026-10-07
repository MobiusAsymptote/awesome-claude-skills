---
name: geopogo-site-context
description: Add site and urban context around a building in Revit through the geopogo-ai connector — topography, sidewalks, curbs, streets, intersections, and site components (trees, furniture, cars). Use when the user wants a site, ground, terrain, sidewalk, curb, street, road, intersection, landscaping, or surrounding context for a model.
---

# Geopogo — Site Context

Follow `geopogo-conventions` first. This covers the ground plane and streetscape around a building.

## 1. Topography / ground

1. `get_topography` to see any existing surface.
2. `create_topography` for the ground plane. Supply the boundary points and elevations; keep it flat unless the user wants grade. Reference the building's L1 elevation so the ground meets the base cleanly.

## 2. Streets, curbs, sidewalks

These are best built as thin floor slabs or masses at the right elevations, layered from the roadway up:

- **Roadway**: a `create_floor` slab (asphalt material) at street level across the right-of-way.
- **Curb**: a low `create_wall` or thin `create_mass_extrusion` run along the roadway edge, typically ~6 in above the road.
- **Sidewalk**: a `create_floor` slab (concrete) between curb and property line, set at curb-top elevation.
- **Intersection**: repeat the roadway slab on the crossing axis and merge/`join_geometry` where they meet; wrap curbs and sidewalks around the corners with the appropriate radius.

Assign materials with `create_material` + `set_material_color`, applied via `set_compound_layer_material` or `paint_face`, so asphalt/concrete/paint read distinctly.

## 3. Site components

Populate with `place_site_component` (trees, benches, cars, lights) and `create_component` for loaded families. Use `get_loaded_families` first; `load_family` anything missing.

## 4. Verify and render

Confirm elevations line up (no floating curbs, sidewalk flush to curb top), `verify_model`, then `export_view_to_image` from a 3D or perspective view. Check that the ground meets the building base and the streetscape reads at human scale.
