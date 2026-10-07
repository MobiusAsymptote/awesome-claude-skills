---
name: geopogo-conventions
description: Core conventions for building anything in Autodesk Revit through the geopogo-ai MCP connector. Load at the start of any Geopogo/Revit modeling task — creating walls, floors, roofs, curtain walls, levels, masses, towers, houses, or site context. Covers model inspection, units, active-view requirements, type-level edits, read-back verification, and known connector limits.
---

# Geopogo Revit — Working Conventions

These are the ground rules for driving Revit through the `geopogo-ai` connector. Follow them for every modeling task; the workflow skills (curtain walls, tower massing, house + roof, site context) build on top of these.

## Always inspect before you build

Never assume model state. At the start of a task call, in this order as needed:

1. `get_model_info` — file name, active view, discipline.
2. `get_levels` — existing levels and elevations (you place most elements by level).
3. `get_element_types` / `get_family_types` — the exact type names available. Type names must match exactly; a wrong name returns a null/"Value cannot be null" error.
4. `get_elements` or the category getters (`get_walls` via `get_elements`, `get_curtain_walls`, `get_rooms`, etc.) to see what already exists.

Match the user's intent to real type names that exist in the model. If the needed type is missing, load it with `load_family` (or duplicate an existing type with `duplicate_element_type`) before creating elements.

## Units

The connector expects **decimal feet** for lengths and coordinates unless a tool documents otherwise. Confirm project units with `get_project_units` when the user gives metric dimensions, and convert before calling. When a user states a size (e.g. "20 ft tall", "6 windows per façade"), treat those as hard targets — model them exactly, then verify (see below).

## The active view matters

Several creation tools require a specific **active view type**, not the 3D view:

- **Floors and walls** work in a 3D view.
- **`create_roof` requires a floor PLAN view active.** Creating a roof from the 3D view fails with "Value cannot be null" even when the footprint and type are valid. Switch with `set_active_view` to the relevant plan (e.g. "L2 - Architectural") first. If `set_active_view` is unavailable in the installed build, ask the user to double-click the plan view in the Project Browser, then retry.
- Plan-based annotation (dimensions, tags, detail lines) needs the corresponding plan/section view active.

If a creation call fails with a null error and the inputs look correct, suspect the active view before suspecting your geometry. Confirm by running the identical footprint through `create_floor` — if the floor succeeds, the geometry is fine and the problem is the view or the command.

## Prefer type-level edits for repeated elements

When a change should apply to many elements at once (all curtain panels, all mullions, a whole wall type), set it on the **element type**, not each instance. Editing the "Exterior Glazing" curtain-wall type propagates to every panel that uses it in one call — far faster and more consistent than looping instances.

## Read back and verify

Do not trust that a call worked because it returned. After a batch of creation/edit calls:

- Re-query with the relevant getter (`get_elements`, `get_element_parameters`) to confirm counts, spacing, and dimensions match the stated intent.
- Use `verify_model` when available for an overall integrity check.
- Use `export_view_to_image` to produce a render the user can eyeball against their reference.

Report actual measured results, and call out any gap between what was asked and what the model now contains.

## Known connector limits (state them honestly)

- **Horizontal curtain-wall mullions can't be set through the connector.** Revit stores horizontal and vertical mullions under two parameters that share the display name "Interior Type", and `set_element_parameter` only reaches the vertical group (it rejects the internal name too). Set vertical mullions via the connector; tell the user horizontal mullions need a one-time manual Edit Type in Revit.
- **Family authoring is not exposed.** You can `load_family` and place instances, but you cannot create or edit the internal geometry of a family from the connector.
- **`run_revit_command` only fires built-in menu commands** (Save, etc.), not geometry authoring.

When something isn't reachable, say so plainly and give the shortest reliable manual path in Revit, rather than repeatedly retrying a call that can't succeed. Offer an on-screen walkthrough when a manual sketch step is unavoidable.

## Check the build

If a tool the user expects is missing, call `get_geopogo_version` and report the version and tool count so they can tell whether it's a build/version gap versus a usage issue.
