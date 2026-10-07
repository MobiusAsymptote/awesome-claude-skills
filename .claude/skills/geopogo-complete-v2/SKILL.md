---
name: geopogo-complete-v2
description: Complete Geopogo/Revit workflow reference through the geopogo-ai MCP connector — conventions, curtain walls, houses/roofs, site context, and tower massing (field-tested), plus structural framing/foundations, MEP systems, documentation/sheets, and rooms/parts/model coordination (new, drafted from the connector's full tool set). Load at the start of any Geopogo/Revit modeling task, whatever the building type or discipline.
---

# Geopogo — Complete Revit Connector Reference (V2)

This is the full accumulated Geopogo skill set: everything learned from actual modeling sessions, plus new workflow areas covering the rest of what the `geopogo-ai` connector exposes.

**Two parts, two confidence levels — read the labels before you rely on a section:**

- **Part I — Field-Tested Workflows** (§1–5). Built from real sessions. The cautions, "known limits," and gotchas here are confirmed — things like the roof active-view bug or the horizontal-mullion connector limitation actually happened and were worked around.
- **Part II — New Workflows** (§6–9). Drafted by mapping the connector's remaining tools (structural, MEP, documentation, coordination) into the same conventions and style as Part I. These have **not** been run against a live Revit session. Treat their sequences as a reasonable starting point, not a proven path — verify empirically and update this doc once they've been battle-tested, the same way §1–5 were.

Always start with §1 (Working Conventions) regardless of which workflow you need — every other section builds on it.

**Contents:** 1. Working Conventions · 2. Curtain Walls, Mullions & Arched Windows · 3. House + Roof · 4. Site Context · 5. High-Rise Tower Massing · 6. Structural Framing & Foundations · 7. MEP Systems · 8. Documentation & Sheets · 9. Rooms, Parts & Model Coordination

---

# Part I — Field-Tested Workflows

## 1. Working Conventions

These are the ground rules for driving Revit through the `geopogo-ai` connector. Follow them for every modeling task; every other section builds on top of these.

### 1.1 Always inspect before you build

Never assume model state. At the start of a task call, in this order as needed:

1. `get_model_info` — file name, active view, discipline.
2. `get_levels` — existing levels and elevations (you place most elements by level).
3. `get_element_types` / `get_family_types` — the exact type names available. Type names must match exactly; a wrong name returns a null/"Value cannot be null" error.
4. `get_elements` or the category getters (`get_walls` via `get_elements`, `get_curtain_walls`, `get_rooms`, etc.) to see what already exists.

Match the user's intent to real type names that exist in the model. If the needed type is missing, load it with `load_family` (or duplicate an existing type with `duplicate_element_type`) before creating elements.

### 1.2 Units

The connector expects **decimal feet** for lengths and coordinates unless a tool documents otherwise. Confirm project units with `get_project_units` when the user gives metric dimensions, and convert before calling. When a user states a size (e.g. "20 ft tall", "6 windows per façade"), treat those as hard targets — model them exactly, then verify (see below).

### 1.3 The active view matters

Several creation tools require a specific **active view type**, not the 3D view:

- **Floors and walls** work in a 3D view.
- **`create_roof` requires a floor PLAN view active.** Creating a roof from the 3D view fails with "Value cannot be null" even when the footprint and type are valid. Switch with `set_active_view` to the relevant plan (e.g. "L2 - Architectural") first. If `set_active_view` is unavailable in the installed build, ask the user to double-click the plan view in the Project Browser, then retry.
- Plan-based annotation (dimensions, tags, detail lines) needs the corresponding plan/section view active.

If a creation call fails with a null error and the inputs look correct, suspect the active view before suspecting your geometry. Confirm by running the identical footprint through `create_floor` — if the floor succeeds, the geometry is fine and the problem is the view or the command.

### 1.4 Prefer type-level edits for repeated elements

When a change should apply to many elements at once (all curtain panels, all mullions, a whole wall type), set it on the **element type**, not each instance. Editing the "Exterior Glazing" curtain-wall type propagates to every panel that uses it in one call — far faster and more consistent than looping instances.

### 1.5 Read back and verify

Do not trust that a call worked because it returned. After a batch of creation/edit calls:

- Re-query with the relevant getter (`get_elements`, `get_element_parameters`) to confirm counts, spacing, and dimensions match the stated intent.
- Use `verify_model` when available for an overall integrity check.
- Use `export_view_to_image` to produce a render the user can eyeball against their reference.

Report actual measured results, and call out any gap between what was asked and what the model now contains.

### 1.6 Known connector limits (state them honestly)

- **Horizontal curtain-wall mullions can't be set through the connector.** Revit stores horizontal and vertical mullions under two parameters that share the display name "Interior Type", and `set_element_parameter` only reaches the vertical group (it rejects the internal name too). Set vertical mullions via the connector; tell the user horizontal mullions need a one-time manual Edit Type in Revit.
- **Family authoring is not exposed.** You can `load_family` and place instances, but you cannot create or edit the internal geometry of a family from the connector.
- **`run_revit_command` only fires built-in menu commands** (Save, etc.), not geometry authoring.

When something isn't reachable, say so plainly and give the shortest reliable manual path in Revit, rather than repeatedly retrying a call that can't succeed. Offer an on-screen walkthrough when a manual sketch step is unavoidable.

### 1.7 Check the build

If a tool the user expects is missing, call `get_geopogo_version` and report the version and tool count so they can tell whether it's a build/version gap versus a usage issue.

---

## 2. Curtain Walls, Mullions & Arched Windows

Follow §1 first. This covers glass facades and the specific tricks that took several iterations to get right.

### 2.1 Create the curtain wall

1. Inspect: `get_curtain_walls`, `get_curtain_wall_grid`, `get_curtain_panel_types`, `get_mullion_types`.
2. Create the wall with `create_wall` (or `create_walls_batch`) using a curtain-wall type. Confirm the type name exactly via `get_element_types`.
3. Set the grid: use `get_curtain_wall_grid` to read current divisions, then `add_curtain_grid_line` / `move_curtain_grid_line` / `remove_curtain_grid_line` to hit the target bay spacing. For a regular pattern, prefer setting the type's vertical/horizontal grid spacing parameters over placing lines one by one.

### 2.2 Mullions — set them on the TYPE

To mullion an entire facade in one shot, assign the mullion profile on the **curtain-wall type**, not per panel. Setting mullions on the "Exterior Glazing" (or equivalent) type propagates to every panel that uses it — hundreds of panels update from a single call.

Sequence:

1. `get_mullion_types` to find a profile (e.g. `1.5" x 2.5" rectangular`).
2. `set_element_parameter` on the curtain-wall type to assign the **vertical** interior/border mullion.
3. Read back with `get_element_parameters` to confirm the profile took.

**Known limit: horizontal mullions.** The connector can only set the **vertical** mullion group (see §1.6). Apply vertical mullions via the connector; tell the user horizontal mullion **bars** require a one-time manual step: select any panel → Edit Type on the glazing type → under **Horizontal Mullions** set Interior/Border to the same profile. That edit propagates to every panel. The horizontal grid still reads visually through per-floor panel joints and projecting slab edges even without horizontal bars.

### 2.3 Arched / round-top windows

Two routes depending on how the base is built.

**Route A — curtain panels with arched tops (`set_wall_profile`).** Newer Geopogo builds expose `set_wall_profile`, which edits a wall/panel's **vertical silhouette** — this is what makes arched tops possible. (Older builds lacked it; if it's absent, run `get_geopogo_version` and fall back to Route B or a manual Edit Profile.)

1. Identify the base storefront/curtain segments with `get_curtain_walls` / `get_elements`.
2. Use `set_wall_profile` to replace the top edge of each segment with a semicircular arc — set the springline just above the head height shown in the reference, with the arc rising to the panel top.
3. Verify with `get_wall_profile` and an `export_view_to_image` from elevation.

**Route B — masonry base with punched arched windows.** If the look is arched openings in solid stone (not glazed curtain wall):

1. Create the base as a solid wall (`create_wall` with a masonry/stone type; set material via `set_compound_layer_material` or `paint_face`).
2. `load_family` for an arched / round-top window family (Revit's "Window - Round Top" / "Arch" families, or a supplied family file).
3. Place openings with `create_window` / `create_window_array` along the frontage at the bay spacing and head height in the reference; set the head height so the arch springline lands where the photo shows it.

### 2.4 Glazing appearance

Tint or set glass with `create_material` + `set_material_color`, then apply via `set_compound_layer_material` on the panel type or `paint_face` on specific panels. Set the type once so all panels update together.

### 2.5 Finish

Re-query counts and spacing, then `export_view_to_image` so the user can compare against their reference. Report the vertical-mullion state and flag the horizontal-mullion manual step explicitly.

---

## 3. House + Roof

Follow §1 first. This is the residential shell pipeline, with the roof gotcha that repeatedly bites.

### 3.1 Levels

Create the levels the house needs (e.g. L1, L2, Roof) with `create_level` / `create_building_levels`, then `get_levels` to confirm elevations. Set floor-to-floor to the user's stated height (default ~9–10 ft residential if unstated — confirm).

### 3.2 Walls and floors

1. Exterior walls: `create_walls_batch` around the footprint on L1 (and L2 if multi-story), using a real wall type from `get_element_types`.
2. Floor slab: `create_floor` with the footprint at each level. Floors create fine in the 3D view.
3. Interior partitions if requested: `create_walls_batch`.

### 3.3 Roof — mind the active view

`create_roof` builds a footprint roof, but it has a hard requirement:

- **`create_roof` requires a floor PLAN view to be active.** From a 3D view it fails with "Value cannot be null" for every valid footprint and type — even though `create_floor` accepts the identical footprint. This is the single most common roof failure.
- Switch with `set_active_view` to the roof/top plan (e.g. "L2 - Architectural"). If the installed build can't switch views via the API, ask the user to double-click that plan view in the Project Browser, then retry.
- The footprint auto-closes, so pass the corner points without repeating the first point.
- For a gable: set the slope-defining edges (the two long eave edges get the pitch, e.g. 6:12; the gable ends stay vertical). For a hip: all edges slope. Set the roof type from `get_element_types` (name must match exactly).

**Fallback when `create_roof` is broken in the build.** If `create_roof` still returns null after a confirmed plan-view + a plugin reload/Revit restart, treat the command as broken in that build rather than hammering it. Fall back to modeling the roof form with `create_mass_extrusion` (extrude the gable cross-section along the ridge) to give a correct silhouette, and advise the user to report the `create_roof` bug to the Geopogo team with the version from `get_geopogo_version`.

### 3.4 Openings

- Doors: `create_door` on the host wall at the right location/level.
- Windows: `create_window`, or `create_window_array` for a regular row at fixed spacing and sill height.
- For a wall opening without a family, `create_wall_opening`.

### 3.5 Verify and render

Re-query wall/floor/opening counts and the roof pitch; confirm dimensions match what was asked. `verify_model`, then `export_view_to_image` from 3D for review. If the roof used the mass-extrusion fallback, say so and note it's a massing stand-in, not a true Revit roof object.

---

## 4. Site Context

Follow §1 first. This covers the ground plane and streetscape around a building.

### 4.1 Topography / ground

1. `get_topography` to see any existing surface.
2. `create_topography` for the ground plane. Supply the boundary points and elevations; keep it flat unless the user wants grade. Reference the building's L1 elevation so the ground meets the base cleanly.

### 4.2 Streets, curbs, sidewalks

These are best built as thin floor slabs or masses at the right elevations, layered from the roadway up:

- **Roadway**: a `create_floor` slab (asphalt material) at street level across the right-of-way.
- **Curb**: a low `create_wall` or thin `create_mass_extrusion` run along the roadway edge, typically ~6 in above the road.
- **Sidewalk**: a `create_floor` slab (concrete) between curb and property line, set at curb-top elevation.
- **Intersection**: repeat the roadway slab on the crossing axis and merge/`join_geometry` where they meet; wrap curbs and sidewalks around the corners with the appropriate radius.

Assign materials with `create_material` + `set_material_color`, applied via `set_compound_layer_material` or `paint_face`, so asphalt/concrete/paint read distinctly.

### 4.3 Site components

Populate with `place_site_component` (trees, benches, cars, lights) and `create_component` for loaded families. Use `get_loaded_families` first; `load_family` anything missing.

### 4.4 Verify and render

Confirm elevations line up (no floating curbs, sidewalk flush to curb top), `verify_model`, then `export_view_to_image` from a 3D or perspective view. Check that the ground meets the building base and the streetscape reads at human scale.

---

## 5. High-Rise Tower Massing

Follow §1 first. This is the mass → floors → skin → core pipeline used to build towers like Salesforce Tower and 30-story office/hotel forms.

### 5.1 Levels first

Towers live or die on levels. Create the full level stack up front:

- Use `create_building_levels` (fastest — makes N levels at a set floor-to-floor height in one call) when available, or loop `create_level`.
- Confirm with `get_levels`. Every floor, wall, and curtain segment references these, so get the count and elevations right before modeling anything else.

### 5.2 Massing form

For anything other than a plain box, start from a mass:

1. `create_mass_box` for a simple prism, or `create_mass_extrusion` for a shaped footprint, or `create_blend` for a tapering/crowned form (e.g. a tapered crown or setback top).
2. Generate `create_mass_floors` at each level so the mass has floor divisions.
3. Convert to building elements with `mass_to_building_elements` (floors + facades from the mass faces), or use the mass purely as a guide and place elements against it.

For a straight extruded tower you can skip the mass and go straight to floors + curtain walls per level.

### 5.3 Floors

Create a floor slab at each level with `create_floor` using the level's footprint. Floors work in the 3D view. Verify slab count equals level count.

### 5.4 Curtain-wall skin

Wrap the tower in glazing. See §2 for the mullion details — the key points for a tower:

- Create the curtain walls per elevation (or `create_walls_batch`), using one curtain-wall type across the whole tower.
- **Set mullions and glazing on the TYPE**, not per panel — one edit updates all ~hundreds of panels. Only the vertical mullion group is reachable through the connector; horizontal mullion bars need a one-time manual Edit Type (see §2.2).
- For a crown or setback, adjust the top segments' grid/profile separately.

### 5.5 Core

Add a service core: interior walls (`create_walls_batch`) enclosing the elevator/stair shaft, and stairs with `create_stairs` (see §6.6 for stairs/railings detail). Place structural columns with `create_column` on a grid (`create_grid`) if the user wants structure — see §6 for the full structural sequence.

### 5.6 Verify and render

- Re-query: floor count, level count, panel spacing — confirm they match the stated program (e.g. "30 stories, 6 bays per face").
- `verify_model` for integrity.
- `export_view_to_image` from a 3D view for the user to review, and iterate on glazing tint / mullion spacing / crown.

State honestly where the connector fell short (e.g. horizontal mullions) and give the manual step.

---

# Part II — New Workflows (Drafted, Not Yet Battle-Tested)

The sections below cover the rest of what `geopogo-ai` exposes — structure, MEP, documentation, and model coordination. They follow the same conventions as Part I, but unlike §1–5, they haven't been run against a live Revit session. Verify each sequence empirically before treating any caution here as a confirmed limit the way §1.6 is; update the status once a section has been through real use.

## 6. Structural Framing & Foundations

Covers the load-bearing side of a model — grid, frame, foundations, reinforcement, and stairs — which §3 and §5 reference but don't detail. Use when the user wants a structural grid, framing, columns, beams, footings, foundations, rebar/reinforcement, or stairs and railings for vertical circulation.

### 6.1 Lay out the grid first

Structural elements are almost always placed relative to a grid, so build it before columns or beams:

1. `get_grids` to see what already exists — don't duplicate a grid the user already has.
2. `create_grid` for each column line (numbered/lettered per the user's convention, e.g. 1–8 and A–D). Grids are 2D reference lines that span all levels, so you typically only create each line once regardless of story count.
3. Confirm with `get_grids` that spacing matches the stated bay dimensions.

### 6.2 Levels and framing types

Structural framing depends on the level stack being right first — see §1 and §5.1 for `create_level` / `create_building_levels`. Before placing anything, check `get_structural_elements` (what's already framed) and `get_element_types` / `get_family_types` for the exact column, beam, and foundation type names — as elsewhere, a mismatched type name fails rather than substituting a default.

### 6.3 Columns and beams

1. Place vertical structure with `create_column` at each grid intersection (or at the specific points the user gives), one level at a time. Set the type from `get_element_types` (e.g. a concrete or steel section).
2. Span beams between columns with `create_beam`, snapping endpoints to grid intersections or column centerlines so the frame reads as continuous.
3. For a repetitive bay pattern, loop the grid intersections programmatically rather than placing each column by hand-picked coordinates — it's the more reliable way to keep spacing exact.
4. `join_geometry` where columns meet beams/foundations if the connector leaves a visible seam — join is a targeted per-pair operation, not something that runs automatically.

### 6.4 Foundations

Pick the foundation type to match what's structurally under each vertical element:

- **Isolated footing under a single column**: `create_isolated_foundation` at the column base point. Check `get_element_types` for the footing family/type first.
- **Continuous footing under a bearing wall**: `create_wall_foundation` along the wall; `get_wall_foundation_types` lists what profiles are available for the host wall type — the foundation type must be compatible with the wall it's hosted on.
- **Mat/raft slab under a whole core or tower base**: `create_mat_foundation` across the footprint, typically at the lowest level.

Set foundation top elevation to meet the lowest level's structural floor, and verify with `get_structural_elements` that count and location match one footing per column (or one continuous run per bearing wall).

### 6.5 Rebar

Reinforcement is placed inside a host element (foundation, column, wall, or beam), so create the host first:

1. `get_rebar_bar_types` and `get_rebar_shapes` to see what bar sizes/shapes are loaded — load more via `load_family` if the spec calls for something not present.
2. `create_rebar` inside the target host, matching the shape/size/spacing the user or the structural spec calls for (e.g. bar size, cover, spacing along the run).
3. Rebar is detail-heavy — if the user only wants a schematic/coordination model, confirm before spending calls on exact bar-by-bar placement; a simplified representative cage is often enough unless they explicitly want construction-documentation-level rebar.

### 6.6 Stairs and railings

Vertical circulation for a structural core or any multi-level building:

1. `create_stairs` between two levels, setting the run/landing geometry to fit the shaft or stair enclosure. Confirm the base and top level are correct — stairs that don't reach the intended level are a common miss.
2. `create_railing` along open edges (stair runs, landings, floor openings, balconies). Pick the railing type from `get_element_types`.
3. For a full core (elevators + stairs + shaft walls), coordinate this with the enclosing walls from `create_walls_batch` — see §5.5.

### 6.7 Verify and render

- Re-query `get_structural_elements` / `get_grids` to confirm column/beam/footing counts match the program (e.g. one column per grid intersection per level, one footing per ground-level column).
- `verify_model` for overall integrity, and check `get_model_warnings` — structural clashes (unjoined geometry, floating footings) often surface there before they're visible in a render.
- `export_view_to_image` from a 3D or structural view for the user to review the frame.

Report actual placed counts against what was asked, and flag anything you simplified (e.g. schematic rebar instead of full detailing) so the user knows where to expect more work before construction documents.

---

## 7. MEP Systems

Covers mechanical, electrical, and plumbing modeling. Use when the user wants HVAC ductwork, plumbing/piping, electrical conduit or fixtures, MEP routing, or MEP spaces coordinated with rooms. MEP work is routing-heavy: get the host geometry and levels right before running any duct, pipe, or conduit, since every run needs real connection points to land on.

### 7.1 Inspect before routing

MEP elements connect to fixtures, equipment, and each other, so confirm what's already in the model before adding runs:

1. `get_mep_systems` — existing systems (supply air, sanitary, power, etc.) so new runs join the right system rather than creating a stray duplicate.
2. `get_mep_spaces` — MEP spaces, which are the mechanical/electrical counterpart to architectural rooms and drive loads and equipment sizing. `get_room_at_point` can confirm which architectural room a given point falls in if you need to cross-reference.
3. `get_electrical_fixtures` and `get_electrical_systems` for existing devices and circuits.
4. `get_element_types` / `get_family_types` for the duct/pipe/conduit types and sizes available, and `load_family` anything the spec calls for that isn't loaded (diffusers, panels, fixtures).

### 7.2 Ducts, pipes, and conduit

All three follow the same pattern: define a path of points at the right elevation, and a system/type.

- **Ductwork**: `create_duct` along the route, sized and typed per the mechanical schedule (e.g. supply vs. return). Route above ceiling or in a shaft per the level's clear height — check the level-to-level height before assuming clearance.
- **Piping**: `create_pipe` for domestic water, sanitary, or process runs. Slope-sensitive systems (sanitary/storm) need correct start/end elevations for gravity flow — don't route them dead level unless the user explicitly wants a pressurized system.
- **Conduit**: `create_conduit` for electrical raceway runs between panels, devices, and junction points.

For all three, place runs level by level and re-check `get_mep_systems` after each batch so you can confirm the run actually joined the intended system rather than creating an orphaned segment.

### 7.3 Electrical fixtures and systems

1. Place devices (outlets, panels, light fixtures, equipment) with `create_component` using a loaded electrical family, or the connector's fixture-placement path if one exists for the category — confirm with `get_electrical_fixtures` after placing.
2. Circuit relationships and panel assignments are read via `get_electrical_systems`; if the connector doesn't expose a direct circuiting call, note that circuiting may need to be finished manually in Revit's Electrical panel schedule and say so plainly rather than guessing at a call that isn't there.

### 7.4 MEP spaces vs. architectural rooms

MEP spaces are a separate object from rooms even when they share a boundary — a room can exist with no space, or vice versa. If the user asks for load calculations, equipment sizing, or space-based tagging, confirm spaces exist (`get_mep_spaces`) and match the architectural rooms (`get_rooms`, `get_room_at_point`) before proceeding; don't assume one implies the other.

### 7.5 Verify and render

- Re-query `get_mep_systems`, `get_electrical_systems`, and the category getters to confirm run counts and connectivity match what was requested (e.g. "supply duct from AHU to every diffuser on L2").
- `verify_model` and check `get_model_warnings` — MEP models commonly surface unconnected segments, disconnected systems, and clash warnings here before they're visible in a 3D render.
- `export_view_to_image` from a 3D or MEP-discipline view so the user can review routing.

State plainly anything the connector can't do end-to-end (e.g. detailed circuit load balancing, fixture-unit sizing) and point to the manual step in Revit rather than approximating a result that looks right but isn't engineered.

---

## 8. Documentation & Sheets

Covers turning a model into drawing output: views, sheets, annotation, schedules, and revisions. Use when the user wants a sheet set, construction documents, a schedule, dimensioning, tagging, a revision cloud, or wants a view's appearance, scale, crop, or graphic overrides changed.

### 8.1 Views before sheets

A sheet is just a placeholder until views are placed on it, so create/prepare views first:

1. `get_views` to see what exists — reuse an existing view rather than duplicating one that already shows what's needed.
2. Create the views the drawing set needs: `create_floor_plan`, `create_ceiling_plan`, `create_section_view` (check `get_section_view_types` for the cut-line style available), or `create_3d_view`. Use `duplicate_view` when you need the same view at a different scale/filter state rather than a fresh cut.
3. Set each view's presentation: `set_view_scale`, `crop_view` (to the sheet's drawing area), `apply_view_template` (pick from `get_view_templates` for a consistent standard look), or `apply_view_filter` (pick from `get_view_filters`, or make a new one with `create_view_filter`).
4. Category-level graphics: `get_category_visibility` / `set_category_visibility` to turn whole categories on/off per view, and `set_category_graphic_override` for line weight/color/pattern overrides that apply only in that view (not the model globally — a common point of confusion, since `set_element_override` is instance-level and category overrides are view-level).

### 8.2 Sheets

1. `get_sheets` and `get_title_block_types` — confirm the title block family/type the user's set uses before creating new sheets, so numbering and border match the existing set.
2. `create_sheet` with the sheet number/name and title block type.
3. `place_view_on_sheet` for each prepared view; `get_sheet_views` afterward to confirm placement and catch any view placed on the wrong sheet.
4. `set_sheet_parameter` for sheet-specific fields (drawn by, checked by, issue date, etc.) that the title block exposes as parameters.

### 8.3 Annotation

- **Dimensions**: `create_dimension` between the reference elements/points the user specifies (wall faces, grid lines, opening edges). Dimension in the view where the geometry is actually visible — a dimension referencing hidden geometry will fail or attach to the wrong element.
- **Tags**: `tag_element` for door/window/room/equipment tags; confirm the tag family is loaded (`get_loaded_families`, `load_family` if not) and that it matches the category being tagged.
- **Text and detail graphics**: `create_text_note` for callouts and notes, `create_detail_line` for 2D linework, and `create_filled_region` / `create_drafting_filled_region` / `create_masking_region` for hatching, poché, and masking. Drafting-view-only regions (`create_drafting_filled_region`) don't reference model geometry — use them for generic details, not for anything that should track the model.
- **General**: `get_annotations` to audit what's already placed in a view before adding more, so you don't duplicate tags or dimensions.

### 8.4 Schedules

`create_schedule` for a category (doors, windows, rooms, walls, etc.), specifying the fields the user wants (mark, type, level, area, etc.). Schedules are live model queries — verify field names against `get_element_parameters` for that category first, since a schedule field name that doesn't match the model's actual parameter name will produce an empty or wrong column rather than an error.

### 8.5 Revisions

1. `get_revisions` to see the existing revision sequence — new revisions append to it, so check the last issued number/letter first.
2. `create_revision` for a new revision (number, description, date, issued-to).
3. `create_revision_cloud` around the changed area in the relevant view(s).
4. `assign_revision_to_sheet` for every sheet the change touches — a revision cloud with no sheet assignment won't show up in that sheet's revision schedule.

### 8.6 Verify and render

- Re-query `get_sheets`, `get_sheet_views`, and `get_annotations` to confirm the drawing set matches what was asked (right views on right sheets, dimensions/tags present, revision clouds assigned).
- `verify_model` for overall integrity and `get_model_warnings` for anything documentation-adjacent (e.g. unresolved tags, duplicate marks).
- `export_view_to_image` on the finished sheet(s) so the user can review layout before printing/issuing.

Report which views/sheets were touched, and flag anything that needed a workaround (e.g. a filter created because none existed, or a manual title-block field the connector couldn't set).

---

## 9. Rooms, Parts & Model Coordination

Covers the model-management layer: rooms/spaces, splitting or grouping elements, coordinating with linked/scanned data, and general element edits that don't fit elsewhere. Use when the user wants rooms named/numbered, an element split into parts or grouped into an assembly, a linked model reloaded, worksets or phases assigned, design options compared, a point-cloud scan referenced, or a model exported to IFC.

### 9.1 Rooms

1. `get_rooms` to see what's already placed, and `get_room_at_point` to check whether a given point already falls inside a room boundary before adding one.
2. `create_room` inside a bounded area (walls must form a closed loop for the room to compute correctly — an open boundary produces an "unbounded" room with no area).
3. `set_room_name_number` to assign the name/number the user gives, or to match a numbering scheme (e.g. floor-prefixed: 201, 202...).
4. If the user also needs MEP load/space data tied to these rooms, see §7.4 (`get_mep_spaces`) — rooms and MEP spaces are separate objects even on the same boundary.

### 9.2 Parts and assemblies

Use these when the user wants an element broken into constructible pieces or grouped for scheduling/fabrication, not for ordinary geometry creation:

- **Parts**: `create_parts` divides a host element (e.g. a floor or wall) into independently-schedulable/paintable pieces — typical for phased construction or multi-material walls. `get_parts` lists what's already split.
- **Assemblies**: `create_assembly` groups selected elements into a single schedulable/callable unit (e.g. a precast panel with its embeds). `get_assemblies` lists existing ones; `disassemble_assembly` reverses the grouping if the user wants the elements back to independent status.

Check `get_groups` / `get_group_types` if the user means a model **group** (a reusable, repeatable cluster of elements) rather than an assembly (a fabrication/scheduling unit) — the two are easy to conflate but serve different purposes, and the connector's write path differs (assemblies have dedicated create/disassemble calls; groups here are read-only via the connector, so creating a new group type is a manual Revit step).

### 9.3 Linked models

1. `get_linked_models`, `get_rvt_links`, and `get_cad_links` to see what's already linked before adding or troubleshooting a link.
2. `reload_rvt_link` after the linked file has been updated externally, so the current session reflects the latest coordination model.
3. `unload_rvt_link` to temporarily drop a link (for performance or to isolate a discipline) without deleting the link itself.
4. When placing new elements near a link, position them relative to the link's shared coordinates, and call out to the user if alignment looks off — the connector doesn't auto-correct link placement.

### 9.4 Point clouds

1. `get_point_clouds` to see what scan data is attached.
2. `query_point_cloud_slice` to sample the scan at a given elevation/region — useful for checking as-built dimensions against the model before placing new geometry (e.g. confirming an existing wall location before adding a footing under it).
3. `set_point_cloud_visibility` to toggle the scan on/off per view so it doesn't clutter documentation views.

### 9.5 Worksets, phases, and design options

- **Worksets**: `get_worksets` to see the workset structure (this only matters in workshared/central models); `set_element_workset` to assign new or moved elements to the right discipline workset.
- **Phases**: `get_phases` to see the project's phase list (existing, demo, new construction, etc.); `set_element_phase` so new elements are correctly flagged as "New Construction" (or whatever phase applies) rather than defaulting to whatever phase is currently active in the view.
- **Design options**: `get_design_option_sets` and `get_design_options` to see what alternatives exist for a given area before adding elements — placing new geometry while the wrong design option is current will put it in the wrong option silently, so confirm before batch-creating.

### 9.6 General element editing

These utilities apply across every category and are handy once elements already exist:

- **Transform**: `move_element`, `rotate_element`, `mirror_element`, `copy_element` for repositioning/duplicating without re-creating from scratch.
- **Type changes**: `change_element_type` to swap an instance to a different existing type; `duplicate_element_type` to create a new type (e.g. a variant with different parameters) without affecting the original.
- **Cleanup**: `delete_element` for removals, `join_geometry` to clean up seams between adjoining elements (walls/floors/foundations), and `set_element_override` for instance-level graphic overrides (view-level category overrides are `set_category_graphic_override` — see §8.1).
- Always re-query (`get_elements` / `get_element_parameters`) after a batch of edits to confirm the count and state match intent, same as any other workflow.

### 9.7 Export and verify

- `export_to_ifc` when the user needs an open, cross-platform deliverable rather than a native Revit file — confirm which view/element set should be included, since a full-model export can be large and slow.
- `verify_model` and `get_model_warnings` before handing off — coordination issues (unresolved links, elements on the wrong workset/phase/design option) are exactly the class of problem this section's checks catch early.
- `export_view_to_image` for a quick visual sanity check when useful.

Report anything ambiguous plainly — e.g. if a linked model wasn't reloaded because the user hadn't said whether the external file changed, or if elements were left on the default workset/phase because none was specified.