---
name: geopogo-curtain-walls
description: Build and refine curtain walls, storefronts, glazing, mullions, and arched-top windows in Revit through the geopogo-ai connector. Use when the user wants a glass facade, curtain wall grid, mullion pattern, storefront, arched or round-top windows, or wants to edit a curtain wall's panels, grid spacing, or vertical profile.
---

# Geopogo — Curtain Walls, Mullions & Arched Windows

Follow `geopogo-conventions` first (inspect, units, active view, read-back). This skill covers glass facades and the specific tricks that took several iterations to get right.

## Create the curtain wall

1. Inspect: `get_curtain_walls`, `get_curtain_wall_grid`, `get_curtain_panel_types`, `get_mullion_types`.
2. Create the wall with `create_wall` (or `create_walls_batch`) using a curtain-wall type. Confirm the type name exactly via `get_element_types`.
3. Set the grid: use `get_curtain_wall_grid` to read current divisions, then `add_curtain_grid_line` / `move_curtain_grid_line` / `remove_curtain_grid_line` to hit the target bay spacing. For a regular pattern, prefer setting the type's vertical/horizontal grid spacing parameters over placing lines one by one.

## Mullions — set them on the TYPE

To mullion an entire facade in one shot, assign the mullion profile on the **curtain-wall type**, not per panel. Setting mullions on the "Exterior Glazing" (or equivalent) type propagates to every panel that uses it — hundreds of panels update from a single call.

Sequence:

1. `get_mullion_types` to find a profile (e.g. `1.5" x 2.5" rectangular`).
2. `set_element_parameter` on the curtain-wall type to assign the **vertical** interior/border mullion.
3. Read back with `get_element_parameters` to confirm the profile took.

### Known limit: horizontal mullions

The connector can only set the **vertical** mullion group. Revit stores horizontal and vertical mullions under two parameters that share the display name "Interior Type", and the set-parameter tool always writes the vertical one (it rejects the internal parameter name too). So:

- Apply vertical mullions via the connector.
- Tell the user horizontal mullion **bars** require a one-time manual step: select any panel → Edit Type on the glazing type → under **Horizontal Mullions** set Interior/Border to the same profile. That edit propagates to every panel.
- Note that the horizontal grid still reads visually through per-floor panel joints and projecting slab edges even without horizontal bars.

## Arched / round-top windows

Two routes depending on how the base is built.

### Route A — curtain panels with arched tops (`set_wall_profile`)

Newer Geopogo builds expose `set_wall_profile`, which edits a wall/panel's **vertical silhouette** — this is what makes arched tops possible. (Older builds lacked it; if it's absent, run `get_geopogo_version` and fall back to Route B or a manual Edit Profile.)

1. Identify the base storefront/curtain segments with `get_curtain_walls` / `get_elements`.
2. Use `set_wall_profile` to replace the top edge of each segment with a semicircular arc — set the springline just above the head height shown in the reference, with the arc rising to the panel top.
3. Verify with `get_wall_profile` and an `export_view_to_image` from elevation.

### Route B — masonry base with punched arched windows

If the look is arched openings in solid stone (not glazed curtain wall):

1. Create the base as a solid wall (`create_wall` with a masonry/stone type; set material via `set_compound_layer_material` or `paint_face`).
2. `load_family` for an arched / round-top window family (Revit's "Window - Round Top" / "Arch" families, or a supplied family file).
3. Place openings with `create_window` / `create_window_array` along the frontage at the bay spacing and head height in the reference; set the head height so the arch springline lands where the photo shows it.

## Glazing appearance

Tint or set glass with `create_material` + `set_material_color`, then apply via `set_compound_layer_material` on the panel type or `paint_face` on specific panels. Set the type once so all panels update together.

## Finish

Re-query counts and spacing, then `export_view_to_image` so the user can compare against their reference. Report the vertical-mullion state and flag the horizontal-mullion manual step explicitly.
