---
name: geopogo-tower-massing
description: Model a high-rise or mid-rise tower in Revit through the geopogo-ai connector — from a massing form to stacked floors, a curtain-wall skin, and a core. Use when the user wants a tower, high-rise, multi-story office/hotel/residential building, a stacked-floor building from a footprint or mass, or references a named tower (e.g. Salesforce Tower).
---

# Geopogo — High-Rise Tower Massing

Follow `geopogo-conventions` first. This is the mass → floors → skin → core pipeline used to build towers like Salesforce Tower and 30-story office/hotel forms.

## 1. Levels first

Towers live or die on levels. Create the full level stack up front:

- Use `create_building_levels` (fastest — makes N levels at a set floor-to-floor height in one call) when available, or loop `create_level`.
- Confirm with `get_levels`. Every floor, wall, and curtain segment references these, so get the count and elevations right before modeling anything else.

## 2. Massing form

For anything other than a plain box, start from a mass:

1. `create_mass_box` for a simple prism, or `create_mass_extrusion` for a shaped footprint, or `create_blend` for a tapering/crowned form (e.g. a tapered crown or setback top).
2. Generate `create_mass_floors` at each level so the mass has floor divisions.
3. Convert to building elements with `mass_to_building_elements` (floors + facades from the mass faces), or use the mass purely as a guide and place elements against it.

For a straight extruded tower you can skip the mass and go straight to floors + curtain walls per level.

## 3. Floors

Create a floor slab at each level with `create_floor` using the level's footprint. Floors work in the 3D view. Verify slab count equals level count.

## 4. Curtain-wall skin

Wrap the tower in glazing. See the `geopogo-curtain-walls` skill for the mullion details — the key points for a tower:

- Create the curtain walls per elevation (or `create_walls_batch`), using one curtain-wall type across the whole tower.
- **Set mullions and glazing on the TYPE**, not per panel — one edit updates all ~hundreds of panels. Only the vertical mullion group is reachable through the connector; horizontal mullion bars need a one-time manual Edit Type (see curtain-walls skill).
- For a crown or setback, adjust the top segments' grid/profile separately.

## 5. Core

Add a service core: interior walls (`create_walls_batch`) enclosing the elevator/stair shaft, and stairs with `create_stairs`. Place structural columns with `create_column` on a grid (`create_grid`) if the user wants structure.

## 6. Verify and render

- Re-query: floor count, level count, panel spacing — confirm they match the stated program (e.g. "30 stories, 6 bays per face").
- `verify_model` for integrity.
- `export_view_to_image` from a 3D view for the user to review, and iterate on glazing tint / mullion spacing / crown.

State honestly where the connector fell short (e.g. horizontal mullions) and give the manual step.
