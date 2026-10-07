---
name: ifcopenshell-toolkit
description: >
  IFC toolkit — 15 routed skills from the OpenAEC Foundation covering IFC data-model
  concepts and runtime, the IfcOpenShell API, element and file I/O syntax, IFC creation,
  geometry, relationships, materials, and validation, schema and performance error patterns,
  a code validator agent, and cross-tool BIM workflows with coordinate-system and
  schema bridging (IFC to Blender, Three.js, FreeCAD, Speckle). Load for any task that
  reads, writes, fixes, or validates IFC files exported from or destined for Revit.
---

# IfcOpenShell IFC Authoring & Validation Toolkit

Compiled from https://github.com/Impertio-Studio/Blender-Bonsai-ifcOpenshell-Sverchok-Claude-Skill-Package (MIT, OpenAEC Foundation) — the IfcOpenShell and cross-technology subset (15 of 73 skills); the Blender, Bonsai, and Sverchok skills are omitted. Requires the IfcOpenShell Python library.

## Router

| Skill | Use when |
|---|---|
| **Core** | |
| [ifcos-core-concepts](#ifcos-core-concepts) | Use when learning IFC data model fundamentals or navigating IFC entity relationships. Prevents the common mistake of creating flat element structures without proper spatial hierarchy (Project > Site > Building > Storey). Covers entity hierarchy from IfcRoot to IfcElement, spatial structure, ownership model, placement system, representation system, and relationships across IFC2X3, IFC4, and IFC4X3 schemas. |
| [ifcos-core-runtime](#ifcos-core-runtime) | Use when debugging IfcOpenShell crashes, entity reference errors, or performance issues. Prevents the common pitfall of comparing entities with == instead of checking .id() or identity, or holding references to entities after removal. Covers C++ binding behavior, entity invalidation, by_type() return semantics, thread safety, memory management, PascalCase attributes, and installation patterns. |
| **API syntax** | |
| [ifcos-syntax-api](#ifcos-syntax-api) | Use when writing IfcOpenShell Python code that creates, modifies, or deletes IFC entities. Prevents the #1 AI mistake: using create_entity() or direct attribute assignment instead of ifcopenshell.api.run(). Covers all 30+ API modules, invocation patterns, parameter conventions, and the difference between api.run() and direct module calls. |
| [ifcos-syntax-elements](#ifcos-syntax-elements) | Use when querying, traversing, or extracting data from IFC elements -- by_type, by_id, by_guid, inverse references, or property extraction. Prevents the common mistake of manually traversing relationships instead of using the universal property extraction pattern (IsDefinedBy -> HasProperties). Covers get_info(), is_a(), GUID utilities, and attribute access patterns. |
| [ifcos-syntax-fileio](#ifcos-syntax-fileio) | Use when opening, creating, writing, or serializing IFC files with IfcOpenShell. Prevents the common mistake of not using transactions for multi-step operations (no undo on failure). Covers ifcopenshell.open(), file.create(), file.write(), transaction management with undo/redo, and schema selection. |
| [ifcos-syntax-util](#ifcos-syntax-util) | Use when extracting data from IFC models using utility functions -- element properties, selector syntax, placement calculations, unit conversion, or cost/schedule data. Prevents the common mistake of manually parsing IFC relationships instead of using ifcopenshell.util helpers. Covers element utilities, selector syntax, placement helpers, date/unit conversion, and shape extraction. |
| **Implementation** | |
| [ifcos-impl-creation](#ifcos-impl-creation) | Use when building IFC models from scratch -- creating projects, spatial structure, walls, slabs, columns, openings, property sets, and type assignments. Prevents the critical mistake of skipping IfcOwnerHistory (required in IFC2X3) or not establishing spatial containment. Covers the complete creation workflow using ifcopenshell.api from project to element level. |
| [ifcos-impl-geometry](#ifcos-impl-geometry) | Use when extracting 3D geometry from IFC files, creating geometric representations, or processing IFC geometry for visualization. Prevents the performance mistake of calling create_shape() per element instead of using the geometry iterator. Covers geometry settings, create_shape(), geometry iterator, extrusion/CSG/BRep creation, and coordinate transforms. |
| [ifcos-impl-relationships](#ifcos-impl-relationships) | Use when managing IFC element relationships -- spatial containment, aggregation, type assignment, property association, material association, or void relationships. Prevents the common mistake of creating elements without establishing their spatial containment (orphaned elements). Covers relationship differences between IFC2X3 and IFC4. |
| [ifcos-impl-materials](#ifcos-impl-materials) | Use when assigning materials to IFC elements -- single materials, layer sets (walls), profile sets (beams/columns), or constituent sets (IFC4+). Prevents the common mistake of using IfcMaterialConstituentSet in IFC2X3 (not available). Covers IfcMaterial, IfcMaterialLayerSet, IfcMaterialProfileSet, material properties, and presentation. |
| [ifcos-impl-validation](#ifcos-impl-validation) | Use when validating IFC files for schema compliance, IDS conformance, or custom quality rules. Prevents the common mistake of only checking schema validity without verifying property set completeness or spatial hierarchy correctness. Covers ifcopenshell.validate, ifctester for IDS validation, georeference validation, and custom validation pipelines. |
| **Errors & QA** | |
| [ifcos-errors-schema](#ifcos-errors-schema) | Use when encountering IFC schema errors or migrating between IFC2X3, IFC4, and IFC4X3. Prevents the common mistake of using IFC4-only entities (e.g., IfcMaterialConstituentSet) in IFC2X3 files. Covers entity availability differences, attribute type changes, ifcpatch for schema migration, and common SchemaError debugging. |
| [ifcos-errors-performance](#ifcos-errors-performance) | Use when processing large IFC files (100MB+) or optimizing slow IfcOpenShell scripts. Prevents the #1 performance mistake: calling create_shape() per element instead of using the geometry iterator for batch processing. Covers geometry iterator, by_type caching, batch patterns, memory management, multiprocessing strategies, and profiling. |
| [ifcos-agents-code-validator](#ifcos-agents-code-validator) | Use when reviewing, validating, or auditing IfcOpenShell Python code for correctness. Runs systematic checks for schema compatibility errors, incorrect API usage (direct attribute modification vs api.run), entity reference invalidation, performance anti-patterns, and IFC standard compliance. Prevents shipping code that works on one schema but fails on another. |
| **Cross-tool workflows** | |
| [aec-core-bim-workflows](#aec-core-bim-workflows) | Use when implementing end-to-end BIM workflows that combine IfcOpenShell, Bonsai, and Blender -- such as IFC creation from scratch, model enrichment, validation pipelines, geometry extraction, or batch processing of building models. Prevents the common mistake of skipping unit and context setup before creating geometry, or directly modifying IFC attributes instead of using ifcopenshell.api.run(). Covers property set management across tools, spatial hierarchy patterns, and version compatibility for IFC2X3/IFC4/IFC4X3. |

---

# Core


## ifcos-core-concepts

> Use when learning IFC data model fundamentals or navigating IFC entity relationships. Prevents the common mistake of creating flat element structures without proper spatial hierarchy (Project > Site > Building > Storey). Covers entity hierarchy from IfcRoot to IfcElement, spatial structure, ownership model, placement system, representation system, and relationships across IFC2X3, IFC4, and IFC4X3 schemas.

## IFC Core Concepts

### Quick Reference

#### Entity Hierarchy Overview

```
IfcRoot (abstract) — GlobalId, OwnerHistory, Name, Description
├── IfcObjectDefinition (abstract)
│   ├── IfcObject (abstract)
│   │   ├── IfcProduct (abstract) — ObjectPlacement, Representation
│   │   │   ├── IfcSpatialElement [IFC4+] / IfcSpatialStructureElement [IFC2X3]
│   │   │   ├── IfcElement (abstract)
│   │   │   │   ├── IfcBuiltElement [IFC4X3] / IfcBuildingElement [IFC2X3/IFC4]
│   │   │   │   ├── IfcDistributionElement
│   │   │   │   ├── IfcFurnishingElement
│   │   │   │   └── ... (see references/methods.md)
│   │   │   ├── IfcAnnotation
│   │   │   └── IfcPort
│   │   ├── IfcProcess — IfcTask
│   │   ├── IfcResource
│   │   ├── IfcControl
│   │   └── IfcGroup
│   ├── IfcContext [IFC4+] / IfcObject [IFC2X3]
│   │   ├── IfcProject
│   │   └── IfcProjectLibrary [IFC4+]
│   └── IfcTypeObject
│       └── IfcTypeProduct → IfcElementType
├── IfcPropertyDefinition
│   ├── IfcPropertySet
│   └── IfcElementQuantity
└── IfcRelationship (abstract)
    ├── IfcRelDecomposes — IfcRelAggregates, IfcRelVoidsElement
    ├── IfcRelAssigns — assignments to actors, groups, processes
    ├── IfcRelConnects — IfcRelContainedInSpatialStructure, IfcRelFillsElement
    ├── IfcRelAssociates — IfcRelAssociatesMaterial, IfcRelAssociatesClassification
    ├── IfcRelDeclares — project/library declarations [IFC4+]
    └── IfcRelDefines — IfcRelDefinesByType, IfcRelDefinesByProperties
```

#### Critical Version Differences

| Concept | IFC2X3 | IFC4 | IFC4X3 |
|---------|--------|------|--------|
| IfcProject parent | IfcObject | IfcContext | IfcContext |
| OwnerHistory | MANDATORY | OPTIONAL | OPTIONAL |
| Spatial abstract parent | IfcSpatialStructureElement | IfcSpatialElement | IfcSpatialElement |
| Building element class | IfcBuildingElement | IfcBuildingElement | **IfcBuiltElement** (renamed) |
| StandardCase subtypes | Not present | Present (IfcWallStandardCase, etc.) | **REMOVED** |
| Infrastructure entities | Not present | Not present | IfcRoad, IfcBridge, IfcRailway, etc. |
| IfcFacility | Not present | Not present | Abstract parent of IfcBuilding |
| Door/Window type | IfcDoorStyle/IfcWindowStyle | IfcDoorType/IfcWindowType | IfcDoorType/IfcWindowType |
| IfcSpatialZone | Not present | Present | Present |
| IfcProjectLibrary | Not present | Present | Present |

#### IfcRoot Attributes (Present on ALL Named Entities)

Every entity inheriting from IfcRoot has these four attributes:

| Attribute | Type | IFC2X3 | IFC4+ |
|-----------|------|--------|-------|
| GlobalId | IfcGloballyUniqueId | REQUIRED | REQUIRED |
| OwnerHistory | IfcOwnerHistory | **REQUIRED** | **OPTIONAL** |
| Name | IfcLabel | OPTIONAL | OPTIONAL |
| Description | IfcText | OPTIONAL | OPTIONAL |

---

### Essential Patterns

#### 1. Spatial Structure Hierarchy

The spatial structure defines the physical organization of a project. ALWAYS build it top-down using `aggregate.assign_object`.

**IFC2X3 — Building-only hierarchy (RIGID):**
```
IfcProject → IfcSite → IfcBuilding → IfcBuildingStorey → IfcSpace
```

**IFC4 — Extended with zones:**
```
IfcProject → IfcSite → IfcBuilding → IfcBuildingStorey → IfcSpace
                                    + IfcSpatialZone (non-hierarchical overlays)
                                    + IfcExternalSpatialElement (outdoor)
```

**IFC4X3 — Infrastructure support (FLEXIBLE):**
```
IfcProject → IfcSite → IfcBuilding → IfcBuildingStorey → IfcSpace
                      → IfcRoad → IfcRoadPart
                      → IfcBridge → IfcBridgePart
                      → IfcRailway → IfcRailwayPart
                      → IfcFacility → IfcFacilityPart
```

```python
## IFC2X3/IFC4: Standard building hierarchy
## Schema: IFC2X3, IFC4
model = ifcopenshell.file(schema="IFC4")
project = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcProject", name="My Project")
site = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcSite", name="My Site")
building = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcBuilding", name="Building A")
storey = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcBuildingStorey", name="Ground Floor")

ifcopenshell.api.run("aggregate.assign_object", model, relating_object=project, products=[site])
ifcopenshell.api.run("aggregate.assign_object", model, relating_object=site, products=[building])
ifcopenshell.api.run("aggregate.assign_object", model, relating_object=building, products=[storey])
```

```python
## IFC4X3: Infrastructure hierarchy
## Schema: IFC4X3
model = ifcopenshell.file(schema="IFC4X3")
project = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcProject", name="Infra Project")
site = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcSite", name="Project Site")
road = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcRoad", name="Highway A1")
road_part = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcRoadPart", name="Segment 1")

ifcopenshell.api.run("aggregate.assign_object", model, relating_object=project, products=[site])
ifcopenshell.api.run("aggregate.assign_object", model, relating_object=site, products=[road])
ifcopenshell.api.run("aggregate.assign_object", model, relating_object=road, products=[road_part])
```

#### 2. Entity Inheritance and Type Checking

ALWAYS use `is_a()` for type checking. It traverses the full inheritance chain.

```python
## Schema: IFC2X3, IFC4, IFC4X3
wall = model.by_type("IfcWall")[0]
wall.is_a()              # Returns "IfcWall"
wall.is_a("IfcWall")     # True
wall.is_a("IfcElement")  # True (parent class)
wall.is_a("IfcProduct")  # True (grandparent)
wall.is_a("IfcRoot")     # True (ancestor)
wall.is_a("IfcSlab")     # False (different subtype)
```

NEVER compare `is_a()` return values as strings for inheritance checks:
```python
## WRONG: misses subtypes
if wall.is_a() == "IfcBuildingElement":  # Fails: wall.is_a() returns "IfcWall"

## CORRECT: checks full inheritance chain
if wall.is_a("IfcBuildingElement"):  # True for all building element subtypes
```

#### 3. Relationship Model (Objectified Relationships)

IFC uses objectified relationships — relationships are first-class IfcRoot entities with their own GlobalId. NEVER set relationships by assigning attributes directly.

**Key relationship types:**

| Relationship | Purpose | API Call |
|-------------|---------|----------|
| IfcRelAggregates | Whole/part decomposition (spatial hierarchy) | `aggregate.assign_object` |
| IfcRelContainedInSpatialStructure | Element-to-storey containment | `spatial.assign_container` |
| IfcRelDefinesByType | Type assignment (occurrence ↔ type) | `type.assign_type` |
| IfcRelDefinesByProperties | Property set assignment | `pset.add_pset` (auto-creates) |
| IfcRelAssociatesMaterial | Material assignment | `material.assign_material` |
| IfcRelVoidsElement | Opening in element | `void.add_opening` |
| IfcRelFillsElement | Door/window in opening | `void.add_filling` |
| IfcRelAssociatesClassification | Classification reference | `classification.add_reference` |

```python
## Schema: IFC2X3, IFC4, IFC4X3
## CORRECT: Use API to create relationships
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[wall])

## CORRECT: Query relationships via utility functions
container = ifcopenshell.util.element.get_container(wall)
element_type = ifcopenshell.util.element.get_type(wall)
material = ifcopenshell.util.element.get_material(wall)
psets = ifcopenshell.util.element.get_psets(wall)
```

#### 4. Ownership Model

Every IfcRoot entity references an IfcOwnerHistory that records who created/modified it.

**IFC2X3:** OwnerHistory is MANDATORY on all IfcRoot entities.
**IFC4/IFC4X3:** OwnerHistory is OPTIONAL.

```python
## Schema: IFC2X3: OwnerHistory REQUIRED
owner_history = ifcopenshell.api.run("owner.create_owner_history", model)
wall = model.createIfcWall(
    ifcopenshell.guid.new(),
    owner_history,  # REQUIRED — cannot be None
    "MyWall"
)

## Schema: IFC4, IFC4X3: OwnerHistory OPTIONAL
wall = model.createIfcWall(
    ifcopenshell.guid.new(),
    None,  # ALLOWED in IFC4+
    "MyWall"
)
```

ALWAYS use `ifcopenshell.api.run("root.create_entity", ...)` instead of direct `createIfc*` calls. The API handles OwnerHistory automatically based on schema version.

#### 5. Placement System

Every IfcProduct has an optional ObjectPlacement. Placements are relative to a parent placement, forming a placement tree.

```python
## Schema: IFC2X3, IFC4, IFC4X3
import numpy

## Set placement using 4x4 transformation matrix (identity = origin)
ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall, matrix=numpy.eye(4))

## Set placement relative to a container
ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall, matrix=numpy.array([
        [1.0, 0.0, 0.0, 5.0],   # X offset = 5.0
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]))
```

#### 6. Representation System

Geometric representation is assigned through representation contexts. ALWAYS create a context before assigning geometry.

```python
## Schema: IFC2X3, IFC4, IFC4X3
## Step 1: Create representation context
model3d = ifcopenshell.api.run("context.add_context", model, context_type="Model")
body_context = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW", parent=model3d)

## Step 2: Create representation
representation = ifcopenshell.api.run("geometry.add_wall_representation", model,
    context=body_context, length=5.0, height=3.0, thickness=0.2)

## Step 3: Assign representation to product
ifcopenshell.api.run("geometry.assign_representation", model,
    product=wall, representation=representation)
```

#### 7. Type Objects (Occurrence/Type Pattern)

IFC separates type definitions from occurrences. A type (e.g., IfcWallType) defines shared properties; occurrences (e.g., IfcWall) reference the type.

```python
## Schema: IFC2X3, IFC4, IFC4X3
## Create a type
wall_type = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWallType", name="Standard Wall 200mm")

## Assign type to occurrences
ifcopenshell.api.run("type.assign_type", model,
    related_objects=[wall1, wall2], relating_type=wall_type)

## Query type of an occurrence
element_type = ifcopenshell.util.element.get_type(wall1)

## Get all occurrences of a type
occurrences = ifcopenshell.util.element.get_types(wall_type)
```

**Version-specific type entity names:**

| Element | IFC2X3 Type | IFC4/IFC4X3 Type |
|---------|-------------|------------------|
| IfcDoor | IfcDoorStyle | IfcDoorType |
| IfcWindow | IfcWindowStyle | IfcWindowType |
| All others | IfcWallType, IfcSlabType, etc. | Same |

---

### Common Operations

#### Query All Elements by Type

```python
## Schema: IFC2X3, IFC4, IFC4X3
walls = model.by_type("IfcWall")           # All walls (tuple)
elements = model.by_type("IfcElement")     # ALL elements (includes subtypes)
products = model.by_type("IfcProduct")     # ALL products (elements + spatial + annotations)
```

#### Navigate Spatial Hierarchy

```python
## Schema: IFC2X3, IFC4, IFC4X3
import ifcopenshell.util.element

## Get the spatial container of an element
container = ifcopenshell.util.element.get_container(wall)  # Returns IfcBuildingStorey etc.

## Get all elements contained in a spatial structure
for rel in storey.ContainsElements:
    for element in rel.RelatedElements:
        print(f"{element.is_a()}: {element.Name}")

## Walk the spatial decomposition tree
for rel in building.IsDecomposedBy:
    for part in rel.RelatedObjects:
        print(f"{part.is_a()}: {part.Name}")  # Storeys
```

#### Read Properties

```python
## Schema: IFC2X3, IFC4, IFC4X3
import ifcopenshell.util.element

## Get all property sets as dict
psets = ifcopenshell.util.element.get_psets(wall)
## Returns: {'Pset_WallCommon': {'id': 42, 'IsExternal': True, 'FireRating': 'REI120'}}

## Get a specific property value
is_external = psets.get("Pset_WallCommon", {}).get("IsExternal")
```

#### Schema Version Detection

```python
## Schema: IFC2X3, IFC4, IFC4X3
model = ifcopenshell.open("building.ifc")
schema = model.schema  # Returns "IFC2X3", "IFC4", or "IFC4X3"

## Version-aware entity class selection
if schema == "IFC4X3":
    elements = model.by_type("IfcBuiltElement")
else:
    elements = model.by_type("IfcBuildingElement")
```

#### Detect Schema and Handle IfcBuiltElement/IfcBuildingElement

```python
## Schema: IFC2X3, IFC4, IFC4X3
def get_building_elements(model):
    """Get all building/built elements regardless of schema version."""
    schema = model.schema
    if schema == "IFC4X3":
        return model.by_type("IfcBuiltElement")
    return model.by_type("IfcBuildingElement")
```

#### Check Entity Existence in Schema

```python
## Schema: IFC2X3, IFC4, IFC4X3
import ifcopenshell.ifcopenshell_wrapper

schema_obj = ifcopenshell.ifcopenshell_wrapper.schema_by_name(model.schema)
try:
    entity = schema_obj.declaration_by_name("IfcRoad")
    print("IfcRoad exists in this schema")
except RuntimeError:
    print("IfcRoad does NOT exist in this schema")
```

---

### Reference Links

- **[references/methods.md](references/methods.md)** — Complete entity class reference with attributes per schema version
- **[references/examples.md](references/examples.md)** — Working code examples for entity traversal, spatial structure creation, property access, and relationship navigation
- **[references/anti-patterns.md](references/anti-patterns.md)** — Common IFC conceptual mistakes with explanations

#### Official Documentation

- IFC4X3 Documentation: https://ifc43-docs.standards.buildingsmart.org/
- buildingSMART IFC Standards: https://technical.buildingsmart.org/standards/ifc/
- IFC Schema Specifications: https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/


## ifcos-core-runtime

> Use when debugging IfcOpenShell crashes, entity reference errors, or performance issues. Prevents the common pitfall of comparing entities with == instead of checking .id() or identity, or holding references to entities after removal. Covers C++ binding behavior, entity invalidation, by_type() return semantics, thread safety, memory management, PascalCase attributes, and installation patterns.

## IfcOpenShell Python Runtime

### Quick Reference

#### Critical Warnings

- **ALWAYS** use `==` for entity comparison, NEVER `is`. Each query returns a new Python wrapper object.
- **ALWAYS** set entity references to `None` after calling `model.remove()`. The C++ object is deallocated regardless of Python reference count.
- **ALWAYS** keep a reference to the `ifcopenshell.file` object alive while any entities from it are in use. If the file is garbage-collected, all entity wrappers become dangling pointers (segfault).
- **NEVER** write to an `ifcopenshell.file` from multiple threads. The C++ backend has no locking. Concurrent writes corrupt the model or crash.
- **NEVER** iterate all entities and filter manually when `by_type()` exists. `by_type()` uses an internal index and is 10-100x faster.
- **NEVER** use `get_info(recursive=True)` on large models. It materializes the entire entity graph into memory.
- **ALWAYS** use named attribute access (`wall.Name`) instead of positional index access (`wall[2]`). Positional indices vary by entity type and schema version.
- **ALWAYS** check `model.schema` before accessing schema-specific attributes.

#### Decision Tree: Entity Reference Safety

```
Working with entity references?
├── Reading attributes?
│   ├── One attribute → entity.AttributeName (PascalCase)
│   ├── All attributes → entity.get_info() (returns dict)
│   └── Bulk read → entity.get_info(scalar_only=True) (faster)
│
├── Comparing entities?
│   ├── Same entity? → entity_a == entity_b (value equality)
│   ├── Same STEP ID? → entity_a.id() == entity_b.id()
│   └── NEVER use → entity_a is entity_b (always False)
│
├── Removing entities?
│   ├── With relationship cleanup → ifcopenshell.api.run("root.remove_product", model, product=entity)
│   ├── Low-level removal → model.remove(entity) (does NOT clean relationships)
│   └── After removal → entity_ref = None (ALWAYS nullify)
│
└── Storing references across operations?
    ├── Store entity.id() instead of the entity object
    ├── Re-fetch with model.by_id(stored_id) when needed
    └── NEVER cache entity objects across remove/undo operations
```

#### Decision Tree: Performance

```
Performance-critical operation?
├── Querying entities by type?
│   ├── Use model.by_type("IfcWall") → indexed, returns tuple
│   ├── First call builds index (slow), subsequent calls are instant
│   └── NEVER iterate all entities with manual is_a() filtering
│
├── Reading many attributes?
│   ├── Single entity → entity.get_info() (one C++ round-trip)
│   ├── Scalar values only → entity.get_info(scalar_only=True)
│   └── AVOID get_info(recursive=True) (massive memory allocation)
│
├── Bulk entity creation?
│   ├── < 100 entities → ifcopenshell.api.run() (safe, handles metadata)
│   ├── > 100 entities → model.create_entity() (5-10x faster, no undo tracking)
│   └── Bulk mode → handle GlobalId, OwnerHistory (IFC2X3) manually
│
└── Large model (500MB+ / 100k+ entities)?
    ├── Memory: ifcopenshell.open() loads ENTIRE file into RAM
    ├── Streaming: ifcopenshell.open(path, should_stream=True) (sequential only)
    ├── Parallel: open SEPARATE file instances per thread
    └── Cleanup: del model + gc.collect() to release C++ memory
```

---

### Essential Patterns

#### Pattern 1: C++ Binding Architecture

IfcOpenShell Python objects are thin wrappers around C++ objects managed by the `ifcopenshell_wrapper` module.

```python
## Schema-agnostic
import ifcopenshell

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

## Python wrapper delegates to C++ core
type(wall)                    # <class 'ifcopenshell.entity_instance'>
type(wall.wrapped_data)       # <class 'ifcopenshell_wrapper.entity_instance'>

## The wrapper holds a reference to its parent file
wall.file  # Returns the ifcopenshell.file object
```

**Key implication:** Python garbage collection does NOT control C++ memory. The C++ backend allocates and deallocates independently. Calling `model.remove(entity)` frees the C++ object immediately, even if Python references still exist.

#### Pattern 2: Entity Identity

```python
## Schema-agnostic
wall = model.by_type("IfcWall")[0]

## Two queries for the same entity return DIFFERENT Python wrapper objects
wall_a = model.by_id(wall.id())
wall_b = model.by_id(wall.id())

wall_a == wall_b    # True  — value equality via wrapped_data comparison
wall_a is wall_b    # False — different Python wrapper objects

## ALWAYS compare with == or by STEP ID
wall_a.id() == wall_b.id()  # True — same STEP ID (#42)
```

#### Pattern 3: Entity Invalidation After Removal

```python
## Schema-agnostic
wall = model.by_type("IfcWall")[0]
wall_id = wall.id()

## Low-level removal deallocates the C++ object
model.remove(wall)

## DANGER: accessing wall after removal causes undefined behavior
## wall.Name  → segfault or garbage data

## ALWAYS nullify references after removal
wall = None

## To re-check existence, query by ID
try:
    still_exists = model.by_id(wall_id)
except RuntimeError:
    still_exists = None  # Entity was removed

## PREFER API removal for products (cleans up relationships)
other_wall = model.by_type("IfcWall")[0]
ifcopenshell.api.run("root.remove_product", model, product=other_wall)
other_wall = None  # Still must nullify
```

#### Pattern 4: by_type() Return Semantics

```python
## Schema-agnostic
walls = model.by_type("IfcWall")

type(walls)   # <class 'tuple'> — NOT a list
len(walls)    # Number of IfcWall instances

## First call for a type builds an internal C++ index (slower)
## Subsequent calls for the same type use the cached index (instant)

## To mutate the result, convert to list
wall_list = list(walls)
wall_list.append(some_other_entity)

## Include subtypes (default behavior)
all_walls = model.by_type("IfcWall")  # Includes IfcWallStandardCase in IFC2X3/IFC4

## Exclude subtypes
only_walls = model.by_type("IfcWall", include_subtypes=False)
```

#### Pattern 5: PascalCase Attribute Access

```python
## Schema-agnostic
wall = model.by_type("IfcWall")[0]

## Named access: PascalCase matching the IFC schema
name = wall.Name                    # str or None
global_id = wall.GlobalId           # str (22-char encoded GUID)
description = wall.Description      # str or None
object_type = wall.ObjectType       # str or None
owner_history = wall.OwnerHistory   # entity_instance or None

## Positional access: fragile, varies by type and schema
name = wall[2]  # AVOID: index 2 = Name for IfcWall, but varies for other types

## Check if attribute has a value (IFC $null → Python None)
if wall.Description is not None:
    print(wall.Description)

## is_a() checks the full class hierarchy
wall.is_a("IfcWall")              # True
wall.is_a("IfcBuildingElement")   # True (parent class)
wall.is_a("IfcProduct")           # True (grandparent)
wall.is_a("IfcSlab")              # False

## get_info() returns all attributes as a dict
info = wall.get_info()
## {"id": 42, "type": "IfcWall", "GlobalId": "...", "Name": "...", ...}
```

#### Pattern 6: Thread Safety

```python
## Schema-agnostic

## SAFE: Read-only operations from multiple threads (no concurrent writes)
import concurrent.futures

def count_type(filepath, ifc_class):
    model = ifcopenshell.open(filepath)  # Separate instance per thread
    return len(model.by_type(ifc_class))

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {
        executor.submit(count_type, "model.ifc", cls): cls
        for cls in ["IfcWall", "IfcSlab", "IfcDoor"]
    }

## SAFE: Separate file instances per thread for writes
def process_copy(filepath, output_path):
    local_model = ifcopenshell.open(filepath)
    # Modify local_model freely — independent C++ instance
    local_model.write(output_path)

## UNSAFE: Multiple threads writing to the SAME model object
## This WILL corrupt data or crash: no C++ locks exist
```

#### Pattern 7: Memory Management for Large Models

```python
## Schema-agnostic
## Standard open loads entire file into memory
model = ifcopenshell.open("large_building.ifc")  # May use 4-8GB RAM

## Access specific attributes instead of materializing everything
name = wall.Name                                          # 1 attribute
material = ifcopenshell.util.element.get_material(wall)   # Targeted query

## AVOID: get_info(recursive=True) on large models
## deep_info = wall.get_info(recursive=True)  # Massive memory allocation

## Release a large model from memory
del model
import gc
gc.collect()  # Ensures Python wrappers are cleaned up and C++ memory freed
```

#### Pattern 8: File Lifecycle: Keep File Reference Alive

```python
## Schema-agnostic
## DANGEROUS: File reference lost while entities are in use
def get_walls():
    model = ifcopenshell.open("model.ifc")
    return model.by_type("IfcWall")  # model goes out of scope after return

walls = get_walls()
## model is garbage-collected → all entity wrappers are dangling pointers
## walls[0].Name  → SEGFAULT

## SAFE: Return both the model and the entities
def get_walls_safe():
    model = ifcopenshell.open("model.ifc")
    walls = model.by_type("IfcWall")
    return model, walls

model, walls = get_walls_safe()
walls[0].Name  # Safe — model reference kept alive
```

---

### Schema-Specific Attribute Differences

```python
## ALWAYS check schema before accessing schema-specific attributes
schema = model.schema  # "IFC2X3", "IFC4", "IFC4X3"

## Entities that differ by schema:
## IFC2X3/IFC4: IfcWallStandardCase exists
## IFC4X3: IfcWallStandardCase does NOT exist: use IfcWall

## IFC2X3: IfcDoorStyle, IfcWindowStyle
## IFC4+:  IfcDoorType, IfcWindowType

## IFC2X3: OwnerHistory is REQUIRED on rooted entities
## IFC4+:  OwnerHistory is OPTIONAL

## IFC4X3: IfcBuiltElement replaces IfcBuildingElement
## IFC4X3: New entities: IfcAlignment, IfcRoad, IfcBridge, IfcFacility

## Accessing a non-existent attribute raises AttributeError
try:
    pt = task.PredefinedType  # Exists in IFC4, not in IFC2X3
except AttributeError:
    pt = None
```

---

### Installation

#### pip (Recommended for Most Users)

```bash
pip install ifcopenshell
python -c "import ifcopenshell; print(ifcopenshell.version)"
```

- Pre-built wheels for Python 3.8-3.12 on Linux, macOS, Windows
- Package name is `ifcopenshell` (all lowercase)
- Bundles C++ core and OpenCASCADE dependencies

#### conda (Recommended for Complex Environments)

```bash
conda install -c conda-forge ifcopenshell
```

- Better dependency resolution for OpenCASCADE
- More up-to-date than pip releases

#### Blender Integration

```bash
## Bonsai addon bundles ifcopenshell: no separate install needed
## For standalone install into Blender's Python:
/path/to/blender/python/bin/python -m pip install ifcopenshell
```

#### Platform Notes

| Platform | Note |
|----------|------|
| Windows | pip works out-of-the-box. For Blender: install into Blender's Python. Watch for PATH conflicts. |
| macOS | Works on Intel and Apple Silicon. Use native arm64 Python, not Rosetta. |
| Linux | Works on most distributions. Headless/Docker: no GPU needed. |

---

### Version Detection

```python
import ifcopenshell

## Library version
ifcopenshell.version  # e.g., "0.8.1"

## Schema of an open file
model = ifcopenshell.open("model.ifc")
model.schema             # "IFC2X3", "IFC4", or "IFC4X3"
model.schema_identifier  # e.g., "IFC4_ADD2"
model.schema_version     # e.g., (4, 0, 2, 1)
```

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for entity_instance, file, by_type, remove, schema
- [Working Code Examples](references/examples.md) — End-to-end runtime patterns
- [Anti-Patterns](references/anti-patterns.md) — Common runtime mistakes and how to avoid them


---

# API syntax


## ifcos-syntax-api

> Use when writing IfcOpenShell Python code that creates, modifies, or deletes IFC entities. Prevents the #1 AI mistake: using create_entity() or direct attribute assignment instead of ifcopenshell.api.run(). Covers all 30+ API modules, invocation patterns, parameter conventions, and the difference between api.run() and direct module calls.

## IfcOpenShell API Module System

### Quick Reference

#### Critical Warnings

- **ALWAYS** use `ifcopenshell.api.run()` or direct module calls for IFC mutations. NEVER modify entity attributes directly (e.g., `wall.Name = "X"`) — use `api.run("attribute.edit_attributes", ...)` instead.
- **ALWAYS** import `ifcopenshell.api` before calling any API function. The module uses lazy loading; functions are NOT available without this import.
- **ALWAYS** pass the `file` (model) object as the first positional argument after the function name in `api.run()`.
- **NEVER** invent API module or function names. There are exactly 35 modules — see the module table below. Hallucinated calls like `api.run("element.create", ...)` or `api.run("wall.add", ...)` do NOT exist.
- **ALWAYS** use keyword arguments for all parameters after the model. Positional arguments beyond the model are NOT supported.
- **NEVER** use `model.create_entity()` for production code. Use `api.run("root.create_entity", ...)` — it generates GlobalIds, sets ownership, and validates predefined types automatically.
- **ALWAYS** set up a complete project before creating elements: IfcProject → units → contexts → spatial hierarchy. See the bootstrap pattern below.
- **NEVER** assume `products` parameters accept single elements. Since IfcOpenShell v0.8+, most relationship functions expect `products` as a **list**, not a single entity.

#### Decision Tree: Which API Module to Use

```
What do you need to do?
├── Create/remove/copy IFC entities?
│   └── root (create_entity, remove_product, copy_class, reassign_class)
│
├── Build spatial hierarchy?
│   ├── Project → Site → Building → Storey → Space?
│   │   └── aggregate (assign_object, unassign_object)
│   ├── Place elements in a storey/space?
│   │   └── spatial (assign_container, unassign_container)
│   └── Reference element in multiple spaces?
│       └── spatial (reference_structure, dereference_structure)
│
├── Add geometry to elements?
│   ├── Set up representation contexts first?
│   │   └── context (add_context — root context, then subcontexts)
│   ├── Parametric wall/slab/beam geometry?
│   │   └── geometry (add_wall_representation, add_slab_representation,
│   │       add_profile_representation)
│   ├── Custom mesh geometry?
│   │   └── geometry (add_mesh_representation)
│   ├── Position element in 3D space?
│   │   └── geometry (edit_object_placement)
│   └── Connect geometry to element?
│       └── geometry (assign_representation)
│
├── Set properties on elements?
│   ├── Key-value metadata (name, fire rating, etc.)?
│   │   └── pset (add_pset, edit_pset)
│   └── Measurable quantities (length, area, volume)?
│       └── pset (add_qto, edit_qto)
│
├── Assign materials?
│   ├── Simple single material?
│   │   └── material (add_material, assign_material)
│   ├── Layered construction (walls, slabs)?
│   │   └── material (add_material_set with IfcMaterialLayerSet, add_layer)
│   ├── Profiled sections (beams, columns)?
│   │   └── material (add_material_set with IfcMaterialProfileSet, add_profile)
│   └── Composite (windows, doors)?
│       └── material (add_material_set with IfcMaterialConstituentSet)
│
├── Assign/manage types?
│   └── type (assign_type, unassign_type, map_type_representations)
│
├── Edit entity attributes directly?
│   └── attribute (edit_attributes)
│
├── Create openings/voids?
│   └── void (add_opening, add_filling)
│
├── Set up units?
│   └── unit (assign_unit — defaults to SI)
│
├── Manage project file?
│   └── project (create_file)
│
└── Other domains?
    ├── Classification → classification
    ├── Groups → group
    ├── Layers (CAD) → layer
    ├── Visual styles → style
    ├── Cost management → cost
    ├── Scheduling (4D) → sequence
    ├── MEP systems → system
    ├── Structural analysis → structural
    ├── Documents → document
    ├── Constraints → constraint
    ├── Resources → resource
    ├── Owner/actors → owner
    ├── Profiles → profile
    ├── Nesting → nest
    ├── Boundaries → boundary
    ├── Libraries → library
    ├── Drawing/annotations → drawing
    ├── Georeference → georeference
    ├── Grid → grid
    ├── Infrastructure alignment → alignment
    ├── Coordinate geometry → cogo
    ├── Features → feature
    └── Property set templates → pset_template
```

---

### Essential Patterns

#### Pattern 1: Two Equivalent Invocation Styles

```python
## IfcOpenShell v0.8+: both styles produce identical results

import ifcopenshell
import ifcopenshell.api

model = ifcopenshell.file(schema="IFC4")

## Style A: api.run() with dot-notation string (original, most documented)
wall = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcWall", name="Wall 1")

## Style B: Direct module call (shorter, IDE-friendly)
wall = ifcopenshell.api.root.create_entity(model, ifc_class="IfcWall", name="Wall 1")
```

**ALWAYS** use one style consistently within a project. Both are correct. `api.run()` is more common in documentation and tutorials.

#### Pattern 2: Complete Project Bootstrap

```python
## IfcOpenShell: IFC4 (change version/schema for IFC2X3 or IFC4X3)
import ifcopenshell
import ifcopenshell.api

## Step 1: Create file with proper headers (production use)
model = ifcopenshell.api.run("project.create_file", version="IFC4")

## Step 2: Create project entity
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="My Project")

## Step 3: Assign units (defaults to SI metric)
ifcopenshell.api.run("unit.assign_unit", model)

## Step 4: Create representation contexts
model3d = ifcopenshell.api.run("context.add_context", model, context_type="Model")
body = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW", parent=model3d)

## Step 5: Build spatial hierarchy
site = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSite", name="Default Site")
building = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuilding", name="Building A")
storey = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Ground Floor")

ifcopenshell.api.run("aggregate.assign_object", model,
    products=[site], relating_object=project)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[building], relating_object=site)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[storey], relating_object=building)
```

**ALWAYS** follow this sequence: file → project → units → contexts → spatial hierarchy. Skipping steps produces invalid IFC files.

#### Pattern 3: Create Element with Full Data

```python
## IfcOpenShell: IFC4 (requires completed bootstrap above)

## Create wall type
wall_type = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWallType", name="Standard Wall 200mm")

## Add material to type (best practice: assign to types, not occurrences)
concrete = ifcopenshell.api.run("material.add_material", model,
    name="Concrete C30/37", category="concrete")
ifcopenshell.api.run("material.assign_material", model,
    products=[wall_type], material=concrete)

## Create wall occurrence
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 001")

## Assign type
ifcopenshell.api.run("type.assign_type", model,
    related_objects=[wall], relating_type=wall_type)

## Add geometry
representation = ifcopenshell.api.run("geometry.add_wall_representation", model,
    context=body, length=5.0, height=3.0, thickness=0.2)
ifcopenshell.api.run("geometry.assign_representation", model,
    product=wall, representation=representation)
ifcopenshell.api.run("geometry.edit_object_placement", model, product=wall)

## Place in spatial structure
ifcopenshell.api.run("spatial.assign_container", model,
    products=[wall], relating_structure=storey)

## Add properties
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={
    "IsExternal": True,
    "LoadBearing": True,
    "FireRating": "REI90",
    "ThermalTransmittance": 0.24,
})
```

---

### Complete API Module Table (35 Modules)

| Module | Category | Purpose | Key Functions |
|--------|----------|---------|---------------|
| `root` | Core | Create/remove/copy entities | `create_entity`, `remove_product`, `copy_class`, `reassign_class` |
| `spatial` | Spatial | Containment and referencing | `assign_container`, `unassign_container`, `reference_structure` |
| `aggregate` | Spatial | Hierarchical decomposition | `assign_object`, `unassign_object` |
| `geometry` | Geometry | Representations and placement | `add_wall_representation`, `add_mesh_representation`, `add_profile_representation`, `assign_representation`, `edit_object_placement` |
| `context` | Geometry | Representation contexts | `add_context`, `edit_context`, `remove_context` |
| `pset` | Properties | Property and quantity sets | `add_pset`, `edit_pset`, `add_qto`, `edit_qto` |
| `material` | Materials | Material definitions and sets | `add_material`, `assign_material`, `add_material_set`, `add_layer` |
| `type` | Types | Type definitions | `assign_type`, `unassign_type`, `map_type_representations` |
| `attribute` | Data | Direct attribute editing | `edit_attributes` |
| `unit` | Setup | Measurement units | `assign_unit`, `add_si_unit`, `add_conversion_based_unit` |
| `project` | Setup | Project file creation | `create_file`, `append_asset` |
| `owner` | Organization | Actors and roles | `add_person`, `add_organisation`, `set_user` |
| `classification` | Organization | Classification systems | `add_classification`, `add_reference` |
| `group` | Organization | Element grouping | `add_group`, `assign_group`, `unassign_group` |
| `void` | Geometry | Openings and voids | `add_opening`, `add_filling` |
| `style` | Visualization | Visual styles | `add_style`, `add_surface_style`, `assign_representation_styles` |
| `layer` | Visualization | CAD layers | `add_layer`, `assign_layer` |
| `profile` | Geometry | Cross-section profiles | `add_parameterised_profile`, `add_arbitrary_profile` |
| `cost` | Management | Cost scheduling | `add_cost_schedule`, `add_cost_item` |
| `sequence` | Management | Task scheduling (4D) | `add_work_schedule`, `add_task`, `edit_task_time` |
| `resource` | Management | Resource allocation | `add_resource`, `assign_resource` |
| `system` | MEP | Building systems | `add_system`, `assign_system` |
| `structural` | Engineering | Structural analysis | `add_structural_analysis_model`, `add_structural_member` |
| `document` | References | Document management | `add_information`, `assign_document` |
| `constraint` | Design | Design constraints | `add_objective`, `add_metric`, `assign_constraint` |
| `nest` | Organization | Nesting relationships | `assign_object`, `unassign_object` |
| `boundary` | Spatial | Space boundaries | `assign_connection_geometry` |
| `library` | References | Library references | `add_library`, `add_reference`, `assign_reference` |
| `drawing` | Visualization | Drawings/annotations | `add_drawing`, `add_annotation` |
| `georeference` | Location | Map coordinates | set coordinates, define projections |
| `grid` | Planning | Architectural grids | create, add axis |
| `feature` | Geometry | Geometric features | `add_feature` |
| `alignment` | Infrastructure | Road/rail alignment | `add_alignment` |
| `cogo` | Geometry | Coordinate geometry | calculate, transform |
| `pset_template` | Standards | Property set templates | create, assign |
| `control` | Relations | Control relationships | assign, establish |

---

### Common Operations

#### Edit Attributes Directly

```python
## IfcOpenShell: all schema versions
ifcopenshell.api.run("attribute.edit_attributes", model,
    product=wall, attributes={"Name": "Wall 001", "Description": "External bearing wall"})
```

#### Create and Assign Opening

```python
## IfcOpenShell: all schema versions
opening = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcOpeningElement", name="Door Opening")
ifcopenshell.api.run("void.add_opening", model, opening=opening, element=wall)

## Optionally fill with door
door = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcDoor", name="Door 001")
ifcopenshell.api.run("void.add_filling", model, opening=opening, element=door)
```

#### Assign Classification

```python
## IfcOpenShell: all schema versions
classification = ifcopenshell.api.run("classification.add_classification", model,
    classification="Uniclass 2015")
ifcopenshell.api.run("classification.add_reference", model,
    products=[wall], identification="Ss_20_10_30",
    name="Walls", classification=classification)
```

#### Add Visual Style

```python
## IfcOpenShell: all schema versions
style = ifcopenshell.api.run("style.add_style", model, name="Concrete Grey")
ifcopenshell.api.run("style.add_surface_style", model, style=style,
    attributes={"SurfaceColour": {"Red": 0.7, "Green": 0.7, "Blue": 0.7}})
ifcopenshell.api.run("style.assign_representation_styles", model,
    shape_representation=representation, styles=[style])
```

#### Safe Element Removal

```python
## IfcOpenShell: all schema versions
## ALWAYS use root.remove_product: it cleans up ALL relationships
ifcopenshell.api.run("root.remove_product", model, product=wall)
## NEVER use model.remove(wall) for products: it leaves dangling references
```

---

### Parameter Conventions

#### List Parameters (v0.8+ Breaking Change)

Since IfcOpenShell v0.8, relationship functions use **list** parameters:

```python
## CORRECT (v0.8+): products is a list
ifcopenshell.api.run("spatial.assign_container", model,
    products=[wall], relating_structure=storey)

## WRONG: single element (raises TypeError in v0.8+)
ifcopenshell.api.run("spatial.assign_container", model,
    product=wall, relating_structure=storey)  # KeyError: 'product'
```

Functions affected: `spatial.assign_container`, `aggregate.assign_object`, `type.assign_type`, `material.assign_material`, `group.assign_group`, `classification.add_reference`, `nest.assign_object`, and others.

#### Property Type Mapping (pset.edit_pset)

Python types map automatically to IFC property types:

| Python Type | IFC Type | Example |
|-------------|----------|---------|
| `str` | IfcLabel | `"REI60"` |
| `float` | IfcReal | `0.24` |
| `int` | IfcInteger | `3` |
| `bool` | IfcBoolean | `True` |
| `None` | (deletes property) | `None` |

#### Matrix Convention (geometry.edit_object_placement)

Placement uses a 4x4 NumPy transformation matrix:

```python
import numpy
## Identity matrix = origin, no rotation
ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall, matrix=numpy.eye(4))
```

**ALWAYS** set `is_si=True` (default) when providing coordinates in meters. Set `is_si=False` only when coordinates match the file's native unit system.

---

### Version Notes

#### Schema-Specific Entities

| Entity | IFC2X3 | IFC4 | IFC4X3 |
|--------|--------|------|--------|
| IfcBuildingStorey | Yes | Yes | Yes |
| IfcSpace | Yes | Yes | Yes |
| IfcFacility | No | No | Yes |
| IfcFacilityPart | No | No | Yes |
| IfcAlignment | No | No | Yes |
| IfcBridge | No | No | Yes |
| IfcRoad | No | No | Yes |

`api.run()` handles most schema differences internally. When creating IFC4X3 infrastructure models, use the infrastructure-specific entity classes.

#### project.create_file Parameter

```python
## CORRECT: parameter is "version" (not "schema")
model = ifcopenshell.api.run("project.create_file", version="IFC4")

## WRONG: "schema" is for ifcopenshell.file(), not project.create_file
model = ifcopenshell.api.run("project.create_file", schema="IFC4")  # Unexpected kwarg
```

---

### Dependency

This skill depends on **ifcos-syntax-fileio** for file creation, opening, writing, and transaction management patterns. Use ifcos-syntax-fileio for:
- `ifcopenshell.open()` / `ifcopenshell.file()`
- `model.write()` / `model.to_string()`
- Transaction management (`begin_transaction` / `end_transaction` / `undo` / `redo`)

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all 35 API modules
- [Working Code Examples](references/examples.md) — End-to-end examples per domain
- [Anti-Patterns](references/anti-patterns.md) — Common API mistakes and how to avoid them


## ifcos-syntax-elements

> Use when querying, traversing, or extracting data from IFC elements -- by_type, by_id, by_guid, inverse references, or property extraction. Prevents the common mistake of manually traversing relationships instead of using the universal property extraction pattern (IsDefinedBy -> HasProperties). Covers get_info(), is_a(), GUID utilities, and attribute access patterns.

## IfcOpenShell Element Traversal and Querying

### Quick Reference

#### Decision Tree: Finding Elements

```
Need to find IFC elements?
├── Know the IFC class? (IfcWall, IfcDoor, etc.)
│   └── model.by_type("IfcWall")
│       ├── Need subtypes included? → include_subtypes=True (DEFAULT)
│       └── Need exact type only? → include_subtypes=False
│
├── Know the STEP ID? (#123 in .ifc file)
│   └── model.by_id(123)
│       └── WARNING: STEP IDs are NOT persistent across re-exports
│
├── Know the GlobalId? (22-char IFC GUID)
│   └── model.by_guid("2O2Fr$t4X7Zf8NOew3FLOH")
│       └── GlobalId is ONLY on IfcRoot-derived entities
│
├── Need complex filtering? (by property, container, material)
│   └── ifcopenshell.util.selector.filter_elements(model, query)
│
└── Need ALL entities in the file?
    └── for entity in model: ...
```

#### Decision Tree: Reading Element Data

```
Need data from an element?
├── Single attribute? → element.Name, element.GlobalId, etc.
│
├── All attributes as dict? → element.get_info()
│   ├── Need referenced entities expanded? → get_info(recursive=True)
│   │   └── WARNING: EXPENSIVE on large models — avoid in loops
│   └── Need only primitive values? → get_info(scalar_only=True)
│
├── Type checking?
│   ├── Get type name → element.is_a()  # returns "IfcWall"
│   └── Check inheritance → element.is_a("IfcElement")  # returns True/False
│
├── Property sets?
│   ├── RECOMMENDED → ifcopenshell.util.element.get_psets(element)
│   └── Manual pattern → element.IsDefinedBy traversal (see below)
│
├── Spatial container? → ifcopenshell.util.element.get_container(element)
├── Element type? → ifcopenshell.util.element.get_type(element)
├── Material? → ifcopenshell.util.element.get_material(element)
└── STEP ID? → element.id()
```

#### Critical Warnings

- **ALWAYS** use `model.by_type()` for type-based queries — it is internally cached after the first call per type.
- **ALWAYS** use `ifcopenshell.guid.new()` to generate GlobalIds. NEVER construct GUID strings manually.
- **ALWAYS** use `ifcopenshell.util.element.get_psets()` for property extraction in production code. Use the manual `IsDefinedBy` traversal only when you need fine-grained control.
- **NEVER** use STEP IDs (`entity.id()`) as persistent identifiers. They change when files are re-exported. Use `GlobalId` for cross-session identification.
- **NEVER** call `get_info(recursive=True)` in a loop over many elements — it recursively expands all references and is extremely expensive.
- **NEVER** assume an entity has a `GlobalId`. Only `IfcRoot`-derived entities (IfcWall, IfcProject, etc.) have GlobalIds. Low-level entities (IfcCartesianPoint, IfcDirection) do NOT.
- **ALWAYS** handle `None` values when accessing optional attributes. Many IFC attributes are optional and return `None`.
- **ALWAYS** check `prop.NominalValue` is not `None` before accessing `.wrappedValue` in the property extraction pattern.

---

### Essential Patterns

#### Pattern 1: Query Elements by IFC Class

```python
## IfcOpenShell: all schema versions
import ifcopenshell

model = ifcopenshell.open("model.ifc")

## Get all walls (includes subtypes like IfcWallStandardCase in IFC2X3)
walls = model.by_type("IfcWall")

## Get ONLY exact IfcWall, NOT subtypes
walls_exact = model.by_type("IfcWall", include_subtypes=False)

## Common element queries
storeys = model.by_type("IfcBuildingStorey")
spaces = model.by_type("IfcSpace")
doors = model.by_type("IfcDoor")
windows = model.by_type("IfcWindow")
slabs = model.by_type("IfcSlab")
columns = model.by_type("IfcColumn")
beams = model.by_type("IfcBeam")
```

#### Pattern 2: Query by ID and GUID

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.guid

model = ifcopenshell.open("model.ifc")

## By STEP ID (the #123 number in .ifc files)
entity = model.by_id(123)

## By GlobalId (22-character IFC GUID)
entity = model.by_guid("2O2Fr$t4X7Zf8NOew3FLOH")

## Generate a new GlobalId
new_guid = ifcopenshell.guid.new()

## Convert between IFC GUID and standard UUID
standard_uuid = ifcopenshell.guid.expand(new_guid)   # → UUID string
ifc_guid = ifcopenshell.guid.compress(standard_uuid)  # → 22-char GUID
```

#### Pattern 3: Entity Attribute Access and Type Checking

```python
## IfcOpenShell: all schema versions
wall = model.by_type("IfcWall")[0]

## Direct attribute access
print(wall.Name)           # "Wall 001" or None
print(wall.GlobalId)       # "2O2Fr$t4X7Zf8NOew3FLOH"
print(wall.Description)    # Optional, may be None

## Type checking
wall.is_a()                # "IfcWall" (returns type name)
wall.is_a("IfcWall")       # True (exact match)
wall.is_a("IfcElement")    # True (parent class)
wall.is_a("IfcRoot")       # True (ancestor)
wall.is_a("IfcSlab")       # False

## STEP ID
wall.id()                  # 123 (integer)

## All attributes as dict
info = wall.get_info()
## {"id": 123, "type": "IfcWall", "GlobalId": "...", "Name": "...", ...}
```

#### Pattern 4: Inverse References

```python
## IfcOpenShell: all schema versions
wall = model.by_type("IfcWall")[0]

## Get ALL entities that REFERENCE this wall
inverse = model.get_inverse(wall)  # returns set

## Find which storey contains this wall
for rel in model.get_inverse(wall):
    if rel.is_a("IfcRelContainedInSpatialStructure"):
        print(f"Wall is in: {rel.RelatingStructure.Name}")

## Find property sets attached to an element
for rel in model.get_inverse(wall):
    if rel.is_a("IfcRelDefinesByProperties"):
        pset = rel.RelatingPropertyDefinition
        if pset.is_a("IfcPropertySet"):
            print(f"PSet: {pset.Name}")

## Find the type object of an element
for rel in model.get_inverse(wall):
    if rel.is_a("IfcRelDefinesByType"):
        print(f"Type: {rel.RelatingType.Name}")
```

#### Pattern 5: Universal IFC Property Extraction

This is the fundamental pattern for extracting properties from ANY IFC element. It traverses: `IsDefinedBy` → `IfcRelDefinesByProperties` → `IfcPropertySet` → `HasProperties` → `wrappedValue`.

```python
## IfcOpenShell: all schema versions
## UNIVERSAL PATTERN: Works with IfcOpenShell, Bonsai, web-ifc
def extract_properties(element):
    """Extract all property sets and their values from an IFC element."""
    result = {}
    for rel in element.IsDefinedBy:
        if rel.is_a("IfcRelDefinesByProperties"):
            pset = rel.RelatingPropertyDefinition
            if pset.is_a("IfcPropertySet"):
                props = {}
                for prop in pset.HasProperties:
                    if prop.is_a("IfcPropertySingleValue") and prop.NominalValue:
                        props[prop.Name] = prop.NominalValue.wrappedValue
                result[pset.Name] = props
    return result

wall = model.by_type("IfcWall")[0]
all_props = extract_properties(wall)
for pset_name, props in all_props.items():
    print(f"\n{pset_name}:")
    for name, value in props.items():
        print(f"  {name}: {value}")
```

#### Pattern 6: Recommended: Use util.element Helpers

```python
## IfcOpenShell: all schema versions
import ifcopenshell.util.element

wall = model.by_type("IfcWall")[0]

## Get ALL property sets as {pset_name: {prop_name: value}}
psets = ifcopenshell.util.element.get_psets(wall)

## Include quantity sets (IfcElementQuantity)
psets_and_qsets = ifcopenshell.util.element.get_psets(wall, psets_only=False)

## Get only quantity sets
qsets = ifcopenshell.util.element.get_psets(wall, qtos_only=True)

## Get element type
wall_type = ifcopenshell.util.element.get_type(wall)

## Get spatial container (typically IfcBuildingStorey)
container = ifcopenshell.util.element.get_container(wall)

## Get material
material = ifcopenshell.util.element.get_material(wall)

## Get all materials as list
materials = ifcopenshell.util.element.get_materials(wall)

## Get parent aggregate
parent = ifcopenshell.util.element.get_aggregate(wall)

## Get decomposition (children)
building = model.by_type("IfcBuilding")[0]
children = ifcopenshell.util.element.get_decomposition(building)
```

---

### Common Operations

#### Iterating Over All Entities

```python
## IfcOpenShell: all schema versions
## Iterate over ALL entities
for entity in model:
    pass

## Total entity count
total = len(model)

## Count entities by type
from collections import Counter
type_counts = Counter(entity.is_a() for entity in model)
for ifc_type, count in type_counts.most_common(20):
    print(f"  {ifc_type}: {count}")
```

#### Finding Openings in a Wall

```python
## IfcOpenShell: all schema versions
def get_openings(model, wall):
    """Get opening elements that void a wall."""
    openings = []
    for rel in model.get_inverse(wall):
        if rel.is_a("IfcRelVoidsElement"):
            openings.append(rel.RelatedOpeningElement)
    return openings
```

#### CSS-like Element Selection

```python
## IfcOpenShell: all schema versions
import ifcopenshell.util.selector

## Select walls by class
walls = ifcopenshell.util.selector.filter_elements(model, "IfcWall")

## Select by property value
ext_walls = ifcopenshell.util.selector.filter_elements(
    model, 'IfcWall, /Pset_WallCommon/.IsExternal = True')

## Select by container
ground_elements = ifcopenshell.util.selector.filter_elements(
    model, 'IfcBuildingElement, container="Ground Floor"')
```

#### Error Handling for Lookups

```python
## IfcOpenShell: all schema versions
## by_id and by_guid raise RuntimeError if not found
try:
    entity = model.by_id(999999)
except RuntimeError:
    print("Entity not found")

try:
    entity = model.by_guid("nonexistent_guid_12345")
except RuntimeError:
    print("Entity not found")

## by_type returns empty tuple if no matches
walls = model.by_type("IfcWall")  # () if none exist
```

---

### Version Notes

#### Schema-Specific Entity Names

| Concept | IFC2X3 | IFC4 | IFC4X3 |
|---------|--------|------|--------|
| Building elements parent | `IfcBuildingElement` | `IfcBuildingElement` | `IfcBuiltElement` |
| Spatial elements parent | `IfcSpatialStructureElement` | `IfcSpatialElement` | `IfcSpatialElement` |
| Wall subtype | `IfcWallStandardCase` | `IfcWall` (subtype removed) | `IfcWall` |
| Facility types | N/A | N/A | `IfcBridge`, `IfcRoad`, `IfcRailway`, `IfcMarineFacility` |

#### Query API Compatibility

The query methods (`by_type`, `by_id`, `by_guid`, `get_inverse`, `get_info`, `is_a`) are **schema-agnostic** — they work identically across IFC2X3, IFC4, and IFC4X3. Only the entity class names passed to these methods differ per schema.

#### GUID Module

`ifcopenshell.guid` is schema-independent. The same GUID format (22-character base64) is used across all IFC versions.

| Function | Purpose |
|----------|---------|
| `ifcopenshell.guid.new()` | Generate a new IFC GlobalId |
| `ifcopenshell.guid.expand(ifc_guid)` | Convert IFC GUID → standard UUID string |
| `ifcopenshell.guid.compress(uuid_str)` | Convert UUID string → 22-char IFC GUID |

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all element traversal methods
- [Working Code Examples](references/examples.md) — End-to-end examples for element queries and property extraction
- [Anti-Patterns](references/anti-patterns.md) — Common element traversal mistakes and how to avoid them


## ifcos-syntax-fileio

> Use when opening, creating, writing, or serializing IFC files with IfcOpenShell. Prevents the common mistake of not using transactions for multi-step operations (no undo on failure). Covers ifcopenshell.open(), file.create(), file.write(), transaction management with undo/redo, and schema selection.

## IfcOpenShell File I/O Operations

### Quick Reference

#### Decision Tree: Opening vs Creating IFC Files

```
Need an IFC model?
├── Existing file on disk?
│   └── YES → ifcopenshell.open("path/to/file.ifc")
│       ├── Large file (100MB+)? → use should_stream=True
│       └── Non-standard extension? → use format=".ifc"
│
└── NO → Create new file
    ├── Need header metadata, timestamps, MVD? (production use)
    │   └── YES → ifcopenshell.api.project.create_file(version="IFC4")
    │
    └── Need bare-minimum empty file? (testing, prototyping)
        └── ifcopenshell.file(schema="IFC4")
```

#### Decision Tree: Writing Output

```
Need to output IFC data?
├── Write to disk?
│   ├── Standard .ifc → model.write("output.ifc")
│   ├── XML format → model.write("output.ifcXML")
│   ├── Compressed → model.write("output.ifc", zipped=True)
│   └── ZIP archive → model.write("output.ifcZIP")
│
└── Get as string? → model.to_string()
```

#### Critical Warnings

- **ALWAYS** specify `schema=` explicitly when calling `ifcopenshell.file()`. The default is `"IFC4"` but relying on implicit defaults is error-prone.
- **ALWAYS** check `model.schema` after opening a file before using schema-specific entities.
- **NEVER** use `ifcopenshell.file()` for production IFC creation. Use `ifcopenshell.api.project.create_file()` instead — it sets up header metadata, timestamps, and MVD automatically.
- **NEVER** call `model.remove()` without understanding that references to the removed entity become null. Use `ifcopenshell.api.run("root.remove_product", ...)` for safe removal of products.
- **ALWAYS** wrap undo-able operations in `begin_transaction()` / `end_transaction()` pairs. NEVER leave a transaction open.
- **NEVER** call `undo()` or `redo()` while a transaction is active.

---

### Essential Patterns

#### Pattern 1: Open an Existing IFC File

```python
## IfcOpenShell: all schema versions
import ifcopenshell

model = ifcopenshell.open("/path/to/model.ifc")
print(model.schema)  # "IFC2X3", "IFC4", or "IFC4X3"
print(f"Entities: {len(model)}")
```

#### Pattern 2: Create a New IFC File (Production)

```python
## IfcOpenShell: IFC4 (change version= for IFC2X3 or IFC4X3)
import ifcopenshell
import ifcopenshell.api

model = ifcopenshell.api.run("project.create_file", version="IFC4")
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="My Project")
ifcopenshell.api.run("unit.assign_unit", model)
context = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW")
```

#### Pattern 3: Create a New IFC File (Bare Minimum)

```python
## IfcOpenShell: IFC4 (specify schema= for other versions)
import ifcopenshell

model = ifcopenshell.file(schema="IFC4")
## WARNING: This file has NO header, NO project, NO units.
## ALWAYS add at minimum: IfcProject, units, and a geometric context.
```

#### Pattern 4: Write IFC to Disk

```python
## IfcOpenShell: all schema versions
model.write("/path/to/output.ifc")

## Write as compressed ZIP
model.write("/path/to/output.ifc", zipped=True)

## Write as XML format
model.write("/path/to/output.ifcXML")
```

#### Pattern 5: Serialize IFC to String

```python
## IfcOpenShell: all schema versions
ifc_string = model.to_string()
```

#### Pattern 6: Transaction Management (Undo/Redo)

```python
## IfcOpenShell: all schema versions
model.begin_transaction()

wall = model.create_entity("IfcWall",
    GlobalId=ifcopenshell.guid.new(), Name="Test Wall")

model.end_transaction()

## Undo the transaction
model.undo()

## Redo the transaction
model.redo()
```

#### Pattern 7: Transfer Entity Between Files

```python
## IfcOpenShell: all schema versions
source = ifcopenshell.open("source.ifc")
target = ifcopenshell.file(schema=source.schema)

wall = source.by_type("IfcWall")[0]
target.add(wall)  # Recursively adds wall and all referenced entities
target.write("target.ifc")
```

#### Pattern 8: Remove Entity from File

```python
## IfcOpenShell: all schema versions
wall = model.by_type("IfcWall")[0]
model.remove(wall)
## WARNING: All attributes referencing this entity become null ($).
## Aggregate references (lists/sets) are cleaned up automatically.
```

---

### Common Operations

#### Opening Files

```python
## IfcOpenShell: all schema versions
import ifcopenshell

## Standard file open
model = ifcopenshell.open("building.ifc")

## Open ZIP-compressed IFC
model = ifcopenshell.open("building.ifcZIP")

## Open XML-format IFC
model = ifcopenshell.open("building.ifcXML")

## Force format when extension is non-standard
model = ifcopenshell.open("building.dat", format=".ifc")

## Streaming mode for large files (100MB+)
## WARNING: Only supports sequential iteration, NOT random access
model = ifcopenshell.open("huge_model.ifc", should_stream=True)
for entity in model:
    if entity.is_a("IfcWall"):
        print(entity.Name)
```

#### Creating Files

```python
## IfcOpenShell: IFC4 (change version/schema for other versions)
import ifcopenshell
import ifcopenshell.api

## RECOMMENDED: Production file with proper header
model = ifcopenshell.api.run("project.create_file", version="IFC4")

## Alternative: Bare empty file (testing only)
model = ifcopenshell.file(schema="IFC4")

## IFC2X3 file
model_legacy = ifcopenshell.file(schema="IFC2X3")

## IFC4X3 file (infrastructure projects)
model_infra = ifcopenshell.file(schema="IFC4X3")

## Specific schema sub-version
model_specific = ifcopenshell.file(schema_version=(4, 0, 2, 1))  # IFC4 ADD2 TC1
```

#### Writing Files

```python
## IfcOpenShell: all schema versions
## Standard STEP format
model.write("output.ifc")

## XML serialization
model.write("output.ifcXML")

## ZIP-compressed STEP
model.write("output.ifcZIP")

## STEP with additional ZIP compression
model.write("output.ifc", zipped=True)

## ZIP-compressed XML
model.write("output.ifcXML", format=".ifcXML", zipped=True)

## Serialize to string (no file written)
ifc_text = model.to_string()
```

#### Adding and Removing Entities

```python
## IfcOpenShell: all schema versions
import ifcopenshell

## Add entity from another file (copies entity + all dependencies)
source = ifcopenshell.open("source.ifc")
target = ifcopenshell.file(schema=source.schema)
wall = source.by_type("IfcWall")[0]
target.add(wall)

## Remove entity from file
model.remove(wall)
```

#### Transaction Management

```python
## IfcOpenShell: all schema versions

## Basic transaction
model.begin_transaction()
wall = model.create_entity("IfcWall",
    GlobalId=ifcopenshell.guid.new(), Name="New Wall")
model.end_transaction()

## Undo last transaction
model.undo()

## Redo undone transaction
model.redo()

## Discard transaction without recording
model.begin_transaction()
## ... experimental changes ...
model.discard_transaction()

## Set maximum undo history size (default: 64)
model.set_history_size(128)
```

#### Error Handling

```python
## IfcOpenShell: all schema versions
import ifcopenshell

try:
    model = ifcopenshell.open("model.ifc")
except FileNotFoundError:
    print("File not found")
except ifcopenshell.Error:
    print("Invalid or corrupt IFC file")
```

#### Accessing File Metadata

```python
## IfcOpenShell: all schema versions
model = ifcopenshell.open("model.ifc")

## Schema information
print(model.schema)             # "IFC2X3", "IFC4", or "IFC4X3"
print(model.schema_identifier)  # e.g., "IFC4_ADD2"
print(model.schema_version)     # e.g., (4, 0, 2, 1)

## Header information
print(model.header.file_description)
print(model.header.file_name)
print(model.header.file_schema)

## Entity count
print(len(model))
```

---

### Version Notes

#### Schema Parameter Differences

| Method | Parameter | Values |
|--------|-----------|--------|
| `ifcopenshell.file()` | `schema=` | `"IFC2X3"`, `"IFC4"`, `"IFC4X3"` |
| `ifcopenshell.api.project.create_file()` | `version=` | `"IFC2X3"`, `"IFC4"`, `"IFC4X3"` |

**ALWAYS** use the correct parameter name: `schema=` for `file()`, `version=` for `create_file()`.

#### `ifcopenshell.file()` vs `ifcopenshell.api.project.create_file()`

| Feature | `ifcopenshell.file()` | `api.project.create_file()` |
|---------|----------------------|----------------------------|
| Header metadata | Empty/minimal | Pre-populated (timestamp, app info) |
| Preprocessor | Not set | Set to "IfcOpenShell" |
| MVD | Not set | DesignTransferView default |
| Timestamp | Not set | Current timestamp |
| Use case | Testing, prototyping | Production IFC creation |

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all file I/O methods
- [Working Code Examples](references/examples.md) — End-to-end examples for all file operations
- [Anti-Patterns](references/anti-patterns.md) — Common file I/O mistakes and how to avoid them


## ifcos-syntax-util

> Use when extracting data from IFC models using utility functions -- element properties, selector syntax, placement calculations, unit conversion, or cost/schedule data. Prevents the common mistake of manually parsing IFC relationships instead of using ifcopenshell.util helpers. Covers element utilities, selector syntax, placement helpers, date/unit conversion, and shape extraction.

## IfcOpenShell Utility Modules (`ifcopenshell.util.*`)

### Quick Reference

#### Decision Tree: Choosing the Right Utility Module

```
What data do you need from an IFC element?
├── Property sets, types, containers, materials?
│   └── ifcopenshell.util.element
│       ├── get_psets()         → all property sets as dict
│       ├── get_pset()          → single property set or property
│       ├── get_type()          → type element (e.g., IfcWallType)
│       ├── get_container()     → spatial container (e.g., IfcBuildingStorey)
│       ├── get_material()      → material assignment
│       ├── get_materials()     → list of individual materials
│       ├── get_decomposition() → child elements
│       └── get_aggregate()     → parent aggregate
│
├── Query/filter elements by criteria?
│   └── ifcopenshell.util.selector
│       └── filter_elements()   → CSS-like query syntax
│
├── Position/coordinates?
│   └── ifcopenshell.util.placement
│       ├── get_local_placement() → 4x4 transformation matrix
│       └── get_storey_elevation() → storey Z elevation
│
├── Unit conversion?
│   └── ifcopenshell.util.unit
│       ├── calculate_unit_scale() → scale factor to SI metres
│       ├── convert()              → value between unit systems
│       └── get_project_unit()     → project's default unit
│
├── Dates, durations, timestamps?
│   └── ifcopenshell.util.date
│       ├── ifc2datetime()  → IFC date → Python datetime
│       └── datetime2ifc()  → Python datetime → IFC format
│
├── Geometry metrics (area, volume, bbox)?
│   └── ifcopenshell.util.shape (requires processed geometry)
│       ├── get_volume()    → element volume
│       ├── get_area()      → surface area
│       ├── get_bbox()      → bounding box
│       └── get_vertices()  → vertex coordinates
│
├── Classification references?
│   └── ifcopenshell.util.classification
│       ├── get_references() → classification refs for element
│       └── get_classification() → parent classification system
│
├── Cost data?
│   └── ifcopenshell.util.cost
│       ├── get_cost_items_for_product() → cost items linked to product
│       └── get_cost_values()            → cost item values
│
├── Schedule/sequence data?
│   └── ifcopenshell.util.sequence
│       ├── get_tasks_for_product() → tasks linked to product
│       └── count_working_days()    → working days between dates
│
└── Schema introspection (attribute types, enums)?
    └── ifcopenshell.util.attribute
        ├── get_primitive_type() → Python type for IFC attribute
        └── get_enum_items()    → enum options for attribute
```

#### Critical Warnings

- **ALWAYS** import utility modules explicitly: `import ifcopenshell.util.element`, NOT `from ifcopenshell.util import *`.
- **ALWAYS** multiply raw coordinate values by `calculate_unit_scale(model)` to get SI metres. IFC files store coordinates in project units (millimetres, feet, etc.).
- **ALWAYS** use `filter_elements()` (modern API) for selector queries. NEVER use the deprecated `Selector().parse()` class.
- **NEVER** traverse IFC inverse relationships manually when a `ifcopenshell.util.element` helper exists. Manual traversal is error-prone and schema-dependent.
- **NEVER** assume property set names are standardized. Custom property sets vary per project. ALWAYS check for `None` returns.
- **ALWAYS** check `model.schema` before using schema-specific property set names (e.g., `Pset_WallCommon` exists in IFC4 but attribute names differ from IFC2X3).
- **NEVER** call `ifcopenshell.util.shape` functions without first processing geometry via `ifcopenshell.geom`. Shape utilities operate on processed geometry objects, NOT raw IFC entities.

---

### Essential Patterns

#### Pattern 1: Extract All Properties from an Element

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.element

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

## All property sets (excludes quantity sets by default)
psets = ifcopenshell.util.element.get_psets(wall)
## Returns: {"Pset_WallCommon": {"id": 42, "IsExternal": True, ...}, ...}

## Include quantity sets
all_props = ifcopenshell.util.element.get_psets(wall, psets_only=False)

## Only quantity sets
qsets = ifcopenshell.util.element.get_psets(wall, qtos_only=True)

## Single property set by name
wall_common = ifcopenshell.util.element.get_pset(wall, "Pset_WallCommon")
## Returns dict or None

## Single property value
is_external = ifcopenshell.util.element.get_pset(
    wall, "Pset_WallCommon", "IsExternal")
## Returns value or None
```

#### Pattern 2: Navigate Element Relationships

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.element

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

## Type element (IfcWallType, IfcDoorType, etc.)
wall_type = ifcopenshell.util.element.get_type(wall)

## Spatial container (IfcBuildingStorey, IfcSpace, etc.)
container = ifcopenshell.util.element.get_container(wall)

## Material assignment
material = ifcopenshell.util.element.get_material(wall)

## Individual materials as flat list
materials = ifcopenshell.util.element.get_materials(wall)

## Parent aggregate
parent = ifcopenshell.util.element.get_aggregate(wall)

## Child elements (decomposition)
building = model.by_type("IfcBuilding")[0]
children = ifcopenshell.util.element.get_decomposition(building)
```

#### Pattern 3: Filter Elements with Selector Queries

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.selector

model = ifcopenshell.open("model.ifc")

## By IFC class
walls = ifcopenshell.util.selector.filter_elements(model, "IfcWall")

## Multiple classes
elements = ifcopenshell.util.selector.filter_elements(
    model, "IfcWall, IfcSlab")

## By attribute value
named = ifcopenshell.util.selector.filter_elements(
    model, 'IfcWall, Name="External Wall"')

## By property set value
external = ifcopenshell.util.selector.filter_elements(
    model, 'IfcWall, /Pset_WallCommon/.IsExternal = True')

## By spatial container
ground = ifcopenshell.util.selector.filter_elements(
    model, 'IfcBuildingElement, container="Ground Floor"')

## By material
concrete = ifcopenshell.util.selector.filter_elements(
    model, 'IfcElement, material="Concrete"')

## By type name
typed = ifcopenshell.util.selector.filter_elements(
    model, 'IfcWall, type="WT01"')

## Partial match (contains)
ext_walls = ifcopenshell.util.selector.filter_elements(
    model, 'IfcWall, Name *= "EXT"')

## Exclusion
non_slabs = ifcopenshell.util.selector.filter_elements(
    model, "! IfcSlab")
```

#### Pattern 4: Unit Conversion

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.unit

model = ifcopenshell.open("model.ifc")

## CRITICAL: Get scale factor from project units to SI metres
unit_scale = ifcopenshell.util.unit.calculate_unit_scale(model)
## Millimetres → 0.001, Metres → 1.0, Feet → 0.3048

## Convert raw coordinate to metres
raw_length = 5000.0  # e.g., value from IFC file in mm
length_metres = raw_length * unit_scale

## Get project's length unit entity
length_unit = ifcopenshell.util.unit.get_project_unit(model, "LENGTHUNIT")

## Convert between specific units
value_mm = ifcopenshell.util.unit.convert(
    value=1.0,
    from_prefix=None, from_unit="METRE",
    to_prefix="MILLI", to_unit="METRE"
)  # Returns 1000.0
```

#### Pattern 5: Get Element Placement

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.placement

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

## Get absolute 4x4 transformation matrix
matrix = ifcopenshell.util.placement.get_local_placement(
    wall.ObjectPlacement)
## Returns numpy 4x4 ndarray

## Extract position
x, y, z = matrix[0][3], matrix[1][3], matrix[2][3]

## Extract rotation (3x3 submatrix)
rotation = matrix[:3, :3]

## Storey elevation
storey = model.by_type("IfcBuildingStorey")[0]
elevation = ifcopenshell.util.placement.get_storey_elevation(storey)
```

#### Pattern 6: Date Conversion

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.date
from datetime import datetime

model = ifcopenshell.open("model.ifc")

## IFC timestamp → Python datetime
owner = model.by_type("IfcOwnerHistory")[0]
if owner.CreationDate:
    dt = ifcopenshell.util.date.ifc2datetime(owner.CreationDate)

## IFC date string → Python date
py_date = ifcopenshell.util.date.ifc2datetime("2024-06-15")

## IFC duration → Python timedelta
duration = ifcopenshell.util.date.ifc2datetime("P30D")

## Python datetime → IFC format
ifc_dt = ifcopenshell.util.date.datetime2ifc(
    datetime(2024, 6, 15, 10, 30), "IfcDateTime")
## Returns "2024-06-15T10:30:00"

ifc_date = ifcopenshell.util.date.datetime2ifc(
    datetime(2024, 6, 15), "IfcDate")
## Returns "2024-06-15"
```

---

### Common Operations

#### Classification Lookup

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.classification

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

refs = ifcopenshell.util.classification.get_references(wall)
for ref in refs:
    classification = ifcopenshell.util.classification.get_classification(ref)
    print(f"{classification.Name}: {ref.Identification} - {ref.Name}")
```

#### Cost Item Lookup

```python
## IfcOpenShell: IFC4/IFC4X3 (cost entities not in IFC2X3)
import ifcopenshell
import ifcopenshell.util.cost

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

cost_items = ifcopenshell.util.cost.get_cost_items_for_product(wall)
for item in cost_items:
    values = ifcopenshell.util.cost.get_cost_values(item)
    schedule = ifcopenshell.util.cost.get_cost_schedule(item)
```

#### Schedule Task Lookup

```python
## IfcOpenShell: IFC4/IFC4X3
import ifcopenshell
import ifcopenshell.util.sequence

model = ifcopenshell.open("model.ifc")

schedules = model.by_type("IfcWorkSchedule")
for schedule in schedules:
    for task in ifcopenshell.util.sequence.get_root_tasks(schedule):
        print(f"Task: {task.Name}")
        calendar = ifcopenshell.util.sequence.get_calendar(task)
        nested = ifcopenshell.util.sequence.get_nested_tasks(task)
```

#### Attribute Schema Introspection

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.attribute

## Get primitive Python type for an IFC attribute
schema = ifcopenshell.ifcopenshell_wrapper.schema_by_name("IFC4")
entity_decl = schema.declaration_by_name("IfcWall")
attr = entity_decl.all_attributes()[1]  # e.g., Name attribute
ptype = ifcopenshell.util.attribute.get_primitive_type(attr)

## Get enum options
enum_attr = entity_decl.all_attributes()[7]  # PredefinedType
items = ifcopenshell.util.attribute.get_enum_items(enum_attr)
```

#### Geometry Extraction (Requires Processed Shapes)

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape

model = ifcopenshell.open("model.ifc")
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

wall = model.by_type("IfcWall")[0]

## REQUIRED: Process geometry first
shape = ifcopenshell.geom.create_shape(settings, wall)

## Now use shape utilities
volume = ifcopenshell.util.shape.get_volume(shape.geometry)
area = ifcopenshell.util.shape.get_area(shape.geometry)
vertices = ifcopenshell.util.shape.get_vertices(shape.geometry)
bbox = ifcopenshell.util.shape.get_bbox(shape.geometry)
bottom_z = ifcopenshell.util.shape.get_bottom_elevation(shape.geometry)
top_z = ifcopenshell.util.shape.get_top_elevation(shape.geometry)
```

#### Copy/Duplicate Elements

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.element

model = ifcopenshell.open("model.ifc")
wall = model.by_type("IfcWall")[0]

## Shallow copy (new GlobalId, same relationships)
new_wall = ifcopenshell.util.element.copy(model, wall)

## Deep copy (copies element + directly related subelements)
deep_wall = ifcopenshell.util.element.copy_deep(model, wall)
```

---

### Selector Query Syntax Reference

| Syntax | Meaning | Example |
|--------|---------|---------|
| `IfcType` | Select by IFC class | `"IfcWall"` |
| `IfcType, IfcType` | Multiple classes | `"IfcWall, IfcSlab"` |
| `, Name="X"` | Filter by Name equals | `'IfcWall, Name="W01"'` |
| `, Name *= "X"` | Name contains | `'IfcWall, Name *= "EXT"'` |
| `, Name != None` | Attribute is not null | `'IfcWall, Name != None'` |
| `, /Pset/.Prop = val` | Filter by property value | `'IfcWall, /Pset_WallCommon/.IsExternal = True'` |
| `, type="X"` | Filter by type name | `'IfcWall, type="WT01"'` |
| `, container="X"` | Filter by spatial container | `'IfcElement, container="Level 1"'` |
| `, material="X"` | Filter by material | `'IfcElement, material="Concrete"'` |
| `! IfcType` | Exclude class | `"! IfcSlab"` |

---

### Module Summary Table

| Module | Import | Primary Functions | Schema Sensitivity |
|--------|--------|-------------------|--------------------|
| `element` | `ifcopenshell.util.element` | `get_psets`, `get_type`, `get_container`, `get_material` | Low — works across all schemas |
| `selector` | `ifcopenshell.util.selector` | `filter_elements`, `get_element_value` | Low — query syntax is schema-agnostic |
| `placement` | `ifcopenshell.util.placement` | `get_local_placement`, `get_storey_elevation` | Low — placement structure is consistent |
| `unit` | `ifcopenshell.util.unit` | `calculate_unit_scale`, `convert`, `get_project_unit` | Low — unit types are consistent |
| `date` | `ifcopenshell.util.date` | `ifc2datetime`, `datetime2ifc` | Medium — IfcCalendarDate is IFC2X3 only |
| `shape` | `ifcopenshell.util.shape` | `get_volume`, `get_area`, `get_bbox`, `get_vertices` | Low — operates on processed geometry |
| `classification` | `ifcopenshell.util.classification` | `get_references`, `get_classification` | Low |
| `cost` | `ifcopenshell.util.cost` | `get_cost_items_for_product`, `get_cost_values` | High — IFC4+ only |
| `sequence` | `ifcopenshell.util.sequence` | `get_root_tasks`, `count_working_days` | High — IFC4+ only |
| `attribute` | `ifcopenshell.util.attribute` | `get_primitive_type`, `get_enum_items` | Low — schema introspection |

---

### Version Notes

#### IFC2X3 Limitations
- `IfcCalendarDate` entity used instead of ISO 8601 date strings. Use `ifc2datetime()` which handles both.
- Cost scheduling entities (`IfcCostSchedule`, `IfcCostItem`) exist but with fewer attributes.
- `IfcTask` has a different attribute structure (no `TaskTime` in IFC2X3).

#### IFC4 vs IFC4X3
- IFC4X3 adds `IfcAlignment` and related entities supported by `ifcopenshell.util.alignment`.
- Property set names are consistent between IFC4 and IFC4X3 for building elements.

#### IfcOpenShell Version Notes
- `filter_elements()` replaced `Selector().parse()`. The `Selector` class is deprecated.
- `get_pset()` (singular) is a convenience wrapper added in recent versions. Falls back to `get_psets()` if unavailable.

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all utility functions
- [Working Code Examples](references/examples.md) — End-to-end examples for common scenarios
- [Anti-Patterns](references/anti-patterns.md) — Common utility module mistakes and how to avoid them


---

# Implementation


## ifcos-impl-creation

> Use when building IFC models from scratch -- creating projects, spatial structure, walls, slabs, columns, openings, property sets, and type assignments. Prevents the critical mistake of skipping IfcOwnerHistory (required in IFC2X3) or not establishing spatial containment. Covers the complete creation workflow using ifcopenshell.api from project to element level.

## IFC Model Creation Workflows

### Quick Reference

#### Decision Tree: Starting a New IFC Model

```
Creating a new IFC model?
├── Production model with proper header/metadata?
│   └── YES → model = ifcopenshell.api.run("project.create_file", version="IFC4")
│
└── Bare-minimum test file?
    └── model = ifcopenshell.file(schema="IFC4")
        └── WARNING: No header, no project, no units. Add these manually.
```

#### Decision Tree: Choosing IFC Schema Version

```
Which schema version?
├── Building/architecture project?
│   ├── Legacy compatibility needed? → IFC2X3
│   │   └── WARNING: OwnerHistory is REQUIRED on all rooted entities
│   └── Modern project? → IFC4
│
├── Infrastructure project (roads, bridges, tunnels)?
│   └── IFC4X3
│       └── Adds: IfcBridge, IfcRoad, IfcTunnel, IfcAlignment
│
└── Unsure? → Default to IFC4
```

#### Decision Tree: Element Creation Order

```
Building an IFC model from scratch?
Follow this EXACT order:

1. Create file         → project.create_file
2. Create IfcProject   → root.create_entity
3. Assign units        → unit.assign_unit
4. Add contexts        → context.add_context (Model + Body subcontext)
5. Create spatial hierarchy:
   a. IfcSite           → root.create_entity + aggregate.assign_object
   b. IfcBuilding       → root.create_entity + aggregate.assign_object
   c. IfcBuildingStorey  → root.create_entity + aggregate.assign_object
6. Create types (optional but recommended):
   a. IfcWallType etc.  → root.create_entity
   b. Assign materials  → material.add_material_set + material.assign_material
7. Create elements:
   a. Create entity     → root.create_entity
   b. Add geometry      → geometry.add_wall_representation (etc.)
   c. Assign geometry   → geometry.assign_representation
   d. Set placement     → geometry.edit_object_placement
   e. Assign container  → spatial.assign_container
   f. Assign type       → type.assign_type
8. Add properties       → pset.add_pset + pset.edit_pset
9. Write file          → model.write("output.ifc")
```

#### Critical Warnings

- **ALWAYS** use `ifcopenshell.api.run()` for entity creation. NEVER use `model.create_entity()` directly — the API handles GlobalId generation, OwnerHistory, and validation automatically.
- **ALWAYS** create the spatial hierarchy (Project → Site → Building → Storey) before creating physical elements. Elements without spatial containment are invisible in most BIM viewers.
- **ALWAYS** assign spatial containment via `spatial.assign_container` for physical elements (walls, slabs, columns, doors). Without containment, elements float in the model with no spatial context.
- **ALWAYS** set up geometric contexts (Model → Body subcontext) before creating geometry. Geometry without a context cannot be displayed.
- **ALWAYS** assign units via `unit.assign_unit` immediately after creating the project. Without units, all dimensions are ambiguous.
- **NEVER** skip `geometry.edit_object_placement` after creating an element. Without a placement, the element has no position in 3D space.
- **NEVER** create physical elements and types with mismatched IFC classes. An IfcWall occurrence MUST use IfcWallType, not IfcSlabType.
- **IFC2X3 ONLY**: OwnerHistory is REQUIRED on every rooted entity. The `root.create_entity` API handles this automatically, but ONLY if an owner/user has been set via `owner.set_user`. Call `owner.set_user` before creating any entities in IFC2X3.

---

### Essential Patterns

#### Pattern 1: Complete IFC4 Model from Scratch

```python
## IfcOpenShell: IFC4
import ifcopenshell
import ifcopenshell.api

## Step 1: Create file with proper header
model = ifcopenshell.api.run("project.create_file", version="IFC4")

## Step 2: Create project
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="My Project")

## Step 3: Assign SI units (meters, radians)
ifcopenshell.api.run("unit.assign_unit", model)

## Step 4: Set up geometric context
model3d = ifcopenshell.api.run("context.add_context", model,
    context_type="Model")
body = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW", parent=model3d)

## Step 5: Create spatial hierarchy
site = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSite", name="Default Site")
building = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuilding", name="Building A")
storey = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Ground Floor")

ifcopenshell.api.run("aggregate.assign_object", model,
    products=[site], relating_object=project)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[building], relating_object=site)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[storey], relating_object=building)

## Step 6: Create wall with geometry
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 001")
representation = ifcopenshell.api.run("geometry.add_wall_representation",
    model, context=body, length=5.0, height=3.0, thickness=0.2)
ifcopenshell.api.run("geometry.assign_representation", model,
    product=wall, representation=representation)
ifcopenshell.api.run("geometry.edit_object_placement", model, product=wall)
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[wall])

## Step 7: Add properties
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={
    "IsExternal": True,
    "LoadBearing": True,
    "FireRating": "REI90"
})

## Step 8: Write
model.write("output.ifc")
```

#### Pattern 2: IFC2X3 Model with Required OwnerHistory

```python
## IfcOpenShell: IFC2X3
import ifcopenshell
import ifcopenshell.api

## Create IFC2X3 file
model = ifcopenshell.api.run("project.create_file", version="IFC2X3")

## REQUIRED for IFC2X3: Set up owner BEFORE creating any entities
person = ifcopenshell.api.run("owner.add_person", model,
    identification="jdoe", family_name="Doe", given_name="John")
org = ifcopenshell.api.run("owner.add_organisation", model,
    identification="ACME", name="ACME Engineering")
user = ifcopenshell.api.run("owner.add_person_and_organisation", model,
    person=person, organisation=org)
application = ifcopenshell.api.run("owner.add_application", model)
ifcopenshell.api.run("owner.set_user", model, user=user)

## Now create entities: OwnerHistory is automatically attached
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="Legacy Project")
ifcopenshell.api.run("unit.assign_unit", model)

site = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSite", name="Site")
building = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuilding", name="Building")
storey = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Ground Floor")

ifcopenshell.api.run("aggregate.assign_object", model,
    products=[site], relating_object=project)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[building], relating_object=site)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[storey], relating_object=building)
```

#### Pattern 3: Spatial Hierarchy with Multiple Storeys

```python
## IfcOpenShell: IFC4
## After project, units, and contexts are set up:
site = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSite", name="Main Site")
building = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuilding", name="Office Block")

## Create multiple storeys
basement = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Basement")
ground = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Ground Floor")
first = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="First Floor")
roof = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Roof")

## Aggregate: Project → Site → Building → all storeys
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[site], relating_object=project)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[building], relating_object=site)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[basement, ground, first, roof], relating_object=building)

## Set storey elevations using object placement
import numpy as np
for storey_obj, elevation in [(basement, -3.0), (ground, 0.0),
                               (first, 3.5), (roof, 7.0)]:
    matrix = np.eye(4)
    matrix[2][3] = elevation  # Z translation = elevation
    ifcopenshell.api.run("geometry.edit_object_placement", model,
        product=storey_obj, matrix=matrix)
```

#### Pattern 4: Creating Elements with Type Assignment

```python
## IfcOpenShell: IFC4
## Create a wall type with material layers
wall_type = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWallType", name="WT-200 External")

## Set up material layers for the type
layer_set = ifcopenshell.api.run("material.add_material_set", model,
    name="WT-200", set_type="IfcMaterialLayerSet")
brick = ifcopenshell.api.run("material.add_material", model,
    name="Brick", category="brick")
insulation = ifcopenshell.api.run("material.add_material", model,
    name="Insulation", category="mineral wool")
plaster = ifcopenshell.api.run("material.add_material", model,
    name="Gypsum Plaster", category="gypsum")

layer1 = ifcopenshell.api.run("material.add_layer", model,
    layer_set=layer_set, material=brick)
ifcopenshell.api.run("material.edit_layer", model,
    layer=layer1, attributes={"LayerThickness": 0.102})
layer2 = ifcopenshell.api.run("material.add_layer", model,
    layer_set=layer_set, material=insulation)
ifcopenshell.api.run("material.edit_layer", model,
    layer=layer2, attributes={"LayerThickness": 0.080})
layer3 = ifcopenshell.api.run("material.add_layer", model,
    layer_set=layer_set, material=plaster)
ifcopenshell.api.run("material.edit_layer", model,
    layer=layer3, attributes={"LayerThickness": 0.018})

ifcopenshell.api.run("material.assign_material", model,
    products=[wall_type], type="IfcMaterialLayerSet", material=layer_set)

## Create wall occurrences and assign the type
wall1 = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 001")
wall2 = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 002")
ifcopenshell.api.run("type.assign_type", model,
    related_objects=[wall1, wall2], relating_type=wall_type)
```

#### Pattern 5: Creating Openings (Doors and Windows)

```python
## IfcOpenShell: IFC4
## Prerequisites: wall exists, body context exists, storey exists

## Create opening element
opening = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcOpeningElement", name="Door Opening")
opening_rep = ifcopenshell.api.run("geometry.add_wall_representation",
    model, context=body, length=0.9, height=2.1, thickness=0.2)
ifcopenshell.api.run("geometry.assign_representation", model,
    product=opening, representation=opening_rep)
ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=opening)

## Cut opening in wall (boolean subtraction)
ifcopenshell.api.run("void.add_opening", model,
    opening=opening, element=wall)

## Create door and fill the opening
door = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcDoor", name="Door 001")
ifcopenshell.api.run("void.add_filling", model,
    opening=opening, element=door)
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[door])
```

#### Pattern 6: Property Sets and Quantity Sets

```python
## IfcOpenShell: IFC4
## Add standard property set to wall
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={
    "Reference": "WT-200",
    "IsExternal": True,
    "LoadBearing": True,
    "FireRating": "REI60",
    "ThermalTransmittance": 0.28
})

## Add quantity set
qto = ifcopenshell.api.run("pset.add_qto", model,
    product=wall, name="Qto_WallBaseQuantities")
ifcopenshell.api.run("pset.edit_qto", model, qto=qto, properties={
    "Length": 5.0,
    "Height": 3.0,
    "Width": 0.2,
    "GrossSideArea": 15.0,
    "NetSideArea": 13.11,
    "GrossVolume": 3.0
})

## Custom property set (use project-specific prefix, NOT "Pset_")
custom_pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall, name="ACME_WallData")
ifcopenshell.api.run("pset.edit_pset", model, pset=custom_pset, properties={
    "CostCode": "STR-W-001",
    "InstallDate": "2026-03-15",
    "Inspector": "J. Doe"
})
```

#### Pattern 7: Slab and Column Creation

```python
## IfcOpenShell: IFC4
## Slab with polyline footprint
slab = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSlab", name="Floor Slab", predefined_type="FLOOR")
slab_rep = ifcopenshell.api.run("geometry.add_slab_representation", model,
    context=body, depth=0.25,
    polyline=[(0.0, 0.0), (10.0, 0.0), (10.0, 8.0), (0.0, 8.0)])
ifcopenshell.api.run("geometry.assign_representation", model,
    product=slab, representation=slab_rep)
ifcopenshell.api.run("geometry.edit_object_placement", model, product=slab)
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[slab])

## Column with profile
column = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcColumn", name="Column C1")
profile = ifcopenshell.api.run("profile.add_parameterised_profile", model,
    ifc_class="IfcRectangleProfileDef", XDim=0.3, YDim=0.3)
col_rep = ifcopenshell.api.run("geometry.add_profile_representation", model,
    context=body, profile=profile, depth=3.0)
ifcopenshell.api.run("geometry.assign_representation", model,
    product=column, representation=col_rep)
ifcopenshell.api.run("geometry.edit_object_placement", model, product=column)
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[column])
```

---

### Version Notes

#### IFC2X3 vs IFC4+ Entity Differences

| Feature | IFC2X3 | IFC4 / IFC4X3 |
|---------|--------|----------------|
| OwnerHistory | REQUIRED on all rooted entities | OPTIONAL |
| IfcWallStandardCase | EXISTS (use for layered walls) | DEPRECATED (use IfcWall with PredefinedType) |
| IfcBuildingStorey | Only valid spatial container | IfcBuildingStorey + IfcSpace + IfcFacility |
| Property set types | IfcPropertySingleValue only | Adds IfcPropertyBoundedValue, IfcPropertyTableValue |
| Material sets | IfcMaterialList (legacy) | IfcMaterialConstituentSet (preferred) |

#### IFC4X3 Infrastructure Entities (Not Available in IFC2X3/IFC4)

- `IfcBridge`, `IfcBridgePart`
- `IfcRoad`, `IfcRoadPart`
- `IfcRailway`, `IfcRailwayPart`
- `IfcTunnel`, `IfcTunnelPart`
- `IfcAlignment`, `IfcLinearElement`
- `IfcFacility`, `IfcFacilityPart`

#### Aggregation Hierarchy by Schema

| Schema | Standard Hierarchy |
|--------|-------------------|
| IFC2X3 | IfcProject → IfcSite → IfcBuilding → IfcBuildingStorey → IfcSpace |
| IFC4 | IfcProject → IfcSite → IfcBuilding → IfcBuildingStorey → IfcSpace |
| IFC4X3 | IfcProject → IfcSite → IfcFacility (or IfcBuilding/IfcBridge/IfcRoad) → IfcFacilityPart (or IfcBuildingStorey) → IfcSpace |

#### Type-to-Occurrence Mapping (Common Elements)

| Element Type | Occurrence Class | Notes |
|-------------|-----------------|-------|
| IfcWallType | IfcWall | IFC2X3: also IfcWallStandardCase |
| IfcSlabType | IfcSlab | Use predefined_type: FLOOR, ROOF, BASESLAB, LANDING |
| IfcColumnType | IfcColumn | |
| IfcBeamType | IfcBeam | |
| IfcDoorType | IfcDoor | IFC2X3: IfcDoorStyle (not IfcDoorType) |
| IfcWindowType | IfcWindow | IFC2X3: IfcWindowStyle (not IfcWindowType) |
| IfcCurtainWallType | IfcCurtainWall | |

---

### Common Operations

#### Set Up Geometric Contexts

```python
## IfcOpenShell: IFC4
## Root context (REQUIRED before any subcontexts)
model3d = ifcopenshell.api.run("context.add_context", model,
    context_type="Model")

## Body subcontext (REQUIRED for 3D solid geometry)
body = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW", parent=model3d)

## Optional: Axis subcontext (for wall/beam centerlines)
axis = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Axis",
    target_view="GRAPH_VIEW", parent=model3d)

## Optional: Plan context (for 2D representations)
plan = ifcopenshell.api.run("context.add_context", model,
    context_type="Plan")
plan_body = ifcopenshell.api.run("context.add_context", model,
    context_type="Plan", context_identifier="Body",
    target_view="PLAN_VIEW", parent=plan)
```

#### Position Elements with Transformation Matrix

```python
## IfcOpenShell: IFC4
import numpy as np

## Place wall at specific X, Y, Z coordinates
matrix = np.eye(4)
matrix[0][3] = 5.0   # X offset = 5 meters
matrix[1][3] = 2.0   # Y offset = 2 meters
matrix[2][3] = 0.0   # Z offset = 0 meters (ground level)

ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall, matrix=matrix)

## Rotate element 90 degrees around Z axis
import math
angle = math.radians(90)
rotation_matrix = np.array([
    [math.cos(angle), -math.sin(angle), 0, 0],
    [math.sin(angle),  math.cos(angle), 0, 0],
    [0,                0,               1, 0],
    [0,                0,               0, 1]
])
ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall, matrix=rotation_matrix)
```

#### Shared Property Sets Across Multiple Elements

```python
## IfcOpenShell: IFC4
## Create pset on first element
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall1, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={
    "IsExternal": True, "FireRating": "REI90"
})

## Share same pset with additional elements
ifcopenshell.api.run("pset.assign_pset", model,
    products=[wall1, wall2, wall3], pset=pset)
```

---

### Visual Alternative: IfcSverchok

For node-based visual IFC creation, use **IfcSverchok** (31 nodes). Key nodes: `SvIfcCreateProject`, `SvIfcCreateEntity`, `SvIfcApi`. Refer to: `sverchok-impl-ifcsverchok`

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all creation-related API methods
- [Working Code Examples](references/examples.md) — End-to-end model creation examples
- [Anti-Patterns](references/anti-patterns.md) — Common creation mistakes and how to avoid them


## ifcos-impl-geometry

> Use when extracting 3D geometry from IFC files, creating geometric representations, or processing IFC geometry for visualization. Prevents the performance mistake of calling create_shape() per element instead of using the geometry iterator. Covers geometry settings, create_shape(), geometry iterator, extrusion/CSG/BRep creation, and coordinate transforms.

## IfcOpenShell Geometry Processing & Creation

### Quick Reference

#### Decision Tree: Reading vs Creating Geometry

```
Need geometry from IFC elements?
├── Extract existing geometry? (read/process)
│   ├── Single element → ifcopenshell.geom.create_shape(settings, element)
│   ├── Multiple elements (100+) → ifcopenshell.geom.iterator(settings, model, cpu_count)
│   └── Specific entity attributes → Manual traversal (element.Representation)
│
└── Create new geometry? (write/author)
    ├── Simple wall block → geometry.add_wall_representation()
    ├── Extruded profile (beam/column) → geometry.add_profile_representation()
    ├── Arbitrary mesh (furniture/equipment) → geometry.add_mesh_representation()
    ├── Boolean operation (opening/cut) → geometry.add_boolean()
    ├── Custom parametric shape → ShapeBuilder + builder.get_representation()
    └── Slab/door/window/railing → geometry.add_{type}_representation()
```

#### Decision Tree: Tessellation vs BRep

```
What do you need the geometry for?
├── Visualization / rendering / game engine / export to mesh format
│   └── Tessellation (default) — triangulated mesh output
│       settings.set(settings.USE_BREP_DATA, False)  # default
│
├── CAD operations / boolean operations / precise measurements
│   └── BRep — exact OpenCASCADE TopoDS_Shape
│       settings.set(settings.USE_BREP_DATA, True)
│       Requires: pythonOCC (PythonOCC-Core) for advanced operations
│
└── Geometry export to glTF/OBJ
    └── Use serializer (ifcopenshell.geom.serializers)
```

#### Decision Tree: Local vs World Coordinates

```
What coordinate space?
├── Need absolute position in the model
│   └── USE_WORLD_COORDS = True
│       Vertices include full placement chain (element → storey → building → site)
│
├── Need position relative to element origin
│   └── USE_WORLD_COORDS = False (default)
│       Apply shape.transformation.matrix manually if needed
│
└── Need to compare positions across elements
    └── USE_WORLD_COORDS = True (ALWAYS for cross-element comparison)
```

#### Critical Warnings

- **ALWAYS** wrap `create_shape()` in try/except RuntimeError. Not all IfcProduct subtypes have geometry (IfcProject, IfcBuildingStorey, some IfcSite).
- **ALWAYS** use the iterator for processing 100+ elements. It is 5-10x faster than calling `create_shape()` in a loop due to internal caching and multithreading.
- **ALWAYS** set up a representation context before creating geometry. Call `context.add_context()` for the root 3D context, then a subcontext for Body/MODEL_VIEW.
- **ALWAYS** call `geometry.edit_object_placement()` on elements that have geometry. Elements without a placement are positioned at the global origin.
- **ALWAYS** apply unit scale when reading raw coordinate values from IFC entities. Use `ifcopenshell.util.unit.calculate_unit_scale(model)` to get the conversion factor to meters.
- **NEVER** assume geometry coordinates are in meters. Check the project units first.
- **NEVER** access `shape.geometry.verts` without checking that `create_shape()` did not raise an exception.
- **NEVER** create geometry representations without first having a context (IfcGeometricRepresentationSubContext with identifier="Body").
- **NEVER** use `model.create_entity("IfcExtrudedAreaSolid", ...)` for production code when `geometry.add_profile_representation()` or `geometry.add_wall_representation()` is available. The API functions handle context assignment, representation types, and validation automatically.

---

### Essential Patterns

#### Pattern 1: Configure Geometry Settings

```python
## IfcOpenShell: all schema versions
import ifcopenshell.geom

settings = ifcopenshell.geom.settings()

## Most common configuration for mesh extraction:
settings.set(settings.USE_WORLD_COORDS, True)   # Absolute coordinates
settings.set(settings.WELD_VERTICES, True)       # Clean mesh
settings.set(settings.USE_BREP_DATA, False)       # Triangulated output

## For BRep/CAD operations:
settings_brep = ifcopenshell.geom.settings()
settings_brep.set(settings_brep.USE_BREP_DATA, True)
settings_brep.set(settings_brep.USE_WORLD_COORDS, True)

## For fast preview (skip openings):
settings_fast = ifcopenshell.geom.settings()
settings_fast.set(settings_fast.DISABLE_OPENING_SUBTRACTIONS, True)
settings_fast.set(settings_fast.USE_WORLD_COORDS, True)
```

#### Pattern 2: Extract Single Element Geometry

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.geom
import numpy as np

model = ifcopenshell.open("model.ifc")
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

wall = model.by_type("IfcWall")[0]

try:
    shape = ifcopenshell.geom.create_shape(settings, wall)
except RuntimeError:
    print("No geometry or processing failed")
    shape = None

if shape:
    verts = np.array(shape.geometry.verts).reshape(-1, 3)
    faces = np.array(shape.geometry.faces).reshape(-1, 3)
    edges = np.array(shape.geometry.edges).reshape(-1, 2)
    print(f"Vertices: {len(verts)}, Triangles: {len(faces)}")
```

#### Pattern 3: Batch Process with Iterator

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.geom
import multiprocessing
import numpy as np

model = ifcopenshell.open("model.ifc")
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count())

if iterator.initialize():
    while True:
        shape = iterator.get()
        element = model.by_id(shape.id)
        verts = np.array(shape.geometry.verts).reshape(-1, 3)
        faces = np.array(shape.geometry.faces).reshape(-1, 3)
        # ... process geometry ...
        if not iterator.next():
            break
```

#### Pattern 4: Filtered Iterator

```python
## IfcOpenShell: all schema versions
## Process only walls
iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count(),
    include=model.by_type("IfcWall"))

## OR exclude spaces (invisible elements)
iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count(),
    exclude=model.by_type("IfcSpace"))

if iterator.initialize():
    while True:
        shape = iterator.get()
        # ... process ...
        if not iterator.next():
            break
```

#### Pattern 5: Create Representation Context (Required Before Any Geometry Creation)

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.api

model = ifcopenshell.api.run("project.create_file", version="IFC4")
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="My Project")
ifcopenshell.api.run("unit.assign_unit", model)

## Step 1: Root 3D context (REQUIRED)
model3d = ifcopenshell.api.run("context.add_context", model,
    context_type="Model")

## Step 2: Body subcontext (REQUIRED for geometry)
body = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW", parent=model3d)
```

#### Pattern 6: Create Wall Geometry

```python
## IfcOpenShell: all schema versions
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="W-01")

## Parametric wall: length=5m, height=3m, thickness=0.2m
wall_rep = ifcopenshell.api.run("geometry.add_wall_representation", model,
    context=body, length=5.0, height=3.0, thickness=0.2)

ifcopenshell.api.run("geometry.assign_representation", model,
    product=wall, representation=wall_rep)

## Set placement (identity = origin, or use a 4x4 matrix)
ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall)
```

#### Pattern 7: Create Profile Extrusion (Beam/Column)

```python
## IfcOpenShell: all schema versions
column = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcColumn", name="C-01")

## Create a rectangle profile
profile = model.create_entity("IfcRectangleProfileDef",
    ProfileType="AREA", XDim=0.3, YDim=0.3)

## Extrude the profile
col_rep = ifcopenshell.api.run("geometry.add_profile_representation", model,
    context=body, profile=profile, depth=3.0)

ifcopenshell.api.run("geometry.assign_representation", model,
    product=column, representation=col_rep)

ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=column)
```

#### Pattern 8: Create Mesh Geometry (Arbitrary Shape)

```python
## IfcOpenShell: all schema versions
element = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcFurniture", name="Table")

vertices = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],
            [0,0,0.8],[1,0,0.8],[1,1,0.8],[0,1,0.8]]
faces = [[0,1,2,3],[4,7,6,5],[0,4,5,1],[1,5,6,2],[2,6,7,3],[3,7,4,0]]

mesh_rep = ifcopenshell.api.run("geometry.add_mesh_representation", model,
    context=body, vertices=vertices, faces=faces)

ifcopenshell.api.run("geometry.assign_representation", model,
    product=element, representation=mesh_rep)

ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=element)
```

#### Pattern 9: Object Placement with Transformation Matrix

```python
## IfcOpenShell: all schema versions
import numpy as np
import ifcopenshell.util.placement

wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Rotated Wall")

## Start with identity matrix
matrix = np.eye(4)

## Rotate 90 degrees around Z axis
matrix = ifcopenshell.util.placement.rotation(90, "Z") @ matrix

## Set position: X=2, Y=3, Z=0
matrix[:, 3][0:3] = (2.0, 3.0, 0.0)

ifcopenshell.api.run("geometry.edit_object_placement", model,
    product=wall, matrix=matrix, is_si=True)
```

#### Pattern 10: Boolean Operations (CSG)

```python
## IfcOpenShell: all schema versions
## Create a wall with an opening (boolean subtraction)
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall with Opening")

wall_rep = ifcopenshell.api.run("geometry.add_wall_representation", model,
    context=body, length=5.0, height=3.0, thickness=0.2)

ifcopenshell.api.run("geometry.assign_representation", model,
    product=wall, representation=wall_rep)

## Create an opening element
opening = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcOpeningElement", name="Door Opening")

opening_rep = ifcopenshell.api.run("geometry.add_wall_representation", model,
    context=body, length=0.9, height=2.1, thickness=0.2)

ifcopenshell.api.run("geometry.assign_representation", model,
    product=opening, representation=opening_rep)

## Create void relationship (boolean subtraction)
ifcopenshell.api.run("void.add_opening", model,
    opening=opening, element=wall)
```

---

### Common Operations

For detailed code examples of these operations, see [Working Code Examples](references/examples.md):

- **Transformation matrix** — Extract and convert 4x3 column-major matrix from processed shapes
- **Material/style access** — Read diffuse color, transparency from shape.geometry.materials
- **ShapeBuilder** — Create custom geometry with rectangle/circle/polyline profiles + extrusion
- **glTF serialization** — Export IFC geometry to glTF/GLB using iterator + serializer
- **Shape helpers** — Use `ifcopenshell.util.shape` for grouped vertex/edge/face arrays

For complete settings and data structure tables, see [API Method Signatures](references/methods.md).

---

### Version Notes

- Geometry processing via `ifcopenshell.geom` is schema-agnostic. The same `create_shape()` and `iterator` calls work for IFC2X3, IFC4, and IFC4X3 files.
- Geometry creation via `ifcopenshell.api.geometry.*` is also schema-agnostic — the API handles schema differences internally.
- The `ShapeBuilder` utility (`ifcopenshell.util.shape_builder`) works across all schema versions.
- IFC4X3 adds alignment-based geometry (IfcLinearPlacement, IfcAlignment) not covered by the standard geometry API functions.
- BRep serialization to IFC depends on schema capabilities: IFC4+ supports more complex curved surfaces than IFC2X3.

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all geometry methods
- [Working Code Examples](references/examples.md) — End-to-end examples for geometry operations
- [Anti-Patterns](references/anti-patterns.md) — Common geometry mistakes and how to avoid them


## ifcos-impl-relationships

> Use when managing IFC element relationships -- spatial containment, aggregation, type assignment, property association, material association, or void relationships. Prevents the common mistake of creating elements without establishing their spatial containment (orphaned elements). Covers relationship differences between IFC2X3 and IFC4.

## IFC Relationship Management with IfcOpenShell

### Quick Reference

#### Decision Tree: Which Relationship Do I Need?

```
What are you connecting?
│
├── Spatial hierarchy (Project → Site → Building → Storey)?
│   └── Use aggregate.assign_object
│       └── Creates IfcRelAggregates
│
├── Element inside a spatial container (Wall in Storey)?
│   └── Use spatial.assign_container
│       └── Creates IfcRelContainedInSpatialStructure
│
├── Element referenced in (but not contained by) a spatial structure?
│   └── Use spatial.reference_structure
│       └── Creates IfcRelReferencedInSpatialStructure (IFC4+ only)
│
├── Type assignment (WallType → Wall occurrences)?
│   └── Use type.assign_type
│       └── Creates IfcRelDefinesByType
│
├── Property set on element?
│   └── Use pset.add_pset (creates IfcRelDefinesByProperties automatically)
│
├── Material on element?
│   └── Use material.assign_material
│       └── Creates IfcRelAssociatesMaterial
│
├── Opening/void in element (hole in wall)?
│   └── Use void.add_opening
│       └── Creates IfcRelVoidsElement
│
├── Filling an opening (door in hole)?
│   └── Use void.add_filling
│       └── Creates IfcRelFillsElement
│
├── Nesting (component attached to host at connection point)?
│   └── Use nest.assign_object
│       └── Creates IfcRelNests
│
├── Physical assembly (stair = flights + landings + railings)?
│   └── Use aggregate.assign_object
│       └── Creates IfcRelAggregates
│
└── Grouping (logical set, e.g. "External Walls")?
    └── Use group.assign_group
        └── Creates IfcRelAssignsToGroup
```

#### Critical Warnings

- **ALWAYS** use `ifcopenshell.api.run()` to create relationships. NEVER create relationship entities directly with `model.create_entity("IfcRelAggregates", ...)` — the API handles GlobalId generation, OwnerHistory, placement recalculation, and cleanup of prior relationships.
- **NEVER** assign attributes directly to set relationship properties. IFC uses objectified relationships — relationships are first-class entities.
- **ALWAYS** check `model.schema` before using schema-specific inverse attributes. `IsTypedBy` exists only in IFC4+; in IFC2X3, type relations are in `IsDefinedBy`.
- **NEVER** contain an element in multiple spatial structures. Each element has exactly ONE spatial container via `IfcRelContainedInSpatialStructure`. Use `spatial.reference_structure` for secondary references.
- **ALWAYS** use `ifcopenshell.util.element` for querying relationships. It handles version differences internally.

---

### Relationship Entity Hierarchy

```
IfcRelationship (abstract)
├── IfcRelDecomposes (abstract)
│   ├── IfcRelAggregates          ← aggregate.assign_object
│   ├── IfcRelNests               ← nest.assign_object
│   ├── IfcRelProjectsElement
│   └── IfcRelVoidsElement        ← void.add_opening
├── IfcRelAssigns (abstract)
│   ├── IfcRelAssignsToGroup      ← group.assign_group
│   └── ... (Actor, Control, Process, Product, Resource)
├── IfcRelAssociates (abstract)
│   ├── IfcRelAssociatesMaterial  ← material.assign_material
│   └── ... (Classification, Document, Library, etc.)
├── IfcRelConnects (abstract)
│   ├── IfcRelContainedInSpatialStructure  ← spatial.assign_container
│   ├── IfcRelFillsElement        ← void.add_filling
│   └── ... (Ports, Structural, Space Boundary, etc.)
├── IfcRelDeclares (IFC4+)
└── IfcRelDefines (abstract)
    ├── IfcRelDefinesByProperties  ← pset.add_pset (automatic)
    └── IfcRelDefinesByType        ← type.assign_type
```

---

### Version Differences: Relationship Splits Between IFC2X3 and IFC4

#### Inverse Attribute Changes

| Query | IFC2X3 | IFC4 / IFC4X3 |
|-------|--------|----------------|
| Type of element | `element.IsDefinedBy` → filter for `IfcRelDefinesByType` | `element.IsTypedBy` (dedicated inverse) |
| Type's inverse | `type.ObjectTypeOf` | `type.Types` (renamed) |
| Aggregation children | `obj.IsDecomposedBy` → returns `IfcRelDecomposes` | `obj.IsDecomposedBy` → returns `IfcRelAggregates` only |
| Nesting children | `obj.IsDecomposedBy` → filter for `IfcRelNests` | `obj.IsNestedBy` (dedicated inverse, IFC4+) |

#### Entity Classification Changes

| Aspect | IFC2X3 | IFC4+ |
|--------|--------|-------|
| `IfcRelVoidsElement` parent | `IfcRelDecomposes` | `IfcRelDecomposes` (unchanged) |
| `IfcRelProjectsElement` parent | `IfcRelDecomposes` | `IfcRelDecomposes` (unchanged) |
| `IfcRelReferencedInSpatialStructure` | Does not exist | Available |
| `IfcRelDeclares` | Does not exist | Available |
| `IfcRelDefinesByObject` | Does not exist | Available |
| `IfcRelAssignsToGroupByFactor` | Does not exist | Available |
| `IfcRelInterferesElements` | Does not exist | Available |
| `IfcRelPositions` | Does not exist | IFC4X3 only |

#### Valid Spatial Containers Per Version

| Container Entity | IFC2X3 | IFC4 | IFC4X3 |
|------------------|--------|------|--------|
| IfcSite | YES | YES | YES |
| IfcBuilding | YES | YES | YES |
| IfcBuildingStorey | YES | YES | YES |
| IfcSpace | YES | YES | YES |
| IfcExternalSpatialElement | — | YES | YES |
| IfcFacility (IfcBridge, IfcRoad, etc.) | — | — | YES |
| IfcFacilityPart (IfcRoadPart, etc.) | — | — | YES |

#### Material Types Per Version

| Material Concept | IFC2X3 | IFC4+ |
|-----------------|--------|-------|
| IfcMaterial | YES | YES |
| IfcMaterialLayerSet | YES | YES |
| IfcMaterialLayerSetUsage | YES | YES |
| IfcMaterialProfileSet | — | YES |
| IfcMaterialProfileSetUsage | — | YES |
| IfcMaterialConstituentSet | — | YES |
| IfcMaterialList | YES | YES (deprecated) |

#### Type Entity Changes

| IFC2X3 | IFC4+ Replacement |
|--------|-------------------|
| IfcDoorStyle | IfcDoorType |
| IfcWindowStyle | IfcWindowType |

---

### Essential Patterns

#### Pattern 1: Build Spatial Hierarchy (Aggregation)

```python
## IfcOpenShell: IFC4
import ifcopenshell
import ifcopenshell.api

model = ifcopenshell.api.run("project.create_file", version="IFC4")
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="My Project")
ifcopenshell.api.run("unit.assign_unit", model)

site = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSite", name="Site")
building = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuilding", name="Building")
storey = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Ground Floor")

## Each call creates an IfcRelAggregates
ifcopenshell.api.run("aggregate.assign_object", model,
    relating_object=project, products=[site])
ifcopenshell.api.run("aggregate.assign_object", model,
    relating_object=site, products=[building])
ifcopenshell.api.run("aggregate.assign_object", model,
    relating_object=building, products=[storey])
```

#### Pattern 2: Contain Elements in Spatial Structure

```python
## IfcOpenShell: all schema versions
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 001")

## Creates IfcRelContainedInSpatialStructure
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[wall])
```

#### Pattern 3: Assign Type to Occurrences

```python
## IfcOpenShell: IFC4
wall_type = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWallType", name="Standard Wall 200mm")

## Creates IfcRelDefinesByType
ifcopenshell.api.run("type.assign_type", model,
    related_objects=[wall], relating_type=wall_type)
```

#### Pattern 4: Add Property Set

```python
## IfcOpenShell: all schema versions
## pset.add_pset creates IfcRelDefinesByProperties automatically
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model,
    pset=pset, properties={
        "IsExternal": True,
        "FireRating": "REI120",
        "ThermalTransmittance": 0.24
    })
```

#### Pattern 5: Assign Material

```python
## IfcOpenShell: all schema versions
material = ifcopenshell.api.run("material.add_material", model,
    name="Concrete")

## Creates IfcRelAssociatesMaterial
ifcopenshell.api.run("material.assign_material", model,
    products=[wall], material=material)
```

#### Pattern 6: Create Opening and Fill It

```python
## IfcOpenShell: all schema versions
opening = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcOpeningElement", name="Door Opening")

## Creates IfcRelVoidsElement
ifcopenshell.api.run("void.add_opening", model,
    opening=opening, element=wall)

door = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcDoor", name="Door 001")

## Creates IfcRelFillsElement
ifcopenshell.api.run("void.add_filling", model,
    opening=opening, element=door)
```

#### Pattern 7: Nest Components

```python
## IfcOpenShell: all schema versions
sink = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSanitaryTerminal", name="Kitchen Sink")
faucet = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcValve", name="Faucet")

## Creates IfcRelNests: faucet is nested in sink
ifcopenshell.api.run("nest.assign_object", model,
    related_objects=[faucet], relating_object=sink)
```

---

### Querying Relationships

#### Version-Safe Queries Using ifcopenshell.util.element

```python
## IfcOpenShell: all schema versions
import ifcopenshell.util.element

## Get spatial container of element
container = ifcopenshell.util.element.get_container(wall)

## Get type of element
element_type = ifcopenshell.util.element.get_type(wall)

## Get all occurrences of a type
occurrences = ifcopenshell.util.element.get_types(wall_type)

## Get property sets
psets = ifcopenshell.util.element.get_psets(wall)
## Returns: {"Pset_WallCommon": {"IsExternal": True, ...}}

## Get material
material = ifcopenshell.util.element.get_material(wall)

## Get full decomposition tree
children = ifcopenshell.util.element.get_decomposition(building)

## Get aggregate parent
parent = ifcopenshell.util.element.get_aggregate(storey)
```

#### Direct Inverse Attribute Queries

```python
## IfcOpenShell: IFC4+
## Aggregation children
for rel in building.IsDecomposedBy:
    for child in rel.RelatedObjects:
        print(f"Child: {child.Name}")

## Aggregation parent
for rel in storey.Decomposes:
    print(f"Parent: {rel.RelatingObject.Name}")

## Spatial containment
for rel in storey.ContainsElements:
    for elem in rel.RelatedElements:
        print(f"Contains: {elem.is_a()} - {elem.Name}")

## Element's container
for rel in wall.ContainedInStructure:
    print(f"In: {rel.RelatingStructure.Name}")

## Type assignment (IFC4+)
for rel in wall.IsTypedBy:
    print(f"Type: {rel.RelatingType.Name}")

## Openings
for rel in wall.HasOpenings:
    opening = rel.RelatedOpeningElement
    for fill in opening.HasFillings:
        print(f"Filled by: {fill.RelatedBuildingElement.Name}")

## Property sets
for rel in wall.IsDefinedBy:
    if rel.is_a("IfcRelDefinesByProperties"):
        pset = rel.RelatingPropertyDefinition
        print(f"PSet: {pset.Name}")

## Material
for rel in wall.HasAssociations:
    if rel.is_a("IfcRelAssociatesMaterial"):
        print(f"Material: {rel.RelatingMaterial.is_a()}")

## Nesting (IFC4+)
for rel in sink.IsNestedBy:
    for child in rel.RelatedObjects:
        print(f"Nested: {child.Name}")
```

#### IFC2X3 Inverse Attribute Differences

```python
## IfcOpenShell: IFC2X3 ONLY
## Type assignment: NO IsTypedBy inverse in IFC2X3
for rel in wall.IsDefinedBy:
    if rel.is_a("IfcRelDefinesByType"):
        print(f"Type: {rel.RelatingType.Name}")

## Aggregation/Nesting: shared inverse in IFC2X3
for rel in building.IsDecomposedBy:
    # Returns IfcRelDecomposes instances (includes both aggregation and nesting)
    if rel.is_a("IfcRelAggregates"):
        for child in rel.RelatedObjects:
            print(f"Aggregated: {child.Name}")
    elif rel.is_a("IfcRelNests"):
        for child in rel.RelatedObjects:
            print(f"Nested: {child.Name}")
```

---

### Removing Relationships

```python
## IfcOpenShell: all schema versions

## Remove spatial containment
ifcopenshell.api.run("spatial.unassign_container", model, products=[wall])

## Remove aggregation
ifcopenshell.api.run("aggregate.unassign_object", model, products=[storey])

## Remove type assignment
ifcopenshell.api.run("type.unassign_type", model, related_objects=[wall])

## Remove material assignment
ifcopenshell.api.run("material.unassign_material", model, products=[wall])

## Remove nesting
ifcopenshell.api.run("nest.unassign_object", model, related_objects=[faucet])

## Remove property set
ifcopenshell.api.run("pset.remove_pset", model, product=wall, pset=pset)

## Remove spatial reference
ifcopenshell.api.run("spatial.dereference_structure", model,
    products=[wall], relating_structure=other_storey)
```

---

### Version-Safe Type Query Pattern

```python
## IfcOpenShell: all schema versions
def get_element_type_safe(element):
    """Get element type across all IFC versions."""
    schema = element.wrapped_data.file.schema
    if schema == "IFC2X3":
        for rel in element.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByType"):
                return rel.RelatingType
    else:
        for rel in element.IsTypedBy:
            return rel.RelatingType
    return None

## PREFERRED: use ifcopenshell.util.element.get_type() which handles this internally
import ifcopenshell.util.element
element_type = ifcopenshell.util.element.get_type(wall)
```

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all relationship API methods
- [Working Code Examples](references/examples.md) — End-to-end examples for all relationship operations
- [Anti-Patterns](references/anti-patterns.md) — Common relationship mistakes and how to avoid them


## ifcos-impl-materials

> Use when assigning materials to IFC elements -- single materials, layer sets (walls), profile sets (beams/columns), or constituent sets (IFC4+). Prevents the common mistake of using IfcMaterialConstituentSet in IFC2X3 (not available). Covers IfcMaterial, IfcMaterialLayerSet, IfcMaterialProfileSet, material properties, and presentation.

## IFC Material Assignment Implementation Guide

### Quick Reference

#### Decision Tree: Which Material Type to Use

```
What kind of element needs material?
├── Single homogeneous material (e.g., steel column, concrete beam)?
│   └── IfcMaterial → assign_material(type="IfcMaterial")
│
├── Layered construction (wall, slab, roof with defined layers)?
│   └── IfcMaterialLayerSet → add_material_set(set_type="IfcMaterialLayerSet")
│       └── Each layer has a thickness (LayerThickness in meters)
│
├── Profiled structural element (beam, column with cross-section)?
│   └── IfcMaterialProfileSet → add_material_set(set_type="IfcMaterialProfileSet")
│       └── Each profile has an IfcProfileDef defining the cross-section
│
├── Composite element with named parts (window: frame+glazing)?
│   ├── IFC4+ → IfcMaterialConstituentSet
│   │   └── add_material_set(set_type="IfcMaterialConstituentSet")
│   └── IFC2X3 → IfcMaterialList (legacy, no named parts)
│       └── add_material_set(set_type="IfcMaterialList")
│
└── Legacy unordered material list (IFC2X3 only)?
    └── IfcMaterialList → add_material_set(set_type="IfcMaterialList")
```

#### Decision Tree: Assign Material to Type or Occurrence?

```
Where to assign the material?
├── Element type (IfcWallType, IfcSlabType, etc.)? [RECOMMENDED]
│   └── Assign to type → all occurrences inherit the material
│       └── ifcopenshell.api.material.assign_material(model,
│           products=[wall_type], type="IfcMaterialLayerSet", material=layer_set)
│
└── Individual occurrence (IfcWall, IfcSlab, etc.)?
    └── Assign to occurrence → overrides type material for this element only
        └── ifcopenshell.api.material.assign_material(model,
            products=[wall], material=concrete)
```

#### Critical Warnings

- **ALWAYS** assign materials to element types (IfcWallType, IfcSlabType), not individual occurrences. Occurrences inherit from their type. Assign to occurrences only when overriding type material.
- **ALWAYS** use `ifcopenshell.api.material.*` functions for material operations. NEVER create IfcMaterial or IfcRelAssociatesMaterial entities directly with `create_entity()`.
- **NEVER** use `IfcMaterialConstituentSet` with IFC2X3 schema. It does not exist in IFC2X3. Use `IfcMaterialList` instead.
- **ALWAYS** check `model.schema` before using schema-specific material types.
- **NEVER** assign multiple materials directly to the same product. Use material sets (layer, profile, constituent) for composite materials. `assign_material()` automatically unassigns previous materials.
- **ALWAYS** set `LayerThickness` on layers after creation using `edit_layer()`. Layers without thickness are invalid.
- **ALWAYS** provide a profile definition (`IfcProfileDef`) when adding profiles to a profile set. A material profile without a profile curve is incomplete.
- **NEVER** set material relationships via direct attribute assignment (e.g., `wall.HasAssociations = ...`). ALWAYS use the API.

---

### Essential Patterns

#### Pattern 1: Create and Assign a Single Material

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.api

## Create a material with category
concrete = ifcopenshell.api.material.add_material(model,
    name="Concrete C30/37", category="concrete")

## Assign to a wall (single material, no layers)
ifcopenshell.api.material.assign_material(model,
    products=[wall], material=concrete)
```

#### Pattern 2: Create a Layered Wall Material (IfcMaterialLayerSet)

```python
## IfcOpenShell: all schema versions
import ifcopenshell.api

## Step 1: Create individual materials
brick = ifcopenshell.api.material.add_material(model,
    name="Facing Brick", category="brick")
insulation = ifcopenshell.api.material.add_material(model,
    name="Mineral Wool", category="glass")
block = ifcopenshell.api.material.add_material(model,
    name="Concrete Block", category="block")

## Step 2: Create layer set container
layer_set = ifcopenshell.api.material.add_material_set(model,
    name="External Wall 300mm", set_type="IfcMaterialLayerSet")

## Step 3: Add layers (order = outside to inside)
layer1 = ifcopenshell.api.material.add_layer(model,
    layer_set=layer_set, material=brick)
ifcopenshell.api.material.edit_layer(model,
    layer=layer1, attributes={"LayerThickness": 0.102})

layer2 = ifcopenshell.api.material.add_layer(model,
    layer_set=layer_set, material=insulation)
ifcopenshell.api.material.edit_layer(model,
    layer=layer2, attributes={"LayerThickness": 0.100})

layer3 = ifcopenshell.api.material.add_layer(model,
    layer_set=layer_set, material=block)
ifcopenshell.api.material.edit_layer(model,
    layer=layer3, attributes={"LayerThickness": 0.100})

## Step 4: Assign to wall TYPE (best practice)
ifcopenshell.api.material.assign_material(model,
    products=[wall_type], type="IfcMaterialLayerSet", material=layer_set)
```

#### Pattern 3: Create a Profiled Beam Material (IfcMaterialProfileSet)

```python
## IfcOpenShell: all schema versions
import ifcopenshell.api

## Step 1: Create material
steel = ifcopenshell.api.material.add_material(model,
    name="S355", category="steel")

## Step 2: Create profile set
profile_set = ifcopenshell.api.material.add_material_set(model,
    name="HEA 200", set_type="IfcMaterialProfileSet")

## Step 3: Create profile definition (cross-section shape)
profile_def = ifcopenshell.api.profile.add_parameterised_profile(model,
    ifc_class="IfcIShapeProfileDef",
    OverallWidth=0.200, OverallDepth=0.190,
    WebThickness=0.0065, FlangeThickness=0.010)

## Step 4: Add profile item to set
profile_item = ifcopenshell.api.material.add_profile(model,
    profile_set=profile_set, material=steel, profile=profile_def)

## Step 5: Assign to column TYPE
ifcopenshell.api.material.assign_material(model,
    products=[column_type], type="IfcMaterialProfileSet", material=profile_set)
```

#### Pattern 4: Constituent Set for Composite Elements (IFC4+ Only)

```python
## IfcOpenShell: IFC4 and IFC4X3 ONLY (NOT IFC2X3)
import ifcopenshell.api

## Step 1: Create materials
aluminium = ifcopenshell.api.material.add_material(model,
    name="Aluminium Frame", category="aluminium")
glass = ifcopenshell.api.material.add_material(model,
    name="Double Glazing", category="glass")

## Step 2: Create constituent set
constituent_set = ifcopenshell.api.material.add_material_set(model,
    name="Window Assembly", set_type="IfcMaterialConstituentSet")

## Step 3: Add named constituents
frame = ifcopenshell.api.material.add_constituent(model,
    constituent_set=constituent_set, material=aluminium, name="Frame")
glazing = ifcopenshell.api.material.add_constituent(model,
    constituent_set=constituent_set, material=glass, name="Glazing")

## Step 4: Assign to window TYPE
ifcopenshell.api.material.assign_material(model,
    products=[window_type], type="IfcMaterialConstituentSet",
    material=constituent_set)
```

#### Pattern 5: Query Material from an Element

```python
## IfcOpenShell: all schema versions
import ifcopenshell.util.element

## Get material (returns IfcMaterial, IfcMaterialLayerSet, etc.)
material = ifcopenshell.util.element.get_material(wall)

if material is None:
    print("No material assigned")
elif material.is_a("IfcMaterial"):
    print(f"Single material: {material.Name}")
elif material.is_a("IfcMaterialLayerSet"):
    for layer in material.MaterialLayers:
        print(f"Layer: {layer.Material.Name}, Thickness: {layer.LayerThickness}")
elif material.is_a("IfcMaterialLayerSetUsage"):
    layer_set = material.ForLayerSet
    for layer in layer_set.MaterialLayers:
        print(f"Layer: {layer.Material.Name}, Thickness: {layer.LayerThickness}")
elif material.is_a("IfcMaterialProfileSet"):
    for profile in material.MaterialProfiles:
        print(f"Profile: {profile.Material.Name}")
elif material.is_a("IfcMaterialConstituentSet"):
    for constituent in material.MaterialConstituents:
        print(f"Constituent: {constituent.Name} - {constituent.Material.Name}")
```

#### Pattern 6: Add Visual Style to a Material

```python
## IfcOpenShell: all schema versions
import ifcopenshell.api

## Create a surface style (visual appearance)
style = ifcopenshell.api.style.add_style(model, name="Concrete Grey")
ifcopenshell.api.style.add_surface_style(model, style=style,
    ifc_class="IfcSurfaceStyleShading",
    attributes={
        "SurfaceColour": {"Name": None, "Red": 0.7, "Green": 0.7, "Blue": 0.7}
    })

## Assign style to a representation
ifcopenshell.api.style.assign_representation_styles(model,
    shape_representation=body_rep, styles=[style])
```

---

### Common Operations

#### Material Categories (Standard Values)

| Category | Use For |
|----------|---------|
| `"concrete"` | Concrete elements, precast |
| `"steel"` | Structural steel, reinforcement |
| `"aluminium"` | Window frames, curtain walls |
| `"brick"` | Masonry walls |
| `"block"` | Concrete blocks |
| `"stone"` | Natural stone elements |
| `"wood"` | Timber construction |
| `"glass"` | Glazing, insulation (glass wool) |
| `"gypsum"` | Plasterboard, gypsum finishes |
| `"plastic"` | PVC pipes, synthetic membranes |
| `"earth"` | Foundation fill, landscaping |

#### Material Set Type Selection Guide

| Element Type | Material Set | Schema |
|-------------|-------------|--------|
| Walls (layered) | `IfcMaterialLayerSet` | All |
| Slabs (layered) | `IfcMaterialLayerSet` | All |
| Roofs (layered) | `IfcMaterialLayerSet` | All |
| Beams | `IfcMaterialProfileSet` | All |
| Columns | `IfcMaterialProfileSet` | All |
| Members | `IfcMaterialProfileSet` | All |
| Windows | `IfcMaterialConstituentSet` | IFC4+ |
| Doors | `IfcMaterialConstituentSet` | IFC4+ |
| Curtain walls | `IfcMaterialConstituentSet` | IFC4+ |
| Furniture | `IfcMaterial` (single) | All |
| Equipment | `IfcMaterial` (single) | All |
| Windows (legacy) | `IfcMaterialList` | IFC2X3 |

#### Remove Material from Element

```python
## IfcOpenShell: all schema versions
ifcopenshell.api.material.unassign_material(model, products=[wall])
```

#### Copy a Material with All Properties

```python
## IfcOpenShell: all schema versions
new_material = ifcopenshell.api.material.copy_material(model,
    material=existing_material)
## Copies psets and styles. Set items are copied but underlying materials reused.
```

#### Edit Material Properties

```python
## IfcOpenShell: all schema versions
ifcopenshell.api.material.edit_material(model,
    material=concrete, attributes={"Name": "Concrete C35/45", "Category": "concrete"})
```

#### Reorder Layers in a Layer Set

```python
## IfcOpenShell: all schema versions
ifcopenshell.api.material.reorder_set_item(model,
    material_set=layer_set, old_index=2, new_index=0)
```

#### Edit Layer Usage (Offset from Reference Line)

```python
## IfcOpenShell: all schema versions
## Get the usage from the element
material = ifcopenshell.util.element.get_material(wall)
if material.is_a("IfcMaterialLayerSetUsage"):
    ifcopenshell.api.material.edit_layer_usage(model,
        usage=material, attributes={"OffsetFromReferenceLine": -0.1})
```

#### Delete Material and Material Set

```python
## IfcOpenShell: all schema versions
## First unassign from all products
ifcopenshell.api.material.unassign_material(model, products=[wall_type])

## Then remove the material set
ifcopenshell.api.material.remove_material_set(model, material_set=layer_set)

## Remove individual materials (only if not used elsewhere)
ifcopenshell.api.material.remove_material(model, material=brick)
```

---

### Version Notes

#### IFC2X3 vs IFC4+ Material Differences

| Feature | IFC2X3 | IFC4 / IFC4X3 |
|---------|--------|----------------|
| IfcMaterial | Yes | Yes |
| IfcMaterialLayerSet | Yes | Yes |
| IfcMaterialProfileSet | Yes | Yes |
| IfcMaterialConstituentSet | **No** | Yes |
| IfcMaterialList | Yes (primary) | Yes (legacy) |
| Material category attribute | **No** | Yes |
| Material description attribute | **No** | Yes |

#### Schema-Aware Material Assignment

```python
## IfcOpenShell: all schema versions
import ifcopenshell.util.element

if model.schema == "IFC2X3":
    # IFC2X3: Use IfcMaterialList for composite elements
    material_list = ifcopenshell.api.material.add_material_set(model,
        name="Window Materials", set_type="IfcMaterialList")
    ifcopenshell.api.material.add_list_item(model,
        material_list=material_list, material=aluminium)
    ifcopenshell.api.material.add_list_item(model,
        material_list=material_list, material=glass)
else:
    # IFC4+: Use IfcMaterialConstituentSet for named parts
    constituent_set = ifcopenshell.api.material.add_material_set(model,
        name="Window Assembly", set_type="IfcMaterialConstituentSet")
    ifcopenshell.api.material.add_constituent(model,
        constituent_set=constituent_set, material=aluminium, name="Frame")
    ifcopenshell.api.material.add_constituent(model,
        constituent_set=constituent_set, material=glass, name="Glazing")
```

---

### Material + Style Integration

Materials define physical properties. Styles define visual appearance. These are separate concepts in IFC. ALWAYS apply both together for visual BIM models.

#### Workflow: Material + Visual Style

```
1. Create IfcMaterial → physical definition
2. Create IfcSurfaceStyle → visual appearance (color, texture)
3. Assign style to representation → visual display
4. Assign material to product → physical association
```

Materials and styles are NOT linked automatically. A material named "Concrete" does not automatically render as grey. The style must be explicitly created and assigned to the element's representation.

---

### Reference Links

- [API Method Signatures](references/methods.md) — Complete signatures for all material API methods
- [Working Code Examples](references/examples.md) — End-to-end examples for all material operations
- [Anti-Patterns](references/anti-patterns.md) — Common material assignment mistakes and how to avoid them


## ifcos-impl-validation

> Use when validating IFC files for schema compliance, IDS conformance, or custom quality rules. Prevents the common mistake of only checking schema validity without verifying property set completeness or spatial hierarchy correctness. Covers ifcopenshell.validate, ifctester for IDS validation, georeference validation, and custom validation pipelines.

## IfcOpenShell Validation Workflows

### Quick Reference

#### Critical Warnings

- **ALWAYS** run `ifcopenshell.validate.validate()` with basic mode first (default `express_rules=False`). NEVER enable EXPRESS WHERE rules on a first pass — they are 10-100x slower on large models.
- **ALWAYS** pass a configured `logging.Logger` instance to `validate()`. The function logs results; it does NOT return them.
- **NEVER** assume a model is valid because `validate()` completes without raising an exception. Validation issues are logged, not raised. Use `LogDetectionHandler` or `json_logger` to detect issues programmatically.
- **ALWAYS** use `ifctester` for IDS (Information Delivery Specification) validation. `ifcopenshell.validate` checks schema compliance only — it does NOT check project-specific requirements.
- **NEVER** confuse schema validation with IDS validation. Schema validation verifies the IFC file structure is correct per EXPRESS schema. IDS validation verifies the IFC data meets project information requirements.
- **ALWAYS** call `add_georeferencing` before `edit_georeferencing`. The IfcMapConversion and IfcProjectedCRS entities MUST exist before editing.
- **NEVER** use `IfcMapConversionScaled` in IFC4 models. The scaled variant is only available in IFC4X3.
- **ALWAYS** check `model.schema` before applying version-specific validation logic. Georeferencing differs between IFC2X3 (property sets) and IFC4+ (dedicated entities).

#### Decision Tree: Which Validation Approach

```
What are you validating?
├── IFC file structure and schema compliance?
│   ├── Basic type/attribute checking?
│   │   └── ifcopenshell.validate.validate(model, logger)
│   ├── Full EXPRESS WHERE rules?
│   │   └── ifcopenshell.validate.validate(model, logger, express_rules=True)
│   ├── GUID format only?
│   │   └── ifcopenshell.validate.validate_guid(guid_string)
│   └── File header only?
│       └── ifcopenshell.validate.validate_ifc_header(model, logger)
│
├── Project information requirements (IDS)?
│   ├── Load IDS specification?
│   │   └── ifctester.open("spec.ids")
│   ├── Validate IFC against IDS?
│   │   └── ids.validate(ifc_file)
│   └── Generate validation report?
│       ├── Console → ifctester.reporter.Console(ids)
│       ├── JSON → ifctester.reporter.Json(ids)
│       ├── HTML → ifctester.reporter.Html(ids)
│       ├── BCF → ifctester.reporter.Bcf(ids)
│       └── ODS → ifctester.reporter.Ods(ids)
│
├── Georeferencing correctness?
│   ├── IFC2X3 → Check property sets on IfcProject
│   ├── IFC4 → Check IfcMapConversion + IfcProjectedCRS entities
│   └── IFC4X3 → Check IfcMapConversion or IfcMapConversionScaled
│
└── Custom business rules?
    └── Write Python functions using ifcopenshell entity traversal
        (see Custom Validation Rules section)
```

---

### Essential Patterns

#### Pattern 1: Basic Schema Validation

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.validate
import logging

model = ifcopenshell.open("building.ifc")

## Set up logger to capture validation output
logger = logging.getLogger("ifcopenshell.validate")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)

## Run basic validation (no EXPRESS WHERE rules)
ifcopenshell.validate.validate(model, logger)
```

#### Pattern 2: Programmatic Validation with json_logger

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.validate

model = ifcopenshell.open("building.ifc")

## Use json_logger for structured, programmatic access to results
json_log = ifcopenshell.validate.json_logger()
ifcopenshell.validate.validate(model, json_log)

## Iterate validation results
for statement in json_log.statements:
    print(f"Level: {statement['level']}, Message: {statement['message']}")

## Check if any issues were found
if json_log.statements:
    print(f"Total issues: {len(json_log.statements)}")
else:
    print("Model is valid")
```

#### Pattern 3: Detect Validation Issues (Pass/Fail Gate)

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.validate
import logging

model = ifcopenshell.open("building.ifc")

logger = logging.getLogger("ifcopenshell.validate")
logger.setLevel(logging.WARNING)

## Add detection handler to check if ANY issues exist
detection_handler = ifcopenshell.validate.LogDetectionHandler()
logger.addHandler(detection_handler)

ifcopenshell.validate.validate(model, logger)

if detection_handler.message_logged:
    print("FAIL: Validation issues found")
else:
    print("PASS: Model is valid")
```

#### Pattern 4: IDS Validation with ifctester

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifctester
import ifctester.ids
import ifctester.reporter

## Step 1: Load the IDS specification
ids = ifctester.open("requirements.ids")

## Step 2: Load the IFC file
ifc_file = ifcopenshell.open("building.ifc")

## Step 3: Validate IFC against IDS
ids.validate(ifc_file)

## Step 4: Report results
reporter = ifctester.reporter.Console(ids)
reporter.report()

## Or generate HTML report
html_reporter = ifctester.reporter.Html(ids)
html_reporter.report()
html_reporter.to_file("validation_report.html")
```

#### Pattern 5: Georeferencing Validation

```python
## IfcOpenShell: IFC4 / IFC4X3
import ifcopenshell

model = ifcopenshell.open("building.ifc")

## Check schema version for georeferencing method
if model.schema == "IFC2X3":
    # IFC2X3: Georeferencing stored as property sets on IfcProject
    project = model.by_type("IfcProject")[0]
    # Check for ePSet_MapConversion and ePSet_ProjectedCRS property sets
    psets = ifcopenshell.util.element.get_psets(project)
    has_georef = "ePSet_MapConversion" in psets
else:
    # IFC4 / IFC4X3: Dedicated entities
    map_conversions = model.by_type("IfcMapConversion")
    projected_crs = model.by_type("IfcProjectedCRS")
    has_georef = len(map_conversions) > 0 and len(projected_crs) > 0

    if model.schema == "IFC4X3":
        # Also check for IfcMapConversionScaled (IFC4X3 only)
        scaled = model.by_type("IfcMapConversionScaled")
        has_georef = has_georef or len(scaled) > 0

if has_georef:
    print("Georeferencing is present")
else:
    print("WARNING: No georeferencing found")
```

---

### IDS Validation (Information Delivery Specification)

#### What is IDS?

IDS is a buildingSMART standard (ISO 7817-3) that defines machine-readable information requirements for IFC models. An IDS file specifies:

- **Applicability**: Which IFC entities a requirement applies to (e.g., all IfcWall instances)
- **Requirements**: What data those entities must contain (e.g., must have a FireRating property)

#### IDS Facet Types

| Facet | Purpose | Example |
|-------|---------|---------|
| `Entity` | Filter by IFC class and predefined type | All IfcWall with PredefinedType=SOLIDWALL |
| `Attribute` | Check entity attribute values | Name must match pattern "W-*" |
| `Classification` | Check classification references | Must have Uniclass 2015 reference |
| `Property` | Check property set values | Pset_WallCommon.FireRating must exist |
| `Material` | Check material assignments | Must have material assigned |
| `PartOf` | Check spatial/aggregation relationships | Must be contained in IfcBuildingStorey |

#### Creating IDS Programmatically

```python
## IfcOpenShell: all schema versions
import ifctester.ids

## Create new IDS document
ids = ifctester.ids.Ids(
    title="Project Requirements",
    description="Minimum information requirements for structural review",
    author="QA Team",
    version="1.0"
)

## Create a specification: All walls must have fire rating
spec = ifctester.ids.Specification(
    name="Wall Fire Rating Required",
    ifcVersion=["IFC4"],
    description="All load-bearing walls must declare fire rating"
)

## Add to IDS
ids.specifications_.append(spec)

## Export to IDS XML
ids.to_xml("project_requirements.ids")
```

#### IDS Reporter Types

| Reporter | Output | Use Case |
|----------|--------|----------|
| `Console` | Terminal text with color | Quick interactive checks |
| `Json` | Structured JSON data | CI/CD pipelines, API integration |
| `Html` | Formatted HTML page | Stakeholder reports |
| `Bcf` | BCF issue file | BIM coordination (links to model elements) |
| `Ods` | Spreadsheet (ODS) | Data analysis, Excel-compatible review |
| `Txt` | Plain text | Log files, archival |

---

### Georeferencing: IFC2X3 vs IFC4+ Differences

#### Version Comparison

| Feature | IFC2X3 | IFC4 | IFC4X3 |
|---------|--------|------|--------|
| Map conversion | Property set on IfcProject | `IfcMapConversion` entity | `IfcMapConversion` or `IfcMapConversionScaled` |
| CRS definition | Property set | `IfcProjectedCRS` entity | `IfcProjectedCRS` entity |
| MapUnit attribute | String (full unit name) | `IfcNamedUnit` object | `IfcNamedUnit` object |
| Removal method | Remove property sets | Remove entities | Remove entities |
| API support | Manual property sets | `georeference.*` API | `georeference.*` API |

#### Georeferencing API (IFC4+)

| Function | Purpose |
|----------|---------|
| `georeference.add_georeferencing` | Create empty IfcMapConversion + IfcProjectedCRS |
| `georeference.edit_georeferencing` | Set coordinate operation and CRS parameters |
| `georeference.edit_true_north` | Set true north orientation (degrees or vector) |
| `georeference.edit_wcs` | Adjust world coordinate system origin |
| `georeference.remove_georeferencing` | Remove all georeferencing data |

#### Georeferencing Anti-Patterns

- **NEVER** set georeferencing without consulting the project surveyor. Incorrect Eastings/Northings place the building at the wrong location on Earth.
- **NEVER** confuse Project North with True North. `XAxisAbscissa`/`XAxisOrdinate` in the coordinate operation define **Project North** rotation. True North is set separately via `edit_true_north`.
- **NEVER** use `IfcMapConversionScaled` in IFC4 models. It exists only in IFC4X3.
- **ALWAYS** use EPSG codes in the format `"EPSG:XXXXX"` for the CRS Name attribute.
- **NEVER** move the WCS from origin (0,0,0) without a specific surveying reason. This affects all geometry in the model.

---

### Custom Validation Rules

#### Pattern: Property Set Completeness Check

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.element

def validate_required_psets(model, ifc_class, required_psets):
    """Validate that all entities of a type have required property sets."""
    errors = []
    elements = model.by_type(ifc_class)
    for element in elements:
        psets = ifcopenshell.util.element.get_psets(element)
        for pset_name, required_props in required_psets.items():
            if pset_name not in psets:
                errors.append(f"#{element.id()} {element.Name}: Missing {pset_name}")
                continue
            for prop in required_props:
                if prop not in psets[pset_name]:
                    errors.append(
                        f"#{element.id()} {element.Name}: "
                        f"Missing {pset_name}.{prop}"
                    )
    return errors

## Usage
model = ifcopenshell.open("building.ifc")
errors = validate_required_psets(model, "IfcWall", {
    "Pset_WallCommon": ["IsExternal", "LoadBearing", "FireRating"],
})
for error in errors:
    print(f"ERROR: {error}")
```

#### Pattern: Spatial Structure Validation

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.util.element

def validate_spatial_containment(model):
    """Check that all physical elements are spatially contained."""
    errors = []
    for element in model.by_type("IfcElement"):
        container = ifcopenshell.util.element.get_container(element)
        if container is None:
            errors.append(
                f"#{element.id()} {element.is_a()} '{element.Name}': "
                f"Not contained in any spatial element"
            )
    return errors
```

---

### Validation Pipeline Pattern

#### Automated QA Pipeline

```python
## IfcOpenShell: all schema versions
import ifcopenshell
import ifcopenshell.validate
import ifctester
import ifctester.reporter
import logging
import sys

def run_validation_pipeline(ifc_path, ids_path=None):
    """Run complete validation pipeline: schema + IDS + custom rules."""
    results = {"schema": None, "ids": None, "custom": []}

    # Phase 1: Schema validation
    model = ifcopenshell.open(ifc_path)
    json_log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(model, json_log)
    results["schema"] = {
        "passed": len(json_log.statements) == 0,
        "issues": len(json_log.statements),
        "details": json_log.statements
    }

    # Phase 2: IDS validation (if specification provided)
    if ids_path:
        ids = ifctester.open(ids_path)
        ids.validate(model)
        json_reporter = ifctester.reporter.Json(ids)
        json_reporter.report()
        results["ids"] = json_reporter.to_string()

    # Phase 3: Custom rules
    for element in model.by_type("IfcElement"):
        container = ifcopenshell.util.element.get_container(element)
        if container is None:
            results["custom"].append(
                f"#{element.id()} {element.is_a()}: No spatial container"
            )

    return results

## Usage
results = run_validation_pipeline("building.ifc", "requirements.ids")
if not results["schema"]["passed"]:
    print(f"Schema issues: {results['schema']['issues']}")
    sys.exit(1)
```

---

### Command-Line Validation

#### ifcopenshell.validate CLI

```bash
## Basic validation
python -m ifcopenshell.validate model.ifc

## With EXPRESS WHERE rules
python -m ifcopenshell.validate model.ifc --rules

## JSON output
python -m ifcopenshell.validate model.ifc --json

## Show attribute field positions in error messages
python -m ifcopenshell.validate model.ifc --fields
```

#### ifctester CLI

```bash
## Validate IFC against IDS
python -m ifctester model.ifc requirements.ids

## Generate HTML report
python -m ifctester model.ifc requirements.ids --reporter Html --output report.html
```

---

### Dependencies

- **ifcos-syntax-api** — For `ifcopenshell.api.run()` invocation patterns and `georeference.*` API functions
- **ifcos-syntax-fileio** — For `ifcopenshell.open()`, `ifcopenshell.file()`, and file I/O patterns

---

### Reference Links

- [Validation API Signatures](references/methods.md) — Complete function signatures for validate, ifctester, and georeference modules
- [Working Code Examples](references/examples.md) — End-to-end validation workflow examples
- [Anti-Patterns](references/anti-patterns.md) — Common validation mistakes and how to avoid them


---

# Errors & QA


## ifcos-errors-schema

> Use when encountering IFC schema errors or migrating between IFC2X3, IFC4, and IFC4X3. Prevents the common mistake of using IFC4-only entities (e.g., IfcMaterialConstituentSet) in IFC2X3 files. Covers entity availability differences, attribute type changes, ifcpatch for schema migration, and common SchemaError debugging.

## IFC Schema Error Reference

### Quick Reference

#### Decision Tree: Schema Error Diagnosis

```
Error when using IFC entity or attribute?
├── RuntimeError: entity "XYZ" not found
│   ├── Entity exists in a DIFFERENT schema version?
│   │   ├── YES → Check model.schema, use version-aware class name
│   │   │   ├── IfcBuildingElement → IFC4X3 uses IfcBuiltElement
│   │   │   ├── IfcWallStandardCase → IFC4X3 removed, use IfcWall
│   │   │   ├── IfcDoorStyle → IFC4+ uses IfcDoorType
│   │   │   └── IfcWindowStyle → IFC4+ uses IfcWindowType
│   │   └── NO → Entity does not exist in ANY schema
│   │       └── Check spelling and IFC specification
│   │
│   └── Entity is IFC4X3-only (infrastructure)?
│       └── IfcRoad, IfcBridge, IfcRailway, IfcAlignment, etc.
│           → ONLY available in schema="IFC4X3"
│
├── AttributeError: entity has no attribute "XYZ"
│   ├── PredefinedType on IFC2X3 elements?
│   │   └── Most elements lack PredefinedType in IFC2X3
│   ├── OwnerHistory is None in IFC2X3?
│   │   └── OwnerHistory is REQUIRED in IFC2X3, OPTIONAL in IFC4+
│   └── Attribute renamed between versions?
│       └── Check attribute change table below
│
├── Need to migrate between schema versions?
│   └── Use ifcpatch Migrate recipe
│       ├── IFC2X3 → IFC4: ifcpatch.execute({...recipe: "Migrate", arguments: ["IFC4"]})
│       └── IFC4 → IFC4X3: ifcpatch.execute({...recipe: "Migrate", arguments: ["IFC4X3"]})
│
└── Schema mismatch when combining files?
    └── ALWAYS check model.schema before transferring entities
        └── Use model.add(entity) ONLY between same-schema files
```

#### Critical Warnings

- **ALWAYS** check `model.schema` before using schema-specific entities. NEVER assume the schema.
- **NEVER** use `IfcBuildingElement` in IFC4X3 code — it was renamed to `IfcBuiltElement`.
- **NEVER** use `IfcWallStandardCase` or any `*StandardCase` entity in IFC4X3 — they were all removed.
- **NEVER** use `IfcDoorStyle` or `IfcWindowStyle` in IFC4+ code — use `IfcDoorType` and `IfcWindowType`.
- **ALWAYS** provide `OwnerHistory` when creating entities in IFC2X3 files (it is REQUIRED).
- **NEVER** transfer entities between files of different schemas without migration.
- **ALWAYS** use `ifcopenshell.api.run()` for entity creation — it handles schema differences automatically.
- **ALWAYS** validate IFC files after schema migration with ifcpatch.

---

### Essential Error Patterns

#### Error 1: Entity Not Found: Schema Version Mismatch

**Symptom**: `RuntimeError` when calling `model.by_type()` or `model.create_entity()` with an entity name that does not exist in the file's schema.

```python
## WRONG: IfcBuiltElement does not exist in IFC2X3 or IFC4
model = ifcopenshell.open("legacy_building.ifc")  # schema = "IFC2X3"
elements = model.by_type("IfcBuiltElement")  # RuntimeError!

## WRONG: IfcBuildingElement does not exist in IFC4X3
model = ifcopenshell.open("new_infra.ifc")  # schema = "IFC4X3"
elements = model.by_type("IfcBuildingElement")  # RuntimeError!
```

**Fix**: ALWAYS check `model.schema` and use the correct entity name.

```python
## CORRECT: Version-aware entity class selection
schema = model.schema
if schema == "IFC4X3":
    building_element_class = "IfcBuiltElement"
else:  # IFC2X3, IFC4
    building_element_class = "IfcBuildingElement"
elements = model.by_type(building_element_class)
```

#### Error 2: StandardCase Entity Not Found in IFC4X3

**Symptom**: `RuntimeError` when querying `IfcWallStandardCase`, `IfcBeamStandardCase`, etc. in an IFC4X3 file.

IFC4 introduced 11 `*StandardCase` subtypes. IFC4X3 **removed all of them**, merging behavior back into parent classes.

**Removed in IFC4X3:**
- IfcBeamStandardCase → use IfcBeam
- IfcColumnStandardCase → use IfcColumn
- IfcDoorStandardCase → use IfcDoor
- IfcMemberStandardCase → use IfcMember
- IfcOpeningStandardCase → use IfcOpeningElement
- IfcPlateStandardCase → use IfcPlate
- IfcSlabStandardCase → use IfcSlab
- IfcSlabElementedCase → use IfcSlab
- IfcWallElementedCase → use IfcWall
- IfcWindowStandardCase → use IfcWindow

```python
## CORRECT: Version-safe wall query
schema = model.schema
if schema == "IFC2X3":
    walls = model.by_type("IfcWallStandardCase")
elif schema == "IFC4":
    walls = model.by_type("IfcWallStandardCase")  # exists in IFC4
else:  # IFC4X3
    walls = model.by_type("IfcWall")  # StandardCase removed
```

#### Error 3: IFC4X3-Only Entities on Older Schemas

**Symptom**: `RuntimeError` when creating infrastructure entities on IFC2X3 or IFC4 files.

```python
## WRONG: IfcRoad only exists in IFC4X3
model = ifcopenshell.file(schema="IFC4")
road = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcRoad", name="Highway")  # RuntimeError!
```

**IFC4X3-only entities** (partial list):
- Facilities: IfcFacility, IfcBridge, IfcRoad, IfcRailway, IfcMarineFacility
- Facility parts: IfcFacilityPart, IfcBridgePart, IfcRoadPart, IfcRailwayPart, IfcMarinePart
- Infrastructure: IfcAlignment, IfcBearing, IfcCourse, IfcKerb, IfcPavement, IfcRail, IfcTrackElement
- Geotechnical: IfcGeotechnicalElement, IfcBorehole, IfcGeomodel
- Other: IfcDeepFoundation, IfcLinearElement, IfcTransportationDevice

**Fix**: ALWAYS create IFC4X3 files for infrastructure projects.

```python
## CORRECT: Use IFC4X3 for infrastructure
model = ifcopenshell.file(schema="IFC4X3")
road = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcRoad", name="Highway")  # Works
```

#### Error 4: OwnerHistory Required in IFC2X3

**Symptom**: Invalid IFC2X3 file — `OwnerHistory` is `$` (null) but IFC2X3 requires it on all `IfcRoot` subclasses.

```python
## WRONG: OwnerHistory is REQUIRED in IFC2X3
model = ifcopenshell.file(schema="IFC2X3")
wall = model.createIfcWall(
    ifcopenshell.guid.new(),
    None,  # OwnerHistory = None → INVALID in IFC2X3!
    "MyWall"
)
```

**Fix**: Use `ifcopenshell.api.run()` which handles OwnerHistory automatically, or provide it explicitly.

```python
## CORRECT: api.run() handles OwnerHistory for all schemas
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="MyWall")

## CORRECT: Manual creation with explicit OwnerHistory
owner_history = ifcopenshell.api.run("owner.create_owner_history", model)
wall = model.createIfcWall(
    ifcopenshell.guid.new(),
    owner_history,  # REQUIRED in IFC2X3
    "MyWall"
)
```

#### Error 5: IfcDoorStyle / IfcWindowStyle vs IfcDoorType / IfcWindowType

**Symptom**: `RuntimeError` when querying `IfcDoorType` in IFC2X3, or `IfcDoorStyle` in IFC4X3.

| Type Entity | IFC2X3 | IFC4 | IFC4X3 |
|-------------|--------|------|--------|
| IfcDoorStyle | YES | Deprecated | REMOVED |
| IfcWindowStyle | YES | Deprecated | REMOVED |
| IfcDoorType | NO | YES | YES |
| IfcWindowType | NO | YES | YES |

```python
## CORRECT: Version-safe type class selection
def get_door_type_class(schema):
    if schema == "IFC2X3":
        return "IfcDoorStyle"
    return "IfcDoorType"  # IFC4, IFC4X3

def get_window_type_class(schema):
    if schema == "IFC2X3":
        return "IfcWindowStyle"
    return "IfcWindowType"  # IFC4, IFC4X3
```

#### Error 6: PredefinedType Not Available in IFC2X3

**Symptom**: `AttributeError` when accessing `element.PredefinedType` on IFC2X3 entities that lack this attribute.

Many entities gained `PredefinedType` in IFC4 that did not have it in IFC2X3: IfcBeam, IfcColumn, IfcDoor, IfcWall, IfcWindow, IfcSlab, and others.

```python
## WRONG: Assumes PredefinedType exists (fails on IFC2X3 IfcBeam)
for beam in model.by_type("IfcBeam"):
    print(beam.PredefinedType)  # AttributeError in IFC2X3!

## CORRECT: Check schema or use hasattr
for beam in model.by_type("IfcBeam"):
    if hasattr(beam, "PredefinedType"):
        print(beam.PredefinedType)
    else:
        print("No PredefinedType (IFC2X3)")
```

#### Error 7: IfcContext Does Not Exist in IFC2X3

**Symptom**: `RuntimeError` querying `IfcContext` in IFC2X3. In IFC2X3, `IfcProject` inherits from `IfcObject`. In IFC4+, `IfcProject` inherits from `IfcContext` (new abstract class).

```python
## WRONG: IfcContext does not exist in IFC2X3
project = model.by_type("IfcContext")  # RuntimeError in IFC2X3!

## CORRECT: Use IfcProject directly (works in all versions)
project = model.by_type("IfcProject")[0]
```

---

### Schema Migration with ifcpatch

#### Migration Recipe

The `Migrate` recipe in ifcpatch converts IFC files between schema versions. Upgrading is more reliable than downgrading.

```python
import ifcopenshell
import ifcpatch

## Upgrade IFC2X3 → IFC4
model = ifcopenshell.open("input_2x3.ifc")
output = ifcpatch.execute({
    "input": "input_2x3.ifc",
    "file": model,
    "recipe": "Migrate",
    "arguments": ["IFC4"]
})
ifcpatch.write(output, "output_ifc4.ifc")

## Upgrade IFC4 → IFC4X3
model = ifcopenshell.open("input_ifc4.ifc")
output = ifcpatch.execute({
    "input": "input_ifc4.ifc",
    "file": model,
    "recipe": "Migrate",
    "arguments": ["IFC4X3"]
})
ifcpatch.write(output, "output_ifc4x3.ifc")
```

#### Migration Limitations

- The Migrate recipe is **experimental** — ALWAYS validate output.
- Upgrading (IFC2X3 → IFC4 → IFC4X3) is more stable than downgrading.
- Entity renames are handled automatically (IfcBuildingElement → IfcBuiltElement).
- StandardCase merging is handled automatically.
- Custom property sets are preserved.
- Geometry may require manual review after migration.
- ALWAYS compare entity counts before and after migration.

#### Post-Migration Validation

```python
import ifcopenshell
import ifcopenshell.validate

model = ifcopenshell.open("migrated.ifc")
logger = ifcopenshell.validate.json_logger()
ifcopenshell.validate.validate(model, logger)

for error in logger.statements:
    print(f"{error['severity']}: {error['message']}")
```

---

### Entity Availability Quick Reference

#### Entities That Changed Name

| IFC2X3 | IFC4 | IFC4X3 |
|--------|------|--------|
| IfcBuildingElement | IfcBuildingElement | **IfcBuiltElement** |
| IfcBuildingElementType | IfcBuildingElementType | **IfcBuiltElementType** |
| IfcDoorStyle | IfcDoorType (new) | IfcDoorType |
| IfcWindowStyle | IfcWindowType (new) | IfcWindowType |

#### Entities Removed in IFC4 (from IFC2X3)

- IfcBezierCurve → use IfcBSplineCurve
- IfcRationalBezierCurve → use IfcBSplineCurve
- Ifc2DCompositeCurve → use IfcCompositeCurve
- IfcCalendarDate, IfcLocalTime, IfcDateAndTime → use IfcDateTime (string)
- IfcMove → use IfcTask
- IfcOrderRequest → use IfcTask
- IfcRelAssignsTasks → use IfcRelAssignsToProcess
- IfcElectricDistributionPoint → use IfcElectricDistributionBoard

#### Entities Removed in IFC4X3 (from IFC4)

All StandardCase subtypes:
- IfcBeamStandardCase, IfcColumnStandardCase, IfcDoorStandardCase
- IfcMemberStandardCase, IfcOpeningStandardCase, IfcPlateStandardCase
- IfcSlabStandardCase, IfcSlabElementedCase, IfcWallElementedCase
- IfcWindowStandardCase
- IfcPresentationStyleAssignment → use IfcStyledItem directly

#### Attribute Changes Across Versions

| Entity | Attribute | IFC2X3 | IFC4+ |
|--------|-----------|--------|-------|
| IfcRoot | OwnerHistory | REQUIRED | OPTIONAL |
| IfcMaterial | Description, Category | Not available | OPTIONAL |
| IfcStairFlight | NumberOfRiser | Singular | NumberOfRisers (plural) |
| IfcBuildingElementProxy | CompositionType | Present | Replaced by PredefinedType |
| IfcRelSequence | LagTime | float | TimeLag (IfcLagTime object) |
| Most elements | PredefinedType | Not available | OPTIONAL |
| Date/Time fields | — | IfcDateAndTime objects | IfcDateTime strings |

---

### Schema Introspection

#### Checking Entity Existence at Runtime

```python
import ifcopenshell

def entity_exists_in_schema(schema_name, entity_name):
    """Check if an entity exists in a specific IFC schema."""
    schema = ifcopenshell.ifcopenshell_wrapper.schema_by_name(schema_name)
    try:
        schema.declaration_by_name(entity_name)
        return True
    except RuntimeError:
        return False

## Usage
print(entity_exists_in_schema("IFC2X3", "IfcBuiltElement"))  # False
print(entity_exists_in_schema("IFC4X3", "IfcBuiltElement"))  # True
print(entity_exists_in_schema("IFC4X3", "IfcBuildingElement"))  # False
```

#### Listing Entity Attributes Per Schema

```python
schema = ifcopenshell.ifcopenshell_wrapper.schema_by_name("IFC4")
entity = schema.declaration_by_name("IfcWall")
for attr in entity.all_attributes():
    print(f"{attr.name()}: {attr.type_of_attribute()}")
```

---

### Version-Safe Coding Patterns

#### Pattern: Universal Building Element Query

```python
def get_building_elements(model):
    """Get all building/built elements regardless of schema version."""
    schema = model.schema
    if schema == "IFC4X3":
        return model.by_type("IfcBuiltElement")
    return model.by_type("IfcBuildingElement")
```

#### Pattern: Safe Entity Creation with Schema Check

```python
def create_entity_safe(model, ifc_class, **kwargs):
    """Create entity with schema validation."""
    schema = ifcopenshell.ifcopenshell_wrapper.schema_by_name(model.schema)
    try:
        schema.declaration_by_name(ifc_class)
    except RuntimeError:
        raise ValueError(
            f"Entity '{ifc_class}' does not exist in {model.schema}. "
            f"Check the schema version compatibility."
        )
    return ifcopenshell.api.run("root.create_entity", model,
        ifc_class=ifc_class, **kwargs)
```

#### Pattern: Schema-Agnostic Utilities

ALWAYS prefer `ifcopenshell.util` functions over manual traversal — they handle schema differences internally:

```python
import ifcopenshell.util.element

## These work identically across IFC2X3, IFC4, and IFC4X3:
container = ifcopenshell.util.element.get_container(element)
psets = ifcopenshell.util.element.get_psets(element)
material = ifcopenshell.util.element.get_material(element)
element_type = ifcopenshell.util.element.get_type(element)
```

---

### Reference Links

- [API Method Signatures](references/methods.md) — Schema introspection and migration methods
- [Working Code Examples](references/examples.md) — Version-safe coding patterns
- [Anti-Patterns](references/anti-patterns.md) — Schema-related mistakes and fixes


## ifcos-errors-performance

> Use when processing large IFC files (100MB+) or optimizing slow IfcOpenShell scripts. Prevents the #1 performance mistake: calling create_shape() per element instead of using the geometry iterator for batch processing. Covers geometry iterator, by_type caching, batch patterns, memory management, multiprocessing strategies, and profiling.

## IfcOpenShell Performance Optimization

### Quick Reference

#### Decision Tree: Geometry Processing Strategy

```
Processing IFC geometry?
├── Single element (interactive/debug)?
│   └── ifcopenshell.geom.create_shape(settings, element)
│
├── Multiple elements (10+)?
│   └── ALWAYS use ifcopenshell.geom.iterator
│       ├── Need all elements? → iterator(settings, model, cpu_count())
│       └── Need specific types? → iterator(settings, model, cpu_count(), include=filtered)
│
└── No geometry needed (data extraction only)?
    └── Skip geometry entirely — use by_type() + get_psets()
```

#### Decision Tree: Large File Strategy

```
File size?
├── < 10 MB (small) → Standard ifcopenshell.open(), no special handling
│
├── 10-200 MB (medium) → Cache by_type() results, batch API calls
│
├── 200 MB - 2 GB (large)
│   ├── Data only? → Load, extract to plain dicts, del model, gc.collect()
│   ├── Geometry? → Use iterator with include filter, limit threads on low-RAM
│   └── Repeated access? → Extract once, cache in external format
│
└── > 2 GB (very large)
    ├── Needs full model? → 32+ GB RAM required
    ├── Needs subset? → Extract IDs first, process in chunks
    └── Geometry? → Process by type in sequence, gc.collect() between types
```

#### Critical Warnings

- **ALWAYS** use `ifcopenshell.geom.iterator` for batch geometry processing (10+ elements). NEVER call `create_shape()` in a loop for bulk operations — iterator is 5-10x faster.
- **ALWAYS** pass `multiprocessing.cpu_count()` to the iterator for optimal parallelism. Reduce thread count only on memory-constrained systems.
- **ALWAYS** cache `by_type()` results when accessing the same type multiple times. The call is fast (O(1) internal index), but repeated calls add overhead in tight loops.
- **ALWAYS** batch spatial containment and type assignments. Pass a list of products to a single API call instead of calling per-element.
- **NEVER** store all geometry shapes in memory simultaneously. Process each shape and discard immediately.
- **NEVER** use `get_info(recursive=True)` on large files — it materializes the entire entity graph into Python dicts.
- **NEVER** open the same large file multiple times. Open once and pass the `model` reference.
- **ALWAYS** call `gc.collect()` after releasing large models or between geometry processing batches.

---

### Essential Patterns

#### Pattern 1: Geometry Iterator (Batch Processing)

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.geom
import multiprocessing

model = ifcopenshell.open("model.ifc")
settings = ifcopenshell.geom.settings()

iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count()
)

if iterator.initialize():
    while True:
        shape = iterator.get()
        element = model.by_id(shape.id)
        verts = shape.geometry.verts   # Flat: [x1,y1,z1, x2,y2,z2, ...]
        faces = shape.geometry.faces   # Flat: [i1,i2,i3, ...]
        # Process immediately, do NOT accumulate shapes
        if not iterator.next():
            break
```

#### Pattern 2: Filtered Geometry Processing

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.geom
import multiprocessing

model = ifcopenshell.open("large_model.ifc")
settings = ifcopenshell.geom.settings()

## Process only walls: reduces memory and time
walls = model.by_type("IfcWall")
iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count(),
    include=walls
)

if iterator.initialize():
    while True:
        shape = iterator.get()
        # Process shape...
        if not iterator.next():
            break
```

#### Pattern 3: Efficient Property Extraction (No Geometry)

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.util.element

model = ifcopenshell.open("large_model.ifc")

## Build pset index ONCE from relationship entities
pset_rels = model.by_type("IfcRelDefinesByProperties")
pset_map = {}
for rel in pset_rels:
    for obj in rel.RelatedObjects:
        if obj.id() not in pset_map:
            pset_map[obj.id()] = []
        pset_map[obj.id()].append(rel.RelatingPropertyDefinition)

## Now O(1) lookup per element instead of traversing relationships each time
```

#### Pattern 4: Batch API Operations

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.api

model = ifcopenshell.open("model.ifc")
storey = model.by_type("IfcBuildingStorey")[0]
walls = list(model.by_type("IfcWall"))

## CORRECT: Single API call for all elements
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=walls)
## Creates ONE IfcRelContainedInSpatialStructure for all walls

## CORRECT: Batch type assignment
wall_type = model.by_type("IfcWallType")[0]
ifcopenshell.api.run("type.assign_type", model,
    related_objects=walls, relating_type=wall_type)
```

#### Pattern 5: Memory Management for Large Files

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.util.element
import gc

def extract_wall_data(filepath):
    """Extract wall data from large file, then release model."""
    model = ifcopenshell.open(filepath)

    data = []
    for wall in model.by_type("IfcWall"):
        psets = ifcopenshell.util.element.get_psets(wall)
        data.append({
            "guid": wall.GlobalId,
            "name": wall.Name,
            "properties": psets
        })

    # Release model and force garbage collection
    del model
    gc.collect()

    return data  # Work with plain Python dicts from here
```

#### Pattern 6: Sequential Type Processing for Very Large Files

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.geom
import gc

model = ifcopenshell.open("huge_model.ifc")

element_types = ["IfcWall", "IfcSlab", "IfcColumn", "IfcBeam"]
for etype in element_types:
    elements = model.by_type(etype)
    if not elements:
        continue

    settings = ifcopenshell.geom.settings()
    iterator = ifcopenshell.geom.iterator(
        settings, model, 4, include=elements
    )

    if iterator.initialize():
        while True:
            shape = iterator.get()
            # Process and store results immediately
            if not iterator.next():
                break

    # Force GC between types to control peak memory
    gc.collect()
```

---

### Performance Reference Tables

#### File Size vs Resource Usage

| File Size | Approx Elements | RAM Usage | Load Time | Notes |
|-----------|----------------|-----------|-----------|-------|
| < 10 MB | < 1,000 | < 200 MB | < 1s | No special handling needed |
| 10-200 MB | 1,000-50,000 | 200 MB-2 GB | 1-10s | Cache query results |
| 200 MB-2 GB | 50,000-500,000 | 2-16 GB | 10-60s | Filter and batch everything |
| > 2 GB | > 500,000 | 16+ GB | 60s+ | Process by type, subprocess isolation |

#### Geometry Iterator vs create_shape()

| Aspect | `create_shape()` | `geom.iterator` |
|--------|-----------------|-----------------|
| Use case | Single element, interactive | Batch processing, export |
| Multi-threading | No | Yes (OpenMP, multi-core) |
| Geometry caching | No | Yes (reuses identical geometry) |
| Error handling | Exception per element | Skips failed elements automatically |
| Speed (1000 elements) | ~60s (sequential) | ~8s (8 cores) |
| Memory per call | Lower overhead | Better amortized for many elements |

#### Geometry Settings for Performance

| Setting | Effect | Performance Impact |
|---------|--------|-------------------|
| `disable-opening-subtractions` | Skips boolean CSG operations | Major speedup, less accurate geometry |
| `use-world-coords` | Applies global transforms | Slight overhead, but avoids manual transform |
| `weld-vertices` | Merges duplicate vertices | Smaller output, slight processing cost |
| `apply-default-materials` | Adds material data | Required for glTF, adds overhead |
| `dimensionality` | Controls output complexity | CURVES_SURFACES_AND_SOLIDS is slowest |

#### Query Performance

| Method | Complexity | Notes |
|--------|-----------|-------|
| `model.by_type("IfcWall")` | O(1) | Uses internal class index |
| `model.by_id(42)` | O(1) | Uses internal ID map |
| `model.by_guid("3Oe$...")` | O(1) | Uses GUID index |
| `for e in model if e.is_a("IfcWall")` | O(n) | NEVER use — iterates ALL entities |
| `ifcopenshell.util.element.get_psets(wall)` | O(k) | Traverses k relationships per call |
| `ifcopenshell.util.selector.filter_elements(model, query)` | O(n) | Full scan, but expressive queries |

---

### Common Operations

#### Profiling IFC Operations

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import time

model = ifcopenshell.open("model.ifc")

## Time file loading
start = time.perf_counter()
model = ifcopenshell.open("model.ifc")
load_time = time.perf_counter() - start
print(f"Load time: {load_time:.2f}s")

## Time by_type queries
start = time.perf_counter()
walls = model.by_type("IfcWall")
query_time = time.perf_counter() - start
print(f"by_type query: {query_time:.6f}s for {len(walls)} walls")

## Time geometry processing
import ifcopenshell.geom
import multiprocessing

settings = ifcopenshell.geom.settings()
start = time.perf_counter()
iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count()
)
count = 0
if iterator.initialize():
    while True:
        shape = iterator.get()
        count += 1
        if not iterator.next():
            break
geom_time = time.perf_counter() - start
print(f"Geometry: {count} shapes in {geom_time:.2f}s "
      f"({count/geom_time:.0f} shapes/sec)")
```

#### Controlling Thread Count for Memory

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.geom
import multiprocessing
import os

model = ifcopenshell.open("large_model.ifc")
settings = ifcopenshell.geom.settings()

## Check available memory (Linux/macOS)
try:
    import psutil
    available_gb = psutil.virtual_memory().available / (1024**3)
except ImportError:
    available_gb = 8  # Conservative fallback

## Scale threads to available memory
## Each thread can use 500MB-1GB for geometry processing
max_threads = multiprocessing.cpu_count()
safe_threads = min(max_threads, max(1, int(available_gb / 1.0)))

iterator = ifcopenshell.geom.iterator(
    settings, model, safe_threads
)
```

#### Subprocess Isolation for Very Large Files

```python
## IfcOpenShell v0.8+: all schema versions
import subprocess
import json

## Process geometry in a subprocess to guarantee memory cleanup
## Python's GC may not release all C++ allocated memory
result = subprocess.run(
    ["python", "-c", """
import ifcopenshell
import ifcopenshell.geom
import json

model = ifcopenshell.open("huge_model.ifc")
settings = ifcopenshell.geom.settings()
walls = model.by_type("IfcWall")
iterator = ifcopenshell.geom.iterator(settings, model, 4, include=walls)

data = []
if iterator.initialize():
    while True:
        shape = iterator.get()
        element = model.by_id(shape.id)
        data.append({"guid": element.GlobalId, "verts": len(shape.geometry.verts)})
        if not iterator.next():
            break

print(json.dumps(data))
"""],
    capture_output=True, text=True
)
data = json.loads(result.stdout)
## Subprocess memory is fully reclaimed by OS on exit
```

#### Disabling Expensive Geometry Operations

```python
## IfcOpenShell v0.8+: all schema versions
import ifcopenshell
import ifcopenshell.geom

model = ifcopenshell.open("model.ifc")
settings = ifcopenshell.geom.settings()

## Skip boolean operations (opening subtractions) for speed
## Doors/windows won't create holes in walls, but processing is much faster
settings.set("disable-opening-subtractions", True)

## Use world coordinates to avoid manual transform calculations
settings.set("use-world-coords", True)
```

---

### Version Notes

#### Schema Sensitivity

This skill has **low schema sensitivity**. Performance patterns apply equally to IFC2X3, IFC4, and IFC4X3 files. The geometry iterator, caching strategies, and memory management techniques are schema-independent.

#### IfcOpenShell Version Notes

| Feature | Version | Notes |
|---------|---------|-------|
| `geom.iterator` | All versions | Core performance feature since early releases |
| `geom.settings()` | All versions | String-based setting names in v0.8+ |
| `by_type()` class index | All versions | O(1) lookup, always available |
| `include` filter on iterator | v0.7+ | Filter elements before geometry processing |
| Subprocess isolation | Any | Python-level pattern, not IfcOpenShell-specific |

---

### Reference Links

- [Performance Method Signatures](references/methods.md) — Complete API signatures for geometry processing and querying
- [Working Performance Examples](references/examples.md) — End-to-end optimization examples for real scenarios
- [Performance Anti-Patterns](references/anti-patterns.md) — Common performance mistakes and how to avoid them


## ifcos-agents-code-validator

> Use when reviewing, validating, or auditing IfcOpenShell Python code for correctness. Runs systematic checks for schema compatibility errors, incorrect API usage (direct attribute modification vs api.run), entity reference invalidation, performance anti-patterns, and IFC standard compliance. Prevents shipping code that works on one schema but fails on another.

## IfcOpenShell Code Validator Agent

### Quick Reference

#### When to Activate This Validator

Activate this validation checklist when:
- Reviewing IfcOpenShell Python code for correctness
- Auditing IFC file manipulation scripts before production use
- Checking code that creates, modifies, or reads IFC files
- Validating code that processes IFC geometry
- Reviewing code that handles multiple IFC schema versions
- Assessing performance of scripts processing large IFC files (100MB+)

#### Severity Levels

| Severity | Meaning | Action |
|----------|---------|--------|
| **BLOCKER** | Code will crash, corrupt data, or produce invalid IFC files | MUST fix before code is accepted |
| **WARNING** | Code has potential bugs, performance issues, or fragile patterns | SHOULD fix; document reason if deferred |
| **INFO** | Code works but does not follow best practices | MAY fix; note for future improvement |

---

### Validation Checklist

Execute these checks in order. Each check references the dependency skill that defines the rule.

#### Step 1: Schema Awareness (BLOCKER)

**Source: ifcos-errors-schema**

```
Code uses IFC entities?
├── Does code check model.schema before using schema-specific entities?
│   ├── NO → BLOCKER: Add schema check
│   └── YES → Pass
│
├── Does code use any *StandardCase entity (IfcWallStandardCase, etc.)?
│   ├── YES + no IFC4X3 guard → BLOCKER: StandardCase removed in IFC4X3
│   └── NO or guarded → Pass
│
├── Does code use IfcBuiltElement or IfcBuildingElement?
│   ├── YES + no schema branch → BLOCKER: Name differs by schema
│   └── Handled → Pass
│
├── Does code use IfcDoorStyle/IfcWindowStyle?
│   ├── YES + targets IFC4+ → BLOCKER: Use IfcDoorType/IfcWindowType
│   └── Handled → Pass
│
├── Does code use IFC4X3-only entities (IfcRoad, IfcBridge, IfcAlignment)?
│   ├── YES + schema != "IFC4X3" → BLOCKER: Entity does not exist
│   └── Correct schema → Pass
│
└── Does code access PredefinedType on IFC2X3 entities?
    ├── YES + no hasattr guard → BLOCKER: Most IFC2X3 entities lack PredefinedType
    └── Guarded → Pass
```

#### Step 2: API Usage Correctness (BLOCKER)

**Source: ifcos-syntax-api, ifcos-errors-patterns**

```
Code creates or modifies IFC entities?
├── Uses model.create_entity() for production code?
│   └── BLOCKER: Use ifcopenshell.api.run("root.create_entity", ...) instead
│
├── Uses ifcopenshell.api.run() or direct module calls?
│   ├── Invents non-existent API modules/functions?
│   │   └── BLOCKER: Verify against the 35 API modules table
│   ├── Uses positional arguments after model?
│   │   └── BLOCKER: ALWAYS use keyword arguments
│   └── Passes single element where list is required (v0.8+)?
│       └── BLOCKER: products=, related_objects= require lists
│
├── Modifies entity attributes directly (wall.Name = "X")?
│   ├── For Name/Description → WARNING: Use api.run("attribute.edit_attributes", ...)
│   └── For relationships (ContainedInStructure, IsTypedBy) → BLOCKER: Use API
│
├── Creates relationships manually (model.create_entity("IfcRelContained..."))?
│   └── BLOCKER: Use spatial.assign_container, aggregate.assign_object, etc.
│
└── Creates IFC file with ifcopenshell.file() for production use?
    └── WARNING: Use ifcopenshell.api.run("project.create_file", ...) instead
```

#### Step 3: File I/O Correctness (BLOCKER/WARNING)

**Source: ifcos-syntax-fileio**

```
Code opens or creates IFC files?
├── Uses ifcopenshell.file() without explicit schema= parameter?
│   └── WARNING: ALWAYS specify schema explicitly
│
├── Uses project.create_file() with schema= instead of version=?
│   └── BLOCKER: Parameter name is version=, not schema=
│
├── Creates file without IfcProject + units + context + spatial hierarchy?
│   └── WARNING: Incomplete IFC files cause downstream failures
│
├── Calls model.remove() directly on products?
│   └── BLOCKER: Use api.run("root.remove_product", ...) for safe removal
│
├── Uses transactions?
│   ├── Missing end_transaction() or discard_transaction()?
│   │   └── BLOCKER: Open transactions cause undefined behavior
│   └── Calls undo()/redo() inside active transaction?
│       └── BLOCKER: NEVER call undo/redo during active transaction
│
└── Writes to disk?
    └── Pass (model.write() is safe)
```

#### Step 4: Entity Reference Safety (BLOCKER)

**Source: ifcos-errors-patterns**

```
Code removes entities or uses undo?
├── Accesses entity attributes after model.remove()?
│   └── BLOCKER: Entity wrapper is invalid after removal
│
├── Iterates and removes simultaneously?
│   └── BLOCKER: Collect to list first, then remove
│
├── Caches entity references across file modifications?
│   └── BLOCKER: References invalidate after remove/undo
│
└── Extracts data before removal?
    └── Pass
```

#### Step 5: None Return Value Handling (BLOCKER)

**Source: ifcos-errors-patterns**

```
Code calls utility functions that return None?
├── Uses get_container(element).Name without None check?
│   └── BLOCKER: get_container returns None if no containment
│
├── Uses get_type(element).Name without None check?
│   └── BLOCKER: get_type returns None if no type assigned
│
├── Uses get_material(element) without None check?
│   └── BLOCKER: get_material returns None if no material
│
├── Uses geom.create_shape() without try/except RuntimeError?
│   └── BLOCKER: Geometry processing fails for many elements
│
└── Uses model.by_guid() without None check?
    └── WARNING: Returns None if GUID not found
```

#### Step 6: GUID Handling (BLOCKER)

**Source: ifcos-errors-patterns**

```
Code creates entities with GlobalId?
├── Uses uuid.uuid4() or str(uuid) for GlobalId?
│   └── BLOCKER: IFC requires 22-char base64 GUID; use ifcopenshell.guid.new()
│
├── Reuses same GUID for multiple entities?
│   └── BLOCKER: Every entity MUST have a unique GlobalId
│
└── Uses ifcopenshell.api.run("root.create_entity") (auto-generates)?
    └── Pass
```

#### Step 7: Unit Handling (WARNING)

**Source: ifcos-errors-patterns**

```
Code reads coordinates or dimensions from IFC files?
├── Assumes coordinates are in meters?
│   └── WARNING: ALWAYS call ifcopenshell.util.unit.calculate_unit_scale(model)
│
├── Applies unit_scale to all extracted coordinates?
│   └── Pass
│
└── Creates geometry with hardcoded values?
    └── INFO: Document assumed unit system in comments
```

#### Step 8: Property Set Handling (WARNING)

**Source: ifcos-errors-patterns**

```
Code creates property sets?
├── Creates pset without checking for existing one?
│   └── WARNING: Produces duplicate property sets; check get_psets() first
│
├── Creates pset manually without IfcRelDefinesByProperties?
│   └── BLOCKER: Orphaned pset; use api.run("pset.add_pset", ...)
│
└── Uses api.run("pset.add_pset") + api.run("pset.edit_pset")?
    └── Pass
```

#### Step 9: Performance Patterns (WARNING)

**Source: ifcos-errors-performance**

```
Code processes geometry for multiple elements?
├── Calls create_shape() in a loop for 10+ elements?
│   └── WARNING: Use ifcopenshell.geom.iterator instead (5-10x faster)
│
├── Uses geom.iterator without multiprocessing.cpu_count()?
│   └── WARNING: Pass cpu_count() for optimal parallelism
│
├── Stores all geometry shapes in memory simultaneously?
│   └── WARNING: Process each shape and discard immediately
│
├── Uses get_info(recursive=True) on large files?
│   └── WARNING: Materializes entire entity graph; extract specific attributes
│
├── Opens same large file multiple times?
│   └── WARNING: Open once, pass model reference
│
├── Iterates all entities with `for e in model` instead of by_type()?
│   └── WARNING: by_type() is O(1), full iteration is O(n)
│
├── Calls spatial.assign_container per-element instead of batching?
│   └── WARNING: Pass all products in one call
│
└── Processes 200MB+ file without gc.collect() between batches?
    └── INFO: Add gc.collect() between processing phases
```

#### Step 10: IFC2X3 Compatibility (BLOCKER)

**Source: ifcos-errors-schema**

```
Code targets or handles IFC2X3 files?
├── Creates entities without OwnerHistory?
│   └── BLOCKER in IFC2X3: OwnerHistory is REQUIRED on all IfcRoot subclasses
│
├── Uses ifcopenshell.api.run() for entity creation?
│   └── Pass (API handles OwnerHistory automatically)
│
├── Queries IfcContext (does not exist in IFC2X3)?
│   └── BLOCKER: Use IfcProject directly
│
└── Uses IfcDoorType/IfcWindowType on IFC2X3?
    └── BLOCKER: Use IfcDoorStyle/IfcWindowStyle for IFC2X3
```

---

### Decision Trees

#### Decision Tree: Severity Classification

```
Is the issue...
├── A crash, data corruption, or invalid IFC output?
│   └── BLOCKER
│       Examples:
│       - Schema mismatch (entity not found)
│       - Invalid entity reference after removal
│       - Missing OwnerHistory in IFC2X3
│       - Dangling references from model.remove()
│       - Wrong GUID format
│       - Open transaction never closed
│
├── A potential bug, performance problem, or fragile pattern?
│   └── WARNING
│       Examples:
│       - Missing None check on get_container()
│       - create_shape() loop instead of iterator
│       - No unit scale applied
│       - Duplicate property sets
│       - Per-element API calls instead of batch
│
└── A best-practice deviation with no functional impact?
    └── INFO
        Examples:
        - Implicit schema parameter
        - Missing gc.collect() call
        - Hardcoded unit assumptions (documented)
```

#### Decision Tree: Auto-Fix Applicability

```
Can this issue be auto-fixed?
├── Schema entity name substitution?
│   └── YES: Replace with version-aware branching
│
├── model.remove() → api.run("root.remove_product")?
│   └── YES: Direct substitution
│
├── model.create_entity() → api.run("root.create_entity")?
│   └── YES: Add ifc_class= and name= parameters
│
├── Missing None check on utility return value?
│   └── YES: Wrap in `if result is not None:` guard
│
├── create_shape() loop → iterator?
│   └── PARTIAL: Requires restructuring; provide template
│
├── Single element → list parameter?
│   └── YES: Wrap in list brackets [element]
│
└── Missing schema check?
    └── PARTIAL: Insert model.schema check; pattern depends on context
```

---

### Auto-Fix Patterns

#### Fix 1: Single Element to List Parameter (v0.8+)

```python
## BEFORE (BLOCKER):
ifcopenshell.api.run("spatial.assign_container", model,
    product=wall, relating_structure=storey)

## AFTER:
ifcopenshell.api.run("spatial.assign_container", model,
    products=[wall], relating_structure=storey)
```

#### Fix 2: Direct Removal to Safe API Removal

```python
## BEFORE (BLOCKER):
model.remove(wall)

## AFTER:
ifcopenshell.api.run("root.remove_product", model, product=wall)
```

#### Fix 3: Low-Level Entity Creation to API

```python
## BEFORE (BLOCKER):
wall = model.create_entity("IfcWall",
    GlobalId=ifcopenshell.guid.new(), Name="Wall 001")

## AFTER:
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 001")
```

#### Fix 4: Missing None Guard

```python
## BEFORE (BLOCKER):
container = ifcopenshell.util.element.get_container(wall)
print(container.Name)

## AFTER:
container = ifcopenshell.util.element.get_container(wall)
if container is not None:
    print(container.Name)
```

#### Fix 5: UUID to IFC GUID

```python
## BEFORE (BLOCKER):
import uuid
wall = model.create_entity("IfcWall", GlobalId=str(uuid.uuid4()))

## AFTER:
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall")
## Or if manual creation is required:
wall = model.create_entity("IfcWall",
    GlobalId=ifcopenshell.guid.new(), Name="Wall")
```

#### Fix 6: Iterate-and-Remove to Collect-Then-Remove

```python
## BEFORE (BLOCKER):
for wall in model.by_type("IfcWall"):
    model.remove(wall)

## AFTER:
walls_to_remove = list(model.by_type("IfcWall"))
for wall in walls_to_remove:
    ifcopenshell.api.run("root.remove_product", model, product=wall)
```

#### Fix 7: create_shape Loop to Iterator

```python
## BEFORE (WARNING):
## IfcOpenShell: all schema versions
for wall in model.by_type("IfcWall"):
    shape = ifcopenshell.geom.create_shape(settings, wall)
    process(shape)

## AFTER:
## IfcOpenShell: all schema versions
import multiprocessing
walls = model.by_type("IfcWall")
iterator = ifcopenshell.geom.iterator(
    settings, model, multiprocessing.cpu_count(), include=walls)
if iterator.initialize():
    while True:
        shape = iterator.get()
        process(shape)
        if not iterator.next():
            break
```

#### Fix 8: Schema-Aware Entity Selection

```python
## BEFORE (BLOCKER):
## IfcOpenShell: assumes single schema
elements = model.by_type("IfcBuildingElement")

## AFTER:
## IfcOpenShell: all schema versions
schema = model.schema
if schema == "IFC4X3":
    elements = model.by_type("IfcBuiltElement")
else:
    elements = model.by_type("IfcBuildingElement")
```

---

### Validation Report Format

After running all checks, produce a report in this format:

```
### IfcOpenShell Code Validation Report

#### Summary
- BLOCKERS: [count]
- WARNINGS: [count]
- INFO: [count]

#### BLOCKER Issues
1. [Line X]: [Description] — [Fix reference]

#### WARNING Issues
1. [Line X]: [Description] — [Fix reference]

#### INFO Issues
1. [Line X]: [Description] — [Fix reference]

#### Verdict
[PASS / FAIL (if any BLOCKERS exist)]
```

---

### Reference Links

- [Validation Rules and Detection Patterns](references/methods.md)
- [Before/After Validation Fix Examples](references/examples.md)
- [Anti-Patterns Catalog](references/anti-patterns.md)

#### Dependency Skills (define the rules this validator checks)
- **ifcos-syntax-fileio** — File I/O patterns and transaction management
- **ifcos-syntax-api** — API module system, invocation patterns, parameter conventions
- **ifcos-errors-patterns** — Error categories, debugging strategies, None handling
- **ifcos-errors-schema** — Schema version differences, entity availability, migration
- **ifcos-errors-performance** — Geometry iterator, caching, memory management

#### External References
- IfcOpenShell Documentation: https://docs.ifcopenshell.org/
- IFC Schema Specifications: https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/


---

# Cross-tool workflows


## aec-core-bim-workflows

> Use when implementing end-to-end BIM workflows that combine IfcOpenShell, Bonsai, and Blender -- such as IFC creation from scratch, model enrichment, validation pipelines, geometry extraction, or batch processing of building models. Prevents the common mistake of skipping unit and context setup before creating geometry, or directly modifying IFC attributes instead of using ifcopenshell.api.run(). Covers property set management across tools, spatial hierarchy patterns, and version compatibility for IFC2X3/IFC4/IFC4X3.

## Cross-Technology BIM Workflows

> **Scope**: End-to-end workflows combining IfcOpenShell, Bonsai, and Blender
> **Dependencies**: `ifcos-impl-creation`, `bonsai-core-architecture`
> **Version coverage**: Blender 3.x-5.x | IFC2X3/IFC4/IFC4X3 | Bonsai v0.8.x

### Critical Warnings

1. **ALWAYS** determine the execution context first: standalone Python (IfcOpenShell only) vs Blender Python (bpy available) vs Bonsai-loaded (IfcStore available). The API surface differs per context.
2. **ALWAYS** use `ifcopenshell.api.run()` for IFC mutations in ALL contexts. NEVER modify IFC entity attributes directly — this bypasses relationship management and breaks graph integrity.
3. **ALWAYS** call `bpy.ops.bim.edit_object_placement()` after modifying a Blender object's location/rotation/scale when Bonsai is active. Blender transforms do NOT auto-sync to IFC.
4. **NEVER** mix `IfcStore.get_file()` (Bonsai context) with `ifcopenshell.open()` on the same file simultaneously. Bonsai owns the in-memory IFC graph — opening a second handle creates divergent state.
5. **NEVER** use `blenderbim.*` imports. The package was renamed to `bonsai.*` in v0.8.0 (2024).
6. **ALWAYS** set up units (`unit.assign_unit`) and geometric contexts (`context.add_context`) before creating any geometry. Geometry without context or units is ambiguous and may render incorrectly.
7. **NEVER** use `void.add_opening()` in Bonsai v0.8.0+. Use `feature.add_feature()` instead.

---

### Decision Tree: Choose Your Execution Context

```
What is your workflow?
|
+-- Creating/modifying IFC files WITHOUT Blender?
|   +-- Use: Standalone IfcOpenShell (headless Python)
|   +-- Import: ifcopenshell, ifcopenshell.api
|   +-- File access: ifcopenshell.open(path) or ifcopenshell.api.run("project.create_file")
|   +-- Best for: batch processing, CI/CD validation, server-side operations
|
+-- Creating/modifying IFC files IN Blender WITH Bonsai?
|   +-- Use: Bonsai-loaded context
|   +-- File access: IfcStore.get_file() — NEVER ifcopenshell.open()
|   +-- IFC mutations: tool.Ifc.run("command", **kwargs) OR ifcopenshell.api.run()
|   +-- Blender sync: bpy.ops.bim.* operators handle bidirectional sync
|   +-- Best for: interactive BIM authoring, visual verification
|
+-- Extracting geometry from IFC for Blender visualization (no Bonsai)?
|   +-- Use: IfcOpenShell geometry + Blender bpy
|   +-- Import: ifcopenshell, ifcopenshell.geom, bpy
|   +-- Geometry: ifcopenshell.geom.create_shape(settings, element)
|   +-- Mesh: bpy.data.meshes.new() + mesh.from_pydata(verts, [], faces)
|   +-- Best for: lightweight IFC viewers, geometry analysis
|
+-- Batch processing multiple IFC files?
    +-- Use: Standalone IfcOpenShell (headless) or blender --background --python
    +-- If Blender ops needed: blender --background --python script.py
    +-- If pure IFC: python script.py (no Blender dependency)
    +-- Best for: model validation, property extraction, report generation
```

---

### Decision Tree: IFC Creation vs Enrichment

```
Starting from scratch or enriching existing?
|
+-- New IFC model from scratch?
|   +-- Follow the 9-step creation pipeline:
|   |   1. project.create_file → Create file with schema version
|   |   2. root.create_entity (IfcProject) → Create project
|   |   3. unit.assign_unit → Set measurement units
|   |   4. context.add_context → Set up Model + Body subcontext
|   |   5. root.create_entity + aggregate.assign_object → Build spatial hierarchy
|   |   6. root.create_entity + type assignment → Create element types
|   |   7. root.create_entity + geometry + placement → Create elements
|   |   8. spatial.assign_container → Place elements in hierarchy
|   |   9. pset.add_pset + pset.edit_pset → Add properties
|   +-- Reference: ifcos-impl-creation (Pattern 1)
|
+-- Enriching an existing IFC file?
|   +-- Open: model = ifcopenshell.open("existing.ifc")
|   +-- Query: elements = model.by_type("IfcWall")
|   +-- Add properties: pset.add_pset + pset.edit_pset
|   +-- Add classifications: classification.add_reference
|   +-- Modify geometry: geometry operations
|   +-- Write: model.write("enriched.ifc")
|   +-- WARNING: Preserve existing GlobalIds. NEVER recreate entities that already exist.
|
+-- Merging data from multiple IFC files?
    +-- Open source: source = ifcopenshell.open("source.ifc")
    +-- Open target: target = ifcopenshell.open("target.ifc")
    +-- Extract data from source (properties, classifications, types)
    +-- Apply to target using ifcopenshell.api.run()
    +-- WARNING: Entity IDs are file-scoped. NEVER copy raw IDs between files.
    +-- WARNING: GlobalIds MUST be unique within a file. Generate new GUIDs for copied entities.
```

---

### Sverchok Parametric Design Step

When workflows involve parametric, generative, or data-driven geometry (arrays, facades, repetitive elements), insert a **Sverchok step** before BIM authoring:

```
[Sverchok: Parametric Geometry] --> [IfcSverchok: Generate IFC] --> [Bonsai: Review/Enrich]
```

- **Sverchok** generates geometry via visual node trees (`SverchCustomTreeType`)
- **IfcSverchok** (31 nodes) converts parametric geometry to IFC entities within the node tree
- Enable `use_bonsai_file` on `SvIfcCreateProject` to write directly into Bonsai's active IFC file
- **Warning**: `SvIfcStore` is transient — purged on every full tree update. Persist via Bonsai or `model.write()`
- Refer to: `sverchok-impl-parametric`, `sverchok-impl-ifcsverchok`

---

### Essential Patterns

#### Pattern 1: Standalone IFC Creation (No Blender)

```python
## Context: Standalone Python: IfcOpenShell only
## Version: IFC4 | IfcOpenShell 0.8.x
import ifcopenshell
import ifcopenshell.api
import numpy as np

model = ifcopenshell.api.run("project.create_file", version="IFC4")
project = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcProject", name="My Project")
ifcopenshell.api.run("unit.assign_unit", model)

model3d = ifcopenshell.api.run("context.add_context", model, context_type="Model")
body = ifcopenshell.api.run("context.add_context", model,
    context_type="Model", context_identifier="Body",
    target_view="MODEL_VIEW", parent=model3d)

site = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcSite", name="Site")
building = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuilding", name="Building A")
storey = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcBuildingStorey", name="Ground Floor")

ifcopenshell.api.run("aggregate.assign_object", model,
    products=[site], relating_object=project)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[building], relating_object=site)
ifcopenshell.api.run("aggregate.assign_object", model,
    products=[storey], relating_object=building)

wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="Wall 001")
rep = ifcopenshell.api.run("geometry.add_wall_representation", model,
    context=body, length=5.0, height=3.0, thickness=0.2)
ifcopenshell.api.run("geometry.assign_representation", model,
    product=wall, representation=rep)
ifcopenshell.api.run("geometry.edit_object_placement", model, product=wall)
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[wall])

model.write("output.ifc")
```

#### Pattern 2: IFC Geometry Extraction to Blender Mesh (No Bonsai)

```python
## Context: Blender Python (bpy available), NO Bonsai
## Version: Blender 3.x-5.x | IfcOpenShell 0.8.x
import bpy
import ifcopenshell
import ifcopenshell.geom

ifc_file = ifcopenshell.open("model.ifc")
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

for wall in ifc_file.by_type("IfcWall"):
    shape = ifcopenshell.geom.create_shape(settings, wall)
    verts = shape.geometry.verts     # flat list: [x0,y0,z0, x1,y1,z1, ...]
    faces = shape.geometry.faces     # flat list: [i0,i1,i2, i3,i4,i5, ...]

    # Reshape into Blender format
    vertices = [(verts[i], verts[i+1], verts[i+2])
                for i in range(0, len(verts), 3)]
    triangles = [(faces[i], faces[i+1], faces[i+2])
                 for i in range(0, len(faces), 3)]

    mesh = bpy.data.meshes.new(name=wall.Name or "Wall")
    mesh.from_pydata(vertices, [], triangles)
    mesh.update()

    obj = bpy.data.objects.new(wall.Name or "Wall", mesh)
    bpy.context.collection.objects.link(obj)
```

#### Pattern 3: Bonsai-Context BIM Authoring

```python
## Context: Blender with Bonsai loaded
## Version: Bonsai v0.8.x | Blender 4.2+
import bpy
from bonsai.bim.ifc import IfcStore
import ifcopenshell.api

## ALWAYS check for active IFC project
model = IfcStore.get_file()
if model is None:
    raise RuntimeError("No IFC project loaded. Create or open a project first.")

## Create element via Bonsai's tool layer
## Option A: Use ifcopenshell.api.run() directly
wall = ifcopenshell.api.run("root.create_entity", model,
    ifc_class="IfcWall", name="New Wall")

## Option B: Use Bonsai operators (handles Blender sync automatically)
bpy.ops.bim.add_wall()

## After creating elements, ensure spatial containment
storey = model.by_type("IfcBuildingStorey")[0]
ifcopenshell.api.run("spatial.assign_container", model,
    relating_structure=storey, products=[wall])

## CRITICAL: If you moved the Blender object, sync placement to IFC
bpy.ops.bim.edit_object_placement(context_override)

## Add property set
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=wall, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={
    "IsExternal": True,
    "LoadBearing": True,
    "FireRating": "REI60"
})
```

#### Pattern 4: Batch Property Extraction (Headless)

```python
## Context: Standalone Python or blender --background
## Version: IfcOpenShell 0.8.x | IFC4
import ifcopenshell
import ifcopenshell.util.element
import csv

model = ifcopenshell.open("building.ifc")

with open("wall_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["GlobalId", "Name", "IsExternal", "FireRating", "LoadBearing"])

    for wall in model.by_type("IfcWall"):
        psets = ifcopenshell.util.element.get_psets(wall)
        common = psets.get("Pset_WallCommon", {})
        writer.writerow([
            wall.GlobalId,
            wall.Name,
            common.get("IsExternal", ""),
            common.get("FireRating", ""),
            common.get("LoadBearing", ""),
        ])
```

#### Pattern 5: Model Validation Pipeline

```python
## Context: Standalone Python
## Version: IfcOpenShell 0.8.x | IFC4/IFC2X3
import ifcopenshell
import ifcopenshell.util.element

def validate_model(filepath: str) -> list[str]:
    errors = []
    model = ifcopenshell.open(filepath)

    # Check 1: Spatial hierarchy exists
    if not model.by_type("IfcProject"):
        errors.append("CRITICAL: No IfcProject found")
    if not model.by_type("IfcSite"):
        errors.append("CRITICAL: No IfcSite found")
    if not model.by_type("IfcBuilding"):
        errors.append("CRITICAL: No IfcBuilding found")
    if not model.by_type("IfcBuildingStorey"):
        errors.append("WARNING: No IfcBuildingStorey found")

    # Check 2: All physical elements have spatial containment
    physical_types = ["IfcWall", "IfcSlab", "IfcColumn", "IfcBeam",
                      "IfcDoor", "IfcWindow"]
    for ifc_type in physical_types:
        for element in model.by_type(ifc_type):
            container = ifcopenshell.util.element.get_container(element)
            if container is None:
                errors.append(
                    f"WARNING: {element.is_a()} '{element.Name}' "
                    f"(#{element.id()}) has no spatial container")

    # Check 3: All elements have geometry
    for element in model.by_type("IfcProduct"):
        if hasattr(element, "Representation") and element.Representation is None:
            if element.is_a() not in ("IfcSite", "IfcBuilding",
                                       "IfcBuildingStorey", "IfcSpace",
                                       "IfcProject"):
                errors.append(
                    f"WARNING: {element.is_a()} '{element.Name}' "
                    f"(#{element.id()}) has no geometry representation")

    # Check 4: Units are assigned
    project = model.by_type("IfcProject")[0] if model.by_type("IfcProject") else None
    if project and not project.UnitsInContext:
        errors.append("CRITICAL: No units assigned to project")

    # Check 5: IFC2X3 OwnerHistory requirement
    if model.schema == "IFC2X3":
        for entity in model.by_type("IfcRoot"):
            if entity.OwnerHistory is None:
                errors.append(
                    f"ERROR: IFC2X3 requires OwnerHistory on "
                    f"{entity.is_a()} '{entity.Name}' (#{entity.id()})")

    return errors
```

#### Pattern 6: Multi-File Batch Processing

```python
## Context: Standalone Python
## Version: IfcOpenShell 0.8.x
import ifcopenshell
import ifcopenshell.api
from pathlib import Path

def enrich_models(input_dir: str, output_dir: str, classification_system: str):
    """Add classification references to all IFC files in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for ifc_file in input_path.glob("*.ifc"):
        model = ifcopenshell.open(str(ifc_file))

        # Add classification system if not present
        classifications = model.by_type("IfcClassification")
        if not any(c.Name == classification_system for c in classifications):
            classification = ifcopenshell.api.run(
                "classification.add_classification", model,
                classification=classification_system)
        else:
            classification = next(
                c for c in classifications if c.Name == classification_system)

        # Process each element
        for wall in model.by_type("IfcWall"):
            ifcopenshell.api.run("classification.add_reference", model,
                products=[wall],
                classification=classification,
                identification="21.22",
                name="Exterior Walls")

        output_file = output_path / ifc_file.name
        model.write(str(output_file))
```

---

### Cross-Technology API Integration Points

#### IfcOpenShell <-> Blender (Without Bonsai)

| IfcOpenShell Operation | Blender Equivalent | Integration Point |
|----------------------|-------------------|-------------------|
| `ifcopenshell.geom.create_shape()` | `mesh.from_pydata(verts, [], faces)` | Geometry extraction: shape.geometry.verts/faces |
| `element.ObjectPlacement` | `obj.matrix_world` | 4x4 transformation matrix |
| `model.by_type("IfcWall")` | `bpy.data.objects` filtering | Element enumeration |
| IFC materials | `bpy.data.materials` | Manual mapping required |

#### IfcOpenShell <-> Bonsai

| IfcOpenShell Operation | Bonsai Equivalent | Notes |
|----------------------|------------------|-------|
| `ifcopenshell.api.run(cmd, model, **kw)` | `tool.Ifc.run(cmd, **kw)` | Bonsai wraps the API; model is implicit |
| `ifcopenshell.open(path)` | `IfcStore.get_file()` | NEVER open separately when Bonsai is active |
| `element.id()` | `obj.BIMProperties.ifc_definition_id` | Bidirectional mapping via IfcStore.id_map |
| `element.GlobalId` | `IfcStore.guid_map` | Bidirectional GUID-to-object lookup |

#### Bonsai <-> Blender

| Bonsai Operation | Blender Equivalent | Sync Rule |
|-----------------|-------------------|-----------|
| `bpy.ops.bim.add_wall()` | Creates mesh + IFC entity | Automatic bidirectional sync |
| IFC placement change | `obj.location` / `obj.matrix_world` | MUST call `bpy.ops.bim.edit_object_placement()` |
| `pset.edit_pset()` | BIM property panels | Panel shows live IFC data |
| `IfcStore.edited_objs` | Modified Blender objects | Pending IFC changes queue |

---

### Version Compatibility Matrix

| Feature | IFC2X3 | IFC4 | IFC4X3 | Notes |
|---------|--------|------|--------|-------|
| OwnerHistory | REQUIRED | OPTIONAL | OPTIONAL | Set via `owner.set_user` before entity creation |
| IfcWallStandardCase | Available | DEPRECATED | DEPRECATED | Use IfcWall with PredefinedType instead |
| IfcFacility | N/A | N/A | Available | Generalization of IfcBuilding for infrastructure |
| IfcAlignment | N/A | N/A | Available | Linear infrastructure alignment |
| IfcDoorType | N/A (use IfcDoorStyle) | Available | Available | |
| IfcWindowType | N/A (use IfcWindowStyle) | Available | Available | |
| Property set types | IfcPropertySingleValue | + Bounded, Table, List | + Bounded, Table, List | |
| Material sets | IfcMaterialList | + IfcMaterialConstituentSet | + IfcMaterialConstituentSet | |

| Feature | Blender 3.x | Blender 4.x | Blender 5.x | Notes |
|---------|-------------|-------------|-------------|-------|
| bgl module | Available | Deprecated | REMOVED | Use `gpu` module for all drawing |
| Extension system | N/A | Available (4.2+) | Required | bl_info replaced by blender_manifest.toml |
| Bonsai compatibility | Pre-rename (BlenderBIM) | Bonsai v0.8.x | Bonsai v0.8.x+ | ALWAYS use `bonsai.*` imports |
| Grease Pencil API | Legacy | Rewritten (4.3) | New API | Complete API break in 4.3 |

---

### Common Operations Quick Reference

#### Property Set Management Across Contexts

```python
## Standalone IfcOpenShell: Read properties
import ifcopenshell.util.element
psets = ifcopenshell.util.element.get_psets(element)
value = psets.get("Pset_WallCommon", {}).get("IsExternal")

## Standalone IfcOpenShell: Write properties
pset = ifcopenshell.api.run("pset.add_pset", model,
    product=element, name="Pset_WallCommon")
ifcopenshell.api.run("pset.edit_pset", model, pset=pset,
    properties={"IsExternal": True})

## Bonsai context: Read properties (same IfcOpenShell util)
model = IfcStore.get_file()
entity = tool.Ifc.get_entity(bpy.context.active_object)
psets = ifcopenshell.util.element.get_psets(entity)

## Bonsai context: Write properties (same API)
ifcopenshell.api.run("pset.edit_pset", model, pset=pset,
    properties={"IsExternal": True})
```

#### Spatial Hierarchy Traversal

```python
## Get container of an element
import ifcopenshell.util.element
container = ifcopenshell.util.element.get_container(element)
## Returns: IfcBuildingStorey, IfcSpace, or None

## Get all elements in a storey
elements = ifcopenshell.util.element.get_decomposition(storey)

## Walk full spatial tree
def walk_spatial(element, depth=0):
    print("  " * depth + f"{element.is_a()}: {element.Name}")
    for rel in getattr(element, "IsDecomposedBy", []):
        for child in rel.RelatedObjects:
            walk_spatial(child, depth + 1)
    for rel in getattr(element, "ContainsElements", []):
        for child in rel.RelatedElements:
            walk_spatial(child, depth + 1)

project = model.by_type("IfcProject")[0]
walk_spatial(project)
```

---

### Reference Links

- [Cross-Technology API Methods](references/methods.md) — Complete integration point signatures
- [End-to-End Workflow Examples](references/examples.md) — Full working examples for common BIM workflows
- [Cross-Tech Anti-Patterns](references/anti-patterns.md) — Common integration mistakes and how to avoid them

### Sources

- IfcOpenShell Documentation: https://docs.ifcopenshell.org
- IfcOpenShell API Reference: https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/index.html
- Bonsai Documentation: https://docs.bonsaibim.org
- Blender Python API: https://docs.blender.org/api/current/index.html
- IfcOpenShell GitHub: https://github.com/IfcOpenShell/IfcOpenShell
- OSArch Community: https://community.osarch.org
