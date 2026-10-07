---
name: geopogo-revit-skills-combined
description: Combined Geopogo Revit skills library (v2026.09.30.2) — 44 workflow skills for driving Revit through the geopogo-ai connector, covering roofs, floor plans, townhomes, towers, façades, structural grids, working drawings, animation, games, vehicles, and interactive delivery, plus diagnostics and validation notes. Use for any Geopogo/Revit task not covered by a narrower geopogo skill.
---

# Geopogo Revit Skills — Complete Combined Library

**Version:** 2026.09.30.2  
**Compiled:** September 30, 2026  
**Contents:** 44 workflow/index skills, two separately attributed external references, source coverage, validation notes, and supporting code.

## Website overview

**44 AI-powered workflows for Revit**

The Geopogo Skills Library captures practical workflows developed through real Revit projects—from architectural design and BIM documentation to playable worlds and custom simulations.

- **Architecture & design:** Homes, organic forms, landmark towers, interiors, furniture, and sculptural details.
- **Infrastructure & complex models:** Bridges, ships, aircraft, vehicles, rockets, factories, and data centers.
- **BIM & documentation:** Floor plans, roofs, structural grids, MEP coordination, sheets, schedules, tags, and dimensions.
- **Cities & environments:** Streets, storefronts, intersections, terrain, highways, landscaping, and material handoffs to Unreal.
- **Games & animation:** Character controls, chase cameras, driving, traffic, missions, shops, autonomous people, theme-park rides, and factory robotics.
- **Simulation & visualization:** Demolition prototypes, flight combat, model-linked dashboards, day/night effects, audio, and cinematic flythroughs.

Built-in guidance emphasizes continuing saved work, preserving editable models, checking results, and packaging projects for others.

Skills guide AI-assisted workflows. Advanced interactive features require companion Dynamo graphs or custom add-ins; simulations are conceptual, not engineering analyses.

## How to use this document

This is the complete reading/reference edition of the expanded library, with the website summary above. Each skill's full instructions follow. Use the table of contents to load or read only the relevant workflow.

References to get_skill and named companion skills describe the modular Geopogo package. In this combined edition, use the matching section below; importing one combined file does not register 44 separate skill names. File paths mentioned inside source instructions refer to the modular package unless their contents are reproduced in an appendix here.

Historical project validation is distinguished from package validation. No original RVTs, game DLLs, private chat logs, or supplied music are embedded. The two external reference documents retain their attribution and distribution limitations.

## Table of contents

1. [Geopogo Revit library](#geopogo-revit-library) — geopogo-revit-library
2. [Create Roof Workflow](#create-roof-workflow) — create-roof-workflow
3. [Floor Plan From Scratch](#floor-plan-from-scratch) — floor-plan-from-scratch
4. [Geopogo — Complete Revit Connector Reference (V2)](#geopogo-complete-v2) — geopogo-complete-v2
5. [Geopogo and Revit connection diagnostics](#geopogo-connection-diagnostics) — geopogo-connection-diagnostics
6. [Geopogo — Missing-Middle Townhome Pattern](#geopogo-missing-middle-townhomes) — geopogo-missing-middle-townhomes
7. [Aircraft shells, decks, interiors, and cutaways](#revit-aircraft-interiors) — revit-aircraft-interiors
8. [Articulated walking, robots, and component animation](#revit-articulated-animation) — revit-articulated-animation
9. [Suspension and cable-stayed bridge studies](#revit-bridges) — revit-bridges
10. [Third-person characters, walking controls, and chase cameras](#revit-character-controls) — revit-character-controls
11. [Camera flythrough and intro-video export](#revit-cinematic-export) — revit-cinematic-export
12. [Data-center BIM, equipment, and MEP coordination](#revit-data-centers-mep) — revit-data-centers-mep
13. [Day/night cycles, ambience, and vehicle radio](#revit-day-night-audio) — revit-day-night-audio
14. [Conceptual demolition and rigid-body playback](#revit-demolition-physics) — revit-demolition-physics
15. [Model-linked dashboards with explicit data provenance](#revit-digital-twin-dashboards) — revit-digital-twin-dashboards
16. [Temporary DirectContext3D animation rendering](#revit-directcontext3d) — revit-directcontext3d
17. [Driving games and vehicle interaction](#revit-driving-games) — revit-driving-games
18. [Dynamo animation and saved-scene playback](#revit-dynamo-animation) — revit-dynamo-animation
19. [Constrained façade recess and dependent slab repair](#revit-facade-repair) — revit-facade-repair
20. [Factory robots, conveyors, and production demos](#revit-factory-animation) — revit-factory-animation
21. [Flight controls and fictional vehicle combat](#revit-flight-combat) — revit-flight-combat
22. [Furniture and compact interior studies](#revit-furniture-interiors) — revit-furniture-interiors
23. [Custom geometry, units, and scoped bounds](#revit-geometry-units) — revit-geometry-units
24. [Continue and verify a Revit/Geopogo model](#revit-geopogo-continue-verify) — revit-geopogo-continue-verify
25. [Landmark towers, setbacks, crowns, and spires](#revit-landmark-towers) — revit-landmark-towers
26. [Missions, shops, rewards, and persistent game progress](#revit-missions-economy) — revit-missions-economy
27. [Modeless Revit controllers and runtime lifecycle](#revit-modeless-runtimes) — revit-modeless-runtimes
28. [Monuments, arches, and sculptural details](#revit-monuments-sculpture) — revit-monuments-sculpture
29. [Native houses and functional interior refinement](#revit-native-house-refinement) — revit-native-house-refinement
30. [Needs-driven people and environment use](#revit-needs-autonomy) — revit-needs-autonomy
31. [Organic architecture, curved glass, and continuous shells](#revit-organic-shells) — revit-organic-shells
32. [Pedestrian and traffic autonomy](#revit-pedestrians-traffic) — revit-pedestrians-traffic
33. [Reference modeling and subject verification](#revit-reference-modeling) — revit-reference-modeling
34. [Resumable modeling and idempotent scene extensions](#revit-resumable-builds) — revit-resumable-builds
35. [Rocket, launch tower, and catch-arm reference modeling](#revit-rocket-launch-site) — revit-rocket-launch-site
36. [Portable delivery of interactive Revit projects](#revit-runtime-delivery) — revit-runtime-delivery
37. [Ship hulls, decks, and conceptual interiors](#revit-ships) — revit-ships
38. [Terrain, highways, factory sites, and landscape context](#revit-sites-landscape) — revit-sites-landscape
39. [Theme-park rides and coordinated scene animation](#revit-theme-park-rides) — revit-theme-park-rides
40. [Revit to Unreal material handoff](#revit-unreal-materials) — revit-unreal-materials
41. [Urban blocks, storefronts, intersections, and street detail](#revit-urban-streets) — revit-urban-streets
42. [Vehicle exteriors, interiors, and reference refinement](#revit-vehicle-modeling) — revit-vehicle-modeling
43. [Working drawings, schedules, tags, and sheet delivery](#revit-working-drawings) — revit-working-drawings
44. [Structural Grid Workflow](#structural-grid-workflow) — structural-grid-workflow

### Appendices

- [Source coverage](#source-coverage)
- [Compatibility and validation](#compatibility-validation)
- [Installation and package usage](#package-usage)
- [Attribution and external references](#external-references)
- [Developer helpers and tests](#developer-helpers)
- [Installer source](#installer-source)

---

<a id="geopogo-revit-library"></a>

## 1. Geopogo Revit library

**Skill name:** `geopogo-revit-library`

Find the appropriate modeling, game, animation, physics, or delivery workflow in the expanded Geopogo Revit skill library.


Use this index when choosing a workflow; do not load the entire library for a simple task. Call get_skill with an exact name below. Start with the requested subject and the actual document, then load only the relevant workflow.

#### Core modeling and recovery

- `geopogo-complete-v2`
- `geopogo-connection-diagnostics`
- `revit-reference-modeling`
- `revit-geometry-units`
- `revit-resumable-builds`
- `revit-geopogo-continue-verify`

#### Architecture, infrastructure and objects

- `floor-plan-from-scratch`
- `create-roof-workflow`
- `structural-grid-workflow`
- `geopogo-missing-middle-townhomes`
- `revit-native-house-refinement`
- `revit-organic-shells`
- `revit-landmark-towers`
- `revit-facade-repair`
- `revit-bridges`
- `revit-ships`
- `revit-rocket-launch-site`
- `revit-aircraft-interiors`
- `revit-vehicle-modeling`
- `revit-furniture-interiors`
- `revit-urban-streets`
- `revit-sites-landscape`
- `revit-monuments-sculpture`
- `revit-unreal-materials`
- `revit-data-centers-mep`
- `revit-working-drawings`

#### Games, simulations and interactive experiences

- `revit-modeless-runtimes`
- `revit-dynamo-animation`
- `revit-character-controls`
- `revit-articulated-animation`
- `revit-driving-games`
- `revit-pedestrians-traffic`
- `revit-needs-autonomy`
- `revit-missions-economy`
- `revit-day-night-audio`
- `revit-cinematic-export`
- `revit-factory-animation`
- `revit-digital-twin-dashboards`
- `revit-directcontext3d`
- `revit-demolition-physics`
- `revit-flight-combat`
- `revit-runtime-delivery`
- `revit-theme-park-rides`

#### Common combinations

- New game: modeless runtime + appropriate movement skill + articulated animation or DirectContext3D + runtime delivery.
- Miami-style world: urban streets + driving + pedestrians/traffic + missions/economy + day/night/audio.
- Character castle: reference modeling + character controls + articulated animation + runtime delivery.
- Walker/airspeeder: geometry/units + articulation + DirectContext3D + flight/combat.
- Sims: native interior modeling + Dynamo animation + needs autonomy.
- Factory: site context + factory animation + dashboard; identify synthetic data.
- Demolition: modeless runtime + rigid-body physics + DirectContext3D + reset verification.
- Extreme architecture or vehicle: reference modeling + geometry/units + organic shells or vehicle modeling; inspect three views before detailing.

#### Shared completion rule

Establish target identity; retain editable source; read back the changed state; inspect the intended subject; report warnings and unfinished work; save and verify the actual deliverable. A compile, file hash, or elapsed animation clock cannot replace live interaction or visual review. Source evidence is historical and some branches remain untested.

#### Optional developer helpers

The extracted package includes scripts/runtime-checks.mjs (target, scoped bounds, playback snapshot checks) and scripts/mission-engine.mjs (configurable pure mission rules), with Node tests. They do not call Revit or install a game. Locate the extracted package before using these files; get_skill returns text and does not provide filesystem attachments.

---

<a id="create-roof-workflow"></a>

## 2. Create Roof Workflow

**Skill name:** `create-roof-workflow`

Create a Revit footprint roof with loaded types and automatic floor-plan view handling.

#### Compatibility and scope

Read the live connector's tool schemas before executing examples; installed versions can differ. Historic failures describe the recorded session, not every release. The installed create_roof schema inspected for this package automatically selects a floor-plan view and restores the original view; older builds may need an explicit view switch. Check returned state and loaded types. Tool availability and a skill's presence do not prove the workflow has been tested on the recipient's Revit version. Use only the intended model and the user's authorized scope.


Guides Claude through the correct sequence for creating a roof in Revit using Geopogo AI tools.

#### Why This Skill Exists

`create_roof` automatically uses a suitable floor-plan view when the current Revit view is 3D, a section, an elevation, or a ceiling plan. It restores the original view after creation and reports whether that restore succeeded. A floor-plan view must exist somewhere in the model.

#### Required Sequence

##### Step 1 — Get available roof family types
```
get_family_types  { "category": "Roofs" }
```
Pick a type name from the results (e.g. `"Generic - 9\""` or `"Steel Truss - Insulation on Metal Deck - EPDM"`).

##### Step 2 — Create the roof
```
create_roof {
  "points": [
    { "x": 0, "y": 0 },
    { "x": 40, "y": 0 },
    { "x": 40, "y": 30 },
    { "x": 0, "y": 30 }
  ],
  "levelName": "Level 2",
  "roofTypeName": "Generic - 9\"",
  "slopeAngle": 26.565
}
```

#### Common Mistakes to Avoid

- The model must contain at least one non-template floor-plan view. If none exists, create one, then retry.
- **Do not skip `get_family_types`.** Passing a type name that doesn't exist in the project will fail.
- **slopeAngle is in degrees** (0 = flat, 26.565 = 6:12 pitch, 45 = 12:12 pitch).
- If the user says "flat roof", use `slopeAngle: 0`.
- Check `viewRestore.restored` in the response. If it is false, manually switch back to the reported original view.

#### Example — Full Interaction

User: "Add a hip roof to the building at Level 2."

1. `get_family_types { "category": "Roofs" }` → pick type
2. `create_roof { "points": [...], "levelName": "Level 2", "roofTypeName": "...", "slopeAngle": 26.565 }`
3. Confirm the response reports a roof category and `viewRestore.restored: true`.

---

<a id="floor-plan-from-scratch"></a>

## 3. Floor Plan From Scratch

**Skill name:** `floor-plan-from-scratch`

Build a Revit floor plan from levels through walls, floors, hosted openings, and verification.

#### Compatibility and scope

Read the live connector's tool schemas before executing examples; installed versions can differ. Historic failures describe the recorded session, not every release. The installed create_roof schema inspected for this package automatically selects a floor-plan view and restores the original view; older builds may need an explicit view switch. Check returned state and loaded types. Tool availability and a skill's presence do not prove the workflow has been tested on the recipient's Revit version. Use only the intended model and the user's authorized scope.


Complete workflow for building a Revit floor plan from a user description or sketch using Geopogo AI tools.

#### Recommended Build Order

Always build in this sequence. Each step depends on the previous one.

```
1. Levels
2. Walls (exterior shell first, then interior partitions)
3. Floors
4. Doors
5. Windows
6. Stairs / Railings (if multi-storey)
7. Ceiling (optional)
8. Verify
```

#### Step-by-Step

##### 1. Create Levels
```
create_level  { "name": "Level 1", "elevation": 0 }
create_level  { "name": "Level 2", "elevation": 10 }
create_level  { "name": "Roof",    "elevation": 20 }
```
Elevations in feet. Typical floor-to-floor: 10–12 ft for residential, 13–15 ft for commercial.

##### 2. Create Walls

Always use `create_walls_batch` for multiple walls — it's faster than calling `create_wall` repeatedly.

```
create_walls_batch  {
  "walls": [
    { "startX": 0, "startY": 0,  "endX": 40, "endY": 0,  "height": 10, "levelName": "Level 1" },
    { "startX": 40, "startY": 0, "endX": 40, "endY": 30, "height": 10, "levelName": "Level 1" },
    { "startX": 40, "startY": 30,"endX": 0,  "endY": 30, "height": 10, "levelName": "Level 1" },
    { "startX": 0,  "startY": 30,"endX": 0,  "endY": 0,  "height": 10, "levelName": "Level 1" }
  ]
}
```

Tips:
- Check wall orientation and exterior faces after creation; reverse or flip any wall whose stored orientation does not match the design.
- Use `get_element_types` with category `Walls` to pick the right wall type before creating walls if the user cares about construction type.
- Interior partition walls connect to exterior walls at their endpoints.

##### 3. Create Floors

Get floor types first, then create:
```
get_family_types  { "category": "Floors" }
create_floor  {
  "floorTypeName": "Generic - 12\"",
  "levelName": "Level 1",
  "points": [
    { "x": 0, "y": 0 }, { "x": 40, "y": 0 },
    { "x": 40, "y": 30 }, { "x": 0, "y": 30 }
  ]
}
```
The boundary uses `points`, an array of `{x,y}` objects in feet. Use a simple closed outline without intersecting edges.

##### 4. Place Doors

```
get_family_types  { "category": "Doors" }
create_door  { "wallId": 12345, "x": 5.0, "y": 0, "familyTypeName": "Single-Flush: 36\" x 84\"" }
```
`x` and `y` are insertion coordinates in the selected units, not distance along the wall. Replace the example wall ID with the actual host ID.

##### 5. Place Windows

```
get_family_types  { "category": "Windows" }
create_window  {
  "wallId": 12345,
  "x": 15.0,
  "y": 0,
  "familyTypeName": "Fixed: 36\" x 48\""
}
```

Set each window's `Sill Height` after creation using the returned element ID and the live `set_element_parameter` schema; `create_window` does not expose a sill-height argument in the inspected connector. Verify the stored value.

##### 6. Verify the Model

Always finish with a verification pass:
```
verify_model  {
  "expectedLevelCount": 3
}
```
The example creates three levels, including Roof. Derive the expected total from the actual existing levels and intended additions. Fix discrepancies before proceeding.

#### Common Mistakes

- **Walls not connecting**: make sure endpoints of adjacent walls share the exact same coordinates (e.g. `endX/endY` of wall 1 = `startX/startY` of wall 2).
- **Floor boundary wrong direction**: if Revit rejects the boundary, reverse the point order.
- **Doors/windows on wrong wall**: always call `get_elements { "category": "Walls" }` first to get the correct wall IDs.
- **Wrong sill height**: read and set the intended sill height explicitly; do not rely on template defaults.

#### Quick Reference — Typical Room Sizes (feet)

| Room            | Width × Depth |
|-----------------|---------------|
| Master bedroom  | 14 × 16       |
| Secondary bed   | 11 × 12       |
| Living room     | 16 × 20       |
| Kitchen         | 12 × 14       |
| Bathroom        | 6 × 8         |
| Hallway         | 4 wide        |
| Garage bay      | 12 wide       |

---

<a id="geopogo-complete-v2"></a>

## 4. Geopogo — Complete Revit Connector Reference (V2)

**Skill name:** `geopogo-complete-v2`

Revit modeling reference: conventions, envelopes, site, structure, MEP, sheets, and coordination.

#### Compatibility and scope

Read the live connector's tool schemas before executing examples; installed versions can differ. Historic failures describe the recorded session, not every release. The installed create_roof schema inspected for this package automatically selects a floor-plan view and restores the original view; older builds may need an explicit view switch. Check returned state and loaded types. Tool availability and a skill's presence do not prove the workflow has been tested on the recipient's Revit version. Use only the intended model and the user's authorized scope.


This is the full accumulated Geopogo skill set: everything learned from actual modeling sessions, plus new workflow areas covering the rest of what the `geopogo-ai` connector exposes.

**Two parts, two confidence levels — read the labels before you rely on a section:**

- **Part I — Field-Tested Workflows** (§1–5). Built from real sessions. The cautions, "known limits," and gotchas here are confirmed — things like the roof active-view bug or the horizontal-mullion connector limitation actually happened and were worked around.
- **Part II — New Workflows** (§6–9). Drafted by mapping the connector's remaining tools (structural, MEP, documentation, coordination) into the same conventions and style as Part I. These have **not** been run against a live Revit session. Treat their sequences as a reasonable starting point, not a proven path — verify empirically and update this doc once they've been battle-tested, the same way §1–5 were.

Always start with §1 (Working Conventions) regardless of which workflow you need — every other section builds on it.

**Contents:** 1. Working Conventions · 2. Curtain Walls, Mullions & Arched Windows · 3. House + Roof · 4. Site Context · 5. High-Rise Tower Massing · 6. Structural Framing & Foundations · 7. MEP Systems · 8. Documentation & Sheets · 9. Rooms, Parts & Model Coordination

---

### Part I — Field-Tested Workflows

#### 1. Working Conventions

These are the ground rules for driving Revit through the `geopogo-ai` connector. Follow them for every modeling task; every other section builds on top of these.

##### 1.1 Always inspect before you build

Never assume model state. At the start of a task call, in this order as needed:

1. `get_model_info` — file name, active view, discipline.
2. `get_levels` — existing levels and elevations (you place most elements by level).
3. `get_element_types` / `get_family_types` — the exact type names available. Type names must match exactly; a wrong name returns a null/"Value cannot be null" error.
4. `get_elements` or the category getters (`get_elements` with category `Walls`, `get_curtain_walls`, `get_rooms`, etc.) to see what already exists.

Match the user's intent to real type names that exist in the model. If the needed type is missing, load it with `load_family` (or duplicate an existing type with `duplicate_element_type`) before creating elements.

##### 1.2 Units

The connector expects **decimal feet** for lengths and coordinates unless a tool documents otherwise. Confirm project units with `get_project_units` when the user gives metric dimensions, and convert before calling. When a user states a size (e.g. "20 ft tall", "6 windows per façade"), treat those as hard targets — model them exactly, then verify (see below).

##### 1.3 The active view matters

Several creation tools require a specific **active view type**, not the 3D view:

- **Floors and walls** work in a 3D view.
- Current inspected connector: `create_roof` automatically selects a suitable floor-plan view and restores the original view. A non-template floor plan must exist. Older builds exhibited null failures from 3D views; use `create-roof-workflow` and the live schema for the installed version.
- Plan-based annotation (dimensions, tags, detail lines) needs the corresponding plan/section view active.

If a creation call fails with a null error and the inputs look correct, suspect the active view before suspecting your geometry. Confirm by running the identical footprint through `create_floor` — if the floor succeeds, the geometry is fine and the problem is the view or the command.

##### 1.4 Prefer type-level edits for repeated elements

When a change should apply to many elements at once (all curtain panels, all mullions, a whole wall type), set it on the **element type**, not each instance. Editing the "Exterior Glazing" curtain-wall type propagates to every panel that uses it in one call — far faster and more consistent than looping instances.

##### 1.5 Read back and verify

Do not trust that a call worked because it returned. After a batch of creation/edit calls:

- Re-query with the relevant getter (`get_elements`, `get_element_parameters`) to confirm counts, spacing, and dimensions match the stated intent.
- Use `verify_model` when available for an overall integrity check.
- Use `export_view_to_image` to produce a render the user can eyeball against their reference.

Report actual measured results, and call out any gap between what was asked and what the model now contains.

##### 1.6 Known connector limits (state them honestly)

- **Horizontal curtain-wall mullions can't be set through the connector.** Revit stores horizontal and vertical mullions under two parameters that share the display name "Interior Type", and `set_element_parameter` only reaches the vertical group (it rejects the internal name too). Set vertical mullions via the connector; tell the user horizontal mullions need a one-time manual Edit Type in Revit.
- **Family authoring is not exposed.** You can `load_family` and place instances, but you cannot create or edit the internal geometry of a family from the connector.
- **`run_revit_command` only fires built-in menu commands** (Save, etc.), not geometry authoring.

When something isn't reachable, say so plainly and give the shortest reliable manual path in Revit, rather than repeatedly retrying a call that can't succeed. Offer an on-screen walkthrough when a manual sketch step is unavoidable.

##### 1.7 Check the build

If a tool the user expects is missing, call `get_geopogo_version` and report the version and tool count so they can tell whether it's a build/version gap versus a usage issue.

---

#### 2. Curtain Walls, Mullions & Arched Windows

Follow §1 first. This covers glass facades and the specific tricks that took several iterations to get right.

##### 2.1 Create the curtain wall

1. Inspect: `get_curtain_walls`, `get_curtain_wall_grid`, `get_curtain_panel_types`, `get_mullion_types`.
2. Create the wall with `create_wall` (or `create_walls_batch`) using a curtain-wall type. Confirm the type name exactly via `get_element_types`.
3. Set the grid: use `get_curtain_wall_grid` to read current divisions, then `add_curtain_grid_line` / `move_curtain_grid_line` / `remove_curtain_grid_line` to hit the target bay spacing. For a regular pattern, prefer setting the type's vertical/horizontal grid spacing parameters over placing lines one by one.

##### 2.2 Mullions — set them on the TYPE

To mullion an entire facade in one shot, assign the mullion profile on the **curtain-wall type**, not per panel. Setting mullions on the "Exterior Glazing" (or equivalent) type propagates to every panel that uses it — hundreds of panels update from a single call.

Sequence:

1. `get_mullion_types` to find a profile (e.g. `1.5" x 2.5" rectangular`).
2. `set_element_parameter` on the curtain-wall type to assign the **vertical** interior/border mullion.
3. Read back with `get_element_parameters` to confirm the profile took.

**Known limit: horizontal mullions.** The connector can only set the **vertical** mullion group (see §1.6). Apply vertical mullions via the connector; tell the user horizontal mullion **bars** require a one-time manual step: select any panel → Edit Type on the glazing type → under **Horizontal Mullions** set Interior/Border to the same profile. That edit propagates to every panel. The horizontal grid still reads visually through per-floor panel joints and projecting slab edges even without horizontal bars.

##### 2.3 Arched / round-top windows

Two routes depending on how the base is built.

**Route A — curtain panels with arched tops (`set_wall_profile`).** Newer Geopogo builds expose `set_wall_profile`, which edits a wall/panel's **vertical silhouette** — this is what makes arched tops possible. (Older builds lacked it; if it's absent, run `get_geopogo_version` and fall back to Route B or a manual Edit Profile.)

1. Identify the base storefront/curtain segments with `get_curtain_walls` / `get_elements`.
2. Use `set_wall_profile` to replace the top edge of each segment with a semicircular arc — set the springline just above the head height shown in the reference, with the arc rising to the panel top.
3. Verify with `get_wall_profile` and an `export_view_to_image` from elevation.

**Route B — masonry base with punched arched windows.** If the look is arched openings in solid stone (not glazed curtain wall):

1. Create the base as a solid wall (`create_wall` with a masonry/stone type; set material via `set_compound_layer_material` or `paint_face`).
2. `load_family` for an arched / round-top window family (Revit's "Window - Round Top" / "Arch" families, or a supplied family file).
3. Place openings with `create_window` / `create_window_array` along the frontage at the bay spacing and head height in the reference; set the head height so the arch springline lands where the photo shows it.

##### 2.4 Glazing appearance

Tint or set glass with `create_material` + `set_material_color`, then apply via `set_compound_layer_material` on the panel type or `paint_face` on specific panels. Set the type once so all panels update together.

##### 2.5 Finish

Re-query counts and spacing, then `export_view_to_image` so the user can compare against their reference. Report the vertical-mullion state and flag the horizontal-mullion manual step explicitly.

---

#### 3. House + Roof

Follow §1 first. This is the residential shell pipeline, with the roof gotcha that repeatedly bites.

##### 3.1 Levels

Create the levels the house needs (e.g. L1, L2, Roof) with `create_level` / `create_building_levels`, then `get_levels` to confirm elevations. Set floor-to-floor to the user's stated height (default ~9–10 ft residential if unstated — confirm).

##### 3.2 Walls and floors

1. Exterior walls: `create_walls_batch` around the footprint on L1 (and L2 if multi-story), using a real wall type from `get_element_types`.
2. Floor slab: `create_floor` with the footprint at each level. Floors create fine in the 3D view.
3. Interior partitions if requested: `create_walls_batch`.

##### 3.3 Roof — mind the active view

`create_roof` builds a footprint roof. View handling is version-dependent:

- Current inspected connector: `create_roof` automatically selects a suitable floor-plan view and restores the original view. A non-template floor plan must exist. Older builds exhibited null failures from 3D views; use `create-roof-workflow` and the live schema for the installed version.
- In older builds without automatic switching, activate a suitable plan with `set_active_view`; use manual switching only if the connector cannot do it. In current builds inspect `viewRestore` and restore the view if needed.
- The footprint auto-closes, so pass the corner points without repeating the first point.
- The inspected `create_roof` schema exposes one uniform `slopeAngle` in degrees, not per-edge slope flags. Do not invent per-edge arguments for a gable roof; use a supported Revit editing workflow and verify the resulting roof. Get the type with `get_family_types` for category `Roofs`.

**Historical fallback, only after reproducing the failure in the installed build.** If `create_roof` still returns null after a confirmed plan-view + a plugin reload/Revit restart, treat the command as broken in that build rather than hammering it. Fall back to modeling the roof form with `create_mass_extrusion` (extrude the gable cross-section along the ridge) to give a correct silhouette, and advise the user to report the `create_roof` bug to the Geopogo team with the version from `get_geopogo_version`.

##### 3.4 Openings

- Doors: `create_door` on the host wall at the right location/level.
- Windows: `create_window`, or `create_window_array` for a regular row at fixed spacing and sill height.
- For a wall opening without a family, `create_wall_opening`.

##### 3.5 Verify and render

Re-query wall/floor/opening counts and the roof pitch; confirm dimensions match what was asked. `verify_model`, then `export_view_to_image` from 3D for review. If the roof used the mass-extrusion fallback, say so and note it's a massing stand-in, not a true Revit roof object.

---

#### 4. Site Context

Follow §1 first. This covers the ground plane and streetscape around a building.

##### 4.1 Topography / ground

1. `get_topography` to see any existing surface.
2. `create_topography` for the ground plane. Supply the boundary points and elevations; keep it flat unless the user wants grade. Reference the building's L1 elevation so the ground meets the base cleanly.

##### 4.2 Streets, curbs, sidewalks

These are best built as thin floor slabs or masses at the right elevations, layered from the roadway up:

- **Roadway**: a `create_floor` slab (asphalt material) at street level across the right-of-way.
- **Curb**: a low `create_wall` or thin `create_mass_extrusion` run along the roadway edge, typically ~6 in above the road.
- **Sidewalk**: a `create_floor` slab (concrete) between curb and property line, set at curb-top elevation.
- **Intersection**: repeat the roadway slab on the crossing axis and merge/`join_geometry` where they meet; wrap curbs and sidewalks around the corners with the appropriate radius.

Assign materials with `create_material` + `set_material_color`, applied via `set_compound_layer_material` or `paint_face`, so asphalt/concrete/paint read distinctly.

##### 4.3 Site components

Populate with `place_site_component` (trees, benches, cars, lights) and `create_component` for loaded families. Use `get_loaded_families` first; `load_family` anything missing.

##### 4.4 Verify and render

Confirm elevations line up (no floating curbs, sidewalk flush to curb top), `verify_model`, then `export_view_to_image` from a 3D or perspective view. Check that the ground meets the building base and the streetscape reads at human scale.

---

#### 5. High-Rise Tower Massing

Follow §1 first. This is the mass → floors → skin → core pipeline used to build towers like Salesforce Tower and 30-story office/hotel forms.

##### 5.1 Levels first

Towers live or die on levels. Create the full level stack up front:

- Use `create_building_levels` (fastest — makes N levels at a set floor-to-floor height in one call) when available, or loop `create_level`.
- Confirm with `get_levels`. Every floor, wall, and curtain segment references these, so get the count and elevations right before modeling anything else.

##### 5.2 Massing form

For anything other than a plain box, start from a mass:

1. `create_mass_box` for a simple prism, or `create_mass_extrusion` for a shaped footprint, or `create_blend` for a tapering/crowned form (e.g. a tapered crown or setback top).
2. Generate `create_mass_floors` at each level so the mass has floor divisions.
3. Convert to building elements with `mass_to_building_elements` (floors + facades from the mass faces), or use the mass purely as a guide and place elements against it.

For a straight extruded tower you can skip the mass and go straight to floors + curtain walls per level.

##### 5.3 Floors

Create a floor slab at each level with `create_floor` using the level's footprint. Floors work in the 3D view. Verify slab count equals level count.

##### 5.4 Curtain-wall skin

Wrap the tower in glazing. See §2 for the mullion details — the key points for a tower:

- Create the curtain walls per elevation (or `create_walls_batch`), using one curtain-wall type across the whole tower.
- **Set mullions and glazing on the TYPE**, not per panel — one edit updates all ~hundreds of panels. Only the vertical mullion group is reachable through the connector; horizontal mullion bars need a one-time manual Edit Type (see §2.2).
- For a crown or setback, adjust the top segments' grid/profile separately.

##### 5.5 Core

Add a service core: interior walls (`create_walls_batch`) enclosing the elevator/stair shaft, and stairs with `create_stairs` (see §6.6 for stairs/railings detail). Place structural columns with `create_column` on a grid (`create_grid`) if the user wants structure — see §6 for the full structural sequence.

##### 5.6 Verify and render

- Re-query: floor count, level count, panel spacing — confirm they match the stated program (e.g. "30 stories, 6 bays per face").
- `verify_model` for integrity.
- `export_view_to_image` from a 3D view for the user to review, and iterate on glazing tint / mullion spacing / crown.

State honestly where the connector fell short (e.g. horizontal mullions) and give the manual step.

---

### Part II — New Workflows (Drafted, Not Yet Battle-Tested)

The sections below cover the rest of what `geopogo-ai` exposes — structure, MEP, documentation, and model coordination. They follow the same conventions as Part I, but unlike §1–5, they haven't been run against a live Revit session yet. Verify each sequence empirically before treating any caution here as a confirmed limit the way §1.6 is; update the status once a section has been through real use.

#### 6. Structural Framing & Foundations

Covers the load-bearing side of a model — grid, frame, foundations, reinforcement, and stairs — which §3 and §5 reference but don't detail. Use when the user wants a structural grid, framing, columns, beams, footings, foundations, rebar/reinforcement, or stairs and railings for vertical circulation.

##### 6.1 Lay out the grid first

Structural elements are almost always placed relative to a grid, so build it before columns or beams:

1. `get_grids` to see what already exists — don't duplicate a grid the user already has.
2. `create_grid` for each column line (numbered/lettered per the user's convention, e.g. 1–8 and A–D). Grids are 2D reference lines that span all levels, so you typically only create each line once regardless of story count.
3. Confirm with `get_grids` that spacing matches the stated bay dimensions.

##### 6.2 Levels and framing types

Structural framing depends on the level stack being right first — see §1 and §5.1 for `create_level` / `create_building_levels`. Before placing anything, check `get_structural_elements` (what's already framed) and `get_element_types` / `get_family_types` for the exact column, beam, and foundation type names — as elsewhere, a mismatched type name fails rather than substituting a default.

##### 6.3 Columns and beams

1. Place vertical structure with `create_column` at each grid intersection (or at the specific points the user gives), one level at a time. Set the type from `get_element_types` (e.g. a concrete or steel section).
2. Span beams between columns with `create_beam`, snapping endpoints to grid intersections or column centerlines so the frame reads as continuous.
3. For a repetitive bay pattern, loop the grid intersections programmatically rather than placing each column by hand-picked coordinates — it's the more reliable way to keep spacing exact.
4. `join_geometry` where columns meet beams/foundations if the connector leaves a visible seam — join is a targeted per-pair operation, not something that runs automatically.

##### 6.4 Foundations

Pick the foundation type to match what's structurally under each vertical element:

- **Isolated footing under a single column**: `create_isolated_foundation` at the column base point. Check `get_element_types` for the footing family/type first.
- **Continuous footing under a bearing wall**: `create_wall_foundation` along the wall; `get_wall_foundation_types` lists what profiles are available for the host wall type — the foundation type must be compatible with the wall it's hosted on.
- **Mat/raft slab under a whole core or tower base**: `create_mat_foundation` across the footprint, typically at the lowest level.

Set foundation top elevation to meet the lowest level's structural floor, and verify with `get_structural_elements` that count and location match one footing per column (or one continuous run per bearing wall).

##### 6.5 Rebar

Reinforcement is placed inside a host element (foundation, column, wall, or beam), so create the host first:

1. `get_rebar_bar_types` and `get_rebar_shapes` to see what bar sizes/shapes are loaded — load more via `load_family` if the spec calls for something not present.
2. `create_rebar` inside the target host, matching the shape/size/spacing the user or the structural spec calls for (e.g. bar size, cover, spacing along the run).
3. Rebar is detail-heavy — if the user only wants a schematic/coordination model, confirm before spending calls on exact bar-by-bar placement; a simplified representative cage is often enough unless they explicitly want construction-documentation-level rebar.

##### 6.6 Stairs and railings

Vertical circulation for a structural core or any multi-level building:

1. `create_stairs` between two levels, setting the run/landing geometry to fit the shaft or stair enclosure. Confirm the base and top level are correct — stairs that don't reach the intended level are a common miss.
2. `create_railing` along open edges (stair runs, landings, floor openings, balconies). Pick the railing type from `get_element_types`.
3. For a full core (elevators + stairs + shaft walls), coordinate this with the enclosing walls from `create_walls_batch` — see §5.5.

##### 6.7 Verify and render

- Re-query `get_structural_elements` / `get_grids` to confirm column/beam/footing counts match the program (e.g. one column per grid intersection per level, one footing per ground-level column).
- `verify_model` for overall integrity, and check `get_model_warnings` — structural clashes (unjoined geometry, floating footings) often surface there before they're visible in a render.
- `export_view_to_image` from a 3D or structural view for the user to review the frame.

Report actual placed counts against what was asked, and flag anything you simplified (e.g. schematic rebar instead of full detailing) so the user knows where to expect more work before construction documents.

---

#### 7. MEP Systems

Covers mechanical, electrical, and plumbing modeling. Use when the user wants HVAC ductwork, plumbing/piping, electrical conduit or fixtures, MEP routing, or MEP spaces coordinated with rooms. MEP work is routing-heavy: get the host geometry and levels right before running any duct, pipe, or conduit, since every run needs real connection points to land on.

##### 7.1 Inspect before routing

MEP elements connect to fixtures, equipment, and each other, so confirm what's already in the model before adding runs:

1. `get_mep_systems` — existing systems (supply air, sanitary, power, etc.) so new runs join the right system rather than creating a stray duplicate.
2. `get_mep_spaces` — MEP spaces, which are the mechanical/electrical counterpart to architectural rooms and drive loads and equipment sizing. `get_room_at_point` can confirm which architectural room a given point falls in if you need to cross-reference.
3. `get_electrical_fixtures` and `get_electrical_systems` for existing devices and circuits.
4. `get_element_types` / `get_family_types` for the duct/pipe/conduit types and sizes available, and `load_family` anything the spec calls for that isn't loaded (diffusers, panels, fixtures).

##### 7.2 Ducts, pipes, and conduit

All three follow the same pattern: define a path of points at the right elevation, and a system/type.

- **Ductwork**: `create_duct` along the route, sized and typed per the mechanical schedule (e.g. supply vs. return). Route above ceiling or in a shaft per the level's clear height — check the level-to-level height before assuming clearance.
- **Piping**: `create_pipe` for domestic water, sanitary, or process runs. Slope-sensitive systems (sanitary/storm) need correct start/end elevations for gravity flow — don't route them dead level unless the user explicitly wants a pressurized system.
- **Conduit**: `create_conduit` for electrical raceway runs between panels, devices, and junction points.

For all three, place runs level by level and re-check `get_mep_systems` after each batch so you can confirm the run actually joined the intended system rather than creating an orphaned segment.

##### 7.3 Electrical fixtures and systems

1. Place devices (outlets, panels, light fixtures, equipment) with `create_component` using a loaded electrical family, or the connector's fixture-placement path if one exists for the category — confirm with `get_electrical_fixtures` after placing.
2. Circuit relationships and panel assignments are read via `get_electrical_systems`; if the connector doesn't expose a direct circuiting call, note that circuiting may need to be finished manually in Revit's Electrical panel schedule and say so plainly rather than guessing at a call that isn't there.

##### 7.4 MEP spaces vs. architectural rooms

MEP spaces are a separate object from rooms even when they share a boundary — a room can exist with no space, or vice versa. If the user asks for load calculations, equipment sizing, or space-based tagging, confirm spaces exist (`get_mep_spaces`) and match the architectural rooms (`get_rooms`, `get_room_at_point`) before proceeding; don't assume one implies the other.

##### 7.5 Verify and render

- Re-query `get_mep_systems`, `get_electrical_systems`, and the category getters to confirm run counts and connectivity match what was requested (e.g. "supply duct from AHU to every diffuser on L2").
- `verify_model` and check `get_model_warnings` — MEP models commonly surface unconnected segments, disconnected systems, and clash warnings here before they're visible in a 3D render.
- `export_view_to_image` from a 3D or MEP-discipline view so the user can review routing.

State plainly anything the connector can't do end-to-end (e.g. detailed circuit load balancing, fixture-unit sizing) and point to the manual step in Revit rather than approximating a result that looks right but isn't engineered.

---

#### 8. Documentation & Sheets

Covers turning a model into drawing output: views, sheets, annotation, schedules, and revisions. Use when the user wants a sheet set, construction documents, a schedule, dimensioning, tagging, a revision cloud, or wants a view's appearance, scale, crop, or graphic overrides changed.

##### 8.1 Views before sheets

A sheet is just a placeholder until views are placed on it, so create/prepare views first:

1. `get_views` to see what exists — reuse an existing view rather than duplicating one that already shows what's needed.
2. Create the views the drawing set needs: `create_floor_plan`, `create_ceiling_plan`, `create_section_view` (check `get_section_view_types` for the cut-line style available), or `create_3d_view`. Use `duplicate_view` when you need the same view at a different scale/filter state rather than a fresh cut.
3. Set each view's presentation: `set_view_scale`, `crop_view` (to the sheet's drawing area), `apply_view_template` (pick from `get_view_templates` for a consistent standard look), or `apply_view_filter` (pick from `get_view_filters`, or make a new one with `create_view_filter`).
4. Category-level graphics: `get_category_visibility` / `set_category_visibility` to turn whole categories on/off per view, and `set_category_graphic_override` for line weight/color/pattern overrides that apply only in that view (not the model globally — a common point of confusion, since `set_element_override` is instance-level and category overrides are view-level).

##### 8.2 Sheets

1. `get_sheets` and `get_title_block_types` — confirm the title block family/type the user's set uses before creating new sheets, so numbering and border match the existing set.
2. `create_sheet` with the sheet number/name and title block type.
3. `place_view_on_sheet` for each prepared view; `get_sheet_views` afterward to confirm placement and catch any view placed on the wrong sheet.
4. `set_sheet_parameter` for sheet-specific fields (drawn by, checked by, issue date, etc.) that the title block exposes as parameters.

##### 8.3 Annotation

- **Dimensions**: `create_dimension` between the reference elements/points the user specifies (wall faces, grid lines, opening edges). Dimension in the view where the geometry is actually visible — a dimension referencing hidden geometry will fail or attach to the wrong element.
- **Tags**: `tag_element` for door/window/room/equipment tags; confirm the tag family is loaded (`get_loaded_families`, `load_family` if not) and that it matches the category being tagged.
- **Text and detail graphics**: `create_text_note` for callouts and notes, `create_detail_line` for 2D linework, and `create_filled_region` / `create_drafting_filled_region` / `create_masking_region` for hatching, poché, and masking. Drafting-view-only regions (`create_drafting_filled_region`) don't reference model geometry — use them for generic details, not for anything that should track the model.
- **General**: `get_annotations` to audit what's already placed in a view before adding more, so you don't duplicate tags or dimensions.

##### 8.4 Schedules

`create_schedule` for a category (doors, windows, rooms, walls, etc.), specifying the fields the user wants (mark, type, level, area, etc.). Schedules are live model queries — verify field names against `get_element_parameters` for that category first, since a schedule field name that doesn't match the model's actual parameter name will produce an empty or wrong column rather than an error.

##### 8.5 Revisions

1. `get_revisions` to see the existing revision sequence — new revisions append to it, so check the last issued number/letter first.
2. `create_revision` for a new revision (number, description, date, issued-to).
3. `create_revision_cloud` around the changed area in the relevant view(s).
4. `assign_revision_to_sheet` for every sheet the change touches — a revision cloud with no sheet assignment won't show up in that sheet's revision schedule.

##### 8.6 Verify and render

- Re-query `get_sheets`, `get_sheet_views`, and `get_annotations` to confirm the drawing set matches what was asked (right views on right sheets, dimensions/tags present, revision clouds assigned).
- `verify_model` for overall integrity and `get_model_warnings` for anything documentation-adjacent (e.g. unresolved tags, duplicate marks).
- `export_view_to_image` on the finished sheet(s) so the user can review layout before printing/issuing.

Report which views/sheets were touched, and flag anything that needed a workaround (e.g. a filter created because none existed, or a manual title-block field the connector couldn't set).

---

#### 9. Rooms, Parts & Model Coordination

Covers the model-management layer: rooms/spaces, splitting or grouping elements, coordinating with linked/scanned data, and general element edits that don't fit elsewhere. Use when the user wants rooms named/numbered, an element split into parts or grouped into an assembly, a linked model reloaded, worksets or phases assigned, design options compared, a point-cloud scan referenced, or a model exported to IFC.

##### 9.1 Rooms

1. `get_rooms` to see what's already placed, and `get_room_at_point` to check whether a given point already falls inside a room boundary before adding one.
2. `create_room` inside a bounded area (walls must form a closed loop for the room to compute correctly — an open boundary produces an "unbounded" room with no area).
3. `set_room_name_number` to assign the name/number the user gives, or to match a numbering scheme (e.g. floor-prefixed: 201, 202...).
4. If the user also needs MEP load/space data tied to these rooms, see §7.4 (`get_mep_spaces`) — rooms and MEP spaces are separate objects even on the same boundary.

##### 9.2 Parts and assemblies

Use these when the user wants an element broken into constructible pieces or grouped for scheduling/fabrication, not for ordinary geometry creation:

- **Parts**: `create_parts` divides a host element (e.g. a floor or wall) into independently-schedulable/paintable pieces — typical for phased construction or multi-material walls. `get_parts` lists what's already split.
- **Assemblies**: `create_assembly` groups selected elements into a single schedulable/callable unit (e.g. a precast panel with its embeds). `get_assemblies` lists existing ones; `disassemble_assembly` reverses the grouping if the user wants the elements back to independent status.

Check `get_groups` / `get_group_types` if the user means a model **group** (a reusable, repeatable cluster of elements) rather than an assembly (a fabrication/scheduling unit) — the two are easy to conflate but serve different purposes, and the connector's write path differs (assemblies have dedicated create/disassemble calls; groups here are read-only via the connector, so creating a new group type is a manual Revit step).

##### 9.3 Linked models

1. `get_linked_models`, `get_rvt_links`, and `get_cad_links` to see what's already linked before adding or troubleshooting a link.
2. `reload_rvt_link` after the linked file has been updated externally, so the current session reflects the latest coordination model.
3. `unload_rvt_link` to temporarily drop a link (for performance or to isolate a discipline) without deleting the link itself.
4. When placing new elements near a link, position them relative to the link's shared coordinates, and call out to the user if alignment looks off — the connector doesn't auto-correct link placement.

##### 9.4 Point clouds

1. `get_point_clouds` to see what scan data is attached.
2. `query_point_cloud_slice` to sample the scan at a given elevation/region — useful for checking as-built dimensions against the model before placing new geometry (e.g. confirming an existing wall location before adding a footing under it).
3. `set_point_cloud_visibility` to toggle the scan on/off per view so it doesn't clutter documentation views.

##### 9.5 Worksets, phases, and design options

- **Worksets**: `get_worksets` to see the workset structure (this only matters in workshared/central models); `set_element_workset` to assign new or moved elements to the right discipline workset.
- **Phases**: `get_phases` to see the project's phase list (existing, demo, new construction, etc.); `set_element_phase` so new elements are correctly flagged as "New Construction" (or whatever phase applies) rather than defaulting to whatever phase is currently active in the view.
- **Design options**: `get_design_option_sets` and `get_design_options` to see what alternatives exist for a given area before adding elements — placing new geometry while the wrong design option is current will put it in the wrong option silently, so confirm before batch-creating.

##### 9.6 General element editing

These utilities apply across every category and are handy once elements already exist:

- **Transform**: `move_element`, `rotate_element`, `mirror_element`, `copy_element` for repositioning/duplicating without re-creating from scratch.
- **Type changes**: `change_element_type` to swap an instance to a different existing type; `duplicate_element_type` to create a new type (e.g. a variant with different parameters) without affecting the original.
- **Cleanup**: `delete_element` for removals, `join_geometry` to clean up seams between adjoining elements (walls/floors/foundations), and `set_element_override` for instance-level graphic overrides (view-level category overrides are `set_category_graphic_override` — see §8.1).
- Always re-query (`get_elements` / `get_element_parameters`) after a batch of edits to confirm the count and state match intent, same as any other workflow.

##### 9.7 Export and verify

- `export_to_ifc` when the user needs an open, cross-platform deliverable rather than a native Revit file — confirm which view/element set should be included, since a full-model export can be large and slow.
- `verify_model` and `get_model_warnings` before handing off — coordination issues (unresolved links, elements on the wrong workset/phase/design option) are exactly the class of problem this section's checks catch early.
- `export_view_to_image` for a quick visual sanity check when useful.

Report anything ambiguous plainly — e.g. if a linked model wasn't reloaded because the user hadn't said whether the external file changed, or if elements were left on the default workset/phase because none was specified.

---

<a id="geopogo-connection-diagnostics"></a>

## 5. Geopogo and Revit connection diagnostics

**Skill name:** `geopogo-connection-diagnostics`

Diagnose missing Geopogo tools, bridge connectivity, document access, and desktop-control availability without confusing them.


#### Evidence and scope

Based on repeated connection troubleshooting and inspection of the locally installed Geopogo loader; host settings and ports must be rediscovered on each installation.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Check whether the current AI session exposes Geopogo tools. A configured connector entry is not proof that the tools loaded into this chat.

2. Check Revit is open, the Geopogo bridge is enabled, and the intended document is available. Use a read-only model-info call and inspect its actual returned path and version.

3. If the configured bridge uses a local port, check that configured port is listening. Port 8765 was used in the source installation; do not assume it on all machines or start a replacement listener blindly.

4. If tools are absent, reconnect/reload the host integration after enabling the Revit side. Recheck in the resulting session. Diagnose tool-loading, bridge-listening, and wrong-document errors separately.

5. For UI automation, enumerate exposed desktop applications and reacquire stale window handles. A missing desktop application does not imply that MCP modeling tools are unavailable, and the reverse is also true.

6. For skills, the inspected loader reads flat .geopogo-skill or .md text files under the current user’s roaming GeopogoAI/Skills directory. Call list_skills then get_skill; meaningful first lines provide discovery descriptions.

#### Failure cases

- Do not install or overwrite unrelated add-ins to solve a missing-session-tool problem. A stale/null accessibility tree requires rediscovery, not blind clicks.

#### Acceptance checks

- Confirm tools are exposed and a read-only call reaches the intended RVT; report which layer is still unavailable.

#### Source coverage

- Geopogo connection and host availability (source key: connection).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="geopogo-missing-middle-townhomes"></a>

## 6. Geopogo — Missing-Middle Townhome Pattern

**Skill name:** `geopogo-missing-middle-townhomes`

Model attached townhomes, party walls, roof terraces, foundations, rooms, and drawing sets.

#### Compatibility and scope

Read the live connector's tool schemas before executing examples; installed versions can differ. Historic failures describe the recorded session, not every release. The installed create_roof schema inspected for this package automatically selects a floor-plan view and restores the original view; older builds may need an explicit view switch. Check returned state and loaded types. Tool availability and a skill's presence do not prove the workflow has been tested on the recipient's Revit version. Use only the intended model and the user's authorized scope.


Drafted by inspecting a real, fully-documented project through the `geopogo-ai` connector's read tools: **an anonymized seven-unit townhome reference project** — 7 attached townhome units, 3 stories each plus a private roof deck. Everything below — level names, room program, numbering scheme, wall types, roof/parapet approach, and the gotchas — is what that project actually contains, warts and all (its own model warnings are quoted in §7). Treat this as a strong starting template for the next missing-middle project, not a spec to copy blindly: verify counts, dimensions, and code requirements (fire-rated demising walls, egress, stair geometry) against the new site and jurisdiction every time.

Always run §1 of `geopogo-complete-v2` first (inspect before you build). This skill layers the townhome-specific pattern on top.

#### 1. What this typology is

A missing-middle townhome building is a row of individually-owned/rented dwelling units, each running the full height of the building, sharing **party (demising) walls** with its neighbors on one or both sides, each with its **own ground-level entrance** (no shared interior corridor), and often a **private roof deck** behind a parapet instead of a pitched roof over the whole unit. It reads as a single building massing-wise but functions as N stacked, side-by-side houses.

#### 2. Level stack

The reference project used six intended levels plus one accidental duplicate for a 3-story-plus-roof-deck building:

| Level | Elevation | Purpose |
|---|---|---|
| Ground Floor | 0'-0" | Entry, garage/carport, flex space, ground-floor bath |
| Second Floor | 9'-0" | Kitchen, dining, living |
| Third Floor | 19'-0" | Bedrooms, bathrooms |
| Roof | 28'-9" | Roof terrace deck + stair-well enclosure |
| Top of Parapets | 32'-9" | Parapet cap around the roof deck |
| Top of Stairs | 37'-9" | Top of the stair-tower enclosure that continues above the roof |

Floor-to-floor heights here are 9'-0" (ground→2nd) and 10'-0" (2nd→3rd) — confirm the user's actual stated heights rather than assuming these.

**Gotcha:** the source project also has a level named **"L3" at the identical elevation as "Third Floor"** (both 19'-0") — almost certainly a leftover duplicate from an earlier revision. Don't replicate that; pick one level name per elevation and confirm with `get_levels` that you don't have two levels stacked on top of each other, which silently splits walls/rooms across both and causes exactly the kind of duplicate-element warnings in §7.

Create the stack with `create_building_levels` (or loop `create_level`), then `get_levels` to confirm — see geopogo-complete-v2 §1.1 and §5.1.

#### 3. Room program per unit, per floor

Each unit repeats roughly this program (not every unit has every room — flex space, garage, or carport vary by unit):

- **Ground Floor:** Entrance, Storage, Hallway, Closet, Bathroom, Flex Space (or Garage / Carport / Bike Storage for end/corner units), Outdoor Patio.
- **Second Floor:** Kitchen, Dining, Living Room, Bathroom, Storage, sometimes a Bedroom or Patio for units that put a bedroom on this level instead of a garage.
- **Third Floor:** Primary Bedroom, Bedroom 1, Bedroom 2, Bathroom(s), Walk-in Closet(s), Hallway, Storage.
- **Roof:** Roof Terrace (the private deck, typically 400–600 ft²) + a Stair Well enclosure (the stair tower that continues up from Third Floor, roughly 35–75 ft² footprint).

Model rooms with `create_room` inside closed wall loops (open boundaries produce an "unbounded" room with zero area — several rooms in the source project show `areaFt2: 0` for exactly this reason, e.g. unenclosed Flex/Patio/W-I-C spaces). Set names/numbers explicitly with `set_room_name_number` — see §7 for why you can't rely on defaults.

#### 4. Room numbering convention

The pattern used: **hundreds digit = unit index** (1 through 7, with 8 reserved for shared amenity spaces like bike storage), **tens+ones = room within the unit** on the ground floor (101, 102, 103…), and a **floor suffix appended with a hyphen** for upper floors: `-2` for Second Floor, `-3` for Third Floor, `-4` for Roof. So unit 3's third-floor primary bedroom is `303-3`, unit 3's roof stair well is `302-4`.

Adopt this scheme (or state your own to the user before you start) up front, because Revit does **not** enforce unique room numbers automatically, and the source project has real duplicate-number warnings from not doing this consistently (§7) — plus at least one unit (unit 6) breaks its own convention, numbering its stair well `601-4` instead of the `X02-4` pattern every other unit uses. Consistency is your job, not the connector's.

#### 5. Party walls, exterior walls, and wall types

- **Exterior envelope:** the reference project uses two wall types depending on trim condition — `Exterior - Wood Shingle on Wood Stud` and `Exterior - Wood Shingle over Wood Siding on Wood Stud` (both wood-framed, shingle-clad — a common light-frame missing-middle assembly). Confirm the actual type names in the new project with `get_element_types` before placing anything; don't assume these exact strings exist.
- **Party/demising walls:** the reference project uses a dedicated custom type, `W1`, for the walls shared between adjacent units, distinct from the exterior types. **This project's `W1` is not one of the model's fire-rated types** (it has separate `Interior - X Partition (1-hr)` and `(2-hr)` types available but W1 isn't tagged as one of them in what's inspectable here) — before you reuse this pattern, confirm with the user what fire-rating their jurisdiction requires for an attached-dwelling demising wall (commonly 1-hour minimum, often 2-hour depending on code and sprinklering) and pick or build a compliant type. The connector can place whatever wall type you tell it to; it cannot verify code compliance for you.
- Use one shared party-wall type across the whole building (type-level edits per geopogo-complete-v2 §1.4) rather than duplicating a new type per unit — see the duplicate-Type-Mark gotcha in §7.

#### 6. Roof and parapet massing

Two roof systems appear side by side in the same building:

1. **Flat roof deck over the terraces:** a `Generic - 9"` flat roof type at the Roof level, ringed by a dedicated `Parapet` wall type rising to "Top of Parapets." This is what makes the private roof deck usable and code-legal as a guarded terrace.
2. **Pitched roof over the stair enclosure / any non-terrace portion:** `Wood Rafter 8" - Asphalt Shingle`, a sloped roof type, used where the massing isn't a walkable deck.

Sequence: build both with `create_roof` per geopogo-complete-v2 — **load `create-roof-workflow` and check the installed schema for automatic view switching** (older builds required an explicitly active floor plan). Add the parapet as a short wall run (`create_wall` with the `Parapet` type) along the terrace edge from Roof level up to Top of Parapets. The stair enclosure walls continue further, from Roof up to Top of Stairs, using the same exterior wall type as the rest of the building so the stair tower reads as part of the massing rather than a mechanical penthouse.

#### 7. Known gotchas — quoted from this project's own `get_model_warnings`

The reference model currently carries 127 live Revit warnings. Most cluster into a few classes that are structural to this typology, not one-off mistakes — expect them and design around them:

- **Duplicate room "Number" values** — by far the most common warning (14+ instances). Happens when a unit's room layout is copied from a template unit and the numbers aren't re-assigned. Always call `set_room_name_number` explicitly after copying a unit, per §4.
- **"Highlighted walls overlap... Use Cut Geometry to embed one wall within the other"** — recurs at nearly every floor-to-floor transition where a Ground Floor wall type meets a different Second/Third Floor or Roof wall type stacked directly above it. After stacking wall types vertically, run `get_model_warnings` and `join_geometry` on the affected pairs rather than assuming Revit auto-resolves the seam.
- **Stair run-width, tread-depth, and riser-height warnings** — the single largest warning category (30+ instances, touching nearly every stair in the building). Missing-middle stairs are squeezed into tight unit footprints, so the stair type's default run width/tread/riser routinely violates the type's own minimums once actually laid out. After `create_stairs` for each unit, explicitly set width/tread/riser to the applicable code minimums (verify with the user's jurisdiction) rather than accepting the family default, and re-check `get_model_warnings` per unit before moving to the next one.
- **Duplicate "Type Mark" values** on wall types that were duplicated per-unit instead of reused (e.g., a `W1` party wall duplicated to `W1 2`, or a `Parapet` type sharing a mark with an exterior wall type). Reuse one shared type across all units (geopogo-complete-v2 §1.4) instead of duplicating a fresh type per unit; if you must duplicate, rename the Type Mark too so schedules stay unambiguous.
- **Wall-sweep mitering failures** at some corners ("Failed to properly create all segments... may not properly miter with neighboring sweeps") — cosmetic/documentation-only, not structural. Flag it to the user but don't burn calls chasing it.
- **"Room is not in a properly enclosed region"** — appears wherever a patio/flex/W-I-C room boundary wasn't fully closed by walls or room-separation lines; matches the zero-area rooms noted in §3.

#### 8. Repeating the unit across the site

Don't model N units from scratch. Build and fully verify **one unit** (all floors, roof, stair, room numbering) first, then:

1. `copy_element` the unit's full element set at the party-wall bay spacing to generate the next unit.
2. If the plan alternates handing (common so kitchens/baths can share a wet wall across the party line), `mirror_element` alternating units instead of a plain copy.
3. Immediately re-run `set_room_name_number` on every copied room — copies inherit the source unit's numbers, which is exactly how the duplicate-number warnings in §7 happen at scale.
4. Re-check `get_model_warnings` after each unit is placed rather than waiting until all N are in, so a systemic issue (e.g., a stair type that's too narrow for the bay width) doesn't get baked into all seven copies before you notice it.

#### 9. Documentation set

The reference project's sheet index is a reasonable template for a missing-middle permit/construction set: Title Sheet, Site Plan(s) (including a curb-cut plan and a flood-plain overlay where applicable), Ground/Second/Third Floor Plan, Roof Plan, North-South and East-West Building Elevations, Building Sections, Architectural Enlarged Views, Architectural Details, Door/Window/Room-Finish/Structural Schedules, Specifications, a 3D-views sheet, plus **per-unit floor-plan sheets** (e.g., "2nd Floor Plan – Unit 6") for individual-unit sales or permit packages. Build views first, then sheets, then place — see geopogo-complete-v2 §8.

#### 10. Verify and render

- Re-query `get_rooms` and confirm exactly N enclosed units with no duplicate numbers.
- Re-query `get_levels` and confirm no accidental duplicate-elevation levels (§2).
- `verify_model` and `get_model_warnings`; work through the categories in §7 rather than treating a large warning count as background noise.
- `export_view_to_image` from a 3D view and from at least one elevation so the user can compare massing and rhythm (bay spacing, roof-deck/parapet line, party-wall alignment) against their reference.

#### 11a. Foundations, foundation walls, and footings

Two viable depths, pick based on what's asked for:

**A. Footings straight under the Ground Floor walls (slab-on-grade / minimal embedment).** Fastest, but the footing sits right at the Ground Floor's own base (elevation 0), which is shallow for anything but a slab-on-grade condition. Just call `create_wall_foundation` directly on the Ground Floor bearing walls — see part C below. This was the first pass on this project and was superseded by B once "drop the foundation down at least 6 feet" was requested.

**B. A real embedment with a foundation (stem) wall up to the first floor — the pattern this project now uses.** When the brief calls for a specific minimum depth (frost depth, a crawlspace, a basement-height embedment), don't just push the footing type deeper — model an actual below-grade foundation wall so there's a real assembly between the footing and the first floor framing, then foot *that* wall:
  1. `create_level` a new level (e.g. `"Foundation"`) at the required negative elevation relative to Ground Floor (e.g. `-6` for a 6' embedment). Existing levels don't need to move.
  2. Trace the **same footprint and wall roles** as the Ground Floor bearing walls (full perimeter + any continuous interior bearing spine) at this new level, using a `Foundation - ##" Concrete` wall type from `get_element_types(category: "Walls")` (this project's template had `Foundation - 10" Concrete` and `Foundation - 12" Concrete` — a thicker one for the exterior/party perimeter, a lighter one is fine for an interior spine wall). Set `Base Constraint` = the new Foundation level and `Top Constraint` = Ground Floor, so the wall physically spans the full embedment depth up to the first floor — this *is* "the foundation wall up to the first floor."
  3. Apply the `create_walls_batch` / `Top Constraint` gotchas from §11 to these walls too — batch type application worked correctly in this pass, but always spot-check with `get_element_parameters`, and always explicitly set `Top Constraint` afterward (new walls still default to unconnected).
  4. If footings already exist directly under the Ground Floor walls from a shallower first pass (part A), delete them (`delete_element`) — they're now redundant and at the wrong depth — and re-run `create_wall_foundation` against the new foundation walls instead, not the Ground Floor walls. The footing then lands ~1' below the new deep level automatically.

**C. Footing placement (either depth):** `get_wall_foundation_types` first — don't assume a name, it varies by template (this project had `Bearing Footing - 36" x 12"`, `Bearing Footing - 36"x18"`, and `Retaining Footing - 24" x 12" x 12"`). Use the plain bearing footing for ordinary perimeter/party/spine walls; reach for the retaining type only where the wall is actually holding back soil on one face (a daylight condition), which a fully-buried perimeter foundation wall isn't. Then `create_wall_foundation(wallId, foundationTypeName)` once per wall — it follows the wall's full length and sits below whatever level that wall's `Base Constraint` actually is, so the depth follows automatically from which walls you foot (Ground Floor walls → shallow; new Foundation-level walls → full embedment). Don't foot Second/Third Floor walls — they bear on the floor structure below, not on soil.
- **Verify:** see the `get_structural_elements` gotcha below — don't rely on that query to confirm placement. Check each `create_wall_foundation` response for `success: true` and a real `elementId`, spot-confirm one or two with `get_element`, and take a 3D or section screenshot to see the footing ledge projecting past the wall face at the base of the building.

#### 11. Historical connector observations (recorded build 2.0.0, 2026-07-10)

These are retained historical observations, not current universal limitations. Recheck the installed version and schema; the currently inspected roof tool documents automatic plan-view switching. Do not skip working native stairs or roofs because of this history.

Confirmed by actually building one full townhome unit (levels → walls → doors/windows → rooms → stairs → roofs) through the connector in a fresh project on 2026-08-20. These are reproducible failures, not one-off flukes — don't spend calls retrying them past the first confirmation:

- **`create_stairs` is broken in this build.** Every call — regardless of a plan view being active, straight geometry, default vs. explicit width — fails with `Revit plugin error (500): A sub-transaction can only be active inside an open Transaction.` This is a connector-side transaction-handling bug, not a geometry problem. **Fallback:** mark the stair core with a `create_mass_box` placeholder sized to the run (width × run-length × floor-to-floor rise, based at the correct level elevation), name it clearly as a placeholder (e.g. `"Stair Shaft G-2 (placeholder - create_stairs broken in build 2.0.0)"`), and tell the user the actual stair needs a manual Stair sketch in Revit (or a retry once the connector is patched — check `get_geopogo_version` against a newer build first). Report the bug to the Geopogo team with the exact version/build string.
- **`create_roof` is broken in this build even with the plan-view fix applied.** geopogo-complete-v2's §3.3 gotcha (switch to a floor-plan view first) is necessary but was **not sufficient** here — with a confirmed-active plan view, `create_roof` still fails on every call, including a trivial 4-point rectangle, with `Revit plugin error (500): Value cannot be null.` Don't loop retrying it once you've confirmed the plan view is active and a minimal-geometry call still fails. **Fallback, in order of preference:** if the "roof" is actually a walkable flat deck or terrace, use `create_floor` with the deck's footprint polygon (a real Floor element — schedulable, room-bounding, and the right category for a walkable surface — rather than a massing stand-in) and ring it with a parapet wall (see next bullet for thickness). Only fall back to `create_mass_extrusion` for a genuinely non-floor roof form (e.g. a pitched cap with no walkable top) as a last-resort massing stand-in, named as a placeholder the same way as the stair fallback above. This is the same "command broken in this build → fall back, advise reporting the bug" pattern geopogo-complete-v2 documents for the single-house case — it applies here too, and this session shows the plan-view workaround alone doesn't always clear it.
- **`create_walls_batch` can silently ignore `wallTypeName` and default every wall in the batch to the model's fallback type, while reporting the *requested* type name back as if it succeeded.** In this session, a 4-batch sequence (Ground/Second/Third floor walls, then Roof-level walls) had its first three batches silently apply `"Generic - 8""` to all 25 walls regardless of the exterior/party/interior type each was supposed to get — the batch response's `wallType` field lied. The 4th batch (Roof level) applied types correctly, so this isn't universal — it's read as a stale-type-cache issue early in a session, not a permanent block. **Always verify:** after any `create_walls_batch` call, spot-check a couple of the created walls with `get_element_parameters` (look at `Type` / `Type Id`, not the batch response) rather than trusting the creation response. If types are wrong, fix with `set_wall_type` per wall — that tool's own response (`previousType`/`newType`) is reliable. This matters most for party/demising walls, where the wrong type silently means the wrong (or no) fire rating.
- **Newly created walls default to an unconnected `Top Constraint` (`-1`) with a fixed `Unconnected Height`, not a live constraint to the level above.** This works dimensionally (the wall physically reaches the next floor if you passed the right height) but isn't how Revit walls are conventionally modeled, and in this session it was the direct cause of the "walls overlap… may be ignored when Revit finds room boundaries" warning cluster at every floor transition (25+ instances) — setting `Top Constraint` explicitly made every one of those warnings disappear. After creating a level's walls, set `Top Constraint` on each to the level above via `set_element_parameter(elementId, "Top Constraint", <levelElementId>)` — it accepts the target level's element ID as a plain number despite the parameter's `ElementId` storage type. Do this before you consider a floor's walls finished, not as a later cleanup pass.
- **`create_door` / `create_window`'s `familyTypeName` matches by dimension string alone, not family, and can silently place the wrong family.** When two loaded families share an identical type-name string (e.g. `Door-Exterior-Single-Two_Lite` and `Door-Passage-Single-Flush` both have a `36" x 80"` type), the tool picked the interior passage-door family for an exterior opening without erroring. Always read the `familyName` field back from the call's own response and check it against what you intended; if it's wrong, fix it with `change_element_type` (pass both `typeId` and `familyName` to disambiguate — `familyName` alone on the create call isn't accepted as a parameter) rather than re-deleting and re-placing.
- **New windows default to `Sill Height: 0`** (bottom of the window at floor level) rather than a residential-typical 3'. The `create_window` tool has no sill-height parameter of its own — set it explicitly afterward with `set_element_parameter(elementId, "Sill Height", 3)` (feet) on every window, or every opening will sit on the floor instead of at a normal sill line.
- **`get_structural_elements(elementType: "Foundation")` does not return continuous wall footings placed with `create_wall_foundation`**, even immediately after a confirmed-successful creation. In this session, 5 footings were placed on Ground Floor bearing walls, each returning `success: true` with a real `elementId`; a follow-up `get_structural_elements(elementType: "Foundation")` call returned `count: 0`. This is a query-side gap, not a creation failure — `create_wall_foundation`'s own response is trustworthy, and `get_element(elementId)` on the returned id confirms the element exists with `category: "Structural Foundations"` and the correct type. **Don't treat an empty `get_structural_elements` result as proof a footing wasn't placed** — verify with `get_element` on the id from the creation response instead, and cross-check visually with a section view or 3D screenshot showing the footing ledge at the base of the wall.

---

<a id="revit-aircraft-interiors"></a>

## 7. Aircraft shells, decks, interiors, and cutaways

**Skill name:** `revit-aircraft-interiors`

Model aircraft exterior and multi-deck conceptual interiors with coordinated shells, rooms, furnishings, and inspection views.


#### Evidence and scope

Saved Air Force One exterior and detailed-interior notes report delivered models, room schedules, and sheet sets; a later requested Zaha project is separate work.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Set airframe axes and public dimensional anchors, then model fuselage, wing sweep, tail, engines, landing gear, glazing, doors, and livery with named parts.

2. Create a genuine interior cavity using thin shells or hollow sections; transparent solid envelopes still intersect furniture. Maintain removable shell groups for cutaway views.

3. Lay out deck studies from supplied diagrams, explicitly treating exact historic/security/system layouts as unverified. Coordinate floor openings and stairs with upper/lower levels.

4. Use native partitions, floors, rooms, and doors for room schedules where useful; keep aircraft-specific seats, consoles, racks, and curved cabin details as clearly identified custom geometry.

5. Build visibility filters for exterior, cockpit, forward/aft cabins, cargo, and integrated cutaways. Preserve full-aircraft views and furnish against actual passage/door clearances.

6. Produce enlarged furniture plans, room keys, longitudinal sections, and schedules. Count modeled seating separately from certified occupancy/capacity.

#### Failure cases

- Whole-project bounds may include template extents. Conceptual lavatories or equipment racks are not connected aircraft systems. Do not erase earlier aircraft delivery just because the session later changed subjects.

#### Acceptance checks

- Scoped airframe dimensions; shell/interior separation; enclosed room count; floor openings; passage clearance; cutaway readability; warning and save/hash evidence.

#### Source coverage

- Air Force One exterior and detailed interiors (source key: aircraft).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-articulated-animation"></a>

## 8. Articulated walking, robots, and component animation

**Skill name:** `revit-articulated-animation`

Animate characters or mechanical walkers using preserved component hierarchies, joint pivots, neutral poses, and measured update cost.


#### Evidence and scope

Based on Mario walk checks, Optimus Gen 2 refinement and responsive controls, and the later 215-part walker preview.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Store immutable bind/neutral transforms and component membership. Define hip, knee, shoulder, elbow, neck, or mechanical pivots in a consistent local coordinate frame.

2. Derive each pose from the bind state plus phase, rather than repeatedly accumulating rotations. Counter-swing paired limbs and keep ground/root translation separate from local articulation.

3. For four-leg walkers, author phase offsets and joint trajectories that preserve foot/leg connectivity. Treat scripted gait as visual motion unless actual kinematics/contact are solved.

4. Keep high-detail static instances shared where possible. Update whole-body transforms more often than expensive mesh/pose rebuilds; a source optimization used an eighth-update/400 ms pose throttle, which must be profiled rather than blindly copied.

5. For temporary high-frequency motion use revit-directcontext3d; for editable key poses or small scenes, controlled document transactions may be appropriate.

6. On pause preserve the chosen pose; on reset/stop restore the neutral geometry and initial position exactly. Close or supersede older animation owners before launching a new one.

#### Failure cases

- A transform handler timing is not full render-frame timing. A model made of separate parts is not automatically a skeletal rig.

#### Acceptance checks

- Opposite strides; connected pivots; no accumulated position drift; stable component identities; neutral reset; visible rendered motion; measured handler and draw timings separated.

#### Source coverage

- Peach Castle, Mario, chase camera, gait and music (source key: mario).
- Fremont Optimus modeling and production animation (source key: factory).
- Optimus controller responsiveness (source key: responsive).
- Four-legged walker modeling and animation (source key: walker).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-bridges"></a>

## 9. Suspension and cable-stayed bridge studies

**Skill name:** `revit-bridges`

Build editable bridge concepts with towers, decks, cables, hangers, supports, and reference-based proportions.


#### Evidence and scope

Derived from saved Golden Gate and Gordie Howe-inspired bridge studies with separate technical and visual checks.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Identify bridge type and design anchors: total length, main spans, deck width, tower height, clearance, and water/ground datum. Use verified sources when exact dimensions matter; label photo-estimated details.

2. Create a coordinate schedule for towers, piers, deck sections, and anchorages. Build a small bay and inspect alignment before duplicating repetitive parts.

3. For suspension bridges, parameterize the main cable curve and sample hanger positions consistently. For cable-stayed bridges, derive individual stays from tower attachment levels to deck anchor stations.

4. Use sweeps, rods, blends, floors, or custom solids appropriate to the geometry. Maintain cross-section orientation and avoid short or degenerate segments.

5. Refine tower silhouette in elevation, not only perspective. Preserve lane/deck edges and cable clearances through tower corrections; save the pre-correction version.

6. Assign coherent materials and create overall, tower, roadway, and side-elevation views. Distinguish conceptual trusses/anchorage geometry from structural design.

#### Failure cases

- Hundreds of correctly counted hangers do not prove the tower shape or engineering. A failed sweep needs corrected orientation, not repeated identical calls.

#### Acceptance checks

- Span and tower anchors; cable continuity; hanger counts and alignment; front/side/three-quarter review; scoped bounds; warnings and saved copy.

#### Source coverage

- Golden Gate suspension bridge and tower revisions (source key: golden-gate).
- Gordie Howe inspired cable-stayed bridge (source key: gordie-howe).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-character-controls"></a>

## 10. Third-person characters, walking controls, and chase cameras

**Skill name:** `revit-character-controls`

Add a controllable character to a Revit scene with heading-relative movement, camera follow, basic collision, and focus-safe input.


#### Evidence and scope

Recovered from delivered Mario and Optimus sources/docs plus Miami walkthroughs; those artifacts demonstrate more than the earlier abbreviated session summaries.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Choose a scene-space position, heading, ground height, and character origin independent of mesh pose. Map forward/side vectors from heading so W/S and sidestep remain local to the character.

2. Use a modeless controller with explicit focus behavior. A/D may turn and Q/E strafe as in source examples, but bindings must be documented for the actual controller.

3. Compute a chase eye/target from the stable body origin, not the animated body bounce. Cache the follow view and update only the selected first/third-person camera.

4. Represent simple barriers and traversable openings explicitly: building footprint, doorway passage, moat/bridge, equipment aisles, terrain, and site edge. Test the narrowest intended route.

5. Apply walking pose while movement is accepted; restore neutral pose on release/focus loss. Revit rendering can lag, so use bounded delta time and avoid teleport-sized updates after stalls.

6. Provide overview, follow, reset, pause, and save actions. Verify both the intended view and the actual control panel; camera activation alone is insufficient.

#### Failure cases

- Basic collision is not a full navigation mesh. Trees, camera obstruction, jumping, or interiors are absent unless implemented and tested.

#### Acceptance checks

- Physical input; heading-relative movement; turning/strafe; camera behind character; doorway/bridge traversal; blocked barriers; focus loss; reset without drift.

#### Source coverage

- Peach Castle, Mario, chase camera, gait and music (source key: mario).
- Fremont Optimus modeling and production animation (source key: factory).
- Optimus controller responsiveness (source key: responsive).
- Miami street, driving, shop, population and environment (source key: miami).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-cinematic-export"></a>

## 11. Camera flythrough and intro-video export

**Skill name:** `revit-cinematic-export`

Export a reproducible Revit camera sequence with frame checkpoints, stable framing, and separate video/audio assembly.


#### Evidence and scope

Derived from the saved Miami Intro.cs camera exporter and frame-generation workflow. Earlier intro footage represents the scene revision at render time.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Freeze the intended scene revision and define a shot list: camera start/end, look-at start/end, duration, frame count, and output aspect ratio. Check the entire camera path for collisions or obscured views.

2. Create a dedicated camera view with deliberate crop/FOV and visibility. Preserve the user’s original active view and restore it in a finally path; the historical exporter should not be copied without that cleanup.

3. Interpolate camera eye/target with a consistent time base. Revit updates and exports happen in valid API contexts; an external video encoder runs after image generation.

4. Write numbered frames and a checkpoint containing completed/total frames and error state. Resume only against the same scene/version; avoid mixing old and new frame sequences.

5. Verify frame count, dimensions, ordering, representative frames, and shot boundaries before encoding. Set encoder FPS explicitly so exported frames produce the intended duration.

6. Add original/authorized music separately. Inspect the resulting video and report whether it represents the current scene or an earlier stage.

#### Failure cases

- A camera script or completion flag does not prove the video exists. Adding later city geometry or live ambience does not update an already rendered film.

#### Acceptance checks

- All frames present; no clipping/blank images; duration/FPS/aspect correct; original view restored; encoded playback reviewed; scene revision documented.

#### Source coverage

- Miami camera flythrough and video export (source key: miami-intro).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-data-centers-mep"></a>

## 12. Data-center BIM, equipment, and MEP coordination

**Skill name:** `revit-data-centers-mep`

Develop data-center concept models with native systems where supported, equipment detail, rooms, and explicit connection limits.


#### Evidence and scope

Based on the saved data-center concept and detail pass; seven recorded plumbing flow-direction warnings remained and connected MEP systems were not delivered.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Translate the requested program into floor/room zones, rack aisles, plant areas, structure, roof, circulation, and service access. Use the actual agreed scope; a folder title is not a design requirement.

2. Source manufacturer families from official suppliers when requested. Record family/version/type and distinguish a placed manufacturer family from correctly selected or sized equipment.

3. Place native walls, floors, ceilings, racks/equipment where available, ducts/pipes/trays, sprinklers, and diffusers according to supported tools. Use named custom geometry for schematic equipment envelopes and details.

4. Add supports, access panels, grilles, valves, roof walkways, hatches, louvers, coping, and scuppers without implying fabrication or connection completeness.

5. Verify height-reference semantics for openings: absolute elevations and offsets from a host level are different. Spot-check ceiling types and family assignments after creation.

6. Inspect actual MEP connectors, system membership, flow direction, and warnings. If joining/routing is unavailable, report placed schematic systems as unconnected; do not hide warnings or change classifications merely to clear them.

#### Failure cases

- Sprinkler placement does not prove hydraulic coverage; diffusers without airflow do not prove HVAC design. Rack detail counts are separate from native equipment/room counts.

#### Acceptance checks

- Enclosed rooms; native categories/types; service clearances; elevations; explicit connector/system status; all residual warnings; sheets and saved output.

#### Source coverage

- Data-center concept and equipment detailing (source key: data-center).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-day-night-audio"></a>

## 13. Day/night cycles, ambience, and vehicle radio

**Skill name:** `revit-day-night-audio`

Add time-of-day viewport effects and layered audio with spatial/daylight blending, radio ducking, and reliable cleanup.


#### Evidence and scope

Derived from Miami V11-V16 environment/audio work and the original generated castle chiptune. Supplied commercial/reference media is not included in this skill package.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Maintain an original daytime material palette and separate simulation time from real wall-clock time. Define day/sunset/night/sunrise transitions and explicit pause/preset behavior.

2. Throttle material/sky/sun updates independently of character movement. The source refreshed lighting about once per second; profile regeneration before increasing frequency.

3. Use persistent audio players for ambience and radio; avoid recreating a player every frame. Blend gains by daylight and scene position, pausing inaudible loops and resuming intentionally.

4. Start/pause radio from vehicle ownership state, including a parked occupied car if desired. Duck environmental audio when radio is active; keep mute and next-track controls independent.

5. Use original or authorized audio supplied for the recipient project. Extract audio from a supplied media container only when appropriate; do not silently redistribute the original session’s music with a public plugin.

6. On controller close, release players and timers. Preserve palette/state assets alongside the runtime; test a fresh launch and missing-audio behavior.

#### Failure cases

- Warm material colors are not physically simulated electric lights. Viewport audio is separate from an already encoded intro video.

#### Acceptance checks

- Full day/night cycle; original palette restoration; shoreline blend; enter/exit radio; independent mute; no double playback; cleanup on close; authorized asset manifest.

#### Source coverage

- Miami street, driving, shop, population and environment (source key: miami).
- Peach Castle, Mario, chase camera, gait and music (source key: mario).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-demolition-physics"></a>

## 14. Conceptual demolition and rigid-body playback

**Skill name:** `revit-demolition-physics`

Build an in-Revit visual collapse prototype with a separate physics simulation, source-element mapping, cached frames, and reset.


#### Evidence and scope

Based on the BEPUphysics 2.4.0 prototype, physics source/tests, and DirectContext3D renderer. Historical final Reset-to-BIM verification was incomplete.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Clarify that native Revit Demolish is phasing, not falling/collision simulation. Preserve the original project and create an explicitly separate demo scene when that is the brief.

2. Map each source BIM element to a simplified body/collider and initial transform. The source prototype used presegmented pieces and a scripted release; it was not an arbitrary-RVT fracture importer.

3. Keep physics computation independent of Revit document APIs. Precompute a bounded cache or advance a pure simulation; marshal only geometry snapshots needed by the renderer.

4. Validate all frames for finite transforms, bounded coordinates, gravity, contact behavior, and expected collapse. Tune collision detection/contact settings against tunneling and report measured penetration tolerance.

5. Render via revit-directcontext3d in the dedicated Shaded view. Expose calculate, run/resume, pause, speed, reset, and load-saved-demo actions with unambiguous state.

6. Test Reset-to-BIM after the final run, not merely before a later capture. Restore source visibility before saving and package required physics libraries with their actual licenses.

#### Failure cases

- Uniform density, box colliders, scripted releases, and pre-cut slabs do not predict structural load paths, fracture, demolition safety, or blast behavior. A playback cache is not a verified engineering result.

#### Acceptance checks

- Every cached frame finite; contact/tunneling tolerance stated; visible debris; correct model ownership; pause/reset/close restoration; source saved and repeat launch verified.

#### Source coverage

- In-Revit demolition and BEPU rigid-body cache (source key: demolition).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-digital-twin-dashboards"></a>

## 15. Model-linked dashboards with explicit data provenance

**Skill name:** `revit-digital-twin-dashboards`

Build modeless factory dashboards that separate real Revit state from synthetic operational metrics and link selections to assets.


#### Evidence and scope

Derived from the native Optimus dashboard, seven-panel UI, model-selection tests, and recorded JSON/CSV export validation.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Define each field’s source: live Revit model, saved inventory snapshot, external feed, or synthetic demo. Label synthetic OEE, throughput, sensors, power, maintenance, safety, and logistics values in the UI.

2. Bind assets with stable model identity and UniqueId plus current element lookup. UI selection should select/reveal the matching Revit object and refresh its actual position.

3. Read document data within Revit API events and marshal immutable snapshots to the UI. Throttle refresh independently of animation; preserve responsiveness when Revit is busy.

4. Provide overview, production, robots/assets, maintenance, utilities, safety, and logistics views when relevant. Do not populate unrelated panels with invented live claims.

5. Separate alert acknowledgement from clearing the underlying condition. Show disconnected feeds explicitly; a Revit warning count is not a real-time equipment safety signal.

6. Export timestamped snapshots with provenance labels and units. Pause animation for a saved model, release controller ownership on close, and test reopening the delivered model.

#### Failure cases

- A polished dashboard is not a commissioned operational twin. Stored site counts are not live occupancy, and synthetic alarms must never be presented as measured safety conditions.

#### Acceptance checks

- All panels; actual asset selection; advancing/paused simulation; acknowledgement semantics; provenance labels; JSON/CSV export; save/reopen.

#### Source coverage

- Optimus model-linked dashboard (source key: dashboard).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-directcontext3d"></a>

## 16. Temporary DirectContext3D animation rendering

**Skill name:** `revit-directcontext3d`

Render moving scene geometry in Revit without rebuilding BIM elements every frame, while preserving reset and document ownership.


#### Evidence and scope

Derived from inspected DirectContext3D server implementations and saved walker/battle tests; this is an add-in pattern, not a Geopogo built-in animation tool.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Extract immutable mesh/material/component data in a valid Revit API context. Keep editable source BIM and temporary rendered poses separate, linked by stable source identifiers.

2. Register an IDirectContext3DServer with the appropriate external service. Implement current-version interface members, valid bounds, buffers, effect instances, and disposal; compile against the recipient Revit API.

3. Keep CanExecute eligibility a stable document/view predicate. Control visible playback separately; a transient false eligibility can be cached and suppress later rendering.

4. Update simulation transforms outside expensive document mutation where possible, then request redraw through valid UI/API handling. Track simulation seconds and renderedFrames independently.

5. Use a dedicated Shaded view for the source pattern and explicitly test other styles if supported. If source objects disappear but no debris renders, check eligibility, visibility, buffers, view style, and renderer error.

6. Temporarily hide only source elements in owned preview views. Reset/close restores their original visibility and stops simulation; do not turn temporary hidden state into permanent deletion or saving.

#### Failure cases

- A rising clock does not prove any pixels rendered. An RVT alone cannot carry this executable renderer. View bounds must cover moving geometry or it may be clipped.

#### Acceptance checks

- Visible temporary motion; increasing renderedFrames; correct bounds; unchanged source BIM; pause; view/document change; reset and close restoration; reopened model.

#### Source coverage

- In-Revit demolition and BEPU rigid-body cache (source key: demolition).
- Four-legged walker modeling and animation (source key: walker).
- Flyable airspeeder and walker battle (source key: battle).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-driving-games"></a>

## 17. Driving games and vehicle interaction

**Skill name:** `revit-driving-games`

Build Revit driving prototypes with acceleration, steering, chase camera, vehicle entry/exit, collision, and persistent state.


#### Evidence and scope

Based on DeLorean Highway and Miami drive/shop revisions. DeLorean road rollover and every later mission route were not fully replayed in recorded validation.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Preserve the original editable vehicle and generate a simplified motion/render representation if needed. Verify its dimensions, origin, materials, and collision footprint.

2. Separate velocity, heading, steering, acceleration, brake, reverse, and drag. Integrate bounded elapsed time; do not derive speed only from UI timer ticks.

3. For enterable vehicles, transfer ownership between player and autonomous traffic. Enter only within an explicit proximity region; exit only when stopped and an adjacent location is clear.

4. Define driveable surfaces and obstacles from scene geometry or a maintained collision model. Update these when roads, sidewalks, curbs, and buildings change. Permit curb crossing only where requested while retaining building/perimeter barriers.

5. Follow the vehicle with a stable chase camera. Clear input and stop/pause appropriately on focus loss; save position/elevation and restore it consistently.

6. Test coast, brake-to-zero, reverse, turning, collision, exit, and save/reload. If a road wraps, drive through the endpoint and verify position/camera continuity rather than assuming the branch works.

#### Failure cases

- Contact counters may count update contacts rather than distinct crashes. Stationary obstacles are not traffic simulation; simplified stopping is not realistic vehicle damage/physics.

#### Acceptance checks

- Acceleration/braking/steering; road and obstacle containment; entry/exit ownership; clear exit position; save/reload; full endpoint/route replay.

#### Source coverage

- DeLorean highway driving game (source key: highway).
- Miami street, driving, shop, population and environment (source key: miami).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-dynamo-animation"></a>

## 18. Dynamo animation and saved-scene playback

**Skill name:** `revit-dynamo-animation`

Create and verify runnable Dynamo animation graphs, periodic playback, state persistence, and safe continuation.


#### Evidence and scope

Based on saved CPython/Dynamo graphs and runtime launchers; source documentation contains several historical intervals, so inspect the actual current graph.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Decide whether the graph directly updates Revit geometry or launches a separate modeless C# runtime. Deliver the graph and required source/runtime companions, not just code pasted in chat.

2. Guard the exact intended project or a validated scene identity. Inspect saved state/result files before rebuilding. Distinguish build graphs for empty documents from playback graphs for existing scenes.

3. For direct animation, use a clock dependency that allows Periodic mode; give PLAY, RESET, speed, and manual-time controls clear semantics. Pulse/latch RESET so a retained true value does not reset every tick.

4. Start from an orthographic view where the source installations permitted Dynamo launch; the runtime can then switch to perspective. Reopen/retrigger cached unchanged launcher nodes when necessary.

5. Use bounded elapsed-time integration and a conservative initial interval. Increase simulation speed separately from update frequency, measuring responsiveness and behavior at each change.

6. Compare timestamped results across a timed interval: playing/running true, increasing simulation seconds or frame count, error null, stable element IDs, and visible motion. Pause before a fixed-pose save.

#### Failure cases

- Python compilation and graph JSON generation are not playback tests. Running two animation graphs can compete for the document. Historical 800/1000/2000/5000 ms settings are examples, not a universal safe interval.

#### Acceptance checks

- Graph opens; correct dependencies/runtime; PLAY moves; pause freezes; reset works once; timed telemetry advances; same objects updated; saved state reloads.

#### Source coverage

- Sims house, people, needs and navigation (source key: sims).
- Wonderland theme-park rides and playback (source key: park).
- Peach Castle, Mario, chase camera, gait and music (source key: mario).
- DeLorean highway driving game (source key: highway).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-facade-repair"></a>

## 19. Constrained façade recess and dependent slab repair

**Skill name:** `revit-facade-repair`

Correct projecting or constrained façade panels together with returns, joins, and affected slab edges.


#### Evidence and scope

Based on the saved Empire State Building recess correction and city storefront/roof cleanup.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Clarify the geometric target from the user’s correction: moving the broad wall panel is different from changing window reveal depth. Identify affected hosts, short connectors, slab edges, and dependent openings.

2. Save a backup and record locations/IDs for the affected set. Derive recess offsets from intended adjacent returns rather than a generic building-wide number.

3. If a move reports success without coordinate change, inspect constraints and joins. Remove only identified short blockers, move the target, and compare the actual location curve.

4. Recreate returns with deliberate join settings such as disallowJoinAtStart/disallowJoinAtEnd where supported. Re-query hosted elements and type assignments afterward.

5. Regenerate affected floor footprints to match the new envelope. Validate new area, elevation, and footprint before deleting an old slab.

6. Inspect multiple elevations and sections, including shadow lines and slab projection. Treat a façade revision as a coordinated assembly change.

#### Failure cases

- Do not trust move success without coordinate readback. Wall-only changes can leave floor edges projecting. Preserve unaffected levels and elements.

#### Acceptance checks

- Expected recess measured; connector continuity; new slab areas; hosted openings intact; warnings; saved revised model and comparison view.

#### Source coverage

- Empire State Building facade correction (source key: esb-repair).
- Paris blocks, storefronts, roofs and street detail (source key: city).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-factory-animation"></a>

## 20. Factory robots, conveyors, and production demos

**Skill name:** `revit-factory-animation`

Build and animate conceptual factory production bays with reusable robots, moving conveyors, arm cycles, and stable saved state.


#### Evidence and scope

Based on Fremont Optimus source/docs, Gen 2 refinement, and responsive-controller measurements; production arrangement is conceptual, not an as-built line.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Separate reference-based campus shell from the invented/confirmed production layout. Mark source evidence and uncertainty explicitly instead of calling a reference reconstruction an as-built digital twin.

2. Create workcells, conveyor lanes, service zones, equipment, and robot definitions with shared geometry. Keep the player robot independent of repeated station robots.

3. Refine robot form with a static front/side/three-quarter study instance so the walking avatar does not leave the inspection view. Preserve repeated instance IDs during geometry revisions.

4. Animate conveyor offsets, wrapped station positions, arm phases, and status indicators from a common simulation state. Keep factory start/pause/reset independent of player movement.

5. Reduce regeneration by grouping repeated motion and separating transform frequency from detailed pose rebuilds. Cache views and update only the selected camera.

6. On save, pause and persist production and avatar state; relaunch into a known paused state. Revalidate after campus/site refinement if the delivery claims retained animation.

#### Failure cases

- Illustrative arm motion is not collision-safe robot programming or industrial kinematics. Selected handler timings do not establish a controlled FPS improvement.

#### Acceptance checks

- All lanes advance; wraps are continuous; pause stable; reset exact; IDs preserved; player control works concurrently; save/reopen restores state.

#### Source coverage

- Fremont Optimus modeling and production animation (source key: factory).
- Optimus controller responsiveness (source key: responsive).
- Fremont highway, parking, yard and landscape (source key: factory-site).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-flight-combat"></a>

## 21. Flight controls and fictional vehicle combat

**Skill name:** `revit-flight-combat`

Create a Revit flight-game prototype with full heading control, altitude, target lock, swept projectile hits, health, and scripted outcomes.


#### Evidence and scope

Based on inspected Flight.cs and saved v6 battle verification: physical steering/climb, circling victory, reset, and an earlier engine-version defeat test were recorded separately.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Keep pure flight/combat rules independent of Revit. Represent position, yaw, pitch, bank, velocity, bounded timestep, run/pause state, health, target state, and cooldowns.

2. Expose clear modes: automatic cruise versus manual forward/back, heading turn, strafe/orbit, climb/descent, pitch, target lock, and chase/overview camera. Full yaw rotation should not be accidentally clamped to a narrow arc.

3. Use segment/swept intersection between previous and current projectile positions to avoid tunneling. Give each volley a stable ID so paired bolts do not apply duplicate intended damage.

4. Model return fire, damage cooldown, defeat, target-hit threshold, collapse phase, and reset explicitly. Distinguish scripted buckling/collapse from a physics simulation.

5. Render temporary craft/walker poses, lasers, and effects through DirectContext3D while retaining editable source components. Scope key capture to battle views and the intended application/controller focus.

6. Test a full orbit and altitude change, unlocked turning, target-lock aiming, hits/misses, enemy damage, victory, defeat, pause, and reset. Record which runtime/engine version produced each result.

#### Failure cases

- One successful combat result does not prove all flight controls. Mixed-version evidence must be labeled, not presented as every branch retested on the final build.

#### Acceptance checks

- Pure simulation tests plus physical-key live tests; swept hit detection; single-volley damage accounting; both outcomes; restored static geometry; no stale controller competing.

#### Source coverage

- Flyable airspeeder and walker battle (source key: battle).
- Four-legged walker modeling and animation (source key: walker).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-furniture-interiors"></a>

## 22. Furniture and compact interior studies

**Skill name:** `revit-furniture-interiors`

Model custom furniture or small rooms with clear dimensions, usable circulation, glass openings, and coordinated presentation.


#### Evidence and scope

Derived from the walnut desk, household layout repairs, and the saved 10-by-10-foot podcast-room verification.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. For furniture, break the reference into top, casework, supports, drawers, rounded frames, and material seams. Specify estimated dimensions before creating editable solids.

2. For a constrained room, establish clear interior dimensions separately from wall centerlines and overall extents. The source podcast example verified a 10-by-10-foot interior and 100-square-foot room; these are example inputs, not default sizes.

3. Place the corridor, glass door, adjacent glazing, ceiling, and walls before tables, chairs, microphones, displays, shelving, and acoustic-looking finishes.

4. Check door swing and passage clearances with furniture in place. Orient work surfaces, chairs, and fixtures toward their intended user and wall.

5. Assign wood, metal, upholstery, glass, and panel materials at the part level. Distinguish geometric acoustic treatment from an acoustic-performance calculation.

6. Create exterior/entry, interior, cutaway, plan, and detail views. Keep source-generated custom furniture editable through documented parameters or code instead of claiming a native family rig.

#### Failure cases

- Rounded custom solids may be selectable but not family-parameter driven. A stylish room does not establish acoustic isolation or measured existing-office conditions.

#### Acceptance checks

- Clear room dimensions/area; door and window count; unobstructed circulation; furniture proportions; material/readability review; save and warnings.

#### Source coverage

- Walnut desk and accessories (source key: desk).
- Stone and Cedar House and interior corrections (source key: house).
- Compact podcast studio and corridor (source key: podcast).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-geometry-units"></a>

## 23. Custom geometry, units, and scoped bounds

**Skill name:** `revit-geometry-units`

Create and audit DirectShape, loft, sweep, and mesh geometry without double unit conversion or misleading model bounds.


#### Evidence and scope

Extracted from custom modeling scripts and scoped-bounds reports. Several whole-document checks included cameras/template geometry; those results alone did not establish object scale.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Read the actual tool schema. Native Revit API lengths are internal feet; connector tools may accept explicit ft/m/mm. Convert once at a defined boundary, never both in coordinates and a declared units argument.

2. Define a local model frame, axis conventions, expected dimensions, and a subject-specific identifier prefix or element set. Keep drawing coordinates separate from camera positions and geographic coordinates.

3. Prototype one known-size solid and measure its stored bounding box before large batches. For profile sweeps, keep the extrusion/path direction compatible with the profile plane.

4. For lofts, use consistently ordered matching profile rings, avoid degenerate caps, and keep edges above Application.ShortCurveTolerance. For a tapered tip, terminate with a valid small ring or suitable solid strategy.

5. Measure bounds of the intended element set, using transformed corners where bounding boxes have transforms. Exclude cameras, levels, template scope boxes, and unrelated context explicitly.

6. After a scale correction, verify all dimensions independently and remove obsolete generated copies only after identifying their ownership. Preserve source parts and material grouping when generating an animation mesh.

#### Failure cases

- The recurring 509-by-600-foot whole-project box is not automatically the vehicle or walker size. More segmented solids will not fix a fundamentally wrong smooth silhouette.

#### Acceptance checks

- Known-size primitive round trip; finite coordinates; valid profiles; scoped bounds within declared tolerance; no duplicate scale-correction copies.

#### Source coverage

- Nautilus organic house and railing revisions (source key: organic).
- Cybertruck, Tesla Semi/trailer and DeLorean modeling (source key: vehicles).
- Four-legged walker modeling and animation (source key: walker).
- Air Force One exterior and detailed interiors (source key: aircraft).
- Fremont highway, parking, yard and landscape (source key: factory-site).
- Monumental arch and sculpture refinement (source key: monument).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-geopogo-continue-verify"></a>

## 24. Continue and verify a Revit/Geopogo model

**Skill name:** `revit-geopogo-continue-verify`

Continue saved Revit work; verify model identity, geometry, warnings, sheets, saves, and packaged files.

#### Compatibility and scope

Read the live connector's tool schemas before executing examples; installed versions can differ. Historic failures describe the recorded session, not every release. The installed create_roof schema inspected for this package automatically selects a floor-plan view and restores the original view; older builds may need an explicit view switch. Check returned state and loaded types. Tool availability and a skill's presence do not prove the workflow has been tested on the recipient's Revit version. Use only the intended model and the user's authorized scope.


#### When to use

Use for an existing Revit model, especially after an interrupted build, a long queued operation, or a targeted refinement. Do not use it to infer a missing design brief or claim historic/reference accuracy from an image.

#### Inputs / context to gather

1. Find the latest saved `.rvt`, prior state files/scripts, and available project handoff notes.
2. Confirm the exact active `.rvt` path and the requested subject before editing. If it is not the intended model, stop; add an exact-path guard to any correction script and confirm that any state file/script belongs to that model.
3. Inspect current project metadata, views, warnings, and relevant element/family types before editing.
4. Identify unfinished queues, deleted temporary geometry, and the user’s exact program or correction request.

#### Procedure

1. Continue the saved model; do not recreate geometry already represented by a state artifact.
2. Before hosted/dependent operations, re-query current element IDs and call `get_family_types`; use exact returned type names.
3. For drawing-sheet work, inspect sheets, placed views, title-block types, and annotation/tag types before adding content. Query exact `Room Tags`/`Door Tags` with `get_element_types`; use `get_title_block_types` rather than an unsupported `get_elements({category:"Title Blocks"})` query. Re-query sheet viewport/readability after placement.
4. For repeated walls/windows/crown details, use bounded `create_walls_batch`, `create_window_array`, or `create_profile_sweep` batches. Persist `queue`/`done` state and idempotent operation keys; if a batch pauses, rerun it and confirm the state marker before saving. Use `create_blend` for tapered spire solids when appropriate.
5. For constrained façade panels, make a backup, remove short connector walls, move the panel, check the actual location curve, recreate connectors with joins disabled, then regenerate affected floor footprints.
6. Do not use `set_wall_profile` on curtain walls or system-family walls that do not support editable profiles. For ports/openings, use `create_wall_opening`, native window families, or separate DirectShape/GenericModel glazing.
7. Before delivery, inspect the changed view/element (both relevant elevations for end-form corrections) and verify semantic identity: active path, requested subject markers/names, expected categories/materials/geometry, and an intended-subject view. For supplied visual references, compare front, side, and three-quarter captures to the reference; technical checks do not establish silhouette fidelity. For custom geometry, independently compare final model bounds to expected dimensions after any unit conversion. Then run `get_model_warnings` and `verify_model`, confirm required room/program counts, save, confirm `isModified:false`, export/inspect requested sheet previews, and verify the actual output path. When packaging an RVT, copy it and compare hashes; if Revit locks the source, hash it through a `FileShare.ReadWrite` FileStream.

#### Efficiency plan

- Read the saved state/artifacts first; they prevent redundant rebuilding.
- Batch repeated geometry, but never treat a success flag as final geometry verification.
- Stop and report partial status if a long queue, restoration, save, view capture, or validation remains unverified.

#### Pitfalls and fixes

- `The referenced object is not valid...` -> stale element ID after a transaction/view change; re-query IDs immediately.
- `ChangeTypeId` argument mismatch on a `FamilyInstance` -> assign `door.Symbol = sym` or use `change_element_type` with the documented family/type identifiers.
- `move_element` succeeds but geometry is unchanged -> connector walls are constraining it; remove/recreate them and compare coordinates.
- A tool response is plugin text, not JSON -> check `r.isError` and content type before parsing.
- `structuredClone` is unavailable in the JavaScript execution environment -> clone tool arguments with `JSON.parse(JSON.stringify(value))`.
- A crown/checkpoint looks plausible but misses the supplied elevation reference -> inspect a dedicated elevation/detail section and revise before delivery.
- `This wall does not have an editable profile. Curtain walls and some system family walls do not support profile editing.` -> do not retry profile edits; pivot to an opening, native window, or separate glazing geometry.
- `Text note type '3/32\" Arial' not found` -> use an exact loaded type reported by Revit (for example, `3/32\" Trebuchet MS`); do not assume Arial is available.
- `Curve length is too small for Revit's tolerance (as identified by Application.ShortCurveTolerance)` while creating a `create_blend` sculpture/solid -> avoid degenerate caps and ensure every profile ring has radius and edge length safely above `Application.ShortCurveTolerance` before retrying.
- `Get-FileHash` cannot read an active RVT -> Revit holds the file; open a FileStream with `FileShare.ReadWrite` for the comparison, and report any remaining warnings separately from drawing-documentation completion.
- The active model is an unrelated live/work project -> abort safely and require the intended path; protect rerunnable scripts with an exact-file guard.
- Passing warnings, level counts, or a hash on an unrelated model -> these validate technical state, not the requested artifact. Re-check `get_model_info.filePath`, state/script ownership, expected subject markers, categories/materials/geometry, and an intended-subject view before packaging.
- A reference-driven model is technically clean but still looks wrong -> compare front, side, and three-quarter captures to the supplied image. For a failed vehicle/organic silhouette assembled from segmented solids, pivot to a continuous smooth shell/mesh or suitable sculpted workflow rather than adding cosmetic pieces.
- The requested artifact conflicts with the active/reference project -> stop and obtain scope confirmation before editing; do not infer that an active vehicle/building is the intended deliverable.
- Custom geometry remains hundreds of feet too large after a millimeter-to-feet correction -> do not apply conversions blindly. Inspect the API's declared-unit behavior, use one conversion strategy, rebuild/clean up as required, then independently check final bounds.
- `The extrusion direction must not be parallel to the plane of the profile loop(s)` -> use a correctly oriented profile/path or replace the attempted sweep with rods where appropriate.

#### Verification checklist

- Latest `.rvt` and continuation state/artifacts inspected.
- Required program counts and changed elements/views checked.
- Long queues completed or explicitly reported as unfinished.
- Active RVT path matched the requested model before edits; rerun state markers completed after any paused batch.
- Active RVT path, state/script ownership, expected subject markers, and an intended-subject view confirmed again before packaging.
- For supplied visual references: front, side, and three-quarter comparison completed; any approximate match explicitly stated.
- For custom geometry or unit conversion: final bounds independently match expected dimensions, or the output is explicitly reported as not true-scale.
- `get_model_warnings` and `verify_model` run after final edits.
- Saved output path confirmed; `isModified:false` confirmed.
- For sheets: viewport/readability rechecked and requested previews exported/inspected.
- For packaged RVTs: source/copy hash comparison completed, or the lock limitation stated.

---

<a id="revit-landmark-towers"></a>

## 25. Landmark towers, setbacks, crowns, and spires

**Skill name:** `revit-landmark-towers`

Model and refine tall reference buildings with level strategies, repeated façades, setbacks, and distinctive crowns.


#### Evidence and scope

Derived from Empire State Building queues and Chrysler crown/spire revisions; early checkpoints and final revision evidence differ.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Create a written massing hierarchy: podium, shaft, setbacks, crown, spire. Distinguish roof height from tip height and choose a level stack that supports the occupied massing.

2. Inspect template levels before adding the tower stack. Reuse or explicitly resolve duplicate levels instead of blindly adding a second base/second floor.

3. Build native walls and slabs for regular floors and use bounded façade/window arrays. Persist queues and counts; verify skipped hosts and actual window placement.

4. Model crown arches, ribs, cap, mast, and finial with appropriate sweeps, blends, or meshes. Keep materials and subject identifiers stable across refinement.

5. Compare a dedicated crown elevation and detail view to the supplied reference before calling the silhouette finished. Enable Mass visibility when a modeled crown seems absent.

6. For wall recess corrections use revit-facade-repair; then restore piers/parapets temporarily removed during repair and finish the outstanding window queue.

#### Failure cases

- A plausible crown is not necessarily the supplied crown. A queue checkpoint or warning-free intermediate state does not prove façade completion.

#### Acceptance checks

- Level strategy; major heights and setbacks; front/side crown profile; completed window queue; restored temporary removals; warnings and final saved output.

#### Source coverage

- Empire State Building massing and window queues (source key: esb).
- Chrysler Building crown and spire (source key: chrysler).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-missions-economy"></a>

## 26. Missions, shops, rewards, and persistent game progress

**Skill name:** `revit-missions-economy`

Add multi-stage objectives, location/mode checks, a game shop, one-time rewards, and durable saves to Revit playable scenes.


#### Evidence and scope

Based on inspected MissionRules.cs, shop behavior notes, and 69 recorded mission rule assertions. Live objective/save-reload checks passed; all missions were not replayed end to end.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Separate pure mission/economy rules from Revit/UI. Define stable mission IDs, ordered steps, objective text, target location, radius, required walking/driving mode, and reward.

2. Represent one active mission with a stage index plus a deduplicated completed set. Normalize corrupt/stale saves: reject invalid mission/stage indices, completed-as-active entries, and non-finite coordinates.

3. Advance only when both mode and spatial conditions match. Award a completion reward once, then clear active state. Prevent duplicate completion, concurrent starts, and cancellation rewards.

4. Expose objective HUD, visible marker, start/cancel actions, and save/reload. Check marker placement against actual reachable surfaces and entrances after geometry changes.

5. For shops, require interaction proximity and appropriate player mode. Validate affordability and duplicate ownership before changing wallet/inventory; persist the purchase consistently. Fictional inventory does not imply a implemented firing mechanic.

6. Test rules outside Revit, then replay every mission route with actual walking/driving transitions, entrances, markers, and reload points. A rule test cannot prove the road or doorway is traversable.

#### Failure cases

- Static access audits and one live stage transition are not all-mission validation. Version launcher, runtime, mission definitions, and saved-state schema together.

#### Acceptance checks

- Invalid-state normalization; duplicate reward/purchase prevention; insufficient funds; cancel/restart; every route end to end; persistence across runtime restart.

#### Source coverage

- Miami street, driving, shop, population and environment (source key: miami).
- Miami missions, rewards and saved progress (source key: missions).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-modeless-runtimes"></a>

## 27. Modeless Revit controllers and runtime lifecycle

**Skill name:** `revit-modeless-runtimes`

Build interactive Revit controllers with ExternalEvent dispatch, scoped input, versioned launchers, and reliable shutdown.


#### Evidence and scope

Synthesized from saved C# controller source and project-specific launcher/verification files. Native add-ins and Dynamo-loaded runtimes have different packaging requirements.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Separate pure simulation state, Revit document access, renderer, UI, and launcher. Select the Revit/.NET target from the actual supported version; these source prototypes mainly targeted Revit 2026/.NET 8.

2. Create ExternalEvent handlers from a valid Revit context. UI timers request work; they do not mutate Document directly from background or WPF callbacks. Coalesce pending updates rather than queuing unbounded frames.

3. Validate the target document and subject before every update. Pause on document/view changes. Handle OpenAndActivateDocument from an appropriate ExternalEvent path; the demolition prototype failed when switching during Idling.

4. Scope keyboard handling to the intended Revit/controller windows and scene views. Clear held keys on focus loss. Keep buttons usable without keyboard capture and release hooks on shutdown.

5. Use a single active controller owner. Close or dispose superseded versions; choose versioned assembly filenames when older DLLs are locked. Expose runtime version, model identity, timing, frame count, and error state.

6. On close/reset, stop timers/audio, release subscriptions/hooks, restore temporary display, and persist only intended state. A fixed-action local mailbox may aid testing; do not make it an arbitrary code execution channel.

#### Failure cases

- Opening a view does not open a controller. Dispatcher interval is not achieved FPS. A compiled DLL or successful Dynamo Run is not proof of live control.

#### Acceptance checks

- Launch visible panel; real key/button interaction; correct target; movement/time progress; pause/focus loss; reset; close and reopen; no duplicate controller.

#### Source coverage

- Peach Castle, Mario, chase camera, gait and music (source key: mario).
- Fremont Optimus modeling and production animation (source key: factory).
- Optimus controller responsiveness (source key: responsive).
- Miami street, driving, shop, population and environment (source key: miami).
- In-Revit demolition and BEPU rigid-body cache (source key: demolition).
- Flyable airspeeder and walker battle (source key: battle).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-monuments-sculpture"></a>

## 28. Monuments, arches, and sculptural details

**Skill name:** `revit-monuments-sculpture`

Create monumental architecture and refine statues or ornaments with silhouette-driven custom geometry and robust profile tolerances.


#### Evidence and scope

Based on the Trump Arch exterior/interior, material pass, and partial lion/statue refinement scripts.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Separate primary architectural massing, arch voids, columns/entablatures, inscriptions, and sculptural groups. Derive proportions from the supplied views and label inferred dimensions.

2. Build architecture and major sculpture silhouettes first. Use front, side, and close detail views to judge posture, anatomy cues, and negative space before fine ornament.

3. Use sweeps, lofts, blends, or meshes according to form. Avoid tiny closing rings or collapsed profile edges that violate Revit short-curve tolerance.

4. Keep sculpture parts and materials independently named; preserve stable IDs where possible during revision. Do not hide a poor silhouette behind extra surface details.

5. For an export view, verify Mass/Generic Model visibility and the entire sculpture body. Route material transfer work through revit-unreal-materials.

6. Save iterative comparison views and state whether statue refinement is complete, approximate, or still unresolved.

#### Failure cases

- A technically valid lion face or statue mesh is not evidence that all sculptural groups were finished. Skipped tiny profiles can leave missing anatomy.

#### Acceptance checks

- Arch clear opening; full monument silhouette; side and close sculpture inspection; valid profiles; export-category visibility; warnings/save.

#### Source coverage

- Monumental arch and sculpture refinement (source key: monument).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-native-house-refinement"></a>

## 29. Native houses and functional interior refinement

**Skill name:** `revit-native-house-refinement`

Create or refine native residential layouts with exact room programs, usable openings, furniture clearances, and coherent roofs.


#### Evidence and scope

Based on Stone and Cedar House, Fallingwater-inspired modeling, saved kitchen/entrance/garage corrections, and a measured small-room build.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Translate the brief into required enclosed rooms and circulation, then inspect levels and loaded wall/floor/door/window types. Preserve the saved layout during continuation.

2. Create the envelope, partitions, floors, openings, and roof using current schemas and exact returned types. Use create-roof-workflow for version-dependent roof view handling.

3. Validate the entrance path and door swings before placing furniture. In a kitchen, preserve access to laundry/storage doors; verify clearances from geometry rather than room labels.

4. Place fixtures against the intended wall with correct orientation and room-side clearance. Treat the source request to align toilets to walls as a layout correction, not evidence of code compliance.

5. For garage/open-door revisions, query the actual family and supported parameters. On a FamilyInstance use the appropriate symbol/type operation rather than assuming every ChangeTypeId overload accepts the same arguments.

6. Create arrival, garden, interior, cutaway, plan, and roof views as needed. Check room enclosure and exact bedroom/bathroom counts after the final change.

#### Failure cases

- Re-query host IDs after transactions. A changed garage symbol is not proof the door is visibly open. Glazing or furniture should not obstruct doors or circulation.

#### Acceptance checks

- Program counts, room areas, door access, fixture orientation, host/type readback, changed views, warnings, saved model.

#### Source coverage

- Stone and Cedar House and interior corrections (source key: house).
- Fallingwater reference study (source key: fallingwater).
- Nautilus organic house and railing revisions (source key: organic).
- Compact podcast studio and corridor (source key: podcast).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-needs-autonomy"></a>

## 30. Needs-driven people and environment use

**Skill name:** `revit-needs-autonomy`

Create Sims-style agents that choose activities, reserve resources, navigate obstacles, animate use, and persist progress.


#### Evidence and scope

Derived from the saved Revit-independent autonomy_engine.py and its Dynamo adapter. The older autonomy summary did not verify final live execution; treat the extracted workflow as a prototype needing live acceptance tests.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Keep simulation rules independent of Revit: needs, decay rates, activities, resource IDs, approach points, durations, person state, and deterministic clock.

2. Model idle, walking, using, waiting, and recovery states. Choose reachable activities by current needs; reserve shared resources before travel and release reservations on completion, cancellation, or failure.

3. Build obstacle-inflated navigation from the actual furniture layout. A grid A* route must prevent diagonal corner cutting; shortcut a route only after checking the complete segment.

4. Use bounded fixed substeps for slow Dynamo updates. Track waiting time, retry unreachable activities with cooldowns, and release stale reservations so two agents cannot deadlock a bathroom forever.

5. Drive Revit positions/poses from the simulation state using stable person IDs. An agent’s use animation should correspond to reaching the object, not merely selecting its task.

6. Persist needs, tasks, routes, reservations, progress, and version. Normalize stale resources after a layout change and latch RESET so it does not wipe every frame.

#### Failure cases

- Authored looping routes in the earlier Sims animation are not the same as needs-based autonomy. Compiled Python alone does not prove agents reach/use furniture in Revit.

#### Acceptance checks

- Each activity reached and completed; exclusivity of shared resources; blocked-path recovery; no obstacle cuts; deterministic pause/reset; live poses and persisted reload verified.

#### Source coverage

- Sims house, people, needs and navigation (source key: sims).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-organic-shells"></a>

## 31. Organic architecture, curved glass, and continuous shells

**Skill name:** `revit-organic-shells`

Build expressive curving Revit concepts with coordinated native interiors, smooth custom shells, glazing, and railings.


#### Evidence and scope

Derived from Nautilus House revisions and Heydar Aliyev-inspired custom-shell scripts. These are conceptual geometric studies, not engineered structures.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Establish plan organization and floor elevations with native floors, partitions, doors, and stairs where those functions matter. Keep the expressive envelope separately named and editable.

2. Parameterize the shell with sampled curves and matched loft sections; control profile winding, sample density, edge tolerance, and overlaps. Use a continuous surface strategy where segmented solids create a visibly faceted result.

3. Generate curved glazing from the same controlling curves with intentional offsets and frame tolerances. Check inner/outer shell intersections and a usable interior cavity.

4. Coordinate canopy ribbons, supports, timber soffits, terraces, pools, and furniture with the main shell. Remove a floating accent when the user rejects it rather than adding detail around it.

5. For curved balcony guards, derive top/bottom rails and panels from the slab edge and maintain continuous height and joint alignment. Inspect transitions at ends and adjacent ribbons.

6. Review shaded surfaces without edges for form and linework/sections for seams and construction conflicts. Keep native floor sketches axis-consistent and verify modified floor footprints.

#### Failure cases

- Closely spaced lofts are not one native parametric roof. Transparency does not create a hollow shell. Floating forms and glass fabrication remain design proposals unless engineered.

#### Acceptance checks

- Front, both sides, three-quarter and interior sections; glazing/shell intersections; native sketch warnings; guard continuity; scoped dimensions and save/hash checks.

#### Source coverage

- Nautilus organic house and railing revisions (source key: organic).
- Heydar Aliyev inspired organic architecture (source key: zaha).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-pedestrians-traffic"></a>

## 32. Pedestrian and traffic autonomy

**Skill name:** `revit-pedestrians-traffic`

Animate distributed pedestrians and cars on maintained road/sidewalk routes with independent toggles and player-aware ownership.


#### Evidence and scope

Derived from Miami V14-V19 route revisions and motion audits; source reports cover 12 cars and 26 outdoor pedestrians across the expanded scene.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Build a route graph from current road/sidewalk boundaries. Expand routes when the city grows rather than keeping all actors on the original boulevard.

2. Distribute existing actors deliberately before adding more. Assign lanes/directions to narrow shared cross streets and test rounded turnaround loops.

3. Sample full routes densely enough to detect off-road segments; the source used half-foot samples. Include vehicle footprint and pedestrian clearance rather than validating only route center points.

4. Separate player-controlled vehicles from automatic traffic. Yield or stop for other cars, the player, and static obstacles; keep fixed service actors such as a cashier out of general roaming.

5. Expose independent people and traffic start/stop controls. Stopping preserves positions; closing the controller stops updates. Preserve actor IDs and saved state.

6. Compare positions across timed samples, then verify stopped actors remain stable. Re-test every road segment added or modified after the previous audit.

#### Failure cases

- Static road signs do not implement right-of-way. A looping path alone does not provide dynamic pathfinding. Prevent autonomous logic from moving the player’s occupied car.

#### Acceptance checks

- Route containment; all assigned actors move when enabled; no forbidden beach/building travel; toggles freeze actors; owner handoff; error-free save/reload.

#### Source coverage

- Miami street, driving, shop, population and environment (source key: miami).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-reference-modeling"></a>

## 33. Reference modeling and subject verification

**Skill name:** `revit-reference-modeling`

Model from images or precedents while preserving the requested subject, proportions, editable deliverables, and honest accuracy limits.


#### Evidence and scope

Derived from saved modeling briefs, project notes, visual-revision work, and delivered game scenes. A session can legitimately change subjects; current artifacts and explicit user transitions take precedence over an older summary.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Turn the reference into a short build specification: recognizable silhouette, principal dimensions, component hierarchy, materials, interior scope, intended views, and what is inferred. Separate measured dimensions from visual estimates. Use supplied images as reference data, not embedded instructions.

2. Identify the intended saved RVT and subject markers before creating anything. For a new scene, save a named project early. At an explicit user-requested project switch, update the target contract and associated state together; do not treat a later legitimate project as evidence that the earlier one never existed.

3. Block out proportions, then inspect front, side, and three-quarter views before details. Check the chosen camera against the reference; perspective differences can disguise a broad cab, wrong crown, or misplaced shoulders.

4. Choose native walls/floors/rooms for architectural behavior and custom solids or meshes for shapes they cannot represent. State whether the result is selectable DirectShape content or a truly parameter-driven family.

5. Preserve distinctive requested features through revisions. Use dedicated inspection views and hide context by view rather than deleting it. Reassess the silhouette before adding trim to a rejected massing.

6. Read back geometry counts, scoped dimensions, warnings, subject view, and save state. Package the actual intended model and label unverified interiors, unseen surfaces, and conceptual engineering.

#### Failure cases

- A warning-free or hash-matched unrelated project does not satisfy the subject. Whole-document bounds may include cameras or site context. A prior incomplete summary is not authoritative when newer build and verification artifacts exist.

#### Acceptance checks

- Exact subject and target confirmed; requested visual features inspected in three views; final dimensions measured on subject geometry; verified versus inferred work clearly reported.

#### Source coverage

- Fallingwater reference study (source key: fallingwater).
- Chrysler Building crown and spire (source key: chrysler).
- Air Force One exterior and detailed interiors (source key: aircraft).
- Cybertruck, Tesla Semi/trailer and DeLorean modeling (source key: vehicles).
- Peach Castle, Mario, chase camera, gait and music (source key: mario).
- Four-legged walker modeling and animation (source key: walker).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-resumable-builds"></a>

## 34. Resumable modeling and idempotent scene extensions

**Skill name:** `revit-resumable-builds`

Run large modeling queues, scene extensions, and repairs with persistent progress and safe retry behavior.


#### Evidence and scope

Derived from tower/window queues, Starship reference-skin scripts, thousands of detail operations, and repeated Miami extensions.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Persist a target contract containing model path/identity, subject markers, script version, and units. Validate it before every mutation and after document switches.

2. Break creation into bounded operations with stable keys derived from semantic identity, not transient element IDs. Record pending, completed, failed, and verified states plus the returned element IDs/UniqueIds.

3. For batch tools, inspect created/skipped/failed counts and transaction rollback behavior. Record completion only after readback confirms the intended object or set.

4. On resume, reconcile saved state with the live model: some committed geometry may exist even when a process stopped before its log write. Query ownership markers and either adopt the verified result or rebuild only the affected stage.

5. Use per-feature scene revision markers for extensions such as beaches, storefronts, intersections, and infill. A rerun should skip an already completed revision rather than duplicate it.

6. Before deleting replacement targets, preserve a backup and validate the replacement geometry. Finish or explicitly report all incomplete queues, temporarily deleted geometry, and deferred save operations.

#### Failure cases

- A successfully rerun script is not proof its final stage completed. Never reuse another project’s queue merely because element IDs look plausible.

#### Acceptance checks

- Interrupt/resume one representative batch; rerun without duplicates; reconcile recorded IDs; verify final counts, subject views, warnings, and save state.

#### Source coverage

- Empire State Building massing and window queues (source key: esb).
- Starship, launch base, tower and catch arms (source key: starship).
- Paris blocks, storefronts, roofs and street detail (source key: city).
- Miami street, driving, shop, population and environment (source key: miami).
- Data-center concept and equipment detailing (source key: data-center).
- Four-legged walker modeling and animation (source key: walker).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-rocket-launch-site"></a>

## 35. Rocket, launch tower, and catch-arm reference modeling

**Skill name:** `revit-rocket-launch-site`

Create and refine rocket stages, launch infrastructure, catch arms, external details, and reference-specific skins.


#### Evidence and scope

Based on StarBase/Starship complex scripts and the recorded reference-skin correction, with exact-target guards and resumable batches.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Separate the vehicle from the tower/base/catch-arm assemblies. Define stage axes, body diameters, overall heights, ground datum, and major clearances.

2. Block out bodies and support structures, then compare the vehicle outline to the reference. Preserve unrelated launch infrastructure when the user requests only a rocket correction.

3. Detail reference-specific nose/shoulder patches, large flaps, backing lattice, external raceways, ribbed bands, and ports as independently named parts.

4. Use actual tool-unit declarations and profile tolerances for cylindrical, tapered, and swept geometry. Measure the vehicle separately from the site and cameras.

5. Persist state and idempotent operation keys for dense skin/detail batches. Resume a paused batch and confirm its completion marker before saving.

6. Capture front/side/three-quarter vehicle views and a tower/base overview. Do not substitute generic cylinders and fins for explicitly requested distinctive geometry.

#### Failure cases

- Project-path mismatch must stop the script. A valid component count is not reference fidelity or aerospace engineering verification.

#### Acceptance checks

- Stage proportions; four-sided flap placement where requested; distinctive skin features; site clearance; complete queue; intended vehicle view; warnings/save.

#### Source coverage

- Starship, launch base, tower and catch arms (source key: starship).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-runtime-delivery"></a>

## 36. Portable delivery of interactive Revit projects

**Skill name:** `revit-runtime-delivery`

Package Revit games, Dynamo launchers, add-ins, assets, state, and source so another user can install and reopen the correct scene.


#### Evidence and scope

Synthesized from delivered prototypes that used both absolute-path Dynamo launchers and relative-root native add-ins. Many original packages required path updates; portability must be tested independently.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Choose the delivery type: static RVT only, RVT plus Dynamo/source, Dynamo-loaded runtime, or native add-in. State exactly which companion files are required; the RVT does not embed executable controls.

2. Build a manifest with supported Revit/.NET version, launch entrypoint, active runtime version, model identity, required assets/dependencies, and save-state location. Avoid shipping superseded DLLs as ambiguous launch targets.

3. Resolve package paths from the installed assembly/launcher directory or an explicit selected root. Convert absolute developer paths in graphs/source/config to a recipient-selected configuration; retain an exact target or validated scene identity guard.

4. Keep immutable program/assets separate from writable state. Do not ship the author’s player progress as the only reset state. Normalize/migrate state versions and provide a clean-start option.

5. For native add-ins, register only the intended per-user manifest for the recipient Revit version and provide removal instructions. Preserve unrelated manifests and handle DLL locks by versioning/restart rather than deleting active files.

6. Test extraction to a different path, including spaces/non-ASCII names, then launch, interact, pause, reset, save/reload, and close. Include source/build instructions and dependency licenses; distribute only authorized media.

#### Failure cases

- A byte-matching RVT does not validate runtime portability. Removing the target guard to make relocation easier is unsafe; regenerate the target contract instead.

#### Acceptance checks

- Clean-machine/path installation; correct runtime/scene; dependency/assets present; mutable state writable; all launch paths portable; reset/reopen; hashes and scoped uninstall.

#### Source coverage

- Peach Castle, Mario, chase camera, gait and music (source key: mario).
- DeLorean highway driving game (source key: highway).
- Miami street, driving, shop, population and environment (source key: miami).
- Miami missions, rewards and saved progress (source key: missions).
- In-Revit demolition and BEPU rigid-body cache (source key: demolition).
- Four-legged walker modeling and animation (source key: walker).
- Flyable airspeeder and walker battle (source key: battle).
- Optimus model-linked dashboard (source key: dashboard).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-ships"></a>

## 37. Ship hulls, decks, and conceptual interiors

**Skill name:** `revit-ships`

Build or continue ship reference models with hull form, deck stacks, repeated openings, lifeboats, and bounded interior scope.


#### Evidence and scope

Derived from Titanic hull/interior scripts and bow/stern correction. Recorded warning cleanup remained partial in the continuation notes.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Set length, beam, waterline, deck elevations, and a longitudinal datum. Create hull stations or controlled profiles so bow/stern form can be revised without disturbing all interiors.

2. Build a recognizable hull and superstructure before railings, funnels, masts, rigging, portholes, and lifeboats. Track repetitive pieces with stable operation keys.

3. Separate documented layout anchors from inferred machinery, bulkheads, rooms, and furnishings. Use native room-bounding elements only where their BIM behavior is needed.

4. For openings, use supported wall openings or native windows. Curtain/system walls that reject profile edits need an alternative; repeated set_wall_profile attempts will not fix that limitation.

5. Inspect both port and starboard elevations after bow/stern changes. Check deck boundaries and floor-axis corrections where hull geometry changes.

6. Audit stairs and warnings by type. A desired/actual riser-count correction resolved some historical warnings, but re-query all remaining issues rather than assuming full cleanup.

#### Failure cases

- The original study was not a certified historic or marine-engineering model. A successful end-form correction can coexist with unresolved model warnings.

#### Acceptance checks

- Length/beam measured on the ship; deck and lifeboat counts; both ends and sides inspected; openings valid; remaining warnings enumerated; state and saved RVT reconciled.

#### Source coverage

- Titanic hull, interior, bow and stern (source key: titanic).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-sites-landscape"></a>

## 38. Terrain, highways, factory sites, and landscape context

**Skill name:** `revit-sites-landscape`

Build site context, terrain, roads, parking, planting, shorelines, and large repeated exterior assets around a Revit subject.


#### Evidence and scope

Derived from truck highways/terrain, Fremont aerial-reference refinement, and Miami beach/perimeter work.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Establish a local coordinate frame and separate subject bounds from the much larger context. For an aerial reference, label alignment, elevations, and unseen site geometry as estimates unless survey/GIS data is actually used.

2. Define road surfaces, shoulders, median, guardrails, connectors, parking stalls, service yards, and pedestrian routes before placing vehicles or furniture.

3. Use shared geometry for repeated trees, cars, trailers, lamps, and roof equipment. Record whether counts refer to individual Revit elements or instances represented inside grouped custom geometry.

4. For terrain and shoreline, coordinate ground, water, sand, curbs, and boardwalk elevations. Resolve coplanar flicker with intentional small offsets and check the finished view.

5. Extend perimeter walls only along intended land edges; keep requested beach/ocean openings. Synchronize collision limits with the revised playable land extent.

6. Preserve the existing interior/animation model when refining exterior context. Revalidate its runtime separately if claiming the delivery includes functioning interaction.

#### Failure cases

- A high tree/car count does not establish geographic accuracy. Large repeated scenes can overwhelm per-element regeneration; use appropriate grouping and scoped views.

#### Acceptance checks

- Site-only bounds; terrain/road interfaces; no surface flicker; planting/parking clearances; context retained without breaking playable routes; warnings/save.

#### Source coverage

- Cybertruck, Tesla Semi/trailer and DeLorean modeling (source key: vehicles).
- Fremont highway, parking, yard and landscape (source key: factory-site).
- Miami street, driving, shop, population and environment (source key: miami).
- Golden Gate suspension bridge and tower revisions (source key: golden-gate).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-theme-park-rides"></a>

## 39. Theme-park rides and coordinated scene animation

**Skill name:** `revit-theme-park-rides`

Build and animate custom Revit rides, trains, gondolas, carousels, drop towers, and visitors with stable object identities.


#### Evidence and scope

Based on the saved Wonderland park source, graph, and playback continuation evidence. Visitor paths and riders were authored, not autonomous queues or ride boarding.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Separate static scenery, track/supports, moving assemblies, riders, and visitor routes. Define local pivots and route parameters for each ride before generating detail.

2. Move coaster train cars along the same track parameterization with consistent spacing and orientation. Keep riders parented to their vehicle transforms.

3. For a Ferris wheel, rotate the wheel while counter-rotating gondolas to stay upright. For carousels, combine rotation with local horse motion; for drop towers, bound carriage travel.

4. Update existing element IDs rather than spawning a new scene each frame. Group repeated custom meshes and limit expensive shape regeneration.

5. Use one Dynamo animation owner with PLAY/manual time/speed and a bounded timestep. Tune the periodic interval against actual Revit responsiveness; faster simulation need not mean more frequent document writes.

6. Inspect each ride separately plus a whole-park view. State whether visitors only follow paths or actually queue, board, purchase, and avoid collisions.

#### Failure cases

- A ride-shaped mesh and looping motion are not ride engineering. Park-only bounds differ from whole-document extents containing cameras/template objects.

#### Acceptance checks

- Each ride visibly moves; gondolas remain upright; cars stay on track; riders follow; IDs stable; pause/manual pose; timed telemetry; save/reload.

#### Source coverage

- Wonderland theme-park rides and playback (source key: park).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-unreal-materials"></a>

## 40. Revit to Unreal material handoff

**Skill name:** `revit-unreal-materials`

Prepare named Revit material assignments and a separate Unreal PBR handoff while preserving export and validation limits.


#### Evidence and scope

Derived from the arch material package and its local Unreal tests. Actual Datasmith import and final appearance were not verified in those notes.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Inventory material assignments and the export view’s visible categories. Distinguish Revit graphics color/transparency from render appearance assets; do not claim the latter changed when the connector only edits graphics properties.

2. Give transferable materials stable names. Package BaseColor, ORM, and normal maps with a mapping file; document scale and channel conventions. The source used ORM R=AO, G=roughness, B=metallic.

3. Treat BaseColor as sRGB and data maps as linear. Match normal-map handedness and the receiving shader’s expected encoding instead of assuming any RGB image is a tangent-space normal.

4. For custom shapes without UVs, a world-space/triplanar strategy may suit static architecture. Note that world-anchored textures can shift relative to moving objects.

5. Create or reuse receiving material assets without overwriting user edits. Apply overrides only to explicitly selected imported actors/children and matching material names; preserve unrelated assets.

6. Test actual export/import, name matching, assignment counts, appearance, and reimport behavior on the recipient engine/exporter versions. Source-library creation is a separate milestone from a successful Datasmith scene transfer.

#### Failure cases

- Newer Unreal binary assets may not load in older versions. A headless assignment test does not verify UI selection or final rendered appearance.

#### Acceptance checks

- Mapping completeness; correct texture channels/scale; intended actors only; real import and reimport inspection; explicit untested stages.

#### Source coverage

- Unreal material transfer and PBR library (source key: unreal).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-urban-streets"></a>

## 41. Urban blocks, storefronts, intersections, and street detail

**Skill name:** `revit-urban-streets`

Extend city scenes with coordinated buildings, sidewalks, curved corners, storefronts, and playable street connections.


#### Evidence and scope

Based on Paris R3-R9 and Miami intersection/infill revisions. These city scenes were conceptual rather than surveyed geographic reconstructions.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Define street centerlines, block footprints, sidewalk edges, elevation bands, and the intended extent before expanding. For a geographically accurate brief, obtain actual footprints/control points rather than repeating invented blocks.

2. Generate building bays and courtyard blocks with controlled variation. Keep roof adjacency coherent; revise adjoining roof profiles and seams together.

3. Inset storefront glazing inside structural bays. Allocate separate ranges for doors, windows, mullions, sills, signs, and awnings so details do not intersect; vary dimensions within constraints rather than arbitrary random overlap.

4. Create curved curb corners and trim sidewalk slabs at intersections. Coordinate zebra crossings, stop bars, ramps, warnings pads, gutter lines, and road markings around the new opening.

5. Place lamps, benches, bollards, bins, cycle stands, drainage details, signs, and planting with walking clearance. Reuse geometric definitions without implying every visual object is a native family.

6. For playable infill, update collision footprints, enterable openings, camera zones, and route graphs alongside geometry. Re-run entrance and vehicle connectivity audits after each extension.

#### Failure cases

- Visual stop signs are not traffic-control logic. Added city geometry may make old route and intro-video reports stale. Roof or sidewalk repairs should not leave hidden duplicate surfaces.

#### Acceptance checks

- No glazing/awning overlap; corner and crossing continuity; roof seams; clear entrances; road containment; named revision marker; scoped extent and saved views.

#### Source coverage

- Paris blocks, storefronts, roofs and street detail (source key: city).
- Miami street, driving, shop, population and environment (source key: miami).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-vehicle-modeling"></a>

## 42. Vehicle exteriors, interiors, and reference refinement

**Skill name:** `revit-vehicle-modeling`

Create or refine cars, trucks, trailers, and detailed cabins while preserving smooth proportions and usable interior volume.


#### Evidence and scope

Based on Cybertruck, Tesla Semi/trailer, DeLorean geometry, and the later measured DeLorean driving copy. Visual accuracy varied across revisions.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Use a centerline, wheelbase, axle positions, body width, height, and overhang anchors. Decide which dimensions are known and which are visual estimates.

2. Prioritize front/side/three-quarter silhouette: windshield rake, roof width, hood continuity, shoulder shape, wheel placement, and nose curvature. Pivot to continuous shells/meshes when stacked segmented solids cannot match the reference.

3. Build hollow or thin cabin skins and separate glazing. Set transparency in an inspected shaded view, then check that inner liners, firewall, or door panels are not hiding the cabin.

4. Furnish seats, dashboard, steering, consoles, pedals, door trims, controls, and storage to fit the actual cavity. Keep model-specific features separate from generic vehicle parts.

5. Preserve trailer and highway context during cab-only refinements; use filters and dedicated study views to inspect the revised subject.

6. For driving use, retain the original editable component group and create a simpler rendering/motion representation with material mapping. Measure the simplified vehicle and document what was reduced.

#### Failure cases

- A rejected slender-cab revision is not made accurate by zero warnings. Unit errors must be diagnosed from scoped geometry, not an unrelated document bounding box.

#### Acceptance checks

- Silhouette comparisons; measured vehicle-only dimensions; cabin clearance; glazing visibility; original source preserved; motion copy materials and bounds checked.

#### Source coverage

- Cybertruck, Tesla Semi/trailer and DeLorean modeling (source key: vehicles).
- DeLorean highway driving game (source key: highway).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="revit-working-drawings"></a>

## 43. Working drawings, schedules, tags, and sheet delivery

**Skill name:** `revit-working-drawings`

Continue or create Revit sheet sets with readable views, dimensions, tags, schedules, notes, and verified saved deliverables.


#### Evidence and scope

Derived from data-center A101/A102/A201/A301 work, aircraft cutaways and furniture plans, and organic-house concept sheets.

This is reusable guidance extracted from saved work, not a fresh live Revit certification. Adapt project dimensions, paths, IDs, assets, and API signatures to the recipient's scene. Keep the user's requested subject and scope.

#### Workflow

1. Inspect existing sheets, placed views, title-block types, annotation types, schedules, and intended deliverable scope. Continue existing numbering and layout rather than duplicating sheets.

2. Create the required plans, elevations, sections, and enlarged views before placing them. Choose scale and crop regions for the actual sheet size and content density.

3. Query exact Room Tags, Door Tags, text types, and title-block types. Use the dedicated title-block query if generic category queries do not support it.

4. Add dimension chains, section/elevation references, room/door tags, legends, schedules, notes, and meaningful viewport titles. Re-query after placements to catch collisions and unreadable content.

5. Export requested preview sheets at a useful resolution and inspect them. A successful export call is not evidence that annotations are legible or the viewports fit.

6. Run model checks after final annotation edits, save, confirm isModified:false, and verify the copied RVT hash. Report remaining model warnings and undelivered sheets separately from the completed documentation scope.

#### Failure cases

- Missing Arial or a tag type requires using a loaded type, not repeated failed calls. Four completed sheets are not a complete construction set. Locked RVTs may need a shared-read hash stream.

#### Acceptance checks

- Sheet/view identity; readable scales and tags; viewport overlap; schedule values; exported preview inspection; save and copy integrity; unresolved warnings stated.

#### Source coverage

- Data-center sheet setup and continuation (source key: drawings).
- Air Force One exterior and detailed interiors (source key: aircraft).
- Nautilus organic house and railing revisions (source key: organic).

Use the relevant companion skill through get_skill when needed; discover the recipient connector schemas before tool calls. The extracted package's SOURCE-COVERAGE.md and source-evidence.json record coverage and source fingerprints without embedding private chat logs.

---

<a id="structural-grid-workflow"></a>

## 44. Structural Grid Workflow

**Skill name:** `structural-grid-workflow`

Create named structural grids and place columns at their intersections.

#### Compatibility and scope

Read the live connector's tool schemas before executing examples; installed versions can differ. Historic failures describe the recorded session, not every release. The installed create_roof schema inspected for this package automatically selects a floor-plan view and restores the original view; older builds may need an explicit view switch. Check returned state and loaded types. Tool availability and a skill's presence do not prove the workflow has been tested on the recipient's Revit version. Use only the intended model and the user's authorized scope.


Step-by-step guide for creating a structural grid with columns at intersections using Geopogo AI tools.

#### Overview

A structural grid in Revit consists of:
1. **Grid lines** — named reference lines (A, B, C... or 1, 2, 3...)
2. **Structural columns** — placed at grid intersections, on every level

#### Recommended Sequence

##### Step 1 — Check existing levels
```
get_levels
```
Note all level names and elevations. Columns will be placed from the base level to the top.

##### Step 2 — Create grid lines

Create X-direction grids (numbers) first, then Y-direction grids (letters).

```
create_grid  { "name": "1", "startX": 0, "startY": 0, "endX": 0, "endY": 60 }
create_grid  { "name": "2", "startX": 20, "startY": 0, "endX": 20, "endY": 60 }
create_grid  { "name": "3", "startX": 40, "startY": 0, "endX": 40, "endY": 60 }

create_grid  { "name": "A", "startX": 0, "startY": 0, "endX": 40, "endY": 0 }
create_grid  { "name": "B", "startX": 0, "startY": 30, "endX": 40, "endY": 30 }
create_grid  { "name": "C", "startX": 0, "startY": 60, "endX": 40, "endY": 60 }
```

All coordinates are in **feet**.

##### Step 3 — Get column family types
```
get_family_types  { "category": "Structural Columns" }
```
Pick a type — e.g. `"W-Wide Flange: W10x49"` for steel, `"Concrete-Round-Column: 24\""` for concrete.

##### Step 4 — Place columns at every intersection

Place a column at each grid intersection. Repeat for each (X-grid, Y-grid) pair.

```
create_column  {
  "familyTypeName": "W-Wide Flange: W10x49",
  "x": 0, "y": 0,
  "levelName": "Level 1",
  "topLevelName": "Level 3"
}
```

For a 3×3 grid (grids 1,2,3 × A,B,C) that's 9 columns total.

#### Tips

- **Bay spacing**: 20–30 ft is typical for office buildings. 15–25 ft for residential.
- **Column height**: set `levelName` to the lowest occupied level and `topLevelName` to the roof level.
- **Batch columns**: call `create_column` for all intersections before moving on — Revit processes them faster in sequence than interleaved with other operations.
- **Naming**: grids should be consistently named; Revit will reject duplicate grid names.

#### Example Layout

3-bay × 2-bay grid, 20 ft bays, columns at all 12 intersections:

```
Grids 1–4 (X-dir, spaced 20 ft apart): x = 0, 20, 40, 60
Grids A–C (Y-dir, spaced 20 ft apart): y = 0, 20, 40

Columns: (0,0), (20,0), (40,0), (60,0),
          (0,20), (20,20), (40,20), (60,20),
          (0,40), (20,40), (40,40), (60,40)
```

---

<a id="source-coverage"></a>

## Appendix: Source coverage

### Source coverage

Snapshot: 2026-09-30. Indexed 41 prior local chats and 29 project folders containing saved artifacts. Source documents, selected implementation files, and validation reports were used to synthesize the workflows. 35 source sets are mapped below; some share a project folder because one chat contained several explicitly requested projects. Original installed workflows remain in the package.

This accounts for all Revit project themes found in the available local history, including July connection attempts and September modeling/game work. It cannot cover unavailable or deleted conversations. Raw chats, private memory, personal paths, client imagery, commercial audio, original RVTs, and original project-specific DLLs are not redistributed here. The product is the reusable skill library, not copies of every game/project.

Older summaries sometimes treated a later requested project switch as a failure of the preceding request. Saved Mario, aircraft, Cybertruck, DeLorean and organic-house deliverables were found and inspected for this expansion; the library records each project separately. No old summary's completion claim is accepted as a fresh live test.

| Source project/work | Skills carrying the workflow | Evidence limits |
|---|---|---|
| Geopogo connection and host availability | `geopogo-connection-diagnostics` | Connection diagnostics; no model restoration inferred from configuration alone. |
| Empire State Building massing and window queues | `revit-resumable-builds`, `revit-landmark-towers` | Queue and source-state evidence; unfinished stages must be reconciled. |
| Empire State Building facade correction | `revit-facade-repair` | Saved revised RVT and historical verified correction; no new geometry audit here. |
| Fallingwater reference study | `revit-reference-modeling`, `revit-native-house-refinement` | Modeling specification present; incomplete features remain bounded. |
| Stone and Cedar House and interior corrections | `revit-native-house-refinement`, `revit-furniture-interiors` | Saved native model, build and entrance/kitchen/fixture/garage correction scripts. |
| Chrysler Building crown and spire | `revit-reference-modeling`, `revit-landmark-towers` | Saved modeling/revision notes and model; crown refinement included. |
| Gordie Howe inspired cable-stayed bridge | `revit-bridges` | Reference-based concept with documented design assumptions. |
| Golden Gate suspension bridge and tower revisions | `revit-bridges`, `revit-sites-landscape` | Documented dimensions, tower corrections, saved model; not engineering certification. |
| Titanic hull, interior, bow and stern | `revit-ships` | Saved scripts and notes; warning cleanup was not fully complete in recorded continuation. |
| Starship, launch base, tower and catch arms | `revit-resumable-builds`, `revit-rocket-launch-site` | Reference detail scripts and saved StarBase model; exact-model guards retained as workflow. |
| Air Force One exterior and detailed interiors | `revit-reference-modeling`, `revit-geometry-units`, `revit-aircraft-interiors`, `revit-working-drawings` | Delivered aircraft and interior artifacts exist; a later requested project switch was distinct. |
| Heydar Aliyev inspired organic architecture | `revit-organic-shells` | Custom-shell modeling and documentation scripts recovered; not newly visually verified. |
| Data-center concept and equipment detailing | `revit-resumable-builds`, `revit-data-centers-mep` | Seven recorded plumbing warnings and connection limits retained. |
| Data-center sheet setup and continuation | `revit-working-drawings` | Recorded four-sheet continuation scope; not a full construction set. |
| Walnut desk and accessories | `revit-furniture-interiors` | Selectable custom geometry; not a fully parametric furniture family. |
| Cybertruck, Tesla Semi/trailer and DeLorean modeling | `revit-reference-modeling`, `revit-geometry-units`, `revit-vehicle-modeling`, `revit-sites-landscape` | Modeling and refinement recovered; visual limitations and scoped-unit checks preserved. |
| Paris blocks, storefronts, roofs and street detail | `revit-resumable-builds`, `revit-facade-repair`, `revit-urban-streets` | Conceptual city, not georeferenced; revisions include curved corners and overlap cleanup. |
| Monumental arch and sculpture refinement | `revit-geometry-units`, `revit-monuments-sculpture` | Statue refinement partial; preserve profile-tolerance and visual checks. |
| Unreal material transfer and PBR library | `revit-unreal-materials` | Material creation/assignment tests recorded; actual Datasmith arch import not verified. |
| Nautilus organic house and railing revisions | `revit-geometry-units`, `revit-native-house-refinement`, `revit-organic-shells`, `revit-working-drawings` | Native interior/custom-shell workflow; apparent floating forms not engineered. |
| Sims house, people, needs and navigation | `revit-dynamo-animation`, `revit-needs-autonomy` | Direct animation and advanced autonomy are distinct stages; final autonomy live acceptance not established here. |
| Wonderland theme-park rides and playback | `revit-dynamo-animation`, `revit-theme-park-rides` | Saved scene and timed playback evidence; visitors do not dynamically board or queue. |
| Peach Castle, Mario, chase camera, gait and music | `revit-reference-modeling`, `revit-modeless-runtimes`, `revit-dynamo-animation`, `revit-character-controls`, `revit-articulated-animation`, `revit-day-night-audio`, `revit-runtime-delivery` | Delivered scene, controller source and walking verification recovered; game interiors/jump physics not claimed. |
| DeLorean highway driving game | `revit-vehicle-modeling`, `revit-dynamo-animation`, `revit-driving-games`, `revit-runtime-delivery` | Driving tests recorded; road rollover was not replayed end to end. |
| Fremont Optimus modeling and production animation | `revit-modeless-runtimes`, `revit-character-controls`, `revit-articulated-animation`, `revit-factory-animation` | Conceptual production bay; not measured factory layout or robot programming. |
| Optimus controller responsiveness | `revit-modeless-runtimes`, `revit-character-controls`, `revit-articulated-animation`, `revit-factory-animation` | Transform/pose throttling measured; timing samples are not a guaranteed FPS benchmark. |
| Miami street, driving, shop, population and environment | `revit-resumable-builds`, `revit-urban-streets`, `revit-sites-landscape`, `revit-modeless-runtimes`, `revit-character-controls`, `revit-driving-games`, `revit-pedestrians-traffic`, `revit-missions-economy`, `revit-day-night-audio`, `revit-runtime-delivery` | Many versioned revisions; geometry/routes/audio and playable features accounted for separately. |
| Miami camera flythrough and video export | `revit-cinematic-export` | Saved exporter and shot sequence; film is tied to scene revision at capture. |
| Miami missions, rewards and saved progress | `revit-missions-economy`, `revit-runtime-delivery` | 69 recorded rule assertions and live save/objective tests; allMissionEndToEndDriveRetested=false. |
| In-Revit demolition and BEPU rigid-body cache | `revit-modeless-runtimes`, `revit-directcontext3d`, `revit-demolition-physics`, `revit-runtime-delivery` | Visual physics prototype; historical final Reset-to-BIM acceptance incomplete. |
| Optimus model-linked dashboard | `revit-digital-twin-dashboards`, `revit-runtime-delivery` | Recorded UI/export/model tests; operational metrics explicitly synthetic. |
| Fremont highway, parking, yard and landscape | `revit-geometry-units`, `revit-sites-landscape`, `revit-factory-animation` | Aerial-reference estimates and grouped repeated geometry; retained interior playback not retested in site pass. |
| Four-legged walker modeling and animation | `revit-reference-modeling`, `revit-geometry-units`, `revit-resumable-builds`, `revit-articulated-animation`, `revit-directcontext3d`, `revit-flight-combat`, `revit-runtime-delivery` | Live walking/fire/reset evidence recorded; dimensions remain reference estimates. |
| Flyable airspeeder and walker battle | `revit-modeless-runtimes`, `revit-directcontext3d`, `revit-flight-combat`, `revit-runtime-delivery` | V6 physical controls/victory/reset evidence; defeat sample references an earlier engine runtime. |
| Compact podcast studio and corridor | `revit-native-house-refinement`, `revit-furniture-interiors` | Measured interior 10x10 ft/100 sf in recorded report; acoustic performance not engineered. |

See source-evidence.json for source-file fingerprints and dates. API signature compatibility, historical test evidence, pure helper tests, package installation, and live Revit acceptance are distinct checks. This packaging pass does not retest every model or game.

---

<a id="compatibility-validation"></a>

## Appendix: Compatibility and validation

### Compatibility and validation boundaries

The library contains 44 flat Geopogo skills plus matching canonical SKILL.md source folders. The installed loader's first non-heading, nonempty line supplies its discovery description; the Geopogo files intentionally do not begin with YAML. The source-skills/ copies do use YAML for skill-authoring tools. Only skills/ belongs in the Geopogo loader directory.

Named tool references were compared with the available connector tool list from the packaging session. All detected Geopogo-style tool names are available in that snapshot. API classes such as ExternalEvent and DirectContext3D are developer interfaces, not callable MCP tools. Inspect live schemas on the recipient installation.

Original introductory wall/floor/door/window/column examples were adjusted to the inspected schemas and roof automatic-view behavior. Historical source examples are not a full argument-by-argument certification of all tool versions. New game/physics skills describe add-in/Dynamo development; they do not imply those runtimes are built into Geopogo.

Saved validation evidence is labeled by workflow: all Miami mission routes were not replayed; advanced Sims autonomy needs live acceptance; DeLorean rollover was not fully driven; demolition final reset was not rechecked in the older record; Unreal actual Datasmith import was not verified; battle reports include a prior-version defeat sample. Source documentation and available artifacts supersede abbreviated history summaries when they conflict about which projects exist.

This release verifies packaging, skill structure, pure helper behavior and installer behavior, not all live Revit projects. Use each skill's acceptance checks on the recipient model/version. No Revit document or plugin binary is modified by the skill-library installer.

### Recorded package validation

```json
{
  "date": "2026-09-30",
  "version": "2026.09.30.2",
  "passed": true,
  "installableSkills": 44,
  "externalReferences": 2,
  "skillFormatChecks": {
    "checked": 44,
    "passed": 44
  },
  "pureHelperTests": {
    "passed": 8,
    "failed": 0,
    "framework": "node:test"
  },
  "contentAudit": {
    "date": "2026-09-30",
    "installableSkills": 44,
    "canonicalBodiesMatch": true,
    "meaningfulDiscoveryDescriptions": true,
    "privatePathScanPassed": true,
    "historicalSessionsIndexed": 41,
    "artifactProjectFoldersIndexed": 29,
    "sourceSets": 35,
    "referencesNeedingReview": [],
    "toolNamesNotExposed": {}
  },
  "installerChecks": [
    "WhatIf leaves destination absent",
    "Clean install produces exactly the manifest count of discoverable skills",
    "Repeated identical install makes no backups or changes",
    "Conflicting user content fails before writes",
    "Replacement preserves custom file and legacy markdown in backups, removes duplicate, and writes restore map",
    "Tampered skill is rejected before destination creation",
    "Installed loader emulation finds the manifest count of unique named skills with meaningful descriptions"
  ],
  "coverage": {
    "priorChats": 41,
    "artifactProjectFolders": 29,
    "sourceSets": 35,
    "unmappedChats": 0,
    "unmappedArtifactFolders": 0
  },
  "liveRevitWorkflowTests": false,
  "originalGamesInstalled": false,
  "externalReferencesInstalled": false
}
```

---

<a id="package-usage"></a>

## Appendix: Installation and package usage

The installation instructions below apply to the ZIP distribution, not to this single Markdown file by itself.

### Geopogo Revit Skills - Expanded Library

Version 2026.09.30.2 replaces the smaller first package. It contains **44 installable skills** (six original workflows, 37 newly extracted workflows, one library index), plus two external references. It captures the reusable modeling, games, animation, custom-physics, dashboard, and delivery work found in the accessible local history. See SOURCE-COVERAGE.md for exactly what is represented.

#### Install

Extract the ZIP, open PowerShell in this folder, and run:

```powershell
.\Install-GeopogoSkills.ps1
```

To update existing versions with backups:

```powershell
.\Install-GeopogoSkills.ps1 -ReplaceExisting
```

Use -WhatIf to preview or -Destination to select an alternate test/profile directory. The default is the current user's roaming GeopogoAI/Skills directory. No administrator rights are needed. Without -ReplaceExisting, conflicting files cause an error before installation. Backups and a restore map go in the sibling Skills-Backups folder. Same-name legacy .md files are backed up and removed from the flat loader directory during an explicit replacement.

If local script policy prevents execution, manually import the .geopogo-skill files through Geopogo AI > Skills, or copy only skills/* into %APPDATA%\GeopogoAI\Skills after backing up conflicts. Keep README and catalog files outside that directory: the inspected loader treats every top-level .md as a skill. Restart the AI connection to refresh prompts, call list_skills, and load geopogo-revit-library with get_skill.

#### What the library adds

- Mario/Optimus movement, walking poses, chase cameras, and focus-safe controls.
- DeLorean/Miami driving, entry/exit, shops, rewards, missions, traffic, and saved progress.
- Sims needs and resource reservations, theme-park rides, factory production and model-linked dashboards.
- Day/night effects, audio/radio blending, camera flythrough/video export.
- DirectContext3D previews, demolition physics, walkers, and airspeeder flight/combat.
- Organic houses, towers/crowns, bridges, ships, aircraft, rockets, vehicles, furniture, small interiors, city/landscape context, MEP, sheets, sculptures and Unreal materials.
- Shared unit/geometry checks, resumable builds, semantic model guards, runtime performance and portable delivery.

These are instructions for building and maintaining those capabilities. They do not install the original games or include the original RVTs, project DLLs, manufacturer assets, personal save games, reference imagery, or music. The extra code under scripts/ is portable pure-logic helper code; it does not access Revit.

#### Plugin integration

Ship the flat skills/ files as content assets and provision them per user on install/first run. Preserve user-edited versions or back them up on upgrades. Keep source-skills/ (canonical SKILL.md folders), package docs, optional helpers, and external references outside the Geopogo flat loader directory. Read only the relevant skills for a task rather than loading the full library. No Geopogo plugin binary has been modified or deployed by this package.

#### Evidence and validation

Each new workflow states its sources, concrete procedures, failure cases, and acceptance checks. SOURCE-COVERAGE.md and source-evidence.json trace the synthesis without distributing private session logs. Source claims are historical: some projects were partial, several tests cover older versions, and all Miami mission routes were not replayed. VALIDATION.json reports checks actually performed for this package. COMPATIBILITY.md separates tool/schema review from live execution. SHA256SUMS.json covers the payload; the ZIP has a separate checksum.

Run optional pure helper tests with Node.js: node --test tests/helpers.test.mjs. Read scripts/README.md before adapting the helpers. Revit runtimes require their own live launch/input/render/reset/save/reopen tests on the recipient version.

#### Attribution

The two original external reference documents remain in external-references/. See THIRD-PARTY-NOTICES.md before adding them to a public plugin release. They are not part of the automatic installer. The packaging process does not assign a new license or claim ownership of third-party material.

### Version 2026.09.30.2

Expanded from six installable workflow files to 44. Added 37 workflows from saved modeling/game/simulation work, a selective router, source coverage/fingerprints, canonical source-skill folders, and portable pure-logic helper examples. Retained the six original workflows and two external references. Generalized the installer for the manifest count. Source completion limits remain explicit; no original game runtime was represented as newly tested.

---

<a id="external-references"></a>

## Appendix: Attribution and external references

### Source attribution and release notes

#### Architecture Studio

The supplied document credits “Federico Negro (2026), Alpaca Design Lab LLC” and states “MIT-licensed”; those statements are preserved verbatim in external-references/architecture-studio-unified.md. The local skill does not include the full MIT license or the referenced docs/agents.md, docs/firm-deployment.md, PATTERNS.md, CHANGELOG.md, individual skill folders, scripts, or templates. Obtain the original license notice and supporting repository before shipping this as a complete working framework. Its 46+ capability descriptions are one reference document, not 46 installed implementations.

#### Revit API Interface

The installed file was named SKILL.md and identifies itself as revit-api-interface with skill-id CIV-SK-016 and mcpmarket-version 1.0.0. No creator or license text accompanies the local copy. Preserved as external-references/revit-api-interface.md for maintainer review; not automatically installed. Confirm redistribution terms with the original source before bundling publicly.

#### Six workflow skills

These were collected from the supplied Geopogo installation and saved Revit skill library. No blanket license or ownership assertion has been added. inventory.json records source filenames, original hashes, and packaging changes. Original files on this machine were left unchanged.

#### Expanded workflows and helper examples

Version 2026.09.30.2 adds 37 workflow syntheses and one library router derived from saved project work, plus newly generalized pure-logic helper examples. Original RVTs, project-specific DLLs, licensed manufacturer assets, supplied reference imagery and music are not redistributed. Source fingerprints support traceability; they do not change third-party rights. No blanket license is assigned by this package.

### External reference: Architecture Studio — Complete AEC Skill Framework

**Identifier:** `architecture-studio-unified`  
**Distribution status:** External framework; claims MIT; full license and supporting files absent locally.

```yaml
name: architecture-studio-unified
description: Complete Architecture Studio framework — 46 professional skills for AEC firms covering EPD & product data, project management, NYC zoning & regulatory, site analysis, design tools, and data schemas. Consolidates color palettes, schedules, specs, occupancy, sustainability, and more.
aliases: [as, arch-studio, aec-tools]
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
```


A unified, local-first framework for architecture firms to standardize AI-assisted workflows. This master skill consolidates **46+ professional capabilities** across product research, project management, site & regulatory analysis, and design operations.

Created by Federico Negro (2026), Alpaca Design Lab LLC. MIT-licensed.

---

#### Quick Navigation

**Dispatch on keywords or use the full skill name:**

##### 📊 **EPD & Product Data** (8 skills)
- **`epd-parser`** — Extract GWP, impact metrics from EPD PDFs
- **`epd-research`** — Search & find industry-standard EPDs
- **`epd-compare`** — Compare GWP and environmental metrics across products
- **`epd-to-spec`** — Write spec language from EPD data
- **`product-research`** — Research building products by category or brand
- **`product-data-import`** — Import & normalize product datasets
- **`product-data-cleanup`** — Clean messy product data into standard schema
- **`product-spec-pdf-parser`** — Extract specs from manufacturer PDFs

##### 🏗️ **Project Management** (8 skills)
- **`master-schedule`** — Create & manage project timelines (CSV-based)
- **`meeting-minutes`** — Template & structure meeting documentation
- **`site-visit-report`** — Document site conditions & findings
- **`project`** — Initialize & manage project workspace (records, templates, context)
- **`tasklist`** — Create task lists & assignment tracking
- **`timetracker`** — Log project time by phase/discipline
- **`workplan`** — Plan phases, deliverables, resource allocation
- **`studio`** — Set up firm-wide studio workspace & preferences

##### 🗽 **NYC Zoning & Regulatory** (8 skills)
- **`nyc-bsa`** — Board of Standards & Appeals: variances, appeals, precedent
- **`nyc-landmarks`** — Landmarks Preservation Commission rules & procedures
- **`nyc-dob-permits`** — NYC DOB permit types, filing requirements, timelines
- **`nyc-dob-violations`** — Search & interpret DOB violation records
- **`nyc-hpd`** — Housing Preservation Dept.: registrations, violations, compliance
- **`nyc-acris`** — ACRIS property transaction & deed data
- **`nyc-property-report`** — Generate property reports: zoning, lot, tax info
- **`zoning-analysis-nyc`** — Zoning compliance, FAR, use groups, restrictions

##### 🌍 **Site & Environmental Analysis** (7 skills)
- **`demographics-analysis`** — Census data, neighborhood profiles, market analysis
- **`environmental-analysis`** — Site remediation, flood risk, environmental assessment
- **`mobility-analysis`** — Transit, walkability, commute patterns
- **`occupancy-calculator`** — Egress, occupancy load, life safety compliance
- **`site-history`** — Property history, prior uses, ownership records
- **`zoning-envelope`** — FAR modeling, massing envelope generation
- **`workplace-programmer`** — Space programming by use type & occupancy

##### 🎨 **Design & Specification** (9 skills)
- **`spec-writer`** — Write CSI-formatted specifications (2-part, 3-part)
- **`slide-deck-generator`** — Create presentation decks from structured content
- **`color-palette-generator`** — Design color schemes for interiors/branding
- **`product-match`** — Match finishes, colors, materials across vendors
- **`product-pair`** — Find compatible products (wood/finish combos, etc.)
- **`product-enrich`** — Add images, specs, sourcing to product records
- **`product-image-processor`** — Resize, optimize product images for specs/web
- **`resize-images`** — Batch image resizing & format conversion
- **`studio-feedback`** — Evaluate design work against studio standards

##### 📈 **Data & Schema Management** (5 skills)
- **`csv-to-sif`** — Convert product CSVs to Sustainability Initiatives Framework
- **`sif-to-csv`** — Export SIF data back to spreadsheet format
- **`product-spec-bulk-fetch`** — Download specs in bulk from manufacturer APIs
- **`tool-catalog`** — Maintain & search firm's tool & software inventory
- **`learn`** — Learn by example: browse templates, examples, sandbox projects

##### 🛠️ **Infrastructure & Governance** (2 skills)
- **`skill-maker`** — Create, validate, test new custom skills for your firm
- **`skill-creator-advanced`** — Optimize & benchmark skill performance

---

#### How to Use This Unified Skill

##### Option 1: Direct Dispatch by Name
State the skill name and task:
```
Use epd-parser to extract GWP from this EPD PDF.
Use master-schedule to create a project timeline.
Use nyc-zoning-analysis to check lot coverage.
```

##### Option 2: Describe Your Task (Smart Routing)
Describe what you need; this skill routes to the right tool:
```
I need to compare environmental impact between these 3 concrete products.
→ Routes to: epd-compare

I want to set up a new project with phases and deliverables.
→ Routes to: project + workplan + master-schedule

What's the zoning for this Manhattan lot?
→ Routes to: nyc-property-report + zoning-analysis-nyc
```

##### Option 3: Chaining Skills
Skills reference each other. Typical workflows:

**Product Specification Workflow:**
1. `product-research` — Find candidate products
2. `product-data-import` — Import datasets
3. `epd-research` — Get EPD for each product
4. `epd-compare` — Compare environmental metrics
5. `epd-to-spec` — Write CSI spec language
6. `spec-writer` — Format full specification

**Project Setup Workflow:**
1. `project init` — Create workspace
2. `nyc-property-report` — Get lot/zoning info
3. `site-history` — Research prior uses
4. `demographics-analysis` — Neighborhood context
5. `workplan` — Define phases & milestones
6. `master-schedule` — Create detailed timeline

**NYC Compliance Workflow:**
1. `zoning-analysis-nyc` — Check FAR, use group
2. `nyc-landmarks` — If applicable, check designation
3. `nyc-bsa` — Identify variance needs
4. `occupancy-calculator` — Calculate egress requirements
5. `meeting-minutes` — Document DoB pre-filing meeting
6. `master-schedule` — Track permit timeline

---

#### Core Concepts Across All Skills

##### 1. **Local-First Data Storage**
- **Studio workspace**: Firm-wide shared data in `~/.as/studio/`
- **Project workspaces**: Project-specific records in `<project-root>/`
- **Portable CSV**: All tabular data uses standardized CSV contracts (epd, ffe, schedule, etc.)
- **No cloud sync**: Records stay local; you control distribution

##### 2. **Data Schemas & Contracts**
All skills use standardized, documented schemas:

| Schema | Purpose | Columns |
|--------|---------|---------|
| **EPD Schema** | Environmental impact data (GWP, ODP, AP, EP, etc.) | 42 columns |
| **FF&E Schema** | Furniture, fixture, equipment product records | 33 columns |
| **Schedule Schema** | Master schedule (phases, tasks, dates, dependencies) | 15+ columns |
| **Meeting Minutes** | Decisions, action items, attendees | Templated |
| **Site Visit Report** | Conditions, findings, photos, recommendations | Templated |
| **Specification** | CSI 2-part or 3-part formatted specs | Markdown + rules |

Schemas are shared across all tools; data stays interoperable.

##### 3. **CSI & Professional Formatting**
Specs and technical documentation follow CSI standards:
- **2-part specs**: General + Technical (concise)
- **3-part specs**: General + Products + Execution (detailed)
- **Proper terminology**: Consistent material names, abbreviations, units
- **Citations**: Track product sources, EPDs, test standards

##### 4. **Governance & Rules**
Every output is validated against firm standards:
- **Terminology rules**: Consistent naming (e.g., "ReadyMix Concrete" not "ready mix" or "RMC")
- **Units & measurements**: Imperial (US), metric, or both with conversion
- **Professional disclaimers**: Liability language for regulatory/structural advice
- **Output formatting**: Markdown, CSI, or spreadsheet
- **Code citations**: Proper reference formatting (IBC, NYC Building Code, ASTM, ISO, etc.)

##### 5. **Multi-Product & Bulk Operations**
Skills handle single items and bulk batches:
- **EPD parser**: One PDF or a whole folder (processes each separately)
- **Product import**: Single item or 100-row CSV (normalized automatically)
- **Image processor**: One image or batch resizing
- **Bulk spec fetch**: Single product or batch download from manufacturers

---

#### Skill Groups Explained

##### EPD & Sustainability (8 skills)
**Use case:** Specify low-carbon concrete, compare insulation GWP, document LEED v4.1 requirements.

- **epd-parser**: Reads EPD PDFs (ISO 14025 format), extracts GWP (kg CO2e), ODP, AP, EP, POCP, resource use, certifications. Handles EN 15804+A1 & +A2 formats, multi-product declarations, industry vs. product-specific EPDs.
- **epd-research**: Finds EPDs by product category (concrete, steel, insulation, etc.) or manufacturer. Searches program databases (NSF, UL, PCR), checks validity dates, identifies product-specific vs. industry-average.
- **epd-compare**: Compares GWP and impact metrics across 2-5 products side-by-side. Normalizes to common declared unit (m³, kg, etc.), flags data quality issues, contextualizes against industry baselines with citations.
- **epd-to-spec**: Converts EPD data into specification paragraph language. Example: *"Concrete shall demonstrate a GWP of ≤350 kg CO2e per m³ (cradle-to-gate, A1-A3) verified by a current product-specific EPD conforming to ISO 14025 and ASTM C1888."*
- **product-research**: General building product research (finishes, windows, HVAC, doors, casework). Searches manufacturer specs, certifications (FSC, Cradle-to-Cradle, Declare), lead times.
- **product-data-import**: Bulk-imports product data from spreadsheets or APIs. Normalizes vendor data into firm schema (product name, manufacturer, finish, cost, lead time, specs).
- **product-data-cleanup**: Deduplicates, standardizes, and enriches messy product datasets. Fixes manufacturer name typos, normalizes finish names, fills missing fields.
- **product-spec-pdf-parser**: Extracts structured data from manufacturer PDF datasheets. Pulls dimensions, material content, fire ratings, acoustic properties, certifications.

**Common workflow:** Research → Import → Clean → Compare EPDs → Write spec

##### Project Management (8 skills)
**Use case:** Set up a new project, track phases, schedule meetings, document decisions.

- **project**: Creates & manages project workspace. Initializes `PROJECT.md`, `AGENTS.md`, `TASKS.md`, record directories. Resolves context across the project (nearby files, scope, team).
- **master-schedule**: Creates project master schedule (CSV). Rows = tasks/phases. Columns = start date, end date, duration, dependencies, assignee, % complete. Integrates with other skills.
- **workplan**: Higher-level planning. Defines project phases (Design, BD, DD, CD, Permit, etc.), key deliverables per phase, resource allocation, risk notes.
- **tasklist**: Creates task lists. Useful for design studios, construction admin, or action-item tracking. Simpler than master schedule (no Gantt). Template-based.
- **meeting-minutes**: Structured meeting documentation. Captures attendees, agenda, decisions, action items (with owners & due dates), next meeting date.
- **site-visit-report**: Documents site conditions. Includes: date, weather, observations (structural, MEP, existing conditions), photos/sketches, recommendations, follow-up items.
- **timetracker**: Logs billable time by project, phase, discipline. Aggregates for invoicing or resource analysis.
- **studio**: Firm-wide workspace setup. Defines studio preferences (units, terminology, style), shared project templates, agent assignments.

**Common workflow:** project init → workplan → master-schedule → tasklist for action items → meeting-minutes for decisions

##### NYC Zoning & Regulatory (8 skills)
**Use case:** Navigate NYC's complex regulatory environment for commercial, residential, and landmark projects.

- **zoning-analysis-nyc**: Interprets NYC zoning rules. Checks: use group (primary/secondary), FAR, lot coverage, height/setback, required parking, residential sky exposure planes, contextual restrictions. Cross-references NYC Building Code.
- **nyc-property-report**: Generates property profile: lot dimensions, zoning district, current use, tax classification, floor area ratio (FAR) allowance, bonuses available (CEQR, LEED density bonus), easements, condo/coop status.
- **nyc-landmarks**: LPC rules for landmark buildings & historic districts. Summarizes: what requires approval (façade, interior, mechanical), design guidelines, appeals process, typical timelines.
- **nyc-bsa**: Board of Standards & Appeals. Navigates: variance types (use, area, bulk), precedent searches, appeal procedures, timeline. References prior decisions.
- **nyc-dob-permits**: NYC DOB (Department of Buildings) permit matrix. Identifies: Alt-2 vs. Alt-1 vs. self-certified, filing requirements, timeline (typically 10 days for review), application forms, examiner specialties.
- **nyc-dob-violations**: DOB violation lookup by BIS number. Searches historical violations, construction/safety issues, status (open, resolved, dismissed).
- **nyc-hpd**: NYC Housing Preservation Dept. Tracks: rent-regulated buildings, violation records, registration requirements for multifamily.
- **nyc-acris**: ACRIS (Automated City Register Information System) property records. Looks up deed history, transfers, liens, document details.

**Common workflow:** Property address → nyc-property-report → zoning-analysis-nyc → (if landmarks) nyc-landmarks → (if variance needed) nyc-bsa → master-schedule for permit timeline

##### Site & Environmental Analysis (7 skills)
**Use case:** Understand neighborhood context, check site constraints, calculate occupancy & egress.

- **demographics-analysis**: Census data, population, income, household composition, employment. Contextualizes location for market feasibility or community engagement.
- **environmental-analysis**: Site environmental constraints: flood zone (FEMA), contamination risk, vapor intrusion, environmental justice, CEQR screening (if in NYC). Flags remediation needs.
- **mobility-analysis**: Transit access (subway, bus), bike infrastructure, walkability score, parking supply. Contextualizes commute patterns.
- **occupancy-calculator**: Life-safety calculations per NYC Building Code (or IBC). Calculates: occupant load by use type (sq ft per person), egress width requirements (0.15 sq in. per person stairwell, 0.1 sq in. doors), stair count, emergency lighting, accessible routes.
- **site-history**: Property history: prior uses, demolitions, ownership chains, historical documents. Useful for contamination assessment or context narrative.
- **zoning-envelope**: Massing envelopes for a lot. Applies FAR limit, setback rules, lot coverage. Shows maximum buildable volume given zoning.
- **workplace-programmer**: Space program generation. Inputs occupancy or org chart; outputs: sq ft per department, total program, common areas, phasing.

**Common workflow:** Address → demographics + environmental + mobility → zoning-envelope for massing → occupancy-calculator for egress → workplace-programmer for space planning

##### Design & Specification (9 skills)
**Use case:** Create specifications, coordinate finishes, generate presentations.

- **spec-writer**: Writes CSI-formatted specifications (2-part or 3-part). Standardizes language, embeds product data, cites standards (ASTM, ISO, NCS), cross-references drawings.
- **slide-deck-generator**: Creates HTML presentation decks. Inputs: slides (text, images, tables). Outputs: interactive slide deck in one `.html` file.
- **color-palette-generator**: Generates harmonious color palettes. Inputs: primary color, mood (corporate, playful, calming, etc.). Outputs: 5–7-color palette with hex codes, usage guidance.
- **product-match**: Matches finishes across vendors. Example: *"I have Benjamin Moore paint in gray-blue; find a compatible wood stain and upholstery."* Searches comparable products.
- **product-pair**: Suggests compatible material combinations. Example: *"Wood species + finish" or "metal frame + fabric."* Uses material databases to find harmonious pairings.
- **product-enrich**: Adds detail to product records: images, finish options, certifications, sourcing (where to buy, cost, lead time).
- **product-image-processor**: Resizes & optimizes product images for specs or web. Batch process, maintain aspect ratio, standardize dimensions.
- **resize-images**: General-purpose batch image resizing & format conversion.
- **studio-feedback**: Evaluates design work (sketches, 3D renderings, layouts) against studio design standards. Provides critique & suggestions.

**Common workflow:** product-research → product-enrich (add images/specs) → product-match/pair (coordinate finishes) → spec-writer (write specs) → slide-deck-generator (present to client)

##### Data & Schema Management (5 skills)
**Use case:** Manage firm data, export to different formats, catalog tools & resources.

- **csv-to-sif**: Convert product data CSV to Sustainability Initiatives Framework (SIF) format. Standardizes environmental data for LEED, Embodied Carbon reporting.
- **sif-to-csv**: Export SIF data back to spreadsheet for analysis, filtering, or re-import to other tools.
- **product-spec-bulk-fetch**: Bulk-download product specs from manufacturer websites (if APIs available). Saves manual PDF hunting.
- **tool-catalog**: Maintains firm's tool & software inventory. Tracks: software name, version, licenses (seats, expiration), cost, purpose, team owner.
- **learn**: Browse templates, examples, sandbox projects. Onboard new team members. Explore Architecture Studio patterns & conventions.

##### Infrastructure (2 skills)
- **skill-maker**: Create custom skills for your firm. Templates, validation, testing framework. Turn firm workflows into reusable AI tools.
- **skill-creator-advanced** (implied): Optimize & benchmark skill performance. Runs evals, measures accuracy, suggests improvements.

---

#### Data & File Conventions

All skills follow these conventions for **portability** and **interoperability**:

##### Workspace Structure
```
~/.as/studio/                          # Firm-wide studio
├── studio-preferences.md              # Units, terminology, templates
├── agents.md                          # Agent definitions
└── data/
    ├── product-library.csv            # Firm product database (FF&E schema)
    ├── epd-library.csv                # EPD records (42-column schema)
    └── tool-catalog.json              # Software inventory

<project-root>/                        # Project workspace
├── PROJECT.md                         # Project metadata & scope
├── WORKPLAN.md                        # Phases & deliverables
├── AGENTS.md                          # Project agents & roles
├── TASKS.md                           # Task list
├── TIMELOG.md                         # Time tracking
├── records/                           # Project-specific data
│   ├── master-schedule.csv
│   ├── epd-library.csv
│   ├── site-visit-reports/
│   └── meeting-minutes/
└── deliverables/                      # Output specs, drawings, etc.
```

##### CSV Schemas (Import/Export)
All CSV data uses documented schemas:
- **EPD Schema** (`epd-library.csv`): 42 columns — GWP, ODP, AP, EP, POCP, resource use, metadata
- **FF&E Schema** (`product-library.csv`): 33 columns — product name, category, manufacturer, finish, cost, specs, certifications
- **Schedule Schema** (`master-schedule.csv`): phases, tasks, start/end, duration, dependencies, % complete, assignee
- **Meeting Minutes** (Markdown template) — attendees, agenda, decisions, actions, next meeting

Schemas ensure data portability across skills.

---

#### Triggering This Skill

This unified skill activates on:

##### Explicit Skill Names
```
Use epd-parser to…
Run product-research on…
Launch master-schedule for…
```

##### Keywords by Domain
| Keyword | Routes To |
|---------|-----------|
| GWP, carbon, EPD, environmental impact | epd-* skills |
| schedule, timeline, Gantt, phases, workplan | master-schedule, workplan |
| NYC zoning, FAR, use group, landmark, BSA | nyc-* or zoning-* skills |
| specification, spec, CSI, 2-part, 3-part | spec-writer |
| color palette, design, finish coordination | color-palette-generator, product-match |
| occupancy, egress, life safety | occupancy-calculator |
| site visit, conditions, observations | site-visit-report |
| meeting minutes, decisions, action items | meeting-minutes |

##### Full Descriptions
*"I need to set up a new NYC commercial project with regulatory checks and a schedule."*
→ Routes to: project init → nyc-property-report → zoning-analysis-nyc → workplan → master-schedule

---

#### Key Features

✅ **46+ Professional Skills** — comprehensive AEC toolkit  
✅ **Data Interoperability** — standardized CSV schemas across all tools  
✅ **Local-First** — firm data stays in your workspace, not in cloud  
✅ **Firm Governance** — CSI formatting, terminology rules, disclaimer enforcement  
✅ **NYC-Specific** — full zoning, regulatory, and compliance tools for New York projects  
✅ **Sustainability** — EPD parsing, GWP comparison, LEED documentation  
✅ **Project Management** — workplans, schedules, site visits, meeting minutes  
✅ **Extensible** — skill-maker for custom firm workflows  
✅ **Open-Source** — MIT-licensed, built by architects for architects  

---

#### Getting Started

1. **Review available skills**: Ask *"What skills are available?"* — this file lists all 46+.
2. **Choose a domain**: Pick a workflow (project setup, product specification, zoning analysis).
3. **Invoke a skill by name**: *"Use master-schedule to create a timeline for phases Design, BD, DD, CD, Permit."*
4. **Chain skills**: Skills reference each other; follow the suggested workflows above.
5. **Explore templates**: Use **`learn`** skill to browse examples & sandbox projects.
6. **Customize**: Use **`skill-maker`** to create firm-specific tools (e.g., a standard site-visit template).

---

#### Support & Attribution

**Architecture Studio** v1.4.4  
Created by Federico Negro (2026)  
Alpaca Design Lab LLC  
MIT License — use freely in your firm, contribute improvements back to open-source.

Questions? See the bundled documentation in the plugin repository:  
- `docs/agents.md` — Agent definitions  
- `docs/firm-deployment.md` — Firm setup guide  
- `PATTERNS.md` — Common workflows & patterns  
- `CHANGELOG.md` — Release history  

---

#### Consolidated Skill Reference (46 Skills)

| Skill | Category | Purpose |
|-------|----------|---------|
| **epd-parser** | EPD & Sustainability | Parse EPD PDFs, extract GWP & environmental metrics |
| **epd-research** | EPD & Sustainability | Find industry-standard EPDs by product/category |
| **epd-compare** | EPD & Sustainability | Compare GWP & impacts across 2-5 products |
| **epd-to-spec** | EPD & Sustainability | Convert EPD data to specification language |
| **product-research** | EPD & Sustainability | Research building products by category or brand |
| **product-data-import** | EPD & Sustainability | Import & normalize product datasets |
| **product-data-cleanup** | EPD & Sustainability | Clean & deduplicate product data |
| **product-spec-pdf-parser** | EPD & Sustainability | Extract specs from manufacturer PDFs |
| **master-schedule** | Project Management | Create & manage project timelines |
| **meeting-minutes** | Project Management | Document meetings, decisions, action items |
| **site-visit-report** | Project Management | Record site conditions & observations |
| **project** | Project Management | Initialize & manage project workspace |
| **tasklist** | Project Management | Create task lists & assignments |
| **timetracker** | Project Management | Log billable time by phase/discipline |
| **workplan** | Project Management | Plan phases, deliverables, resources |
| **studio** | Project Management | Set up firm-wide studio workspace |
| **nyc-bsa** | NYC Regulatory | Board of Standards & Appeals: variances, appeals |
| **nyc-landmarks** | NYC Regulatory | Landmarks Preservation Commission rules |
| **nyc-dob-permits** | NYC Regulatory | DOB permit types & filing requirements |
| **nyc-dob-violations** | NYC Regulatory | Search DOB violation records |
| **nyc-hpd** | NYC Regulatory | Housing Preservation: registrations, violations |
| **nyc-acris** | NYC Regulatory | ACRIS property & deed records |
| **nyc-property-report** | NYC Regulatory | Generate property reports: zoning, lot, tax |
| **zoning-analysis-nyc** | NYC Regulatory | Zoning compliance, FAR, use groups |
| **demographics-analysis** | Site Analysis | Census data, neighborhood profiles |
| **environmental-analysis** | Site Analysis | Site constraints, flood risk, remediation |
| **mobility-analysis** | Site Analysis | Transit, walkability, commute patterns |
| **occupancy-calculator** | Site Analysis | Egress, occupancy load, life safety |
| **site-history** | Site Analysis | Property history & prior uses |
| **zoning-envelope** | Site Analysis | FAR massing, setback envelopes |
| **workplace-programmer** | Site Analysis | Space program generation |
| **spec-writer** | Design & Spec | Write CSI 2-part or 3-part specs |
| **slide-deck-generator** | Design & Spec | Create HTML presentation decks |
| **color-palette-generator** | Design & Spec | Design harmonious color palettes |
| **product-match** | Design & Spec | Match finishes across vendors |
| **product-pair** | Design & Spec | Find compatible material combinations |
| **product-enrich** | Design & Spec | Add images, specs, sourcing to products |
| **product-image-processor** | Design & Spec | Optimize product images for specs/web |
| **resize-images** | Design & Spec | Batch resize & convert images |
| **studio-feedback** | Design & Spec | Evaluate design work against standards |
| **csv-to-sif** | Data & Schema | Convert product CSV to SIF format |
| **sif-to-csv** | Data & Schema | Export SIF data to spreadsheet |
| **product-spec-bulk-fetch** | Data & Schema | Bulk-download product specs |
| **tool-catalog** | Data & Schema | Maintain firm tool & software inventory |
| **learn** | Data & Schema | Browse templates, examples, sandbox |
| **skill-maker** | Infrastructure | Create custom skills for your firm |

---

**Ready to start?** Describe your task or invoke a skill by name. This unified framework routes to the right tool. 🏗️

### External reference: Revit API Interface Skill

**Identifier:** `revit-api-interface`  
**Distribution status:** External marketplace-style metadata; license not supplied locally.

```yaml
name: revit-api-interface
description: Revit API interface skill for element extraction, creation, and automation
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: BIM Coordination
  skill-id: CIV-SK-016
  mcpmarket-version: 1.0.0
```

#### Purpose

The Revit API Interface Skill provides programmatic access to Revit models for element extraction, creation, schedule generation, and automation of structural workflows.

#### Capabilities

- Extract element properties
- Create structural elements
- Generate schedules
- Apply structural parameters
- Export to analysis software
- Rebar detailing automation
- Family parameter management
- View and sheet automation

#### Usage Guidelines

##### When to Use
- Automating Revit workflows
- Extracting model data
- Creating structural elements
- Generating documentation

##### Prerequisites
- Revit model available
- API access configured
- Element parameters defined
- Automation script developed

##### Best Practices
- Test on model copies
- Validate data integrity
- Handle errors gracefully
- Document API usage

#### Process Integration

This skill integrates with:
- BIM Coordination
- Reinforced Concrete Design
- Structural Steel Design

#### Configuration

```yaml
revit-api-interface:
  operations:
    - extract
    - create
    - modify
    - export
  element-types:
    - structural-framing
    - structural-columns
    - walls
    - foundations
    - rebar
```

#### Output Artifacts

- Element extractions
- Schedule exports
- Parameter reports
- Automation logs

---

<a id="developer-helpers"></a>

## Appendix: Developer helpers and tests

### Optional pure-logic helpers

These are newly generalized examples based on the recovered workflows. They are not the original game runtimes, Dynamo nodes, add-ins, or a Revit connection. They require Node.js 18 or later and have no third-party dependencies. Run the accompanying tests from the package root with `node --test tests/helpers.test.mjs`.

#### mission-engine.mjs

Use `createMissionEngine(definitions)` with stable string mission IDs, nonnegative integer rewards, and steps containing `x`, `y`, `radius`, and mode `walk` or `drive`. All coordinates must use the same unit system as the host player state. `start`, `cancel`, `normalize`, and `advance` return new state rather than mutating the caller's save.

Apply a returned completion reward and save the returned mission state together in one host-level durable update. The helper prevents duplicate rewards within a correctly persisted state machine; it does not provide crash-safe storage, multiplayer authority, wallet persistence, or navigation. Replaying an old save can still replay progress unless the host has its own durable ledger.

#### runtime-checks.mjs

- `assertTarget(expected, actual)` compares absolute Windows `modelPath` values and a stable `sceneId`. Resolve the recipient's package/model path first. Do not hard-code the author's path or disable the guard to relocate a model.
- `verifyPlayback(before, after, {requireRendered:true})` expects `modelPath`, `sceneId`, `runtimeVersion`, ISO `capturedAt`, boolean `running`, finite `seconds`, explicit `error:null`, and optionally increasing `renderedFrames`. Adapt the actual runtime's telemetry into this schema; missing evidence deliberately fails. This checks state progression, not visible pixels, keyboard response, reset, or scene correctness.
- `scopedBounds({units:'ft', elements}, sceneId)` unions the matching elements' world-space `min` and `max` arrays. Export only valid geometry and tag ownership reliably. Apply Revit BoundingBoxXYZ transforms to all eight corners before computing those world-space boxes. Cameras/templates with other scene IDs are excluded. The helper does not query Revit or prove the exported element set is complete.

Pair these checks with the corresponding skill's live acceptance steps. No original project media, names, coordinates, account data, or save files are required.

### scripts/mission-engine.mjs

Save this block as `scripts/mission-engine.mjs` relative to the extracted developer folder.

```javascript
// Portable pure mission rules, generalized from the source game's state-machine pattern.
// No Revit calls. Persist returned state and reward together in the host application.
export function createMissionEngine(definitions) {
  if (!Array.isArray(definitions) || !definitions.length) throw Error('Mission definitions are required');
  const defs = structuredClone(definitions);
  const ids = new Set();
  for (const d of defs) {
    if (typeof d.id !== 'string' || !/^[a-z0-9-]+$/.test(d.id) || ids.has(d.id)) throw Error('Mission IDs must be unique stable names');
    ids.add(d.id);
    if (!Number.isSafeInteger(d.reward) || d.reward < 0 || !Array.isArray(d.steps) || !d.steps.length) throw Error('Invalid reward or steps');
    for (const s of d.steps) {
      if (![s.x,s.y,s.radius].every(Number.isFinite) || s.radius <= 0 || !['walk','drive'].includes(s.mode)) throw Error('Invalid objective geometry or mode');
    }
  }
  const byId = new Map(defs.map(d=>[d.id,d]));
  function normalize(input = {}) {
    const completed = [...new Set((Array.isArray(input?.completed) ? input.completed : []).filter(id=>byId.has(id)))];
    const active = input?.active;
    const stage = input?.stage;
    const valid = byId.has(active) && !completed.includes(active) && Number.isInteger(stage) && stage >= 0 && stage < byId.get(active).steps.length;
    return {version:1,active:valid?active:null,stage:valid?stage:0,completed};
  }
  function start(input,id) {
    const state = normalize(input);
    if (!byId.has(id) || state.active !== null || state.completed.includes(id)) return {state,accepted:false};
    return {state:{...state,active:id,stage:0},accepted:true};
  }
  function cancel(input) {return {...normalize(input),active:null,stage:0};}
  function advance(input, position, mode) {
    const state=normalize(input);
    if (state.active===null || !position || ![position.x,position.y].every(Number.isFinite)) return {state,changed:false,reward:0};
    const d=byId.get(state.active),s=d.steps[state.stage];
    if (mode!==s.mode || Math.hypot(position.x-s.x,position.y-s.y)>s.radius) return {state,changed:false,reward:0};
    const stage=state.stage+1;
    if (stage<d.steps.length) return {state:{...state,stage},changed:true,reward:0};
    return {state:{...state,active:null,stage:0,completed:[...state.completed,d.id]},changed:true,reward:d.reward};
  }
  return Object.freeze({normalize,start,cancel,advance});
}
```

### scripts/runtime-checks.mjs

Save this block as `scripts/runtime-checks.mjs` relative to the extracted developer folder.

```javascript
// Pure checks for exported state. This module does not open or edit a Revit document.
import path from 'node:path';
function winPath(value) {
  if(typeof value!=='string' || !path.win32.isAbsolute(value)) throw Error('Expected an absolute Windows model path');
  return path.win32.resolve(value).toLowerCase();
}
export function assertTarget(expected, actual) {
  if(!expected?.sceneId || !actual?.sceneId || expected.sceneId!==actual.sceneId) throw Error('Scene identity mismatch');
  if(winPath(expected.modelPath)!==winPath(actual.modelPath)) throw Error('Model path mismatch');
  return true;
}
export function verifyPlayback(before, after, {requireRendered=false}={}) {
  assertTarget(before,after);
  if(!before.runtimeVersion || before.runtimeVersion!==after.runtimeVersion) throw Error('Runtime version mismatch');
  const a=Date.parse(before.capturedAt),b=Date.parse(after.capturedAt);
  if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a) throw Error('Snapshots must have increasing capture timestamps');
  if(before.error!==null||after.error!==null) throw Error('Error must be explicitly null in both snapshots');
  if(before.running!==true||after.running!==true) throw Error('Both snapshots must show active playback');
  if(!Number.isFinite(before.seconds)||!Number.isFinite(after.seconds)||after.seconds<=before.seconds) throw Error('Simulation time did not advance');
  if(requireRendered&&(!Number.isFinite(before.renderedFrames)||!Number.isFinite(after.renderedFrames)||after.renderedFrames<=before.renderedFrames)) throw Error('Rendered frames did not advance');
  return {passed:true,simulationDelta:after.seconds-before.seconds,wallDeltaSeconds:(b-a)/1000,renderEvidenceRequired:requireRendered};
}
export function scopedBounds(exported, sceneId) {
  if(exported?.units!=='ft' || !sceneId || !Array.isArray(exported.elements)) throw Error('Expected feet-based world-space element bounds and a scene ID');
  const subject=exported.elements.filter(e=>e.sceneId===sceneId);
  if(!subject.length) throw Error('No subject geometry');
  const min=[Infinity,Infinity,Infinity],max=[-Infinity,-Infinity,-Infinity];
  for(const e of subject) {
    if(e.transform) throw Error('Apply BoundingBoxXYZ transform to all corners before exporting world-space bounds');
    if(!Array.isArray(e.min)||!Array.isArray(e.max)||e.min.length!==3||e.max.length!==3||![...e.min,...e.max].every(Number.isFinite)) throw Error('Invalid bounds');
    for(let i=0;i<3;i++){if(e.min[i]>e.max[i])throw Error('Inverted bounds');min[i]=Math.min(min[i],e.min[i]);max[i]=Math.max(max[i],e.max[i]);}
  }
  return {units:'ft',sceneId,count:subject.length,min,max,size:max.map((x,i)=>x-min[i])};
}
```

### tests/helpers.test.mjs

Save this block as `tests/helpers.test.mjs` relative to the extracted developer folder.

```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import {createMissionEngine} from '../scripts/mission-engine.mjs';
import {assertTarget,verifyPlayback,scopedBounds} from '../scripts/runtime-checks.mjs';
const definitions=[{id:'delivery',reward:300,steps:[{x:0,y:0,radius:2,mode:'walk'},{x:20,y:0,radius:3,mode:'drive'}]}];
test('mission must satisfy location and mode; completion pays once after persisted reload',()=>{
 const engine=createMissionEngine(definitions);const original={};let p=engine.start(original,'delivery').state;
 assert.deepEqual(original,{});assert.equal(engine.advance(p,{x:0,y:0},'drive').changed,false);
 assert.equal(engine.advance(p,{x:10,y:0},'walk').changed,false);
 p=engine.advance(p,{x:0,y:0},'walk').state;
 const done=engine.advance(p,{x:20,y:0},'drive');assert.equal(done.reward,300);
 p=JSON.parse(JSON.stringify(done.state));assert.equal(engine.advance(p,{x:20,y:0},'drive').reward,0);
 assert.equal(engine.start(p,'delivery').accepted,false);
});
test('invalid indices, completion duplicates, missing definitions and nonfinite positions are contained',()=>{
 const engine=createMissionEngine(definitions);
 assert.deepEqual(engine.normalize({active:'delivery',stage:-1,completed:['unknown','delivery','delivery']}),{version:1,active:null,stage:0,completed:['delivery']});
 const p=engine.start({},'delivery').state;
 assert.equal(engine.advance(p,{x:NaN,y:0},'walk').changed,false);
 assert.equal(engine.advance(p,{x:Infinity,y:0},'walk').changed,false);
 assert.equal(engine.start(p,'delivery').accepted,false);
 assert.equal(engine.start({},'unknown').accepted,false);
});
test('cancellation does not reward and allows restart',()=>{
 const engine=createMissionEngine(definitions);const p=engine.cancel(engine.start({},'delivery').state);
 assert.equal(p.active,null);assert.equal(engine.advance(p,{x:20,y:0},'drive').reward,0);
 assert.equal(engine.start(p,'delivery').accepted,true);
});
test('invalid mission definitions fail rather than creating unreachable or duplicate objectives',()=>{
 assert.throws(()=>createMissionEngine([...definitions,...definitions]));
 assert.throws(()=>createMissionEngine([{...definitions[0],reward:NaN}]));
 assert.throws(()=>createMissionEngine([{...definitions[0],steps:[{x:0,y:0,radius:-1,mode:'walk'}]}]));
});
const before={modelPath:'C:\\Scenes\\Example.rvt',sceneId:'demo-01',runtimeVersion:'1',capturedAt:'2026-09-30T12:00:00Z',running:true,seconds:2,error:null,renderedFrames:10};
const after={...before,capturedAt:'2026-09-30T12:00:02Z',seconds:4,renderedFrames:12};
test('target guard accepts case normalization but rejects other scenes/files or empty paths',()=>{
 assert.equal(assertTarget(before,{...before,modelPath:'c:/scenes/EXAMPLE.rvt'}),true);
 assert.throws(()=>assertTarget(before,{...before,sceneId:'another'}));
 assert.throws(()=>assertTarget(before,{...before,modelPath:'C:\\Scenes\\Other.rvt'}));
 assert.throws(()=>assertTarget(before,{...before,modelPath:''}));
});
test('playback needs fresh matching telemetry and real progression, including rendering when requested',()=>{
 assert.equal(verifyPlayback(before,after,{requireRendered:true}).passed,true);
 assert.throws(()=>verifyPlayback(before,{...after,seconds:2}));
 assert.throws(()=>verifyPlayback(before,{...after,renderedFrames:10},{requireRendered:true}));
 assert.throws(()=>verifyPlayback(before,{...after,runtimeVersion:'old'}));
 assert.throws(()=>verifyPlayback(before,{...after,capturedAt:before.capturedAt}));
 assert.throws(()=>verifyPlayback(before,{...after,error:undefined}));
 assert.throws(()=>verifyPlayback(before,{...after,running:false}));
});
test('subject bounds exclude large template/camera extents',()=>{
 const result=scopedBounds({units:'ft',elements:[{sceneId:'car',min:[0,0,0],max:[14,6,5]},{sceneId:'car',min:[-1,1,0],max:[0,5,2]},{sceneId:'camera',min:[-500,-600,0],max:[500,600,100]}]},'car');
 assert.deepEqual(result.size,[15,6,5]);assert.equal(result.count,2);
});
test('bounds reject missing subject, wrong units, nonfinite or untransformed geometry',()=>{
 assert.throws(()=>scopedBounds({units:'ft',elements:[]},'car'));
 assert.throws(()=>scopedBounds({units:'mm',elements:[]},'car'));
 assert.throws(()=>scopedBounds({units:'ft',elements:[{sceneId:'car',min:[0,NaN,0],max:[1,1,1]}]},'car'));
 assert.throws(()=>scopedBounds({units:'ft',elements:[{sceneId:'car',min:[0,0,0],max:[1,1,1],transform:{}}]},'car'));
});
```

---

<a id="installer-source"></a>

## Appendix: Installer source

This installer requires the modular package's skills, inventory.json, and SHA256SUMS.json. Copying it from this document alone is insufficient to install the library.

```powershell
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$Destination = (Join-Path $env:APPDATA 'GeopogoAI\Skills'),
    [switch]$ReplaceExisting
)
$ErrorActionPreference = 'Stop'
$packageRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$destinationRoot = [IO.Path]::GetFullPath($Destination)
$hashManifest = Get-Content -LiteralPath (Join-Path $packageRoot 'SHA256SUMS.json') -Raw | ConvertFrom-Json
foreach ($entry in $hashManifest.files) {
    $payload = [IO.Path]::GetFullPath((Join-Path $packageRoot $entry.path))
    if (-not $payload.StartsWith($packageRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Invalid manifest path: $($entry.path)"
    }
    if ((Get-FileHash -LiteralPath $payload -Algorithm SHA256).Hash -ne $entry.sha256) {
        throw "Package integrity check failed: $($entry.path). Extract a fresh copy."
    }
}
$inventory = Get-Content -LiteralPath (Join-Path $packageRoot 'inventory.json') -Raw | ConvertFrom-Json
$skills = @($inventory.inventory | Where-Object { $_.installByDefault })
if (($inventory.installableCount -isnot [int] -and $inventory.installableCount -isnot [long]) -or $inventory.installableCount -lt 1 -or $skills.Count -ne $inventory.installableCount) { throw 'Skill count does not match the release inventory.' }
$plan = @()
foreach ($skill in $skills) {
    if ($skill.id -notmatch '^[a-z0-9-]+$') { throw 'Invalid skill name.' }
    $sourcePath = Join-Path $packageRoot ('skills\' + $skill.id + '.geopogo-skill')
    $targetPath = Join-Path $destinationRoot ($skill.id + '.geopogo-skill')
    $oldMarkdown = Join-Path $destinationRoot ($skill.id + '.md')
    $newHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
    $targetExists = Test-Path -LiteralPath $targetPath
    $same = $targetExists -and ((Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash -eq $newHash)
    $legacyExists = Test-Path -LiteralPath $oldMarkdown
    if ((($targetExists -and -not $same) -or $legacyExists) -and -not $ReplaceExisting) {
        throw "Existing skill conflicts with $($skill.id). Nothing installed. Use -ReplaceExisting to back up and update it."
    }
    $plan += [pscustomobject]@{ Source = $sourcePath; Target = $targetPath; Legacy = $oldMarkdown; Same = $same; TargetExists = $targetExists; LegacyExists = $legacyExists }
}
$changes = @($plan | Where-Object { -not $_.Same -or $_.LegacyExists })
if ($changes.Count -eq 0) { Write-Output "All $($skills.Count) skills are already installed and match this package."; return }
if (-not $PSCmdlet.ShouldProcess($destinationRoot, "Install/update $($changes.Count) Geopogo workflow skills")) { return }
$backupRoot = Join-Path (Split-Path $destinationRoot -Parent) ('Skills-Backups\' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [guid]::NewGuid().ToString('N').Substring(0,8))
$restoreMap = @()
$written = @()
try {
    New-Item -ItemType Directory -Path $destinationRoot -Force | Out-Null
    foreach ($item in $changes) {
        foreach ($existing in @($item.Target, $item.Legacy)) {
            if (($existing -eq $item.Target -and $item.Same) -or -not (Test-Path -LiteralPath $existing)) { continue }
            New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
            $backup = Join-Path $backupRoot ([IO.Path]::GetFileName($existing))
            Copy-Item -LiteralPath $existing -Destination $backup
            $restoreMap += [pscustomobject]@{ Original = $existing; Backup = $backup }
        }
        if (-not $item.Same) {
            $written += $item.Target
            Copy-Item -LiteralPath $item.Source -Destination $item.Target -Force
            if ((Get-FileHash -LiteralPath $item.Source).Hash -ne (Get-FileHash -LiteralPath $item.Target).Hash) { throw "Copy verification failed: $($item.Target)" }
        }
        if ($item.LegacyExists) {
            # A verified backup exists outside the loader's flat skill directory.
            Remove-Item -LiteralPath $item.Legacy
        }
    }
    if ($restoreMap.Count) {
        $restoreMap | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath (Join-Path $backupRoot 'restore-map.json') -Encoding UTF8
    }
} catch {
    $failure = $_
    foreach ($file in $written) { if (Test-Path -LiteralPath $file) { Remove-Item -LiteralPath $file -ErrorAction Continue } }
    foreach ($record in $restoreMap) { Copy-Item -LiteralPath $record.Backup -Destination $record.Original -Force -ErrorAction Continue }
    throw $failure
}
Write-Output "Installed $($skills.Count) skills in $destinationRoot"
if ($restoreMap.Count) { Write-Output "Previous files backed up in $backupRoot" }
Write-Output 'Restart the connected AI session, call list_skills, then load a workflow using get_skill.'
```
