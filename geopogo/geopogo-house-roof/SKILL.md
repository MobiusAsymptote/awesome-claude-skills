---
name: geopogo-house-roof
description: Model a house or small residential shell in Revit through the geopogo-ai connector — levels, exterior walls, floors, a gable/hip/flat roof, and door/window openings. Use when the user wants a house, home, tiny home, townhome, cottage, residential shell, or specifically a gable or pitched roof. Includes the plan-view requirement and mass-extrusion fallback for roofs.
---

# Geopogo — House + Roof

Follow `geopogo-conventions` first. This is the residential shell pipeline, with the roof gotcha that repeatedly bites.

## 1. Levels

Create the levels the house needs (e.g. L1, L2, Roof) with `create_level` / `create_building_levels`, then `get_levels` to confirm elevations. Set floor-to-floor to the user's stated height (default ~9–10 ft residential if unstated — confirm).

## 2. Walls and floors

1. Exterior walls: `create_walls_batch` around the footprint on L1 (and L2 if multi-story), using a real wall type from `get_element_types`.
2. Floor slab: `create_floor` with the footprint at each level. Floors create fine in the 3D view.
3. Interior partitions if requested: `create_walls_batch`.

## 3. Roof — mind the active view

`create_roof` builds a footprint roof, but it has a hard requirement:

- **`create_roof` requires a floor PLAN view to be active.** From a 3D view it fails with "Value cannot be null" for every valid footprint and type — even though `create_floor` accepts the identical footprint. This is the single most common roof failure.
- Switch with `set_active_view` to the roof/top plan (e.g. "L2 - Architectural"). If the installed build can't switch views via the API, ask the user to double-click that plan view in the Project Browser, then retry.
- The footprint auto-closes, so pass the corner points without repeating the first point.
- For a gable: set the slope-defining edges (the two long eave edges get the pitch, e.g. 6:12; the gable ends stay vertical). For a hip: all edges slope. Set the roof type from `get_element_types` (name must match exactly).

### Fallback when `create_roof` is broken in the build

If `create_roof` still returns null after a confirmed plan-view + a plugin reload/Revit restart, treat the command as broken in that build rather than hammering it. Fall back to modeling the roof form with `create_mass_extrusion` (extrude the gable cross-section along the ridge) to give a correct silhouette, and advise the user to report the `create_roof` bug to the Geopogo team with the version from `get_geopogo_version`.

## 4. Openings

- Doors: `create_door` on the host wall at the right location/level.
- Windows: `create_window`, or `create_window_array` for a regular row at fixed spacing and sill height.
- For a wall opening without a family, `create_wall_opening`.

## 5. Verify and render

Re-query wall/floor/opening counts and the roof pitch; confirm dimensions match what was asked. `verify_model`, then `export_view_to_image` from 3D for review. If the roof used the mass-extrusion fallback, say so and note it's a massing stand-in, not a true Revit roof object.
