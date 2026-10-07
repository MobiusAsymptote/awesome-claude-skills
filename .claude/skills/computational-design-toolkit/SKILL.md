---
name: computational-design-toolkit
description: >
  Computational design toolkit — 18 routed skills covering parametric modeling, geometry and
  mesh processing, generative design, structural and environmental simulation, facades,
  fabrication, BIM scripting, interoperability, optimization, and ML for AEC.
source: https://github.com/Amanbh997/Claude-skills-for-Computational-Designers (MIT, Abhinav Bhardwaj)
version: 1.0.0
---

# Computational Design Toolkit — 18 skills, one file

Compiled from *Claude Skills for Computational Designers* v1.0.0 (MIT). Companion reference/template files are not included.

## Router

| Skill | Use when |
|---|---|
| **Foundation** | |
| [Computational Design Foundations](#cd-foundations) | Auto-activating foundation layer providing computational design paradigms, key pioneers, tools landscape, core concepts, and skill routing for all AEC computational design tasks |
| **Core design** | |
| [Parametric Modeling](#parametric-modeling) | Parametric design methodology, data structures, constraint systems, Grasshopper and Dynamo patterns, parameter space exploration, and associative geometry for AEC computational design |
| [Computational Geometry](#computational-geometry) | NURBS curves and surfaces, mesh geometry, boolean operations, subdivision surfaces, tessellation methods, surface analysis, and point cloud processing for AEC computational design |
| [Mesh Processing](#mesh-processing) | Mesh data structures, mesh operations, mesh analysis, mesh repair, UV mapping and unfolding, quad meshing, mesh-to-NURBS conversion, and mesh quality assessment for AEC computational design |
| [Algorithmic Patterns](#algorithmic-patterns) | L-systems, cellular automata, agent-based modeling, swarm intelligence, reaction-diffusion, growth algorithms, packing algorithms, and nature-inspired computation for AEC design |
| [Generative Design](#generative-design) | Evolutionary algorithms, multi-objective optimization, design space exploration, fitness function design, population-based methods, and generative workflows for AEC computational design |
| [Design Automation](#design-automation) | Rule-based design systems, constraint satisfaction, space planning algorithms, automated layout generation, drawing automation, code compliance checking, and computational workflows for AEC design automation |
| **Analysis & simulation** | |
| [Structural Computation](#structural-computation) | Finite element analysis fundamentals, form-finding methods, shell and gridshell structures, topology optimization, structural optimization, material-aware computation, and computational structural tools for AEC |
| [Environmental Simulation](#environmental-simulation) | Daylight analysis, solar radiation, energy simulation, CFD wind analysis, thermal comfort, acoustic simulation, and the Ladybug Tools ecosystem for performance-driven AEC computational design |
| [Data-Driven Design](#data-driven-design) | GIS integration, sensor data, occupancy analytics, space syntax analysis, urban data analytics, climate data processing, and API data sources for evidence-based AEC computational design |
| **Facades & fabrication** | |
| [Facade Computation](#facade-computation) | Panelization strategies, surface rationalization, attractor-based patterning, double-skin facades, kinetic and responsive facades, environmental performance facades, and fabrication-aware facade design for AEC |
| [Digital Fabrication](#digital-fabrication) | CNC milling, robotic fabrication, additive manufacturing, laser cutting, timber joinery, formwork design, assembly sequencing, and file preparation for digitally-fabricated AEC components |
| **BIM & interoperability** | |
| [BIM Scripting](#bim-scripting) | Revit API fundamentals, Dynamo for Revit, pyRevit framework, IFC schema and openBIM, model checking, automated documentation, clash detection, and BIM interoperability tools for AEC computational design |
| [Interoperability](#interoperability) | File format encyclopedia, data exchange strategies, API integration patterns, Grasshopper-to-Revit pipelines, Rhino.Inside workflows, Speckle data streams, and schema mapping for AEC computational design |
| [Scripting Reference](#scripting-reference) | Python for Rhino and Grasshopper (RhinoCommon, rhinoscriptsyntax, ghpythonlib), C# for Grasshopper components, Python for Revit (pyRevit, RevitPythonShell), JavaScript for web 3D (Three.js), and code patterns for AEC computational design |
| **Optimization & intelligence** | |
| [Optimization Methods](#optimization-methods) | Genetic algorithms, simulated annealing, particle swarm optimization, gradient-based methods, topology optimization, shape optimization, size optimization, and benchmark problems for AEC computational design |
| [Machine Learning for AEC](#ml-for-aec) | Computer vision for buildings, image-to-floorplan, generative ML models, performance prediction, structural analysis ML, energy prediction, natural language to design, and point cloud ML for AEC computational design |
| [Computational Design Calculator](#cd-calculator) | Python calculators for geometry analysis, structural checking, solar calculations, panel optimization, mesh analysis, material estimation, and fabrication cost estimation for AEC computational design |

---

# Foundation


## cd-foundations

### Computational Design Foundations

> Auto-activating foundation layer providing computational design paradigms, key pioneers, tools landscape, core concepts, and skill routing for all AEC computational design tasks

## Computational Design Foundations

This skill auto-activates whenever a computational design context is detected. It provides the foundational knowledge layer, paradigm classification, tool routing, and anti-pattern awareness that underpins every other skill in the Computational Design Skills Plugin.

---

### 1. Computational Design Paradigm Overview

Computational design is not a single methodology but a spectrum of interrelated paradigms. Each paradigm carries distinct assumptions about the relationship between the designer, the algorithm, and the artifact. Understanding which paradigm applies to a given problem is the first critical decision in any computational design workflow.

#### 1.1 Parametric Design

**Definition:** Parametric design establishes explicit relationships between design elements through variable parameters and constraints, enabling the exploration of a continuous design space by adjusting input values. The geometry is not drawn; it is described as a system of dependencies.

**Key Characteristics:**
- Associative relationships between geometry elements (change one parameter, downstream geometry updates)
- Design intent is encoded as a graph of operations, not a static drawing
- Enables rapid iteration and variant generation from a single model definition
- Parameters can be numeric (dimensions), geometric (reference curves), or categorical (material type)

**When to Use:** When the design problem has well-defined variables and the goal is to explore a constrained solution space — e.g., facade panel optimization, structural member sizing, massing studies with fixed programmatic requirements, and any scenario where rapid iteration across known parameters is valuable.

#### 1.2 Generative Design

**Definition:** Generative design delegates part of the design ideation to algorithmic processes that produce novel solutions based on goals, constraints, and evaluation criteria. The designer defines the problem space and fitness criteria; the algorithm proposes solutions the designer may not have conceived.

**Key Characteristics:**
- Goal-oriented: the designer specifies objectives (minimize material, maximize daylight, optimize circulation)
- Produces many candidate solutions rather than a single output
- Requires a fitness function or multi-objective evaluation framework
- Often employs evolutionary algorithms, agent-based systems, or stochastic search
- The designer's role shifts from form-maker to problem-framer and solution-curator

**When to Use:** When the solution space is too large for manual exploration, when multiple conflicting objectives must be balanced (structural performance vs. daylighting vs. cost), when design innovation is prioritized over predictability, or when the problem can be meaningfully quantified.

#### 1.3 Algorithmic Design

**Definition:** Algorithmic design uses step-by-step computational procedures — loops, conditionals, recursion, data transformations — to generate or manipulate geometry and spatial configurations. It treats design as a computational process expressible in code or visual programming.

**Key Characteristics:**
- Procedural logic: if/then branching, iteration, recursion
- Deterministic or stochastic depending on algorithm type
- Can encode complex rules (zoning regulations, structural grammars, spatial syntax rules)
- Bridges the gap between design logic and code
- Enables rule-based generation (shape grammars, L-systems, cellular automata)

**When to Use:** When the design can be described by a set of rules or procedures — e.g., space allocation by adjacency matrix, facade patterning by rule sets, urban block generation from regulatory codes, structural branching systems, or any design task that benefits from codified logic.

#### 1.4 Data-Driven Design

**Definition:** Data-driven design integrates real-world datasets — environmental, demographic, geospatial, behavioral, sensor-based — directly into the design process, allowing external information to inform or drive geometric and spatial decisions.

**Key Characteristics:**
- Real-world data as design input (GIS layers, weather files, pedestrian counts, census data)
- Requires data acquisition, cleaning, transformation, and mapping to design parameters
- Enables evidence-based design decisions
- Often combined with parametric or generative workflows
- Visualization and analytics are integral to the design process

**When to Use:** When site-specific conditions must directly inform design — e.g., solar exposure driving facade design, wind data informing massing, population density shaping program distribution, traffic data determining access points, or sensor data driving adaptive building systems.

#### 1.5 Performance-Driven Design

**Definition:** Performance-driven design places quantifiable performance metrics — structural efficiency, energy consumption, daylight autonomy, acoustic quality, thermal comfort — at the center of the design process, using simulation feedback loops to iteratively refine form and materiality.

**Key Characteristics:**
- Simulation-in-the-loop: design decisions are evaluated against performance models at every iteration
- Requires validated simulation engines (EnergyPlus, Radiance, FEA solvers)
- Multi-physics coupling: thermal, structural, lighting, acoustic, aerodynamic
- Performance targets as hard constraints or optimization objectives
- Demands understanding of both design and engineering domains

**When to Use:** When building performance is a primary driver — e.g., net-zero energy targets, structural weight minimization, acoustic optimization for concert halls, daylight optimization for workplaces, wind comfort in urban canyons, or any project where quantifiable metrics must be met or optimized.

---

### 2. Pioneers & Key Figures Quick-Reference Table

The following table provides a rapid lookup of the most influential figures in computational design. For detailed biographies, projects, and publications, see `references/pioneers-and-movements.md`.

| # | Name | Key Contribution | Primary Domain | Relevance to Practice |
|---|------|-----------------|----------------|----------------------|
| 1 | **Patrik Schumacher** | Parametricism manifesto; codified parametric design as an architectural movement and style | Architectural Theory, Parametric Design | Provided theoretical framework for parametric architecture as a unified design language for the 21st century |
| 2 | **Greg Lynn** | Animate Form (1999); pioneered blob architecture and calculus-based form generation | Digital Morphogenesis | Introduced time-based, force-driven form generation to architecture; catalyzed NURBS-based design |
| 3 | **Neri Oxman** | Material Ecology; multi-material 3D printing; biology-informed computational fabrication | Material Computation, Bio-Design | Bridged computational design, biology, and material science; redefined fabrication paradigms |
| 4 | **Achim Menges** | ICD/ITKE Stuttgart research pavilions; material computation; robotic fabrication | Material Computation, Fabrication | Demonstrated that material behavior and fabrication constraints can drive design form generation |
| 5 | **Mark Burry** | Digital completion of Sagrada Familia; pioneered practical application of parametric modeling to complex geometry | Parametric Modeling, Heritage | Proved parametric tools could resolve geometries impossible to build by traditional means |
| 6 | **Zaha Hadid** | Parametric architecture at building and urban scale; fluid formal language through computational methods | Parametric Architecture | Demonstrated computational design at the highest level of architectural practice and cultural ambition |
| 7 | **Toyo Ito** | Algorithmic structural systems; Sendai Mediatheque; Serpentine Pavilion algorithm | Algorithmic Structure | Showed how algorithmic thinking produces structurally innovative, spatially rich architecture |
| 8 | **Cecil Balmond** | Informal structural design; non-linear structural logic; collaboration with OMA, Toyo Ito | Structural Design | Redefined structural engineering as a creative, algorithmic discipline inseparable from architecture |
| 9 | **Frei Otto** | Form-finding with physical models (soap films, hanging chains); Institute for Lightweight Structures | Form-Finding, Minimal Surfaces | Established the foundational methods of form-finding that digital tools now simulate computationally |
| 10 | **Buckminster Fuller** | Geodesic domes; tensegrity structures; synergetics; design science | Structural Systems, Systems Thinking | Pioneered systematic, geometry-driven approaches to structural efficiency at every scale |
| 11 | **Sergio Musmeci** | Ponte sul Basento; sculptural structural form-finding through physical and mathematical models | Structural Art | Demonstrated that structural optimization produces forms of extraordinary beauty and efficiency |
| 12 | **Mike Weinstock** | Morphogenetic design theory; Emergence and Design Group at AA | Morphogenetic Design, Theory | Provided theoretical framework connecting biological morphogenesis to architectural design processes |
| 13 | **Skylar Tibbits** | Self-Assembly Lab MIT; 4D printing; programmable materials | Self-Assembly, Smart Materials | Extended computational design into time-based material behavior and autonomous construction |
| 14 | **Mario Carpo** | The Digital Turn in Architecture (2012); The Second Digital Turn (2017); historiography of digital design | Theory, History | Articulated the cultural and epistemological implications of computational design for architecture |
| 15 | **Antoine Picon** | Digital Culture in Architecture; Smart Cities: A Spatialised Intelligence | Theory, Digital Culture | Connected computational design to broader cultural, political, and philosophical frameworks |
| 16 | **Kostas Terzidis** | Algorithmic Architecture (2006); Expressive Form; rigorous computational approaches to design | Algorithmic Design, Theory | Provided rigorous definitions distinguishing algorithmic, parametric, and computational design |
| 17 | **Branko Kolarevic** | Architecture in the Digital Age (2003); digital manufacturing and mass customization | Digital Fabrication | Documented and theorized the link between digital design and digitally controlled manufacturing |
| 18 | **Philippe Block** | Block Research Group ETHZ; funicular structures; 3D graphic statics; COMPAS framework | Structural Design, Form-Finding | Revived and digitized graphic statics; enabled unreinforced masonry shell design through computation |
| 19 | **Sigrid Adriaenssens** | Form-finding and structural optimization; computational mechanics for thin shells | Structural Optimization | Advanced computational methods for form-finding of structurally efficient thin-shell structures |
| 20 | **Caitlin Mueller** | Digital Structures Group MIT; structural optimization; machine learning for structural design | Structural Optimization, ML | Pioneered the integration of machine learning with structural design optimization for early-stage design |
| 21 | **Michael Hansmeyer** | Computational architecture and ornament; subdivided columns; Grotto project | Algorithmic Ornament | Demonstrated that computation enables geometric complexity far beyond human manual capacity |
| 22 | **Jenny Sabin** | Jenny Sabin Studio; material research through knitting and weaving; bio-inspired pavilions | Material Computation, Textiles | Bridged textile fabrication, biology, and computational design at architectural scale |
| 23 | **Ronald Rael** | Emerging Objects; large-scale 3D printing with sustainable materials (clay, salt, cement) | Additive Manufacturing | Pioneered sustainable material palettes for large-scale architectural 3D printing |

---

### 3. Tools Landscape Matrix

The computational design tools ecosystem spans parametric modeling, simulation, fabrication, and interoperability. For detailed tool descriptions, version info, and workflows, see `references/tools-ecosystem.md`.

#### 3.1 Parametric Modeling Tools

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size | Notes |
|------|----------|-------------|----------------------|----------------|-------|
| **Grasshopper** | Rhino 7/8 | Visual parametric modeling, algorithmic design | 3 | Very Large | De facto standard for computational design in architecture |
| **Dynamo** | Revit, Civil 3D, Advance Steel | BIM automation, parametric modeling within Revit | 3 | Large | Tightly integrated with Autodesk BIM ecosystem |
| **Marionette** | Vectorworks | Parametric modeling within Vectorworks | 2 | Small | Python-based; good for Vectorworks-centric firms |
| **GenerativeComponents** | Bentley MicroStation | Parametric infrastructure and building design | 4 | Small | Strong in infrastructure; less common in architecture |
| **Houdini** | Standalone (SideFX) | Procedural modeling, simulation, VFX-grade geometry | 5 | Medium (growing in AEC) | Extremely powerful procedural engine; steep learning curve |

#### 3.2 Visual Programming Environments

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size |
|------|----------|-------------|----------------------|----------------|
| **Grasshopper** | Rhino | Full visual programming for geometry and data | 3 | Very Large |
| **Dynamo** | Revit | Visual programming for BIM workflows | 3 | Large |
| **Sverchok** | Blender | Parametric geometry nodes for Blender | 3 | Medium |
| **Geometry Nodes** | Blender 3.0+ | Native procedural geometry system in Blender | 3 | Large (growing) |
| **Nodes** | Various | General-purpose visual programming | 2 | Small |

#### 3.3 Environmental Analysis Tools

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size |
|------|----------|-------------|----------------------|----------------|
| **Ladybug** | Grasshopper, Dynamo | Weather data visualization, sun path, radiation | 3 | Large |
| **Honeybee** | Grasshopper, Dynamo | Energy modeling (EnergyPlus/OpenStudio), daylight (Radiance) | 4 | Large |
| **Butterfly** | Grasshopper | CFD simulation (OpenFOAM wrapper) | 4 | Medium |
| **Dragonfly** | Grasshopper | Urban-scale energy modeling, urban heat island | 4 | Medium |
| **ClimateStudio** | Rhino | Annual daylight, thermal, glare simulation | 3 | Medium |
| **DIVA for Rhino** | Rhino | Daylight and energy modeling | 3 | Medium |
| **Eddy3D** | Grasshopper | Real-time CFD for wind analysis | 3 | Small |

#### 3.4 Structural Analysis & Optimization Tools

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size |
|------|----------|-------------|----------------------|----------------|
| **Karamba3D** | Grasshopper | Interactive structural FEA for parametric models | 4 | Medium |
| **Millipede** | Grasshopper | Topology optimization | 3 | Small |
| **Kangaroo** | Grasshopper | Physics simulation, form-finding, dynamic relaxation | 3 | Large |
| **Galapagos** | Grasshopper | Evolutionary solver (single/dual objective) | 2 | Large (built-in) |
| **Ameba** | Grasshopper, Rhino | Topology optimization for architecture | 3 | Small |
| **BESO** | Various | Bi-directional evolutionary structural optimization | 4 | Small |
| **Colibri** | Grasshopper | Design space exploration and data capture | 2 | Medium |
| **Opossum** | Grasshopper | Model-based optimization (RBF surrogate) | 3 | Small |

#### 3.5 Fabrication & Robotics Tools

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size |
|------|----------|-------------|----------------------|----------------|
| **HAL Robotics** | Grasshopper | Industrial robot programming (ABB, KUKA, UR) | 4 | Medium |
| **KUKA\|prc** | Grasshopper | KUKA robot programming and simulation | 4 | Medium |
| **Robots** | Grasshopper | Multi-brand robot programming | 3 | Small |
| **Silkworm** | Grasshopper | Custom G-code generation for 3D printing | 3 | Small |
| **Taco** | Grasshopper | IFC import/export for BIM interop | 2 | Small |
| **Elefront** | Grasshopper | Baking management, attribute handling | 2 | Medium |
| **Pufferfish** | Grasshopper | Tweens, morphing, blending geometry | 2 | Medium |

#### 3.6 Interoperability & Data Exchange Tools

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size |
|------|----------|-------------|----------------------|----------------|
| **Speckle** | Multi-platform | Open-source data exchange and collaboration | 2 | Large (growing) |
| **Rhino.Inside** | Revit, others | Embed Rhino/Grasshopper inside Revit and other apps | 3 | Medium |
| **BHoM** | Multi-platform | Buildings and Habitats object Model; open interop | 4 | Medium |
| **IFC.js** | Web | IFC parsing and visualization in browser | 3 | Medium |
| **xBIM** | .NET | IFC toolkit for BIM development | 4 | Medium |
| **IfcOpenShell** | Python | Open-source IFC geometry engine and parser | 3 | Medium |

#### 3.7 Data, ML & Visualization Tools

| Tool | Platform | Primary Use | Learning Curve (1-5) | Community Size |
|------|----------|-------------|----------------------|----------------|
| **LunchBox** | Grasshopper | Paneling, data management, ML basics | 2 | Large |
| **Elk** | Grasshopper | OpenStreetMap data import, GIS mapping | 2 | Medium |
| **Heron** | Grasshopper | GIS data import (rasters, shapefiles) | 2 | Medium |
| **TT Toolbox** | Grasshopper | Data management, geometry utilities | 2 | Medium |
| **Owl** | Grasshopper | Machine learning integration (Accord.NET) | 4 | Small |
| **Brain** | Grasshopper | Neural network training inside Grasshopper | 3 | Small |
| **Lark** | Grasshopper | Spectral daylight analysis | 3 | Small |
| **Decoding Spaces** | Grasshopper | Urban analysis (isovist, visibility, network) | 3 | Small |

---

### 4. Core Concepts Quick Reference

For in-depth explanations and mathematical foundations, see `references/core-concepts.md`.

#### 4.1 Data Structures

| Concept | Definition | AEC Example |
|---------|-----------|-------------|
| **List** | Ordered collection of items accessible by index | A list of floor-to-floor heights for a tower: {3.5, 3.2, 3.2, 3.0, 3.0, ...} |
| **Data Tree** | Hierarchical, nested list structure unique to Grasshopper | Building floors (branches) containing rooms (items per branch) |
| **Dictionary** | Key-value pairs for named data access | Room names mapped to areas: {"Office A": 45.2, "Meeting": 22.0} |
| **Graph** | Nodes and edges representing relationships | Spatial adjacency graph: nodes = rooms, edges = required adjacencies |
| **Mesh** | Vertices, edges, faces topology for surface representation | Building envelope represented as quad mesh for panelization |

#### 4.2 Geometric Concepts

| Concept | Definition | AEC Relevance |
|---------|-----------|---------------|
| **NURBS** | Non-Uniform Rational B-Splines; smooth curves/surfaces defined by control points, knots, degree | Free-form facade geometry, complex roof surfaces, organic massing |
| **Degree** | Polynomial degree of a NURBS curve (1=linear, 2=arc-like, 3=smooth) | Controls curvature continuity at joints; degree 3 standard for smooth surfaces |
| **Control Points** | Points that influence (but don't lie on) a NURBS curve/surface | Adjusting control points reshapes geometry without breaking continuity |
| **Knot Vector** | Sequence controlling parameter distribution along a NURBS curve | Determines where control points have most influence; uniform vs. non-uniform |
| **Boolean Operations** | Union, difference, intersection of solid volumes | Combining building masses, cutting openings, creating floor plates from massing |
| **Voronoi Diagram** | Partition of space into regions closest to each seed point | Floor plan subdivision, facade paneling patterns, structural diagrid generation |
| **Delaunay Triangulation** | Triangulation maximizing minimum angle; dual of Voronoi | Terrain mesh generation, structural surface triangulation, point cloud meshing |
| **Subdivision Surfaces** | Iterative mesh refinement for smooth surfaces (Catmull-Clark, Loop) | Smooth facade panels from coarse control meshes; organic form generation |
| **UV Space** | 2-parameter coordinate system on a surface (0-1 range in each direction) | Mapping patterns, panels, or analysis results onto curved surfaces |

#### 4.3 Optimization Concepts

| Concept | Definition | AEC Relevance |
|---------|-----------|---------------|
| **Genetic Algorithm** | Evolutionary search using selection, crossover, mutation on a population | Multi-objective building optimization (energy, daylight, cost) |
| **Fitness Function** | Quantitative measure of solution quality in optimization | Daylight autonomy percentage, structural weight, energy use intensity |
| **Pareto Front** | Set of non-dominated solutions in multi-objective optimization | Trade-off visualization between conflicting objectives (cost vs. performance) |
| **Topology Optimization** | Material distribution optimization within a design domain | Structural member layout, floor plate opening placement, facade density |
| **Gradient Descent** | Iterative optimization following the steepest descent of objective function | Fast convergence for smooth, single-objective problems with known gradients |
| **Simulated Annealing** | Probabilistic optimization with decreasing randomness over time | Escaping local optima in complex design spaces; layout optimization |
| **Swarm Intelligence** | Optimization inspired by collective behavior (PSO, ant colony) | Urban layout optimization, pedestrian flow simulation |

#### 4.4 Fabrication Concepts

| Concept | Definition | AEC Relevance |
|---------|-----------|---------------|
| **Panelization** | Decomposing a surface into manufacturable panels (planar, single-curved, doubly-curved) | Facade rationalization; minimizing unique panel types for cost reduction |
| **Rationalization** | Simplifying complex geometry for feasible fabrication | Converting free-form surfaces to planar quads or developable strips |
| **Robotic Toolpath** | Sequence of spatial positions and orientations for a robotic end-effector | Robotic hot-wire cutting, 3D printing, bricklaying, welding |
| **G-code** | Machine instruction language for CNC and 3D printing | Controlling 3-axis CNC mills, laser cutters, FDM printers |
| **Nesting** | Optimal arrangement of 2D parts on sheet material to minimize waste | CNC cutting of facade panels, plywood formwork, sheet metal parts |
| **Kerf Bending** | Cutting parallel slots to allow sheet material to bend | Making planar sheet material conform to curved formwork |
| **Unrolling/Flattening** | Mapping a 3D surface to a flat 2D pattern | Developable surfaces for metal cladding; fabric cutting patterns |

#### 4.5 Interoperability Concepts

| Concept | Definition | AEC Relevance |
|---------|-----------|---------------|
| **IFC Schema** | Industry Foundation Classes; open BIM data standard (ISO 16739) | Exchanging building models between Revit, ArchiCAD, Tekla, etc. |
| **LOD/LOI** | Level of Development / Level of Information for BIM elements | Defining how much geometric and data detail a BIM element carries at each project stage |
| **Digital Twin** | Real-time digital replica of a physical asset fed by sensor data | Building operations, predictive maintenance, energy management |
| **gbXML** | Green Building XML; schema for transferring building energy model data | Energy simulation model exchange between design and analysis tools |
| **Speckle Stream** | Version-controlled, real-time data channel for design collaboration | Live syncing geometry between Grasshopper, Revit, Unity, web dashboards |

---

### 5. Design Paradigm Decision Tree

Use this decision tree to determine which computational design paradigm and toolset best fits a given design problem.

```
START: What is the primary design challenge?
|
+-- [A] "I need to explore variations of a known design concept"
|   |
|   +-- Are the variables well-defined and bounded?
|       +-- YES --> PARAMETRIC DESIGN
|       |   Tools: Grasshopper, Dynamo
|       |   Skills: parametric-modeling, surface-rationalization
|       |
|       +-- NO --> GENERATIVE DESIGN
|           Tools: Grasshopper + Galapagos/Octopus, Dynamo + Refinery
|           Skills: generative-design, optimization-solvers
|
+-- [B] "I need to generate designs from rules or procedures"
|   |
|   +-- Are rules geometric (shapes, patterns)?
|   |   +-- YES --> ALGORITHMIC DESIGN (Shape Grammars, L-Systems)
|   |   |   Tools: Grasshopper, Python scripting, Processing
|   |   |   Skills: algorithmic-patterns, form-generation
|   |   |
|   |   +-- NO (rules are spatial/programmatic) --> ALGORITHMIC DESIGN (Space Planning)
|   |       Tools: Grasshopper, custom Python, Dynamo
|   |       Skills: space-planning, graph-based-layout
|   |
+-- [C] "I need to optimize for measurable performance"
|   |
|   +-- Which performance domain?
|       +-- Structural --> PERFORMANCE-DRIVEN (Structural)
|       |   Tools: Karamba3D, Kangaroo, Millipede
|       |   Skills: structural-optimization, form-finding
|       |
|       +-- Environmental (energy, daylight, wind) --> PERFORMANCE-DRIVEN (Environmental)
|       |   Tools: Ladybug/Honeybee, ClimateStudio, Butterfly/Eddy3D
|       |   Skills: environmental-analysis, climate-responsive-design
|       |
|       +-- Multi-objective --> GENERATIVE + PERFORMANCE-DRIVEN
|           Tools: Octopus, Opossum, Colibri + simulation tools
|           Skills: multi-objective-optimization, design-space-exploration
|
+-- [D] "I need to incorporate real-world data into design"
|   |
|   +-- What kind of data?
|       +-- GIS/Geospatial --> DATA-DRIVEN (GIS)
|       |   Tools: Elk, Heron, QGIS, ArcGIS
|       |   Skills: site-analysis, urban-data
|       |
|       +-- Sensor/IoT --> DATA-DRIVEN (Real-time)
|       |   Tools: Firefly, custom APIs, Speckle
|       |   Skills: responsive-systems, digital-twin
|       |
|       +-- Demographic/Programmatic --> DATA-DRIVEN (Programming)
|           Tools: Excel/CSV + Grasshopper, Python + Pandas
|           Skills: program-analysis, data-visualization
|
+-- [E] "I need to prepare design for manufacturing"
|   |
|   +-- What fabrication method?
|       +-- CNC (subtractive) --> FABRICATION
|       |   Tools: RhinoCAM, Grasshopper toolpath plugins
|       |   Skills: cnc-fabrication, nesting-optimization
|       |
|       +-- 3D Printing (additive) --> FABRICATION
|       |   Tools: Silkworm, custom G-code, slicer integration
|       |   Skills: additive-manufacturing, toolpath-generation
|       |
|       +-- Robotic --> FABRICATION (Robotic)
|       |   Tools: HAL Robotics, KUKA|prc, Robots
|       |   Skills: robotic-fabrication, toolpath-planning
|       |
|       +-- Formwork/Mold --> FABRICATION
|           Tools: Grasshopper + Unrolling, nesting plugins
|           Skills: formwork-design, surface-development
|
+-- [F] "I need to exchange data between platforms"
    |
    +-- INTEROPERABILITY
        Tools: Speckle, Rhino.Inside, BHoM, IfcOpenShell
        Skills: bim-interop, data-exchange
```

---

### 6. Anti-Pattern Catalog

These are the most common mistakes in computational design practice. Recognizing and avoiding them is as important as mastering the tools themselves.

#### 6.1 Over-Parametrization

**Description:** Creating a parametric model with dozens of sliders and parameters without a clear design intent or understanding of which parameters matter most. The result is an unmanageable definition where changing any slider produces unpredictable results.

**Symptoms:** 50+ sliders in a Grasshopper definition, no parameter hierarchy, parameters that interact chaotically, inability to explain what the model "does."

**Remedy:** Start with the minimum viable parameterization. Identify the 3-5 parameters that most affect design quality. Use sensitivity analysis to prune irrelevant parameters. Document the design intent each parameter serves.

#### 6.2 Black-Box Optimization

**Description:** Running an evolutionary solver without understanding the fitness landscape, the search space topology, or why the solver converges (or fails to converge) to particular solutions. The designer trusts the output without critical evaluation.

**Symptoms:** Accepting the first Galapagos/Octopus result without interrogating it, unable to explain why the "optimal" solution looks the way it does, no visualization of the fitness landscape.

**Remedy:** Always visualize the design space (use Colibri/Design Explorer). Understand what your fitness function actually rewards. Run the optimizer multiple times from different starting points. Critically evaluate whether the "optimal" solution makes architectural sense.

#### 6.3 Geometric Complexity Without Structural Logic

**Description:** Generating complex geometry (doubly-curved surfaces, branching structures, cellular forms) without any consideration of how forces flow through the structure or how it will be supported.

**Symptoms:** Beautiful renders that cannot be built, structural engineers rejecting the geometry entirely, massive structural redundancy to make arbitrary forms work.

**Remedy:** Integrate structural feedback early (Karamba3D, Kangaroo). Use form-finding methods that inherently produce structurally efficient shapes. Collaborate with structural engineers from the beginning, not after form is "finalized."

#### 6.4 Ignoring Fabrication Constraints

**Description:** Designing geometry that is theoretically elegant but practically impossible or prohibitively expensive to fabricate. Every panel is unique, curvature exceeds material bending limits, assembly sequence is impossible.

**Symptoms:** Thousands of unique panels, no consideration of material sheet sizes, tolerances ignored, no unfolding/nesting strategy, "we'll figure out fabrication later."

**Remedy:** Establish fabrication constraints as inputs to the parametric model, not afterthoughts. Rationalize surfaces early. Minimize unique component count. Consult fabricators during design, not after.

#### 6.5 Data Tree Mismatches (Grasshopper-Specific)

**Description:** Grasshopper data tree structures between components don't match, causing either no output, incorrect output, or explosive combinatorial results. This is the single most common Grasshopper debugging issue.

**Symptoms:** Components produce unexpected numbers of outputs, geometry appears in wrong locations, Param Viewer shows mismatched tree structures, "null" items throughout trees.

**Remedy:** Always use Param Viewer to inspect tree structures. Understand Grasshopper's matching rules (longest list, shortest list, cross-reference). Use Graft, Flatten, Simplify, and Path Mapper deliberately. Consider restructuring the definition to maintain clean data tree alignment.

#### 6.6 Resolution Mismatch

**Description:** Using different geometric resolutions for analysis and design — e.g., running energy simulation on a highly detailed architectural model, or performing structural analysis on geometry too coarse to capture critical features.

**Symptoms:** Simulations that take days instead of minutes, analysis results that don't correspond to the actual design, mesh-dependent results.

**Remedy:** Create purpose-specific geometric representations: a coarse massing model for energy, a refined mesh for structural analysis, a rationalized surface for fabrication. Establish clear LOD protocols for each analysis type.

#### 6.7 Premature Optimization

**Description:** Optimizing details before the overall design concept is established. Spending weeks optimizing facade panel angles when the building massing hasn't been resolved.

**Symptoms:** Highly optimized subsystem designs that become irrelevant when the overall design changes, wasted computation time, losing the forest for the trees.

**Remedy:** Follow a staged optimization approach: massing first, then systems, then components. Each stage should be sufficiently resolved before optimizing the next level of detail. Accept that early-stage models will be approximate.

#### 6.8 Tool-Driven Design

**Description:** Letting the capabilities and defaults of software tools dictate the design outcome. The design looks like "a Grasshopper project" rather than a response to site, program, and context.

**Symptoms:** Projects that look like Voronoi diagrams or attractor-field patterns because those are easy to generate, not because they serve a design purpose. Design intent is "I wanted to try this component."

**Remedy:** Start with the design question, not the tool. Define the problem, objectives, and constraints before opening Grasshopper. Use computational tools to explore and evaluate, not to generate the starting concept.

#### 6.9 Ignoring Interoperability From the Start

**Description:** Building an elaborate parametric model in one platform without considering how it will be exchanged with collaborators using different tools (structural engineer in SAP2000, contractor in Tekla, client in Revit).

**Symptoms:** Manual model rebuilding in every platform, data loss at every exchange, inconsistent models across disciplines, last-minute interoperability crises.

**Remedy:** Plan the data exchange workflow at project kickoff. Use open standards (IFC, gbXML) where possible. Adopt Speckle or similar platforms for live interop. Design the parametric model with exportability in mind (clean geometry, consistent naming).

#### 6.10 Over-Reliance on Visual Scripting for Complex Logic

**Description:** Building extremely complex logic — nested loops, recursive algorithms, database queries, file I/O — entirely in visual programming (Grasshopper/Dynamo) when text-based scripting would be far more readable, maintainable, and performant.

**Symptoms:** Grasshopper definitions with 500+ components that could be 100 lines of Python, spaghetti wires that no one can follow, extreme slowness from Grasshopper overhead on simple operations.

**Remedy:** Use GhPython/C# scripting components for complex logic. Move substantial algorithms into standalone Python libraries. Use visual scripting for geometry flow and high-level workflow orchestration; use code for data processing and algorithmic logic.

#### 6.11 No Version Control

**Description:** Working on computational design files without version control, relying on "Save As" with date-stamped filenames, losing the ability to track changes, revert, or collaborate effectively.

**Symptoms:** Folders full of "definition_v3_final_FINAL_v2.gh", no ability to diff or merge, lost work after crashes, inability to collaborate on the same definition.

**Remedy:** Use Git for version control. Grasshopper XML format is somewhat diffable. Use Speckle for geometry versioning. Adopt naming conventions and folder structures. Consider text-based representations (Python scripts, Hops definitions) for complex logic.

#### 6.12 Neglecting User Experience of the Definition

**Description:** Creating parametric definitions that only the author can use. No documentation, no logical grouping, no named groups, no input/output clarity.

**Symptoms:** Colleagues cannot use the definition, parameters have no labels or bounds, the definition breaks when anyone else touches it, knowledge leaves when the author leaves.

**Remedy:** Group and color-code definition sections. Label all inputs with human-readable names and valid ranges. Use Metahopper for documentation. Create a "user interface" cluster with exposed parameters. Write a companion document explaining the definition's logic.

---

### 7. Skill Router

This section routes to the appropriate specialized skill based on the user's computational design context. When the foundational layer detects a specific domain need, it activates the relevant skill.

#### Routing Table

| User Context / Keywords | Recommended Skill | Description |
|--------------------------|-------------------|-------------|
| Parametric modeling, Grasshopper definition, sliders, parameters | `parametric-modeling` | Core parametric modeling workflows and best practices |
| Generative design, evolutionary optimization, multi-objective | `generative-design` | Generative and evolutionary design strategies |
| Form-finding, minimal surfaces, hanging chain, Kangaroo | `form-finding` | Physics-based form-finding and dynamic relaxation |
| Structural analysis, FEA, Karamba, load paths | `structural-computation` | Computational structural analysis and optimization |
| Environmental analysis, energy, daylight, Ladybug, Honeybee | `environmental-simulation` | Environmental performance simulation workflows |
| Facade, panelization, rationalization, cladding | `surface-rationalization` | Surface panelization and fabrication rationalization |
| Robotic fabrication, CNC, 3D printing, toolpath | `digital-fabrication` | Digital fabrication and robotic manufacturing |
| Data exchange, IFC, Speckle, Rhino.Inside, BIM | `interoperability` | Cross-platform data exchange and BIM integration |
| Urban analysis, GIS, site data, morphology | `urban-computation` | Urban-scale computational analysis and generation |
| Python scripting, C#, code, algorithm | `scripting-for-designers` | Programming and scripting for computational designers |
| Machine learning, neural network, classification, prediction | `ml-for-design` | Machine learning applications in AEC design |
| Data visualization, dashboard, mapping | `data-visualization` | Design data visualization and communication |
| Topology optimization, material distribution | `topology-optimization` | Topology optimization methods and workflows |
| Mesh, subdivision, remeshing, geometry processing | `geometry-processing` | Computational geometry and mesh processing |
| Pattern, tessellation, tiling, ornament | `algorithmic-patterns` | Algorithmic pattern generation and tessellation |
| Responsive, adaptive, kinetic, smart materials | `responsive-systems` | Responsive and adaptive building systems |
| Workflow, pipeline, automation, batch processing | `workflow-automation` | Computational design workflow automation |

#### Routing Logic

```
1. Parse user query for domain-specific keywords
2. Match against routing table (multiple matches possible)
3. If single match: activate that skill directly
4. If multiple matches: present top 3 candidates with brief descriptions
5. If no match: remain in cd-foundations and provide general guidance
6. Always keep cd-foundations active as the knowledge base layer
```

---

### 8. References Section

The following reference files provide deeper knowledge for each foundational topic:

| Reference File | Content | Lines |
|---------------|---------|-------|
| `references/pioneers-and-movements.md` | Detailed biographies of 20+ computational design pioneers; 8 major movements with origins, tenets, projects, and current state | 400+ |
| `references/tools-ecosystem.md` | Complete tool descriptions, capabilities, licensing, workflows, integration points, community resources, plugin ecosystems | 400+ |
| `references/core-concepts.md` | Data structures, mathematical foundations, coordinate systems, tolerance, computational complexity, recursion/iteration patterns | 350+ |
| `references/learning-pathways.md` | Beginner-to-expert learning roadmaps by tool, by domain; key books, courses, conferences, communities, portfolio guidance | 300+ |

#### How to Use References

- **Quick Lookup:** Use the tables in this SKILL.md for rapid reference during conversations
- **Deep Dive:** When a user needs detailed explanations, consult the appropriate reference file
- **Teaching:** When explaining concepts to learners, use the learning-pathways.md to calibrate explanation depth
- **Tool Selection:** When recommending tools, cross-reference tools-ecosystem.md for detailed capabilities and limitations

#### External Resources

- Food4Rhino: https://www.food4rhino.com/ (Grasshopper plugin repository)
- Dynamo Package Manager: https://dynamopackages.com/
- Speckle: https://speckle.systems/
- COMPAS Framework: https://compas-dev.github.io/
- Ladybug Tools: https://www.ladybug.tools/
- ShapeDiver: https://shapediver.com/
- Hypar: https://hypar.io/
- McNeel Forum (Grasshopper): https://discourse.mcneel.com/c/grasshopper/
- Dynamo Forum: https://forum.dynamobim.com/
- Computational Design community: https://parametrichouse.com/

---

*This foundation layer remains active throughout all computational design interactions, providing paradigm context, tool awareness, and routing intelligence to specialized skills.*


---

# Core design


## parametric-modeling

### Parametric Modeling

> Parametric design methodology, data structures, constraint systems, Grasshopper and Dynamo patterns, parameter space exploration, and associative geometry for AEC computational design

## Parametric Modeling for AEC Computational Design

This skill provides a complete reference for parametric design methodology as applied to architecture, engineering, and construction. It covers the intellectual framework, data structures, constraint logic, tool-specific taxonomies for Grasshopper and Dynamo, associative geometry patterns, and professional best practices.

---

### 1. Parametric Thinking Methodology

#### 1.1 What Makes Design Parametric vs. Static

A static design is a fixed artifact — a single geometric configuration with hard-coded dimensions. Changing one element requires manually adjusting every dependent element. A parametric design is a system of relationships: a directed graph of inputs, transformations, and outputs where modifying any input propagates changes through the entire dependency chain automatically.

The distinction is not merely about sliders. Parametric thinking means encoding **design intent** rather than design outcome. The designer authors a set of rules that describe a family of possible designs, not a single instance.

**Key characteristics of parametric models:**
- **Dependency awareness** — Every element knows what it depends on and what depends on it.
- **Reversibility** — Changes propagate backward and forward through the logic chain without loss of intent.
- **Multiplicity** — A single definition produces an infinite set of valid design instances within the parameter space.
- **Traceability** — Every output can be traced back through the logic to its originating inputs.

#### 1.2 The Input-Logic-Output Paradigm

Every parametric definition follows a three-stage pipeline:

```
INPUTS              LOGIC                    OUTPUTS
───────────────     ─────────────────────    ──────────────────
Parameters          Transformations          Geometry
 - Sliders          - Mathematical ops       - Points, Curves
 - Toggles          - Geometric ops          - Surfaces, Solids
 - Points           - Conditional branching  - Meshes
 - Geometry refs    - Data restructuring     - Data (areas, etc.)
 - Data files       - Constraint solving     - Text, Reports
 - User text        - Optimization loops     - Fabrication data
```

**Inputs** define the design space. They must be carefully named, ranged, and organized so that every combination within the parameter space produces a valid (even if suboptimal) output.

**Logic** is the design intelligence — the rules, relationships, and transformations that encode the designer's intent. This is where computational design expertise lives.

**Outputs** are the artifacts consumed by downstream workflows: visualization, analysis, documentation, fabrication.

#### 1.3 Design Intent Encoding

The most critical skill in parametric modeling is translating design intent into computable relationships. This requires decomposing design decisions into:

1. **What is fixed** — Constraints that never change (site boundary, structural grid module, code-mandated setbacks).
2. **What varies** — Parameters the designer wants to explore (floor-to-floor height, facade panel density, roof curvature).
3. **What is derived** — Values calculated from other values (total floor area from footprint and floor count, structural member depth from span length).
4. **What is conditional** — Logic that switches behavior based on thresholds (if panel area > 2 m², subdivide; if slope > 15%, add retaining wall).

#### 1.4 Parameter Identification: Independent vs. Dependent Variables

**Independent variables** are the inputs the designer directly controls. They are the sliders, number inputs, point positions, and toggle switches at the top of the dependency graph. They have no upstream dependencies.

**Dependent variables** are computed from independent variables through the logic chain. They cannot be directly set — only influenced by changing their upstream inputs.

**Intermediate variables** sit between inputs and outputs. They are dependent on upstream inputs but serve as inputs to downstream logic. Identifying these is critical for modular definition design.

**Rules for parameter identification:**
- Start with the design question: "What do I want to explore?"
- List every dimension, proportion, count, and configuration option.
- Classify each as independent (I control it), dependent (it is calculated), or fixed (it never changes).
- Establish the direction of dependency: which parameters drive which.
- Identify feedback loops (rare but possible in optimization workflows).

#### 1.5 Constraint Hierarchies

Not all constraints are equal. Parametric models encode a hierarchy of constraint strength:

| Priority | Constraint Type | Example | Behavior |
|----------|----------------|---------|----------|
| 1 (Highest) | Legal/Code | Setback lines, FAR limits | Hard boundary, never violated |
| 2 | Structural | Maximum span, minimum depth | Hard boundary with safety factor |
| 3 | Functional | Minimum room area, corridor width | Soft boundary, can flex slightly |
| 4 | Environmental | Solar access, wind comfort | Optimization target, not hard limit |
| 5 | Aesthetic | Proportional ratios, rhythm | Preference, fully negotiable |
| 6 (Lowest) | Exploratory | Novel geometries, experiments | No constraint, free exploration |

Constraint hierarchies determine what happens when parameters conflict: higher-priority constraints override lower-priority ones.

#### 1.6 Associative vs. Explicit Modeling

**Explicit modeling** defines geometry by its absolute coordinates and dimensions. A wall is a box at position (0,0,0) with width 6m, height 3m, thickness 0.2m.

**Associative modeling** defines geometry by its relationships. A wall starts at point A, ends at point B, has height equal to floor-to-floor parameter minus slab thickness, and thickness from the wall-type lookup table. Moving point A moves the wall. Changing the floor height changes the wall height.

Associative modeling is the foundation of parametric design. Every geometry element is defined by its relationships, not its absolute state.

#### 1.7 When Parametric Is Appropriate vs. Overkill

**Use parametric when:**
- The design requires exploring many variations of the same system.
- Geometric relationships are complex and manually maintaining them is error-prone.
- The project involves repetitive elements with systematic variation (facade panels, structural bays, landscape modules).
- Design-analysis feedback loops demand rapid iteration.
- Fabrication requires precise geometric data extraction.
- The client or design process demands option comparison.

**Avoid parametric when:**
- The design is a one-off sculptural form with no systematic logic.
- The time to build the parametric definition exceeds the time saved by manual modeling.
- The team lacks the skills to maintain or modify the definition after the author leaves.
- The geometry is simple enough that direct modeling is faster and clearer.
- The project has no iteration phase — the design is fixed and only needs documentation.

---

### 2. Data Structures for Computational Design

#### 2.1 Lists (Flat Collections)

The most fundamental data structure. An ordered collection of elements accessed by zero-based index.

**Operations:**
- **Indexing** — Access element at position `i`. Zero-based in Grasshopper and Python; zero-based in Dynamo.
- **Slicing** — Extract a sub-list from index `a` to `b`. Python: `list[a:b]`. GH: `SubList`.
- **Appending** — Add element to end. GH: `Merge`. Dynamo: `List.AddItemToEnd`.
- **Inserting** — Add element at specific index.
- **Removing** — Remove by index or by value.
- **Reversing** — Reverse order. GH: `Reverse List`. Dynamo: `List.Reverse`.
- **Sorting** — Sort by value or by key. GH: `Sort List`. Dynamo: `List.SortByKey`.
- **Filtering** — Remove elements by condition. GH: `Cull Pattern`, `Dispatch`. Dynamo: `List.FilterByBoolMask`.

#### 2.2 Data Trees (Grasshopper)

Data trees are Grasshopper's hierarchical data structure — the single most important concept to master for productive Grasshopper work.

**Path Anatomy:**
A path is a sequence of integers in curly braces: `{A;B;C}`. Each integer represents a level in the hierarchy. A branch is a list of items at a specific path.

```
{0;0} → [item0, item1, item2]        Branch 0 of Group 0
{0;1} → [item3, item4]               Branch 1 of Group 0
{1;0} → [item5, item6, item7, item8] Branch 0 of Group 1
{1;1} → [item9]                      Branch 1 of Group 1
```

**Core Operations:**

| Operation | Effect | When to Use |
|-----------|--------|-------------|
| **Flatten** | Collapses all branches into a single list `{0}` | When you need all items regardless of structure |
| **Graft** | Wraps every item in its own branch | When you need each item processed independently |
| **Simplify** | Removes shared path prefix | When tree has unnecessarily deep paths |
| **Flip Matrix** | Transposes branches and indices (rows↔columns) | When you need to reorganize grid data |
| **Unflatten** | Restores tree structure from a flat list using a guide tree | When recovering structure after flat operations |
| **Prune** | Removes branches with fewer than N items | When cleaning sparse trees |
| **Trim** | Removes path levels from left or right | When aligning trees with different depth |
| **Path Mapper** | Remaps paths using lexical patterns | Advanced restructuring |

**Matching Algorithms:**

When two or more data trees enter a component with different structures, Grasshopper must decide how to pair items:

| Algorithm | Behavior | Use Case |
|-----------|----------|----------|
| **Longest List** | Repeats the last item of shorter lists | Default. Most common. |
| **Shortest List** | Truncates longer lists to match shortest | When pairing must be 1:1 with no repetition |
| **Cross Reference** | Every item paired with every other item | Combinatorial exploration (N×M results) |

#### 2.3 Nested Lists (Dynamo)

Dynamo uses nested Python-style lists instead of tree paths. A 2D list is a list of lists. A 3D list is a list of lists of lists.

**Levels and Lacing:**

Dynamo's `@L1`, `@L2` syntax specifies which nesting level a node should operate on:
- `@L1` — Operate on the outermost list.
- `@L2` — Operate on sub-lists within the outermost list.
- `@L3` — Operate on sub-sub-lists.

**Lacing options** control how inputs of different lengths combine:
- **Shortest** — Pairs items 1:1, truncates at shortest input.
- **Longest** — Pairs items 1:1, repeats last item of shorter input.
- **Cross Product** — Every combination of items from each input.

#### 2.4 Graphs and Networks

For topological relationships (adjacency, connectivity, flow), graph structures are essential:

- **Nodes** — Entities (rooms, intersections, structural joints).
- **Edges** — Connections between entities (corridors, roads, beams).
- **Directed vs. Undirected** — Whether connections have direction (water flow vs. adjacency).
- **Weighted edges** — Connections with associated values (distance, cost, capacity).

**AEC applications:** circulation analysis, structural load paths, utility routing, spatial adjacency diagrams, pedestrian flow networks.

#### 2.5 Dictionaries / Key-Value Pairs

Dictionaries map unique keys to values. Useful for:
- Associating metadata with geometry (panel ID → area, material, cost).
- Lookup tables (material name → thermal conductivity).
- Configuration storage (parameter name → value).

Grasshopper added native dictionary support in later versions. Dynamo supports dictionaries natively. Python scripting in both platforms has full dictionary support.

#### 2.6 Data Tree Manipulation Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Accidental flatten | All items in one branch, lost grouping | Use `Simplify` instead if paths are too deep |
| Graft before cross-reference | Exponential item count, slow/crash | Only graft when genuinely needed |
| Mismatched tree structures | Unexpected item pairing, wrong geometry | Use `Param Viewer` to inspect trees before connecting |
| Path Mapper syntax error | Null output, orange component | Test with small data first, verify path pattern |
| Flip Matrix on jagged tree | Missing items, wrong dimensions | Ensure all branches have equal item count first |
| Forgetting Simplify after multiple operations | Paths like `{0;0;0;0;0}` accumulating depth | Simplify periodically to keep paths clean |
| Operating on wrong tree level | Component receives tree when expecting item | Match tree structures or use `Branch` component to extract |

---

### 3. Parameter Space Design

#### 3.1 Defining Meaningful Parameter Ranges

Every parameter needs a domain — a minimum and maximum value that define the range of valid designs. Setting these ranges requires domain expertise:

**Principles:**
- **Physical validity** — No negative lengths, no zero-area rooms, no impossible angles.
- **Code compliance** — Ranges must respect legal minimums and maximums.
- **Structural feasibility** — Spans, depths, and loads within material capacity.
- **Constructability** — Dimensions achievable with available fabrication methods.
- **Design relevance** — Ranges should span the interesting design space, not the theoretically possible space.

#### 3.2 Domain and Remapping

**Domains** in Grasshopper represent numerical intervals: `Domain(A, B)` where A is the start and B is the end.

**Remapping** transforms a value from one domain to another:
```
Remap(value, source_domain, target_domain)
```

Common remapping patterns:
- **Normalize to 0-1:** `Remap(value, {min, max}, {0, 1})` — Useful for blending, interpolation.
- **Map to geometry range:** `Remap(slider_0_to_1, {0,1}, {2.4m, 4.2m})` — Map abstract slider to floor height.
- **Invert:** `Remap(value, {0,1}, {1,0})` — Reverse the influence direction.

#### 3.3 Slider Management Strategies

- **Group sliders by system** — Structural sliders together, envelope sliders together, site sliders together.
- **Name sliders descriptively** — `Floor_Height_m` not `Slider_1`.
- **Set slider resolution** — Integer for counts, one decimal for meters, two decimals for fine-tuning.
- **Use Expression components** — Derive secondary parameters from primary sliders to reduce slider count.
- **Lock sliders during development** — Prevent accidental changes while building logic.

#### 3.4 Number Sequences

| Sequence | Generation | Use Case |
|----------|-----------|----------|
| **Range** | Start to end with N items | Even division of an interval |
| **Series** | Start, step, count | Regular spacing with known increment |
| **Random** | Domain + seed + count | Organic variation, testing robustness |
| **Fibonacci** | Each number = sum of two preceding | Natural growth patterns, phyllotaxis |
| **Gaussian** | Normal distribution around mean | Realistic variation (material properties, tolerances) |
| **Sine/Cosine** | Periodic oscillation | Wave-like facades, undulating rooflines |
| **Geometric** | Each term = previous × ratio | Exponential growth/decay, logarithmic spirals |

#### 3.5 Parameter Sensitivity Analysis

Not all parameters have equal impact on the design. Sensitivity analysis identifies which parameters most influence key performance indicators:

1. Set all parameters to their midpoint values (baseline design).
2. Vary one parameter at a time across its full range while holding others constant.
3. Measure the output metric (area, cost, daylight factor, structural utilization).
4. Plot parameter value vs. output metric.
5. Rank parameters by their influence on the output.

High-sensitivity parameters deserve finer slider resolution and more exploration. Low-sensitivity parameters can be fixed early to reduce design space dimensionality.

---

### 4. Constraint Systems

#### 4.1 Geometric Constraints

| Constraint | Description | Degrees Removed |
|------------|-------------|-----------------|
| **Coincident** | Two points share the same location | 2 (2D) or 3 (3D) |
| **Tangent** | Curve meets surface/curve without crossing | 1-2 |
| **Perpendicular** | Two elements meet at 90 degrees | 1 |
| **Parallel** | Two elements maintain constant orientation offset | 1 |
| **Co-planar** | Points or lines lie on the same plane | 1 per point |
| **Concentric** | Two arcs/circles share a center | 2 (2D) or 3 (3D) |
| **Symmetric** | Elements mirror across an axis | Varies |
| **Collinear** | Points lie on the same line | 1 per point |
| **On-surface** | Point constrained to a surface | 1 (reduces 3D to 2D) |
| **On-curve** | Point constrained to a curve | 2 (reduces 3D to 1D) |

#### 4.2 Dimensional Constraints

- **Fixed length** — A dimension is locked to a specific value.
- **Fixed angle** — An angle is locked.
- **Ratio** — Two dimensions maintain a fixed proportion (e.g., width = 2× height).
- **Min/Max bounds** — A dimension must stay within a range.
- **Equal** — Two dimensions must be identical.

#### 4.3 Relational Constraints

- **Distance** — Two elements must maintain a minimum or exact distance.
- **Area** — A region must meet a minimum or maximum area.
- **Volume** — A solid must meet a volume target.
- **Adjacency** — Two spaces must share a boundary.
- **Containment** — One element must be fully inside another.

#### 4.4 Degrees of Freedom Analysis

A 2D point has 2 DOF. A 3D point has 3 DOF. Each constraint removes DOF. A fully constrained system has 0 remaining DOF — every element's position is uniquely determined.

- **Under-constrained (DOF > 0):** The system has remaining freedom. Elements can move without violating constraints. This is normal for parametric models — the remaining DOF are the parameters.
- **Fully constrained (DOF = 0):** The system has exactly one valid configuration. Useful for structural analysis models.
- **Over-constrained (DOF < 0):** More constraints than DOF. The system either has no solution (contradictory constraints) or redundant constraints (multiple constraints enforce the same condition).

#### 4.5 Constraint Propagation in Parametric Models

When an input changes, constraints must propagate through the model:

1. **Forward propagation** — Change flows from input to output through the dependency graph. This is the standard behavior in Grasshopper and Dynamo.
2. **Backward propagation** — Change flows from output back to input (goal-seeking). Requires iterative solvers like Galapagos (GH) or Refinery (Dynamo).
3. **Bidirectional propagation** — Changes flow in both directions simultaneously. Requires constraint solvers like Kangaroo (physics-based) or dedicated CSP solvers.

---

### 5. Grasshopper Component Taxonomy

#### 5.1 Params — Geometry Types and Primitives

**Geometry Primitives:** Point, Vector, Plane, Line, Circle, Arc, Curve, Surface, Brep, Mesh, SubD
**Primitive Parameters:** Boolean, Integer, Number, Text, Domain, Color, Matrix, Time, Transform, Data Path, File Path
**Input:** Panel, Slider, Toggle, Button, Value List, Gradient, Graph Mapper, MD Slider, Digit Scroller
**Special:** Data, Geometry Pipeline, Group, Cluster Input/Output

**Typical Use:** Every definition begins with Params for input. Geometry Pipeline pulls referenced Rhino geometry into GH. Graph Mapper provides non-linear remapping curves.

#### 5.2 Maths — Operators, Trigonometry, Polynomials, Domains

**Operators:** Addition, Subtraction, Multiplication, Division, Modulus, Power, Absolute, Negative, Maximum, Minimum
**Trigonometry:** Sine, Cosine, Tangent, Arcsine, Arccosine, Arctangent, Degrees, Radians
**Polynomials:** Evaluate, Factorial, Log, Ln, Exponential
**Domain:** Construct Domain, Deconstruct Domain, Remap Numbers, Bounds, Consecutive Domains
**Matrix:** Construct Matrix, Deconstruct Matrix, Multiply Matrix, Invert Matrix, Transpose Matrix
**Script:** Expression (single-line formula evaluation)

#### 5.3 Sets — List Management, Trees, Text

**List:** List Item, List Length, Reverse List, Sort List, Shift List, Insert Items, Replace Items, Split List, Sub List, Dispatch, Cull Pattern, Cull Index, Cull Nth, Partition List, Combine Data, Merge, Entwine, Weave, Zip/Unzip
**Tree:** Flatten, Graft, Simplify, Unflatten, Prune Tree, Trim Tree, Flip Matrix, Path Mapper, Tree Branch, Tree Item, Tree Statistics, Explode Tree, Construct Path, Deconstruct Path, Replace Paths, Relative Item, Split Tree, Stream Filter, Stream Gate
**Text:** Text Join, Text Split, Format, Concatenate, Characters, Text Length, Replace Text, Match Text, RegEx

#### 5.4 Vector — Points, Vectors, Planes, Grids

**Point:** Construct Point, Deconstruct Point, Distance, Closest Point, Point Groups, Sort Along Curve, Project Point, Pull Point
**Vector:** Unit Vector, Vector 2Pt, Vector Length, Amplitude, Reverse, Cross Product, Dot Product, Angle, Rotate
**Plane:** XY/XZ/YZ Plane, Construct Plane, Deconstruct Plane, Align Plane, Evaluate Plane, Plane Fit, Plane Normal, Plane Closest Point
**Grid:** Rectangular Grid, Hexagonal Grid, Radial Grid, Triangular Grid, Populate 2D, Populate 3D, Populate Geometry

#### 5.5 Curve — Primitives, Splines, Analysis, Division

**Primitives:** Line, Polyline, Circle, Arc, Ellipse, Rectangle, Polygon
**Splines:** Interpolate Curve, Nurbs Curve, Bezier Span, Catenary, Geodesic
**Analysis:** Evaluate Curve, Curvature, Length, Closed, Discontinuity, Curve CP (Closest Point), End Points, Tangent
**Division:** Divide Curve, Divide Length, Divide Distance, Shatter, Contour
**Utility:** Offset Curve, Fillet, Chamfer, Extend, Trim, Join Curves, Explode, Flip Curve, Simplify Curve, Rebuild Curve, Project Curve, Pull Curve, Seam

#### 5.5 Curve — Primitives, Splines, Analysis, Division

**Primitives:** Line, Polyline, Circle, Arc, Ellipse, Rectangle, Polygon
**Splines:** Interpolate Curve, Nurbs Curve, Bezier Span, Catenary, Geodesic
**Analysis:** Evaluate Curve, Curvature, Length, Closed, Discontinuity, Curve CP (Closest Point), End Points, Tangent
**Division:** Divide Curve, Divide Length, Divide Distance, Shatter, Contour
**Utility:** Offset Curve, Fillet, Chamfer, Extend, Trim, Join Curves, Explode, Flip Curve, Simplify Curve, Rebuild Curve, Project Curve, Pull Curve, Seam

#### 5.6 Surface — Primitives, Freeform, Analysis, Utility

**Primitives:** Plane Surface, Bounding Box, Sphere, Cylinder, Cone, Torus, Box
**Freeform:** Loft, Sweep1, Sweep2, Patch, Network Surface, Edge Surface, Ruled Surface, Extrude, Rail Revolution, Surface From Points
**Analysis:** Evaluate Surface, Surface CP, Surface Curvature, Osculating Circles, Deconstruct Brep, Area, Volume, IsPlanar, Surface Frames
**Utility:** Offset Surface, Isotrim (SubSrf), Divide Surface, Divide Domain², Reparameterize, Retrim, Brep Join, Cap, Flip, Untrim

#### 5.7 Mesh — Primitives, Triangulation, Analysis, Utility

**Primitives:** Mesh Box, Mesh Sphere, Mesh Plane, Construct Mesh, Mesh Surface, Mesh Brep
**Triangulation:** Delaunay Mesh, Voronoi, Convex Hull, Mesh from Lines, QuadRemesh
**Analysis:** Mesh Eval, Mesh CP, Face Normals, Mesh Area, Mesh Volume, Mesh Edges, Naked/Clothed Edges, Deconstruct Mesh
**Utility:** Mesh Join, Mesh Split, Mesh Smooth, Weld, Unweld, Flip, Cull Faces, Cull Vertices, Mesh Offset, Thicken Mesh, Blur, Reduce

#### 5.8 Transform — Affine, Array, Morph

**Affine:** Move, Rotate, Scale, Mirror, Orient, Shear, Project
**Array:** Linear Array, Rectangular Array, Polar Array, Curve Array, Box Array
**Morph:** Box Morph, Surface Morph, Twisted Box, Sporph (Surface Map), Bend, Taper, Flow Along Curve, Maelstrom

#### 5.9 Intersect — Physical, Mathematical, Region

**Physical:** Brep|Brep, Mesh|Mesh, Brep|Mesh, Curve|Curve, Curve|Brep, Curve|Mesh, Line|Plane, Brep|Plane, Mesh|Plane, Clash Detection
**Mathematical:** Point In Curve, Point In Brep, Point In Mesh, Curve|Self, Curve Proximity, Brep Proximity
**Region:** Region Union, Region Difference, Region Intersection, Region XOR, Split Brep, Trim Solid, Solid Union, Solid Difference, Solid Intersection

#### 5.10 Display — Preview, Color, Dimensions

**Preview:** Custom Preview, Preview (with material), Point Display, Dot Display
**Color:** Colour Swatch, Gradient, Colour RGB, Colour HSL
**Dimensions:** Linear Dimension, Aligned Dimension, Angular Dimension, Annotation

---

### 6. Dynamo Node Taxonomy

#### 6.1 Geometry Nodes

**Points:** Point.ByCoordinates, Point.Origin, Point.Add, Point.Project
**Curves:** Line.ByStartPointEndPoint, NurbsCurve.ByControlPoints, NurbsCurve.ByPoints, Circle.ByCenterPointRadius, Arc.ByThreePoints, PolyCurve.ByPoints, Rectangle.ByWidthLength, Curve.Offset, Curve.Extrude
**Surfaces:** Surface.ByLoft, Surface.ByPatch, Surface.ByPerimeterPoints, Surface.Offset, Surface.PointAtParameter, Surface.NormalAtParameter, NurbsSurface.ByControlPoints, NurbsSurface.ByPoints
**Solids:** Solid.ByUnion, Solid.ByLoft, Solid.Difference, Cuboid.ByLengths, Sphere.ByCenterPointRadius, Cylinder.ByPointsRadius, Cone.ByPointsRadii
**Meshes:** Mesh.ByPointsFaceIndices, Mesh.TriangleCount, Mesh.Vertices
**Coordinate Systems:** CoordinateSystem.ByOriginVectors, CoordinateSystem.Rotate, CoordinateSystem.Scale, Geometry.Transform

**Typical Use:** Geometry creation in Dynamo is node-based with explicit method names — highly readable for debugging and sharing.

#### 6.2 Math Nodes

**Operators:** +, -, *, /, %, Math.Pow, Math.Sqrt, Math.Abs, Math.Round, Math.Floor, Math.Ceiling, Math.Clamp
**Trigonometry:** Math.Sin, Math.Cos, Math.Tan, Math.Asin, Math.Acos, Math.Atan, Math.Atan2, Math.DegreesToRadians, Math.RadiansToDegrees
**Formulas:** Formula node (accepts multi-variable expressions), Code Block (inline DesignScript)

#### 6.3 List Nodes

**Create:** List.Create, Number Sequence, Number Range, List.OfRepeatedItem, List.Empty, List.Cycle
**Modify:** List.AddItemToEnd, List.AddItemToFront, List.Insert, List.RemoveItemAtIndex, List.Reverse, List.Sort, List.SortByKey, List.Shuffle, List.Flatten, List.Sublists, List.Chop, List.Combine, List.SetDifference, List.SetIntersection, List.SetUnion
**Query:** List.Count, List.FirstItem, List.LastItem, List.RestOfItems, List.GetItemAtIndex, List.IsEmpty, List.ContainsItem, List.AllIndicesOf, List.UniqueItems
**Advanced:** List.Map, List.Reduce, List.Scan, List.FilterByBoolMask, List.GroupByKey, List.Transpose, List.DiagonalRight, List.DiagonalLeft

#### 6.4 String Operations

String.Concat, String.Contains, String.Split, String.Join, String.Replace, String.Substring, String.ToNumber, String.FromObject, String.StartsWith, String.EndsWith, String.IndexOf, String.Length, String.ToUpper, String.ToLower, String.PadLeft, String.PadRight

#### 6.5 Core Nodes

**Input:** Boolean, Number, Integer, String, File Path, Directory Path, Number Slider
**Logic:** If, ScopeIf, Not, And, Or, ==, !=, <, >, <=, >=
**Scripting:** Code Block (DesignScript), Python Script, Custom Node
**Data:** Object.Type, Object.IsNull, List.Create, Dictionary.ByKeysValues, Dictionary.ValueAtKey

#### 6.6 Revit Nodes

**Elements:** Element.GetParameterValueByName, Element.SetParameterByName, Element.GetLocation, Element.Geometry, Element.BoundingBox, Element.Delete
**Selection:** Categories, All Elements of Category, Select Model Element, Select Face, Select Edge
**Create:** Wall.ByCurveAndHeight, Floor.ByOutlineTypeAndLevel, FamilyInstance.ByPoint, FamilyInstance.ByLine, Level.ByElevation, Room.ByLocation, StructuralFraming.BeamByCurve, ModelCurve.ByCurve, FilledRegion.ByCurves
**Views:** Sheet.ByNameNumberTitleBlockAndViews, Viewport.Create, FloorPlanView.ByLevel, SectionView.ByBoundingBox, View.SetFilterOverrides
**Parameters:** Parameter.ParameterByName, GlobalParameter.ByName, Element.OverrideColorInView

**Typical Use:** Dynamo's primary value proposition is deep Revit integration. These nodes allow reading, creating, and modifying Revit elements programmatically — enabling automation of documentation, element placement, and parameter management at scale.

---

### 7. Associative Geometry Patterns

#### 7.1 Point Grid to Surface to Panelization

**Description:** Create a 2D point grid, deform it (e.g., via attractors or mathematical functions), create a surface through the points, then panelize the surface into fabrication-ready panels.

**Inputs:** Grid dimensions (U count, V count), grid spacing, deformation parameters (attractor points, Z-function), panel type
**Logic Flow:** Rectangular Grid → Move points (Z = f(x,y) or attractor-based) → Surface from Points → Divide Domain² → Isotrim → Optional: Box Morph custom panel geometry
**Output:** Panelized surface with individual panel geometry, areas, and normal vectors
**Common Issues:** Non-planar panels (check planarity tolerance), extreme curvature causing panel overlap, data tree mismatch between division and morph operations.

#### 7.2 Curve Network to Lofted Surfaces to Offset Shells

**Description:** Define building sections as curves at intervals, loft between them to create a continuous surface, then offset inward and outward for wall thickness.

**Inputs:** Section curves (drawn or generated), loft type (normal, loose, tight), shell thickness
**Logic Flow:** Section Curves → Loft → Offset Surface (inward + outward) → Brep Join → Cap Holes
**Output:** Closed solid shell representing building envelope
**Common Issues:** Loft twisting (check seam alignment on curves), offset failure on high-curvature regions, non-manifold edges after joining.

#### 7.3 Attractor-Based Scaling and Rotation

**Description:** Place elements on a grid and vary their size, rotation, or other properties based on distance to one or more attractor points.

**Inputs:** Grid of base points, attractor point(s), influence radius, min/max scale, element geometry
**Logic Flow:** Grid Points → Distance to Attractor → Remap Distance to {scale_max, scale_min} (inverse: closer = larger) → Scale/Rotate element at each point → Display
**Output:** Field of elements with gradient variation responding to attractor position
**Common Issues:** Division by zero when attractor coincides with grid point, influence falloff function choice (linear vs. inverse square vs. Gaussian), multiple attractor blending.

#### 7.4 Surface Division to Module Placement

**Description:** Divide a freeform surface into UV cells and place custom 3D modules (brise-soleil, curtain wall units, cladding tiles) at each cell, oriented to the surface normal.

**Inputs:** Target surface, U/V division counts, module geometry, scale factor
**Logic Flow:** Divide Surface → Surface Frames at division points → Construct target planes from frames → Box Morph (or Orient) module from reference plane to each target plane
**Output:** Array of oriented modules populating the surface
**Common Issues:** Module orientation flipping on surface seams, UV distortion on highly curved regions, scale compensation for varying cell sizes.

#### 7.5 Profile Sweep Along Path

**Description:** Sweep a 2D profile (cross-section) along a 3D curve to create elongated geometry (structural members, handrails, ductwork, moldings).

**Inputs:** Profile curve(s), rail curve(s), profile orientation option
**Logic Flow:** Define profile in reference plane → Sweep1 along single rail or Sweep2 between two rails → Optional: Cap ends
**Output:** Solid geometry following the path with consistent cross-section
**Common Issues:** Profile twist along curved paths (adjust roadlike vs. freeform option), self-intersection on tight curves, profile scaling on diverging two-rail sweeps.

#### 7.6 Section Stacking

**Description:** Generate a building form by stacking floor plan outlines vertically, varying each floor's geometry parametrically (scaling, rotating, offsetting).

**Inputs:** Base floor plan curve, number of floors, floor-to-floor height, per-floor transformations (scale factor, rotation angle, XY offset)
**Logic Flow:** Base Curve → Copy to Z-levels → Transform each copy (Scale from centroid, Rotate, Move XY) → Loft between floors → Optional: Floor plate from each curve
**Output:** Building massing with articulated floor-by-floor variation
**Common Issues:** Loft twisting between rotated floors (match seam points), structural feasibility of aggressive floor offsets, floor area calculation per level.

#### 7.7 Boolean Solid Operations

**Description:** Combine, subtract, or intersect solid volumes to create complex building geometry from simple primitives.

**Inputs:** Solid volumes (boxes, cylinders, extruded curves, etc.), operation type (union, difference, intersection)
**Logic Flow:** Create primitive solids → Position and orient each → Apply Boolean operation → Clean result
**Output:** Complex solid geometry derived from Boolean combinations
**Common Issues:** Non-manifold results from tangent surfaces, tolerance issues with near-coincident faces, performance degradation with many sequential Booleans (prefer combining operands first, then single Boolean).

#### 7.8 Morph Box Deformation

**Description:** Define a reference box around source geometry, define a target twisted/deformed box on a surface or in space, and morph the geometry from reference to target.

**Inputs:** Source geometry, reference box (axis-aligned bounding box), target box (twisted box from surface cell or manually defined)
**Logic Flow:** Source Geometry → Bounding Box (reference) → Define target Twisted Box(es) → Box Morph → Output deformed geometry
**Output:** Source geometry deformed to conform to target box topology
**Common Issues:** Distortion quality depends on source geometry resolution (more control points = smoother deformation), extreme box distortion causes self-intersection, performance scales with geometry complexity.

---

### 8. Best Practices and Anti-Patterns

#### 8.1 Do's and Don'ts

| Do | Don't |
|----|-------|
| Name every component with a descriptive label | Leave default names like "Move" or "List Item" |
| Group related components into labeled groups | Create sprawling definitions with no organization |
| Use Relay components to create clean wire paths | Allow spaghetti wiring across the canvas |
| Internalize referenced geometry for portability | Leave external references that break when Rhino file changes |
| Use Clusters for repeated logic patterns | Copy-paste the same component chain 10 times |
| Set meaningful slider ranges based on domain knowledge | Use default 0-100 slider for a floor height parameter |
| Preview only the outputs you need to see | Preview every component (massive performance hit) |
| Build incrementally, testing at each step | Build the entire definition before testing any output |
| Document complex logic with Scribble/Panel notes | Assume future-you will remember the logic |
| Use data dam components during development | Let every change propagate through a huge definition |
| Save incremental versions of complex definitions | Overwrite the same file and lose recoverable states |
| Profile performance to find bottlenecks | Assume slow = "need faster computer" |

#### 8.2 Performance Optimization

**Internalize vs. Reference:**
- Internalize geometry that does not change frequently. This eliminates Rhino scene dependency and speeds loading.
- Keep references for geometry that must stay editable in Rhino (site context, client-provided models).

**Mesh Resolution:**
- Use the coarsest mesh resolution acceptable for the current task.
- Visualization meshes can be rough; analysis meshes need precision; fabrication meshes need extreme accuracy.
- Set custom mesh parameters (`MeshingParameters` in scripting) rather than relying on defaults.

**Data Tree Efficiency:**
- Avoid unnecessary Graft → Flatten cycles. Each restructuring copies data.
- Use `Data Dam` to pause propagation during development.
- Prefer `Entwine` over repeated `Merge` for combining multiple branches.
- Use `Trim Tree` and `Simplify` to keep path depths minimal.

**General:**
- Disable preview on all components except final outputs.
- Disable solver (F5) when making large definition changes.
- Use Profiler (Grasshopper's built-in) to identify slow components.
- Replace scripting components with native components where possible — native components run compiled C++ and are faster than interpreted C#/Python.
- Avoid recomputing geometry that has not changed — use Data Dam or manual caching.

#### 8.3 File Management

- **Naming convention:** `ProjectName_SystemName_v##.gh` (e.g., `TowerA_Facade_v03.gh`).
- **Companion files:** Keep a text file or panel documenting the definition's purpose, inputs, outputs, and dependencies.
- **Linked files:** Document all external file paths (CSV data, image textures, Rhino references).
- **Version milestones:** Save a versioned copy before any major restructuring.

#### 8.4 Version Control for Definitions

Grasshopper `.gh` files are XML-based and can be diffed/merged with appropriate tools, though practical merge conflict resolution is difficult. Recommended approach:

- Use Git for tracking versions, but treat `.gh` files as binary (no merge, always full replacement).
- Write meaningful commit messages documenting what changed.
- For team collaboration, divide the definition into multiple Clusters saved as separate `.ghcluster` files — these can be independently versioned.
- Dynamo `.dyn` files are JSON-based and slightly more diff-friendly but still complex.

#### 8.5 Cluster and Group Organization Strategies

**Groups** are visual containers — they organize the canvas but have no functional effect.

**Clusters** are functional encapsulation — they wrap a set of components into a single reusable node with defined inputs and outputs.

**When to Group:** Organize related components visually. Use consistent color coding:
- Blue: Inputs / Parameters
- Green: Geometric operations
- Orange: Data manipulation
- Red: Outputs / Baking
- Yellow: Conditional logic
- Purple: Analysis / Evaluation

**When to Cluster:**
- A component chain is reused more than once in the definition.
- A logically complete sub-system needs to be shared with another team member.
- Complexity demands hierarchical abstraction (a 500-component definition should have no more than 30-50 visible at any level).

**Cluster best practices:**
- Define clear, typed inputs and outputs with descriptive names.
- Include a Panel inside the Cluster documenting its purpose and expected input formats.
- Save reusable Clusters as `.ghcluster` files in a shared team library.
- Nest Clusters sparingly — more than 3 levels deep becomes hard to navigate and debug.

---

### Quick Reference: Tool Selection Guide

| Task | Grasshopper Approach | Dynamo Approach |
|------|---------------------|-----------------|
| Freeform surface design | Rhino geometry + GH manipulation | Limited — Dynamo geometry kernel less suited for complex NURBS |
| BIM element automation | Via Rhino.Inside.Revit | Native Dynamo-Revit integration |
| Data-driven design | CSV/JSON → GH data trees | CSV/Excel → Dynamo lists |
| Structural analysis | Karamba3D plugin | Robot Structural Analysis link |
| Environmental analysis | Ladybug/Honeybee | Insight (Autodesk) |
| Physics simulation | Kangaroo2 | Not natively available |
| Optimization | Galapagos, Wallacei | Refinery (Generative Design) |
| Fabrication output | GH → DXF/G-code export | Dynamo → Revit shop drawings |
| Interoperability | GH → Rhino → IFC/DWG/FBX | Dynamo → Revit → IFC/DWG |
| Python scripting | GhPython (IronPython/CPython) | Python Script node (CPython 3) |
| C# scripting | C# Script component | Not available (use Zero Touch) |
| Visual programming complexity | Handles extreme complexity well | Best for BIM automation, moderate geometry |

---

*This skill provides the foundational knowledge for parametric modeling in AEC computational design. For detailed tool-specific patterns and recipes, see the companion references: `grasshopper-patterns.md`, `dynamo-patterns.md`, and `data-structures.md`.*


## computational-geometry

### Computational Geometry

> NURBS curves and surfaces, mesh geometry, boolean operations, subdivision surfaces, tessellation methods, surface analysis, and point cloud processing for AEC computational design

## Computational Geometry for AEC

This skill encapsulates the full breadth of computational geometry knowledge required for architecture, engineering, and construction workflows. It covers fundamental primitives, advanced surface mathematics, mesh processing, tessellation strategies, point cloud pipelines, and the precise tolerance management that separates prototype-grade geometry from fabrication-ready output.

---

### 1. Geometry Type Hierarchy

Every computational design system is built on a layered hierarchy of geometric types. Understanding the properties, capabilities, and conversion paths of each type is essential for selecting the right representation at every stage of a project.

#### 1.1 Points, Vectors, Planes, Frames

**Point (Point3d)**
- Definition: A dimensionless location in 3D Euclidean space defined by (x, y, z) coordinates.
- Properties: No length, area, or volume. Carries only positional information.
- AEC use cases: Survey control points, grid intersections, insertion points for components, structural node locations, sensor positions.
- Conversion: A point can seed any higher-order geometry. Points become curve control points, mesh vertices, or centroid markers.

**Vector (Vector3d)**
- Definition: A direction and magnitude in 3D space, defined by (x, y, z) components. Unlike a point, a vector has no fixed position.
- Properties: Magnitude (length), direction (unit vector). Supports dot product, cross product, angle computation, projection.
- AEC use cases: Wind direction encoding, structural force vectors, surface normals for solar analysis, movement direction for pedestrian simulation, facade orientation vectors.
- Key operations: Normalize, scale, add, subtract, dot product (scalar projection), cross product (perpendicular vector), angle between vectors, reflection, rotation.

**Plane**
- Definition: An infinite flat surface defined by an origin point and a normal vector, or equivalently by an origin and two in-plane axes (X-axis, Y-axis) with the normal as Z-axis.
- Properties: Origin, Normal, XAxis, YAxis. Divides space into two half-spaces.
- AEC use cases: Floor levels, section cut planes, mirror planes for symmetric designs, construction planes for drawing, reference datums.
- Conversion: Planes can generate planar surfaces, serve as projection targets, or define local coordinate systems.

**Frame**
- Definition: A right-handed orthonormal coordinate system defined by an origin point and three mutually perpendicular unit vectors (X, Y, Z).
- Properties: Origin, XAxis, YAxis, ZAxis. Fully defines position and orientation.
- AEC use cases: Structural member local axes, robotic fabrication tool frames, camera positions for rendering, element insertion frames, joint coordinate systems.
- Distinction from Plane: A frame carries full rotational information (three axes), while a plane is defined by only one axis (the normal) plus a rotation ambiguity around that normal.

#### 1.2 Curves

**Line**
- Definition: The shortest path between two points; a degree-1 NURBS curve with two control points.
- Properties: Start point, end point, length, midpoint, direction vector.
- AEC use cases: Grid lines, structural member centerlines, dimension lines, sight lines, setback lines.
- Conversion: Can be treated as a degree-1 NURBS curve, a polyline with two vertices, or a mesh edge.

**Polyline**
- Definition: A connected sequence of line segments defined by an ordered list of vertices.
- Properties: Vertex list, segment count, total length, is-closed flag, bounding box.
- AEC use cases: Property boundaries, road centerlines, building footprints, pipe routes, cable tray paths, simplified contour lines.
- Conversion: Each segment is a line. The entire polyline can be degree-elevated to a NURBS curve. Can be used as a mesh wireframe or triangulated polygon boundary.

**Arc**
- Definition: A portion of a circle defined by center, radius, start angle, and end angle (or equivalently by three points).
- Properties: Center, radius, start/end angles, arc length, start/end points, midpoint.
- AEC use cases: Curved walls, arch profiles, fillet transitions, roundabout geometry, curved beam profiles.
- Conversion: Can be represented exactly as a rational NURBS curve of degree 2 (using weights).

**Circle**
- Definition: A closed planar curve where every point is equidistant from the center. A special case of an arc (360 degrees) and of an ellipse (equal radii).
- Properties: Center, radius, plane, circumference, area.
- AEC use cases: Column cross-sections, roundabouts, circular openings, pipe profiles, rotunda plans.
- Conversion: Exactly representable as a rational NURBS curve of degree 2 with specific weights. Can be approximated by a polygon with n vertices.

**Ellipse**
- Definition: A closed planar curve defined by a center, two perpendicular semi-axes of different lengths.
- Properties: Center, semi-major axis (a), semi-minor axis (b), plane, eccentricity, perimeter (approximation), area.
- AEC use cases: Elliptical domes, stadium plans, oval windows, landscape features, acoustic reflectors.
- Conversion: Exactly representable as a rational NURBS curve. Can be approximated by a polyline or polygon.

**NURBS Curve**
- Definition: Non-Uniform Rational B-Spline curve defined by degree, control points, knot vector, and weights.
- Properties: Degree, control point count, knot vector, domain, length, is-closed, is-periodic, continuity.
- AEC use cases: Freeform facades, road alignments with complex geometry, landscape contours, furniture profiles, any smooth curved design element.
- Conversion: The universal curve representation. All other curve types can be expressed as NURBS curves. Can be approximated by a polyline (tessellated) for meshing or CNC output.

**Polycurve (Composite Curve)**
- Definition: An ordered sequence of connected curve segments that may include lines, arcs, and NURBS spans joined end-to-end.
- Properties: Segment list, total length, is-closed, continuity at joints (G0 minimum).
- AEC use cases: Road alignments (tangent-spiral-arc-spiral-tangent), building outlines mixing straight and curved edges, complex trim boundaries, rail profiles.
- Conversion: Can be rebuilt as a single NURBS curve (with potential continuity loss at joints). Each segment retains its native type.

#### 1.3 Surfaces

**Planar Surface**
- Definition: A flat, bounded region of a plane defined by one or more closed boundary curves (outer boundary plus optional holes).
- Properties: Plane, area, centroid, boundary curves, perimeter.
- AEC use cases: Floor slabs, wall faces, ceiling panels, glass panes, site boundaries.
- Conversion: Trivially meshable. Representable as a degree-1 NURBS surface.

**NURBS Surface**
- Definition: A bi-parametric surface defined by a grid of control points, degrees in U and V directions, knot vectors in U and V, and weights.
- Properties: Degree U/V, control point grid (rows x cols), domain U/V, is-closed in U/V, is-trimmed, area, centroid.
- AEC use cases: Freeform facades, shell roofs, landscape terrain patches, furniture surfaces, ship hull forms.
- Conversion: Can be tessellated into a mesh. Can be trimmed, split, or joined with other surfaces.

**Extrusion Surface**
- Definition: A surface generated by sweeping a profile curve along a straight direction vector.
- Properties: Profile curve, direction vector, is-capped, length.
- AEC use cases: Walls, columns, mullions, linear structural members, ducting, pipe runs.
- Conversion: A special case of a sweep along a line. Representable as a NURBS surface or mesh.

**Surface of Revolution**
- Definition: A surface generated by rotating a profile curve around an axis.
- Properties: Profile curve, axis (point + direction), angle range, is-full-revolution.
- AEC use cases: Domes, columns with entasis, vases, cooling towers, rotational decorative elements.
- Conversion: Representable as a rational NURBS surface. Can be tessellated into a mesh.

**Lofted Surface**
- Definition: A surface interpolating or approximating a series of cross-section curves.
- Properties: Section curves, loft type (normal, loose, tight, uniform, closed), rebuild options.
- AEC use cases: Towers with varying floor plates, bridge decks, transition pieces between different profiles, terrain ribbons.
- Conversion: Results in a NURBS surface. Quality depends on curve compatibility (matching point counts and parameterization).

**Swept Surface**
- Definition: A surface generated by sweeping a profile curve along one or two rail curves.
- Properties: Profile curve(s), rail curve(s), sweep type, alignment options.
- AEC use cases: Handrails, cornices, moldings, highway guardrails, complex facade bands.
- Conversion: Results in a NURBS surface. Two-rail sweeps provide more geometric control than single-rail.

**Pipe Surface**
- Definition: A surface generated by sweeping a circular cross-section along a rail curve with specified radius.
- Properties: Rail curve, radius (or variable radii), cap type.
- AEC use cases: Structural tubes, piping systems, handrails, cable-stayed bridge cables, conduit runs.
- Conversion: A special case of a swept surface with circular profile. Representable as NURBS or mesh.

#### 1.4 Solids

**Brep (Boundary Representation)**
- Definition: A solid defined by its bounding surfaces (faces), edges, and vertices, with topological connectivity information.
- Properties: Face list, edge list, vertex list, is-solid (closed), is-manifold, volume, centroid, surface area, Euler characteristic.
- AEC use cases: Building massing models, structural elements, MEP components, furniture, any volumetric design element requiring boolean operations.
- Conversion: Can be meshed for analysis or rendering. Can be sectioned to produce curves. Individual faces are surfaces.

**Extrusion Solid**
- Definition: A closed solid generated by extruding a closed planar curve along a direction, with top and bottom caps.
- Properties: Profile curve, direction, height, volume, surface area.
- AEC use cases: Columns, walls (prismatic), floor slabs, simple massing volumes, extruded structural profiles (I-beam, channel, angle).
- Conversion: A special case of Brep. Can be converted to mesh.

**Boolean Result Solid**
- Definition: A solid resulting from CSG (Constructive Solid Geometry) operations (union, difference, intersection) between two or more solids.
- Properties: Inherits Brep properties. Topology may be complex with many faces and edges depending on the intersection geometry.
- AEC use cases: Wall openings (difference), merged building volumes (union), spatial overlap analysis (intersection), complex façade panel geometries.
- Conversion: Standard Brep after boolean resolution. May require cleanup (merge coplanar faces, remove micro-edges).

#### 1.5 Meshes

**Triangular Mesh (Tri-mesh)**
- Definition: A mesh composed entirely of triangular faces. Each face is defined by three vertex indices.
- Properties: Vertex count, face count, edge count, is-manifold, is-closed, surface area, volume (if closed), Euler characteristic.
- AEC use cases: FEA (finite element analysis) discretization, 3D printing, terrain surfaces (TIN), real-time visualization, photogrammetry output.
- Conversion: Universal mesh format. All other mesh types can be triangulated. Cannot directly convert to smooth NURBS without fitting.

**Quadrilateral Mesh (Quad-mesh)**
- Definition: A mesh composed entirely of four-sided faces. Each face is defined by four vertex indices.
- Properties: Same as tri-mesh plus: face planarity deviation, edge alignment quality.
- AEC use cases: Facade panelization (flat quads preferred for glass), structural shell analysis, subdivision surface base meshes, textile/fabric patterns.
- Conversion: Each quad can be split into two triangles. Quads can be derived from NURBS surface isoparm sampling.

**Ngon Mesh**
- Definition: A mesh allowing faces with any number of vertices (3, 4, 5, or more sides per face).
- Properties: Same as other meshes plus: maximum face valence, face planarity metrics.
- AEC use cases: Voronoi-based facade panels, organic surface panelization, architectural geometries where non-standard face shapes are acceptable.
- Conversion: Any ngon face can be triangulated by fan or ear-clipping methods.

**Subdivision Mesh**
- Definition: A coarse control mesh that defines a smooth limit surface via recursive subdivision rules (Catmull-Clark, Loop, Doo-Sabin).
- Properties: Control mesh, subdivision level, limit surface, crease edges, corner vertices.
- AEC use cases: Organic architectural forms, furniture design, smooth transitions between geometric elements, concept modeling.
- Conversion: At any subdivision level, the result is a standard mesh. The limit surface can be approximated by sufficient subdivision levels.

#### 1.6 Other Geometric Types

**Point Cloud**
- Definition: An unstructured collection of points in 3D space, typically with associated attributes (color, intensity, normal, classification).
- Properties: Point count, bounding box, density, attributes per point.
- AEC use cases: As-built documentation, heritage preservation scanning, site survey, construction progress monitoring, clash detection against design models.
- Conversion: Can be meshed (Poisson, ball-pivoting, alpha shapes). Can be segmented and fitted with geometric primitives. Cannot directly become NURBS without reconstruction.

**Voxels**
- Definition: Volumetric pixels; a 3D grid of cubic cells, each storing a value (occupied/empty, density, material, temperature).
- Properties: Grid resolution (nx, ny, nz), voxel size, total volume, memory footprint.
- AEC use cases: Solar radiation analysis (volumetric irradiance), wind comfort studies (CFD grids), 3D printing slicing, structural topology optimization, spatial analysis (occupancy, visibility).
- Conversion: Voxel boundaries can be extracted as meshes (marching cubes algorithm). Voxels can be derived from mesh or Brep by spatial sampling.

---

### 2. NURBS Deep Dive

#### 2.1 NURBS Curves

NURBS (Non-Uniform Rational B-Spline) curves are the industry-standard representation for freeform curves in CAD systems. They unify lines, arcs, circles, conics, and freeform curves under a single mathematical framework.

**Degree and Order**
- Degree (p): The polynomial degree of the basis functions. Common values: 1 (linear/polyline), 2 (conic sections, arcs), 3 (cubic, most common for freeform), 5 (automotive/aerospace).
- Order (k): k = p + 1. A cubic curve has order 4.
- Higher degree = smoother curve but more computational cost, potential oscillation, and harder to control locally.
- Degree 3 (cubic) is the workhorse of AEC: sufficient smoothness for architectural curves, good local control, efficient computation.

**Control Points**
- Control points define the shape of the curve. The curve does not generally pass through interior control points (except at endpoints for clamped curves).
- Minimum number of control points: degree + 1 (e.g., 4 for cubic).
- Moving a control point affects only a local region of the curve (local support property).
- More control points = more local control but more complex management.

**Knot Vector**
- An ordered sequence of non-decreasing parameter values that define where each basis function is active.
- Length of knot vector: n + p + 1, where n = number of control points, p = degree.
- Clamped (open) knot vectors: First and last knot values repeated p+1 times, forcing the curve through the first and last control points.
- Uniform knot vectors: Interior knots are equally spaced.
- Non-uniform: Interior knots at arbitrary spacing, allowing variable parameterization.
- Knot multiplicity: Repeating an interior knot reduces continuity at that parameter. Multiplicity = p creates a sharp corner (C0 only).

**Weights**
- Each control point has an associated weight (w_i). When all weights are equal, the curve is a non-rational B-spline.
- Rational NURBS (weights != 1) can exactly represent conic sections: circles, ellipses, hyperbolas, parabolas.
- Increasing a weight pulls the curve toward that control point; decreasing pushes it away.
- Weight of 1.0 is standard. For a circular arc of 90 degrees, the corner control point has weight sqrt(2)/2 ~ 0.7071.

**Continuity**
- G0 (Geometric positional): Curves share an endpoint. No smoothness guarantee.
- G1 (Geometric tangent): Curves share an endpoint and have the same tangent direction (but potentially different speeds/magnitudes).
- G2 (Geometric curvature): G1 plus matching curvature magnitude. Produces visually smooth transitions with no curvature discontinuity.
- G3 (Geometric torsion): G2 plus matching rate of curvature change. Used in high-end automotive and aerospace surfaces.
- C0, C1, C2, C3 (parametric continuity): Stricter than geometric continuity. C1 requires matching tangent vectors (same direction AND magnitude).

#### 2.2 Curve Operations

| Operation | Description | AEC Application |
|-----------|-------------|-----------------|
| Evaluate | Compute point at parameter t | Query any position along a road alignment |
| Tangent | Unit tangent vector at parameter t | Structural member orientation along curved path |
| Curvature | Curvature value and center at t | Identify tight bends in road design for safety |
| Division | Split curve at equal lengths/parameters/counts | Place equally spaced facade mullions |
| Offset | Parallel curve at distance d | Generate wall inner/outer faces from centerline |
| Fillet | Round corner between two curves | Smooth transitions at corridor junctions |
| Chamfer | Straight-cut corner between curves | Beveled edges on structural elements |
| Extend | Lengthen curve beyond endpoint | Extend a property line to intersection |
| Trim | Remove portion of curve at intersection | Cut curves at building footprint boundary |
| Split | Divide curve at parameter(s) | Break road alignment at intersection points |
| Join | Combine end-to-end curves into one | Assemble complex boundary from segments |
| Rebuild | Refit curve with new degree/point count | Simplify scanned data curve for clean geometry |
| Fit | Create curve through a set of points | Generate road alignment from survey points |

#### 2.3 NURBS Surfaces

**Degree in U and V**
- NURBS surfaces have independent degrees in U and V directions.
- Common: degree 3 in both directions (bi-cubic).
- Can be asymmetric: degree 1 in U (ruled surface) and degree 3 in V.

**Control Point Grid**
- Arranged in an (m x n) grid where m = points in U direction, n = points in V direction.
- Surface shape is controlled by moving grid points.
- Local support: moving one control point affects only a local patch of the surface.

**Isocurves (Isoparametric Curves)**
- Curves on the surface at constant U or constant V parameter values.
- Useful for visualizing surface shape, generating panelization grids, and extracting section curves.
- Isocurve density can indicate surface curvature variation.

**Trimmed vs. Untrimmed Surfaces**
- Untrimmed: The surface exists over its full U-V domain. Boundary is defined by the domain edges.
- Trimmed: The visible boundary is defined by trim curves (2D curves in UV space + 3D edge curves). The underlying surface extends beyond the trim boundary.
- Trimmed surfaces are extremely common in AEC: any time a surface is cut, split, or bounded by non-rectangular boundaries.
- Trimmed surfaces can cause meshing difficulties and analysis inaccuracies if trim curves are not well-defined.

#### 2.4 Surface Operations

| Operation | Description | AEC Application |
|-----------|-------------|-----------------|
| Evaluate | Point + normal at (u,v) | Place elements on a freeform facade |
| Normal | Surface normal vector at (u,v) | Determine panel orientation for solar analysis |
| Gaussian Curvature | K = k1 * k2 at (u,v) | Identify regions requiring double-curved panels (K != 0) |
| Mean Curvature | H = (k1+k2)/2 at (u,v) | Detect minimal surface regions (H = 0) |
| Principal Curvatures | k1, k2 and their directions | Orient panelization grid along principal curvature lines |
| Offset | New surface at constant distance | Generate inner/outer shell surfaces |
| Extend | Lengthen surface beyond edge | Extend roof surface past wall line |
| Trim | Cut surface with curves/surfaces | Create openings in facade surface |
| Split | Divide surface at isocurves or cutting geometry | Segment facade into zones |
| Join | Combine adjacent surfaces | Assemble polysurface from patches |
| Rebuild | Refit with new degree/point counts | Simplify scanned-data surface |
| Isotrim | Extract sub-surface at UV interval | Extract individual panels from surface grid |

#### 2.5 Surface Creation Methods

**Loft**
- Interpolates a surface through a set of section curves.
- Curves should have compatible directions and similar point counts for best results.
- Loft types: Normal, Loose, Tight, Straight (ruled between sections).
- AEC: Tower massing with varying floor plates, bridge deck surfaces, transition geometry.

**Sweep 1-Rail**
- Sweeps a profile curve along a single rail curve.
- Profile orientation options: freeform, roadlike (profile stays vertical), maintain height.
- AEC: Cornices, handrails, extruded mullion profiles along curved paths.

**Sweep 2-Rail**
- Sweeps one or more profile curves along two rail curves, scaling the profile to match rail separation.
- Provides more control than 1-rail sweep over surface width and shape variation.
- AEC: Variable-width soffits, tapered structural members, curved curtain wall bands.

**Network Surface**
- Creates a surface from a network of intersecting curves (U-curves and V-curves).
- Produces higher-quality surfaces than loft when curves in both directions are available.
- AEC: Complex facade surfaces defined by structural grid curves, boat hull forms.

**Patch**
- Fits a surface to a collection of points, curves, and/or edges as boundary conditions.
- Useful for filling gaps and creating surfaces from irregular boundary conditions.
- AEC: Terrain surface patches, infill surfaces for complex roof geometries, repair of scan data gaps.

**Edge Surface**
- Creates a surface from 2, 3, or 4 boundary edge curves.
- Simplest method for creating surfaces from boundary curves.
- AEC: Infill panels between structural members, simple canopy surfaces.

**Revolve**
- Rotates a profile curve around an axis to create a surface of revolution.
- AEC: Dome surfaces, circular columns with entasis, rotunda walls, decorative elements.

**Extrude**
- Moves a curve along a direction vector to create a ruled surface.
- AEC: Wall surfaces from plan curves, extruded structural profiles, simple facade panels.

#### 2.6 Surface Continuity

| Continuity | Condition | Visual Effect | AEC Requirement |
|------------|-----------|---------------|-----------------|
| G0 | Shared edge, surfaces touch | Visible crease/edge | Acceptable for panel joints |
| G1 | Matching tangent planes across edge | Smooth shading, no sharp highlight break | Required for smooth facade surfaces |
| G2 | Matching curvature across edge | Perfectly smooth reflections | Required for high-end cladding, automotive-inspired architecture |

#### 2.7 NURBS vs. Mesh Comparison

| Criterion | NURBS | Mesh |
|-----------|-------|------|
| Precision | Mathematically exact, resolution-independent | Approximate, resolution-dependent |
| Memory | Compact for smooth surfaces (few control points) | Can be large (millions of faces for complex forms) |
| Rendering | Requires tessellation for GPU rendering | Directly renderable by GPU |
| Analysis | Exact normals and curvature everywhere | Requires interpolation between vertices |
| Fabrication | Direct CNC tool-path generation | Requires slicing or conversion |
| Boolean Operations | Computationally expensive, tolerance-sensitive | Faster but approximation errors |
| Editing | Intuitive control-point manipulation | Vertex-level editing, sculpting tools |
| Import/Export | STEP, IGES, 3DM | STL, OBJ, FBX, PLY, glTF |
| Best for | Design, documentation, manufacturing | Visualization, analysis, 3D printing, scanning |

---

### 3. Boolean Operations (CSG)

#### 3.1 Operation Types

**Union (Boolean Add)**
- Combines two or more solids into a single solid encompassing the total volume of all inputs.
- Overlapping regions become interior and are removed.
- AEC: Merging building volumes, combining structural elements, assembling composite massing models.

**Difference (Boolean Subtract)**
- Removes the volume of one solid (tool) from another solid (target).
- The tool solid defines the void; the target retains its exterior minus the intersection.
- AEC: Creating window/door openings in walls, cutting pipe penetrations through slabs, carving atrium voids.

**Intersection (Boolean And)**
- Retains only the volume shared by two or more solids.
- AEC: Analyzing spatial overlaps (e.g., where two setback volumes intersect), generating connection pieces between structural elements, extracting shared zones.

**Split**
- Divides a solid into multiple pieces using a cutting surface or solid without removing any material.
- AEC: Splitting a building volume at floor levels, dividing a facade into panels, sectioning terrain.

#### 3.2 Solid vs. Surface Booleans

- Solid booleans operate on closed (watertight) volumes. The result is always a valid closed solid.
- Surface booleans operate on open surfaces. Results may have naked (unbounded) edges and require careful boundary management.
- Solid booleans are more reliable because the inside/outside classification is unambiguous for closed volumes.
- Surface booleans often fail when surfaces are tangent, nearly coincident, or have edges exactly on the splitting surface.

#### 3.3 Common Failures and Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Non-manifold edges | Boolean result has edges shared by more than two faces | Increase tolerance, simplify input geometry, split into simpler operations |
| Naked edges | Input geometry is not closed | Ensure all inputs are valid closed Breps before boolean |
| Tolerance mismatch | Input geometries modeled at different tolerances | Standardize document tolerance before boolean |
| Coincident faces | Two faces lie exactly on the same plane | Offset one input slightly (0.001 units), or pre-split at coincident faces |
| Micro-edges/faces | Boolean creates tiny geometric features | Post-process: merge coplanar faces, collapse short edges, remove sliver faces |
| Operation returns empty | Solids do not overlap | Verify intersection exists before performing boolean |
| Wrong piece retained | Difference removes the wrong part | Reverse the order (A minus B vs B minus A), or check solid normals |

#### 3.4 Boolean Operation Order

- Boolean operations are NOT commutative for difference: A - B != B - A.
- Union and intersection ARE commutative: A + B = B + A.
- For complex multi-body booleans, the order of operations can affect both the result and performance.
- Strategy: Perform booleans pairwise, starting with the simplest intersections, and validate at each step.

#### 3.5 Performance Considerations

- Boolean complexity scales with the number of face-face intersections between input solids.
- Planar faces are cheapest; NURBS-NURBS intersections are most expensive.
- Pre-simplify inputs: merge coplanar faces, remove unnecessary detail, reduce control point counts.
- For repetitive booleans (e.g., 500 window openings), consider alternative strategies: split the wall surface rather than boolean each opening individually, or use face-replacement approaches.
- Mesh booleans (libigl, CGAL, Cork) are faster for complex geometry but introduce approximation.

---

### 4. Tessellation Methods

#### 4.1 Voronoi Diagrams

**2D Voronoi**
- Partitions a plane into convex cells, each containing all points closest to one generator (seed) point.
- Cell boundaries are segments of perpendicular bisectors between adjacent generators.
- Properties: Every cell is convex; edges are equidistant from exactly two generators; vertices are equidistant from exactly three generators.
- AEC applications: Facade panel layouts, floor plan partitioning, urban block subdivision, landscape zone design, structural foam/bone-inspired patterns.

**3D Voronoi**
- Partitions 3D space into convex polyhedral cells.
- Cell faces are planar polygons on perpendicular bisector planes.
- AEC applications: 3D-printed structural lattices, acoustic diffuser geometry, volumetric space partitioning, porous material design.

**Weighted Voronoi (Power Diagram / Laguerre Diagram)**
- Each generator has an associated weight that controls cell size.
- Higher-weight generators produce larger cells.
- Enables control over cell size distribution while maintaining the Voronoi topology.
- AEC applications: Adaptive facade panels (larger in low-detail areas, smaller near stress concentrations), variable-density space partitioning.

**Centroidal Voronoi Tessellation (CVT)**
- An iterative refinement (Lloyd's algorithm) where generators are moved to their cell centroids.
- Converges to a tessellation where cells are approximately equal-sized and equilateral.
- Produces highly regular, aesthetically pleasing patterns.
- AEC applications: Regularized facade panels, uniform structural grid generation, even distribution of program zones.

#### 4.2 Delaunay Triangulation

**2D Delaunay**
- The dual of the 2D Voronoi diagram. Connects generators with edges such that no generator lies inside the circumcircle of any triangle.
- Maximizes the minimum angle of all triangles (avoids sliver triangles).
- Unique for a given set of points (assuming no four co-circular points).
- AEC applications: Terrain TIN (Triangulated Irregular Network) generation, structural triangulated grids, FEA mesh generation.

**3D Delaunay**
- Tetrahedralization of a point set in 3D, dual to the 3D Voronoi diagram.
- No point lies inside the circumsphere of any tetrahedron.
- AEC applications: Volumetric FEA mesh generation, 3D terrain modeling, structural analysis discretization.

**Constrained Delaunay Triangulation (CDT)**
- A Delaunay triangulation that includes specified edges (constraints) as triangle edges.
- Ensures boundary conformity: building outlines, road edges, and property lines appear as mesh edges.
- AEC applications: Site plan meshing with boundary conformity, terrain meshing with breaklines (ridges, valleys, retaining walls).

#### 4.3 Convex Hull

- The smallest convex set containing all input points.
- 2D: A convex polygon. 3D: A convex polyhedron.
- Algorithms: Graham scan (2D, O(n log n)), Quickhull (2D/3D), incremental insertion.
- AEC applications: Bounding volume for clash detection, simplified massing envelope, maximum buildable volume from setback points.

#### 4.4 Alpha Shapes

- A generalization of the convex hull controlled by a parameter alpha.
- Alpha = infinity gives the convex hull; smaller alpha values reveal concavities and holes.
- Useful for reconstructing boundaries from unstructured point sets.
- AEC applications: Building footprint extraction from LiDAR point clouds, site boundary detection, as-built outline generation.

#### 4.5 Quad Meshing from NURBS

**Isoparm-based**
- Sample the NURBS surface at regular U-V intervals to generate a structured quad grid.
- Simple and predictable but produces non-uniform cell sizes on surfaces with non-uniform parameterization.
- Reparameterize the surface first (arc-length parameterization) for more uniform quads.
- AEC: Facade panelization of smooth surfaces, structural grid for shell analysis.

**Advancing Front**
- Starts from the boundary and progressively fills the interior with quads.
- Produces better-quality quads near boundaries.
- AEC: Structural panel layouts that must respect edge conditions, floor tile patterns.

#### 4.6 Hexagonal Tessellation

- Regular hexagons tile the plane with each cell having six equidistant neighbors.
- Three coordinate systems: offset, cube, axial.
- Hexagonal grids minimize perimeter-to-area ratio among regular tessellations.
- AEC: Facade panel patterns, landscape paving, structural honeycomb cores, acoustic tile layouts.

#### 4.7 Penrose Tiling

- Aperiodic tiling using two tile shapes (kites and darts for P2, or thin and thick rhombi for P3).
- Never repeats but covers the plane completely; exhibits five-fold rotational symmetry.
- Matching rules prevent periodic arrangements.
- Inflation/deflation generates tiles at multiple scales.
- AEC: Decorative floor patterns, facade panel layouts with non-repeating aesthetic, Islamic-geometry-inspired designs.

#### 4.8 Space-Filling Polyhedra

- Polyhedra that tile 3D space without gaps or overlaps.
- Examples: Cube, truncated octahedron, rhombic dodecahedron, gyrobifastigium, and the recently discovered "hat" aperiodic monotile (2D).
- AEC: 3D-printed structural infill, modular space-frame geometries, volumetric subdivision for analysis, acoustic chamber design.

#### 4.9 AEC Tessellation Applications

| Application | Preferred Method | Reasoning |
|-------------|-----------------|-----------|
| Facade panelization (flat glass) | Planar quad meshing | Glass panels must be planar; quads minimize waste |
| Facade panelization (decorative) | Voronoi, Penrose | Visual variety, non-repeating patterns |
| Structural diagrid | Delaunay / triangulated quad | Triangles are inherently rigid |
| Floor plan partitioning | Weighted Voronoi | Cell sizes can match programmatic area requirements |
| Terrain modeling | Constrained Delaunay TIN | Respects breaklines, handles irregular point distributions |
| Shell structure analysis mesh | Quad-dominant with boundary conformity | FEA requires quality elements at boundaries |
| 3D printing infill | Hexagonal / gyroid | High strength-to-weight ratio |
| Acoustic panels | Voronoi / Penrose | Non-repeating patterns diffuse sound effectively |

---

### 5. Surface Analysis

#### 5.1 Gaussian Curvature (K)

- Definition: K = k1 * k2, the product of the two principal curvatures at a point.
- K > 0 (positive): Synclastic surface (dome, sphere). Both principal curvatures curve in the same direction. Cannot be flattened without stretching/compression.
- K = 0 (zero): Developable surface (cylinder, cone, tangent surface). At least one principal curvature is zero. Can be unrolled flat without distortion.
- K < 0 (negative): Anticlastic surface (saddle, hyperbolic paraboloid). Principal curvatures curve in opposite directions. Cannot be flattened.

**Fabrication implications:**
- K = 0 panels can be made from flat sheet material (metal, glass, plywood) by bending.
- K != 0 panels require molds, hot-forming, thermoforming, or panelization into smaller approximately-flat pieces.
- Threshold: |K| < tolerance can often be treated as developable for practical purposes.

#### 5.2 Mean Curvature (H)

- Definition: H = (k1 + k2) / 2, the average of the principal curvatures.
- H = 0: Minimal surface (e.g., catenoid, helicoid, soap film). Minimal surfaces minimize area for given boundary conditions.
- H = constant != 0: Constant mean curvature surface (e.g., sphere, cylinder). These surfaces model soap bubbles and capillary surfaces.
- AEC relevance: Minimal surfaces are structurally efficient tension membranes. Constant-H surfaces appear in pneumatic structures.

#### 5.3 Principal Curvatures (k1, k2) and Directions

- At every point on a smooth surface, there exist two orthogonal directions (principal directions) along which curvature is maximized (k1) and minimized (k2).
- k1 >= k2 by convention.
- Points where k1 = k2 are called umbilical points (curvature is the same in all directions, e.g., apex of a sphere).
- Principal curvature lines (integral curves of principal directions) form an orthogonal network on the surface.
- AEC applications: Orienting facade panel grids along principal curvature lines minimizes panel warping. Structural reinforcement can follow principal stress directions (which often align with principal curvature on shells).

#### 5.4 Draft Angle Analysis

- Measures the angle between the surface normal and a specified pull direction (typically vertical for mold extraction).
- Used in manufacturing to ensure parts can be extracted from molds without undercuts.
- AEC relevance: Precast concrete panels need draft angles for mold extraction. Metal facade panels formed on male/female dies require draft analysis.
- Visualization: Color map from 0 degrees (normal parallel to pull direction) to 90 degrees (normal perpendicular).

#### 5.5 Deviation Analysis

- Measures the distance between two surfaces or between a surface and a reference geometry (point cloud, mesh, or another surface).
- Results displayed as a color map with min/max/average/RMS deviation values.
- AEC applications: Comparing as-built scan to design model, quality control of fabricated panels, measuring facade flatness deviation.
- Tolerances: Typical facade panel flatness tolerance is 1-3mm; structural steel is 2-5mm; cast-in-place concrete is 5-15mm.

#### 5.6 Zebra Stripe Analysis

- Projects parallel stripes (simulating a striped environment reflection) onto the surface.
- Reveals surface continuity issues that are invisible in standard shading:
  - G0 joints: Stripes break/jump at the edge.
  - G1 joints: Stripes are continuous but change direction abruptly (kink in stripe).
  - G2 joints: Stripes flow smoothly across the edge.
- AEC applications: Quality-checking facade surfaces, verifying smooth transitions on freeform architecture, ensuring visual smoothness of polished surfaces.

#### 5.7 Environment Map Analysis

- Maps a spherical or cylindrical environment image onto the surface via reflection vectors.
- Similar to zebra analysis but with a more complex pattern that reveals subtler imperfections.
- Used when the surface will be highly reflective (polished metal cladding, glass, water features).

#### 5.8 Curvature Comb

- Displays curvature magnitude as a series of lines (comb teeth) perpendicular to a curve or surface edge.
- Comb height = curvature magnitude. Direction = toward center of curvature.
- Reveals: Curvature discontinuities (sudden jumps in comb height), inflection points (comb crosses the curve), curvature smoothness.
- AEC applications: Evaluating road alignment smoothness, checking facade curve fairness, verifying smooth handrail profiles.

#### 5.9 Visualization Methods

| Method | What It Reveals | Best For |
|--------|----------------|----------|
| False-color curvature map | Curvature magnitude distribution | Identifying developable regions, panel rationalization |
| Zebra stripes | Surface continuity (G0/G1/G2) | Checking surface quality for reflective materials |
| Environment map | Surface smoothness and distortion | Polished/glossy facade panels |
| Curvature comb | Curvature profile along a curve | Road alignments, handrail profiles |
| Deviation color map | Distance to reference geometry | As-built vs. design comparison |
| Normal vector display | Surface orientation | Panel orientation, solar angle analysis |
| Isocurve density | Parameterization quality | Identifying surface stretching/compression |

---

### 6. Point Cloud Processing

#### 6.1 Acquisition Methods

**LiDAR (Light Detection and Ranging)**
- Terrestrial laser scanning (TLS): Tripod-mounted scanner, sub-millimeter accuracy, 360-degree capture.
- Mobile laser scanning (MLS): Vehicle or backpack-mounted, covers large areas quickly, centimeter accuracy.
- Aerial LiDAR: Drone or aircraft-mounted, terrain mapping, building roof extraction.
- Typical output: 1-100 million points per scan, XYZ + intensity + return number.
- AEC context: As-built documentation of existing buildings, site surveys, construction monitoring.

**Photogrammetry**
- Reconstructs 3D geometry from overlapping 2D photographs using Structure from Motion (SfM) and Multi-View Stereo (MVS).
- Produces point clouds with color (RGB) information.
- Accuracy depends on camera quality, overlap, ground control points. Typical: 1-5 cm outdoor, 1-5 mm indoor close-range.
- AEC context: Heritage documentation (lower cost than LiDAR), facade texture capture, drone site surveys.

**Structured Light**
- Projects a known light pattern (stripes, grids) onto a surface and captures deformation with cameras.
- Very high accuracy (sub-millimeter) but short range (typically < 2m).
- AEC context: Detailed documentation of ornamental elements, quality inspection of fabricated components.

#### 6.2 Registration

**ICP (Iterative Closest Point)**
- Aligns two overlapping point clouds by iteratively minimizing the distance between corresponding point pairs.
- Requires a reasonable initial alignment (within ~30 degrees rotation, ~50% overlap).
- Variants: Point-to-point ICP, point-to-plane ICP (faster convergence), generalized ICP.
- AEC workflow: Aligning multiple scan positions into a unified coordinate system.

**Target-Based Registration**
- Uses physical targets (spheres, checkerboard patterns) placed in the scene and visible from multiple scan positions.
- Registration accuracy depends on target placement geometry (well-distributed, not collinear).
- More reliable than ICP for large projects; typically achieves sub-millimeter registration error.
- AEC workflow: Standard for high-accuracy interior scanning of existing buildings.

#### 6.3 Filtering

**Statistical Outlier Removal (SOR)**
- For each point, computes the mean distance to its k nearest neighbors. Points with mean distances exceeding a threshold (e.g., mean + 2*std) are removed.
- Removes noise, phantom reflections, and isolated erroneous points.

**Voxel Downsampling**
- Divides space into a regular voxel grid and replaces all points within each voxel with a single representative point (centroid).
- Reduces point count uniformly while preserving overall shape.
- Typical: Downsample from 100M to 10M points for processing, then reference full-resolution cloud for detail.

**Pass-Through Filter**
- Removes all points outside a specified axis-aligned bounding box or distance range.
- Simple but effective for isolating regions of interest (e.g., a single building from a site scan).

#### 6.4 Segmentation

**RANSAC Plane Fitting**
- RANdom SAmple Consensus: Iteratively selects random point triplets, fits a plane, and counts inliers within a distance threshold.
- Robust to outliers; the dominant plane is extracted first, then subsequent planes from remaining points.
- AEC: Extracting walls, floors, ceilings, roofs as planar surfaces from scan data.

**Region Growing**
- Starts from seed points and expands regions by adding neighboring points that meet criteria (e.g., similar normal direction, within curvature threshold).
- Produces smooth, connected segments.
- AEC: Segmenting curved surfaces (vaulted ceilings, domed roofs) that RANSAC cannot handle.

**Clustering (DBSCAN, Euclidean)**
- Groups points based on spatial proximity without assuming geometric shape.
- DBSCAN handles arbitrary cluster shapes and identifies noise.
- AEC: Separating furniture from walls, isolating individual building components, identifying structural elements.

#### 6.5 Surface Reconstruction

**Poisson Surface Reconstruction**
- Formulates surface reconstruction as a Poisson equation, solving for an implicit function whose isosurface represents the surface.
- Produces watertight (closed) meshes. Requires oriented normals.
- Strengths: Handles noise well, produces smooth surfaces.
- Weaknesses: May fill holes where no data exists; boundary artifacts if normals are noisy.

**Ball-Pivoting Algorithm (BPA)**
- Simulates a ball of radius r rolling over the point cloud. When the ball contacts three points, a triangle is created.
- Produces meshes that closely follow the point data without extrapolation.
- Strengths: Does not fill gaps (preserves holes), fast for dense clouds.
- Weaknesses: Sensitive to ball radius parameter; fails on sparse or noisy data.

**Alpha Shapes**
- Generalizes convex hull with parameter alpha controlling the level of detail.
- Can produce non-manifold results and requires post-processing.
- AEC: Quick boundary extraction, rough surface reconstruction for visualization.

#### 6.6 Mesh from Point Cloud Workflows

1. Acquire scan data (LiDAR/photogrammetry).
2. Register multiple scans into unified coordinate system.
3. Filter: Remove noise (SOR), downsample (voxel grid), clip region of interest (pass-through).
4. Compute normals: Estimate and orient surface normals at each point.
5. Segment: Extract major geometric primitives (planes, cylinders) via RANSAC if needed.
6. Reconstruct surface: Poisson (for watertight mesh) or BPA (for preserving gaps).
7. Post-process mesh: Remove non-manifold elements, fill small holes, smooth, decimate to target face count.
8. Optionally: Fit NURBS surfaces to mesh regions for CAD integration.

#### 6.7 Tools

| Tool | Type | Strengths |
|------|------|-----------|
| CloudCompare | Open-source desktop | Registration, filtering, segmentation, surface reconstruction, comparison |
| Autodesk ReCap | Commercial | LiDAR import, registration, clash integration with Revit |
| Rhino + point cloud plugins | Commercial | Direct NURBS fitting from point clouds, Grasshopper integration |
| Open3D (Python) | Open-source library | Programmatic pipeline: filtering, registration, reconstruction |
| PDAL (Point Data Abstraction Library) | Open-source CLI/library | Format conversion, filtering, large-scale point cloud processing |
| PCL (Point Cloud Library) | Open-source C++ library | Full algorithmic toolkit for point cloud processing |

---

### 7. Coordinate Systems & Transformations

#### 7.1 Fundamental Transformations

**Translation**
- Moves geometry by a displacement vector (dx, dy, dz).
- Preserves shape, size, angles, and parallelism.
- Matrix: 4x4 identity with dx, dy, dz in the last column.

**Rotation**
- Rotates geometry around an axis by an angle.
- Preserves shape, size, and distances.
- Defined by: axis of rotation (point + direction) and angle.
- Matrix: 3x3 rotation sub-matrix within the 4x4 transformation.

**Scale**
- Uniform scale: Same factor in all directions. Preserves angles and proportions.
- Non-uniform scale: Different factors along X, Y, Z. Changes proportions, may affect angles.
- Scale center matters: scaling about the origin vs. about a custom point.

**Shear**
- Displaces points proportionally to their distance from a reference plane.
- Changes angles and proportions; parallelism is preserved.
- AEC: Rarely used intentionally but important to recognize in deformed geometry.

**Mirror (Reflection)**
- Reflects geometry across a plane.
- Reverses handedness (right-hand becomes left-hand).
- Important: Mirrored Breps have reversed face normals; mirrored text reads backward.
- AEC: Symmetric building wings, mirrored apartment layouts, reflected structural elements.

#### 7.2 Transformation Matrices (4x4 Homogeneous)

All affine transformations (translation, rotation, scale, shear, mirror) can be represented as 4x4 matrices operating on homogeneous coordinates [x, y, z, 1].

```
| R00  R01  R02  Tx |
| R10  R11  R12  Ty |
| R20  R21  R22  Tz |
|  0    0    0    1 |
```

- Upper-left 3x3: Rotation, scale, shear, mirror.
- Right column (Tx, Ty, Tz): Translation.
- Bottom row: [0, 0, 0, 1] for affine transformations.
- Matrix multiplication order: Transformations are applied right-to-left (the rightmost matrix is applied first).

#### 7.3 Euler Angles vs. Quaternions

**Euler Angles**
- Three rotation angles (typically roll, pitch, yaw or alpha, beta, gamma) applied in sequence around coordinate axes.
- Intuitive but suffer from gimbal lock (loss of one degree of freedom when two axes align).
- Multiple conventions (XYZ, ZYX, ZXZ, etc.) cause confusion.

**Quaternions**
- Four-component representation (w, x, y, z) encoding axis-angle rotation.
- No gimbal lock, smooth interpolation (SLERP), computationally efficient.
- Less intuitive to visualize but mathematically superior for rotation representation.
- Used in: Animation, robotic fabrication tool paths, camera control, structural dynamics.

#### 7.4 Construction Planes and Local Coordinate Systems

- A construction plane (CPlane) defines a local XY plane for drawing, measuring, and projecting.
- Components: Origin point, X-axis direction, Y-axis direction, Z-axis (normal) derived.
- In Rhino: Named CPlanes can be saved and recalled. The default World CPlane has origin at (0,0,0).
- AEC workflows: Set CPlane to a sloped roof surface for drawing roof elements in-plane; set CPlane to a wall face for placing openings.

#### 7.5 UV Space and Surface Parameterization

- Every NURBS surface has a parametric domain: U in [u_min, u_max] and V in [v_min, v_max].
- UV coordinates map to 3D points on the surface: S(u,v) -> (x, y, z).
- Surface parameterization may be non-uniform: equal parameter intervals may map to unequal arc lengths.
- Reparameterization: Normalize domain to [0,1] x [0,1] or reparameterize by arc length.
- AEC applications: Placing elements on curved facades (specify UV location), generating panelization grids, texture mapping.

#### 7.6 World to Screen Transformations

- The pipeline from 3D world coordinates to 2D screen pixels involves:
  1. Model transform: Local to world coordinates.
  2. View transform: World to camera/eye coordinates.
  3. Projection transform: Eye to clip coordinates (perspective or orthographic).
  4. Viewport transform: Clip to screen pixel coordinates.
- Each step is a matrix multiplication.
- AEC relevance: Understanding projection for rendering, setting up architectural views (plan, section, elevation, perspective), viewport-aligned annotations.

#### 7.7 Compound Transformations

- Multiple transformations combine by matrix multiplication.
- Order matters: Rotate-then-translate != Translate-then-rotate.
- Common pattern in AEC: Transform element from local coordinates (designed at origin) to world position (move to building location, rotate to correct orientation, scale if needed).
- Matrix decomposition: Given a compound transformation matrix, extract the individual translation, rotation, and scale components.

---

### 8. Tolerance & Precision

#### 8.1 Tolerance Types

**Absolute Tolerance**
- The maximum allowable distance between two entities for them to be considered coincident or joined.
- In Rhino: `DocumentProperties > Units > Absolute tolerance`. Default: 0.01 (units dependent).
- Affects: Curve joining, surface joining, boolean operations, intersection calculations.

**Relative Tolerance**
- A dimensionless ratio (percentage) controlling the accuracy of curve/surface approximations.
- In Rhino: Default 1%. Means approximations are within 1% of the true geometry.
- Affects: Curve fitting, surface fitting, isocurve density.

**Angular Tolerance**
- The maximum allowable angle (in degrees) between tangent vectors for entities to be considered tangent.
- In Rhino: Default 1 degree.
- Affects: Tangent continuity checking, smooth shading, edge joining decisions.

#### 8.2 Tolerance in Rhino

| Setting | Default | Range | Affects |
|---------|---------|-------|---------|
| Absolute tolerance | 0.01 | 0.0001 to 1.0 | Join, boolean, intersection, trim |
| Relative tolerance | 1% | 0.1% to 10% | Curve/surface approximation quality |
| Angular tolerance | 1 degree | 0.1 to 20 degrees | Tangent checking, smooth shading |
| Short curve tolerance | Derived from absolute | - | Minimum curve length threshold |

**Join Tolerance**: When joining curves or surface edges, edges within the absolute tolerance are joined. Edges farther apart than this tolerance remain naked (unjoined).

#### 8.3 Floating-Point Arithmetic Issues

- Computers use IEEE 754 double-precision floating-point (64-bit): ~15-17 significant decimal digits.
- This means: 0.1 + 0.2 != 0.3 exactly (it equals 0.30000000000000004).
- Implications for geometry: Never compare coordinates with `==`. Always use tolerance-based comparison: `|a - b| < tolerance`.
- Accumulated error: Long chains of geometric operations can accumulate floating-point error. Periodically refit/rebuild geometry to reset precision.
- Units matter: Working in millimeters (values ~1000) vs. meters (values ~1) affects relative precision. Very large coordinates (>1e6) or very small features (<1e-6) can cause precision problems.

#### 8.4 Tolerance Settings by Workflow

| Workflow | Recommended Absolute Tolerance | Notes |
|----------|-------------------------------|-------|
| Conceptual design | 1.0 mm or 0.1 in | Loose tolerance for fast iteration |
| Detailed design (architecture) | 0.1 mm or 0.01 in | Standard for building-scale models |
| Fabrication (CNC) | 0.01 mm or 0.001 in | Matches CNC machine precision |
| Fabrication (3D print) | 0.05-0.1 mm | Matches printer layer resolution |
| Structural analysis (FEA) | 1.0 mm | Mesh quality matters more than geometric precision |
| Survey/GIS integration | 10-100 mm | Matches survey instrument accuracy |
| Jewelry / small objects | 0.001 mm | Sub-micron precision for fine detail |

#### 8.5 Recommended Tolerances Table by Application

| Application | Absolute Tol. | Relative Tol. | Angular Tol. | Rationale |
|-------------|---------------|---------------|--------------|-----------|
| Curtain wall design | 0.1 mm | 1% | 1 deg | Glass panel fit tolerances |
| Steel fabrication | 0.01 mm | 0.5% | 0.5 deg | CNC cutting precision |
| Precast concrete | 1.0 mm | 1% | 1 deg | Mold precision + material shrinkage |
| Timber joinery | 0.1 mm | 1% | 0.5 deg | CNC router precision |
| Landscape grading | 10 mm | 5% | 5 deg | Survey accuracy, soil movement |
| MEP routing | 1.0 mm | 1% | 1 deg | Pipe/duct fitting tolerances |
| Heritage documentation | 0.5 mm | 0.5% | 0.5 deg | Match scanner accuracy |
| Urban massing | 100 mm | 5% | 5 deg | Conceptual, not fabrication-bound |
| Interior millwork | 0.05 mm | 0.5% | 0.5 deg | Fine cabinetry and joinery |
| Facade panelization | 0.1 mm | 1% | 1 deg | Panel fit and waterproofing seals |

#### 8.6 Best Practices

1. Set tolerance at project start and do not change it mid-project. Changing tolerance after geometry is created causes inconsistencies.
2. Model at the correct scale from the start. Do not model in meters and then scale to millimeters.
3. Keep geometry near the world origin. Points at coordinates > 1e6 lose precision (only ~10 digits remain for the fractional part).
4. Validate geometry regularly: Check for naked edges, non-manifold edges, micro-edges (shorter than tolerance), and degenerate faces.
5. When importing geometry from other software, match the source tolerance. If the source used 0.001 mm tolerance, do not join edges at 0.1 mm tolerance (this will create false joins).
6. For boolean operations, use the tightest tolerance that still produces successful results. Looser tolerance increases success rate but reduces accuracy.
7. Document your tolerance settings in the project BIM execution plan or computational design standards document.

---

### Summary

This skill provides the complete computational geometry foundation for AEC computational design. The hierarchy from points to voxels gives the right representation for every design stage. NURBS mathematics powers the freeform design language of contemporary architecture. Boolean operations enable the additive and subtractive logic of building assembly. Tessellation methods transform continuous surfaces into fabricable discrete elements. Surface analysis ensures that designed geometry is manufacturable and structurally sound. Point cloud processing bridges the physical and digital worlds. Coordinate transformations place every element precisely in space. And tolerance management ensures that the digital model translates faithfully to the physical artifact.

Every section in this skill is designed to be referenced during active computational design work -- whether you are writing a Grasshopper definition, a Python script in Rhino, a parametric model in Revit Dynamo, or a custom geometry kernel. The mathematics, workflows, and best practices here represent the accumulated knowledge of decades of computational geometry research applied to the specific demands of architecture, engineering, and construction.


## mesh-processing

### Mesh Processing

> Mesh data structures, mesh operations, mesh analysis, mesh repair, UV mapping and unfolding, quad meshing, mesh-to-NURBS conversion, and mesh quality assessment for AEC computational design

## Mesh Processing

This skill provides comprehensive guidance on mesh processing for architecture, engineering, and construction. Meshes are the workhorse representation for simulation (FEA, CFD, acoustics), fabrication (3D printing, CNC), visualization (rendering, VR/AR), and increasingly for design geometry itself. This reference covers data structures, operations, analysis, repair, UV mapping, quad meshing, and reverse engineering.

---

### 1. Mesh Processing in AEC

#### 1.1 Why Meshes Matter

Meshes represent 3D geometry as collections of vertices, edges, and faces. In AEC:

- **Simulation**: Finite Element Analysis (structural), Computational Fluid Dynamics (wind/airflow), thermal simulation, acoustic simulation, and daylight simulation all require mesh discretization of geometry. The mesh quality directly determines simulation accuracy.
- **Visualization**: Real-time rendering (game engines, VR/AR) operates on triangulated meshes. Level-of-detail mesh decimation controls rendering performance.
- **Fabrication**: 3D printing requires watertight triangulated meshes (STL/3MF). CNC milling requires surface meshes for toolpath generation. Robotic fabrication uses mesh representations for collision checking and path planning.
- **Scanning**: LiDAR, photogrammetry, and structured light scanning produce point clouds that are reconstructed into meshes. Scan-to-BIM workflows begin with mesh processing.
- **Design**: Freeform architectural surfaces (shells, facades, roofs) are often designed as meshes, particularly when the target is a panelized or discrete structure.

#### 1.2 Mesh vs. NURBS Trade-offs

| Dimension | Mesh | NURBS |
|---|---|---|
| Representation | Discrete vertices + faces | Continuous parametric surface |
| Precision | Approximate (chord tolerance) | Mathematically exact |
| Topology | Arbitrary (any connectivity) | Rectangular patch structure |
| Boolean operations | Robust (with good libraries) | Fragile (trimmed surface issues) |
| Simulation compatibility | Direct (FEA/CFD mesh = geometry mesh) | Requires meshing step |
| File size (complex forms) | Smaller (for tessellated freeform) | Larger (many control points) |
| Editing | Vertex-level sculpting, subdivision | Control point manipulation, continuity |
| Rendering | Direct (GPU operates on triangles) | Requires tessellation |
| Fabrication (3D print) | Direct (STL is triangulated mesh) | Requires tessellation |
| Industry standard | Visualization, gaming, scanning | CAD, BIM, manufacturing |

**When to use meshes in AEC**:
- Freeform geometry that resists NURBS patch layout (organic shapes, scanned surfaces)
- Direct-to-simulation workflows (structural shells, CFD domains)
- Fabrication output (3D printing, panelization)
- Processing scan data (point cloud to mesh to BIM)
- Real-time visualization and VR/AR content

**When to use NURBS**:
- Precise geometric control with continuity constraints (G0/G1/G2)
- Standard architectural elements (planar walls, cylindrical columns, ruled surfaces)
- BIM integration (Revit, ArchiCAD expect NURBS/solid geometry)
- Manufacturing with CNC that expects parametric surfaces

#### 1.3 The Mesh Processing Pipeline

```
[Input Geometry]
    |
    v
[Mesh Generation] -- from NURBS, from point cloud, from implicit, from scratch
    |
    v
[Mesh Repair] -- fix non-manifold, fill holes, remove degenerates, orient normals
    |
    v
[Mesh Operations] -- subdivide, remesh, decimate, smooth, boolean, offset
    |
    v
[Mesh Analysis] -- curvature, thickness, quality metrics, topology check
    |
    v
[Mesh Optimization] -- improve quality for target application (FEA, printing, rendering)
    |
    v
[Output]
    |-- Simulation mesh (FEA/CFD solver format)
    |-- Fabrication mesh (STL/3MF for 3D printing, unfolded for sheet fabrication)
    |-- Visualization mesh (glTF/FBX for rendering, LOD variants)
    |-- Reverse-engineered NURBS (mesh-to-NURBS conversion for CAD)
```

---

### 2. Mesh Data Structures

#### 2.1 Vertex-Face List (Simple Mesh)

The simplest representation. Two arrays:
- **Vertices**: List of 3D coordinates. V = [(x0,y0,z0), (x1,y1,z1), ..., (xn,yn,zn)]
- **Faces**: List of vertex index tuples. F = [(v0,v1,v2), (v0,v2,v3), ...] for triangles, or [(v0,v1,v2,v3), ...] for quads.

**Memory**: 3 floats per vertex (12 bytes as float32, 24 bytes as float64) + 3 or 4 ints per face (12 or 16 bytes as int32).

**Advantages**: Simple, compact, easy to serialize (STL, OBJ, PLY formats use this structure). Direct GPU upload.

**Limitations**: No explicit edge representation. Adjacency queries are O(F) where F = number of faces. Finding neighboring faces of a face requires scanning all faces. Finding all faces incident on a vertex requires scanning all faces.

**Use**: File I/O, GPU rendering, simple geometry storage. Not suitable for topological operations.

#### 2.2 Half-Edge Data Structure

The standard data structure for mesh processing algorithms. Each undirected edge is represented as two directed half-edges pointing in opposite directions.

**Components**:
- **Vertex**: Stores position (x,y,z) and pointer to one outgoing half-edge.
- **Face**: Stores pointer to one bounding half-edge.
- **Half-edge**: Stores pointers to:
  - `next`: Next half-edge around the same face (counter-clockwise).
  - `prev`: Previous half-edge around the same face (or computed from next).
  - `twin` (or `opposite`): The half-edge on the adjacent face sharing the same edge but pointing in the opposite direction.
  - `vertex`: The vertex this half-edge points to (its target vertex).
  - `face`: The face this half-edge bounds.

**Key traversal operations** (all O(1)):
- Adjacent face across an edge: `halfedge.twin.face`
- Next vertex around a face: `halfedge.next.vertex`
- All faces around a vertex: Follow `halfedge.twin.next` repeatedly until returning to start.
- All vertices adjacent to a vertex: Same traversal, collecting vertex pointers.
- Is edge on boundary?: `halfedge.twin == null` (boundary half-edges have no twin, or twin points to a null/boundary face).

**Memory**: Each half-edge stores 5 pointers (next, prev, twin, vertex, face). Each vertex stores 1 pointer. Each face stores 1 pointer. For a mesh with V vertices, E edges, and F faces: 2E half-edges * 5 pointers + V * 1 pointer + F * 1 pointer. Roughly 10E + V + F pointers.

**Implementations**:
- C++: OpenMesh, CGAL Surface_mesh, libigl (uses different internal structure but exposes half-edge interface)
- Python: trimesh (uses face adjacency internally, not true half-edge), OpenMesh Python bindings, pmp-library
- C#: Plankton (Grasshopper plugin, true half-edge), RhinoCommon Mesh (vertex-face list, not half-edge)

#### 2.3 Winged-Edge Data Structure

Predecessor to half-edge. Each edge stores pointers to:
- Two vertices (endpoints)
- Two faces (left and right)
- Four edges (next and previous on each face)

More complex to traverse than half-edge. Largely superseded by half-edge in modern implementations but historically important.

#### 2.4 Corner Table

Compact representation for triangle meshes. Each triangle has 3 corners (one per vertex). Each corner stores:
- Vertex index
- Opposite corner index (the corner across the shared edge in the adjacent triangle)

**Memory**: 2 integers per corner = 6 integers per triangle. Very compact.

**Advantages**: Cache-friendly, suitable for GPU processing. Jarek Rossignac's corner table enables efficient traversal with minimal storage.

**Limitations**: Triangle meshes only (no quads or n-gons).

#### 2.5 Data Structure Comparison

| Operation | Vertex-Face List | Half-Edge | Winged-Edge | Corner Table |
|---|---|---|---|---|
| Adjacent faces of face | O(F) | O(1) | O(1) | O(1) |
| Adjacent vertices of vertex | O(F) | O(valence) | O(valence) | O(valence) |
| Faces around vertex | O(F) | O(valence) | O(valence) | O(valence) |
| Boundary detection | O(E) | O(1) per edge | O(1) per edge | O(1) per corner |
| Edge collapse | Difficult | O(valence) | O(valence) | O(valence) |
| Face insertion | O(1) | O(1) | O(1) | O(1) |
| Memory per triangle | Low | Medium--High | High | Low |
| Implementation complexity | Simple | Medium | High | Medium |
| Quad/n-gon support | Yes | Yes | Yes | No (tri only) |

---

### 3. Mesh Operations Catalog

#### 3.1 Subdivision

Subdivision increases mesh resolution by splitting faces and repositioning vertices to approach a smooth limit surface.

##### Catmull-Clark Subdivision
- **Input**: Quad mesh (or mixed, but quad-dominant preferred)
- **Algorithm**: (1) Face points: centroid of each face. (2) Edge points: average of edge midpoint and adjacent face points. (3) Vertex points: weighted average of original vertex, adjacent face points, and adjacent edge midpoints. (4) Connect face points to edge points and vertex points to form new quads.
- **Properties**: Limit surface is C2 continuous everywhere except at extraordinary vertices (valence != 4), where it is C1. All faces become quads after one iteration.
- **Parameters**: Number of iterations (1--4 typical).
- **Use**: Smooth freeform surfaces, furniture design, organic shapes, rendering subdivision surfaces.

##### Loop Subdivision
- **Input**: Triangle mesh only
- **Algorithm**: (1) Edge points: weighted average of edge endpoints and opposite vertices. (2) Vertex points: weighted average of original vertex and neighbors. (3) Each triangle splits into 4 triangles.
- **Properties**: Limit surface is C2 except at extraordinary vertices (valence != 6), where it is C1. Output is always triangles.
- **Use**: Triangle mesh smoothing, FEA mesh refinement (with care).

##### Doo-Sabin Subdivision
- **Input**: Any mesh (quad, tri, mixed)
- **Algorithm**: Face-based. New vertices at weighted positions within each face. New faces formed from corner cutting. Dual-like operation.
- **Properties**: Limit surface is C1 everywhere. Produces mostly quad faces.
- **Use**: Less common. Rounded, bevel-like effect.

##### Sqrt(3) Subdivision
- **Input**: Triangle mesh
- **Algorithm**: Insert vertex at face centroid. Connect to face vertices. Flip original edges. Each triangle becomes 3 triangles.
- **Properties**: Slower refinement rate than Loop (sqrt(3) increase per iteration vs. 4x). Produces more uniform triangle sizes.
- **Use**: When gradual refinement is needed.

##### Mid-Edge Subdivision
- **Input**: Quad mesh
- **Algorithm**: Insert vertices at edge midpoints. Connect to form new quads. Simplest quad subdivision.
- **Properties**: No smoothing -- just refines topology. Use with separate smoothing step for controlled results.

#### 3.2 Decimation

Reduce face count while preserving shape as much as possible.

##### Vertex Decimation
Remove vertices and retriangulate the resulting hole. Simple but poor quality control.

##### Edge Collapse (QEM -- Quadric Error Metric)
- **Algorithm**: (1) For each vertex, compute a 4x4 quadric matrix Q representing the sum of squared distances to incident face planes. (2) For each edge, compute the optimal merged vertex position that minimizes the quadric error and the error value. (3) Collapse the edge with the smallest error. (4) Update quadric matrices for affected vertices. (5) Repeat until target face count reached.
- **Quality**: Excellent shape preservation. The gold standard for mesh decimation.
- **Parameters**: Target face count or target error threshold.
- **Boundary preservation**: Weight boundary edges higher to prevent boundary deformation.
- **Implementation**: trimesh (`simplify_quadric_decimation`), MeshLab (Quadric Edge Collapse Decimation), Open3D (`simplify_quadric_decimation`).

##### Face Clustering
Group adjacent faces into clusters. Replace each cluster with a single face. Fast but lower quality than QEM.

#### 3.3 Remeshing

Improve mesh quality without changing shape significantly.

##### Isotropic Remeshing
- **Goal**: Uniform triangle sizes. All edges approximately equal length.
- **Algorithm**: Iterative process: (1) Split long edges (> 4/3 * target length). (2) Collapse short edges (< 4/5 * target length). (3) Flip edges to improve vertex valence (target valence 6 for interior, 4 for boundary). (4) Smooth vertex positions (tangential Laplacian). Repeat 5--10 iterations.
- **Parameters**: Target edge length. Choose based on feature size and application needs.
- **Implementation**: CGAL `isotropic_remeshing`, PyMeshLab, libigl.

##### Anisotropic Remeshing
- **Goal**: Adapt triangle size and orientation to surface curvature. Small triangles in high-curvature areas, large triangles in flat areas.
- **Parameters**: Minimum and maximum edge length, curvature adaptation factor.
- **Use**: Efficient simulation meshes (fine where needed, coarse where geometry is simple).

##### Quad-Dominant Remeshing
- **Goal**: Replace triangle mesh with mostly-quad mesh. See Section 7 for detailed quad meshing.

##### Instant Meshes Approach
- **Algorithm**: Compute a smooth cross-field aligned to principal curvature directions. Extract a quad mesh from the field using integer-grid maps.
- **Tool**: Instant Meshes (free, standalone application). Extremely fast and produces high-quality quad meshes.
- **Parameters**: Target vertex count, edge orientation (alignment to features/boundaries).

#### 3.4 Smoothing

Reduce noise and irregularity in vertex positions.

##### Laplacian Smoothing
- **Algorithm**: Move each vertex toward the centroid of its neighbors: v_new = v_old + lambda * (centroid(neighbors) - v_old).
- **Parameter**: Lambda (0--1, typically 0.3--0.5) and iteration count (1--50).
- **Problem**: Volume shrinkage. Each iteration moves vertices inward, reducing overall volume.
- **Use**: Quick noise reduction when slight shrinkage is acceptable.

##### Taubin Smoothing (Volume-Preserving)
- **Algorithm**: Alternating Laplacian smoothing with positive lambda and negative mu: step 1: v = v + lambda * L(v), step 2: v = v + mu * L(v), where lambda > 0, mu < 0, and |mu| > lambda.
- **Parameters**: Lambda (0.3--0.5), mu (-0.31 to -0.53), iterations (5--50). Typical: lambda=0.5, mu=-0.53.
- **Advantage**: Preserves volume. The negative mu step inflates the mesh to compensate for the positive lambda step's shrinkage.
- **Use**: Scan data noise reduction where volume accuracy matters.

##### HC Laplacian Smoothing
- **Algorithm**: Modified Laplacian that preserves volume by tracking the original vertex positions and biasing the smoothed positions back toward them.
- **Advantage**: Better volume preservation than Taubin with similar smoothing quality.

##### Bilateral Smoothing
- **Algorithm**: Adapts bilateral filter from image processing. Smooths along the surface but preserves sharp features (edges, creases) by weighting neighbors by both spatial proximity and normal similarity.
- **Advantage**: Preserves sharp edges while smoothing flat areas. Ideal for architectural meshes with intended creases.
- **Parameters**: Spatial sigma (smoothing radius), normal sigma (feature sensitivity), iterations.

#### 3.5 Boolean Operations

Combine meshes using set operations.

##### Union (A + B)
Result contains all volume inside A or B. Merging two building volumes.

##### Difference (A - B)
Result contains volume inside A but not inside B. Cutting a courtyard out of a building mass.

##### Intersection (A ∩ B)
Result contains volume inside both A and B. Finding the overlap between two building footprints.

**Robustness issues**: Mesh booleans are notoriously fragile. Common failures:
- Coincident faces (faces from A and B are coplanar): causes ambiguous inside/outside classification.
- Near-miss intersections: numerical precision issues when intersection curves pass very close to existing vertices/edges.
- Non-manifold input: meshes with holes, self-intersections, or non-manifold topology cause boolean failure.

**Solutions**:
- Use exact arithmetic libraries (CGAL, libigl with exact predicates).
- Pre-process: repair meshes, remove degenerates, slightly perturb coincident geometry.
- Cork library: specifically designed for robust mesh booleans.
- Manifold library (Emmett Lalish): guaranteed-correct mesh booleans using halfedge structure.

**Implementation**:
- Python: trimesh (`boolean` via Blender/manifold3d), PyMeshLab, libigl
- C++: CGAL Nef_polyhedron, libigl boolean, Cork, Manifold
- Grasshopper: Mesh Boolean components (Rhino 7+), Cockatoo, Dendro (volume-based)
- Rhino: MeshBooleanUnion, MeshBooleanDifference, MeshBooleanIntersection commands

#### 3.6 Offset

Create a thickened or shell version of a mesh.

##### Vertex-Normal Offset
- **Method**: Move each vertex along its vertex normal by offset distance.
- **Problem**: Self-intersections at concave regions (normals converge inward). Gaps at convex regions (normals diverge outward).
- **Mitigation**: Post-process with self-intersection removal. Or use variable offset distance based on local curvature.

##### Minkowski Sum Offset
- **Method**: Convolve the mesh with a small sphere. Mathematically correct but computationally expensive.
- **Implementation**: CGAL Minkowski_sum_3.

##### Implicit Offset
- **Method**: Convert mesh to signed distance field (SDF). Offset by adjusting the iso-surface level. Extract the new mesh from the modified SDF.
- **Advantage**: No self-intersections. Works on complex geometry.
- **Implementation**: OpenVDB (voxel-based SDF), Dendro (Grasshopper plugin wrapping OpenVDB).

##### Shell/Thickening for 3D Printing
- **Method**: Create inner offset surface (vertex-normal offset inward), close the boundary edges between inner and outer surfaces, creating a hollow shell.
- **Parameters**: Wall thickness (minimum depends on material: 1mm for SLA resin, 2mm for FDM PLA, 3mm for SLS nylon).

#### 3.7 Other Operations

##### Weld/Unweld Vertices
- **Weld**: Merge vertices within a tolerance distance. Reduces vertex count and creates shared edges. Essential after importing meshes with duplicate vertices.
- **Unweld**: Split shared vertices, creating separate vertices per face at a given edge. Used to create hard edges for rendering (normal discontinuities) or to detach faces for unfolding.

##### Edge Flip
Swap the diagonal of a quad formed by two adjacent triangles. Used during remeshing to improve vertex valence. A triangle pair (v0,v1,v2) and (v1,v3,v2) becomes (v0,v1,v3) and (v0,v3,v2).

##### Edge Collapse
Merge two vertices connected by an edge into one vertex. The fundamental operation of decimation. All faces incident on the removed vertex are updated or removed.

##### Edge Split
Insert a new vertex at the midpoint of an edge. Split the two adjacent faces. Increases mesh resolution locally.

##### Fill Hole
Find boundary loops (sequences of boundary edges forming a closed path). Create new faces to close the hole. Methods: simple fan triangulation (from a single vertex), advancing front (adds triangles from the boundary inward), minimum area triangulation, Liepa's algorithm (curvature-aware filling).

##### Extract Boundary
Identify all boundary edges (edges with only one adjacent face). Group into boundary loops (closed sequences of boundary edges). Output as polyline curves.

##### Mesh Slice/Contour
Intersect mesh with a plane. Output: one or more closed polylines (the cross-section curves). Used for: section drawings, contour lines, layer slicing for 3D printing.

##### Mesh from Curves
Loft between profile curves, ruled surface between two curves, patch from boundary curve, Coons patch from four boundary curves, Delaunay triangulation of point set (2D or on surface).

---

### 4. Mesh Analysis

#### 4.1 Curvature Estimation on Meshes

On smooth surfaces, curvature is well-defined. On meshes (piecewise-flat), curvature must be estimated.

##### Discrete Gaussian Curvature
```
K_v = (2*pi - sum(angles at v)) / A_v
```
Where `sum(angles at v)` is the sum of face angles meeting at vertex v, and A_v is the area associated with vertex v (one-third of incident face areas, or the Voronoi area).

- K > 0: elliptic (dome-like)
- K = 0: flat or saddle with equal principal curvatures
- K < 0: hyperbolic (saddle-like)

Gauss-Bonnet theorem: sum of K_v * A_v over all vertices = 2 * pi * chi, where chi is the Euler characteristic.

##### Discrete Mean Curvature
```
H_v = (1 / (4 * A_v)) * sum over edges at v of: (cot(alpha_ij) + cot(beta_ij)) * (v_i - v_j)
```
Where alpha_ij and beta_ij are the angles opposite to edge (v_i, v_j) in the two adjacent faces (cotangent Laplacian formula).

|H_v| is half the magnitude of the Laplacian vector, which points in the mean curvature normal direction.

##### Principal Curvatures
```
k1 = H + sqrt(H^2 - K)
k2 = H - sqrt(H^2 - K)
```
Where k1 >= k2 are the maximum and minimum principal curvatures.

Principal curvature directions require fitting a quadric to the local mesh neighborhood (Taubin's method) or computing the shape operator from the discrete differential geometry operators.

**Applications in AEC**:
- Panelization: high curvature regions need smaller panels or doubly-curved panels.
- Structural: curvature determines membrane stresses in shells.
- Fabrication: developable (K=0) surfaces can be unrolled flat; non-zero K requires stretching/compression.

#### 4.2 Thickness Analysis

Determine the minimum material thickness at every point on a mesh. Critical for 3D printing and structural assessment.

##### Ray-Based Method
- From each vertex, cast a ray inward (along -normal). Find the nearest intersection with the mesh. The distance is the local thickness.
- **Issue**: Misses cases where thickness is measured to a non-opposite face.

##### Sphere-Based Method
- At each vertex, find the largest inscribed sphere that is tangent to the mesh at that vertex and at least one other point. The sphere diameter is the local thickness.
- More accurate than ray-based, but computationally expensive.

**Thresholds by application**:
- FDM 3D printing: minimum 1.5--2.0 mm wall, 0.8 mm feature
- SLA 3D printing: minimum 0.5--1.0 mm wall, 0.3 mm feature
- SLS 3D printing: minimum 1.0--1.5 mm wall, 0.5 mm feature
- CNC milling: depends on tool diameter, typically 1.0 mm minimum feature

#### 4.3 Normal Analysis

##### Face Normals
Cross product of two edge vectors: n_f = (v1 - v0) x (v2 - v0), normalized.

##### Vertex Normals
Weighted average of incident face normals. Weighting options:
- Uniform: simple average (fast but biased by tessellation).
- Area-weighted: larger faces contribute more (most common).
- Angle-weighted: weight by the face angle at that vertex (theoretically better for irregular meshes).

##### Normal Consistency
All face normals should point outward (for a closed mesh) or consistently to one side (for an open mesh). Inconsistent normals cause rendering artifacts (back faces visible) and boolean/offset failures.

**Fix**: Use connected-component flood fill. Starting from a seed face with known correct orientation, propagate consistent orientation to all connected faces via shared edges.

#### 4.4 Area and Volume Computation

**Surface area**: Sum of all face areas.
```
Area_total = sum(0.5 * |(v1-v0) x (v2-v0)|) for all triangles
```

**Volume** (for closed, consistently-oriented mesh):
```
Volume = (1/6) * sum(v0 . (v1 x v2)) for all triangles
```
(Signed volume via divergence theorem. Positive for outward normals.)

#### 4.5 Mesh Quality Metrics

| Metric | Definition | Ideal | Acceptable | Poor |
|---|---|---|---|---|
| Aspect ratio | Longest edge / shortest edge (per face) | 1.0 (equilateral) | < 3.0 | > 5.0 |
| Skewness | 1 - (min_angle / ideal_angle) | 0.0 | < 0.5 | > 0.75 |
| Min angle | Smallest angle in triangle | 60 degrees (equilateral) | > 20 degrees | < 10 degrees |
| Max angle | Largest angle in triangle | 60 degrees (equilateral) | < 140 degrees | > 160 degrees |
| Jacobian | Determinant of element shape function Jacobian | 1.0 | > 0.3 | < 0.1 |
| Edge length ratio | Max edge / min edge (globally) | 1.0 | < 5.0 | > 10.0 |
| Face area ratio | Max area / min area (globally) | 1.0 | < 10.0 | > 100.0 |
| Valence deviation | |vertex valence - 6| for interior (tri mesh) | 0 | <= 2 | > 3 |

#### 4.6 Topological Analysis

**Euler characteristic**:
```
chi = V - E + F
```
For a closed mesh with genus g: chi = 2 - 2g. Sphere: chi = 2, g = 0. Torus: chi = 0, g = 1.

**Boundary loops**: Connected sequences of boundary edges. A watertight mesh has 0 boundary loops. An open mesh (like a shell) has 1 or more.

**Non-manifold edges**: Edges shared by more than 2 faces. Indicate topological errors.

**Non-manifold vertices**: Vertices where the incident faces do not form a single fan (disk topology). The vertex is a "pinch point" where two surface sheets meet.

**Connected components**: Number of separate, disconnected mesh pieces. For a single solid: 1 component. Shells with separate inner and outer meshes: 2 components.

---

### 5. Mesh Repair

#### 5.1 Common Defects and Repair Strategies

##### Non-Manifold Edges
- **Symptom**: Edge shared by 3+ faces. Causes boolean failure, offset failure, slicing failure.
- **Repair**: Identify non-manifold edges. Duplicate the edge and associated vertices. Separate the face groups into independent manifold sheets. Choose which sheet to keep, or merge them into a single manifold.

##### Non-Manifold Vertices
- **Symptom**: Vertex where incident faces don't form a proper fan topology. Two surface sheets pinched at a point.
- **Repair**: Duplicate the vertex. Assign each face group its own copy.

##### Degenerate Faces
- **Symptom**: Faces with zero area (collinear vertices) or near-zero area (very thin sliver triangles).
- **Repair**: Remove zero-area faces. Collapse sliver triangles by collapsing their shortest edge.

##### Duplicate Vertices
- **Symptom**: Two or more vertices at the same position (within tolerance). Causes edges to appear as boundary even though geometry is continuous.
- **Repair**: Weld vertices within tolerance (merge duplicates). Typical tolerance: 1e-6 to 1e-3 times the bounding box diagonal.

##### Self-Intersections
- **Symptom**: Faces penetrating through other faces of the same mesh.
- **Detection**: AABB tree intersection queries between all face pairs (accelerated with bounding volume hierarchy).
- **Repair**: Compute intersection curves. Retriangulate intersecting faces along intersection curves. Remove internal faces. Complex -- often easier to rethink the geometry than to repair algorithmically.

##### Inconsistent Normals
- **Symptom**: Some face normals point inward, others outward. Causes visual artifacts (black faces in rendering) and incorrect volume computation.
- **Repair**: Orient normals consistently using connected-component flood fill from a seed face. For closed meshes, then flip all if necessary so normals point outward (test with signed volume).

##### Holes
- **Symptom**: Boundary edges forming open loops. Mesh is not watertight.
- **Repair**: Identify boundary loops. Fill each hole with new faces. Use advanced filling algorithms (Liepa) to match surrounding curvature.

##### T-Junctions
- **Symptom**: A vertex lies on an edge of an adjacent face but is not topologically connected to it. The faces appear to share a boundary but are not properly connected.
- **Repair**: Split the edge at the T-junction vertex. Update face connectivity.

#### 5.2 Automated Repair Workflows

##### MeshLab Repair Pipeline
1. Import mesh (STL, OBJ, PLY, OFF).
2. Filters > Cleaning and Repairing > Remove Duplicate Vertices.
3. Filters > Cleaning and Repairing > Remove Duplicate Faces.
4. Filters > Cleaning and Repairing > Remove Zero Area Faces.
5. Filters > Cleaning and Repairing > Remove Non-Manifold Edges.
6. Filters > Cleaning and Repairing > Remove Non-Manifold Vertices.
7. Filters > Normals, Curvatures > Re-Orient All Faces Coherently.
8. Filters > Remeshing > Close Holes (set max hole size).
9. Export repaired mesh.

##### Rhino MeshRepair Command
Interactive wizard:
1. `_MeshRepair` command.
2. Check for: non-manifold edges, duplicate faces, degenerate faces, naked edges (holes), disjoint pieces.
3. Apply repairs step-by-step.
4. `_FillMeshHoles` for hole filling.
5. `_UnifyMeshNormals` for normal consistency.
6. `_RebuildMeshNormals` for vertex normal recomputation.

##### trimesh Repair (Python)
```python
import trimesh

mesh = trimesh.load("input.stl")

## Check mesh properties
print(f"Watertight: {mesh.is_watertight}")
print(f"Volume: {mesh.volume}")
print(f"Euler number: {mesh.euler_number}")

## Automatic repair
trimesh.repair.fix_normals(mesh)
trimesh.repair.fix_winding(mesh)
trimesh.repair.fill_holes(mesh)
mesh.remove_degenerate_faces()
mesh.remove_duplicate_faces()
mesh.remove_unreferenced_vertices()

## Merge close vertices
mesh.merge_vertices()

print(f"Watertight after repair: {mesh.is_watertight}")

mesh.export("repaired.stl")
```

#### 5.3 3D Print Preparation Checklist

- [ ] Mesh is watertight (no boundary edges, 0 holes)
- [ ] No self-intersections
- [ ] No non-manifold edges or vertices
- [ ] Consistent outward-facing normals
- [ ] No degenerate or zero-area faces
- [ ] Minimum wall thickness met (material-dependent)
- [ ] No inverted faces
- [ ] Single connected component (or intentionally separate pieces)
- [ ] File size manageable (decimate if > 50 MB for typical printers)
- [ ] Units correct (mm for most slicers)
- [ ] Geometry fits build volume
- [ ] Overhangs assessed for support structure needs

---

### 6. UV Mapping & Unfolding

#### 6.1 UV Parameterization Methods

UV mapping assigns 2D coordinates (u,v) to every vertex on a 3D mesh surface, creating a flattening of the surface into a 2D plane.

##### Conformal (Angle-Preserving) -- LSCM
- **Least Squares Conformal Maps**: Minimizes angular distortion. Angles on the UV plane match angles on the 3D surface as closely as possible.
- **Properties**: Preserves angles. May distort areas (triangles may be scaled differently). Requires at least 2 fixed (pinned) boundary vertices.
- **Use**: Texture mapping where pattern alignment matters (bricks, wood grain).

##### Authalic (Area-Preserving)
- **Minimizes area distortion**: Each triangle's UV area is proportional to its 3D area.
- **Properties**: Preserves areas. May distort angles.
- **Use**: Fabrication unfolding where material usage must be accurate.

##### ABF++ (Angle-Based Flattening)
- **Optimizes per-angle**: Each angle in each triangle is optimized independently to match its 3D counterpart.
- **Properties**: Very low angular distortion. High quality for complex surfaces.
- **Use**: High-quality texture mapping.

##### ARAP (As-Rigid-As-Possible)
- **Minimizes combined angular and area distortion**: Each triangle should be as close to a rigid transformation of its 3D counterpart as possible.
- **Properties**: Good balance between angle and area preservation. No fixed boundary required (free boundary).
- **Use**: General-purpose parameterization. Fabrication unfolding.

#### 6.2 Seam Placement Strategies

The UV map requires cuts (seams) to unfold a 3D surface into 2D. Seam placement affects distortion and fabrication:

- **Minimum distortion**: Place seams along high-curvature edges (ridges, valleys) where distortion would be worst without a cut.
- **Feature alignment**: Place seams along natural edges (building corners, panel joints).
- **Minimum total seam length**: Fewer/shorter seams = less physical joining in fabrication.
- **Visibility**: In texture mapping, place seams where they are least visible (back of object, under overhangs).
- **Automatic seam generation**: Methods based on curvature analysis, spectral analysis, or user-guided tools.

#### 6.3 Distortion Metrics

| Metric | Formula | Ideal | Meaning |
|---|---|---|---|
| Angular distortion | max |UV_angle - 3D_angle| per triangle | 0 | Shape preservation |
| Area distortion | (UV_area / 3D_area) / mean_ratio | 1.0 | Scale consistency |
| Stretch (L2) | sqrt(eigenvalues of Jacobian) | 1.0 | Directional stretch |
| Stretch (Linf) | max singular value of Jacobian | 1.0 | Maximum stretch in any direction |
| Isometric distortion | Frobenius norm of (J - R) where R is nearest rotation | 0.0 | Overall rigidity |

#### 6.4 Unfolding for Fabrication

##### Strip Unfolding
For surfaces of revolution or ruled surfaces: cut along rulings and unfold into flat strips. Each strip is a developable surface (Gaussian curvature = 0) and unrolls without distortion.

Steps:
1. Divide the surface into approximately developable strips.
2. For each strip, compute the ruling directions.
3. Unfold each strip by rotating faces around shared edges until flat.
4. Output as 2D cutting patterns with fold lines and tabs.

##### Flattening Double-Curved Panels
Non-developable (K != 0) panels cannot be unfolded without distortion. Strategies:
- **Approximate with developable strips**: Divide the panel into narrow strips that are approximately developable.
- **Allow controlled stretching**: Specify maximum allowable stretch (e.g., 1--2%) for flexible materials like fabric or sheet metal.
- **Use darts/seams**: Cut darts into the pattern to absorb excess material in areas of positive curvature.
- **Spring-back compensation**: For bent metal panels, adjust the unfolded pattern to account for elastic spring-back.

##### Pepakura-Style Unfolding
For complex freeform meshes fabricated from flat sheet material (paper, cardboard, thin metal):
1. Unfold all mesh faces into a connected 2D layout.
2. Add tabs (flaps) along certain edges for gluing/joining.
3. Arrange (nest) unfolded pieces on standard sheet sizes.
4. Score fold lines. Cut boundary lines.
5. Fold and assemble.

**Tools**: Pepakura Designer (commercial), ExactFlat (Rhino plugin), custom Grasshopper definitions.

##### Tab Placement for Physical Assembly
- Place tabs on alternating edges so that every joint has one tab and one non-tab edge.
- Tab width: 5--15 mm for paper/cardboard, proportional to face size.
- Tab shape: trapezoidal (narrower at tip) for easier folding and gluing.
- Mark fold direction (mountain/valley) on the pattern.

##### Nesting Unfolded Pieces
Pack 2D pieces onto rectangular sheets with minimal waste:
- **Algorithms**: Bottom-left fill, no-fit polygon, genetic algorithm optimization.
- **Spacing**: Minimum 2--5 mm between pieces for cutting tool kerf.
- **Grain direction**: For wood or directional materials, align pieces with grain.
- **Tools**: RhinoNest (Rhino plugin), SVGnest (free web tool), DeepNest (free), custom Python with shapely.

---

### 7. Quad Meshing

#### 7.1 Why Quads Matter

- **FEA**: Quadrilateral elements generally produce more accurate results than triangles for the same element count. Quad elements have better convergence properties for thin shell analysis.
- **Subdivision**: Catmull-Clark subdivision requires quad input for best results. The limit surface from quads is C2 except at extraordinary vertices.
- **Fabrication**: Planar quad meshes (PQ meshes) map directly to flat panel fabrication. Each quad face is a flat panel. Edges define the structural grid.
- **Aesthetics**: Quad meshes produce cleaner, more regular visual patterns for facades, cladding, and structural grids.
- **Mesh editing**: Quads support edge loop selection and operations that are natural for modeling workflows.

#### 7.2 Methods

##### Parameterization-Based
1. Compute a global parameterization (UV mapping) of the surface.
2. Place a regular grid in UV space.
3. Map the grid back to 3D.
4. The regularity of the grid in UV space produces a regular quad mesh on the surface.
5. **Limitation**: UV distortion causes non-uniform quad sizes. Singularities in parameterization create degenerate quads.

##### Field-Guided (Cross-Field) Methods
1. Compute principal curvature directions on the surface (or user-specified directions).
2. Smooth the direction field to create a globally consistent cross-field (4-RoSy field).
3. Integrate the cross-field to find a parameterization aligned with the field.
4. Extract the quad mesh from the parameterization.
5. **Advantage**: Quads align with curvature directions, which is structurally and aesthetically optimal.
6. **Singularities**: Cross-field singularities (points where the field direction is undefined) become extraordinary vertices in the quad mesh.

##### Integer-Grid Maps
1. Compute a seamless parameterization aligned to a cross-field.
2. The parameterization maps the surface to the plane with integer grid lines as edges.
3. Round to integer values to extract exact quad connectivity.
4. **Advantage**: Produces pure quad meshes with minimal singularities.
5. **State of the art**: Methods like QuadCover, MIQ, IGM.

##### Instant Meshes
- Standalone application by Wenzel Jakob et al.
- Computes a smooth cross-field and extracts quad mesh in seconds.
- Input: triangle mesh (OBJ, PLY). Output: quad-dominant mesh.
- User controls: target vertex count, edge orientation constraints, boundary alignment.
- Excellent for quick quad remeshing of scanned or sculpted meshes.

##### Catmull-Clark + Retopology
1. Start with a coarse hand-built quad cage that approximates the target shape.
2. Apply Catmull-Clark subdivision to get a smooth surface.
3. Project subdivided vertices onto the target surface.
4. Iterate: adjust cage, subdivide, project, evaluate.
5. **Use**: Manual retopology for characters, organic shapes. Less automated but maximum control.

#### 7.3 Singularities in Quad Meshes

In a pure quad mesh, most interior vertices have valence 4 (connected to 4 edges). Vertices with valence != 4 are "extraordinary" or "singular":

- **Valence 3**: One quad edge missing. Creates a "corner" effect. Gaussian curvature > 0 (convex bump) at limit surface.
- **Valence 5**: One extra quad edge. Creates a "saddle" effect. Gaussian curvature < 0 (saddle) at limit surface.
- **Higher valence (6+)**: Multiple missing/extra edges. Strong singularity. Generally avoided.

**Design principles**:
- Minimize the number of extraordinary vertices.
- Place them in low-visibility areas or where curvature naturally changes.
- Avoid adjacent extraordinary vertices (creates poor limit surface quality).
- Use the Euler formula constraint: for a closed surface of genus g, the total index (sum of valence-4 for each vertex) equals 4(1-g). A sphere requires exactly 8 extraordinary vertices of valence 3 (or equivalent total index).

#### 7.4 Alignment to Features

Quad mesh edges should align with:
- **Surface boundaries**: Boundary-aligned quads ensure clean edges without fragmented triangles.
- **Creases/sharp edges**: Quad edges along creases preserve sharp features through subdivision.
- **Principal curvature directions**: Alignment produces structurally optimal meshes for shells and better visual quality.
- **Architectural grids**: Align to building axes, column grids, or facade modules.
- **Fabrication constraints**: Align to material directions, panel sizes, or machine axes.

#### 7.5 Quad Mesh Quality Metrics

| Metric | Definition | Ideal | Acceptable | Poor |
|---|---|---|---|---|
| Planarity (max deviation) | Max distance from face vertices to best-fit plane | 0 mm | < L/500 | > L/100 |
| Aspect ratio | Length / width of quad | 1.0 | 0.5--2.0 | < 0.2 or > 5.0 |
| Interior angle | Each of 4 angles | 90 degrees | 60--120 degrees | < 30 or > 150 degrees |
| Edge length uniformity | Max edge / min edge | 1.0 | < 2.0 | > 5.0 |
| Singularity count | Number of extraordinary vertices | Minimum possible | < 5% of vertices | > 10% of vertices |
| Diagonal ratio | Long diagonal / short diagonal | 1.0 (square) | < 2.0 | > 3.0 |

---

### 8. Mesh-to-NURBS Conversion

#### 8.1 Reverse Engineering Workflow

Converting a mesh (from scanning, sculpting, or simulation) back to NURBS surfaces for CAD/BIM integration:

```
[Input Mesh]
    |
    v
[Clean and Repair] -- remove noise, fill holes, fix topology
    |
    v
[Segmentation] -- divide mesh into regions for individual NURBS patches
    |
    v
[Quad Remeshing] -- convert each region to a regular quad grid
    |
    v
[Surface Fitting] -- fit NURBS surface to each quad region
    |
    v
[Continuity Matching] -- adjust patches for G0/G1/G2 continuity across boundaries
    |
    v
[Validation] -- measure deviation between NURBS surfaces and original mesh
    |
    v
[Output NURBS Model]
```

#### 8.2 Patch Layout from Quad Mesh

The quad mesh structure naturally defines a NURBS patch layout:
- Each regular quad region (all interior vertices have valence 4) maps to one NURBS patch.
- Extraordinary vertices define patch corners where multiple patches meet.
- Edge loops between extraordinary vertices define patch boundaries.

**Automatic patch layout**: Identify extraordinary vertices in a quad mesh. Trace edge loops between them to define patch boundaries. Each enclosed region becomes one surface patch.

#### 8.3 Surface Fitting to Mesh Patches

For each patch region:
1. Extract the quad grid vertices as a 2D array (u rows x v columns).
2. Fit a NURBS surface to the vertex positions using least-squares approximation.
3. Control the number of control points (degree of approximation). More control points = closer fit but heavier surface.
4. Evaluate deviation: compute distance from each original mesh vertex to the fitted surface. Target: maximum deviation < tolerance (typically 0.1--1.0 mm for AEC).

#### 8.4 Continuity Between Patches

Adjacent NURBS patches must connect smoothly:
- **G0 (positional)**: Patches share boundary positions. No gap. This is the minimum requirement.
- **G1 (tangent)**: Tangent planes match across the boundary. No visible crease. Achieved by constraining the first row of control points across the boundary.
- **G2 (curvature)**: Curvature matches across the boundary. Seamless reflection highlights. Achieved by constraining the first two rows of control points.

#### 8.5 Automatic vs. Manual Approaches

**Automatic** (Rhino `MeshToNurb`):
- Creates one NURBS face per mesh face. For a 10,000-face mesh, this produces 10,000 trimmed planar surfaces. Not useful for most purposes.

**Semi-automatic** (Rhino `_Patch`, `_SrfFromPtGrid`, `_NetworkSrf`):
- Select mesh regions manually. Fit surfaces using Rhino surfacing tools.
- Time-consuming for complex meshes (hours to days).

**Dedicated reverse engineering** (Geomagic Design X, Mesh2Surface for Rhino, SpaceClaim):
- Automated segmentation, fitting, and continuity enforcement.
- Guided workflow with interactive adjustment.
- Best results for scan-to-CAD workflows.

#### 8.6 Scan-to-BIM Considerations

Converting scanned mesh data (LiDAR, photogrammetry) to BIM objects:
- **Point cloud to mesh**: Poisson surface reconstruction, ball-pivoting, alpha shapes.
- **Mesh to geometric primitives**: Detect planes, cylinders, spheres in mesh. Fit parametric shapes. Map to BIM categories (wall, floor, column, pipe).
- **Accuracy targets**: USIBD Level of Accuracy (LOA) specification: LOA10 = 50mm, LOA20 = 15mm, LOA30 = 5mm, LOA40 = 1mm.
- **Tools**: Autodesk ReCap, CloudCompare, Trimble RealWorks, FARO SCENE, Scan-to-BIM Revit plugins.

---

### 9. Tools Reference

#### 9.1 Desktop Applications

| Tool | Platform | Strengths | Mesh Formats | Cost |
|---|---|---|---|---|
| MeshLab | Win/Mac/Linux | Repair, filtering, remeshing, measurement, massive meshes | STL, OBJ, PLY, OFF, 3DS, X3D, VRML, U3D | Free |
| Rhino | Win/Mac | NURBS + mesh hybrid, Grasshopper integration, SubD | STL, OBJ, PLY, 3DM, FBX, STEP, IGES | Commercial |
| Blender | Win/Mac/Linux | Sculpting, retopology, modifiers, animation, rendering | STL, OBJ, PLY, FBX, glTF, USD, ABC | Free |
| Instant Meshes | Win/Mac/Linux | Fast quad remeshing from triangle meshes | OBJ, PLY | Free |
| CloudCompare | Win/Mac/Linux | Point cloud and mesh comparison, registration | STL, OBJ, PLY, E57, LAS, PTS | Free |

#### 9.2 Grasshopper Plugins

| Plugin | Developer | Key Capabilities | Cost |
|---|---|---|---|
| Weaverbird | Giulio Piacentino | Subdivision (Catmull-Clark, Loop), mesh topology operations, smoothing | Free |
| MeshEdit | ? | Advanced mesh editing, mesh from curves, mesh offsetting | Free |
| Plankton | Daniel Piker, Will Pearson | Half-edge mesh data structure for Grasshopper. True topological mesh queries. | Free |
| Cockatoo | Max Eschenbach | Polyline-based mesh operations, mesh skeletonization | Free |
| Dendro | ecr labs | Volume-based mesh operations using OpenVDB. Robust booleans, offsets, blends. | Free |
| Kangaroo | Daniel Piker | Physics-based mesh relaxation, form-finding, planarization | Free (bundled with Rhino 7+) |
| MeshMachine | Daniel Piker | Mesh topology editing (insert edge loops, merge vertices) | Free |
| Lunchbox | Nathan Miller | Paneling, surface subdivision, math surfaces | Free |
| Ivy | Tukal (Zubin Khabazi) | Mesh unfolding/flattening for fabrication | Free |

#### 9.3 Python Libraries

| Library | Key Features | Installation |
|---|---|---|
| trimesh | Load/save 20+ formats, repair, boolean (via manifold3d), ray casting, convex hull, section, thickness, proximity | `pip install trimesh` |
| Open3D | Point cloud + mesh processing, registration, visualization, reconstruction, TSDF | `pip install open3d` |
| PyMeshLab | Python bindings for MeshLab. Access all MeshLab filters programmatically. | `pip install pymeshlab` |
| libigl (Python bindings) | Discrete differential geometry, parameterization, boolean, FEM | `pip install libigl` |
| pyvista | Mesh visualization, filtering, analysis. VTK wrapper. | `pip install pyvista` |
| meshio | Universal mesh I/O for simulation formats (VTU, MSH, MED, XDMF, Abaqus, ANSYS) | `pip install meshio` |
| pygalmesh | Python interface to CGAL mesh generation | `pip install pygalmesh` |
| numpy-stl | Simple STL read/write with numpy arrays | `pip install numpy-stl` |

#### 9.4 C++ Libraries

| Library | Key Features |
|---|---|
| CGAL | Comprehensive computational geometry: mesh processing, boolean, remeshing, parameterization, surface reconstruction. Industrial-strength. |
| libigl | Header-only. Discrete differential geometry, parameterization, boolean, deformation. Research-oriented. |
| OpenMesh | Half-edge data structure. Subdivision, decimation, smoothing. Clean API. |
| VCGlib | MeshLab's underlying library. Mesh processing, simplification, filtering. |
| OpenVDB | Sparse voxel data structure. Level set operations, mesh-to-volume, volume-to-mesh, CSG. |
| Manifold | Guaranteed-correct mesh booleans. Fast, robust. By Emmett Lalish (Google). |
| pmp-library | Polygon Mesh Processing. Modern C++. Subdivision, remeshing, smoothing, parameterization. |

---

### Summary: Choosing the Right Operation

| I need to... | Operation | Key Tool |
|---|---|---|
| Add detail to a coarse mesh | Subdivision (Catmull-Clark for quads, Loop for tris) | Weaverbird, trimesh |
| Reduce polygon count for performance | Decimation (QEM edge collapse) | MeshLab, trimesh, Open3D |
| Get uniform triangle sizes | Isotropic remeshing | CGAL, PyMeshLab |
| Get aligned quad mesh | Quad remeshing | Instant Meshes, CGAL |
| Remove scan noise | Smoothing (Taubin for volume preservation) | MeshLab, trimesh |
| Combine two shapes | Boolean union | Manifold, Dendro, CGAL |
| Create a hollow shell | Offset (implicit via SDF) | Dendro, OpenVDB |
| Fix a broken mesh for 3D printing | Repair pipeline | trimesh, MeshLab |
| Flatten for fabrication | UV unfolding (ARAP) | Ivy, Pepakura, ExactFlat |
| Convert mesh to NURBS for CAD | Reverse engineering | Mesh2Surface, Geomagic, Rhino manual |
| Analyze curvature for panelization | Discrete curvature estimation | libigl, Grasshopper curvature components |
| Check mesh for simulation suitability | Quality metrics (aspect ratio, skewness) | PyMeshLab, pyvista |
| Planarize quad mesh faces | Physics-based planarization | Kangaroo, custom optimization |


## algorithmic-patterns

### Algorithmic Patterns

> L-systems, cellular automata, agent-based modeling, swarm intelligence, reaction-diffusion, growth algorithms, packing algorithms, and nature-inspired computation for AEC design

## Algorithmic Patterns for AEC Design

### 1. Nature-Inspired Computation in AEC

#### Why Biological Algorithms Matter for Design

For three and a half billion years, evolution has solved the optimization problems architects and engineers face daily: distributing material efficiently, creating structures that resist loads with minimal mass, organizing circulation for millions of agents, regulating temperature without mechanical systems, and generating complex forms from simple rules. Nature-inspired computation translates these solutions into programmable algorithms that transform AEC practice.

The fundamental insight is that complexity does not require complex instructions. A fern frond with thousands of precisely placed leaflets emerges from a recursive rule fitting in a single line of code. A termite mound maintaining two-degree temperature stability is built by agents following three local rules. An oak tree optimally distributing material to resist wind has no central controller -- it grows according to Wolff's law, depositing material where stress is highest.

#### Emergence and Self-Organization

Emergence produces macro-scale patterns from micro-scale interactions without centralized control. In AEC, this challenges conventional top-down design, replacing it with local rules and boundary conditions that self-organize into coherent spatial configurations.

**Key properties of emergent systems:**
- **Nonlinearity** -- small changes in rules produce disproportionate changes in output
- **Feedback loops** -- positive feedback amplifies patterns, negative feedback stabilizes them
- **Decentralization** -- no single agent has global knowledge of the system
- **Adaptation** -- the system responds to environmental changes in real time
- **Robustness** -- local failures do not cascade to system-level collapse

The computational thesis underlying all algorithmic patterns is that irreducible complexity can emerge from reducible rules. Stephen Wolfram demonstrated this with elementary cellular automata: Rule 110, defined by 8 binary transitions, is Turing-complete. A one-dimensional grid of cells with two states and nearest-neighbor rules can compute anything computable. For AEC: a branching structure with thousands of unique members can be specified by 3-4 L-system rules; a facade with apparent randomness generated by a 2-state CA; an optimal circulation network by 10,000 agents following 3 flocking rules.

| Aspect | Top-Down (Traditional) | Bottom-Up (Algorithmic) |
|--------|----------------------|------------------------|
| Control | Centralized | Distributed |
| Specification | Global geometry | Local rules |
| Adaptability | Low (manual redesign) | High (rules adapt) |
| Scalability | Difficult | Inherent |
| Novelty | Limited by imagination | Generates unexpected solutions |

#### Applications Across AEC

| Domain | Algorithm Class | Application |
|--------|----------------|-------------|
| Urban growth | Cellular automata, ABM | Land use simulation, sprawl prediction |
| Structural branching | L-systems, space colonization | Tree columns, dendritic roofs |
| Facade patterning | Reaction-diffusion, CA | Perforated screens, shading panels |
| Space planning | Agent-based, packing | Room layout, furniture arrangement |
| Material distribution | Topology optimization, DLA | Graded density structures |
| Circulation design | Ant colony, shortest path | Corridor networks, staircase placement |
| Acoustic design | Reaction-diffusion, fractal | Diffuser panel geometry |
| Thermal design | Swarm optimization | Ventilation opening placement |

---

### 2. L-Systems (Lindenmayer Systems)

#### Formal Grammar

An L-system is a parallel rewriting system G = (V, w, P) where V is the alphabet, w is the axiom (initial string), and P is the production rules. Unlike Chomsky grammars, all rules apply simultaneously, modeling biological growth where cells divide concurrently.

#### DOL-Systems (Deterministic, Context-Free)

Each variable has exactly one production rule; rules are context-independent.

**Algae (Lindenmayer's original):** `Alphabet: {A,B} | Axiom: A | Rules: A->AB, B->A`
String length follows the Fibonacci sequence: A, AB, ABA, ABAAB, ABAABABA.

**Koch Curve:** `Axiom: F | Rule: F->F+F-F-F+F | Angle: 90deg`
Fractal dimension log(5)/log(3) = 1.465.

**Sierpinski Triangle:** `Axiom: F-G-G | Rules: F->F-G+F+G-F, G->GG | Angle: 120deg`

**Dragon Curve:** `Axiom: FX | Rules: X->X+YF+, Y->-FX-Y | Angle: 90deg`

**Hilbert Curve:** `Axiom: A | Rules: A->-BF+AFA+FB-, B->+AF-BFB-FA+ | Angle: 90deg`

#### Stochastic L-Systems

Multiple rules per predecessor with probabilities summing to 1:
```
F -> F[+F]F[-F]F    (p=0.33)
F -> F[+F]F          (p=0.33)
F -> FF-[-F+F+F]+[+F-F-F]  (p=0.34)
```
No two generated trees are identical, yet all share the same structural grammar. Critical for facades with varied but coherent panel geometries.

#### Context-Sensitive L-Systems

Rules depend on adjacent symbols: `A < B > C -> D` (B becomes D only between A and C). AEC application: signal propagation along structural members -- stress information triggers material deposition only where neighbors indicate high stress.

#### Parametric L-Systems

Symbols carry numerical parameters with guard conditions:
```
A(l,w) : l > 0.1 -> F(l) [+(30) A(l*0.7, w*0.8)] [-(30) A(l*0.7, w*0.8)]
A(l,w) : l <= 0.1 -> (terminal leaf)
```
Parameters 0.7 and 0.8 control child-to-parent ratios, mapping directly to Murray's law for biological branching.

#### Turtle Interpretation

| Symbol | Action | Symbol | Action |
|--------|--------|--------|--------|
| `F` | Move forward, draw line | `[` | Push state (branch start) |
| `f` | Move forward, no draw | `]` | Pop state (branch end) |
| `+`/`-` | Turn left/right by delta | `&`/`^` | Pitch down/up (3D) |
| `\`/`/` | Roll left/right (3D) | `!` | Decrement diameter |

#### Extended Grammars

**Binary Tree (2D):**
```
Axiom: 0
Rules: 1 -> 11, 0 -> 1[+0]-0
Angle: 45 degrees, Iterations: 7
```
Produces a symmetric binary tree with 128 terminal branches.

**Stochastic Shrub:**
```
Axiom: F
Rules: F -> FF+[+F-F-F]-[-F+F+F] (p=0.5), F -> FF-[-F+F]+[+F-F] (p=0.5)
Angle: 22.5 degrees, Iterations: 4
```

**3D Tree (with pitch and roll):**
```
A -> F(1)[&(30)B][/(120)&(30)B][/(240)&(30)B]
B -> F(0.8)[+(25)$C][--(25)$C]B
C -> F(0.5)[+(20)$C][--(20)$C]
```

**City Block Generator:**
```
X -> F[-X][+X]FX | F -> FF
Angle: 90 degrees
```
Generates recursive block subdivision resembling organic street networks.

**Column Capital (parametric, 3D):**
```
A(h,r) -> F(h,r) [+(60)&(40) B(h*0.3,r*0.6)] [+(180)&(40) B(h*0.3,r*0.6)] [+(300)&(40) B(h*0.3,r*0.6)]
B(h,r) : h > 0.05 -> F(h,r) [+(45)&(30) B(h*0.5,r*0.7)] [-(45)&(30) B(h*0.5,r*0.7)]
```

#### AEC Applications

**Branching Structures:** Tree-columns in airports and stations (Stuttgart Airport, Sendai Mediatheque). A 5-rule L-system defines a column branching into 200+ terminal supports for a roof canopy.

**Root-Like Foundations:** Inverted L-system trees distributing loads through soil following optimized branching angles per Murray's law.

**Dendritic Circulation:** Corridor systems following L-system branching produce naturally navigable spaces with clear hierarchy.

**Fractal Facades:** Koch-curve-based facades provide increased surface area for shading while maintaining structural regularity.

#### Implementation

**Python:**
```python
def l_system(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        current = "".join(rules.get(c, c) for c in current)
    return current
```
**Grasshopper:** String rewriting via text components, Anemone loop for iterations, turtle geometry components for line/curve generation, pipe/mesh for 3D visualization.

---

### 3. Cellular Automata (CA)

#### 1D Elementary CA (Wolfram's 256 Rules)

A row of binary cells; next state depends on 3-cell neighborhood (8 configurations, 2^8 = 256 rules).

**Rule 30** (chaotic): Aperiodic, seemingly random from a single cell. Found on Conus textile shell.
**Rule 90** (Sierpinski): XOR of neighbors. Perfect for facade patterning -- regularity with complexity.
**Rule 110** (Turing-complete): Proved by Cook (2004). Generates gliders and spaceships. The simplest known universal computer.

#### 2D Cellular Automata

**Game of Life (B3/S23):** Dead cell with 3 neighbors is born; alive cell with 2-3 survives; all others die. Produces gliders, oscillators, guns, and self-replicating patterns.

**Urban Growth (B3678/S2345678):** Compact blob growth mimicking suburban sprawl. Adjusting to B45/S2345 produces polycentric growth.

**Floor Plan Generator (B3/S1234):** From random initial conditions, produces room-like enclosed spaces connected by narrow passages.

#### Neighborhoods

**Von Neumann (4):** Orthogonal patterns for rectilinear layouts. **Moore (8):** Organic, rounded patterns; standard for most 2D CA. **Extended Moore (24, radius 2):** Smoother boundaries for urban simulation. **Hexagonal (6):** Isotropic, no directional bias.

#### State Transitions and Multi-State CA

**Binary (0/1):** Simplest case -- cell is active or inactive.

**Multi-state (0-N):** Enables gradient effects and functional zoning:
- State 0: empty / undeveloped
- State 1: residential low-density
- State 2: residential high-density
- State 3: commercial
- State 4: industrial
- State 5: park / green space

Transition rules encode zoning logic: residential adjacent to 3+ commercial cells transitions to mixed-use. Green space cells never transition (protected). Totalistic CA depends only on the sum of neighbor states; outer-totalistic (like Game of Life) depends on center state AND neighbor sum but not arrangement.

#### 3D Cellular Automata

Cubic lattice with 6 (von Neumann), 18 (edge-sharing), or 26 (Moore) neighbors.

**Structural topology application:**
```
States: solid (1), void (0)
Initial: solid block
Rules: Death: solid cell with < 4 solid Moore-26 neighbors -> void
       Birth: void cell with 8-12 solid neighbors -> solid
```
Produces porous, trabecular bone-like structures exportable as mesh for 3D printing or CNC fabrication.

#### AEC Applications

**Urban Growth Simulation:** SLEUTH/DUEM models simulate decades of land-use change for infrastructure planning.
**Structural Topology:** Voxel rules remove low-stress material, approximating optimal distributions.
**Facade Patterns:** CA grid mapped to facade; cell states determine panel type. Rule 90 produces Sierpinski; Game of Life produces organic patterns.

**Python:**
```python
import numpy as np
from scipy.signal import convolve2d
def gol_step(grid):
    n = convolve2d(grid, np.array([[1,1,1],[1,0,1],[1,1,1]]), mode='same', boundary='wrap')
    return ((grid==0) & (n==3) | (grid==1) & ((n==2)|(n==3))).astype(int)
```

---

### 4. Agent-Based Modeling (ABM)

#### Agent Architecture

An agent has: position (x,y,z), velocity, state variables (energy, type, memory), behavioral rules executed each timestep, perception radius, and communication mode (direct messaging or stigmergy).

**Environments:** Grid-based (simple collision, coarse simulations), continuous (realistic pedestrian/vehicle movement, requires KDTree spatial indexing), network-based (agents move along graph edges for transit simulation).

#### Stigmergy

Indirect communication through environment modification. Agents deposit pheromone; it diffuses (Gaussian blur) and evaporates: `P(t+1) = P(t) * (1 - rho)`. Others sense gradients and bias movement toward high concentrations. This is how ant colonies find shortest paths -- and how pedestrians create desire lines.

#### Flocking (Reynolds Boids)

Three rules applied each timestep:
- **Separation:** `force = sum((self.pos - neighbor.pos) / dist^2)` within separation_radius
- **Alignment:** `force = avg(neighbor.velocity) - self.velocity` within alignment_radius
- **Cohesion:** `force = centroid(neighbors) - self.pos` within cohesion_radius

Combined: `velocity += w1*sep + w2*ali + w3*coh; clamp(velocity, max_speed); pos += velocity*dt`

High w1 = dispersed; high w2 = parallel streams; high w3 = tight swarms; balanced = natural flocking.

#### Ant Colony Optimization (ACO)

Path selection: `P(i->j) = (tau_ij^alpha * eta_ij^beta) / sum(tau_ik^alpha * eta_ik^beta)` where tau = pheromone, eta = 1/distance. Pheromone update: `tau = (1-rho)*tau + Q/L_k` for ants using edge.

**AEC:** Hospital corridor layout optimization. Nodes = rooms (ER, ICU, pharmacy). ACO minimizes total daily staff travel distance, producing a connectivity graph that informs spatial adjacency.

#### Termite Mound Algorithms

Stigmergic construction: deposit material where pheromone is high; deposits emit pheromone; positive feedback creates pillars, arches, chambers. Translates to robotic construction agents building without centralized control.

#### AEC Applications

**Pedestrian Flow:** Thousands of agents navigating stations/malls; identify bottlenecks, optimize door placement.
**Evacuation:** Social force model (Helbing) validates egress timeframes with body-compression physics.
**Urban Morphogenesis:** Developer/resident agents produce clustering, segregation, gentrification from individual decisions.
**Structural Placement:** Agents walking force-flow lines deposit material at convergences, reflecting principal stress trajectories.
**Adaptive Facades:** Each panel is an agent with sensors/actuators, coordinating shading with neighbors.

**Tools:** Quelea (Grasshopper real-time ABM), NetLogo (visual ABM platform), Mesa (Python framework integrating with compas/ladybug/honeybee).

---

### 5. Swarm Intelligence

#### Particle Swarm Optimization (PSO)

```
v_i = w*v_i + c1*r1*(p_i - x_i) + c2*r2*(g - x_i)
x_i = x_i + v_i
```
w (inertia): 0.9 -> 0.4 over iterations. c1, c2 (cognitive/social): typically 2.0. r1, r2: random [0,1].
**AEC:** Optimize building orientation, WWR, shading angles via EnergyPlus fitness function. Converges in 50-200 iterations.

#### ACO Pheromone Strategies

**Ant System:** All ants deposit; simple but slow. **Ant Colony System:** Best-ant-only with local decay; faster convergence. **MAX-MIN:** Bounded pheromone prevents premature convergence.
**AEC:** Pipe routing through ceiling cavities minimizing length while avoiding structural members.

#### Bee Algorithm

Scout bees (random global search), employed bees (local exploitation), onlooker bees (quality-weighted roulette selection). Abandoned food sources trigger scouting.
**AEC:** Multi-objective optimization balancing energy performance, structural efficiency, daylight, and cost.

#### Firefly Algorithm

Attractiveness: `beta(r) = beta_0 * exp(-gamma*r^2)`. Brighter fireflies attract dimmer ones; distance-dependent attraction clusters solutions around promising regions.
**AEC:** Structural member sizing -- each firefly is a set of beam/column cross-sections; brightness = low weight satisfying constraints.

| Criterion | PSO | ACO | Bee | Firefly |
|-----------|-----|-----|-----|---------|
| Continuous variables | Excellent | Poor | Good | Good |
| Discrete/combinatorial | Poor | Excellent | Good | Fair |
| Multi-objective | Fair | Fair | Good | Fair |
| Convergence speed | Fast | Moderate | Moderate | Slow |
| Best AEC use | Parametric opt. | Routing/layout | Multi-objective | Sizing opt. |

---

### 6. Reaction-Diffusion

#### Turing Patterns

Two morphogens -- activator (slow diffusion, self-promoting) and inhibitor (fast diffusion, activator-suppressing) -- produce stable spatial patterns via short-range activation / long-range inhibition: spots, stripes, labyrinths, inverse spots. Found throughout biology: leopard spots, zebra stripes, seashell markings, fingerprints.

#### Gray-Scott Model

```
du/dt = Du*laplacian(u) - u*v^2 + f*(1-u)
dv/dt = Dv*laplacian(v) + u*v^2 - (f+k)*v
```
Typical: Du=0.16, Dv=0.08. The (f,k) parameter space maps to distinct regimes:

| f | k | Pattern Type |
|---|---|-------------|
| 0.010 | 0.045 | Spots (mitosis) |
| 0.022 | 0.051 | Spots and stripes |
| 0.030 | 0.057 | Stripes / labyrinthine |
| 0.040 | 0.063 | Worms / meandering |
| 0.050 | 0.065 | Holes (inverse spots) |
| 0.025 | 0.060 | Solitons (isolated spots) |
| 0.014 | 0.054 | Pulsating spots |

#### Belousov-Zhabotinsky Patterns

Chemical reaction producing concentric target waves and spiral waves. Modeled by Oregonator equations. AEC: spiral/concentric patterns for acoustic diffusers breaking up sound reflections.

#### AEC Applications

**Facade Patterning:** Concentration field drives perforation density -- dense shading where solar gain is highest, open where views are prioritized.
**Structural Porosity:** 3D reaction-diffusion determines solid/void in 3D-printed elements, lighter than solid while maintaining load paths.
**Ventilation:** Opening density correlates with local wind pressure via tuned diffusion parameters.
**Acoustic Diffusers:** Labyrinthine patterns achieve broadband diffusion without periodicity artifacts.

#### Implementation

Discretized Laplacian (5-point): `L(u,i,j) = u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1] - 4*u[i,j]`
9-point stencil (more isotropic): weight corners 0.05, edges 0.2, center -1.0.

```python
import numpy as np
def gray_scott_step(u, v, f, k, Du=0.16, Dv=0.08, dt=1.0):
    Lu = np.roll(u,1,0)+np.roll(u,-1,0)+np.roll(u,1,1)+np.roll(u,-1,1) - 4*u
    Lv = np.roll(v,1,0)+np.roll(v,-1,0)+np.roll(v,1,1)+np.roll(v,-1,1) - 4*v
    uvv = u*v*v
    return np.clip(u+dt*(Du*Lu-uvv+f*(1-u)),0,1), np.clip(v+dt*(Dv*Lv+uvv-(f+k)*v),0,1)
```
256x256 runs real-time on CPU; 512+ requires GPU (CUDA/WebGL compute shaders).

---

### 7. Growth and Packing Algorithms

#### Diffusion-Limited Aggregation (DLA)

Seed at origin; random walkers perform Brownian motion, sticking permanently on cluster contact. Fractal dimension ~1.71 (2D). Produces patterns resembling lightning, river deltas, mineral dendrites, frost.
**AEC:** Branching structural topologies refined by FEA, green infrastructure networks (branching bioswales).

#### Space Colonization Algorithm

Attraction points fill target volume (canopy envelope). Tree nodes grow toward nearest points; points consumed within kill distance. Parameters: influence distance, kill distance, step length D, point distribution.
**AEC:** Column-tree structures for large-span roofs with branch density proportional to local load. More natural branching than L-systems for canopy-filling geometries.

#### Circle/Sphere Packing

**Apollonian gasket:** Recursive tangent circle insertion (D~1.31). **RSA:** Random placement rejecting overlaps; jams at ~54.7% coverage. **Force-directed:** Repulsive forces between overlapping circles iterate to equilibrium, producing dense organic packings.

```python
def force_pack(circles, iterations=1000):
    for _ in range(iterations):
        for i, ci in enumerate(circles):
            force = [0, 0]
            for j, cj in enumerate(circles):
                if i == j: continue
                d = dist(ci, cj); overlap = (ci.r + cj.r) - d
                if overlap > 0:
                    force[0] += overlap * (ci.x-cj.x)/d
                    force[1] += overlap * (ci.y-cj.y)/d
            ci.x += force[0]*0.1; ci.y += force[1]*0.1
```
**AEC:** Column placement (circles = tributary areas), window placement on curved facades, bubble diagrams for space planning.

#### Bin Packing and Graph Algorithms

**2D Nesting:** Irregular polygons on sheets; NP-hard; bottom-left + NFP heuristics. CNC steel cutting, facade panel nesting. 5-10% efficiency gain = significant cost savings.

**Dijkstra:** Shortest paths O((V+E)log V) for service routing. **A*:** Heuristic-guided single-target wayfinding. **MST:** Minimum-length corridor/utility networks (Kruskal/Prim).

---

### 8. Space-Filling and Fractal Geometry

#### Fractal Dimension

`D = log(N)/log(S)` for self-similar fractals. Box-counting method: cover pattern with epsilon-boxes, plot log(N) vs. log(1/epsilon); slope = D. Urban analysis: compact cities D~2.0; sprawling cities D~1.3-1.5. Track D over time to quantify sprawl. Skyline D~1.3-1.5 correlates with visual preference.

#### Iterated Function Systems (IFS)

Contractive affine transformations applied recursively. Barnsley fern: 4 transformations with probabilities (stem p=0.01, leaflets p=0.85, branches p=0.07 each). AEC: decorative screens, tile designs, mullion layouts with parameterized self-similarity.

#### Space-Filling Curves

**Hilbert curve:** Visits every point in 2^N x 2^N grid preserving locality. AEC: CNC toolpaths, sensor placement, robotic inspection routes.
**Peano curve:** 3x3 recursive, denser coverage. **Z-Order (Morton):** Bit-interleaved 2D-to-1D for spatial database indexing.

#### Self-Similar Structures and Fractal Architecture

Historical examples of fractal architecture:
- **African vernacular settlements:** Recursive compound layouts where village plans mirror individual compound plans (Ron Eglash's research)
- **Hindu temples:** Shikhara towers with recursive self-similar profile
- **Gothic cathedrals:** Pointed arch motif repeated at window, door, vault, and building scales
- **Menger sponge structures:** Theoretical 3D fractal (D=log(20)/log(3)=2.727) with infinite surface area and zero volume, informing ultra-lightweight structural concepts

**Fractal analysis of cities:**
- Street networks: organic medieval cities D~1.8-1.9 vs. grid cities D~2.0 vs. suburban dendritic D~1.3-1.5
- Building footprints: D of built/unbuilt boundary correlates with walkability and urban vitality
- Skyline silhouettes: D~1.3-1.5 correlates with visual preference in perception studies

---

### 9. Implementation Guide

#### Grasshopper Ecosystem

- **Anemone:** Looping and recursion for iterative algorithms
- **Quelea:** Real-time agent-based simulation with custom force fields
- **Heteroptera:** CA and ABM utilities
- **4D Noise:** Perlin/simplex noise field generation
- **Kangaroo 2:** Physics simulation (particle-spring, packing)
- **Dendro:** Volume/SDF operations for 3D CA output
- **Cocoon:** Isosurface extraction from scalar fields
- **C# scripting:** 10-100x faster than GhPython for tight numerical loops

#### Python Libraries

`numpy` (array ops, convolution), `scipy` (KDTree, signal processing), `matplotlib` (visualization), `networkx` (graph algorithms), `compas` (AEC geometry framework), `shapely` (2D polygon ops), `trimesh` (3D mesh export).

**Performance:** Vectorize with numpy (100x over Python loops). scipy.spatial.KDTree for O(log n) agent neighbor queries. Preallocate arrays. GPU via cupy/CUDA for grids > 512x512.

#### Processing/p5.js for Visualization

**Processing (Java):** Excellent for real-time interactive visualization. Built-in 2D/3D rendering with straightforward pixel manipulation for CA and RD simulations.

**p5.js (JavaScript):** Browser-based Processing ideal for client presentations and web demos. WebGL mode enables GPU-accelerated rendering of large simulations. Particularly effective for interactive reaction-diffusion and flocking demonstrations.

#### Performance Considerations

**Grid resolution vs. computation:**
- 256x256 RD: real-time on CPU. 1024x1024: requires GPU (CUDA, OpenCL, WebGL compute).
- Doubling grid resolution quadruples memory and computation per step.

**Agent scaling:**
- ABM: O(N^2) naive -> O(N log N) with spatial hashing/KDTree. Essential for >10,000 agents.

**Memory management:**
- 3D CA at 256^3: 16M cells, 16 MB/step. 100 timesteps = 1.6 GB. Use sparse representations for low fill ratios.

**Convergence:**
- L-systems: deterministic, terminate after specified generation count.
- CA/RD: may need thousands of steps to reach steady state. Define convergence threshold (change between steps < epsilon).
- ABM: may never reach equilibrium. Use maximum iteration limits or target metric values.

---

### Algorithm Selection Guide

| Design Goal | Algorithm | Rationale |
|-------------|-----------|-----------|
| Branching structure | L-system / Space Colonization | Controlled recursion with biological analogy |
| Organic facade pattern | Gray-Scott reaction-diffusion | Tunable Turing patterns with density control |
| Regular-complex pattern | CA (Rule 90, Game of Life) | Deterministic complexity from simple rules |
| Pedestrian flow analysis | ABM (boids + social force) | Captures individual decision-making |
| Structural optimization | PSO / topology-optimized CA | Continuous variable optimization |
| Routing optimization | Ant Colony Optimization | Graph-based combinatorial problems |
| Column/support placement | Circle packing, force-directed | Distributes supports with minimum spacing |
| Panel nesting (fabrication) | 2D bin packing, NFP nesting | Minimizes material waste |
| Urban growth prediction | CA (SLEUTH) or ABM | Captures spatial dynamics of development |
| Ventilation openings | Reaction-diffusion | Organic density variation across surface |
| Multi-objective optimization | Bee Algorithm, NSGA-II | Balanced Pareto front exploration |
| Fractal complexity analysis | Box-counting dimension | Quantifies pattern complexity across scales |

---

### References

- Prusinkiewicz, P. & Lindenmayer, A. (1990). *The Algorithmic Beauty of Plants*. Springer.
- Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.
- Reynolds, C. (1987). "Flocks, Herds, and Schools." SIGGRAPH.
- Turing, A. (1952). "The Chemical Basis of Morphogenesis." Phil. Trans. Royal Society.
- Pearson, J.E. (1993). "Complex Patterns in a Simple System." Science, 261(5118).
- Runions, A. et al. (2007). "Modeling Trees with a Space Colonization Algorithm." Eurographics.
- Shiffman, D. (2012). *The Nature of Code*. Self-published.
- Terzidis, K. (2006). *Algorithmic Architecture*. Architectural Press.
- Hensel, M., Menges, A. & Weinstock, M. (2010). *Emergent Technologies and Design*. Routledge.
- Frazer, J. (1995). *An Evolutionary Architecture*. Architectural Association.
- Coates, P. (2010). *Programming.Architecture*. Routledge.
- Dorigo, M. & Stutzle, T. (2004). *Ant Colony Optimization*. MIT Press.
- Kennedy, J. & Eberhart, R. (1995). "Particle Swarm Optimization." IEEE ICNN.
- Witten, T.A. & Sander, L.M. (1981). "Diffusion-Limited Aggregation." PRL.
- Eglash, R. (1999). *African Fractals*. Rutgers University Press.


## generative-design

### Generative Design

> Evolutionary algorithms, multi-objective optimization, design space exploration, fitness function design, population-based methods, and generative workflows for AEC computational design

## Generative Design for AEC Computational Design

### 1. Generative Design Paradigm

#### 1.1 Definition and Scope

Generative design is a computational design methodology in which a designer defines a problem through goals, constraints, and variable parameters, and an algorithmic system autonomously generates, evaluates, and evolves candidate solutions across a defined design space. Unlike traditional design where the human produces every solution manually, generative design shifts the designer's role from direct form-maker to curator of outcomes — defining *what* is desired rather than *how* to achieve it.

In the AEC context, generative design applies to problems ranging from single-building floor plan layouts and structural topologies to neighborhood-scale massing studies and infrastructure routing. The common thread is a design space too large for exhaustive manual exploration.

#### 1.2 Distinction from Parametric Design

The confusion between parametric and generative design is pervasive. The distinction is fundamental:

| Aspect | Parametric Design | Generative Design |
|---|---|---|
| **Core action** | Define relationships between parameters | Explore the solution space algorithmically |
| **Designer's role** | Adjust sliders, observe outcomes | Define objectives and constraints, curate results |
| **Output** | One solution per parameter state | Population of diverse candidate solutions |
| **Search method** | Manual, intuition-driven | Automated, algorithm-driven |
| **Model requirement** | Parametric model with exposed variables | Parametric model + fitness function + solver |
| **Typical scale** | Dozens to hundreds of manual explorations | Thousands to millions of evaluated candidates |

A parametric model is a *prerequisite* for generative design — it provides the mechanism by which the solver manipulates geometry. But parametric design alone does not search; it merely responds to human input. Generative design automates the search.

#### 1.3 The Generate-Evaluate-Evolve Loop

Every generative design process follows a three-phase loop:

1. **Generate** — The solver creates candidate solutions by sampling or evolving design variable values within defined ranges. In evolutionary approaches, this involves applying genetic operators (crossover, mutation) to parent solutions.

2. **Evaluate** — Each candidate is assessed against one or more fitness functions. This is typically the computational bottleneck: running energy simulations, structural analyses, daylight calculations, or spatial adjacency checks for every individual in every generation.

3. **Evolve** — Based on evaluation results, the solver selects better-performing candidates and uses them to produce the next generation. Over many iterations, the population converges toward high-performing regions of the design space.

This loop continues until convergence criteria are met: a generation limit is reached, fitness improvements plateau below a threshold, or population diversity drops below a minimum.

#### 1.4 When to Use Generative Design

Generative design is appropriate when:

- The design space is large (more than 5-10 independent variables)
- Multiple conflicting objectives must be balanced simultaneously
- Optimal or near-optimal performance is critical (structural efficiency, energy, cost)
- The relationship between variables and outcomes is non-linear and non-intuitive
- The designer needs evidence-based justification for design decisions
- Time exists for computational exploration (hours to days of compute)

Generative design is **not** appropriate when:

- The problem is well-understood and a known heuristic suffices
- Only one or two variables are being tuned (manual slider adjustment is faster)
- Evaluation is extremely expensive and no surrogate model is feasible
- Aesthetic or experiential qualities dominate and resist quantification
- The parametric model is unstable or produces invalid geometry frequently

#### 1.5 Design Agency and Authorship

The designer retains authorship because they define the problem, construct the fitness landscape, set constraints, and select solutions. The algorithm is a tool with no intent. However, generative design shifts creative decisions upstream: defining what matters (fitness functions), what is possible (variable ranges), and what is acceptable (feasibility thresholds). This demands deeper understanding of design performance than traditional workflows.

#### 1.6 Human-in-the-Loop vs. Fully Automated Generation

**Fully automated**: Solver runs autonomously from initialization to convergence. Designer intervenes only at setup and selection. Appropriate for well-defined problems with reliable fitness functions.

**Human-in-the-loop (IEC)**: Designer evaluates candidates subjectively during optimization, guiding evolution toward aesthetically or experientially desirable outcomes.

The hybrid approach — automated fitness for quantifiable metrics, human selection for qualitative criteria — is often most productive in practice.

---

### 2. Evolutionary Algorithm Fundamentals

#### 2.1 Genetic Algorithm (GA) — Core Framework

The Genetic Algorithm is the foundational evolutionary optimization method used in AEC generative design. Inspired by Darwinian natural selection, it maintains a population of candidate solutions that evolve over generations through selection, crossover, and mutation.

##### 2.1.1 Encoding Schemes

The encoding (genotype representation) determines how design variables are stored and manipulated:

**Binary encoding**: Variables as bit strings (e.g., 8-bit = 0-255). Simple operators but suffers from Hamming cliffs and imprecision for continuous variables.

**Real-valued encoding**: Variables as floating-point numbers directly. Standard for AEC — design variables (dimensions, angles, positions) are inherently continuous. Used by all major Grasshopper solvers.

**Permutation encoding**: For ordering problems (room sequencing, scheduling). Requires order-preserving operators (PMX, OX, CX).

**Tree/graph encoding**: For evolving solution topology itself (bracing patterns, connectivity graphs). Enables topological innovation but complex to implement.

##### 2.1.2 Selection Methods

Selection determines which individuals become parents for the next generation:

**Tournament selection**: Randomly pick *k* individuals (tournament size, typically k=2 to 7), select the best. Larger *k* increases selection pressure. This is the most commonly used method in AEC tools — simple, efficient, no global fitness sorting required.

**Roulette wheel (fitness-proportionate) selection**: Selection probability proportional to fitness. Problem: premature convergence when one individual dominates.

**Rank-based selection**: Selection probability proportional to rank rather than raw fitness. Avoids scaling issues of roulette wheel.

**Stochastic universal sampling (SUS)**: Like roulette wheel but uses equally spaced pointers, reducing selection variance.

##### 2.1.3 Crossover (Recombination) Operators

Crossover combines genetic material from two parents to produce offspring:

**Single-point crossover**: Choose a random point; offspring gets genes from parent A before the point and parent B after.

**Two-point crossover**: Two random points; segment between points from one parent, rest from the other. Better gene block preservation.

**Uniform crossover**: Each gene independently chosen from either parent with equal probability. Maximum mixing — good when variables are independent.

**Simulated Binary Crossover (SBX)**: Standard for NSGA-II. Operates directly on real numbers. Distribution index eta_c (typically 2-20) controls offspring distance from parents. Higher eta_c = offspring closer to parents (exploitation); lower = larger jumps (exploration).

**Blend Crossover (BLX-alpha)**: Offspring sampled uniformly from [min(p1,p2) - alpha*d, max(p1,p2) + alpha*d]. Alpha=0.5 is typical.

##### 2.1.4 Mutation Operators

Mutation introduces random variation to maintain diversity:

**Bit-flip mutation**: For binary encoding. Each bit has probability 1/L of flipping.

**Gaussian mutation**: For real-valued encoding. Add N(0, sigma) noise to each gene. Most common mutation in AEC problems. Sigma can be fixed or adaptive.

**Polynomial mutation**: Used in NSGA-II. Distribution index eta_m (typically 20-100) controls perturbation magnitude. Higher eta_m = smaller perturbations.

**Swap / Scramble mutation**: For permutation encoding. Swap exchanges two positions; scramble randomly rearranges a subset.

**Adaptive mutation**: Rate or step size adjusts during the run — higher early (exploration), lower later (exploitation).

##### 2.1.5 Elitism

Elitism ensures the best individual(s) from the current generation survive unchanged into the next generation. Without elitism, the best solution found can be lost through crossover and mutation. Typically, the top 1-5% of the population is preserved. NSGA-II implements elitism through its combined parent+offspring selection scheme.

#### 2.2 Population Sizing

Population size determines the balance between solution diversity and computational cost:

- **Rule of thumb**: 50-200 individuals for most AEC problems
- **Small populations (20-50)**: Faster per generation but higher risk of premature convergence and loss of diversity. Acceptable for problems with few variables (<10) and smooth fitness landscapes
- **Medium populations (50-200)**: Standard range. Provides sufficient diversity for most problems with 10-50 variables
- **Large populations (200-1000)**: Necessary for highly multimodal landscapes, many-objective problems, or when each variable has a large range. Computationally expensive if evaluation is slow
- **Adaptive population sizing**: Start small, increase if diversity drops. Some frameworks support this

The critical trade-off: larger populations explore more of the design space per generation but require more evaluations per generation. If a single evaluation takes 30 seconds (e.g., energy simulation), a population of 200 requires nearly 2 hours per generation.

#### 2.3 Convergence Criteria

Optimization terminates when:

- **Generation limit**: Fixed number of generations (e.g., 50-500). Simple and predictable but may stop too early or waste time
- **Fitness plateau**: Average or best fitness has not improved by more than epsilon over the last N generations. Typical: epsilon = 0.1%, N = 10-20 generations
- **Diversity threshold**: Population diversity (measured by genotypic or phenotypic distance) drops below a minimum, indicating convergence
- **Computational budget**: Total evaluation count reaches a limit (e.g., 10,000 evaluations). Useful when evaluation cost is the binding constraint
- **Target fitness**: A satisfactory fitness value is reached. Rarely used in multi-objective optimization

#### 2.4 Exploration vs. Exploitation Balance

The fundamental tension in optimization:

- **Exploration**: Searching broadly across the design space for promising regions. Promoted by: large populations, high mutation rates, low selection pressure, diverse initialization
- **Exploitation**: Intensifying search near known good solutions. Promoted by: small populations, low mutation rates, high selection pressure, elitism

Effective optimization requires both. Early generations should favor exploration; later generations should favor exploitation. This can be achieved through:

- Adaptive operator rates (decreasing mutation rate over time)
- Island models (separate subpopulations with periodic migration)
- Restart strategies (re-initialize if stuck)
- Niching methods (fitness sharing, clearing) to maintain diverse subpopulations

#### 2.5 Schema Theorem and Building Blocks

Holland's Schema Theorem: short, low-order, above-average schemata (building blocks) receive exponentially increasing trials in subsequent generations. Implication for encoding: variables that interact strongly should be positioned near each other in the genotype to reduce disruption by crossover.

---

### 3. Multi-Objective Optimization

#### 3.1 Pareto Optimality

Most AEC design problems involve multiple conflicting objectives. A building cannot simultaneously minimize cost, minimize energy consumption, and maximize floor area — these objectives conflict. Multi-objective optimization acknowledges this and seeks the set of best trade-off solutions.

**Pareto dominance**: Solution A dominates solution B if A is at least as good as B in all objectives and strictly better in at least one. A solution that is not dominated by any other solution in the population is called **non-dominated** or **Pareto optimal**.

**Pareto front**: The set of all non-dominated solutions forms the Pareto front (or Pareto frontier) in objective space. This front represents the best achievable trade-offs — improving one objective requires worsening another.

#### 3.2 Pareto Front Visualization

For 2 objectives: a 2D scatter plot with each axis representing one objective. The Pareto front appears as a curve along the boundary of the feasible region.

For 3 objectives: a 3D scatter plot or parallel coordinate plot. The Pareto front is a surface.

For 4+ objectives: direct visualization is impossible. Use parallel coordinate plots, radar charts, heatmaps, or dimensionality reduction (PCA, t-SNE) to explore the solution set. Wallacei provides built-in multi-dimensional Pareto analytics.

#### 3.3 NSGA-II (Non-dominated Sorting Genetic Algorithm II)

NSGA-II (Deb et al., 2002) is the most widely used multi-objective evolutionary algorithm in AEC. It is the engine behind Wallacei and many other tools.

**Key mechanisms**:

1. **Non-dominated sorting**: The combined parent+offspring population is sorted into fronts. Front 1 contains all non-dominated solutions. Front 2 contains solutions dominated only by Front 1, and so on
2. **Crowding distance**: Within each front, solutions are ranked by crowding distance — a measure of how isolated a solution is in objective space. Solutions with larger crowding distances are preferred to maintain diversity along the Pareto front
3. **Selection**: Binary tournament selection using (front rank, crowding distance) as the comparison key. Lower front rank is better; within the same front, higher crowding distance is better
4. **Elitism**: The next generation is filled by taking solutions front-by-front from the combined population until the population size is reached. The last front that fits may be truncated using crowding distance

**Typical NSGA-II parameters for AEC**:
- Population size: 50-200
- Crossover: SBX with eta_c = 20, probability = 0.9
- Mutation: Polynomial with eta_m = 20, probability = 1/n (n = number of variables)
- Generations: 50-300

#### 3.4 SPEA2 (Strength Pareto Evolutionary Algorithm 2)

SPEA2 maintains an external archive of non-dominated solutions. Fitness based on domination strength and density (k-th nearest neighbor distance). Often produces better-distributed Pareto fronts than NSGA-II for many-objective problems. Available in Octopus for Grasshopper.

#### 3.5 MOEA/D (Multi-Objective Evolutionary Algorithm based on Decomposition)

Decomposes the multi-objective problem into single-objective subproblems using weight vectors. Each subproblem optimized simultaneously with information sharing between neighbors. Efficient for many-objective problems (4+) where NSGA-II's crowding distance becomes less effective.

#### 3.6 Trade-Off Analysis and Decision-Making

The Pareto front provides options, not answers. Decision-making methods:

- **Knee point selection**: Point of maximum curvature where marginal trade-offs are most balanced
- **Aspiration-based**: Define acceptable thresholds per objective, select solutions satisfying all
- **TOPSIS**: Rank by distance to ideal point and from anti-ideal point
- **Clustering**: Group similar Pareto-optimal solutions, select representatives. Wallacei provides K-means and agglomerative clustering
- **Designer preference**: Review phenotype geometry and select on qualitative judgment

#### 3.7 Weighted Sum vs. Epsilon-Constraint Methods

**Weighted sum**: F = w1*f1 + w2*f2 + ... + wn*fn. Simple but cannot find solutions on non-convex Pareto front regions. Galapagos uses this approach.

**Epsilon-constraint**: Optimize f1 subject to f2 <= epsilon_2, f3 <= epsilon_3. Can find non-convex Pareto front solutions. Requires choosing which objective to optimize and setting constraint bounds.

---

### 4. Fitness Function Design

#### 4.1 The Most Critical Step

The fitness function is the single most consequential decision in generative design. It encodes what the designer values. A poorly designed fitness function will efficiently produce solutions that are technically "optimal" but designically irrelevant. The fitness function is the designer's proxy — it must faithfully represent design intent.

#### 4.2 Common AEC Fitness Criteria

##### Structural Objectives
- **Total weight / material volume**: Minimize structural material usage (steel tonnage, concrete volume)
- **Maximum deflection**: Minimize peak deflection under service loads (L/360, L/240 limits)
- **Stress utilization ratio**: Minimize peak stress/capacity ratio across all members (target: 0.6-0.85 range)
- **Material efficiency**: Maximize load-carried-per-unit-material (structural efficiency index)
- **Natural frequency**: Maximize first natural frequency to avoid resonance (target: >3 Hz for floors)
- **Redundancy**: Maximize structural redundancy (number of alternative load paths)

##### Environmental Objectives
- **Annual daylight hours**: Maximize useful daylight illuminance (300-3000 lux) across floor area
- **Solar heat gain**: Minimize unwanted solar gain in cooling season; maximize in heating season
- **Energy use intensity (EUI)**: Minimize annual energy demand per unit floor area (kWh/m2/year)
- **View factor**: Maximize percentage of floor area with quality views to exterior
- **Daylight autonomy (DA)**: Maximize percentage of occupied hours when daylight exceeds 300 lux
- **Useful Daylight Illuminance (UDI)**: Maximize hours in 100-2000 lux range (avoid glare)
- **Embodied carbon**: Minimize total embodied CO2 of structural and envelope materials (kgCO2e)

##### Spatial Objectives
- **Area efficiency**: Maximize net-to-gross floor area ratio (usable area / total area)
- **Circulation ratio**: Minimize circulation area relative to total area (target: 15-25%)
- **Adjacency satisfaction**: Maximize satisfaction of programmatic adjacency requirements (percentage of required adjacencies achieved)
- **Daylight factor**: Maximize average daylight factor across occupied spaces (target: >2%)
- **Spatial connectivity**: Maximize/minimize integration values from space syntax analysis
- **Room proportion**: Minimize deviation from target aspect ratios (1:1 to 1:1.5 for offices)

##### Fabrication Objectives
- **Panel planarity**: Minimize maximum deviation of quad panels from planar (target: <panel-diagonal/500)
- **Unique element count**: Minimize number of unique panel types / structural members
- **Material waste**: Minimize cutting waste when nesting panels on stock sheets
- **Assembly complexity**: Minimize number of distinct connection types or assembly steps
- **Curvature variation**: Minimize rate of curvature change across surface (smoother = easier to build)

##### Cost Objectives
- **Material quantity**: Minimize total material volume/weight across all systems
- **Construction duration**: Minimize critical path length in construction schedule
- **Lifecycle cost**: Minimize 30-year total cost (construction + operation + maintenance + demolition)
- **Operational cost**: Minimize annual energy + maintenance + staffing costs

#### 4.3 Normalization Strategies

When combining multiple objectives, normalization is essential to prevent one objective from dominating due to scale differences:

**Min-max**: f_norm = (f - f_min) / (f_max - f_min). Maps to [0,1]. Requires estimating bounds.
**Z-score**: f_norm = (f - mean) / std_dev. Maps to ~[-3, 3]. Dynamic per generation.
**Target-based**: f_norm = |f - f_target| / f_target. For absolute performance targets.
**Rank-based**: Replace values with population rank. Eliminates scale differences but loses magnitude.

#### 4.4 Constraint Handling

Not all variable combinations produce valid designs. Constraint handling manages infeasible solutions:

**Penalty method**: F_penalized = F_original + penalty * violation_magnitude. Penalty coefficient must balance discouraging infeasibility without undervaluing near-boundary feasible solutions. Adaptive penalties that increase over generations are effective.

**Repair method**: Map infeasible solutions to nearest feasible solution (e.g., clip oversized rooms to maximum). Effective but requires domain-specific logic.

**Decoder method**: Genotype maps to feasible phenotypes via a decoder function. Feasibility guaranteed by construction. Example: floor plan decoder ensures rooms tile without overlaps.

**Feasibility rules (Deb's rules)**: Feasible beats infeasible; between infeasible, smaller violation wins; between feasible, better fitness wins. Used in NSGA-II.

**Multi-objective constraint handling**: Treat constraint satisfaction as an additional objective in Pareto ranking.

#### 4.5 Weighted Aggregation

For single-objective solvers (Galapagos): F_total = w1*f1_norm + w2*f2_norm + ... + wn*fn_norm where sum(wi) = 1.0. Start with equal weights, then adjust to reflect priorities. Warning: cannot discover solutions on non-convex Pareto front regions.

#### 4.6 Feasibility Thresholds

Hard boundaries: minimum room areas (code), maximum stress (safety), minimum daylight factor (LEED/BREEAM), maximum height (zoning), minimum setbacks (zoning), fire egress distances (life safety). These are constraints defining the feasible region, not objectives.

---

### 5. Design Space Exploration

#### 5.1 Parameter Space Definition

The design space is the set of all possible solutions defined by the design variables and their ranges. Each variable defines one dimension of the space. A problem with 20 variables defines a 20-dimensional space.

Variable types:
- **Continuous**: Position, dimension, angle (e.g., column spacing from 6.0m to 12.0m)
- **Discrete**: Count, selection (e.g., number of floors from 3 to 15)
- **Categorical**: Type choice (e.g., structural system: steel frame, concrete frame, timber)
- **Boolean**: On/off (e.g., include atrium: yes/no)

#### 5.2 Dimensionality and the Curse of Dimensionality

As the number of variables increases, the volume of the design space grows exponentially. A problem with 10 variables, each with 10 possible values, has 10^10 = 10 billion possible solutions. Exhaustive search is impossible.

Practical implications:
- **< 5 variables**: Grid search or full factorial DOE may be feasible
- **5-15 variables**: Evolutionary algorithms work well with moderate populations (50-100)
- **15-50 variables**: Larger populations (100-300) and more generations needed. Sensitivity analysis to identify and fix unimportant variables is valuable
- **50+ variables**: Decompose the problem, use surrogate models, or apply dimensionality reduction before optimization

#### 5.3 Sampling Strategies

Initial population generation affects convergence speed and solution quality:

**Random sampling**: Each variable sampled uniformly and independently. Simple but leaves gaps in high dimensions.

**Latin Hypercube Sampling (LHS)**: Each variable's range divided into N equal intervals with exactly one sample per interval. Standard for DOE in AEC. Better coverage than random sampling.

**Sobol sequences**: Quasi-random low-discrepancy sequences with superior space-filling properties. Available in Python (scipy.stats.qmc.Sobol).

**Orthogonal sampling**: Extension of LHS ensuring uniform distribution in multi-dimensional subspaces, not just marginal distributions.

#### 5.4 Sensitivity Analysis

Before full optimization, sensitivity analysis identifies which variables most influence the objectives, enabling dimensionality reduction:

**Morris method (Elementary Effects)**: Screening method computing mean and standard deviation of elementary effects per variable. Large mean = influential variable; large std = variable interacts with others. Cost: O(k*(n+1)) evaluations.

**Sobol indices**: Variance-based global sensitivity. First-order index S_i measures variance due to variable i alone. Total-order index ST_i includes all interactions involving i. Computationally expensive (thousands of evaluations); use surrogate models to reduce cost.

#### 5.5 Design of Experiments (DOE)

DOE provides structured approaches to sample the design space before or instead of optimization:

- **Full factorial**: All combinations of variable levels. Exponential cost, feasible for <5 variables
- **Fractional factorial**: Systematic subset, aliases some interactions but drastically reduces evaluations
- **Central composite design (CCD)**: Full factorial + axial + center points. For response surface models
- **Box-Behnken design**: Alternative to CCD with fewer points, excludes corner points
- **Optimal designs (D-optimal, I-optimal)**: Algorithmically selected points maximizing information per evaluation

#### 5.6 Surrogate Models

When fitness evaluation is expensive (minutes per evaluation for energy simulation or FEA), surrogate models approximate the fitness function with a cheap-to-evaluate mathematical model:

**Kriging (Gaussian Process Regression)**: Interpolates known points with uncertainty estimates, enabling intelligent sampling via expected improvement criterion. Gold standard for expensive optimization.

**Radial Basis Functions (RBF)**: Weighted sums of radial functions centered at known points. Faster than Kriging for large datasets. Used by Opossum (RBFOpt).

**Polynomial regression**: Low-order polynomials. Fast but limited to smooth, low-dimensional landscapes. Useful for initial screening.

**Neural networks**: Approximate complex, high-dimensional landscapes. Require hundreds to thousands of training points.

#### 5.7 Visualization Methods

**Parallel coordinate plots**: Each axis = one variable/objective; each solution = a polyline. Reveals correlations and preferred ranges. Wallacei provides interactive versions.
**Scatter matrix**: Grid of pairwise scatter plots revealing correlations and trade-offs.
**Heatmaps**: Fitness values across 2D variable slices. Identifies ridges, valleys, optima.
**t-SNE / UMAP**: Dimensionality reduction grouping similar solutions, revealing clusters.

---

### 6. Tools for Generative Design in AEC

#### 6.1 Tool Comparison Table

| Tool | Platform | Algorithm(s) | Objectives | Strengths | Limitations |
|---|---|---|---|---|---|
| **Galapagos** | Grasshopper | GA, Simulated Annealing | Single (weighted multi) | Built-in, simple UI, fast setup | No true multi-objective, limited analytics |
| **Wallacei** | Grasshopper | NSGA-II | Multi-objective | Pareto analytics, clustering, parallel coords, phenotype explorer | Learning curve, slower for large populations |
| **Octopus** | Grasshopper | HypE, SPEA2 | Multi-objective | Many-objective support, interactive Pareto | Less actively maintained, UI complexity |
| **Opossum** | Grasshopper | RBFOpt (surrogate) | Single/Multi | Efficient for expensive evaluations, fewer evaluations needed | Requires initial sampling, less exploratory |
| **Optimus** | Grasshopper | Multiple (GA, PSO, DE) | Single/Multi | Algorithm selection flexibility | Complexity, less community support |
| **Refinery** | Dynamo/Autodesk | GA (cloud-based) | Multi-objective | Cloud compute, Autodesk integration, no local compute limit | Requires Autodesk subscription, limited customization |
| **Autodesk Forma** | Web/Cloud | Performance-driven gen. | Multi-objective | Real-time feedback, wind/sun/energy, urban scale | Less flexible than scripted approaches, limited variable types |
| **Topos** | Standalone/Plugin | SIMP, BESO | Topology optimization | True topology optimization, structural focus | Structural only, requires FEA integration |

#### 6.2 Detailed Tool Notes

**Galapagos**: The entry point for most designers. Drag a fitness output and a set of sliders into the Galapagos component. It handles GA setup automatically. For multi-objective problems, manually combine objectives into a weighted sum. Best for: quick single-objective explorations, learning generative workflows, problems with <15 variables.

**Wallacei**: The professional standard for multi-objective generative design in Grasshopper. Provides NSGA-II with full Pareto front analytics including: generation-by-generation convergence tracking, objective value distributions, parallel coordinate filtering, K-means clustering of solutions, phenotype (geometry) preview for any solution. Wallacei X adds enhanced analytics. Best for: serious multi-objective AEC optimization, research, design competitions.

**Octopus**: Supports many-objective optimization (4+ objectives) better than Wallacei through HypE (Hypervolume-based) algorithm. Interactive Pareto front allows the designer to steer evolution in real time. Best for: many-objective problems, interactive exploration.

**Opossum**: Uses surrogate-based optimization (RBFOpt) to minimize the number of true evaluations. Instead of evaluating thousands of solutions, it builds a surrogate model from dozens of evaluations and optimizes the surrogate. Best for: problems where each evaluation takes minutes (energy simulation, CFD, detailed structural analysis).

**Refinery (Autodesk)**: Cloud-based generative design for Dynamo. Offloads computation to Autodesk servers. Provides multi-objective optimization with result visualization in a web interface. Best for: Revit/Dynamo users, teams without powerful local hardware.

**Autodesk Forma**: Cloud platform for early-stage urban and building design. Provides real-time performance feedback (wind, daylight, energy, noise) and generative exploration of massing options. Best for: urban-scale generative studies, early concept design, non-specialist users.

---

### 7. Generative Design Workflow

#### Step 1: Define Design Problem and Objectives

Clearly articulate what you are optimizing and why. Write out:
- The design context (building type, site, program)
- The performance objectives (what to minimize/maximize)
- The constraints (hard limits that must be satisfied)
- The evaluation criteria (how will you judge the results beyond fitness)

Example: "Optimize the floor plan layout of a 2,000 m2 office floor to maximize daylight autonomy, maximize programmatic adjacency satisfaction, and minimize circulation area, subject to minimum room sizes per the brief and maximum distance-to-exit per fire code."

#### Step 2: Identify Design Variables and Ranges

List every parameter the solver can manipulate. For each variable, specify:
- Name and description
- Type (continuous, discrete, categorical)
- Range (minimum, maximum, or list of options)
- Whether it interacts with other variables

Aim for 5-30 variables. Fewer than 5 may not need generative design; more than 30 may require decomposition or dimensionality reduction.

#### Step 3: Build Parametric Model

Construct the parametric model in Grasshopper, Dynamo, or a scripting environment. The model must:
- Accept all design variables as inputs
- Produce valid geometry for all variable combinations within ranges
- Be robust (no crashes or null geometry for edge cases)
- Run in reasonable time (seconds, not minutes, per evaluation — or use surrogates)

Model robustness is critical. If 10% of variable combinations crash the model, the solver wastes 10% of evaluations and may converge to regions that avoid crashes rather than regions with high fitness.

#### Step 4: Design Fitness Functions

Implement computable functions that evaluate each objective. Use simulation plugins (Ladybug/Honeybee for environmental, Karamba for structural, custom scripts for spatial) to compute performance metrics. Normalize all fitness values to comparable scales.

Test fitness functions manually with a few known configurations to verify they produce sensible values and rankings.

#### Step 5: Configure Solver

Select the solver based on the problem:
- Single objective: Galapagos
- Multi-objective (2-3 objectives): Wallacei (NSGA-II)
- Many-objective (4+ objectives): Octopus (HypE/SPEA2)
- Expensive evaluation: Opossum (RBFOpt)

Set parameters:
- Population size: start with 50, increase if diversity is insufficient
- Generations: start with 50, increase if convergence is not reached
- Crossover rate: 0.8-0.95 (SBX with eta_c = 15-20)
- Mutation rate: 1/n to 3/n where n is the number of variables

#### Step 6: Run Optimization

Launch the solver. Monitor:
- Best fitness per generation (should improve and plateau)
- Average fitness per generation (should improve, indicating population-wide learning)
- Diversity metrics (should decrease gradually, not crash)
- Computation time per generation (estimate total runtime)

For long runs (hours/days), save checkpoints. Most tools allow pausing and resuming.

#### Step 7: Analyze Results

For single-objective: examine the best solution and compare to the initial design.

For multi-objective:
- Visualize the Pareto front. Is it well-distributed? Are there gaps?
- Apply clustering to group similar solutions on the Pareto front
- Use parallel coordinates to identify common patterns among high-performing solutions
- Preview phenotypes (geometries) for diverse Pareto-optimal solutions
- Compute hypervolume indicator to measure Pareto front quality across runs

#### Step 8: Select and Refine Solutions

Choose 3-5 solutions from the Pareto front that represent distinct trade-off strategies. For each:
- Document objective values and how they compare to baseline
- Generate high-quality geometry for presentation
- Identify refinement opportunities not captured by the fitness function (aesthetics, constructability details, user experience)
- Iterate manually or run a focused local optimization around the selected solution

---

### 8. Case Study Examples

#### 8.1 Floor Plan Layout Optimization

**Problem**: Optimize the layout of 12 rooms on a 40m x 30m rectangular floor plate for an educational building.

**Variables (18 total)**:
- Room centroid positions: 12 rooms x (x, y) = 24 variables, reduced to 18 by fixing corridors and constraining room connectivity
- Room proportions: 12 aspect ratios (1.0 to 2.0)

**Objectives**:
1. Maximize adjacency satisfaction — percentage of required adjacencies (e.g., labs near prep rooms, offices near classrooms) achieved based on centroid distances
2. Maximize average daylight factor — computed via Radiance/Honeybee for each room based on window exposure
3. Minimize circulation area — area consumed by corridors and lobbies as a percentage of total

**Constraints**: Minimum room areas per educational standards. Maximum distance to nearest exit. No room overlaps (enforced by decoder).

**Solver**: Wallacei, NSGA-II, population 100, 80 generations = 8,000 evaluations.

**Results**: Pareto front with 45 non-dominated solutions. Three clusters emerge: (A) high-daylight layouts with rooms along perimeter, higher circulation; (B) compact layouts with minimal circulation but reduced daylight for interior rooms; (C) balanced layouts with light wells providing daylight to interior rooms. Cluster C reveals a design strategy (light wells) that was not initially considered — a generative discovery.

#### 8.2 Facade Shading System Optimization

**Problem**: Optimize a parametric louver shading system on a south-facing office facade (20m wide x 15m tall, Latitude 40N).

**Variables (8 total)**:
- Louver depth: 0.2m to 1.0m
- Louver spacing: 0.3m to 1.5m
- Louver tilt angle: 0 to 60 degrees
- Number of louver zones (horizontal divisions): 2 to 5
- Per-zone depth multiplier: 0.5 to 1.5 (2-5 variables depending on zone count)

**Objectives**:
1. Minimize annual cooling load contribution from solar gain (kWh/m2/yr) — computed via EnergyPlus/Honeybee
2. Maximize annual average useful daylight illuminance at desk level (% floor area >300 lux)
3. Minimize material cost — proportional to total louver surface area (cost/m2 of aluminum louver)

**Solver**: Wallacei, NSGA-II, population 80, 60 generations. Each evaluation requires a Radiance simulation (~10 seconds) and an EnergyPlus simulation (~30 seconds). Total runtime: approximately 27 hours.

**Results**: Pareto front reveals that deeper louvers dramatically reduce cooling load but at diminishing returns beyond 0.6m depth. View and daylight preservation is best achieved with variable-depth zoning — deeper louvers at eye level and shallower louvers above. The cost-optimal region suggests 0.45m depth at 0.6m spacing as the knee point of the cost-performance trade-off.

#### 8.3 Structural Form-Finding Optimization

**Problem**: Optimize the shape of a long-span roof shell (50m x 50m footprint) for a sports hall.

**Variables (12 total)**:
- Control point heights for a 4x4 NURBS surface: 16 control points, of which 4 corners are fixed and edge midpoints are symmetric, yielding 12 free variables
- Height range: 3m to 20m per control point

**Objectives**:
1. Minimize total structural weight (steel shell + supporting structure) — computed via Karamba3D finite element analysis
2. Minimize maximum deflection under dead + live load combination
3. Maintain minimum interior clearance of 8m (constraint, handled via penalty)

**Solver**: Octopus (HypE), population 120, 100 generations. Each evaluation requires a Karamba3D analysis (~2 seconds). Total runtime: approximately 6.5 hours.

**Results**: The Pareto front shows a clear trade-off between weight and deflection. Minimum-weight solutions tend toward anticlastic (saddle-shaped) surfaces that carry load efficiently through membrane action but have higher deflections. Minimum-deflection solutions tend toward synclastic (dome-like) shapes that are stiffer but heavier. The knee point reveals a hybrid form — a shallow dome with edge curvature — that achieves 85% of the minimum weight at only 120% of the minimum deflection. This form was not intuitively predictable.

---

### 9. Advanced Topics

#### 9.1 Interactive Evolutionary Computation (IEC)

In IEC, the human designer serves as the fitness function for some or all objectives. Each generation, the designer views rendered phenotypes and selects preferred solutions. Evolution is guided by aesthetic, experiential, or cultural criteria that resist quantification.

Challenges: human fatigue limits populations to 10-20 individuals and runs to 20-30 generations. Solutions: pre-filter with computational fitness to reduce the set the human must evaluate; use surrogate models trained on human selections to automate subsequent generations.

#### 9.2 Co-Evolution

Multiple populations evolve simultaneously, with fitness depending on interactions between populations. Applications in AEC:
- **Structure-envelope co-evolution**: The structural system and the facade system evolve in separate populations, with fitness evaluated on the combined design
- **Building-landscape co-evolution**: Building massing and site design evolve together
- **Supply-demand co-evolution**: Space layouts and circulation networks evolve interdependently

Co-evolution can discover emergent synergies between subsystems that would be missed by optimizing them sequentially.

#### 9.3 Novelty Search

Instead of optimizing fitness, novelty search rewards solutions that are *different* from all previously found solutions. The archive of encountered solutions grows over time, and fitness is defined as the distance from the nearest archived solution in behavior space.

Application: when the fitness landscape is deceptive (local optima trap conventional optimization), novelty search explores more broadly and often finds globally optimal solutions as a side effect. In AEC: generating diverse facade patterns, exploring unusual structural topologies, or discovering non-obvious spatial configurations.

#### 9.4 MAP-Elites (Quality-Diversity)

MAP-Elites divides the design space into a grid of behavioral niches (defined by user-chosen feature dimensions) and seeks the highest-performing solution in each niche. The result is a map of the design space showing the best achievable fitness for every combination of behavioral features.

Example: for a tower design, the feature dimensions might be (building height, floor plate aspect ratio). MAP-Elites fills a 2D grid where each cell contains the best-performing tower with that height and aspect ratio. The designer can browse the map to understand how performance varies across the design space, not just at the optimum.

#### 9.5 Neuroevolution

Using evolutionary algorithms to optimize neural network architectures and weights. Applications in AEC:
- Evolving neural network controllers for adaptive building systems (lighting, HVAC)
- Evolving generative neural networks (GANs, VAEs) that produce building geometries
- Evolving surrogate models that predict simulation outcomes

#### 9.6 Transfer Learning Between Design Problems

Knowledge from one optimization can bootstrap another. If a floor plan optimization for Building A converges on effective layout strategies, the final population can seed the initial population for Building B's optimization (with modified constraints). This reduces convergence time and improves solution quality for repeated problem types (e.g., a firm designing many office buildings with similar programs).

Strategies:
- **Population seeding**: Use solutions from a previous run as part of the initial population
- **Surrogate transfer**: Train a surrogate model on evaluations from previous runs and use it to guide the new optimization
- **Operator transfer**: Learn effective crossover/mutation distributions from previous runs and apply them to the new problem

---

### Quick Reference: Generative Design Decision Tree

```
Is the problem single-objective?
  YES -> Is evaluation fast (<1 sec)?
           YES -> Galapagos (GA or SA)
           NO  -> Opossum (surrogate-based)
  NO  -> How many objectives?
           2-3 -> Wallacei (NSGA-II)
           4+  -> Octopus (HypE/SPEA2)
         Is evaluation fast (<1 sec)?
           YES -> Direct evaluation
           NO  -> Surrogate-assisted (Opossum or custom Kriging)
         Are qualitative criteria important?
           YES -> Human-in-the-loop (IEC) or hybrid
           NO  -> Fully automated
```

### Common Pitfalls

1. **Fitness function does not reflect design intent**: The optimizer finds solutions that score well but are designically poor. Solution: iterate on fitness functions with manual spot-checks.
2. **Premature convergence**: Population loses diversity before finding the global optimum. Solution: increase population, add diversity maintenance, check for dominant genes.
3. **Unstable parametric model**: Many evaluations crash or produce invalid geometry. Solution: add robust error handling, constrain variables more tightly, use decoder approaches.
4. **Overfitting to the fitness function**: Solutions exploit weaknesses in the evaluation method. Solution: validate top solutions with independent analysis tools.
5. **Ignoring qualitative criteria**: Generative design optimizes what you measure. If you do not measure aesthetics, the optimizer ignores aesthetics. Solution: human-in-the-loop, post-optimization curation.
6. **Insufficient generations**: Optimization stops before convergence. Solution: monitor convergence metrics, increase generation count.
7. **Too many variables**: Curse of dimensionality prevents effective search. Solution: sensitivity analysis to fix unimportant variables, decompose the problem.


## design-automation

### Design Automation

> Rule-based design systems, constraint satisfaction, space planning algorithms, automated layout generation, drawing automation, code compliance checking, and computational workflows for AEC design automation

## Design Automation for AEC

Design automation is the disciplined application of computational logic to replace, accelerate, or augment repetitive and rule-governed design tasks across architecture, engineering, and construction. This skill covers the full spectrum from simple parametric rules through constraint-satisfaction engines to fully generative layout systems, drawing automation pipelines, and automated code-compliance verification.

---

### 1. Design Automation Spectrum

#### 1.1 Levels of Automation in AEC

Design automation exists on a continuum. Understanding where a task falls on this spectrum determines the appropriate technology and the degree of human oversight required.

| Level | Label | Description | Example |
|-------|-------|-------------|---------|
| 0 | Manual | Designer makes every decision, draws every line | Hand-drafted floor plans |
| 1 | Parametric | Geometry driven by explicit parameters; designer controls inputs | Grasshopper slider controlling facade panel width |
| 2 | Rule-Based | IF-THEN logic encodes design knowledge; system applies rules automatically | Auto-sizing exit widths based on occupant load |
| 3 | Constraint-Based | System searches solution space satisfying stated constraints | CSP solver placing rooms to satisfy adjacency + area constraints |
| 4 | Generative | System produces many candidate designs autonomously; human selects | GA-based floor plan generator producing 500 layout options |
| 5 | AI-Assisted | Machine-learned models propose designs or predict performance | GAN generating floor plan from adjacency graph |
| 6 | Autonomous | Fully closed-loop: sense conditions, generate design, validate, output | Automated site grading from survey to construction docs (emerging) |

#### 1.2 What Can vs. Should Be Automated

**High automation potential:**
- Code compliance checking (deterministic rules)
- Structural member sizing (engineering formulas)
- Parking layout optimization (geometric + count)
- Sheet creation and annotation (repetitive)
- Clash detection (spatial intersection)
- Area and quantity takeoffs (data extraction)

**Medium automation potential:**
- Space planning and room layout (heuristic + constraint)
- Facade design (performance + aesthetic rules)
- MEP routing (complex constraints, many valid solutions)
- Site grading (optimization with soft constraints)

**Low automation potential (human judgment critical):**
- Architectural concept design (cultural, contextual)
- Urban massing and placemaking (experiential quality)
- Material palette selection (aesthetic, tactile)
- Client presentation and persuasion (social)

#### 1.3 Human-in-the-Loop Design Automation

The most effective AEC automation systems keep designers in the loop at critical decision points:

1. **Define** — Human sets objectives, constraints, preferences
2. **Generate** — System produces candidate solutions
3. **Evaluate** — System scores and ranks; human reviews
4. **Select** — Human chooses preferred direction
5. **Refine** — System develops selected option further
6. **Validate** — Automated compliance checking; human sign-off

This cycle can repeat at multiple scales: master plan level, building level, floor level, room level.

#### 1.4 The Role of Design Rules and Heuristics

Design rules encode domain expertise in computable form:

- **Hard rules**: Must be satisfied (building code, structural limits). Violation = invalid design.
- **Soft rules**: Should be satisfied (rules of thumb, best practices). Violation = penalty score.
- **Heuristics**: Rules of thumb that usually produce good results but are not guaranteed optimal. Examples:
  - Office floor plate depth should not exceed 15m from core to window
  - Residential corridor length should not exceed 30m without a window
  - Parking bay angle of 90 degrees maximizes density; 60 degrees improves maneuverability
  - Structure grid spacing of 7.5-9.0m suits most office programs

---

### 2. Rule-Based Design Systems

#### 2.1 Production Rules (IF-THEN)

The simplest and most widely used automation pattern in AEC:

```
IF occupant_load > 500
THEN required_exits >= 3
     AND exit_width_total >= occupant_load * 5.0mm

IF room_type == "bathroom" AND floor_area < 4.0
THEN min_dimension >= 1.5m
     AND door_swing == "outward"

IF building_height > 23m
THEN fire_resistance_rating >= 120min
     AND sprinkler_system == required
```

Production rules are stored in a rule base and executed by a rule engine that:
1. Matches rules against current facts (pattern matching)
2. Resolves conflicts when multiple rules fire (conflict resolution)
3. Executes the winning rule's action (assertion or modification)
4. Repeats until no more rules fire (quiescence)

#### 2.2 Decision Trees

Hierarchical rule structures where each node tests a condition and branches lead to sub-decisions:

```
Building Classification Decision Tree:
├── Occupancy > 300?
│   ├── YES → Assembly (A)
│   │   ├── Fixed seating? → A-1
│   │   ├── No fixed seating? → A-2
│   │   └── Worship? → A-3
│   └── NO → Business (B)
│       ├── Office? → B
│       └── Educational? → E
│           ├── Students > 12 yrs? → E
│           └── Students ≤ 12 yrs? → E (daycare)
```

Decision trees are valuable because they are transparent, auditable, and can be validated against code text.

#### 2.3 Rule Engines

Production rule engines for AEC applications:

- **Forward chaining**: Start from known facts, derive conclusions. Used for compliance checking. "Given this building, what rules are violated?"
- **Backward chaining**: Start from goal, find supporting facts. Used for design guidance. "What do I need to achieve fire compliance?"
- **Rete algorithm**: Efficient pattern matching for large rule sets. Maintains a network of partial matches; only re-evaluates affected rules when facts change.

Implementation options:
- Python: `durable-rules`, `business-rules`, custom engines
- Java/Kotlin: Drools (most mature open-source rule engine)
- .NET: NRules (for Revit add-in integration)
- Grasshopper: Conditional components, custom C# script nodes

#### 2.4 Shape Grammars (Stiny)

Shape grammars define a set of shape rules that transform geometric configurations. Formally:

```
SG = (S, L, R, I)
where:
  S = finite set of shapes
  L = finite set of labels (markers, reference points)
  R = finite set of shape rules: α → β (replace shape α with shape β)
  I = initial shape
```

Shape grammar applications in AEC:
- **Palladian villa grammar** (Stiny & Mitchell, 1978): Generates villa plans following Palladio's compositional logic
- **Prairie house grammar** (Koning & Eizenberg, 1981): Encodes Frank Lloyd Wright's Prairie style
- **Musgum grammar**: Encodes traditional Musgum shell house typology
- **Islamic geometric pattern grammars**: Tile-based generation of complex ornamental patterns
- **Facade grammar**: Generates facade variations from a vocabulary of elements (window, panel, mullion, spandrel)

#### 2.5 Graph Grammars

Extend shape grammars to operate on graph structures (nodes + edges) rather than geometric shapes:

- Nodes represent rooms, spaces, or building elements
- Edges represent adjacency, access, containment, or structural relationships
- Rules transform subgraphs: match a pattern, replace with a new pattern

Graph grammars are powerful for:
- Floor plan generation from room adjacency programs
- Building massing from spatial relationship diagrams
- Urban block subdivision from land-use programs

#### 2.6 Rule Priority and Conflict Resolution

When multiple rules apply simultaneously, conflict resolution strategies include:

1. **Priority ordering**: Each rule has a numeric priority; highest fires first
2. **Specificity**: More specific rules override general rules (e.g., local code overrides IBC)
3. **Recency**: Rules matching recently modified facts fire first
4. **Refraction**: A rule does not fire twice on the same set of facts
5. **Jurisdictional hierarchy**: Federal > State > Local > Project-specific

#### 2.7 Rule Libraries for AEC

| Domain | Rule Source | Key Rules |
|--------|-----------|-----------|
| Egress | IBC Chapter 10 | Occupant load factors, exit width, travel distance, common path |
| Fire safety | IBC Chapter 7 | Fire resistance ratings, compartment sizes, opening protection |
| Accessibility | ADA/ABA, EN 17210 | Clear widths, ramp grades, turning radii, reach ranges |
| Structural | ASCE 7, Eurocode | Load combinations, deflection limits, drift limits |
| Zoning | Local zoning code | Setbacks, height, FAR, lot coverage, parking ratios |
| Energy | ASHRAE 90.1, IECC | Envelope U-values, WWR limits, HVAC efficiency |
| Plumbing | IPC | Fixture counts by occupancy, pipe sizing |

---

### 3. Constraint Satisfaction Problems (CSP)

#### 3.1 CSP Formalism

A CSP is defined by the triple (X, D, C):

- **X** = {X1, X2, ..., Xn}: set of variables
- **D** = {D1, D2, ..., Dn}: set of domains (possible values for each variable)
- **C** = {C1, C2, ..., Cm}: set of constraints (relations restricting variable assignments)

A **solution** is an assignment of values to all variables such that every constraint is satisfied.

#### 3.2 CSP for Floor Plan Layout

Formulating floor plan layout as a CSP:

**Variables**: Room positions and dimensions
- X_i = (x_i, y_i, w_i, h_i) for each room i

**Domains**:
- Position: within building boundary
- Width/height: within acceptable range for room type

**Constraints**:
- **Non-overlap**: No two rooms share interior area
- **Boundary containment**: All rooms within building envelope
- **Adjacency**: Specified room pairs must share a wall segment of minimum length (door width)
- **Non-adjacency**: Certain rooms must not be adjacent (e.g., bedroom not adjacent to mechanical)
- **Area**: Room area within specified range (e.g., living room 20-35 m2)
- **Aspect ratio**: Room width-to-depth ratio within range (e.g., 1:1 to 1:2)
- **Window access**: Rooms requiring daylight must touch an exterior wall
- **Structural grid alignment**: Room boundaries align with structural grid lines

#### 3.3 Arc Consistency

Arc consistency (AC-3) prunes variable domains before search begins:

For every pair of constrained variables (Xi, Xj), remove values from Di that have no supporting value in Dj. Repeat until no more pruning occurs.

This dramatically reduces the search space. For AEC problems with continuous domains, discretize positions to a grid (e.g., 300mm module) to make the domain finite.

#### 3.4 Backtracking Search

The standard algorithm for solving CSPs:

```
function BACKTRACK(assignment, csp):
    if assignment is complete: return assignment
    var = SELECT-UNASSIGNED-VARIABLE(csp)
    for value in ORDER-DOMAIN-VALUES(var, assignment, csp):
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences = INFERENCE(csp, var, value)
            if inferences != failure:
                add inferences to assignment
                result = BACKTRACK(assignment, csp)
                if result != failure: return result
            remove inferences and {var = value}
    return failure
```

Key heuristics for AEC CSPs:
- **MRV (Minimum Remaining Values)**: Assign the room with fewest valid placements first (fail-early)
- **Degree heuristic**: Assign the room with most adjacency constraints first
- **Least Constraining Value**: Try placements that leave the most options for unassigned rooms

#### 3.5 Constraint Propagation

Beyond arc consistency, stronger propagation techniques:
- **Path consistency**: Ensures consistency for triples of variables
- **MAC (Maintaining Arc Consistency)**: Run AC-3 after each assignment
- **Forward checking**: Remove inconsistent values from neighbors of just-assigned variable

#### 3.6 Soft vs. Hard Constraints

In real AEC problems, not all constraints are absolute:

**Hard constraints** (must satisfy):
- Building code requirements
- Structural limits
- Site boundary
- Non-overlap of rooms

**Soft constraints** (prefer to satisfy, with penalty for violation):
- Preferred adjacency (e.g., kitchen near dining)
- View orientation (e.g., living room faces south)
- Preferred aspect ratio
- Acoustic separation preferences

Soft constraints are handled by:
1. **Weighted CSP**: Each soft constraint has a weight; minimize total penalty
2. **Optimization over feasible set**: Find all hard-constraint-satisfying solutions, then rank by soft constraint satisfaction
3. **Pareto frontier**: When soft constraints conflict, find non-dominated solutions

#### 3.7 CSP for Structural Grid

Variables: Grid line positions along X and Y axes
Domains: Continuous within building boundary, discretized to module (e.g., 100mm)
Constraints:
- Minimum span: 5.0m (functional space between columns)
- Maximum span: 12.0m (without transfer structures for typical concrete)
- Column-free zones: No columns in specified areas (auditorium, lobby)
- Edge alignment: Grid aligns with building perimeter
- Core alignment: Grid lines pass through core walls
- Regularity: Prefer uniform bay sizes (soft constraint)

---

### 4. Space Planning Algorithms

#### 4.1 Adjacency-Based Layout

The classic space planning approach:

1. **Adjacency matrix**: Define required and desired adjacencies between rooms

```
         LIV  DIN  KIT  BED1 BED2 BATH ENT
Living    -    2    1    0    0    0    2
Dining    2    -    2    0    0    0    0
Kitchen   1    2    -    0    0    0    0
Bed 1     0    0    0    -    0    2    0
Bed 2     0    0    0    0    -    1    0
Bath      0    0    0    2    1    -    0
Entry     2    0    0    0    0    0    -

(0 = no relation, 1 = preferred, 2 = required)
```

2. **Bubble diagram generation**: Place rooms as circles/rectangles; connect required adjacencies with springs; use force-directed layout to minimize spring energy

3. **Graph-based placement**: Represent adjacency as a planar graph; find a planar embedding; assign rooms to faces of the graph

#### 4.2 Grid-Based Placement

Discretize the floor plate into a grid and assign rooms to grid cells:

- **Grid resolution**: Typically 300mm, 600mm, or 1200mm module
- **Bin packing**: Treat rooms as rectangles, floor plate as a bin; use heuristics (bottom-left, best-fit, shelf algorithms)
- **Integer programming**: Assign binary variables x_{i,j,k} = 1 if room i occupies grid cell (j,k); add constraints for contiguity, adjacency, area
- **Advantages**: Naturally handles structural grid alignment
- **Disadvantages**: Grid resolution limits design freedom; large grids = many variables

#### 4.3 Force-Directed Layout

Model rooms as particles in a physics simulation:

- **Attractive forces**: Between rooms that should be adjacent (spring force, F = k * delta)
- **Repulsive forces**: Between all room pairs to prevent overlap (Coulomb-like, F = q / r^2)
- **Boundary forces**: Repel rooms from floor plate boundary (containment)
- **Gravity**: Pull rooms toward building center (compactness)
- **Damping**: Reduce velocity each step to reach equilibrium (damping factor 0.8-0.95)

Algorithm:
```
1. Initialize room positions randomly within boundary
2. For each timestep:
   a. Calculate all forces on each room
   b. Update velocities: v += F * dt / mass
   c. Apply damping: v *= damping_factor
   d. Update positions: p += v * dt
   e. Resolve overlaps (push apart along shortest separating axis)
   f. Enforce boundary containment
3. Stop when total kinetic energy < threshold
```

Force-directed layout produces organic, relationship-driven arrangements but rarely produces rectangular room boundaries without post-processing.

#### 4.4 Evolutionary Layout (GA-Based Floor Plan Generation)

Genetic algorithm approach:

**Genome encoding**:
- Sequence of room placements: [(room_id, x, y, w, h, rotation), ...]
- Or: slicing floorplan tree (horizontal/vertical cuts + room assignment)
- Or: adjacency graph + relative positioning flags (left-of, above, ...)

**Fitness function** (multi-objective):
- Adjacency satisfaction score (weighted)
- Area utilization (minimize wasted space)
- Aspect ratio quality (penalize extreme ratios)
- Circulation efficiency (total corridor area)
- Daylight access (perimeter contact for daylight-required rooms)
- Code compliance (exit distance, egress width)

**Operators**:
- **Selection**: Tournament selection (size 3-5)
- **Crossover**: Swap room subtrees between two parent slicing trees; or swap room positions
- **Mutation**: Shift room position, resize room, swap two rooms, change cut direction
- **Repair**: Fix overlaps, enforce boundary, adjust areas to program

**Parameters**:
- Population: 200-1000
- Generations: 500-5000
- Crossover rate: 0.7-0.9
- Mutation rate: 0.05-0.20
- Elitism: preserve top 5-10%

#### 4.5 Recursive Subdivision

Top-down partitioning of a floor plate:

**BSP-Tree (Binary Space Partitioning)**:
1. Start with the entire floor plate as a single region
2. Choose a cutting line (horizontal or vertical)
3. Split the region into two sub-regions
4. Assign rooms to sub-regions based on program
5. Recursively subdivide each sub-region
6. Stop when each region contains exactly one room

**K-D Tree variant**: Alternate between horizontal and vertical cuts at each level.

**Squarified treemap**: Choose cut direction and position to minimize aspect ratio deviation from 1:1. Produces compact, well-proportioned rooms.

Decision: Where to cut?
- Proportional to area: Cut position based on area ratio of rooms assigned to each side
- Adjacency-driven: Keep adjacent rooms on the same side of the cut
- Structural grid-aligned: Snap cuts to structural grid lines

#### 4.6 Stacking Algorithms (Multi-Story)

For multi-story buildings, stacking determines which rooms/units go on which floors:

1. **Core alignment**: Vertical circulation (stairs, elevators) must align across all floors
2. **Structural continuity**: Load-bearing walls and columns must stack vertically
3. **Program zoning**: Public/commercial on lower floors, private/residential above
4. **MEP continuity**: Wet rooms (kitchens, bathrooms) should stack for efficient plumbing risers
5. **Unit type assignment**: Assign unit types to floor plates considering:
   - Typical floor repetition (efficiency)
   - Setback floors (larger/different units)
   - Ground floor special conditions (retail, lobby)
   - Penthouse floor special conditions

#### 4.7 Corridor and Circulation Routing

After rooms are placed, corridors must connect them:

- **Shortest path**: A* or Dijkstra on grid graph connecting room doors to building exits
- **Minimum spanning tree**: Connect all rooms with minimum total corridor length
- **Dead-end elimination**: Ensure corridors form loops or connect to multiple exits
- **Width compliance**: Corridors must meet minimum width (typically 1200mm residential, 1500mm commercial, 2400mm hospital)
- **Travel distance**: Maximum travel distance from any point to an exit (IBC: 60m sprinklered, 45m unsprinklered for most occupancies)

#### 4.8 Room Sizing Rules by Program Type

| Room Type | Area Range (m2) | Min Dimension | Notes |
|-----------|----------------|---------------|-------|
| Studio apartment | 28-40 | 3.6m | Combined living/sleeping |
| 1-bed apartment | 45-65 | - | Separate bedroom |
| 2-bed apartment | 65-90 | - | - |
| 3-bed apartment | 85-120 | - | - |
| Living room | 18-35 | 3.3m | Daylight required |
| Master bedroom | 12-20 | 3.0m | Daylight, closet |
| Secondary bedroom | 9-14 | 2.7m | Daylight, closet |
| Kitchen | 7-15 | 2.4m | Ventilation required |
| Bathroom | 3.5-8 | 1.5m | Wet area |
| Powder room | 1.5-3 | 0.9m width | No shower/tub |
| Office (private) | 9-15 | 2.7m | Daylight preferred |
| Office (open plan) | 6-10 per person | - | 8-12m max depth from window |
| Meeting room (small) | 12-20 | 3.0m | 4-8 persons |
| Meeting room (large) | 30-60 | 5.0m | 12-20 persons |
| Hotel guest room | 22-35 | 3.6m | Standard; 40-65 for suite |
| Hospital patient room | 14-22 (single) | 3.6m | With en-suite |
| Classroom | 50-75 | 6.0m | 25-30 students |
| Restaurant dining | 1.2-1.8 per seat | - | Varies by service style |
| Retail | varies | 6.0m frontage min | Varies widely |

---

### 5. Automated Layout Generation

#### 5.1 Residential Unit Layout Generation

Automated residential layout follows a hierarchical process:

1. **Unit boundary definition**: From structural grid and building envelope
2. **Zone identification**: Public zone (living, dining, kitchen), private zone (bedrooms, bathrooms), service zone (laundry, storage), circulation (entry, corridors)
3. **Room placement priority order**:
   - Entry (fixed by corridor access point)
   - Kitchen (plumbing riser location)
   - Bathrooms (plumbing riser location)
   - Living room (largest contiguous window wall)
   - Bedrooms (remaining window walls)
   - Storage/utility (interior, no window needed)
4. **Circulation routing**: Entry to all rooms with minimum corridor
5. **Window assignment**: Each habitable room gets exterior wall contact
6. **Validation**: Check minimum areas, dimensions, ventilation, egress

Key constraints:
- Every habitable room must have natural light (window access)
- Kitchen requires exhaust ventilation path
- Bathroom requires mechanical or natural ventilation
- Entry should not open directly into bedroom
- No room should be a pass-through (except living to dining)

#### 5.2 Office Floor Plate Optimization

Office layout automation considers:

- **Core-to-window depth**: 8-12m for open plan, 6-8m for cellular offices
- **Core placement**: Central core maximizes usable perimeter; side core maximizes contiguous floor area
- **Planning grid**: 1.35m or 1.50m module (furniture coordination)
- **Cellular office sizing**: 1-module (2.7m) small, 2-module (4.05m) standard, 3-module (5.4m) large
- **Open plan zones**: 6-8 workstations per cluster, team neighborhoods
- **Support spaces**: Meeting rooms at core adjacency, break rooms at perimeter
- **Circulation**: Primary corridor (1.8m), secondary aisles (1.2m)
- **Efficiency target**: 80-85% net-to-gross ratio

#### 5.3 Hospital Department Layout

Hospital layout automation is among the most constrained:

- **Clinical adjacencies**: ED adjacent to imaging and lab; OR suite adjacent to ICU; CSSD below OR suite
- **Clean/dirty flows**: Separate clean and dirty corridors in surgical suites; soiled utility rooms with pass-through
- **Patient flow**: Intake → triage → treatment → discharge (linear, no backtracking)
- **Staff flow**: Separate from patient and visitor flows
- **Infection control zones**: Negative pressure rooms, anteroom airlocks
- **Department sizing**: By bed count, procedure volume, and throughput models
- **Wayfinding**: Clear circulation hierarchy; minimize decision points

#### 5.4 Hotel Floor Plate

Hotel floor plate automation:

- **Room arrangement**: Double-loaded corridor (rooms on both sides) is most efficient
- **Room width**: Structural bay width (typically 3.6-4.2m standard, 7.2-8.4m for suite)
- **Room depth**: 6.0-8.0m for standard rooms
- **Service core placement**: Centralized or dual cores; housekeeping rooms per floor
- **Corner rooms**: Premium rooms, typically suites, require special planning
- **Corridor length**: Maximum ~60m between elevator lobby and last room (guest experience)
- **Back-of-house**: Service elevator, linen chute, housekeeping station, trash room

#### 5.5 Parking Layout Optimization

Parking is highly amenable to automation:

- **Bay angle options**: 90 degrees (most dense), 60 degrees (easier maneuver), 45 degrees (one-way aisles), 0 degrees (parallel, least dense)
- **Stall dimensions**: 2.4m x 5.4m standard, 2.6m x 5.4m accessible
- **Aisle width**: 7.2m for 90-degree two-way, 5.5m for 60-degree one-way, 3.6m for parallel
- **Ramp placement**: Typically at perimeter; 12% max slope, 6% transition at top/bottom; 3.6m clear width per lane
- **Optimization objective**: Maximize stall count within site boundary
- **Algorithm**: Grid search over bay angle and aisle direction; evaluate count for each configuration
- **Structural grid**: 5.0m x 5.0m bays typical for parking; 8.1m x 5.0m for column-free spans
- **Accessible stalls**: 1 per 25 stalls minimum; van-accessible 1 per 6 accessible

#### 5.6 Classroom/School Layout

School layout automation:

- **Classroom clusters**: Groups of 4-6 classrooms sharing a breakout space
- **Adjacency**: Classrooms near related labs; art/music with acoustic separation
- **Outdoor access**: Ground-floor classrooms with direct outdoor access (primary school)
- **Acoustic separation**: Music rooms and gymnasia separated from quiet classrooms (STC 55+ walls)
- **Supervision lines**: Staff offices with sightlines to corridors and play areas
- **Safe access**: Single controlled entry point; perimeter security
- **Hall/gymnasium**: Central location accessible from all classroom wings

---

### 6. Drawing Automation

#### 6.1 Automated Floor Plan Generation from Spatial Data

Given a spatial model (rooms with geometry), automated floor plan production:

1. **Wall line generation**: Extract room boundaries, merge shared walls, assign wall types (exterior, interior, fire-rated)
2. **Door and window placement**: From openings in spatial model; apply standard sizes
3. **Fixture placement**: Bathroom fixtures, kitchen counters by room type templates
4. **Hatch/fill patterns**: Apply by material (concrete, tile, carpet) or by room type
5. **Line weight assignment**: By element type (heavy for cut walls, medium for furniture, light for ceiling grid)
6. **Annotation layer**: Room names, numbers, areas, door/window tags

#### 6.2 Section and Elevation Generation

Automated sections and elevations:

- **Section cut placement**: At key locations (through stairs, through atrium, through typical bay)
- **Depth limiting**: Clip section depth to show relevant information only
- **Material hatching**: Auto-apply section hatches by material
- **Annotation**: Floor-to-floor heights, slab thicknesses, structural member sizes
- **Elevation generation**: Project facade elements; apply material annotations; dimension window/door openings

#### 6.3 Detail Library Management and Auto-Placement

- **Standard detail library**: Organized by CSI division (02-Sitework, 03-Concrete, 04-Masonry, etc.)
- **Detail keying**: Each detail has a unique key (type + condition + material)
- **Auto-placement**: System identifies conditions in the model (e.g., wall-to-slab junction) and places the appropriate standard detail
- **Detail adaptation**: Parametric details adjust dimensions to match model conditions
- **Version control**: Detail library versioned; updates propagate to all projects

#### 6.4 Annotation Automation

- **Dimension strings**: Auto-dimension structural grids, wall-to-wall, opening positions
- **Room tags**: Auto-place with room name, number, area, finish floor elevation
- **Door/window tags**: Auto-tag with mark number, type, size
- **Keynoting**: Auto-keynote materials by element type; generate keynote legend
- **Leader and callout placement**: Avoid overlaps using collision detection; route leaders to clear space
- **Coordination**: Ensure annotation does not overlap with drawing content

#### 6.5 Sheet Layout Optimization

- **View-to-sheet assignment**: Assign views to sheets based on drawing set organization (plans on A-series, sections on A-series, details on A-series sub-sheets)
- **View placement**: Optimize view positions on sheets to minimize white space
- **Title block**: Auto-populate project info, sheet number, revision history
- **Sheet numbering**: Follow standard conventions (A1.01, A2.01, S1.01, etc.)
- **Cross-referencing**: Auto-update section markers, detail callouts, drawing references

#### 6.6 Export Automation

- **Batch PDF export**: Export all sheets to PDF with naming convention
- **DWG export**: Export to DWG with layer mapping table (Revit layers → CAD layers)
- **Transmittal generation**: Auto-generate drawing list, revision log, transmittal cover sheet
- **Naming convention**: Project#-Discipline-SheetType-Number-Revision (e.g., 2024001-A-FP-101-R03.pdf)
- **Quality checks**: Verify all views are placed, all tags are filled, no empty sheets

#### 6.7 Revit API for Drawing Automation

Key Revit API classes for drawing automation (C# / pyRevit / RevitPythonShell):

```python
## pyRevit example: Create sheets from Excel schedule
from Autodesk.Revit.DB import (
    FilteredElementCollector, ViewSheet,
    ViewFamilyType, Viewport
)

doc = __revit__.ActiveUIDocument.Document

## Get title block family type
title_blocks = FilteredElementCollector(doc) \
    .OfClass(FamilySymbol) \
    .OfCategory(BuiltInCategory.OST_TitleBlocks) \
    .ToElements()

## Create new sheet
with Transaction(doc, "Create Sheet") as t:
    t.Start()
    new_sheet = ViewSheet.Create(doc, title_blocks[0].Id)
    new_sheet.SheetNumber = "A1.01"
    new_sheet.Name = "FLOOR PLAN - LEVEL 1"

    # Place view on sheet
    view = get_view_by_name("Level 1 Floor Plan")
    viewport = Viewport.Create(doc, new_sheet.Id, view.Id, XYZ(0.4, 0.3, 0))
    t.Commit()
```

#### 6.8 Dynamo for View/Sheet Management

Dynamo workflows for drawing automation:
- **Sheets.CreateByNumber**: Create sheets from list of numbers and names
- **Views.SetCropBox**: Auto-set crop regions based on room/level boundaries
- **Viewport.SetLocation**: Position viewports on sheets by coordinates
- **Element.SetParameterByName**: Batch-update parameters (scale, detail level, view template)
- **Data.ImportExcel**: Read sheet lists, room schedules, or parameter data from Excel

---

### 7. Code Compliance Checking

#### 7.1 Building Code Automation: Egress

Automated egress checking is the most mature area of code compliance:

**Occupant load calculation**:
```
Occupant_Load = Floor_Area / Load_Factor

Load factors (IBC Table 1004.5):
- Assembly (chairs) = 0.65 m2/person
- Business = 9.3 m2/person
- Residential = 18.6 m2/person
- Educational = 1.9 m2/person
- Mercantile (ground floor) = 2.8 m2/person
```

**Exit requirements**:
- 1-500 occupants: minimum 2 exits
- 501-1000: minimum 3 exits
- 1001+: minimum 4 exits

**Exit width**:
```
Total_exit_width = Occupant_load * width_factor
  Stairways: 7.6 mm/person (sprinklered), 5.1 mm/person (unsprinklered) [IBC]
  Other egress: 5.0 mm/person (sprinklered), 3.8 mm/person (unsprinklered) [IBC]
Minimum single exit width: 810 mm (door), 1120 mm (corridor)
```

**Travel distance** (IBC Table 1017.2):
- Business, sprinklered: 90m (300 ft)
- Residential, sprinklered: 75m (250 ft)
- Assembly, sprinklered: 75m (250 ft)
- High hazard: 23m (75 ft)

**Common path of egress travel**: Maximum distance before two separate paths to exits are available. Typically 23m (75 ft).

#### 7.2 Fire Safety Automation

- **Compartmentation**: Maximum compartment area by construction type (IBC Table 506.2). Auto-check that fire walls divide building into compliant compartments.
- **Fire resistance rating**: By construction type and element (IBC Table 601). Auto-assign to wall, floor, and roof assemblies.
- **Sprinkler coverage**: Maximum coverage area per sprinkler head (standard 12.1 m2, light hazard). Auto-generate sprinkler layout.
- **Fire separation distance**: Distance from building face to property line or adjacent building. Determines allowable opening percentage.
- **Smoke control**: Atrium smoke management, stair pressurization requirements.

#### 7.3 Accessibility Automation

Key accessibility rules for automated checking:

- **Door clear width**: Minimum 815mm clear (ADA), 900mm (EN); auto-check all doors
- **Ramp grades**: Maximum 1:12 (8.3%); preferred 1:20 (5%); maximum rise 760mm per run; landings at top, bottom, and every 9m
- **Turning circles**: 1500mm diameter (ADA 1525mm) at all turns, at ends of corridors, in accessible rooms
- **Reach ranges**: Forward reach 380-1220mm; side reach 230-1370mm (ADA)
- **Accessible route**: Continuous accessible path from site entrance to all building functions; auto-trace and verify
- **Elevator requirements**: Buildings 3+ stories or 3000+ sq ft per floor require elevator
- **Accessible fixtures**: Toilet centerline 450-460mm from side wall; grab bars at 840-920mm; lavatory knee clearance 685mm

#### 7.4 Zoning Compliance

Automated zoning checks:

- **Setback verification**: Measure from building face to property line; compare to required front, side, rear setbacks
- **Height limit**: Building height (grade to highest point) vs. zoning maximum; also story count limits
- **FAR calculation**: Floor Area Ratio = Gross Floor Area / Lot Area; compare to zoning maximum
- **Lot coverage**: Building footprint area / Lot area; compare to maximum
- **Parking requirements**: Required spaces by use type and area/unit count; compare to provided
- **Open space**: Required open space calculation; verify provided open space meets minimum

#### 7.5 Daylight Compliance

- **Right to light**: Check that new construction does not reduce daylight to neighboring buildings below acceptable levels (BRE 209 method: VSC, NSL)
- **Daylight factor**: Minimum 2% average daylight factor for habitable rooms (UK standard); 1% minimum at any point
- **Window-to-floor ratio**: Minimum glazing area as percentage of floor area (varies by code; often 10-12.5%)
- **Automated checking**: From model geometry, calculate sky view factor at window; compare to threshold

#### 7.6 Automated Compliance Report Generation

Generate structured compliance reports:

```
BUILDING CODE COMPLIANCE REPORT
Project: [Auto-fill from model]
Code: IBC 2021 / Local amendments
Date: [Auto-generate]

1. BUILDING CLASSIFICATION
   Occupancy: B (Business)
   Construction Type: IIA
   Height: 23.5m (< 55m allowed) ✓
   Stories: 6 (< 12 allowed) ✓
   Area per floor: 1,850 m2 (< 3,700 m2 allowed) ✓

2. EGRESS
   Floor 1: Occupant load 199, Required exits 2, Provided 3 ✓
   Floor 2: Occupant load 199, Required exits 2, Provided 2 ✓
   ...
   Max travel distance: 42.3m (< 90m) ✓
   Common path: 18.7m (< 23m) ✓

3. ACCESSIBILITY
   Accessible route: Continuous ✓
   Door clearances: All doors ≥ 815mm ✓
   Elevator provided: Yes ✓
   Accessible toilet: 1 per floor ✓
   ...

RESULT: 47/47 checks PASS, 0 FAIL, 3 ADVISORY
```

---

### 8. Computational Workflow Design

#### 8.1 Workflow Orchestration Patterns

**Sequential**: Step A → Step B → Step C. Each step requires output of previous step.
Example: Site analysis → massing generation → energy simulation → report.

**Parallel**: Steps A, B, C run simultaneously; results merged at sync point.
Example: Structural analysis, energy analysis, daylight analysis run in parallel; results combined in dashboard.

**Conditional branching**: IF condition THEN path A ELSE path B.
Example: IF building height > 23m THEN high-rise structural system ELSE conventional framing.

**Iterative loop**: Repeat steps until convergence or max iterations.
Example: Adjust facade WWR → run energy simulation → check EUI target → if not met, adjust again.

**Fan-out/fan-in**: Generate N variants (fan-out) → evaluate all → select best (fan-in).
Example: Generate 100 floor plan options → score each → present top 10.

#### 8.2 Workflow Engines for AEC

| Engine | Language | Strengths | AEC Use |
|--------|----------|-----------|---------|
| Grasshopper | Visual/C# | Visual, real-time preview, huge plugin ecosystem | Parametric geometry, environmental analysis, optimization |
| Dynamo | Visual/Python | Revit integration, BIM automation | Drawing automation, model checking, data management |
| Speckle Automate | Python/C# | Cloud-native, event-driven, BIM data | Automated model checks, data transformations |
| n8n | Node.js | API integration, webhook triggers | Multi-tool orchestration, notification pipelines |
| Apache Airflow | Python | DAG-based, scalable, monitoring | Large-scale batch processing, simulation farms |
| Prefect | Python | Modern Airflow alternative, easy debugging | ML pipeline orchestration |
| Custom Python | Python | Full control, any library | Complex multi-step automation |

#### 8.3 Error Handling in Automated Workflows

Robust automation requires comprehensive error handling:

1. **Input validation**: Check all inputs before processing (file existence, data types, value ranges)
2. **Graceful degradation**: If optional step fails, continue with defaults
3. **Retry logic**: Transient failures (network, license server) retry with exponential backoff
4. **Fallback strategies**: If primary method fails, use alternative method
5. **Error logging**: Record all errors with context (timestamp, inputs, stack trace)
6. **User notification**: Alert user to failures requiring human intervention
7. **Checkpoint/restart**: Save intermediate results; resume from last checkpoint after failure

#### 8.4 Logging and Audit Trails

Design automation must maintain audit trails for:
- Professional liability (documenting design decisions)
- Quality assurance (tracing errors to source)
- Regulatory compliance (demonstrating code compliance process)
- Knowledge management (understanding why decisions were made)

Log levels: DEBUG (detailed computation), INFO (workflow steps), WARNING (non-critical issues), ERROR (failures), CRITICAL (system failures).

#### 8.5 Version Control for Workflows

- Store Grasshopper definitions in Git (`.gh` files are binary; use `.ghx` XML format for diffing)
- Dynamo graphs: `.dyn` files are JSON; store in Git with meaningful commit messages
- Python scripts: Standard Git workflow with branching, code review
- Rule libraries: Version rule sets independently from code; track code edition and amendment dates
- Template libraries: Version parametric detail templates with semantic versioning

---

### 9. Design Automation Case Studies

#### 9.1 Automated Facade Design

**Pipeline**: Solar analysis → shading device sizing → panel generation → fabrication data

1. **Solar analysis**: Run annual solar radiation simulation on facade surfaces (Ladybug/Honeybee or custom raytracing). Output: radiation map (kWh/m2/yr) per facade cell.
2. **Shading device sizing**: For each cell, calculate required shading depth based on radiation and orientation:
   ```
   shade_depth = window_height * tan(critical_sun_angle) * shading_factor
   critical_sun_angle = solar altitude at cooling design day peak
   ```
3. **Panel generation**: Generate facade panel geometry with sized shading devices. Apply panel types from a limited palette (e.g., 4-5 fin depths) for constructability.
4. **Structural check**: Verify fin depth/projection within structural capacity of facade framing.
5. **Fabrication data**: Export panel schedule with dimensions, material, finish. Generate CNC cutting files for custom panels. Output IFC model for coordination.

**Result**: 3000 unique panels documented in 2 hours instead of 2 weeks.

#### 9.2 Automated Parking Garage

**Pipeline**: Site boundary → ramp placement → bay layout → structural grid → count verification

1. **Input**: Site boundary polygon, required stall count, entry/exit locations, floor-to-floor height
2. **Ramp placement**: Test ramp locations at site perimeter and interior; evaluate traffic flow for each
3. **Bay layout**: For each ramp configuration, run parking layout algorithm:
   - Try 90-degree bays along long axis, then short axis
   - Try 60-degree bays if count is not met
   - Evaluate: stall count, aisle efficiency, dead-end length
4. **Structural grid**: Overlay structural grid aligned with parking bays (typically 5.0 x 8.1m or 5.0 x 16.2m for long-span)
5. **Count verification**: Total stalls per level x number of levels; check against requirement
6. **Accessible stalls**: Place required accessible stalls near elevators
7. **Output**: Floor plans, sections, stall count schedule, structural grid drawing

#### 9.3 Automated Residential Tower

**Pipeline**: Unit type library → floor plate stacking → core placement → code checking

1. **Unit type library**: Pre-designed unit types with variants:
   - Studio (28-35 m2): 3 variants
   - 1-bed (45-60 m2): 4 variants
   - 2-bed (70-90 m2): 5 variants
   - 3-bed (95-120 m2): 3 variants
   - Penthouse (150-250 m2): 2 variants
2. **Floor plate definition**: Building footprint from massing model; structural grid
3. **Core placement**: Position cores (elevator, stairs, shafts) considering structural, egress, and efficiency requirements
4. **Unit arrangement**: Pack unit types into floor plate around core; maximize units per floor; ensure all units have exterior windows; check corridor length
5. **Stacking**: Assign unit types to floors; align wet walls vertically; vary unit mix by floor level
6. **Code checking**: Run automated egress, fire safety, accessibility, and daylight compliance checks
7. **Output**: Typical floor plans, unit mix schedule, area tabulation, compliance report

#### 9.4 Automated Site Grading

**Pipeline**: Topography → cut/fill optimization → drainage design → retaining wall placement

1. **Topographic input**: Point cloud or contour data → TIN surface
2. **Design constraints**: Building pad elevation, access road grades (max 8%), parking areas (max 5%), ADA paths (max 5%), minimum drainage slope (1%)
3. **Cut/fill optimization**: Linear programming to balance cut and fill volumes (minimize import/export). Variables: finished grade elevations at grid points. Constraints: max/min grades, building pad, road connections.
4. **Drainage design**: Identify watersheds on finished grade; route overland flow to retention areas; size drainage infrastructure
5. **Retaining walls**: Where grade change between adjacent areas exceeds safe slope (typically 1:3 or 1:2), insert retaining wall. Size wall by height and soil conditions.
6. **Output**: Grading plan with spot elevations, cut/fill quantity table, drainage plan, retaining wall schedule

#### 9.5 Automated MEP Routing

**Pipeline**: Room requirements → duct/pipe sizing → route generation → clash detection

1. **Room requirements**: From room program, determine:
   - Airflow (CFM/L/s) based on occupancy and use
   - Heating/cooling loads (kW)
   - Plumbing fixture count
   - Electrical load (kW)
2. **Duct sizing**: Calculate duct dimensions from airflow using equal friction method:
   ```
   duct_area = airflow / velocity
   velocity: main duct 6-10 m/s, branch 3-6 m/s
   friction_rate: 0.8-1.2 Pa/m (low velocity), 1.5-2.5 Pa/m (high velocity)
   ```
3. **Route generation**: A* pathfinding on 3D grid from AHU to terminal units. Cost function includes: path length, number of bends (fittings), vertical elevation changes, proximity to structure (hanger points).
4. **Collision avoidance**: Route ducts to avoid structural members, other services. Priority: gravity drains > pressurized pipes > supply ducts > return ducts > cable trays.
5. **Clash detection**: Check all service routes against structure and each other. Report clashes with location and clearance required.
6. **Output**: 3D duct/pipe model, routing diagrams, duct/pipe schedules, clash report

---

### Key Design Automation Principles

1. **Automate the boring, not the creative**: Focus automation on repetitive, rule-based tasks. Leave conceptual design to humans.
2. **Start with the constraint, not the solution**: Model the problem as constraints first; let the solver find solutions.
3. **Validate early and often**: Check outputs against requirements at every step; do not accumulate errors.
4. **Design for maintenance**: Rules change (code updates, new standards). Build rule systems that are easy to update.
5. **Transparency over black boxes**: Designers must understand and trust the automation. Show reasoning, not just results.
6. **Graceful degradation**: When automation fails or produces poor results, fall back to manual workflow without data loss.
7. **Measure what matters**: Track automation ROI: time saved, error reduction, design quality improvement.

---

### Tools and Technologies

| Category | Tools |
|----------|-------|
| Rule engines | Drools, NRules, durable-rules, custom Python |
| CSP solvers | Google OR-Tools, python-constraint, MiniZinc |
| Optimization | Galapagos (GH), Optimus (GH), scipy.optimize, pymoo |
| Workflow | Grasshopper, Dynamo, Speckle Automate, Airflow, n8n |
| Drawing automation | Revit API, pyRevit, Dynamo, OpenBIM (IFC) |
| Compliance checking | Solibri, SMC, custom rule engines, BIM Checker |
| Space planning | Archilogic, Finch, depthmapX, custom solvers |
| Version control | Git, GitHub/GitLab, Speckle (model versioning) |


---

# Analysis & simulation


## structural-computation

### Structural Computation

> Finite element analysis fundamentals, form-finding methods, shell and gridshell structures, topology optimization, structural optimization, material-aware computation, and computational structural tools for AEC

## Structural Computation

### 1. Computational Structural Design Philosophy

#### The Unity of Form and Force

Structure is not an afterthought applied to a completed form. In the computational paradigm, structure **is** form. The geometry of a building, a bridge, a canopy -- each is a direct expression of the forces acting upon it. When we allow force to generate geometry rather than merely verifying geometry against force, we unlock an entirely different class of architectural expression: one that is simultaneously more efficient, more beautiful, and more materially honest.

This represents a fundamental epistemological shift: from **analysis-after-design** to **analysis-as-design**. The former treats structure as a constraint to be checked; the latter treats structure as a generative engine. In computational structural design, the distinction between "architect" and "engineer" dissolves. The designer works directly with force, curvature, material flow, and stress trajectories as primary design media.

#### Performance-Driven Geometry

Performance-driven geometry emerges when structural performance metrics (stress utilization, deflection, weight, embodied carbon) become the objective functions of a generative process. The designer defines boundary conditions, loads, material palettes, and performance targets. The computation produces geometry. This is not a loss of authorship -- it is an expansion of the design space far beyond what manual intuition can explore.

Key principles of performance-driven geometry:

- **Axial action over bending** -- Funicular forms carry load through compression or tension, avoiding costly bending. A catenary cable and an inverted catenary arch are the purest examples.
- **Curvature as stiffness** -- A flat plate is structurally weak; a curved shell resists load through membrane action. Double curvature provides bidirectional stiffness. The egg is the canonical example.
- **Material where stress exists** -- Topology optimization removes material where stress is absent and concentrates it along principal stress trajectories. The result resembles trabecular bone.
- **Hierarchy and redundancy** -- Efficient structures distribute load through hierarchical branching (trees, Gothic vaults, diagrid systems) with multiple load paths for robustness.

#### Historical Lineage

- **Gaudi (1852-1926)** -- Hanging chain models for the Colonia Guell chapel: physical form-finding producing pure compression vaults. The method is exact for catenary forms under self-weight.
- **Isler (1926-2009)** -- Hanging cloth models (fabric + plaster, inverted). Thin concrete shells at Deitingen, Norwich, Sicli: 40m+ spans at 70-90mm thickness. Physical analogue of dynamic relaxation.
- **Frei Otto (1925-2015)** -- Soap film experiments for minimal surface form-finding. Munich Olympic Stadium (1972), Mannheim Multihalle (1975). Founded the Institute for Lightweight Structures (IL) at Stuttgart.
- **Philippe Block (b. 1980)** -- Thrust Network Analysis (TNA): computational framework for compression-only funicular surfaces. Armadillo Vault (2016), NEST HiLo (2021).
- **Contemporary** -- Real-time structural feedback (Karamba3D, Kangaroo Physics), multi-objective optimization coupling structure with daylighting/thermal/fabrication, ML surrogates enabling population-based search over thousands of variants.

---

### 2. Finite Element Analysis Fundamentals

#### Overview

Finite Element Analysis (FEA) discretizes a continuous structure into a mesh of finite-sized elements, each governed by simple constitutive equations. By assembling element stiffness matrices into a global system, FEA solves for displacements, from which strains and stresses are derived. FEA is the universal method for structural verification in AEC.

#### Element Types

| Element Type | Dimensionality | DOF per Node | Captures | Typical Use |
|---|---|---|---|---|
| **Truss** | 1D (axial only) | 2 (2D) or 3 (3D) translations | Axial force only | Trusses, cables, bracing |
| **Beam** | 1D (axial + bending) | 6 (3 translations, 3 rotations) | Axial, shear, bending, torsion | Frames, columns, beams |
| **Shell** | 2D (membrane + bending) | 5-6 per node | In-plane + out-of-plane | Floors, walls, shells, slabs |
| **Plate** | 2D (bending only) | 3 (1 translation, 2 rotations) | Out-of-plane bending | Floor slabs |
| **Solid** | 3D | 3 translations | Full 3D stress state | Connections, nodes, foundations |
| **Cable** | 1D (tension only) | 3 translations | Tension, large displacements | Cables, tendons |
| **Spring** | 0D/1D | variable | Stiffness in specific DOFs | Supports, connections |

#### Element Formulations

- **Linear (first-order) elements**: Triangles (3-node), quadrilaterals (4-node), tetrahedra (4-node), hexahedra (8-node). Linear interpolation of displacements within each element. Require finer meshes but are computationally cheap per element.
- **Quadratic (second-order) elements**: Mid-side nodes added (6-node triangle, 8-node quad, 10-node tet, 20-node hex). Capture curved geometry and stress gradients more accurately. Preferred for stress analysis near holes, notches, and concentrated loads.
- **Reduced integration**: Uses fewer Gauss points than full integration (e.g., 1 point for a 4-node quad instead of 4). Faster but can exhibit hourglass modes (zero-energy deformation patterns). Remedied by hourglass control or selective reduced integration.

#### Mesh Requirements for FEA

Structural FEA meshes differ fundamentally from visualization/rendering meshes:

- **Aspect ratio** -- Elements should be as equilateral as possible. Aspect ratios above 5:1 degrade accuracy. Target < 3:1.
- **Minimum elements per span** -- At least 4-6 elements across any structural span; 8-12 for accurate stress recovery.
- **Mesh grading** -- Refine mesh near stress concentrations (holes, corners, load application points, support reactions) and use coarser mesh in low-gradient regions.
- **Element quality metrics** -- Jacobian ratio > 0.5, warpage < 15 degrees, skewness < 60 degrees for quads.
- **Mesh transitions** -- Avoid sudden jumps in element size (ratio of adjacent elements < 2:1).
- **Compatibility** -- Nodes must match at element boundaries. Hanging nodes require constraint equations or multi-point constraints (MPCs).

#### Boundary Conditions

| Type | Translation | Rotation | Symbol | Physical Example |
|---|---|---|---|---|
| **Fixed (Encastre)** | Restrained all | Restrained all | Triangle filled | Moment-resisting base plate |
| **Pinned** | Restrained all | Free all | Triangle open | Pin connection, ball joint |
| **Roller** | Free in 1 dir, restrained in others | Free all | Circle on line | Expansion bearing |
| **Spring** | Elastic (k) | Elastic (k_r) | Zigzag | Soil springs, flexible supports |
| **Symmetry** | Free parallel, restrained normal | Free about normal, restrained about parallel | Dashed line | Half-model symmetry plane |

#### Load Types

- **Point load (concentrated)** -- Force applied at a single node. Units: kN (SI), kip (Imperial).
- **Line load (distributed)** -- Force per unit length along a beam element. Units: kN/m, kip/ft.
- **Area load (pressure)** -- Force per unit area on shell/plate elements. Units: kN/m², psf.
- **Self-weight** -- Gravity applied to all elements based on material density. Acceleration: g = 9.81 m/s² (32.2 ft/s²).
- **Wind load** -- Pressure distribution from wind codes (EN 1991-1-4, ASCE 7-22 Ch. 26-31). Varies with height, exposure, building shape.
- **Seismic load** -- Equivalent lateral force (ELF) or response spectrum analysis per EN 1998 or ASCE 7-22 Ch. 11-23.
- **Thermal load** -- Temperature change causing expansion/contraction. Gradient through cross-section causes bending.
- **Prestress** -- Applied internal force (post-tensioning tendons, cable pretension).

#### Load Combinations

Structural design requires checking multiple load combinations per code. Key combinations:

- **Eurocode ULS**: 1.35G + 1.5Q (fundamental); with psi factors for multiple variable actions
- **ASCE 7 LRFD**: 1.2D + 1.6L (gravity dominant); 1.2D + 1.0E + L (seismic); 0.9D + 1.0W (uplift)

See `references/fea-fundamentals.md` for complete load combination tables with psi factors.

#### The Stiffness Matrix Concept

The fundamental FEA equation: **[K]{u} = {F}** where [K] is the global stiffness matrix (assembled from element stiffness matrices), {u} is the displacement vector (unknowns), and {F} is the force vector. The system is solved for {u}, from which strains and stresses are derived.

Key element stiffness matrices (truss: EA/L terms; beam: EI/L^3 terms; shell: Et and Et^3/(12(1-nu^2)) terms) are derived and tabulated in `references/fea-fundamentals.md`.

#### Result Interpretation

- **Von Mises stress**: sigma_vm = sqrt(sigma_x^2 - sigma_x*sigma_y + sigma_y^2 + 3*tau_xy^2). Combined equivalent stress for ductile material yield check.
- **Principal stresses**: sigma_1, sigma_2, sigma_3 (eigenvalues of stress tensor). Directions indicate natural force flow.
- **Utilization ratio**: U = demand/capacity. U < 1.0 = safe. Color: green (< 0.5), yellow (0.5-0.8), orange (0.8-1.0), red (> 1.0).
- **Deflection**: Check against limits (L/250 total, L/360 live load typical). See `references/fea-fundamentals.md` for complete deflection limits table.

#### Convergence Checking

- **h-method** -- Refine mesh (halve element sizes) and re-run. If results change by < 5%, mesh is adequate.
- **p-method** -- Increase element polynomial order (linear to quadratic) and re-run. More efficient for smooth solutions.
- **Adaptive mesh refinement** -- Automated refinement based on error estimators (Zienkiewicz-Zhu, residual-based).
- **Target**: Stress convergence within 2-5% between successive refinements.

#### Units (Quick Reference)

| Quantity | SI | Imperial |
|---|---|---|
| Force | kN | kip (= 1000 lb) |
| Stress | MPa (= N/mm^2) | ksi (= 1000 psi) |
| Moment | kN.m | kip.ft |
| Distributed load | kN/m | kip/ft |
| Young's modulus | GPa | ksi |

Full units table and cross-section property tables in `references/fea-fundamentals.md`.

---

### 3. Form-Finding Methods

Form-finding discovers structural geometry in static equilibrium under given loads, producing shapes that carry load through membrane action (tension or compression) rather than bending. These **funicular** forms are inherently material-efficient.

#### 3.1 Hanging Chain / Catenary Method

A freely hanging chain adopts a catenary curve y(x) = a*cosh(x/a) where a = H/w. Inverting gives a pure compression arch. For uniform horizontal load, the shape is parabolic y = wx^2/(2H). Only valid for a single load case -- changing load changes the funicular shape.

#### 3.2 Force Density Method (FDM)

Assigns a force-density ratio q = F/L to each element, linearizing the equilibrium equations (Schek, 1974): `[C^T * diag(q) * C] * {x} = {p_x} - [C_f^T * diag(q_f)] * {x_f}`. Linear system = direct solution, no iteration, guaranteed equilibrium. Force densities are prescribed (not forces), requiring experience to choose meaningful q-distributions. Best for cable nets, membranes, tensile canopies. See `references/form-finding-methods.md` for full derivation and worked example.

#### 3.3 Dynamic Relaxation

A fictitious dynamic system oscillates under applied loads with artificial damping until static equilibrium is reached. Algorithm: initialize positions -> compute internal forces -> compute residuals -> update velocities with damping -> update positions -> check convergence (kinetic energy or residual force < tolerance) -> iterate.

**Kinetic damping** (Barnes, 1988) is the standard method: reset all velocities to zero when total kinetic energy peaks. Extremely robust, no parameter tuning. Time step must satisfy Courant condition: dt < sqrt(2*m_min/k_max). Best for cable nets, membranes, inflatables, gridshells. See `references/form-finding-methods.md` for pseudocode and damping strategies.

#### 3.4 Thrust Network Analysis (TNA)

Block's method (2009) finds compression-only funicular surfaces using reciprocal force diagrams. A **form diagram** (horizontal projection of the network) has a dual **force diagram** where edge lengths represent horizontal force magnitudes. Vertical coordinates are solved from equilibrium. Scaling the force diagram changes the rise-to-span ratio without breaking the compression-only constraint.

Applications: unreinforced masonry vaults, stone shells, tile vaulting, 3D-printed compression structures. Software: RhinoVAULT, RV2, compas_tna. See `references/form-finding-methods.md` for reciprocal diagram theory.

#### 3.5 Particle-Spring Systems (Kangaroo Physics)

**Principle**: Structural elements are represented as particles (nodes with mass) connected by springs (elements with stiffness). Loads, constraints, and geometric objectives are expressed as "goals" that apply forces to particles. The solver iteratively moves particles toward equilibrium.

**Kangaroo 2 (Daniel Piker)** uses a position-based dynamics approach:
- Each **Goal** calculates target positions for its participating nodes
- The solver averages target positions from all goals at each node
- Convergence occurs when goals agree (residual forces vanish)

**Common goal types**:
- **Length** -- Spring with rest length and stiffness
- **Angle** -- Angular spring between adjacent edges
- **Planarize** -- Forces a set of points toward coplanarity
- **OnMesh/OnSurface** -- Constrains points to lie on a reference geometry
- **Load** -- Applies constant force (gravity, wind)
- **Anchor** -- Fixes points with high stiffness
- **Pressure** -- Applies uniform pressure to a closed mesh (inflation)
- **SoapFilm** -- Minimizes area (minimal surface)
- **Hinge** -- Resists bending at mesh edges
- **Floor/Plane collision** -- Prevents penetration through a plane

**Best for**: Interactive form-finding, real-time feedback, multi-physics simulation (structure + fabrication constraints simultaneously), educational exploration.

#### 3.6 Minimal Surfaces

**Definition**: A minimal surface has zero mean curvature (H = 0) at every point. Equivalently, it locally minimizes surface area for a given boundary. Soap films naturally form minimal surfaces.

**Mathematical characterization**: Mean curvature H = (kappa_1 + kappa_2) / 2 = 0, where kappa_1 and kappa_2 are principal curvatures. This means the surface curves equally in opposite directions at every point (anticlastic geometry).

**Classical minimal surfaces**:
- **Catenoid** -- Only minimal surface of revolution. Generated by rotating a catenary curve.
- **Helicoid** -- Ruled minimal surface. Generated by a line sweeping helically.
- **Enneper surface** -- Self-intersecting, algebraically simple.

**Triply periodic minimal surfaces (TPMS)**:
- **Schwarz-P** (Primitive) -- Cubic symmetry, channel-like openings on faces.
- **Schwarz-D** (Diamond) -- Channels along body diagonals.
- **Gyroid** -- No planes of symmetry, no straight lines. Channel structure.
- **I-WP** (I-graph Wrapped Package) -- Complex interconnected channels.
- Applications in architecture: lightweight infill structures, acoustic panels, thermal exchangers, 3D-printed facade elements.

**Structural implications**: Minimal surfaces carry uniform tension under uniform pressure. They are structurally efficient for membrane structures (tents, canopies) but require edge cables or rigid boundaries to anchor the tension field.

#### Method Comparison Table

| Method | Speed | Accuracy | Geometric Freedom | Tool Availability | Best For |
|---|---|---|---|---|---|
| Hanging chain | Fast | Exact (catenary) | Low (2D curves) | Physical models, Python | Arches, cables |
| Force Density | Very fast | Good (equilibrium exact) | Medium (network topology) | Python, compas | Cable nets, membranes |
| Dynamic Relaxation | Medium | High | High (any topology) | Kangaroo, custom code | Shells, gridshells, inflatables |
| TNA | Medium | High (compression-only) | Medium-High | RhinoVAULT, compas_tna | Masonry vaults, stone shells |
| Particle-Spring | Fast (interactive) | Good | Very high | Kangaroo 2 (GH) | Conceptual design, mixed goals |
| Minimal Surface | Varies | Exact (H=0) | Low (boundary-driven) | Kangaroo, Evolver, MATLAB | Tensile canopies, TPMS |

---

### 4. Shell Structures

#### Classification by Curvature

| Type | Gaussian Curvature K | Principal Curvatures | Examples |
|---|---|---|---|
| **Synclastic** | K > 0 (positive) | Same sign (both up or both down) | Dome, elliptic paraboloid |
| **Anticlastic** | K < 0 (negative) | Opposite signs | Hyperbolic paraboloid (hypar), saddle |
| **Developable** | K = 0 | One curvature is zero | Cylinder, cone, tangent surface |
| **Free-form** | Variable K | Varying | Irregular blobs, organic shells |

#### Membrane Theory vs. Bending Theory

**Membrane theory** assumes the shell is so thin that it carries load purely through in-plane forces (N_x, N_y, N_xy) with no bending moments. Valid when:
- Shell thickness t << radius of curvature R (t/R < 1/20)
- Loading is smooth and distributed
- Boundaries allow free in-plane movement (membrane-compatible supports)
- No concentrated loads or abrupt geometry changes

**Bending theory** (general shell theory) includes both membrane and bending actions. Required when:
- Near edges and supports (boundary layer effects, with decay length ~ sqrt(R*t))
- At geometric discontinuities (openings, ribs, thickness changes)
- Under concentrated loads
- When the shell is thick relative to its curvature

#### Buckling Analysis for Thin Shells

Thin shells are extremely sensitive to buckling. The classical critical buckling pressure for a sphere under uniform external pressure is:

```
p_cr = 2E / sqrt(3(1-nu^2)) * (t/R)^2
```

However, real shells buckle at 15-50% of the classical prediction due to geometric imperfections. Knockdown factors are essential:
- **NASA SP-8007** knockdown factors for cylindrical and spherical shells
- **Eurocode EN 1993-1-6** shell buckling assessment (LSA, MNA, GMNIA analyses)
- **Nonlinear buckling analysis (GMNIA)** -- Geometrically and Materially Nonlinear Analysis with Imperfections. The gold standard. Requires seeding geometric imperfections (first eigenmode shape scaled to fabrication tolerance, typically t/10 to t/2).

#### Shell Thickness Optimization

Shell thickness can vary spatially to match structural demand:
- **Regions of high membrane force** -- increase thickness
- **Regions near supports** -- increase thickness (bending zone)
- **Central regions far from boundaries** -- minimize thickness
- Parametric thickness variation: linear, stepped, or continuously graded
- Optimization methods: sensitivity-based gradient descent, evolutionary algorithms, or topology optimization of shell thickness field

#### Geometric Stiffness: Curvature = Strength

A fundamental principle of shell design: curvature provides stiffness. A flat plate of thickness t has bending stiffness D = Et^3/[12(1-nu^2)]. A curved shell of the same thickness resists load primarily through membrane action, with effective stiffness proportional to Et (not Et^3). This means a shell can be dramatically thinner than a flat plate spanning the same distance.

- Doubling curvature approximately halves the required thickness
- Gaussian curvature (K = kappa_1 * kappa_2) provides biaxial stiffness
- Zero Gaussian curvature (developable surfaces) allows deformation along the zero-curvature direction
- Corrugation adds effective curvature in one direction (folded plates)

#### Edge Conditions and Boundary Effects

- **Free edge** -- Membrane forces must vanish at the edge. Edge beam or thickening required to collect forces.
- **Simply supported edge** -- Vertical reaction provided but no moment restraint. Causes local bending concentration.
- **Fixed edge** -- Full moment connection. Highest bending demand at edge.
- **Ring beam / edge beam** -- Collects horizontal thrust from dome or vault. Sized for the horizontal component of membrane force.
- **Boundary layer width** -- The distance over which bending effects decay from an edge into the membrane zone is approximately L_b = sqrt(R * t) * pi / sqrt(12(1-nu^2)). For a concrete dome with R = 20m, t = 100mm: L_b is approximately 2.5m.

#### Ribbed Shells and Stiffening Strategies

When a pure shell is insufficient (due to buckling, openings, or concentrated loads), stiffening is added:
- **Ribs** -- Beam elements on the shell surface. Orthogonal grids or radial-circumferential patterns.
- **Corrugation / folding** -- Adds effective depth without adding material.
- **Sandwich construction** -- Two thin skins separated by a core (foam, honeycomb, lattice).
- **Grid stiffening** -- Continuous shell replaced by a lattice shell (gridshell) where elements act as ribs.

#### Historical Reference Shells

| Designer | Project | Year | Span | Thickness | Material | Innovation |
|---|---|---|---|---|---|---|
| Felix Candela | Los Manantiales | 1958 | 30m | 40mm | RC | Hypar intersections |
| Pier Luigi Nervi | Palazzetto dello Sport | 1957 | 59m | ~25mm (ribs) | RC | Ferrocement prefab ribs |
| Heinz Isler | Deitingen Service Station | 1968 | 32m | 90mm | RC | Hanging model form-finding |
| Eladio Dieste | Church of Christ the Worker | 1958 | 16m | 120mm | Brick | Gaussian curvature brick |
| Cecil Balmond | Serpentine Pavilion (w/ Ito) | 2002 | 18m | - | Steel | Algorithmic pattern |
| SANAA | Rolex Learning Center | 2010 | 166x121m | varies | RC | Free-form continuous shell |
| BIG | Amager Bakke (CopenHill) | 2019 | - | - | Steel/aluminum | Facade as shell |
| Zaha Hadid | Al Janoub Stadium | 2019 | - | - | Steel/PTFE | Operable roof shell |

#### Material Considerations for Shells

- **Reinforced concrete** -- Classic shell material. Formwork cost is the main challenge; fabric-formed or CNC-milled foam formwork reduce cost.
- **Timber** -- CLT/LVL panels CNC-cut for segments. Good for compression shells. Joints are critical.
- **Steel** -- Welded plates for free-form shells. Expensive but precise.
- **GFRP** -- Lightweight, formable, corrosion-resistant. Limited by creep and fire performance.
- **ETFE** -- Pneumatic cushions. Transparent, lightweight, not structural in the traditional sense.
- **Brick/stone** -- Compression-only shells designed with TNA. Block Research Group projects.

---

### 5. Gridshell Structures

#### Definition and Classification

A gridshell is a structure with the shape and stiffness of a double-curved shell but made from a grid of linear elements (beams or laths) rather than a continuous surface. The grid carries load through a combination of membrane action (in-plane forces) and bending in individual elements.

**Single-layer gridshells**: One layer of beams. Structurally efficient when the form is funicular. Susceptible to buckling due to low bending stiffness in the normal direction. Requires in-plane bracing (diagonal cables or rods) to resist shear.

**Double-layer (or multi-layer) gridshells**: Two layers of beams separated by a core depth, connected by diagonal bracing or shear connectors. Much stiffer and more stable. Better for non-funicular or asymmetric loading.

#### Elastic Gridshells (Bent from Flat)

The defining innovation: a flat grid of flexible laths is assembled on the ground and then pushed/pulled into a doubly-curved shape. The laths bend elastically to accommodate the curvature. Once in shape, the grid is braced and the structure is stiff.

**Process**:
1. Fabricate flat grid (typically with sliding/rotating connections)
2. Lift or push grid into target shape using cranes, scaffolding, or actuators
3. Lock connections (tighten bolts, weld, or add bracing)
4. The stored bending energy in the laths provides initial stiffness

**Key constraint**: The lath material must accommodate the maximum bending strain without failure. For timber laths: epsilon_max = t / (2R_min) < epsilon_allow. This limits the minimum radius of curvature for a given lath thickness.

**Material choices**: Timber (oak, larch, bamboo), GFRP rods, steel tubes (for larger radii).

#### Rigid Gridshells (Assembled in Shape)

Beam elements are fabricated straight (or pre-bent to match local curvature) and assembled on scaffolding in the final curved shape. Connections are moment-rigid or pin-connected.

- No residual bending stress from erection
- Allow larger members and longer spans
- More complex fabrication and erection
- Examples: British Museum Great Court (Foster + Partners), Smithsonian Courtyard

#### Node Design and Connection Types

The node is the critical detail -- it must transfer forces between converging members while accommodating geometric complexity and remaining economically fabricable.

**Connection types**: Slotted plate nodes (simple, economical for orthogonal grids), cast steel nodes (3D-printed or investment-cast for complex geometry), bolted steel plates (adjustable, tolerance-forgiving), laminated timber finger joints (CNC-cut for all-timber gridshells), 3D-printed metal nodes (topology-optimized, SLM/DMLS, minimum material), and proprietary systems (MERO/KK ball joints for space frames).

#### Bracing Strategies

Single-layer gridshells require in-plane shear stiffness (bracing) to resist asymmetric loads:
- **Diagonal cables** -- Lightweight, nearly invisible. Pretensioned for load reversal. Most common.
- **Diagonal rods** -- Can resist both tension and compression. Heavier than cables.
- **Rigid panels** -- Glass or metal panels acting as shear diaphragms. Eliminates need for separate bracing.
- **Third layer of members** -- Triangulation. Converts the grid from quad-dominant (shear-flexible) to triangle-dominant (shear-stiff).

#### Form-Finding for Gridshells

- **Compass method** -- A kinematic method for elastic gridshells. Starting from a flat Chebyshev net (constant member spacing), the net is draped onto a target surface while maintaining constant member lengths. The resulting shape satisfies the fabrication constraint of using equal-length laths.
- **Projection method** -- A target surface is defined (from dynamic relaxation or other form-finding). A flat grid is projected onto this surface. Member lengths vary, requiring custom cutting.
- **Inverse hanging model** -- A cable net is hung under gravity, inverted, and the node positions define the gridshell geometry. Combined with dynamic relaxation for accuracy.
- **Optimization-based** -- Minimizing a combination of structural weight, bending stress in laths, and deviation from a target surface. Multi-objective optimization using genetic algorithms or gradient methods.

#### Panel Planarity

For glazed gridshells, quadrilateral panels must be planar or near-planar (tolerance: < L/500 to L/1000 of panel diagonal). Strategies:
- **Conical meshes** -- Normals at each node lie on a cone, guaranteeing planar quad faces
- **Planarization** -- Post-processing optimization of node positions (Kangaroo Planarize goal, Evolute Tools)
- **Triangulation** -- Always planar but increases member/node count and cost
- **Curved panels** -- Cold-bent or hot-bent glass. Expensive but increasingly feasible

#### Key Gridshell Projects

| Project | Year | Span | Material | Type | Designers |
|---|---|---|---|---|---|
| Mannheim Multihalle | 1975 | 60x60m | Timber laths | Elastic | Frei Otto, Mutschler |
| British Museum Great Court | 2000 | 73x96m | Steel + glass | Rigid | Foster + Partners, Buro Happold |
| Japan Pavilion (Hannover) | 2000 | 73x25m | Cardboard tubes | Elastic | Shigeru Ban |
| Downland Gridshell | 2002 | 50x16m | Oak laths | Elastic | Edward Cullinan, Buro Happold |
| Savill Garden | 2006 | 25m | Timber laths | Elastic | Glenn Howells, Buro Happold |
| Yas Hotel | 2009 | 217m length | Steel | Rigid | Asymptote, Schlaich |
| Chadstone Shopping Centre | 2016 | 190x55m | Steel + glass | Rigid | CallisonRTKL |

---

### 6. Topology Optimization

#### Overview

Topology optimization determines the optimal distribution of material within a design domain to maximize or minimize an objective function subject to constraints. Unlike sizing optimization (which changes member sizes) or shape optimization (which moves boundaries), topology optimization can create entirely new topologies -- holes, branches, and connections that were not present in the initial design.

#### SIMP Method (Solid Isotropic Material with Penalization)

The most widely used topology optimization method in AEC.

**Design variable**: Element pseudo-density rho_e in [0, 1] where 0 = void and 1 = solid.

**Penalized stiffness**: E_e = rho_e^p * E_0 where p is the penalization factor (typically p = 3). The penalization drives intermediate densities toward 0 or 1, producing a clear solid/void result.

**Objective**: Minimize compliance (= maximize global stiffness):
```
min C = {F}^T {u} = sum(rho_e^p * u_e^T * k_e * u_e)
```
Subject to:
```
[K(rho)]{u} = {F}     (equilibrium)
V = sum(rho_e * v_e) <= V_target   (volume constraint)
0 < rho_min <= rho_e <= 1          (bounds)
```

**Solution**: Sensitivity analysis (dC/d_rho_e) via adjoint method, followed by optimality criteria (OC) update or Method of Moving Asymptotes (MMA).

#### Level-Set Method

Represents the material boundary as the zero-level contour of a level-set function phi(x). phi > 0 = solid, phi < 0 = void. The boundary evolves by solving a Hamilton-Jacobi equation driven by shape sensitivities.

**Advantages**: Crisp boundaries (no intermediate densities). Natural for manufacturing.
**Disadvantages**: Cannot easily nucleate new holes (requires seeding). More complex to implement.

#### ESO/BESO (Evolutionary Structural Optimization)

**ESO** (Xie and Steven, 1993): Iteratively removes elements with the lowest stress or strain energy density. Simple but can get stuck in local optima.

**BESO** (Bi-directional ESO): Allows both removal and addition of elements. More robust than ESO. Uses sensitivity filtering and stabilization.

**Advantages**: Simple to implement. Produces clear 0/1 solutions.
**Disadvantages**: Heuristic (no formal convergence proof for ESO). Can produce mesh-dependent results without filtering.

#### Ground Structure Method

Starts with a highly connected truss network (the "ground structure") spanning the design domain. Optimization removes members with zero or near-zero force, leaving the optimal truss topology. Produces discrete, fabricable structures directly.

**Best for**: Long-span roof trusses, bridges, tower structures.

#### Design Domain, Loads, and Constraints

Setting up a topology optimization problem requires careful definition of:
- **Design domain** -- The 3D region within which material can be placed. Defined by architectural/spatial constraints.
- **Non-design domains** -- Regions that must remain solid (connection zones, load introduction points) or void (openings, passages).
- **Loads** -- Applied forces and their distributions. Multiple load cases handled by summing weighted compliances.
- **Supports** -- Boundary conditions (fixed, pinned, spring).
- **Volume fraction** -- Target material usage as a percentage of the design domain. Typical values: 20-50%. Lower fractions produce more organic, branching topologies.
- **Symmetry** -- Mirror symmetry planes, rotational symmetry, cyclic repetition.

#### Filtering

Without filtering, topology optimization produces **checkerboard patterns** (alternating solid/void elements) and **mesh-dependent** results (different meshes give different topologies).

- **Sensitivity filter** -- Smooths sensitivity values by averaging over a neighborhood of radius r_min. The most common approach.
- **Density filter** -- Smooths densities directly. Produces gray (intermediate density) boundaries.
- **Heaviside projection** -- After density filtering, applies a smooth step function to sharpen the 0/1 boundary. Controlled by a parameter beta that increases during optimization (continuation method).
- **Minimum member size** -- Enforced by choosing r_min >= minimum desired feature size.

#### Penalization Factor

The standard SIMP penalization p = 3 works well for stiffness-based optimization:
- p = 1: No penalization, result is full of gray.
- p = 2: Moderate penalization. Some gray remains.
- p = 3: Standard. Most intermediate densities penalized away.
- p = 4-5: Aggressive penalization. Can cause convergence issues.

**Continuation approach**: Start with p = 1 and gradually increase to p = 3 over iterations. Improves convergence and can find better optima.

#### Interpretation of Results

Raw topology optimization output requires post-processing:
- **Thresholding** -- Set a density cutoff (e.g., rho > 0.5 = solid). Produces a binary solid/void result.
- **Smoothing** -- Apply Laplacian or Gaussian smoothing to the boundary. Removes staircase artifacts.
- **CAD reconstruction** -- Fit NURBS surfaces or B-rep geometry to the smoothed result. Manual or semi-automated (e.g., nTopology, Altair Inspire).
- **Structural verification** -- Re-analyze the interpreted geometry with FEA to confirm performance. The post-processed shape may differ from the optimized result.

#### 2D vs. 3D Topology Optimization

**2D optimization** is used for:
- Planar components (brackets, gusset plates, flat connection details)
- Cross-sections of beams or walls
- Pedagogical examples and initial exploration
- Computation time: seconds to minutes

**3D optimization** is used for:
- Spatial structural nodes
- Transfer structures (load paths through a 3D volume)
- Foundation layouts
- Full building volumes
- Computation time: minutes to hours (can be very large for fine meshes)

#### Tools for Topology Optimization

| Tool | Platform | Method | 2D/3D | Cost | Notes |
|---|---|---|---|---|---|
| **Millipede** | Grasshopper | SIMP-like | 2D + 3D | Free | Fast, good GH integration |
| **Ameba** | Grasshopper | BESO | 2D + 3D | Free | Clear results, slower |
| **TopOpt** | Web (DTU) | SIMP | 2D | Free | Educational, interactive |
| **TOSCA** | Abaqus (Dassault) | SIMP, Level-set | 3D | Expensive | Industrial, validated |
| **Altair Inspire** | Standalone | SIMP (OptiStruct) | 3D | Expensive | Intuitive GUI, mfg constraints |
| **nTopology** | Standalone | Lattice + TO | 3D | Expensive | Lattice infill, AM-ready |
| **ANSYS Topology** | ANSYS | SIMP | 3D | Expensive | Integrated with ANSYS FEA |

#### AEC Applications

- **Structural nodes** -- Topology-optimized steel nodes for space frames and gridshells. 3D-printed in metal. Up to 75% weight reduction vs. conventional welded nodes. Arup's 3D-printed steel nodes for a structural tree.
- **Floor plates** -- Ribbed slabs with topology-optimized rib patterns. ETH Zurich NEST HiLo project: 3D-printed concrete floor with 70% less material than flat slab.
- **Facade brackets** -- Connection elements between facade panels and primary structure. Optimize for multiple load cases (wind, self-weight, seismic).
- **Foundations** -- Material distribution in transfer beams and pile caps. Strut-and-tie models are a classical topology optimization concept.
- **Furniture and pavilions** -- Increasingly common for one-off or small-series production. Branch Technology, AI Build, MX3D.

---

### 7. Material-Aware Computation

#### Material Properties Table

| Property | Steel (S355) | Concrete (C40/50) | Timber (GL28h) | Aluminum (6061-T6) | GFRP | CFRP | Bamboo |
|---|---|---|---|---|---|---|---|
| E (GPa) | 210 | 35 | 12.6 (parallel) | 69 | 25-40 | 70-150 | 15-20 |
| f_y (MPa) | 355 | - | - | 275 | - | - | - |
| f_u (MPa) | 510 | - | - | 310 | 400-800 | 600-2000 | 100-200 |
| f_c (MPa) | - | 40 | 28 | - | 150-250 | 500-1500 | 40-80 |
| f_t (MPa) | 355 | 3.5 | 22.3 | 275 | 400-800 | 600-2000 | 100-200 |
| f_b (MPa) | 355 | - | 28 | 275 | 250-500 | 600-1500 | 80-150 |
| Density (kg/m^3) | 7850 | 2500 | 410 | 2700 | 1800-2100 | 1500-1600 | 600-800 |
| Poisson's ratio | 0.30 | 0.20 | 0.35 (major) | 0.33 | 0.25-0.35 | 0.25-0.30 | 0.30 |
| alpha (10^-6/C) | 12 | 10 | 5 (parallel) | 23 | 6-10 | -1 to 2 | 3-5 |

#### Anisotropic Materials

**Timber**: Strongly anisotropic. Properties differ along grain (longitudinal), across grain (radial), and tangential directions. E_L : E_R : E_T is approximately 20 : 1.6 : 1. Computational models must account for grain direction. CLT (Cross-Laminated Timber) alternates grain direction for quasi-isotropic behavior in-plane.

**Fiber composites (GFRP, CFRP)**: Properties depend on fiber orientation. Unidirectional laminates are strongly anisotropic. Quasi-isotropic layups ([0/+45/-45/90]s) provide balanced in-plane properties but are weaker than aligned laminates in any single direction. Classical Laminate Theory (CLT -- confusingly same acronym) governs composite analysis.

**Masonry**: Anisotropic due to mortar joints. Different stiffness and strength along bed joints vs. head joints vs. diagonal. Homogenized masonry models treat the assembly as an equivalent anisotropic continuum.

#### Material Behavior Models

- **Linear elastic** -- Stress proportional to strain (Hooke's law). Valid for most materials at service load levels. The basis for most FEA in AEC.
- **Elasto-plastic** -- Linear elastic up to yield, then plastic deformation at constant (or hardening) stress. Required for steel design at ULS. Bilinear or multilinear stress-strain models.
- **Viscoelastic** -- Time-dependent deformation under sustained load (creep). Critical for concrete and timber. Modeled as spring-dashpot combinations (Maxwell, Kelvin-Voigt, Burgers models).
- **Nonlinear elastic** -- Stress-strain curve is nonlinear but unloading follows the loading path. Rubber, some polymers.
- **Brittle** -- No plastic deformation before failure. Concrete in tension, glass, unreinforced masonry. Requires fracture mechanics or damage models.

#### Composite Action

When two materials act together (steel-concrete beams, timber-concrete floors), **transformed section analysis** converts to an equivalent single-material section using modular ratio n = E_1/E_2 (full composite). Partial composite action (interface slip) is modeled with interface springs. Shear connectors (headed studs, screws) transfer horizontal shear.

#### Material Efficiency Metrics

| Material | Strength/Weight (f/rho, kN.m/kg) | Stiffness/Weight (E/rho, MN.m/kg) | Embodied Carbon (kgCO2e/kg) |
|---|---|---|---|
| Steel S355 | 45 | 27 | 1.5-2.5 |
| Concrete C40 | 16 (compression) | 14 | 0.1-0.2 |
| Timber GL28h | 68 | 31 | -1.0 to 0.5 |
| Aluminum 6061 | 102 | 26 | 8.0-12.0 |
| CFRP | 400-1300 | 47-100 | 20-30 |
| Bamboo | 130-250 | 20-30 | 0.5-2.0 |

Timber and bamboo are exceptional: high strength-to-weight, low-to-negative embodied carbon. CFRP is phenomenal structurally but carries enormous environmental cost. Steel and concrete are the workhorses with moderate efficiency.

#### Digital Material Systems

Emerging paradigm of spatially varying material properties:
- **Functionally Graded Materials (FGM)** -- Continuous variation of composition (e.g., concrete with graded fiber density)
- **Variable-density lattices** -- 3D-printed lattice infill matched to stress fields from topology optimization (nTopology, Altair)
- **Multi-material printing** -- Simultaneous deposition of stiff and flexible materials for spatially tuned stiffness
- **Programmable materials** -- Shape-memory alloys, 4D printing, materials responding to stimuli (temperature, moisture)

---

### 8. Structural Computation Tools

#### 8.1 Karamba3D (Grasshopper)

**Capabilities**: Real-time FEA within Grasshopper. Beam and shell elements. Linear and second-order analysis. Cross-section optimization. Utilization checking. Eigen-frequency and buckling analysis. Large deformation analysis (geometrically nonlinear).

**Limitations**: No material nonlinearity (no concrete cracking, no steel yielding). No dynamic time-history analysis. Not a code-checking tool (no automatic Eurocode/ASCE capacity checks -- requires manual setup). Accuracy depends on mesh quality.

**Integration**: Fully embedded in Grasshopper. Takes Rhino geometry (lines, meshes) as input. Outputs displaced shapes, stress results, utilization ratios as colored meshes. Connects to Octopus, Galapagos, Wallacei for optimization.

**Learning curve**: Moderate. Structural concepts required. Well-documented with tutorials.

**Typical workflow**: Define geometry (lines/mesh) -> assign cross-sections -> define supports -> apply loads -> assemble model -> analyze -> read results -> iterate/optimize.

#### 8.2 Kangaroo Physics (Grasshopper)

**Capabilities**: Interactive particle-spring solver. Form-finding (cable nets, membranes, inflatables, shells, gridshells). Multi-physics simulation (structural + fabrication constraints simultaneously). Real-time manipulation. Custom goal creation via C# scripting.

**Limitations**: Not a verified FEA tool. Cannot produce code-compliant stress results. Approximate stiffness (no rigorous element formulations). Not suitable for final structural verification.

**Integration**: Native Grasshopper component. Kangaroo 2 is the current version (position-based dynamics). Works with any mesh or line network. Combined with Weaverbird, Mesh+, Lunchbox for mesh processing.

**Learning curve**: Low-to-moderate. Very intuitive for form-finding. Advanced use (custom goals, coupled simulations) requires deeper understanding.

**Typical workflow**: Create mesh/network -> assign goals (springs, loads, anchors, constraints) -> run solver -> extract equilibrium geometry -> refine.

#### 8.3 Millipede (Grasshopper)

**Capabilities**: Topology optimization (2D and 3D SIMP-like method). FEA for 2D and 3D solid domains. Iso-surface extraction (marching cubes). Very fast computation using parallelized C++ backend.

**Limitations**: Limited to voxel-based analysis (regular grid). No beam or shell elements. Mesh refinement limited by voxel resolution and RAM. Limited post-processing tools.

**Integration**: Grasshopper plugin. Outputs iso-surfaces or voxel densities. Can be combined with Weaverbird for mesh smoothing, Dendro for SDF operations.

**Learning curve**: Low for basic topology optimization. Understanding of FEA fundamentals needed for meaningful results.

**Typical workflow**: Define domain (box) -> set resolution -> apply loads and supports -> define volume fraction -> run optimization -> extract iso-surface -> smooth -> verify.

#### 8.4 Ameba (Grasshopper)

**Capabilities**: BESO-based topology optimization. Clear black/white results (no gray elements). 2D and 3D. Multiple load cases. Displacement constraints. Stress visualization.

**Limitations**: Slower than Millipede (BESO is iterative FEA, not sensitivity-based). Can be mesh-sensitive. Limited to linear elastic analysis.

**Integration**: Grasshopper plugin. Similar workflow to Millipede but with BESO algorithm.

**Learning curve**: Low-to-moderate. Good documentation.

#### 8.5 SAP2000 / ETABS (CSI)

Professional-grade FEA with full linear/nonlinear analysis, seismic (response spectrum, time-history, pushover), and automated code-based design checks (Eurocode, ASCE, ACI, AISC). GUI-centric but has OAPI for scripted automation (C#, VB, Python via COM). Grasshopper links via Geometry Gym. ETABS is building-specific; SAP2000 is general-purpose. High learning curve.

#### 8.6 RFEM / RSTAB (Dlubal)

Professional FEA with excellent shell/solid capabilities and extensive code-checking modules (steel, concrete, timber per Eurocode, ASCE, DIN). Built-in topology optimization and form-finding. Grasshopper link via parametric_FEM-Toolbox. Python API (RFEM 6). IFC/Revit integration. Expensive per-module licensing.

#### 8.7 SOFiSTiK

Specialized for bridges and complex structures. Parametric input language (CADINP) for scripted models. Excellent nonlinear and construction-stage analysis. Grasshopper interface available. Very high learning curve but unmatched for bridge engineering.

#### 8.8 Robot Structural Analysis (Autodesk)

General-purpose FEA with steel/concrete/timber design. Direct bidirectional Revit link. Cloud analysis. Dynamo scripting. Less capable than SAP2000/RFEM for advanced nonlinear/seismic analysis but well-priced for Autodesk subscribers.

#### Tool Comparison Summary

| Feature | Karamba3D | Kangaroo | Millipede | SAP2000 | RFEM | SOFiSTiK | Robot |
|---|---|---|---|---|---|---|---|
| Early design | Excellent | Excellent | Good | Poor | Fair | Poor | Fair |
| Form-finding | Good | Excellent | - | Fair | Good | Good | - |
| Topology opt | - | - | Excellent | - | Good | - | - |
| Code checking | Manual | - | - | Excellent | Excellent | Excellent | Good |
| Seismic | Basic | - | - | Excellent | Excellent | Good | Good |
| Parametric | Excellent | Excellent | Good | Via API | Via API/GH | Via CADINP | Via Dynamo |
| Real-time | Yes | Yes | Near | No | No | No | No |
| Cost | ~800 EUR | Free | Free | ~5000 USD | ~3000 EUR | ~5000 EUR | Subscription |

---

### 9. Worked Examples

#### Example 1: Simple Truss Optimization

**Problem**: Planar truss spanning 12m, central point load 100 kN, depth limited to 3m. Minimize weight in S355 steel.

**Tool chain**: Grasshopper + Karamba3D + Galapagos

**Setup**: Ground structure (7x3 node grid, fully connected) -> pin/roller supports -> cross-section areas as design variables (100-5000 mm^2) -> minimize total weight -> stress constraint (fy = 355 MPa) + Euler buckling check.

**Result**: Optimal topology resembles a Warren truss with ~45-degree diagonals. Members with near-zero area removed. Total weight 60-70% of initial. Verify: all utilization ratios < 1.0, max deflection < L/250 = 48mm.

#### Example 2: Shell Form-Finding (Funicular Dome)

**Problem**: Compression-only dome, circular boundary R = 15m, concrete shell t = 100mm.

**Tool chain**: Rhino + Grasshopper + Kangaroo Physics

**Setup**: Flat triangulated mesh (~500 faces) -> Anchor goals (boundary at z=0, strength 10000) -> Load goals (self-weight per tributary area) -> Length goals (force density q controls rise) -> run solver to convergence.

**Key parameter**: Force density q controls rise-to-span. Higher q = shallower dome. Iterate to achieve desired rise (e.g., 7.5m). The funicular shape under self-weight approximates a catenary of revolution.

**Verification**: Karamba3D shell analysis confirms dominant membrane compression, utilization < 0.3. Eigenvalue buckling safety factor > 5. Ring beam sized for horizontal thrust H = wR^2/(2z).

#### Example 3: Topology Optimization of a Structural Node

**Problem**: Steel node connecting four tubes at spatial angles. Minimize weight for 3D printing.

**Tool chain**: Grasshopper + Millipede

**Setup**: 400mm cube design domain -> non-design cylinders at tube entries (50mm solid for welding) -> 3 load cases (gravity, wind, uplift) with weights (0.5, 0.3, 0.2) -> volume fraction 15% -> resolution 80^3 voxels -> filter radius 3 voxels -> p = 3.

**Result**: Material concentrates along principal stress paths (organic, bone-like branching). Extract iso-surface at threshold 0.3-0.5, smooth with Taubin smoothing. Verify: max von Mises < fy/1.5 = 237 MPa. Export STL for SLM/DMLS printing. Weight saving: 40-75% vs. conventional welded node.

---

### References and Further Reading

1. Block, P., Lachauer, L., & Rippmann, M. (2014). *Shell Structures for Architecture: Form Finding and Optimization*. Routledge.
2. Adriaenssens, S., Block, P., Veenendaal, D., & Williams, C. (2014). *Shell Structures for Architecture: Form Finding and Optimization*. Routledge.
3. Bendsoe, M. P., & Sigmund, O. (2003). *Topology Optimization: Theory, Methods and Applications*. Springer.
4. Preisinger, C. (2013). "Linking Structure and Parametric Geometry." *Architectural Design*, 83(2), 110-113. (Karamba3D)
5. Piker, D. (2013). "Kangaroo: Form Finding with Computational Physics." *Architectural Design*, 83(2), 136-137.
6. Schek, H.-J. (1974). "The Force Density Method for Form Finding and Computation of General Networks." *Computer Methods in Applied Mechanics and Engineering*, 3(1), 115-134.
7. Bletzinger, K.-U., & Ramm, E. (1999). "A General Finite Element Approach to the Form Finding of Tensile Structures by the Updated Reference Strategy." *International Journal of Space Structures*, 14(2), 131-145.
8. Sigmund, O., & Maute, K. (2013). "Topology optimization approaches." *Structural and Multidisciplinary Optimization*, 48(6), 1031-1055.


## environmental-simulation

### Environmental Simulation

> Daylight analysis, solar radiation, energy simulation, CFD wind analysis, thermal comfort, acoustic simulation, and the Ladybug Tools ecosystem for performance-driven AEC computational design

## Environmental Simulation for AEC Computational Design

This skill provides a comprehensive reference for environmental performance simulation
in the Architecture, Engineering, and Construction industry. It covers daylight analysis,
solar radiation studies, energy modeling, computational fluid dynamics for wind, thermal
comfort assessment, acoustic simulation, and the Ladybug Tools ecosystem that ties these
workflows together within parametric design environments.

---

### 1. Performance-Driven Design Philosophy

#### Why Simulate Early

The single most consequential decision in building performance is made in the first
five percent of the design timeline. Orientation, massing, window-to-wall ratio, and
floor plate depth are locked in during concept design, yet their impact on energy
consumption, daylight quality, and occupant comfort persists for the entire operational
life of the building — typically 50 to 100 years.

Late-stage simulation is a diagnostic exercise. Early-stage simulation is a generative
tool. The distinction matters because retrofitting performance into an already-resolved
form is orders of magnitude more expensive than shaping the form around performance
from the beginning.

**Cost of late performance analysis:**

| Stage where issue discovered | Relative cost to fix |
|------------------------------|---------------------|
| Concept design               | 1x (baseline)       |
| Schematic design              | 5x                  |
| Design development            | 15x                 |
| Construction documents        | 50x                 |
| Construction                  | 150x                |
| Post-occupancy                | 500x+               |

These multipliers are well-documented across the AEC industry and reflect the reality
that changing a window-to-wall ratio on a sketch costs nothing, but changing it after
curtain wall shop drawings are issued can cost hundreds of thousands of dollars.

#### Integration of Simulation into the Design Loop

Performance simulation must not live in a separate silo from the design model. The
traditional workflow — architect designs, sends model to energy consultant, waits two
weeks, receives PDF report, ignores half the recommendations because they conflict
with the architectural intent — is fundamentally broken.

The correct workflow is a tight feedback loop:

1. **Parametric model** defines geometry with variable parameters (orientation, WWR,
   floor depth, shading depth, envelope composition).
2. **Simulation engine** evaluates one or more performance metrics against that geometry.
3. **Results** feed back into the model as color-mapped surfaces, numeric dashboards,
   or fitness values for optimization.
4. **Designer** adjusts parameters or launches an automated optimization run.
5. **Repeat** at increasing fidelity as the design matures.

This loop should complete in seconds to minutes during early design and in minutes to
hours during detailed design. Any simulation that takes days to return results is, by
definition, excluded from the design loop and relegated to post-rationalization.

#### Performance as a Design Driver

Performance-driven design does not mean surrendering architectural intent to a
spreadsheet. It means treating environmental performance as a first-class design
variable alongside spatial quality, structural logic, and aesthetic expression. The
best performing buildings in the world — the Bullitt Center, One Angel Court, the
Manitoba Hydro Place — are also among the most architecturally compelling because their
designers used performance constraints as creative catalysts.

Metrics that can drive design decisions:

- **Daylight autonomy** drives floor plate depth, section profile, and facade design.
- **Solar radiation** drives orientation, massing articulation, and shading strategy.
- **Energy use intensity** drives envelope specification, HVAC selection, and renewable capacity.
- **Wind comfort** drives podium design, canopy placement, and landscape strategy.
- **Thermal comfort** drives material selection, ventilation strategy, and public realm design.
- **Acoustic performance** drives room proportions, material specification, and partition layout.

#### Iterative vs. Single-Pass Simulation Strategies

**Single-pass simulation** runs one analysis on a fixed design. It answers the question
"how does this design perform?" This is the minimum viable use of simulation and is
appropriate only for compliance checking at the end of a design phase.

**Iterative simulation** runs multiple analyses across a parameter space. It answers the
question "which design performs best?" This is the correct use of simulation in a
computational design workflow.

Iterative strategies include:

- **Manual parameter sweeps**: Designer changes one variable at a time and observes the
  effect on performance. Simple but slow and unable to capture multi-variable interactions.
- **Parametric studies**: Systematic variation of two or three parameters across defined
  ranges, producing a response surface that reveals optimal regions.
- **Evolutionary optimization**: Genetic algorithms (Galapagos, Wallacei) explore a
  high-dimensional parameter space, evolving toward Pareto-optimal solutions across
  multiple conflicting objectives.
- **Machine learning surrogates**: A neural network is trained on a sample of simulation
  results and then used to predict performance across the full parameter space at near
  zero computational cost. This enables real-time performance feedback during design.

---

### 2. Daylight Analysis

#### Core Metrics

**Daylight Factor (DF)**
The ratio of indoor illuminance to outdoor diffuse horizontal illuminance under a CIE
overcast sky, expressed as a percentage. DF is climate-independent and therefore useful
for comparing designs but not for predicting actual illuminance.

- Minimum DF of 2% is generally required for a space to be considered "daylit."
- Average DF of 5% or more indicates strong daylight availability.
- DF does not account for direct sunlight, building orientation, or climate.

**Spatial Daylight Autonomy (sDA)**
The percentage of analysis area that achieves at least 300 lux for at least 50% of
occupied hours annually. sDA is the primary metric in LEED v4.1 and IES LM-83.

- sDA300/50% >= 55% is the LEED threshold for 2 points.
- sDA300/50% >= 75% earns 3 points.
- Based on annual simulation with climate-specific weather data.
- Accounts for orientation, context, and dynamic shading.

**Annual Sunlight Exposure (ASE)**
The percentage of analysis area that receives more than 1000 lux of direct sunlight
for more than 250 occupied hours per year. ASE measures visual discomfort risk from
excessive direct sun.

- ASE1000/250h must be <= 10% for LEED compliance.
- High ASE indicates glare risk and potential overheating.
- ASE is often in tension with sDA — maximizing daylight can increase glare risk.

**Useful Daylight Illuminance (UDI)**
The percentage of occupied hours that illuminance falls within a useful range:

| UDI category          | Illuminance range | Interpretation           |
|-----------------------|-------------------|--------------------------|
| UDI-fell-short        | < 100 lux         | Too dark, electric light needed |
| UDI-supplementary     | 100–300 lux       | Useful with supplemental light |
| UDI-autonomous        | 300–3000 lux      | Ideal daylight range     |
| UDI-exceeded          | > 3000 lux        | Too bright, glare likely |

UDI is more nuanced than sDA because it penalizes both under-lit and over-lit conditions.

**Daylight Glare Probability (DGP)**
A metric for evaluating glare from a specific viewpoint, based on luminance distribution
in the field of view.

| DGP value   | Glare perception       |
|-------------|------------------------|
| < 0.35      | Imperceptible          |
| 0.35–0.40   | Perceptible            |
| 0.40–0.45   | Disturbing             |
| > 0.45      | Intolerable            |

DGP is evaluated using Evalglare from the Radiance suite and requires a rendered
fisheye luminance image from the occupant's viewpoint.

#### Standards Reference

**LEED v4.1 IEQ Credit: Daylight**
- Option 1 (Simulation): sDA300/50% >= 55% in 55% of regularly occupied area (2 pts),
  >= 75% (3 pts). ASE1000/250h <= 10%. Analysis grid at workplane height (0.76 m).
- Option 2 (Measurement): Illuminance between 300–3000 lux at 9 AM and 3 PM on equinox.

**EN 17037: Daylight in Buildings**
- Target illuminance of 300 lux for 50% of daylight hours at the worst point.
- Minimum illuminance of 100 lux for 50% of daylight hours across 95% of area.
- Recommends evaluation of view out, sunlight exposure, and glare protection.

**BREEAM Hea 01: Visual Comfort**
- Average daylight factor >= 2% or point daylight factor >= 0.8% at the worst point.
- Uniformity ratio (minimum DF / average DF) >= 0.4.
- View of sky from desk height (requirement for higher credits).

#### Simulation Engines

**Radiance**
The gold standard for physically-based lighting simulation. Uses backward ray-tracing
to compute illuminance and luminance with high accuracy. All major daylight standards
reference Radiance as a validated engine.

Key Radiance parameters for annual simulation:

| Parameter   | Low quality | Medium quality | High quality |
|-------------|-------------|----------------|--------------|
| -ab (bounces)| 2          | 3              | 5            |
| -ad (divisions)| 512      | 2048           | 4096         |
| -as (super-samples)| 128  | 1024           | 2048         |
| -ar (resolution)| 64      | 128            | 256          |
| -aa (accuracy)| 0.25      | 0.15           | 0.1          |

**3-Phase Method**
Decomposes daylight transport into three matrices:
1. View matrix (V): sensor points to interior surface patches
2. Transmission matrix (T): window group behavior
3. Daylight matrix (D): sky patches to exterior window surfaces

Annual daylight = V * T * D * sky_vector. This allows rapid recalculation when only
the window system changes (swap T matrix) without recomputing V or D.

**5-Phase Method**
Adds direct solar contribution more accurately by separating the direct sun component
from the diffuse sky component and computing it with higher resolution. Essential for
accurate ASE calculations and glare analysis.

#### Material Properties

Common material reflectances for Radiance modeling:

| Material                | Reflectance | Specularity | Roughness |
|-------------------------|-------------|-------------|-----------|
| White painted wall       | 0.70        | 0.0         | 0.0       |
| Light grey painted wall  | 0.50        | 0.0         | 0.0       |
| Dark grey painted wall   | 0.20        | 0.0         | 0.0       |
| Concrete (raw)           | 0.30        | 0.0         | 0.05      |
| Wood flooring (light)    | 0.40        | 0.02        | 0.02      |
| Carpet (medium)          | 0.20        | 0.0         | 0.0       |
| Ceiling tile (white)     | 0.80        | 0.0         | 0.0       |
| Glass (clear single)     | Tvis: 0.88  | —           | —         |
| Glass (clear double)     | Tvis: 0.78  | —           | —         |
| Glass (low-e double)     | Tvis: 0.65  | —           | —         |
| Ground (grass)           | 0.20        | 0.0         | 0.0       |
| Ground (asphalt)         | 0.10        | 0.0         | 0.0       |
| Ground (concrete paving) | 0.30        | 0.0         | 0.0       |
| Red brick                | 0.25        | 0.0         | 0.03      |
| Aluminum (brushed)       | 0.60        | 0.50        | 0.05      |

#### Grid-Based vs. Point-in-Time Analysis

**Grid-based analysis** places sensors at regular intervals across a horizontal workplane
(typically 0.76 m above floor for offices, 0.85 m for standing desks). Grid spacing
should be no larger than 0.5 m for final analysis and no larger than 1.0 m for early
design studies. Results are spatial maps showing illuminance distribution.

**Point-in-time analysis** evaluates illuminance or luminance at a specific moment
(date, time, sky condition). Useful for worst-case glare checks (e.g., December 21
at 3 PM with low sun angle) or for visualizing light distribution at critical moments.

#### Parametric Daylight Optimization Workflow

1. Define variable parameters: window-to-wall ratio (20–80%), window sill height,
   head height, external shading depth (0–1.5 m), light shelf depth, room depth.
2. Set up Honeybee model with Radiance modifiers for all surfaces.
3. Run annual daylight simulation (Honeybee-Radiance recipe).
4. Extract sDA, ASE, and UDI from results.
5. Feed metrics into multi-objective optimizer (Wallacei recommended).
6. Objectives: maximize sDA, minimize ASE, minimize facade cost.
7. Analyze Pareto front to select design variants that balance performance and cost.

#### Common Modeling Mistakes

- **Missing context buildings**: Omitting neighboring buildings that cast shadows leads
  to dramatically overstated daylight predictions. Always include context within at
  least 200 m radius for urban sites.
- **Wrong material reflectance**: Using default white (0.50) for all surfaces when
  actual materials are much darker (0.20–0.30) can overpredict daylight by 30–50%.
- **Insufficient grid resolution**: A 2 m grid misses spatial variation entirely. Use
  0.5 m maximum for compliance analysis.
- **Ignoring furniture**: Large obstructions like tall storage units significantly
  affect daylight distribution in deep plans.
- **Wrong analysis period**: Using calendar year instead of occupied hours misrepresents
  sDA values. Always define occupancy schedule correctly.
- **Not modeling window frames**: Frames reduce glazed area by 15–30%. Omitting them
  overpredicts daylight proportionally.

---

### 3. Solar Radiation Analysis

#### Solar Geometry

The position of the sun is defined by two angles:

- **Altitude (elevation)**: Angle above the horizon (0° at horizon, 90° at zenith).
- **Azimuth**: Angle measured clockwise from true north (0° = N, 90° = E, 180° = S, 270° = W).

Solar position depends on latitude, longitude, date, and time. Key concepts:

- **Solar noon**: The moment the sun crosses the local meridian (highest altitude).
- **Equation of time**: Correction for the difference between solar time and clock
  time due to Earth's elliptical orbit and axial tilt. Varies by +/- 16 minutes.
- **Declination**: The angle between the sun's rays and the equatorial plane. Ranges
  from +23.45° (summer solstice) to -23.45° (winter solstice).
- **Hour angle**: Angular displacement of the sun from solar noon. 15° per hour.

#### Solar Radiation Components

| Component   | Source                           | Behavior           | Typical share (annual) |
|-------------|----------------------------------|---------------------|----------------------|
| Direct beam | Sun disk                         | Casts sharp shadows | 50–70%               |
| Diffuse     | Sky vault (scattered by atmosphere)| Uniform, no shadows| 25–40%               |
| Reflected   | Ground and surrounding surfaces  | Depends on albedo   | 5–15%                |

Total solar radiation (global) = direct + diffuse + reflected.

#### Radiation Analysis Types

**Cumulative annual radiation**: Total solar energy received by a surface over an
entire year, measured in kWh/m². This is the most common analysis for facade studies
and PV potential assessment. Typical values for a horizontal surface range from
900 kWh/m²/yr (northern Europe) to 2200 kWh/m²/yr (desert regions).

**Monthly radiation**: Breakdown of annual radiation by month, revealing seasonal
patterns. Critical for understanding heating vs. cooling season dynamics.

**Hourly radiation**: Instantaneous radiation values for specific hours, used for
peak load calculations and shadow studies.

#### Solar Access Hours

Solar access analysis counts the number of hours per year (or per day for a specific
date) that a point receives direct sunlight. Used for:

- Right-to-light assessments (UK planning requirement: 2+ hours on March 21).
- BRE Site Layout Planning guidelines (25+ hours on March 21 for outdoor amenity).
- Passive solar design (minimum 4 hours winter solstice for south-facing facades).

#### Shadow Range Analysis

Shadow range diagrams overlay all shadow positions for a specific date or period,
showing which areas are always in shade, always in sun, or intermittently shaded.
Useful for:

- Public space design (ensuring benches get winter sun).
- Urban planning (assessing impact of new tall buildings on surrounding neighborhoods).
- PV array siting (avoiding partially shaded zones).

#### Radiation on Tilted Surfaces

Radiation on a tilted surface differs from horizontal radiation. The optimal tilt
angle for annual energy collection is approximately equal to the site latitude. For
winter-optimized collection, add 15° to latitude. For summer-optimized, subtract 15°.

Isotropic sky model: Diffuse radiation is uniform across the sky dome. Simple but
inaccurate — underestimates radiation near the horizon and circumsolar region.

Perez all-weather model: Divides the sky into circumsolar, horizon brightening, and
isotropic components. Most accurate model for tilted surface calculations.

#### PV Potential Assessment

1. Calculate annual radiation on candidate surfaces (roof, facade, canopy).
2. Subtract shading losses from context geometry and self-shading.
3. Apply panel efficiency (monocrystalline: 20–22%, polycrystalline: 16–18%, thin-film: 10–13%).
4. Apply system losses (inverter: 3–5%, wiring: 2–3%, soiling: 2–5%, temperature: 5–10%).
5. Result: annual energy yield in kWh per panel or per m².

Typical yield: 150–200 kWh/m²/yr in northern Europe, 250–350 kWh/m²/yr in southern
US and Middle East.

#### Sky Models

| Sky model       | Use case                     | Characteristics                        |
|-----------------|------------------------------|----------------------------------------|
| CIE overcast    | Daylight factor calculation  | Luminance varies only with altitude     |
| CIE clear       | Sunny day analysis           | Includes circumsolar and horizon zones  |
| CIE intermediate| Partly cloudy conditions     | Blend of clear and overcast             |
| Perez all-weather| Annual simulation           | Uses weather data, most accurate        |
| Uniform         | Simple diffuse analysis      | Equal luminance everywhere (unrealistic)|

#### EPW Weather Files

EPW (EnergyPlus Weather) files contain hourly data for a typical meteorological year:

- Dry bulb temperature, dew point temperature, relative humidity
- Direct normal radiation, diffuse horizontal radiation, global horizontal radiation
- Wind speed, wind direction
- Atmospheric pressure, sky cover, precipitation

**Sources**: EnergyPlus.net, Climate.OneBuilding.org (most comprehensive), ASHRAE IWEC2,
Meteonorm (commercial, can generate for any location).

**TMY methodology**: Typical Meteorological Year data is constructed by selecting the
most representative month from a 15–30 year record for each calendar month. TMY data
represents typical conditions, not extreme conditions. For resilience analysis, use
actual year data or future climate projections.

---

### 4. Energy Simulation

#### Building Energy Model Components

A complete building energy model requires the following layers:

1. **Geometry**: Thermal zones defined by enclosed volumes. Each zone has a single
   air temperature assumption. Zones should be separated where significantly different
   thermal conditions exist (perimeter vs. core, different orientations, different uses).

2. **Constructions**: Material layers for each opaque surface (walls, roofs, floors)
   and glazing properties for windows. Each layer defined by thickness, conductivity,
   density, and specific heat.

3. **Schedules**: Hourly profiles for occupancy, lighting, equipment, thermostat
   setpoints, HVAC availability, and ventilation rates. Schedules are the single most
   influential input in energy modeling after geometry.

4. **Internal loads**: Heat gains from people (sensible + latent), lighting, and
   equipment. Specified as peak values modulated by schedules.

5. **HVAC systems**: Heating, cooling, and ventilation equipment. Ranges from
   ideal air (unlimited capacity, perfect efficiency — for early design) to fully
   detailed systems with specific equipment curves.

6. **Infiltration**: Uncontrolled air leakage through the envelope. Specified as
   ACH (air changes per hour) or flow per unit envelope area.

7. **Natural ventilation**: Window opening behavior, stack effect, wind-driven
   ventilation. Can be modeled as scheduled or as airflow network.

#### EnergyPlus Engine Fundamentals

EnergyPlus is a whole-building energy simulation engine developed by the US Department
of Energy. It uses a heat-balance method that simultaneously solves:

- Conduction through opaque surfaces (conduction transfer functions)
- Solar radiation through windows (detailed optical calculations)
- Internal convection (TARP algorithm)
- Longwave radiation exchange between surfaces
- Air heat balance (zone energy balance)
- HVAC system response

EnergyPlus runs sub-hourly timesteps (typically 6 per hour = 10-minute intervals)
with weather data interpolated from hourly EPW values.

#### Honeybee-Energy Workflow

1. **Create rooms**: Define thermal zone geometry from Rhino surfaces or procedural
   generation. Each room = one thermal zone.
2. **Assign program types**: Predefined combinations of loads, schedules, and setpoints
   for common space types (office, residential, retail, etc.).
3. **Set construction sets**: Climate-appropriate envelope specifications. Honeybee
   includes ASHRAE baseline construction sets by climate zone.
4. **Define HVAC**: Start with IdealAirSystem for early design. Progress to detailed
   systems (VAV, VRF, DOAS, radiant) for later stages.
5. **Set simulation parameters**: Run period, timestep, terrain, solar distribution.
6. **Run simulation**: Honeybee generates IDF file and calls EnergyPlus.
7. **Parse results**: Monthly/annual energy by end use, zone temperatures, comfort hours.

#### Key Outputs

**Energy Use Intensity (EUI)**
Total annual energy consumption divided by gross floor area, measured in kWh/m²/yr
(or kBtu/ft²/yr in US practice). EUI is the primary benchmark for building energy
performance.

| Building type      | Good EUI (kWh/m²/yr) | Average EUI | Poor EUI |
|--------------------|-----------------------|-------------|----------|
| Office             | 80–120                | 150–200     | 250+     |
| Residential (apt)  | 50–80                 | 100–140     | 180+     |
| Retail             | 100–150               | 200–280     | 350+     |
| Education          | 70–110                | 130–170     | 220+     |
| Hospital           | 200–300               | 350–450     | 550+     |
| Hotel              | 120–180               | 220–300     | 400+     |
| Laboratory         | 250–400               | 500–700     | 900+     |
| Warehouse          | 30–50                 | 60–100      | 150+     |

**Heating/Cooling Loads**
Annual energy required for space heating and cooling, broken down monthly. The ratio
of heating to cooling reveals the building's dominant load and guides passive strategy
selection.

**Peak Loads**
Maximum instantaneous heating and cooling demand, measured in kW or W/m². Peak loads
size the HVAC equipment. Reducing peak loads through passive design (thermal mass,
shading, high-performance envelope) allows smaller, less expensive mechanical systems.

#### Early-Stage Energy Estimation

For concept design, full EnergyPlus simulation may be premature. Simplified methods:

- **Degree-day method**: Estimate heating/cooling energy from HDD/CDD and envelope
  UA-value. Fast but ignores solar gains, internal gains, and thermal mass.
- **Lookup tables**: Reference EUI values from benchmarking databases (CBECS, CIBSE
  TM46, EU building typologies) adjusted for climate and building features.
- **Shoebox models**: Single-zone energy models representing a typical floor section.
  Capture the essential physics in 1% of the modeling effort.
- **Regression surrogates**: Train a model on thousands of EnergyPlus runs, then
  predict EUI from a handful of input parameters in milliseconds.

#### Parametric Energy Optimization

Key parameters for early-stage energy optimization:

| Parameter          | Typical range     | Impact on EUI          |
|--------------------|-------------------|------------------------|
| Orientation        | 0–360°            | 5–15% (climate-dependent)|
| WWR (north)        | 15–60%            | 5–20%                  |
| WWR (south)        | 15–60%            | 10–30%                 |
| WWR (east/west)    | 15–40%            | 10–25%                 |
| Wall U-value       | 0.15–0.50 W/m²K   | 5–15%                  |
| Roof U-value       | 0.10–0.30 W/m²K   | 3–10%                  |
| Glazing U-value    | 0.8–3.0 W/m²K     | 5–20%                  |
| Glazing SHGC       | 0.20–0.60         | 10–25%                 |
| Shading depth      | 0–2.0 m           | 5–15%                  |
| Infiltration rate  | 0.1–1.0 ACH       | 5–15%                  |
| Lighting power     | 4–12 W/m²         | 10–20%                 |

#### Passive Design Strategies Validated by Simulation

- **Orientation**: Long axis east-west maximizes southern exposure (northern hemisphere),
  improving winter solar gain while allowing effective summer shading.
- **Thermal mass**: Exposed concrete soffits absorb daytime gains and release heat
  at night, reducing peak cooling loads by 10–20%.
- **Night purge ventilation**: Flushing the building with cool night air pre-cools
  thermal mass, shifting cooling loads and reducing HVAC energy by 15–30%.
- **External shading**: Horizontal overhangs on south, vertical fins on east/west.
  Fixed shading design derived from sun path analysis.
- **High-performance glazing**: Triple glazing with low-e coatings (U < 1.0 W/m²K,
  SHGC 0.25–0.40) dramatically reduces both heating and cooling loads.
- **Daylighting with dimming**: Photosensor-controlled dimming of electric lights in
  daylit zones reduces lighting energy by 40–60%.

---

### 5. CFD Wind Analysis

#### Outdoor Wind Comfort — Lawson Criteria

The Lawson comfort criteria classify wind conditions by acceptable activity:

| Category          | Mean wind speed threshold | Gust equivalent | Acceptable activity       |
|-------------------|--------------------------|-----------------|---------------------------|
| Sitting (long)    | < 2.5 m/s                | < 4.0 m/s       | Outdoor dining, reading   |
| Sitting (short)   | < 4.0 m/s                | < 6.0 m/s       | Bus stops, café terraces  |
| Standing          | < 6.0 m/s                | < 8.0 m/s       | Window shopping, waiting  |
| Walking (leisure) | < 8.0 m/s                | < 10.0 m/s      | Strolling, walking routes |
| Business walking  | < 10.0 m/s               | < 12.0 m/s      | Walking to work, commuting|
| Uncomfortable     | 10–15 m/s                | 12–18 m/s       | Hair disturbed, clothing flaps|
| Dangerous         | > 15 m/s                 | > 20 m/s        | Structural damage risk    |

Wind comfort is typically assessed at pedestrian level (1.5 m above ground) for the
annual wind climate, reporting the worst-season or annual probability of exceedance.

#### Computational Wind Tunnel Setup

**Domain sizing rules** (H = tallest building height):

| Boundary           | Distance from buildings | Rationale                           |
|--------------------|------------------------|-------------------------------------|
| Inlet              | 5H upstream            | Allow boundary layer to develop     |
| Outlet             | 15H downstream         | Allow wake to dissipate             |
| Lateral walls      | 5H from edge of model  | Prevent blockage effects (< 3%)     |
| Top                | 5H above tallest point | Prevent artificial acceleration     |

**Blockage ratio** (frontal area of buildings / domain cross-section) must be < 3%.
Higher blockage artificially accelerates flow around buildings.

**Mesh resolution guidelines**:

| Region                        | Cell size          |
|-------------------------------|--------------------|
| Near building surfaces        | 0.5–1.0 m         |
| Pedestrian level (0–3 m)      | 0.5–1.0 m         |
| Near-field (within 2H)        | 1.0–3.0 m         |
| Far-field (beyond 2H)         | 3.0–10.0 m        |
| Boundary layer refinement     | First cell < 0.5 m|

Total cell count for a typical urban study: 2–10 million cells.

#### Turbulence Models

**RANS (Reynolds-Averaged Navier-Stokes)**: Time-averaged equations with turbulence
closure models. Solves for mean flow quantities. Computationally affordable.

| Model              | Strengths                          | Weaknesses                    | Use case              |
|--------------------|------------------------------------|-------------------------------|-----------------------|
| Standard k-epsilon | Robust, well-validated             | Poor for separation, wakes    | Initial screening     |
| Realizable k-epsilon| Better for recirculation          | Still struggles with anisotropy| General urban studies |
| k-omega SST        | Excellent near-wall, good separation| Higher cost than k-epsilon  | Detailed pedestrian comfort|
| Spalart-Allmaras   | Low cost, good for attached flow   | Poor for complex urban geometry| Aerospace, not urban  |

**LES (Large Eddy Simulation)**: Resolves large-scale turbulent structures directly,
models only the smallest scales. Much more accurate for urban flows but 100–1000x
more expensive than RANS. Reserved for research and critical safety assessments.

#### Butterfly (OpenFOAM for Grasshopper) Workflow

1. Create geometry in Rhino/Grasshopper (buildings as closed Breps).
2. Define wind tunnel (domain) using Butterfly components.
3. Set inlet boundary condition: atmospheric boundary layer profile with reference
   wind speed, direction, roughness length (z0), and reference height.
4. Set mesh parameters: base cell size, refinement levels near buildings.
5. Select turbulence model (k-epsilon or k-omega SST).
6. Run snappyHexMesh for mesh generation.
7. Run simpleFoam (steady-state RANS solver).
8. Post-process: extract wind speed at 1.5 m height plane, map to Lawson categories.

#### Simplified Wind Analysis for Early Design

Full CFD is expensive and time-consuming. For early design, use:

- **Desktop wind assessment**: Classify building form using standard typologies
  (slab, tower, podium-tower, courtyard) and apply known wind behavior patterns.
- **Wind comfort rules of thumb**: Tall buildings create downwash proportional to
  their height. Corner acceleration increases with building width. Through-building
  passages create venturi effects.
- **Lawson screening tool**: Quick assessment based on building height, width, and
  surroundings without running CFD.
- **Reduced-order models**: Pre-computed wind pressure databases for simple shapes.

#### Natural Ventilation Potential

CFD can assess whether natural ventilation is viable:

- Calculate pressure coefficients (Cp) on building facades from wind simulation.
- Derive pressure difference between windward and leeward openings.
- Estimate ventilation flow rate: Q = Cd * A * sqrt(2 * dP / rho).
- Compare achieved air change rate against minimum ventilation requirements.

#### Wind-Driven Rain

Wind-driven rain analysis predicts wetting patterns on building facades:

- Combines rainfall intensity with wind speed and direction.
- Identifies facade zones at risk of water penetration.
- Informs material selection, detailing, and drainage design.
- Quantified as catch ratio: rain on vertical surface / rain on horizontal surface.

---

### 6. Thermal Comfort

#### Indoor Thermal Comfort

**PMV/PPD (Fanger Model)**
Predicted Mean Vote (PMV) is a steady-state thermal comfort index on a 7-point scale:

| PMV value | Thermal sensation |
|-----------|-------------------|
| -3        | Cold              |
| -2        | Cool              |
| -1        | Slightly cool     |
| 0         | Neutral           |
| +1        | Slightly warm     |
| +2        | Warm              |
| +3        | Hot               |

Predicted Percentage Dissatisfied (PPD) is derived from PMV. At PMV = 0, PPD = 5%
(some people are always dissatisfied). ASHRAE 55 requires -0.5 < PMV < +0.5 (PPD < 10%).

PMV inputs:
| Parameter              | Symbol | Typical indoor range    |
|------------------------|--------|-------------------------|
| Air temperature        | Ta     | 18–28°C                 |
| Mean radiant temperature| Tr    | 16–35°C                 |
| Air speed              | Va     | 0.05–0.5 m/s            |
| Relative humidity      | RH     | 30–70%                  |
| Metabolic rate         | Met    | 1.0–2.0 met (office: 1.1)|
| Clothing insulation    | Clo    | 0.5–1.5 clo             |

**Adaptive Model**
For naturally ventilated buildings, the adaptive model (ASHRAE 55 Section 5.4, EN 15251)
defines acceptable indoor temperature as a function of outdoor running mean temperature.

Acceptable operative temperature = 17.8 + 0.31 * outdoor running mean temperature
(80% acceptability band: +/- 3.5°C; 90% band: +/- 2.5°C).

The adaptive model acknowledges that occupants in naturally ventilated buildings
tolerate wider temperature ranges because they have more control (opening windows,
adjusting clothing).

#### Outdoor Thermal Comfort

**Universal Thermal Climate Index (UTCI)**
An equivalent temperature that represents the physiological response of the human
body to the outdoor thermal environment.

| UTCI range (°C)  | Stress category           | Thermal perception |
|-------------------|---------------------------|--------------------|
| > 46              | Extreme heat stress       | Unbearable         |
| 38–46             | Very strong heat stress   | Very hot           |
| 32–38             | Strong heat stress        | Hot                |
| 26–32             | Moderate heat stress      | Warm               |
| 9–26              | No thermal stress         | Comfortable        |
| 0–9               | Slight cold stress        | Slightly cool      |
| -13–0             | Moderate cold stress      | Cool               |
| -27–(-13)         | Strong cold stress        | Cold               |
| -40–(-27)         | Very strong cold stress   | Very cold          |
| < -40             | Extreme cold stress       | Extreme cold       |

**Physiological Equivalent Temperature (PET)**
The air temperature at which the body's heat balance would be the same in a standard
indoor reference environment. More intuitive for non-specialists.

**Mean Radiant Temperature (MRT)**
The uniform temperature of an imaginary black enclosure that would result in the same
net radiation heat exchange as the actual environment. MRT is often the dominant factor
in outdoor comfort and is strongly influenced by:

- Direct solar radiation (sun exposure vs. shade)
- Longwave radiation from surrounding surfaces (hot pavement vs. vegetation)
- Sky view factor (open sky vs. enclosed courtyard)

MRT can be 20–30°C higher in direct sun than in shade. This is why shade trees and
canopies are the single most effective microclimate intervention in hot climates.

#### Microclimate Simulation Workflow

1. Model urban geometry (buildings, ground surfaces, vegetation).
2. Assign surface materials (albedo, emissivity, thermal admittance).
3. Set meteorological boundary conditions from EPW data.
4. Run coupled simulation: radiation (solar + longwave) + CFD (wind field) + energy
   balance (surface temperatures).
5. Calculate MRT at pedestrian height from radiation field.
6. Compute UTCI or PET at grid of points.
7. Map comfort categories spatially and temporally.

Tools: ENVI-met (most comprehensive urban microclimate tool), Ladybug Tools (MRT
and UTCI from weather data and simplified radiation), RayMan, SOLWEIG.

---

### 7. Acoustic Simulation

#### Room Acoustics Metrics

| Metric | Full name                     | Target (speech)    | Target (music)       |
|--------|-------------------------------|--------------------|----------------------|
| RT60   | Reverberation time (60 dB decay)| 0.4–0.8 s (office)| 1.5–2.5 s (concert) |
| EDT    | Early Decay Time              | ≈ RT60             | ≈ RT60 (uniform)     |
| C80    | Clarity (ratio early/late)    | —                  | -2 to +4 dB          |
| D50    | Definition (early/total ratio)| > 0.50             | —                    |
| STI    | Speech Transmission Index     | > 0.60 (good)      | —                    |
| G      | Strength (dB re: 10 m free field)| —               | 0 to +10 dB          |

**RT60** is the most commonly specified acoustic metric. It depends on room volume
and total absorption:

Sabine equation: RT60 = 0.161 * V / A

Where V = room volume (m³) and A = total absorption (m² Sabins).

**Eyring equation** (more accurate for highly absorptive rooms):
RT60 = 0.161 * V / (-S * ln(1 - alpha_avg))

Where S = total surface area and alpha_avg = average absorption coefficient.

#### Material Absorption Coefficients

| Material                  | 125 Hz | 250 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz |
|---------------------------|--------|--------|--------|-------|-------|-------|
| Concrete (painted)         | 0.01   | 0.01   | 0.02   | 0.02  | 0.02  | 0.03  |
| Brick (unglazed)           | 0.03   | 0.03   | 0.03   | 0.04  | 0.05  | 0.07  |
| Plasterboard on studs      | 0.29   | 0.10   | 0.06   | 0.05  | 0.04  | 0.04  |
| Glass (window)             | 0.35   | 0.25   | 0.18   | 0.12  | 0.07  | 0.04  |
| Timber floor               | 0.15   | 0.11   | 0.10   | 0.07  | 0.06  | 0.07  |
| Carpet (heavy on pad)      | 0.08   | 0.24   | 0.57   | 0.69  | 0.71  | 0.73  |
| Acoustic ceiling tile      | 0.50   | 0.70   | 0.60   | 0.70  | 0.70  | 0.50  |
| Curtain (heavy, draped)    | 0.07   | 0.31   | 0.49   | 0.75  | 0.70  | 0.60  |
| Mineral wool (50 mm)       | 0.15   | 0.45   | 0.70   | 0.80  | 0.80  | 0.80  |
| Perforated metal + absorber| 0.40   | 0.70   | 0.80   | 0.85  | 0.75  | 0.65  |
| Upholstered seat (occupied)| 0.60   | 0.75   | 0.85   | 0.90  | 0.90  | 0.85  |
| Open doorway               | 1.00   | 1.00   | 1.00   | 1.00  | 1.00  | 1.00  |

#### Ray-Tracing Acoustic Simulation

**Pachyderm Acoustics** is a Grasshopper plugin for room acoustics simulation:

1. Define room geometry as closed meshes in Rhino.
2. Assign absorption and scattering coefficients to each surface.
3. Place source and receiver points.
4. Run ray-tracing simulation (10,000–100,000 rays).
5. Extract impulse response at each receiver.
6. Compute RT60, EDT, C80, D50, STI from impulse response.
7. Visualize sound pressure level distribution as color map.

#### Sound Insulation

**STC (Sound Transmission Class)**: Single-number rating for airborne sound insulation
of partitions (North American standard, ASTM E413).

| STC rating | Performance                                       |
|------------|---------------------------------------------------|
| 25         | Normal speech easily understood                    |
| 30         | Loud speech understood, normal speech audible      |
| 35         | Loud speech audible but not easily understood      |
| 40         | Loud speech audible as murmur                      |
| 45         | Loud speech not audible                            |
| 50         | Very loud sounds barely heard                      |
| 55+        | Most sounds inaudible                              |

**Rw (Weighted Sound Reduction Index)**: ISO equivalent of STC (ISO 717-1).

Typical constructions:
- Single plasterboard on studs: STC 33–38
- Double plasterboard on studs with insulation: STC 45–50
- Concrete block (200 mm): STC 45–50
- Concrete slab (200 mm): STC 50–55
- Double stud wall with resilient channels: STC 55–60

#### Outdoor Noise Propagation

Environmental noise from roads, railways, and aircraft is assessed using:

- **ISO 9613-2**: Attenuation of sound during outdoor propagation (geometric spreading,
  atmospheric absorption, ground effect, screening by barriers).
- **CNOSSOS-EU**: Harmonized European noise calculation method.
- **Distance attenuation**: Point source: -6 dB per doubling of distance. Line source
  (road): -3 dB per doubling of distance.
- **Barrier effect**: A solid barrier provides 5–15 dB insertion loss depending on
  path length difference.
- **Noise mapping**: Color-coded maps of facade or free-field noise levels, typically
  at 4 m height. Required for Environmental Impact Assessments.

---

### 8. Ladybug Tools Ecosystem

#### Overview

Ladybug Tools is an open-source collection of plugins for Grasshopper (Rhino) that
provides comprehensive environmental analysis capabilities for building and urban
design. It connects parametric geometry to validated simulation engines.

#### Ladybug (Weather Data and Outdoor Analysis)

Core capabilities:
- **EPW import and visualization**: Dry bulb temperature, radiation, wind, humidity
  as hourly heatmaps, bar charts, and statistical summaries.
- **Sun path diagram**: 3D stereographic or orthographic sun path with hourly sun
  positions, analemmas, and sun vectors for any location.
- **Wind rose**: Frequency and speed distribution by direction for any analysis period.
- **Radiation rose**: Directional radiation distribution for facade orientation studies.
- **Shadow study**: Calculate sunlight hours on test surfaces with context geometry.
- **Outdoor comfort**: UTCI, PET, and other outdoor comfort models from weather data.
- **Sky dome**: Visualize sky luminance/radiance distribution (Tregenza sky patches).
- **Direct sun hours**: Mesh-based analysis of solar access hours.
- **View analysis**: Assess visual exposure from points to targets.

#### Honeybee (Building Simulation)

**Honeybee-Radiance** (daylight):
- Create Radiance models from Grasshopper geometry.
- Assign material modifiers (plastic, glass, trans, BSDF).
- Define sensor grids and views.
- Run point-in-time illuminance, daylight factor, annual daylight (sDA/ASE/UDI).
- Glare analysis with Evalglare.
- Parametric blind/shade studies.

**Honeybee-Energy** (thermal/energy):
- Create thermal zones (rooms) from geometry.
- Assign program types (loads and schedules by space type).
- Define construction sets (opaque + glazing assemblies).
- Set HVAC systems (ideal air, detailed systems).
- Run EnergyPlus simulations.
- Parse results: energy by end use, zone temperatures, comfort.

Key Honeybee concepts:
- **Room**: A closed volume representing one thermal zone.
- **Face**: A planar surface bounding a room (wall, floor, roof/ceiling).
- **Aperture**: A window or skylight within a face.
- **Door**: An opaque or glass door within a face.
- **Shade**: An external shading surface (overhang, fin, context building).
- **Modifier**: Radiance material properties (reflectance, transmittance).
- **Construction**: Energy material layers (conductivity, density, specific heat).
- **ProgramType**: Combination of people, lighting, equipment, ventilation, setpoints.
- **ConstructionSet**: Collection of constructions for all face types.

#### Butterfly (CFD)

- Wraps OpenFOAM for use in Grasshopper.
- Creates computational domain (wind tunnel) around building geometry.
- Generates block-structured mesh with refinement regions.
- Sets boundary conditions (inlet velocity profile, outlet, walls).
- Runs steady-state RANS solver (simpleFoam).
- Extracts velocity and pressure fields for visualization.
- Current status: Less actively maintained than Ladybug/Honeybee. For production
  CFD work, consider standalone OpenFOAM or commercial tools.

#### Dragonfly (Urban Scale)

- **Urban weather generator (UWG)**: Modifies rural EPW data to account for urban
  heat island effect, producing urban-specific weather data.
- **District energy modeling**: Aggregates building energy models for neighborhood-scale
  analysis.
- **Urban geometry**: Creates building footprint extrusions from GIS data.
- **REopt integration**: Optimizes distributed energy resources (PV, storage, CHP).
- **Urban microclimate**: Couples with other tools for outdoor comfort mapping.

#### Version Compatibility

| Component         | Current version | Rhino compatibility | Python   |
|-------------------|-----------------|---------------------|----------|
| Ladybug           | 1.8.x           | Rhino 7, Rhino 8    | IronPython / CPython |
| Honeybee          | 1.8.x           | Rhino 7, Rhino 8    | IronPython / CPython |
| Honeybee-Radiance | 1.66.x          | Rhino 7, Rhino 8    | CPython 3.7+         |
| Honeybee-Energy   | 1.104.x         | Rhino 7, Rhino 8    | CPython 3.7+         |
| Butterfly         | 0.0.x           | Rhino 6, Rhino 7    | IronPython           |
| Dragonfly         | 1.8.x           | Rhino 7, Rhino 8    | CPython 3.7+         |

Note: Ladybug Tools 1.x (LBT) uses the Pollination installer, which manages
Radiance, EnergyPlus, and OpenStudio dependencies automatically.

#### Installation

1. Install Rhino 7 or 8.
2. Download Pollination Grasshopper installer from pollination.cloud.
3. Run installer — it sets up Ladybug Tools, Radiance 5.4+, EnergyPlus 23.1+,
   and OpenStudio 3.7+ automatically.
4. Alternatively, install from Food4Rhino and manually configure engine paths.
5. Verify installation: drop LB Versioner component on Grasshopper canvas.

#### Common Workflows

| Workflow                     | Components used                         | Engine   | Output                |
|------------------------------|-----------------------------------------|----------|-----------------------|
| Daylight factor              | HB Model, HB Modifier, HB Grid, HB DF  | Radiance | DF spatial map        |
| Annual daylight (sDA/ASE)    | HB Model, HB Annual Daylight            | Radiance | sDA, ASE percentages  |
| Point-in-time illuminance    | HB Model, HB Point-in-Time              | Radiance | Illuminance grid      |
| Glare analysis               | HB Model, HB Glare, Evalglare           | Radiance | DGP images            |
| Energy model (annual)        | HB Room, HB Program, HB Construction, HB Energy| EnergyPlus| EUI, loads, temps |
| Outdoor solar radiation      | LB Direct Sun Hours, LB Radiation       | Built-in | kWh/m² map            |
| Sun path + shadow study      | LB Sun Path, LB Shadow Study            | Built-in | Hours of sunlight     |
| Wind rose                    | LB Wind Rose                            | Built-in | Directional wind plot |
| Outdoor comfort (UTCI)       | LB UTCI, LB MRT                         | Built-in | UTCI spatial map      |
| Parametric optimization      | Above + Galapagos / Wallacei            | Various  | Pareto-optimal designs|

#### Integration with Optimization

**Galapagos** (single-objective): Built into Grasshopper. Uses genetic algorithm.
Connect performance metric to fitness input. Good for single-metric optimization
(e.g., minimize EUI). Limited to one objective.

**Wallacei** (multi-objective): NSGA-2 algorithm for Grasshopper. Handles 2–10+
objectives simultaneously. Produces Pareto front of non-dominated solutions. Includes
built-in analytics for exploring the solution space. Recommended for performance-driven
design where multiple conflicting objectives exist.

**Colibri** (design space exploration): Records every iteration of a parametric
study (inputs and outputs) to a structured data file. Pairs with Design Explorer
web app for parallel coordinates visualization. Useful for understanding parameter
sensitivity before launching optimization.

---

### 9. Simulation Quality Assurance

#### Validation Strategies

Every simulation result should be viewed with appropriate skepticism. Validation builds
confidence in results:

- **Analytical validation**: Compare simulation output against known analytical
  solutions for simple cases (e.g., steady-state heat flow through a wall, illuminance
  from a point source). If the engine cannot reproduce analytical results, something
  is fundamentally wrong.
- **Empirical validation**: Compare simulation output against measured data from real
  buildings or controlled experiments. ASHRAE Standard 140 (BESTEST) provides
  standardized test cases for energy simulation engines.
- **Comparative validation**: Compare results from two different simulation engines
  on the same model. Agreement builds confidence; disagreement demands investigation.
- **Sensitivity analysis**: Vary uncertain inputs (material properties, schedules,
  weather data) and observe the effect on outputs. If results are highly sensitive to
  an uncertain input, invest effort in getting that input right.

#### Mesh Independence Studies

For any spatially discretized simulation (daylight grids, CFD meshes, FEM meshes):

1. Run the simulation with a coarse mesh.
2. Refine the mesh (halve cell size) and rerun.
3. Compare results at key locations.
4. If results change by more than 5%, refine further.
5. Repeat until results converge (< 2% change between successive refinements).
6. Report the final mesh resolution and the convergence behavior.

Mesh independence is non-negotiable for CFD and strongly recommended for daylight grids.
A simulation on an inadequate mesh is not worth the computation time.

#### Result Interpretation Guidelines

- **Order of magnitude**: Do results fall within the expected range for this building
  type and climate? An EUI of 500 kWh/m²/yr for a well-insulated office is wrong.
- **Spatial distribution**: Do daylight, temperature, and wind maps show physically
  plausible patterns? Symmetric buildings should produce symmetric results.
- **Temporal patterns**: Do energy loads follow expected seasonal patterns? Cooling
  should peak in summer, heating in winter (for most climates).
- **Comparative ranking**: Even if absolute values are uncertain, the relative ranking
  of design options is usually reliable. Use simulation for comparison, not prediction.

#### Common Errors and Diagnostic Checklist

| Error                          | Symptom                              | Fix                                    |
|--------------------------------|--------------------------------------|----------------------------------------|
| Missing surfaces               | Unrealistic heat loss / daylight     | Check for gaps in geometry             |
| Wrong boundary conditions      | Adiabatic exterior walls             | Verify face types (wall/floor/roof)    |
| Interior walls as exterior     | Excessive heating/cooling loads      | Check adjacencies between rooms        |
| Wrong weather file             | Results don't match climate          | Verify EPW location matches project    |
| Schedule errors                | Overnight loads in unoccupied building| Review occupancy and HVAC schedules   |
| Unit confusion                 | Values 10x too high or low           | Check W vs kW, m² vs ft², °C vs °F    |
| Insufficient Radiance bounces  | Dark interiors, low daylight values  | Increase -ab parameter                 |
| Coarse CFD mesh                | Smoothed-out wind patterns           | Refine mesh, check independence        |
| Wrong material properties      | Unrealistic surface temperatures     | Verify conductivity, reflectance, etc. |
| Unconverged CFD                | Oscillating residuals                | Improve mesh quality, check BC setup   |

#### When to Trust Results vs. Use Engineering Judgment

Trust simulation results when:
- The model has been validated against analytical or empirical benchmarks.
- Mesh independence has been demonstrated.
- Material properties and boundary conditions are well-characterized.
- Results are within expected physical ranges.
- Sensitivity analysis shows results are robust to uncertain inputs.

Use engineering judgment when:
- Input data is highly uncertain (occupant behavior, future climate).
- The simulation engine has known limitations for the specific case.
- Results contradict well-established physical principles.
- The model uses significant simplifications (shoebox model, ideal HVAC).
- Computational constraints prevented adequate mesh resolution.

#### Reporting Simulation Results

Professional simulation reports should include:

1. **Executive summary**: Key findings and recommendations in non-technical language.
2. **Model description**: Geometry, materials, boundary conditions, assumptions.
3. **Simulation setup**: Engine, version, settings, mesh details, weather data.
4. **Results**: Spatial maps, charts, tables with clear units and legends.
5. **Interpretation**: What the results mean for design decisions.
6. **Limitations**: What the simulation does not capture, uncertainty bounds.
7. **Recommendations**: Specific design actions supported by the analysis.
8. **Appendices**: Detailed input data, convergence plots, sensitivity results.

Never present simulation results without stating the assumptions and limitations.
A number without context is more dangerous than no number at all.

---

### Quick Reference: Simulation Engine Selection

| Analysis need                  | Recommended engine          | Ladybug tool    | Accuracy level    |
|--------------------------------|-----------------------------|-----------------|-------------------|
| Daylight factor                | Radiance                    | Honeybee        | High              |
| Annual daylight (sDA/ASE)      | Radiance (3/5-phase)        | Honeybee        | High              |
| Glare analysis                 | Radiance + Evalglare        | Honeybee        | High              |
| Solar radiation                | Built-in (Tregenza method)  | Ladybug         | Medium-High       |
| Sun hours / shadow             | Built-in (ray intersection) | Ladybug         | High              |
| Building energy (annual)       | EnergyPlus                  | Honeybee        | High              |
| Building energy (early stage)  | Degree-day / lookup         | Manual          | Low-Medium        |
| Outdoor wind comfort           | OpenFOAM                    | Butterfly       | Medium-High       |
| Indoor thermal comfort (PMV)   | EnergyPlus                  | Honeybee        | High              |
| Outdoor thermal comfort (UTCI) | Built-in                    | Ladybug         | Medium            |
| Urban microclimate             | ENVI-met                    | External        | High              |
| Room acoustics                 | Pachyderm                   | External (GH)   | Medium-High       |
| Outdoor noise                  | ISO 9613 / CadnaA           | External        | Medium-High       |

---

### Key Formulas Reference

**Daylight Factor:**
DF = (Ei / Eo) * 100%
Where Ei = indoor illuminance, Eo = unobstructed outdoor diffuse horizontal illuminance.

**Sabine reverberation time:**
RT60 = 0.161 * V / A
Where V = volume (m³), A = total absorption (m² Sabins).

**Natural ventilation flow rate:**
Q = Cd * A * sqrt(2 * deltaP / rho)
Where Cd = discharge coefficient (~0.6), A = opening area, deltaP = pressure difference, rho = air density.

**Solar heat gain through glazing:**
Qsolar = A_glazing * SHGC * I_solar
Where SHGC = solar heat gain coefficient, I_solar = incident solar radiation (W/m²).

**Thermal transmittance (U-value):**
U = 1 / R_total
R_total = R_si + sum(d_i / k_i) + R_se
Where R_si/R_se = surface resistances, d = thickness, k = conductivity.

**UTCI (simplified approximation):**
UTCI ≈ f(Ta, Tr, va, RH) — computed via 6th-order polynomial regression.

**Reynolds number:**
Re = rho * v * L / mu
Where rho = air density, v = velocity, L = characteristic length, mu = dynamic viscosity.
Re > 4000 indicates turbulent flow (for external aerodynamics, Re >> 10^6 always turbulent).


## data-driven-design

### Data-Driven Design

> GIS integration, sensor data, occupancy analytics, space syntax analysis, urban data analytics, climate data processing, and API data sources for evidence-based AEC computational design

## Data-Driven Design

This skill provides comprehensive guidance on integrating quantitative data into every stage of the architectural and urban design process. It covers geospatial data, environmental sensing, occupancy analytics, spatial network analysis, climate processing, urban datasets, and the APIs that serve them. The goal is to replace intuition-only design with evidence-based reasoning while preserving creative agency.

---

### 1. Data-Driven Design Philosophy

#### 1.1 Evidence-Based vs. Intuition-Based Design

Traditional design relies heavily on precedent, aesthetic judgment, and professional intuition. These are valuable but unverifiable. Evidence-based design augments intuition with measurable inputs:

| Dimension | Intuition-Based | Evidence-Based |
|---|---|---|
| Site analysis | Walkthrough, photos | GIS layers, sensor grids, satellite imagery |
| Program sizing | Rules of thumb | Occupancy analytics, utilization studies |
| Circulation | Designer judgment | Space syntax integration/choice values |
| Orientation | Sun path intuition | EPW-parsed radiation/temperature analysis |
| Massing | Formal exploration | Daylight/energy simulation feedback loops |
| Post-occupancy | Anecdotal feedback | Sensor-driven POE dashboards |

Evidence-based design does not eliminate intuition. It provides a quantitative substrate on which creative decisions rest, making design rationale transparent, defensible, and reproducible.

#### 1.2 Data as Design Input, Not Just Validation

The critical shift: data must enter the design process at the very beginning, not after decisions are made. In the traditional workflow, simulation runs after design is locked, serving only to confirm or reject. In a data-driven workflow:

1. **Pre-design data collection** -- site climate, demographics, transport, land use, environmental constraints
2. **Data-informed brief** -- program areas derived from utilization studies, not guesses
3. **Generative exploration** -- design options generated with data constraints embedded
4. **Continuous feedback** -- every design iteration evaluated against data-derived KPIs
5. **Post-occupancy loop** -- sensor data feeds back into future project templates

#### 1.3 The Data-to-Design Pipeline

```
[Raw Data Sources]
    |
    v
[Acquisition] -- APIs, sensors, manual surveys, open data portals
    |
    v
[Cleaning & Validation] -- missing value handling, outlier detection, CRS alignment
    |
    v
[Processing & Analysis] -- statistical summaries, spatial analysis, temporal patterns
    |
    v
[Translation to Design Parameters] -- the critical creative step
    |
    v
[Parametric Model Integration] -- Grasshopper data trees, Dynamo lists, scripted geometry
    |
    v
[Design Evaluation] -- simulation, scoring, multi-criteria comparison
    |
    v
[Visualization & Communication] -- dashboards, reports, AR overlays
```

#### 1.4 Ethical Considerations in Data Use

- **Bias recognition**: Census data reflects historical segregation. Transport data skews toward car owners. WiFi tracking data skews toward smartphone owners. Understand what populations are invisible in your dataset.
- **Consent and transparency**: Occupancy data collection must be disclosed to building users. GDPR, CCPA, and equivalent regulations apply.
- **Algorithmic fairness**: When data drives automated design decisions (e.g., park placement), audit for equitable outcomes across demographics.
- **Data provenance**: Document the source, date, methodology, and known limitations of every dataset used in design decisions.

#### 1.5 Privacy and Anonymization

- Aggregate occupancy data to zones and time windows (minimum 15-minute bins, minimum 5-person zones) to prevent individual identification.
- Strip MAC addresses, device IDs, and personal identifiers before storage.
- Use k-anonymity (k >= 5) for any published spatial movement data.
- Separate data collection infrastructure from building access control systems.
- Establish data retention policies: raw sensor data purged after 12 months, aggregated statistics retained indefinitely.

---

### 2. GIS Integration

#### 2.1 GIS Fundamentals for Designers

**Coordinate Reference Systems (CRS)**:
- **Geographic CRS**: Latitude/longitude on an ellipsoid (WGS84 = EPSG:4326). Units: degrees. Not suitable for distance/area measurement.
- **Projected CRS**: Flat plane projection. UTM zones (EPSG:326xx for north, 327xx for south), State Plane (US), British National Grid. Units: meters or feet. Required for accurate geometric operations.
- **Rule**: Always know your CRS. Always reproject to a projected CRS before measuring distances or areas.

**Projections**:
- **Conformal** (preserve angles): Mercator, Transverse Mercator, Lambert Conformal Conic. Best for navigation and local design.
- **Equal-area** (preserve area): Albers, Mollweide. Best for thematic mapping at continental/global scale.
- **Equidistant** (preserve distance along certain lines): Azimuthal Equidistant.
- For site-scale AEC work, UTM or local State Plane projections are almost always appropriate.

**Vector vs. Raster**:
- **Vector**: Points (trees, sensors), lines (roads, utilities), polygons (parcels, buildings). Precise geometry. Attribute tables. Formats: Shapefile, GeoJSON, GeoPackage, KML.
- **Raster**: Grid of pixels. Each pixel holds a value (elevation, temperature, land cover class). Formats: GeoTIFF, IMG, ASCII Grid. Resolution matters: 1m DEM vs. 30m DEM.

#### 2.2 Key GIS Data Sources

| Source | Data Types | Resolution/Coverage | Cost |
|---|---|---|---|
| OpenStreetMap | Buildings, roads, POIs, land use | Global, variable quality | Free |
| USGS 3DEP | DEM, LiDAR point clouds | 1m (US), 10m (US) | Free |
| Copernicus DEM | Elevation | 30m global | Free |
| NLCD | Land cover classification | 30m (US) | Free |
| Census TIGER | Boundaries, roads, tracts | US | Free |
| Ordnance Survey | Buildings, terrain, addresses | UK | Mixed |
| Google Earth Engine | Satellite imagery, derived products | 10m--1km, global | Free (research) |
| Mapbox | Vector tiles, satellite | Global | Freemium |
| Local government GIS portals | Parcels, zoning, utilities, trees | City-level | Usually free |

#### 2.3 GIS Tools

- **QGIS**: Free, open-source, full-featured desktop GIS. Plugin ecosystem. Python scripting (PyQGIS). Best for data preparation and analysis before importing to design tools.
- **ArcGIS Pro**: Industry standard. CityEngine integration. Geodatabase management. Advanced spatial analysis. Expensive license.
- **Mapbox**: Web-based tiles and APIs. Excellent for interactive maps. Mapbox GL JS for web dashboards.
- **Google Earth Engine**: Planetary-scale raster analysis. JavaScript/Python API. Best for satellite time-series analysis (vegetation change, urban growth, heat island).

#### 2.4 Grasshopper GIS Plugins

- **Elk** (free): Imports OSM data (buildings, roads, topography) into Grasshopper. Supports .osm files. Terrain from .img files. Simple but effective for urban context models.
- **Heron** (free): Imports Shapefiles, raster images, topography. More format support than Elk. GeoTIFF import for terrain. Reprojection built in.
- **Meerkat** (free): Real-time GIS data streaming. OpenStreetMap tiles. WMS/WMTS service connections.
- **Urbano** (commercial): Urban mobility analysis. Walkability scoring. Amenity accessibility. Network-based analysis integrated with Grasshopper geometry.
- **DeCodingSpaces Toolbox** (free): Space syntax, network analysis, urban morphology metrics computed directly on GIS-imported geometry.

#### 2.5 Typical GIS-to-Design Workflows

1. **Terrain modeling**: Download DEM (GeoTIFF) -> import via Heron -> create mesh surface -> drape site boundary -> cut/fill analysis.
2. **Site boundary extraction**: Download parcel Shapefile from local GIS portal -> import via Heron -> extract target parcel polygon -> set as design boundary.
3. **Context building generation**: Download OSM buildings -> import via Elk -> extrude by height attribute (or estimate floors x 3.5m) -> use as solar/wind context.
4. **Road network import**: OSM road centerlines -> import -> offset for right-of-way widths -> classify by road type.
5. **Land use mapping**: Zoning Shapefile -> import -> color-code by zone type -> overlay with site boundary -> identify constraints.
6. **Walkability analysis**: Import road network + POIs -> compute walking distances via network -> generate isochrone maps -> identify underserved areas.

---

### 3. Sensor Data & IoT

#### 3.1 Sensor Types for Buildings

| Sensor | Measures | Range | Accuracy | Placement |
|---|---|---|---|---|
| Thermocouple/RTD | Temperature | -200 to +850 C | +/-0.5 C | Duct, room, outdoor |
| Capacitive RH | Relative humidity | 0--100% | +/-2% | Room center, avoid direct airflow |
| NDIR CO2 | CO2 concentration | 0--5000 ppm | +/-50 ppm | Breathing zone (1.2m height) |
| Photodiode/Lux | Illuminance | 0--100,000 lux | +/-5% | Desktop height, avoid direct sun |
| PIR | Occupancy (binary) | 5--12m range | N/A | Ceiling, corner mount |
| MEMS microphone | Sound level | 30--130 dBA | +/-1.5 dB | Wall, 1.5m height |
| Electrochemical | PM2.5, VOC, O3, NO2 | Varies | +/-10--20% | Representative location |
| Ultrasonic | Distance/presence | 0.2--6m | +/-1cm | Desk, doorway |

#### 3.2 Building Management Systems (BMS)

Modern BMS systems (Siemens Desigo, Honeywell Niagara, Johnson Controls Metasys, Schneider EcoStruxure) centralize HVAC, lighting, and fire/safety data. Key concepts:
- **Points**: Individual data values (supply air temp, damper position, setpoint). A typical office building has 5,000--50,000 points.
- **Trends**: Historical time-series logs of point values. Typical interval: 5--15 minutes.
- **Alarms**: Threshold-triggered events.
- **Schedules**: Time-based control programs.

#### 3.3 Data Protocols

- **BACnet**: Building Automation and Control Networks. The dominant building protocol. Defines object types (analog input, binary output, schedule). IP-based or MS/TP (RS-485). Read via BACnet libraries (BAC0 for Python).
- **Modbus**: Simple register-based protocol. RTU (serial) or TCP (Ethernet). Each device has a register map. Common for submetering, VFDs.
- **MQTT**: Lightweight publish/subscribe messaging. Ideal for IoT sensors. Broker-based (Mosquitto, HiveMQ). JSON payloads. Topics structured as building/floor/zone/sensor_type.
- **REST API**: HTTP-based. Many modern BMS and IoT platforms expose REST endpoints. JSON responses. Polling-based (not real-time without webhooks/WebSockets).

#### 3.4 Time-Series Data Handling

- **Storage**: InfluxDB (purpose-built time-series DB), TimescaleDB (PostgreSQL extension), or cloud (AWS Timestream, Azure Time Series Insights).
- **Sampling rate**: Environmental sensors: 1--5 minute intervals. Energy meters: 1--15 minute intervals. Occupancy: 1--5 minute intervals.
- **Missing data**: Forward-fill for slow-changing variables (temperature). Interpolation for gradual variables. Flag and exclude for fast-changing variables (occupancy).
- **Aggregation**: Downsample to hourly/daily for long-term storage. Preserve min/max/mean/count.
- **Anomaly detection**: Z-score method for univariate, Isolation Forest for multivariate. Flag sensor drift (gradual offset), sensor failure (flatline or NaN), and impossible values (negative CO2).

#### 3.5 Digital Twin Sensor Integration

A digital twin is a live 3D model synchronized with real-time sensor data. Architecture:

```
[Physical Building]
    |
    v
[Sensors + BMS] -- BACnet, Modbus, MQTT
    |
    v
[Data Ingestion Layer] -- Node-RED, Apache Kafka, custom ETL
    |
    v
[Time-Series Database] -- InfluxDB, TimescaleDB
    |
    v
[API Layer] -- REST/GraphQL endpoints
    |
    v
[3D Visualization] -- Unity/Unreal, Three.js, Forge Viewer
    |
    v
[Digital Twin Dashboard] -- color-coded zones, real-time charts, alerts
```

Sensor data maps to 3D model via spatial identifiers (room ID, zone ID, floor number). Color gradients on room surfaces represent temperature, CO2, occupancy density. Historical playback enables pattern discovery.

---

### 4. Occupancy Analytics

#### 4.1 Sensing Technologies

| Technology | Accuracy | Granularity | Privacy Impact | Cost |
|---|---|---|---|---|
| PIR sensors | 85--90% (binary only) | Room-level, binary | Low | Low |
| WiFi probe requests | 70--80% (counting) | Zone-level, count + dwell | Medium--High | Low (uses existing infra) |
| Bluetooth beacons | 80--90% | Zone-level, individual tracking | High | Medium |
| Camera + AI counting | 95%+ | Entry-level, count + direction | High (even anonymized) | Medium--High |
| Badge/access card | 99% (entry only, no exit) | Door-level, individual | Medium | Low (uses existing infra) |
| Desk sensors (ultrasonic/PIR) | 95%+ | Desk-level, binary | Low | Medium |
| CO2-based estimation | 60--75% | Room-level, count estimate | None | Low |
| LiDAR people counting | 95%+ | Entry-level, count + height | Low--Medium | High |

#### 4.2 Occupancy Density Mapping

Convert raw sensor counts to spatial density:
1. Assign sensors to spatial zones (rooms, departments, floors).
2. Compute occupancy rate: actual_count / design_capacity.
3. Aggregate over time: peak (95th percentile), typical (median), average (mean).
4. Visualize as heat map overlay on floor plan.

Key metrics:
- **Utilization rate**: Hours occupied / total available hours (a room used 4 of 8 workday hours = 50% utilization).
- **Peak occupancy**: Maximum simultaneous occupants (drives HVAC sizing).
- **Diversity factor**: Peak of whole building / sum of individual room peaks (typically 0.6--0.8).
- **Frequency**: How often a space is used per week.

#### 4.3 Design Implications of Occupancy Data

- **Right-sizing**: If meeting rooms average 30% utilization, reduce count and add more informal collaboration zones.
- **HVAC zoning**: High-variability zones need VAV with fast response. Consistently occupied zones can use simpler systems.
- **Circulation sizing**: Peak flow data from entry sensors drives corridor width and elevator sizing.
- **Flexible programming**: Low-utilization spaces become candidates for multi-use or hot-desking.
- **Post-occupancy feedback**: Compare design assumptions (occupancy schedules in energy models) with reality.

---

### 5. Space Syntax

#### 5.1 Core Concepts

Space syntax, developed by Bill Hillier and Julienne Hanson at UCL in the 1980s, quantifies the configurational properties of spatial networks. It reveals how the structure of space itself shapes movement, encounter, and social outcomes.

**Axial map**: The minimum set of longest straight lines (axial lines) that pass through all convex spaces and make all connections in a spatial system. Constructed by drawing lines of sight and access.

**Key measures** (computed on the axial graph where nodes = axial lines, edges = intersections):

| Measure | Definition | Interpretation |
|---|---|---|
| Connectivity | Number of lines directly intersecting a given line | Local accessibility |
| Depth | Shortest topological distance from one line to another | Remoteness |
| Mean Depth | Average depth from a line to all other lines | Overall accessibility |
| Integration (Rn) | Reciprocal of Relative Asymmetry (normalized mean depth) | Global accessibility; high = well-connected |
| Integration (R3) | Integration computed within topological radius 3 | Local accessibility within 3 steps |
| Choice (Rn) | Number of shortest paths passing through a line | Through-movement potential; high = likely route |

#### 5.2 Axial Analysis

Global integration formula:
```
RA = 2(MD - 1) / (k - 2)
```
Where MD = mean depth, k = number of lines in the system.

Real Relative Asymmetry (normalized for system size):
```
RRA = RA / D_k
```
Where D_k is the diamond value for a graph of k nodes.

Integration = 1 / RRA. Higher values = more integrated (accessible).

Choice counts how many shortest paths between all pairs of nodes pass through a given node. Normalized choice (NACH) enables cross-system comparison.

#### 5.3 Segment Analysis

More recent method. Axial lines are broken at intersections into segments. Analysis uses angular distance (cumulative turn angle) rather than topological distance. This better predicts vehicular movement and pedestrian route choice.

Angular choice and angular integration at various metric radii (400m, 800m, 1200m, 2000m, 5000m, n) reveal multi-scale spatial structure.

#### 5.4 Visibility Graph Analysis (VGA)

1. Overlay a regular grid of points on the floor plan (typically 0.5--1.0m spacing).
2. For each pair of points, determine mutual visibility (unobstructed straight line).
3. Construct the visibility graph (nodes = grid points, edges = mutual visibility).
4. Compute graph measures: visual connectivity, visual integration, visual mean depth, clustering coefficient.

VGA reveals:
- Visual fields and their depth
- Spaces that are visually dominant or hidden
- Potential for natural surveillance (high clustering = many mutual visibility connections)
- Wayfinding legibility

#### 5.5 Isovist Analysis

An isovist is the set of all points visible from a given vantage point. Isovist properties:
- **Area**: Total visible floor area. Larger = more open.
- **Perimeter**: Boundary length. Longer relative to area = more complex visual field.
- **Compactness**: 4 * pi * area / perimeter^2. Circle = 1. Lower = more elongated/fragmented.
- **Occlusivity**: Length of the isovist boundary not formed by real surfaces (i.e., depth edges). Higher = more hidden areas beyond view.
- **Drift**: Distance from the isovist centroid to the vantage point. Higher = directional bias in the visual field.
- **Min/Max radial**: Shortest and longest line of sight.

Isovist fields: compute isovists at every point on a grid. Map each property as a scalar field. Reveals spatial character continuously across the plan.

#### 5.6 Tools for Space Syntax

- **depthmapX** (free, open-source): The reference implementation. Axial, segment, VGA, isovist, agent analysis. Import DXF plans. Export CSV results for statistical analysis.
- **Syntactic (Paco Holanda)**: Grasshopper plugin. Axial and segment analysis within parametric workflow. Enables real-time space syntax feedback during design.
- **SpiderWeb (Paco Holanda)**: Agent-based pedestrian simulation in Grasshopper. Agents navigate using space syntax logic.
- **DeCodingSpaces Toolbox**: Grasshopper plugin. Includes space syntax, shape grammar, and urban morphology analysis.

#### 5.7 Correlation Studies

Space syntax measures consistently correlate with observed phenomena:
- **Pedestrian flow**: Integration (R3) correlates with pedestrian counts (r = 0.7--0.9 in many studies).
- **Retail rents**: Choice (Rn) correlates with commercial property values. High-choice streets attract retail.
- **Crime**: Low integration (segregated spaces) correlates with higher burglary rates. "Eyes on the street" effect.
- **Wayfinding**: Higher visual integration correlates with faster navigation and fewer wrong turns.

#### 5.8 Application Scales

- **Floor plan**: Optimize room connectivity, visual relationships, circulation efficiency. Compare design variants quantitatively.
- **Building complex/campus**: Analyze building-to-building connectivity, identify isolated zones, optimize pedestrian routes.
- **Urban district**: Street network analysis. Identify high-integration streets for active frontages. Locate public amenities on high-choice streets. Predict pedestrian and vehicular flow distribution.
- **City scale**: Metropolitan integration structure. Identify integration cores, deformed wheels, urban villages.

---

### 6. Climate Data Processing

#### 6.1 EPW Weather Files

EPW (EnergyPlus Weather) is the standard weather file format for building energy simulation. Each file represents one year (8760 hours) of weather data for a specific location.

**Structure**: Header (8 lines with location, design conditions, ground temperatures) + 8760 data rows (one per hour).

**Key data fields** (67 total, most important listed):

| Field | Unit | Description |
|---|---|---|
| Dry Bulb Temperature | C | Air temperature |
| Dew Point Temperature | C | Moisture indicator |
| Relative Humidity | % | Moisture ratio |
| Atmospheric Pressure | Pa | Station pressure |
| Global Horizontal Radiation | Wh/m2 | Total solar on horizontal |
| Direct Normal Radiation | Wh/m2 | Solar beam component |
| Diffuse Horizontal Radiation | Wh/m2 | Scattered solar |
| Wind Direction | degrees | 0=N, 90=E, 180=S, 270=W |
| Wind Speed | m/s | At measurement height (usually 10m) |
| Total Sky Cover | tenths | 0=clear, 10=overcast |
| Precipitable Water | mm | Column water vapor |
| Horizontal Infrared Radiation | Wh/m2 | Longwave from sky |

**Sources**: climate.onebuilding.org (4000+ locations), EnergyPlus website, Ladybug Tools EPW Map.

#### 6.2 TMY Methodology

Typical Meteorological Year (TMY) files are composites: each month is selected from a multi-year record (typically 15--30 years) as the most "typical" month for that calendar month. Selection uses Finkelstein-Schafer statistics on key variables (solar radiation, temperature, humidity, wind). TMY represents normal conditions, not extremes. For extreme event analysis, use AMY (Actual Meteorological Year) files.

#### 6.3 Climate Analysis Techniques

**Temperature bins**: Histogram of hourly temperatures. Reveals heating/cooling balance points, dominant temperature ranges. Drives passive design strategy selection.

**Degree-days**: Heating Degree Days (HDD) = sum of (base_temp - outdoor_temp) for all hours where outdoor < base. Cooling Degree Days (CDD) = sum of (outdoor_temp - base_temp) for all hours where outdoor > base. Typical base: 18.3C (65F). Used for energy benchmarking and climate classification.

**Psychrometric chart**: Plots temperature vs. humidity ratio. Overlay with comfort zone and passive strategy boundaries (evaporative cooling, thermal mass + night ventilation, natural ventilation). Givoni's bioclimatic chart is the classic reference.

**Wind rose**: Polar histogram of wind speed and direction. Segment by season, time of day, or temperature range for nuanced analysis. Critical for natural ventilation orientation, windbreak placement, and outdoor comfort.

**Sun path diagram**: Stereographic projection of solar positions throughout the year. Plot obstructions to determine solar access. Overlay with direct normal irradiance for useful solar hours. Essential for shading device design and PV placement.

#### 6.4 Ladybug Weather Data Components

Ladybug (Grasshopper plugin) provides comprehensive weather data visualization and analysis:
- `LB Import EPW`: Parse EPW file into individual data streams.
- `LB Hourly Plot`: Time-series visualization of any weather variable.
- `LB Wind Rose`: Directional wind analysis.
- `LB Sun Path`: 3D sun path diagram in Rhino.
- `LB Psychrometric Chart`: Interactive psychrometric analysis with strategy overlays.
- `LB Adaptive Comfort`: Thermal comfort assessment using ASHRAE 55 adaptive model.
- `LB UTCI`: Universal Thermal Climate Index for outdoor comfort.
- `LB Degree Days`: Heating and cooling degree day calculation.

#### 6.5 Future Climate Projections

Climate change requires designers to consider 2050 and 2080 conditions. Methods:
- **CCWorldWeatherGen** (free tool): "Morphs" present-day EPW files using IPCC AR4/AR5 climate model outputs. Applies monthly shift factors to temperature, radiation, humidity, wind.
- **WeatherShift** (commercial): Similar morphing with probabilistic approach (10th, 50th, 90th percentile outcomes).
- **Meteonorm future files**: Generated using climate model projections for specific emission scenarios (RCP 4.5, 8.5 / SSP 2-4.5, 5-8.5).

Typical 2050 shifts for mid-latitude cities: +1.5 to +3.0C mean temperature, +5 to +15% cooling energy, -5 to -15% heating energy, increased extreme heat events.

#### 6.6 Urban Heat Island Effect

Urban areas are typically 1--5C warmer than surrounding rural areas due to:
- Reduced vegetation and evapotranspiration
- Increased thermal mass (concrete, asphalt)
- Waste heat from buildings, vehicles, industry
- Reduced sky view factor (canyon geometry traps longwave radiation)
- Reduced wind speed from surface roughness

Monitoring: Mobile transect surveys, fixed weather station networks, satellite-derived land surface temperature (Landsat, MODIS). Integration with design: adjust EPW data for urban context using UWG (Urban Weather Generator) by MIT.

---

### 7. Urban Data Analytics

#### 7.1 Census Data Integration

Census data provides demographic, socioeconomic, and housing characteristics at multiple geographic levels (block, block group, tract, county, state in the US). Key variables for design:
- Population density (drives infrastructure sizing)
- Age distribution (playground vs. senior center needs)
- Household size (unit mix for housing projects)
- Income levels (affordability requirements)
- Commute mode (parking vs. transit infrastructure)
- Housing tenure (own vs. rent, vacancy rates)

Access via Census Bureau API (api.census.gov), IPUMS, or processed datasets (Social Explorer, PolicyMap).

#### 7.2 Transport Data

**GTFS (General Transit Feed Specification)**: Standardized format for public transit schedules and routes. Published by transit agencies worldwide. Contains: stops, routes, trips, stop_times, calendar, shapes. Use for:
- Transit accessibility mapping (isochrone from any point via transit)
- Service frequency analysis (headways by time of day)
- Transit coverage gap identification

**Traffic counts**: State DOTs publish AADT (Annual Average Daily Traffic) counts on major roads. Available as GIS layers. Use for noise modeling, pedestrian safety analysis, roadway capacity assessment.

**Cycling/pedestrian counts**: Increasingly available from permanent counters (Eco-Counter) and Strava Metro data. Reveals active transport patterns and demand.

#### 7.3 Real Estate Data

- **Transaction data**: Sale prices, rent levels, cap rates. Sources: Zillow (US), Zoopla (UK), local MLS feeds.
- **Land values**: Assessed values from tax records. Useful for development feasibility analysis.
- **Spatial patterns**: Price gradients, gentrification indicators, correlation with transit/amenity proximity.

#### 7.4 Social Media and Sentiment Data

- **Geotagged posts**: Twitter/X, Instagram, Flickr. Reveal popular gathering spots, underused areas, perception of places.
- **Sentiment analysis**: NLP on location-tagged text. Identify areas perceived as unsafe, beautiful, lively, boring.
- **Limitations**: Severe demographic bias (young, tech-savvy, English-speaking over-represented). Use as supplement, not primary evidence.

#### 7.5 Noise Mapping Data

EU Environmental Noise Directive requires strategic noise maps for agglomerations >100,000 population. Data includes:
- Road traffic noise (Lden, Lnight contours)
- Rail noise
- Aircraft noise
- Industrial noise

Use for: facade acoustic design, building orientation, buffer zone planning, amenity placement (playgrounds away from noise sources).

#### 7.6 Air Quality Data

Sources: EPA AirNow (US), EEA (Europe), OpenAQ (global aggregator). Key pollutants: PM2.5, PM10, O3, NO2, SO2, CO. Available as station measurements and modeled surfaces. Design implications:
- Air intake placement (away from high-pollution zones)
- Filtration specification
- Outdoor space programming (avoid exercising near highways)
- Green infrastructure placement for particulate capture

#### 7.7 Urban Metabolism Data

Material and energy flow analysis for cities: water consumption, waste generation, energy use, food supply. Data from utility companies, waste management, and municipal sustainability reports. Design implications for circular economy buildings and net-zero neighborhoods.

---

### 8. API Data Sources for AEC

#### 8.1 Comprehensive API Reference

##### OpenStreetMap Overpass API
- **Endpoint**: `https://overpass-api.de/api/interpreter`
- **Data**: Buildings (footprints + height + levels), roads, railways, waterways, land use, POIs, amenities, trees
- **Rate limits**: Fair use; heavy queries may be throttled. Use local Overpass instance for production.
- **Auth**: None
- **Python library**: `overpy`, `osmnx`
- **Query language**: Overpass QL. Example: `[out:json];way["building"]({{bbox}});out body;>;out skel qt;`

##### Mapbox APIs
- **Endpoints**: `api.mapbox.com/v4/` (tiles), `/directions/v5/`, `/isochrone/v1/`, `/geocoding/v5/`
- **Data**: Vector/raster tiles, driving/walking/cycling directions, isochrones (travel time polygons), geocoding
- **Rate limits**: 100,000 free tile requests/month; 100,000 free directions/month
- **Auth**: Access token (free tier available)
- **Python library**: `mapbox` SDK, or direct HTTP via `requests`

##### Google Maps Platform
- **Endpoints**: `maps.googleapis.com/maps/api/place/`, `/directions/`, `/elevation/`
- **Data**: Place details (ratings, hours, type), directions with traffic, elevation profiles
- **Rate limits**: $200 free monthly credit; ~40,000 direction requests
- **Auth**: API key + billing account
- **Python library**: `googlemaps`

##### OpenWeather / NOAA
- **Endpoints**: `api.openweathermap.org/data/2.5/`, `www.ncdc.noaa.gov/cdo-web/api/v2/`
- **Data**: Current weather, forecasts, historical observations, climate normals
- **Rate limits**: OpenWeather: 1000 calls/day free. NOAA: 1000 calls/day free.
- **Auth**: API key
- **Python library**: `pyowm`, `noaa-sdk`

##### EPA APIs
- **Endpoints**: `aqs.epa.gov/data/api/`, `enviro.epa.gov/`
- **Data**: Air quality (AQI, criteria pollutants), brownfield/superfund sites, toxic release inventory, water quality
- **Rate limits**: Generous; registration required
- **Auth**: Email registration
- **Python library**: Direct `requests`; some community wrappers

##### Census Bureau API
- **Endpoint**: `api.census.gov/data/`
- **Data**: ACS (demographics, income, housing), Decennial Census, Economic Census, TIGER boundaries
- **Rate limits**: 500 calls/day without key; unlimited with free key
- **Auth**: Free API key
- **Python library**: `census`, `cenpy`

##### USGS 3DEP
- **Endpoint**: `elevation.nationalmap.gov/arcgis/rest/services/`
- **Data**: DEM (1/3 arc-second = ~10m, 1m where available), LiDAR point clouds
- **Rate limits**: Generous
- **Auth**: None
- **Python library**: `py3dep`, `requests`

##### Zillow / Zoopla
- **Endpoints**: `api.bridgedataoutput.com/api/v2/` (Zillow via Bridge), `api.zoopla.co.uk/api/v1/`
- **Data**: Property values, listings, Zestimates, comparable sales, neighborhood data
- **Rate limits**: Varies by plan; Bridge API has free tier
- **Auth**: API key
- **Python library**: Direct `requests`

##### GTFS Feeds
- **Source**: `transitfeeds.com`, individual agency websites
- **Data**: Static schedules (stops, routes, trips, stop_times) and GTFS-realtime (vehicle positions, trip updates, alerts)
- **Format**: ZIP of CSV files (static), Protocol Buffers (real-time)
- **Python library**: `gtfs-kit`, `partridge`, `gtfs-realtime-bindings`

##### Copernicus Data
- **Endpoint**: `scihub.copernicus.eu/dhus/`, `dataspace.copernicus.eu/`
- **Data**: Sentinel-2 (10m multispectral imagery), Sentinel-1 (SAR), Copernicus DEM (30m global)
- **Rate limits**: Generous; large file downloads
- **Auth**: Free registration
- **Python library**: `sentinelsat`, `eodag`, Google Earth Engine

---

### 9. Data Visualization for Design

#### 9.1 Charts and Plots for Design Communication

Choose chart type by data type and audience:
- **Bar/column**: Compare categories (land use areas, room counts by type)
- **Line**: Time-series (temperature over year, occupancy over week)
- **Scatter**: Correlation (integration vs. pedestrian count, rent vs. distance to transit)
- **Heatmap**: 2D intensity (occupancy by hour and day-of-week, solar radiation by month and hour)
- **Radar/spider**: Multi-criteria comparison (design variant scoring across KPIs)
- **Sankey**: Flow diagrams (energy flow, material flow, movement distribution)
- **Box plot**: Distribution and outliers (indoor temperatures across zones)
- **Violin**: Distribution shape (daylight factor across rooms)

#### 9.2 Spatial Data Visualization

- **Choropleth map**: Polygon fill color by data value (census tract by income, parcels by zoning).
- **Dot density**: Random dots within polygon proportional to value (population distribution).
- **Isoline/contour**: Equal-value lines (noise contours, temperature isotherms).
- **3D extrusion**: Height proportional to data (buildings by energy use, blocks by density).
- **Flow map**: Lines with width proportional to flow (pedestrian routes, transit ridership).
- **Heat map**: Continuous surface interpolated from point observations (air quality, temperature).

#### 9.3 Dashboard Design for Stakeholder Engagement

Key principles:
- Lead with the "so what" -- headline KPI at top, detail below.
- Maximum 5--7 visualizations per dashboard view.
- Interactive filtering by time, zone, scenario.
- Consistent color coding across views.
- Annotations explaining thresholds and benchmarks.
- Export to PDF for offline review.

#### 9.4 Grasshopper Visualization Tools

- **Human UI** (free): Build interactive WPF dashboards inside Grasshopper. Sliders, charts, data grids, buttons. Excellent for design review sessions.
- **Design Explorer** (free): Multi-objective design space exploration. Parallel coordinates plot. Filter Pareto-optimal solutions. Integrates with Colibri for automated iteration capture.
- **Colibri** (free): Automated design iteration. Records images, data, and parameters for every iteration. Exports to Design Explorer for interactive exploration.
- **TT Toolbox**: Data tree manipulation and visualization utilities.
- **Squid**: PDF generation from Grasshopper for automated reporting.

#### 9.5 Web-Based Dashboards

- **Plotly Dash** (Python): Full-featured dashboarding framework. Interactive charts (Plotly.js). Layout with HTML/CSS. Callbacks for interactivity. Deploy as web app.
- **Streamlit** (Python): Rapid dashboard prototyping. Minimal code. Auto-refresh on script change. Built-in chart types. Map support (Folium, Pydeck, Mapbox).
- **Kepler.gl**: WebGL-powered large-scale geospatial visualization. 3D building layers, arc layers, heatmaps, hexbin. Jupyter integration.
- **Three.js / Speckle**: 3D model visualization in browser with data overlay. Speckle provides AEC-specific 3D viewer with data streams.

#### 9.6 AR/VR Data Overlay

Emerging capability: overlay sensor data, simulation results, and analytics on physical or virtual building models.
- **AR**: Microsoft HoloLens, Apple Vision Pro. Overlay temperature gradients, occupancy counts, maintenance alerts on physical spaces during walkthroughs.
- **VR**: Oculus/Meta Quest, HTC Vive. Navigate data-rich virtual models during design review. Color-code surfaces by daylight factor, acoustic performance, energy flux.
- **Frameworks**: Unity with custom shaders for data visualization. Unreal Engine with Datasmith for AEC model import. WebXR for browser-based lightweight experiences.

---

### Summary of Key Workflows

| Workflow | Data Source | Processing Tool | Design Integration |
|---|---|---|---|
| Site context model | OSM, DEM | QGIS, Elk/Heron | Grasshopper geometry |
| Climate-responsive orientation | EPW | Ladybug | Parametric massing |
| Walkability analysis | OSM, GTFS | Urbano, osmnx | Site plan, amenity placement |
| Occupancy-driven program | Sensors, BMS | InfluxDB, Python | Area schedule adjustment |
| Circulation optimization | Floor plan | depthmapX, Syntactic | Layout refinement |
| Noise-informed planning | Noise maps | QGIS, Python | Building orientation, buffer zones |
| Demographic-responsive design | Census | cenpy, Python | Unit mix, community facilities |
| Real-time building performance | IoT sensors | Digital twin platform | Ongoing operations optimization |

---

### References and Further Reading

- Hillier, B. & Hanson, J. (1984). *The Social Logic of Space*. Cambridge University Press.
- Hillier, B. (1996). *Space is the Machine*. Cambridge University Press.
- Al-Sayed, K. et al. (2014). *Space Syntax Methodology*. Bartlett School of Architecture, UCL.
- Reinhart, C. (2014). *Daylighting Handbook I*. MIT Press.
- Ratti, C. & Claudel, M. (2016). *The City of Tomorrow*. Yale University Press.
- Batty, M. (2013). *The New Science of Cities*. MIT Press.
- EnergyPlus Documentation: Weather Data format specifications.
- Ladybug Tools documentation: ladybug.tools
- QGIS documentation: docs.qgis.org


---

# Facades & fabrication


## facade-computation

### Facade Computation

> Panelization strategies, surface rationalization, attractor-based patterning, double-skin facades, kinetic and responsive facades, environmental performance facades, and fabrication-aware facade design for AEC

## Facade Computation

### 1. Computational Facade Design Philosophy

The building facade is not a wrapper. It is the single most consequential architectural element — the mediator between interior environment and exterior climate, the primary determinant of energy consumption, the structural skin that must resist wind, seismic, and thermal loads, and the public expression of a building's identity. Computational facade design treats every square meter of this surface as a field of optimizable variables rather than a repeating module selected from a catalog.

#### Facade as Environmental Mediator

Every facade simultaneously manages five environmental flows:

| Flow | Inward | Outward |
|------|--------|---------|
| **Solar radiation** | Daylight, solar heat gain | Glare, overheating |
| **Thermal energy** | Heat loss in winter | Heat gain in summer |
| **Air** | Natural ventilation, infiltration | Exfiltration, stack effect |
| **Moisture** | Rain penetration, condensation | Vapor diffusion |
| **Sound** | Exterior noise intrusion | Interior noise escape |

A computationally-driven facade optimizes across all five flows simultaneously, varying panel geometry, material, porosity, and depth point-by-point across the surface based on orientation, local microclimate, interior program, and structural constraints.

#### Integration of Performance, Structure, and Aesthetics

Traditional practice separates these into different consultancies — the architect draws the pattern, the structural engineer sizes the mullions, the facade consultant specifies the glass, and the energy modeler checks compliance. Computational facade design collapses these into a single parametric model where every design decision is simultaneously evaluated against structural, thermal, daylight, acoustic, and aesthetic criteria. The parametric model is the single source of truth, and downstream deliverables — shop drawings, energy models, structural calculations, panel schedules — are all derived outputs.

#### The Shift from Standard Curtain Walls to Computationally-Derived Systems

Standard curtain wall systems (stick-built or unitized) impose a regular orthogonal grid with fixed mullion depths and standardized infill panels. This approach optimizes for fabrication simplicity and erection speed at the cost of environmental performance — every panel on the building receives the same glass, the same SHGC, the same U-value, regardless of whether it faces north or south, is at ground level or the 60th floor, or fronts an office or a server room.

Computational facade design replaces this uniformity with gradient variation:
- Glass type varies by orientation and floor level
- Mullion depth varies by wind pressure zone
- Shading device angle varies by solar exposure
- Panel porosity varies by ventilation requirement
- Panel size varies by structural span and visual rhythm

The result is a facade that performs 30-50% better than a uniform curtain wall while often using less material, because material is concentrated where loads demand it rather than uniformly distributed.

#### Facade as a Data-Driven Element

Modern computational facades are designed from data, not from intuition:
- **Solar radiation maps** (kWh/m²/year per panel) drive shading geometry
- **Wind pressure coefficients** (Cp values from CFD or wind tunnel) drive mullion sizing
- **View analysis** (percentage of sky visible, view direction quality) drives glazing transparency
- **Daylight autonomy targets** (sDA, ASE) drive aperture size and light redirection
- **Acoustic mapping** (dB levels from traffic, aircraft) drives acoustic performance requirements
- **Structural analysis** (gravity, wind, seismic, thermal movement) drives connection design
- **Cost models** ($/m² by panel type) drive rationalization strategies

Each of these data layers becomes an input field that the computational model reads and responds to, producing a facade that is locally optimized everywhere.

---

### 2. Panelization Strategies

Panelization is the process of decomposing a continuous design surface into discrete, fabricable panels. The choice of panelization strategy determines fabrication cost, structural behavior, weatherproofing strategy, and visual character.

#### 2.1 Planar Panelization

Planar panels are the most economical to fabricate because flat glass can be cut from stock sheets without any forming process.

##### Quad Panels from UV Subdivision

The simplest approach: subdivide the surface along its natural UV parameter lines to produce quadrilateral panels. On a planar or single-curved surface, these quads are inherently planar. On a double-curved surface, they will deviate from planarity.

**Planarity tolerance**: Industry standard is < 2mm deviation of the fourth corner from the plane defined by the other three corners. For structural silicone glazing, tolerances tighten to < 1mm. For mechanically captured glazing with gaskets, up to 3mm may be acceptable depending on gasket profile.

**PQ-mesh (Planar Quadrilateral Mesh) generation methods**:
1. **Conjugate curve network**: Identify two families of curves on the surface that intersect at consistent angles. If the curves follow conjugate directions (where the second fundamental form vanishes), the resulting quad mesh will have planar faces. On a surface of revolution, meridians and parallels are conjugate. On a translational surface, the two generating curve families are conjugate.
2. **Conical mesh construction**: A mesh where all vertices have the property that the face planes around each interior vertex share a common tangent cone. Conical meshes guarantee planar quad faces and also allow offset meshes at constant face-to-face distance — critical for multi-layer facade assemblies.
3. **Planarization by optimization**: Start with any quad mesh and iteratively move vertices to minimize a planarity energy functional while maintaining proximity to the design surface and regularity of panel sizes. Typical solver: Kangaroo 2 in Grasshopper, or custom Newton-Raphson solver.
4. **Projection methods**: Project a planar grid onto the surface along surface normals, then adjust to enforce planarity. Works well for near-planar surfaces but diverges on highly curved regions.

##### Triangulated Panels

Triangulation guarantees planarity (any three points define a plane) but produces more edges, more mullion intersections, and higher framing cost. Triangulated facades typically cost 15-25% more in framing than quad facades of equivalent area due to the increased total edge length and the complexity of six-way mullion intersections.

**Triangulation methods**:
- Delaunay triangulation of point sets on the surface
- Subdivision of quad meshes along diagonals
- Voronoi dual meshing (produces triangles from Voronoi centers)
- Advancing front methods for graded triangle sizes
- Remeshing algorithms (e.g., isotropic remeshing for uniform triangle size)

##### Hexagonal Panels

Hex panels produce three-way intersections (120-degree angles) which are structurally efficient and visually distinctive. However, hexagonal panels on a double-curved surface cannot all be planar — the Euler characteristic of the sphere requires exactly 12 pentagonal panels in any hexagonal tiling of a closed convex surface (Euler's formula: V - E + F = 2).

**Generation methods**:
- Dual of a triangulated mesh (Voronoi of triangle vertices on the surface)
- Hex-dominant meshing algorithms
- Circle packing on the surface (produces hex-like patterns)

##### Irregular Planar Panels

Voronoi tessellations, irregular polygonal meshes, and other non-regular planar decompositions. These maximize design freedom but complicate fabrication scheduling and erection sequencing. Every panel is unique, so panel identification and tracking become critical — each panel requires a unique ID, a fabrication drawing, and a location tag.

#### 2.2 Single-Curved Panelization

Single-curved panels (cylindrical, conical, or general ruled surfaces) can be fabricated by bending flat material along one axis.

##### Ruled Surfaces

A ruled surface is generated by moving a straight line through space. If the facade surface can be decomposed into strips where each strip is a ruled surface, the panels can be fabricated from flat sheet material bent around a single-curved mold.

**Ruling analysis**: For a given surface, compute the asymptotic directions (directions of zero normal curvature). Along these directions, the surface is locally ruled. On a surface with negative Gaussian curvature, there are two asymptotic directions at every point; on a surface with zero Gaussian curvature (developable), there is one; on a surface with positive Gaussian curvature, there are none (the surface is locally non-ruled).

##### Developable Strips

A developable surface has zero Gaussian curvature everywhere — it can be unrolled flat without stretching. Decomposing a free-form surface into developable strips is a powerful rationalization strategy because each strip can be fabricated from flat sheet material with zero waste from forming.

**Strip decomposition algorithms**:
1. Geodesic strip decomposition: Cut the surface along geodesic lines to produce strips that approximate developable surfaces
2. Ruling-based decomposition: Identify ruling directions and segment the surface along them
3. Principal curvature strip decomposition: Cut along lines of principal curvature (one family of principal curvature lines on a surface always produces developable strips if the other curvature is zero)

##### Cold-Bent Glass

Cold bending involves forcing a flat glass panel into a curved frame, inducing residual stress in the glass. This is the most economical way to achieve single-curved panels.

**Minimum bend radius by glass thickness and type**:

| Glass Thickness | Annealed (min radius) | Heat-Strengthened | Fully Tempered |
|----------------|----------------------|-------------------|----------------|
| 4 mm | 2.0 m | 1.5 m | 1.0 m |
| 6 mm | 3.0 m | 2.2 m | 1.5 m |
| 8 mm | 4.0 m | 3.0 m | 2.0 m |
| 10 mm | 5.0 m | 3.8 m | 2.5 m |
| 12 mm | 6.0 m | 4.5 m | 3.0 m |
| 15 mm | 7.5 m | 5.6 m | 3.8 m |
| 19 mm | 9.5 m | 7.1 m | 4.8 m |

**Stress limits**: Cold-bent annealed glass should not exceed 7 MPa residual bending stress under sustained load. Heat-strengthened glass can tolerate up to 24 MPa, and fully tempered up to 46 MPa. These limits must account for additional wind and thermal stresses during service.

**Bending moment calculation**: For a rectangular panel of width w, thickness t, and bend radius R, the bending stress sigma = E * t / (2 * R), where E = 70 GPa for soda-lime glass. This determines whether a given curvature is achievable with a given glass type and thickness.

#### 2.3 Double-Curved Panelization

Double-curved panels require forming processes that deform the material in two directions simultaneously.

##### Hot-Bent Glass

Glass is heated to approximately 620-680 degrees C (above its softening point) and slumped or pressed over a mold. This allows complex curvatures but requires a unique mold for each panel geometry.

**Process constraints**:
- Minimum radius: approximately 300mm for 6mm glass (much tighter than cold bending)
- Mold material: stainless steel, ceramic fiber, or CNC-milled refractory
- Optical quality: hot-bent glass may show slight optical distortion; critical for reflective facades
- Tempering after forming: glass must be re-tempered after hot bending (additional process step and cost)
- Lead time: 8-12 weeks for mold fabrication plus 2-4 weeks for glass forming

##### Mold-Based Fabrication

For non-glass materials (GFRC, FRP, precast concrete), molds can be CNC-milled from foam, 3D-printed, or fabricated from sheet metal. Mold cost dominates when panel count per unique geometry is low.

**Mold cost amortization**: If a mold costs $2,000 and produces 1 panel, the mold cost per panel is $2,000. If it produces 20 identical panels, the cost drops to $100/panel. This is why panel clustering and repetition are so critical for double-curved facades.

##### Cost Implications

| Panel Type | Relative Cost (per m²) | Typical Application |
|-----------|----------------------|---------------------|
| Flat (planar) | 1.0x (baseline) | Standard curtain wall |
| Cold-bent single-curved | 1.3-1.8x | Gentle curvature, towers |
| Hot-bent single-curved | 1.5-2.0x | Tighter curves |
| Cold-bent double-curved | 1.8-2.5x | Warped quads, minimal curvature |
| Hot-bent double-curved | 3.0-5.0x | Moderate double curvature |
| Free-form hot-bent | 5.0-8.0x | Complex sculptural forms |
| 3D printed mold + cast | 4.0-10.0x | Unique panels, small runs |

#### 2.4 Panel Optimization

The goal of panel optimization is to minimize cost by reducing the number of unique panel geometries while maintaining design intent and surface quality.

##### Reducing Unique Panel Count

Strategies:
1. **Symmetry exploitation**: Mirror symmetry, rotational symmetry, translational repetition
2. **Geometric simplification**: Replace double-curved panels with single-curved or planar approximations where curvature is below a perceptual threshold
3. **Mold sharing**: Group panels that can be fabricated on the same mold with minor adjustments (shims, adjustable mold points)
4. **Modular systems**: Design the surface geometry to accommodate a fixed kit of panel shapes

##### Panel Clustering

**K-means clustering**: Represent each panel as a feature vector (e.g., four corner deviation from planarity, edge lengths, diagonal lengths, curvatures). Apply k-means to group panels into k families. Each family shares a single mold or cutting template.

**DBSCAN clustering**: Density-based clustering that does not require specifying k in advance. Panels that are geometrically similar within a tolerance epsilon are grouped together. Outliers (panels that do not fit any cluster) are flagged for individual fabrication.

**Hierarchical clustering**: Build a dendrogram of panel similarity. Cut at the desired tolerance level to produce families. Allows interactive exploration of the tradeoff between unique count and geometric deviation.

##### Panel Families

A panel family is a group of panels that share a common fabrication template. Within a family, panels may differ by:
- Edge trim (cut to different outlines from the same curved blank)
- Drilling pattern (different hole locations for point-fixed connections)
- Coating or treatment (different frit patterns, colors)
- But they share the same curvature/forming geometry

##### Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| Unique panel count | Number of distinct geometries | Minimize (< 20% of total ideal) |
| Total panel count | Total panels on facade | Determined by subdivision |
| Repetition ratio | Total / Unique | Maximize (> 5:1 ideal) |
| Waste ratio | Material wasted in cutting / total material | < 15% |
| Planarity deviation | Max corner deviation from plane (mm) | < 2mm for glass |
| Edge length variation | Std dev of edge lengths within a family | < 5% of mean |
| Curvature deviation | Max deviation from design surface (mm) | < 5mm typically |

---

### 3. Surface Rationalization

Surface rationalization transforms a free-form design surface into a geometry that can be constructed from discrete elements with known fabrication processes. It is distinct from panelization (which subdivides a surface into panels) — rationalization modifies the surface itself to be more constructible.

#### 3.1 Developable Surface Approximation

Any smooth surface can be approximated by a collection of developable strips. The quality of approximation depends on strip width and surface curvature.

**Ruling analysis**: Compute the Gaussian curvature K at every point. Where K = 0, the surface is already developable. Where K is small (|K| < threshold), the surface can be closely approximated by a developable surface. Where |K| is large, the surface must be split into narrower strips.

**Strip decomposition**: Segment the surface into strips along one family of curvature lines. Each strip is then approximated by a ruled surface (the simplest developable form). The approximation error is proportional to strip width squared times the Gaussian curvature.

#### 3.2 Conical Mesh Generation

A conical mesh is a polyhedral mesh where, at every interior vertex, the face planes are tangent to a common cone. This geometric property has profound practical consequences:

1. **Planar faces**: All faces of a conical mesh are planar (follows from the cone tangency condition)
2. **Torsion-free nodes**: The mullion axes at each node are coplanar, eliminating the need for custom twisted node connectors
3. **Constant-width offsets**: The mesh can be offset at a constant face-to-face distance, producing a parallel mesh for the inner layer of a multi-layer facade assembly

**Generation algorithms**:
- Start from a smooth reference surface
- Compute a conjugate curve network aligned with principal curvature directions
- Discretize into a quad mesh
- Apply conical mesh optimization: minimize the deviation from the cone condition at each vertex while maintaining proximity to the design surface
- Iterate until convergence (typically 20-50 iterations)

Reference: Helmut Pottmann, Andreas Wallner, et al., "Freeform surfaces from single curved panels," ACM Transactions on Graphics, 2008.

#### 3.3 Planar Hex Mesh from Dupin Cyclides

Dupin cyclides are surfaces where all lines of curvature are circles or straight lines. They include tori, cones, cylinders, and their inversions. A hex mesh derived from a Dupin cyclide decomposition of a surface produces planar hexagonal faces — a non-trivial geometric result since general hex meshes on curved surfaces are not planar.

**Method**:
1. Fit a patchwork of Dupin cyclides to the design surface
2. Extract the circular arc lines of curvature from each patch
3. Construct the hex mesh as the dual of the triangle mesh formed by three families of curvature circles

#### 3.4 Edge-Offset Meshes for Structural Facades

An edge-offset mesh is a mesh where every edge has a well-defined offset direction perpendicular to the edge and lying in the bisector plane of the adjacent faces. This property allows beams of constant cross-section to be placed along edges without custom end cuts — the beam profile at each node fits perfectly with its neighbors.

This is critical for steel or aluminum structural facades where mullions and transoms are extruded profiles. Without the edge-offset property, every beam end requires a custom miter cut, dramatically increasing fabrication cost.

#### 3.5 Circular Arc Structures

Replacing straight mullion segments with circular arcs allows a coarser mesh (fewer panels) to approximate a curved surface. Circular arcs can be fabricated by rolling straight profiles through a three-roll bender — a standard steel fabrication process.

**Design parameters**:
- Arc radius (determines curvature fidelity)
- Arc subtended angle (determines member length)
- Node geometry (tangent-continuous or kinked connections)

#### 3.6 Principal Curvature Line Networks

The principal curvature lines of a surface are curves along which normal curvature is maximized or minimized. They form an orthogonal network on the surface (except at umbilical points where principal curvatures are equal). This network has special properties:

- Panels bounded by principal curvature lines have minimal twist
- The network aligns with the directions of maximum and minimum structural stiffness
- Mullions along principal curvature lines experience minimal torsion

**Computation**: Principal curvature lines are found by integrating the principal direction field across the surface. Singularities occur at umbilic points, where the direction field is undefined. Special handling (rounding, splitting) is required at these points.

#### 3.7 Reference Implementations and Tool Comparison

| Tool | Platform | Capabilities | Limitations |
|------|----------|-------------|-------------|
| Evolute Tools | Rhino/GH | Conical mesh, PQ mesh, edge offset mesh optimization | Commercial, no longer actively developed |
| Kangaroo 2 | Grasshopper | Planarization, developability, mesh relaxation | General purpose — requires custom goal setup |
| LunchBox | Grasshopper | Panel types (diamond, hex, quad, random) | Geometry generation only, no rationalization optimization |
| Paneling Tools | Rhino | UV-based panelization, attractor-based | Limited to surface UV structure |
| ShapeOp | C++/Python | Projective dynamics for geometric optimization | Research code, requires integration |
| Custom scripts | Python/C# | Full control over rationalization algorithms | Development time, no GUI |
| Karamba3D | Grasshopper | Structural analysis of facade meshes | Analysis only, not geometry generation |

---

### 4. Attractor-Based Patterning

Attractor-based patterning uses geometric primitives (points, curves, surfaces) as control inputs to modulate facade properties across the surface. This produces gradient effects that respond to environmental conditions, program, or purely aesthetic intent.

#### 4.1 Point Attractors

A point attractor P located at coordinates (px, py, pz) influences a panel centered at (cx, cy, cz) based on the distance d = |P - C|.

**Distance-based scaling**: Panel size S = S_base * f(d), where f is a mapping function:
- Linear: f(d) = d / d_max
- Inverse: f(d) = 1 - d / d_max
- Gaussian: f(d) = exp(-d² / (2 * sigma²))
- Sigmoid: f(d) = 1 / (1 + exp(-k * (d - d_0)))
- Power: f(d) = (d / d_max)^n

**Rotation**: Panel rotation angle theta = theta_max * f(d). Useful for louver facades where louver angle varies with proximity to a design feature (entrance, corner, sightline).

**Density variation**: Subdivision density increases near the attractor (smaller panels near the point, larger panels far from it). Implemented by adaptive subdivision: refine quads where d < threshold, coarsen where d > threshold.

#### 4.2 Curve Attractors

A curve attractor C(t) influences panels based on the minimum distance from the panel center to the curve. This produces band-like gradient effects along the facade.

**Applications**:
- Gradient transparency bands around a building's waistline or crown
- Increased shading density near a horizontal datum
- Variable perforation density following a diagonal line across the facade

**Implementation**: For each panel center, compute the closest point on the curve using iterative projection (Newton-Raphson on the distance function) or by sampling the curve at fine intervals and finding the minimum.

#### 4.3 Multi-Attractor Blending

When multiple attractors are active simultaneously, their effects must be combined:

| Method | Formula | Character |
|--------|---------|-----------|
| Weighted average | f = sum(w_i * f_i) / sum(w_i) | Smooth blending, values stay in range |
| Nearest | f = f_i where d_i is minimum | Sharp transitions at equidistant boundaries |
| Additive | f = sum(f_i), clamped | Reinforcement where attractors overlap |
| Multiplicative | f = product(f_i) | Rapid falloff, only activates near intersection |
| Maximum | f = max(f_i) | Each attractor dominates in its zone |
| Minimum | f = min(f_i) | Intersection-like behavior |

#### 4.4 Attractor-Driven Aperture Control

Use attractors to vary window-to-wall ratio (WWR) or glazing transparency across the facade:

- **Daylight optimization**: Place attractors at points where interior daylight levels are below target (from daylight simulation). Increase aperture size near attractors to admit more light.
- **View optimization**: Place attractors at facade zones with high-quality views (toward parks, skyline, water). Increase transparency near these attractors.
- **Privacy control**: Place attractors at facade zones facing neighboring buildings at close range. Decrease aperture size or increase opacity near these attractors.

#### 4.5 Attractor-Driven Perforation Patterns

Perforated metal screens can vary their perforation density, hole size, or hole shape based on attractor distance:

- **Hole diameter**: d_hole = d_min + (d_max - d_min) * f(d_attractor)
- **Hole spacing**: spacing = s_min + (s_max - s_min) * (1 - f(d_attractor))
- **Open area ratio**: OAR = OAR_min + (OAR_max - OAR_min) * f(d_attractor)

Typical open area ratios for facade screens: 20-60%. Below 20%, the screen reads as nearly solid. Above 60%, the screen loses its shading effectiveness and structural integrity.

#### 4.6 Attractor-Driven Louver Angle Variation

Horizontal or vertical louvers can vary their tilt angle based on attractor distance:

- **Solar attractor**: Use the sun position (azimuth, altitude) as a time-varying attractor. Louver angle tracks solar altitude to block direct sun while admitting diffuse light.
- **View attractor**: Louvers near important view corridors are angled to preserve outward views while blocking solar gain from adjacent angles.

#### 4.7 Grasshopper Implementation Patterns

```
Typical Grasshopper data flow for attractor-based patterning:

Surface → Subdivide (UV) → Panel Centers (points)
Attractor Point(s) → Distance (panel centers to attractors)
Distance → Remap (to 0-1 domain) → Scale/Rotate/Color panels
Panels → Geometry output
Panels → Data output (panel schedule)
```

Key components: `Surface Divide`, `Distance`, `Remap Numbers`, `Graph Mapper` (for custom falloff curves), `Scale`, `Rotate`, `Extrude`.

#### 4.8 Environmental Attractors

The most powerful application maps environmental simulation data directly to attractor fields:

- **Solar radiation map to panel density**: Run an annual solar radiation simulation (e.g., Ladybug/Honeybee). High-radiation zones get denser shading elements (more panels, deeper fins, lower SHGC glass). Low-radiation zones get more transparent treatments.
- **View angle to transparency**: Compute view quality metric per panel (sky view factor, view content analysis). High-quality-view panels get higher VLT glass. Low-quality-view panels get opaque or translucent infill.
- **Wind pressure to ventilation openings**: Map CFD wind pressure coefficients to operable panel locations. High positive-pressure zones and high negative-pressure zones are connected by ventilation paths.
- **Noise map to acoustic performance**: Map exterior noise levels (from traffic simulation or measurement) to required STC rating per panel. High-noise zones get triple glazing or laminated acoustic glass.

---

### 5. Double-Skin Facades

A double-skin facade (DSF) consists of an outer skin, an inner skin, and a ventilated cavity between them. The cavity acts as a thermal buffer, an acoustic buffer, a natural ventilation path, and a space for integrating shading devices protected from wind and rain.

#### 5.1 Typologies

| Typology | Cavity Height | Cavity Depth | Ventilation | Best For |
|----------|--------------|-------------|-------------|----------|
| **Box window** | 1 story, 1 bay | 200-300 mm | Inlet/outlet per box | Renovation, noise reduction |
| **Shaft-box** | Multi-story shaft + box | 200-400 mm | Stack effect through shaft | High-rise, natural vent |
| **Corridor** | 1 story, full width | 400-800 mm | Horizontal flow per floor | Maintenance access, moderate height |
| **Multi-story** | 3+ stories | 600-1000+ mm | Stack-driven, full height | Landmark buildings, atria |

#### 5.2 Cavity Sizing and Ventilation Strategies

**Cavity depth guidelines**:
- 150-200 mm: Minimum for venetian blind integration, limited airflow
- 200-400 mm: Standard DSF cavity, accommodates blinds and maintenance access for cleaning
- 400-800 mm: Walk-in cavity for maintenance, significant thermal buffer
- 800-1000+ mm: Occupied intermediate space (wintergarden typology)

**Ventilation strategies**:
- **Naturally ventilated**: Openings at top and bottom of cavity. Stack effect and wind pressure drive airflow. Flow rate Q = Cd * A * sqrt(2 * g * H * (Ti - To) / To), where Cd is discharge coefficient, A is opening area, H is cavity height, Ti is cavity air temperature, To is outdoor air temperature.
- **Mechanically ventilated**: Fans drive airflow through the cavity. Allows precise control and heat recovery. Higher energy cost.
- **Hybrid**: Natural ventilation when conditions permit, mechanical when needed.

**Airflow modes**:
- Outdoor air curtain: Air enters from outside at bottom, exits outside at top (summer mode — flushes solar heat gain)
- Indoor air curtain: Air drawn from interior at bottom, returned to interior at top (winter mode — preheats ventilation air)
- Supply air: Outdoor air enters cavity, is preheated, then supplied to interior HVAC system
- Exhaust air: Interior air is exhausted through the cavity, recovering heat to the outer skin in winter

#### 5.3 Natural Ventilation Through DSF

The DSF cavity enables natural ventilation in high-rise buildings where direct window opening would be impractical due to wind pressure. The outer skin acts as a wind buffer while the inner skin provides operable openings.

**Design requirements for natural ventilation via DSF**:
- Inner skin openings: minimum 5% of floor area for ventilation
- Cavity bypass dampers to prevent floor-to-floor smoke/sound transmission
- Acoustic baffles in the cavity to maintain STC rating between floors
- Wind speed sensors to close outer skin openings when wind exceeds 8-10 m/s

#### 5.4 Acoustic Performance

The DSF cavity provides significant acoustic attenuation, typically 10-15 dB improvement over a single skin of equivalent mass. This is due to the mass-air-mass resonance system formed by the two skins and the air cavity.

**Acoustic design parameters**:
- Outer skin: typically 10-12 mm laminated glass (mass law)
- Cavity depth: deeper = better low-frequency attenuation (mass-air-mass resonance drops)
- Inner skin: 6-8 mm laminated glass minimum
- Cavity absorption: blinds and perforated metal liners absorb cavity reverberance
- Expected composite STC: 42-55 depending on configuration

#### 5.5 Fire Safety Considerations

The DSF cavity presents fire safety challenges:
- **Chimney effect**: The cavity can accelerate fire spread vertically via stack effect
- **Mitigation**: Fire-rated spandrel panels between floors, automatic closing dampers at each floor level, sprinkler heads in the cavity at each floor
- **Code requirements**: Many jurisdictions require the cavity to be compartmentalized at each floor or every 2-3 floors. Fire-rated glass (E30, EW30, or EI30) may be required for the inner or outer skin at spandrel zones.
- **Smoke extraction**: Provide openable vents or breakout panels at the top of each cavity compartment

#### 5.6 Energy Performance Modeling

DSF energy modeling requires coupled thermal-airflow simulation:
- **Tools**: EnergyPlus Airflow Network, IES VE, TRNSYS, ESP-r
- **Key parameters**: Solar absorptance of blinds, cavity airflow rate, outer skin U-value, inner skin U-value, blind position and angle
- **Typical results**: DSF reduces heating energy by 20-40% in cold climates (preheated ventilation air) and reduces cooling energy by 10-25% in hot climates (solar chimney flushing heat gain)

#### 5.7 Maintenance Access Requirements

- **Corridor and multi-story types**: The cavity must be wide enough for a person to enter (minimum 600 mm clear, 800 mm preferred) with walkable grating floors at each level
- **Box window type**: Cleaning access via hinged or removable inner panes
- **Exterior cleaning**: BMU (building maintenance unit) or rope access for outer skin exterior face
- **Interior cavity cleaning**: Annual minimum; more frequent in polluted urban environments

#### 5.8 Precedent Projects

| Project | Location | Type | Cavity Depth | Key Innovation |
|---------|----------|------|-------------|----------------|
| **30 St Mary Axe** (The Gherkin) | London | Multi-story (6 floors) | 1200 mm | Spiraling light wells with DSF ventilation |
| **GSW Headquarters** | Berlin | Corridor | 900 mm | West-facing thermal flue with automated blinds |
| **KfW Westarkade** | Frankfurt | Box window | 350 mm | Pressure-equalized box modules, 80% natural vent |
| **One Angel Square** | Manchester | Multi-story | 600 mm | BREEAM Outstanding, passive solar heating |
| **Manitoba Hydro Place** | Winnipeg | Multi-story | 1000 mm | Solar chimney, 115 m tall, -40°C to +35°C climate |
| **Stadttor Düsseldorf** | Düsseldorf | Corridor | 1400 mm | Habitable cavity, full walk-in access |

---

### 6. Kinetic & Responsive Facades

Kinetic facades contain elements that physically move in response to environmental conditions, occupant input, or programmed patterns. They represent the most sophisticated integration of computational design, mechanical engineering, and environmental performance.

#### 6.1 Actuation Types

##### Mechanical Actuation
- **Electric motors**: DC servo, stepper, or brushless DC. Precise control, high reliability, moderate cost. Typical torque range: 0.5-50 Nm per shading element.
- **Pneumatic**: Compressed air actuators. Fast actuation, suitable for binary open/close states. Requires air supply infrastructure.
- **Hydraulic**: High force for large elements. Used in large-scale kinetic structures (bridges, retractable roofs). Rarely used for individual facade elements due to complexity.
- **Linear actuators**: Electric motor with lead screw or ball screw. Provides linear push/pull motion. Stroke range: 50-1000 mm typical.

##### Material-Based Actuation
- **Shape memory alloy (SMA)**: Nitinol wire contracts when heated above transition temperature (typically 60-80°C). Silent, no motor, but limited stroke and slow response. Suitable for small elements (individual louver blades).
- **Bi-metal strips**: Two metals with different thermal expansion coefficients bonded together. Curvature changes with temperature. Completely passive — no energy input. Limited force and stroke.
- **Hygroscopic materials**: Wood or other materials that change shape with humidity. Extremely slow response (hours to days). Used in experimental/art installations.
- **Electroactive polymers**: Polymer films that deform under electric field. Research stage for facade applications.

##### Passive Actuation
- **Wind-driven**: Facade elements that rotate or deflect under wind pressure. No energy input, no control. Examples: kinetic wind sculptures, flutter panels.
- **Thermal expansion**: Elements that change geometry with temperature. Predictable, maintenance-free, but limited range.

#### 6.2 Sensor Types

| Sensor | Measures | Typical Placement | Range | Application |
|--------|----------|-------------------|-------|-------------|
| Pyranometer | Global solar irradiance (W/m²) | Roof, facade | 0-1400 W/m² | Solar tracking, shading control |
| Photodiode array | Light level and direction | Facade surface | 0-100,000 lux | Glare detection, daylight optimization |
| Thermocouple/RTD | Temperature | Cavity, interior, exterior | -40 to +80°C | Thermal control, overheating protection |
| Anemometer | Wind speed and direction | Roof | 0-50 m/s | Wind safety, natural vent control |
| Occupancy sensor | Presence/absence | Interior zones | Binary or count | Demand-based facade response |
| Rain sensor | Precipitation | Roof or facade | Binary | Close ventilation openings |
| CO2 sensor | Indoor air quality | Interior | 0-5000 ppm | Ventilation demand control |

#### 6.3 Control Systems

**Open-loop**: Facade elements follow a pre-programmed schedule based on time-of-day and season. No sensors. Simple and reliable but cannot respond to actual conditions (cloud cover, etc.).

**Closed-loop**: Sensors measure environmental conditions; a controller adjusts facade elements to maintain setpoints (e.g., interior illuminance = 500 lux, interior temperature < 25°C). PID control or rule-based logic.

**Predictive**: Weather forecast data (cloud cover, temperature, wind) is integrated into the control algorithm. The facade pre-adjusts before conditions change, reducing lag and overshoot. Machine learning models can learn optimal strategies from historical data.

**Distributed vs. centralized**: Each facade module can have its own controller (distributed — resilient but complex to coordinate) or a central BMS (building management system) can command all modules (centralized — easier to coordinate but single point of failure).

#### 6.4 Kinematic Mechanisms

| Mechanism | DOF | Motion Type | Complexity | Example |
|-----------|-----|------------|------------|---------|
| Rotation (single axis) | 1 | Angular | Low | Louver blade |
| Translation (slide) | 1 | Linear | Low | Sliding screen |
| Folding (single hinge) | 1 | Angular | Low | Hinged panel |
| Bi-fold | 1 (coupled) | Double angular | Medium | Folding shutter |
| Scissor mechanism | 1 | Expanding | Medium | Deployable screen |
| Origami fold | 1-3 | Complex folding | High | Miura-ori panel |
| Iris mechanism | 1 | Radial open/close | Medium | Circular aperture |
| Auxetic expansion | 1 | 2D expansion | High | Rotating square pattern |
| Cable-net deformation | Multiple | Surface deformation | High | Tensioned mesh |

#### 6.5 Shading Device Geometries

- **Horizontal louvers**: Most common. Effective for south-facing facades (northern hemisphere). Blade angle and spacing determine shading coefficient. Blade profile: flat, airfoil, Z-shaped.
- **Vertical fins**: Effective for east and west facades where sun angle is low. Fin depth and spacing control shading.
- **Egg-crate**: Combined horizontal and vertical elements. Effective for all orientations but complex and expensive.
- **Perforated screens**: Fixed or sliding panels with perforation patterns that filter light. Perforation density can vary across the panel.
- **Deployable/retractable**: Fabric, metal mesh, or rigid panels that can be fully retracted when shading is not needed. Maximizes daylight and views during overcast conditions.
- **Origami-based**: Folding panels based on rigid origami patterns (Miura-ori, Yoshizawa). Single-DOF deployment from flat to fully shading.

#### 6.6 Solar Tracking Algorithms

Solar position calculation:
- **Inputs**: Latitude, longitude, date, time, timezone
- **Outputs**: Solar altitude (degrees above horizon), solar azimuth (degrees from north)
- **Algorithm**: NREL Solar Position Algorithm (SPA) — accurate to 0.0003 degrees for years -2000 to +6000

**Tracking strategies**:
- Single-axis tracking: Louver rotates around one axis to follow solar altitude. Reduces direct solar gain by 70-90%.
- Dual-axis tracking: Panel rotates around two axes to always face (or always avoid) the sun. Maximum performance but highest mechanical complexity.
- Segmented tracking: Different facade zones track independently based on their orientation and the sun's current position relative to their surface normal.

#### 6.7 Al Bahar Towers Case Study

The Al Bahar Towers in Abu Dhabi (2012, Aedas Architects) feature a kinetic mashrabiya screen on the exterior of twin 145m towers. Key technical data:

- **1,049 units** per tower (2,098 total), each a folding triangular umbrella
- **Actuation**: Linear electric actuators, one per unit
- **Material**: PTFE-coated fiberglass mesh on steel frame
- **Control**: Pre-programmed solar tracking schedule, updated daily via BMS
- **Performance**: Reduces solar gain by up to 50%, reducing cooling energy by 20%
- **Response time**: Full open to full close in approximately 15 minutes
- **Wind safety**: Units retract to closed position at wind speeds above 35 km/h
- **Maintenance**: Each unit can be individually replaced from within the cavity between the screen and the curtain wall

#### 6.8 Adaptive Facade Energy Performance Modeling

Modeling kinetic facades requires time-step simulation because the facade state changes throughout the day and year:

1. **Hourly simulation**: Run building energy simulation (EnergyPlus, IDA ICE) with facade state updated each hour based on control logic
2. **Co-simulation**: Couple facade control algorithm (Python/MATLAB) with energy simulation engine via FMI (Functional Mock-up Interface)
3. **Key metrics**: Annual heating/cooling energy (kWh/m²), peak cooling load (W/m²), daylight autonomy (%), glare hours
4. **Comparison**: Always compare against a static reference facade (e.g., fixed louvers at optimal annual angle) to quantify the benefit of kinetic operation
5. **Typical savings**: 15-30% cooling energy reduction compared to optimal fixed shading

#### 6.9 Prototyping Strategies

1. **Digital prototype**: Grasshopper kinematic simulation with Kangaroo for mechanism physics. Validate range of motion, collision detection, structural behavior.
2. **Tabletop mockup**: 3D-printed or laser-cut 1:10 scale model with micro servos to test mechanism. Validate kinematics, identify binding or interference.
3. **Full-scale single unit**: Fabricate one full-size kinetic element. Test actuation force, cycle time, weather resistance, durability (10,000+ cycles).
4. **Bay mockup**: Full-scale multi-unit mockup (3x3 units minimum) installed on a test wall. Test coordination, edge conditions, weatherproofing, maintenance access.
5. **Environmental chamber testing**: Subject mockup to temperature cycling (-20 to +60°C), UV exposure, rain, wind (up to design wind speed), and salt spray (coastal projects).

---

### 7. Environmental Performance Facades

Environmental performance facades are designed from the outside in — the environmental loads on each square meter of facade surface determine its composition, geometry, and behavior.

#### 7.1 Solar Shading

##### Horizontal Overhang Depth Calculator

For a horizontal overhang to shade a window at a given cut-off solar altitude angle alpha:

**Overhang depth D = H / tan(alpha)**

Where H is the height from the bottom of the window to the overhang.

**Cut-off angle by latitude and orientation** (for south-facing facade, northern hemisphere, summer solstice noon):

| Latitude | Solar Altitude (summer solstice) | Recommended Cut-off Angle |
|----------|--------------------------------|--------------------------|
| 0° (Equator) | 66.5° (at solstice) / 90° (equinox) | 75° |
| 10° | 76.5° / 80° | 70° |
| 20° | 86.5° / 70° | 65° |
| 30° | 83.5° / 60° | 55° |
| 40° | 73.5° / 50° | 50° |
| 50° | 63.5° / 40° | 45° |
| 60° | 53.5° / 30° | 40° |

Example: At 40°N latitude, south-facing window 1.5m tall, with overhang at window head.
Cut-off angle = 50°. Overhang depth D = 1.5 / tan(50°) = 1.5 / 1.19 = 1.26 m.

##### Vertical Fin Design

Vertical fins are most effective on east and west facades where the sun angle is low. Fin depth and spacing determine the shading mask:

**Shading mask angle = arctan(fin depth / fin spacing)**

For 80% shading of low-angle sun: fin depth / spacing ratio should be approximately 1.0 to 1.5.

##### Egg-Crate Shading

Combines horizontal and vertical elements. The resulting shading mask is the intersection of the horizontal overhang mask and the vertical fin mask. Provides omnidirectional shading but reduces daylight admission and views.

#### 7.2 Daylight Redirection

- **Light shelves**: Horizontal reflective surfaces positioned at or above eye level. Bounce daylight onto the ceiling, extending daylight penetration from the typical 1.5x window head height to 2.5x or more. Reflective surface should have > 85% reflectance. Optimal depth: 0.5-1.5 m.
- **Prismatic glazing**: Micro-structured glass that refracts direct sunlight upward toward the ceiling. Effective for south facades (northern hemisphere). Reduces glare while maintaining daylight levels.
- **Fiber optic daylighting**: Rooftop or facade-mounted solar concentrators coupled to fiber optic cables that deliver daylight to interior zones without windows. Effective depth: up to 15 m from facade. Emerging technology with decreasing cost.

#### 7.3 Ventilation

- **Pressure-equalized rainscreen**: The outer cladding layer has open joints that allow air pressure to equalize between the exterior and the cavity behind the cladding. This prevents rain from being driven through joints by wind pressure. Cavity depth: minimum 25 mm. Compartmentalization: vertical and horizontal baffles at maximum 6 m intervals.
- **Ventilated cavity**: A continuous air space behind the outer cladding, open at top and bottom. Stack effect drives upward airflow, removing moisture and reducing solar heat gain to the inner wall. Typical cavity depth: 50-150 mm. Airflow velocity: 0.1-0.5 m/s.
- **Operable elements**: Windows, louvers, or panels that can be opened for natural ventilation. Effective free area for natural ventilation: minimum 4% of floor area. Cross-ventilation requires openings on two sides of the floor plate.

#### 7.4 Thermal Performance

- **U-value optimization**: The overall thermal transmittance of the facade assembly. Target values vary by climate: cold climate < 0.8 W/m²K, temperate < 1.2 W/m²K, hot-arid < 1.8 W/m²K, hot-humid < 2.2 W/m²K (for glazed facades).
- **Thermal bridge analysis**: Mullion and transom profiles create thermal bridges. Thermally broken profiles use polyamide or polyurethane insulating strips to separate inner and outer aluminum sections. Thermal break width: 20-35 mm. Without thermal break: effective U-value of framing can be 5-8 W/m²K. With thermal break: 1.5-3.0 W/m²K.
- **Condensation risk**: At any point on the interior surface where the surface temperature drops below the dew point of the interior air, condensation will form. Use two-dimensional heat flow analysis (THERM, Flixo) to identify cold spots at frame corners, mullion intersections, and sill details.

#### 7.5 Integrated Photovoltaics (BIPV)

| BIPV Type | Efficiency | Transparency | Appearance | Cost ($/Wp) |
|-----------|-----------|-------------|------------|-------------|
| Monocrystalline silicon | 18-22% | Opaque (or spaced cells for semi-transparent) | Dark blue/black cells | 0.30-0.50 |
| Polycrystalline silicon | 15-18% | Opaque | Blue cells | 0.25-0.40 |
| Amorphous silicon (a-Si) | 6-8% | 10-30% VLT achievable | Uniform dark tint | 0.40-0.60 |
| CdTe thin-film | 12-16% | 10-40% VLT achievable | Dark brown/black | 0.30-0.50 |
| CIGS thin-film | 14-18% | Low (typically opaque) | Black | 0.35-0.55 |
| Organic PV (OPV) | 8-12% | Up to 50% VLT | Colored, printable | 0.50-1.00 |
| Perovskite (emerging) | 15-25%+ | Tunable | Tunable color | Research stage |

**Aesthetic integration strategies**:
- Custom cell spacing for desired transparency/opacity ratio
- Colored PV cells (interference coatings for red, green, blue, gold appearances)
- Patterned cell arrangements (logo, abstract patterns)
- Curved BIPV on single-curved panels using flexible thin-film
- BIPV as spandrel panels (opaque zones between vision glass)

#### 7.6 Green Facades and Living Walls

- **Green facades**: Climbing plants on cables, mesh, or trellis attached to the building facade. Low maintenance, seasonal variation (deciduous species provide summer shading, winter solar gain). Support structure: stainless steel cable net (typical cable diameter 3-5 mm, mesh spacing 200-400 mm) or welded wire mesh.
- **Living walls**: Pre-vegetated panels or felt-based systems mounted on the facade with integrated irrigation and drainage. Higher maintenance (irrigation, fertilization, plant replacement) but immediate visual impact and year-round coverage.
- **Performance benefits**: Surface temperature reduction of 5-15°C compared to bare wall, noise reduction of 5-10 dB, particulate matter capture, biodiversity habitat, psychological well-being.
- **Structural considerations**: Dead load of living wall systems: 30-100 kg/m² depending on system type and saturation. Wind load on planting: additional drag coefficient.

---

### 8. Fabrication-Aware Facade Design

Fabrication-aware design integrates manufacturing constraints into the computational model from the outset, preventing designs that are geometrically elegant but unbuildable or prohibitively expensive.

#### 8.1 Glass

**Glass types and properties**:

| Type | Thickness Range | Max Size (typical) | Key Property |
|------|----------------|-------------------|-------------|
| Float (annealed) | 2-25 mm | 3210 x 6000 mm | Base product, can be cut to shape |
| Heat-strengthened | 4-19 mm | 2440 x 4800 mm | 2x bending strength of annealed |
| Fully tempered | 4-19 mm | 2440 x 4800 mm | 4x bending strength, safety glass |
| Laminated | 2+2 to 19+19 mm | Limited by autoclave | Safety, acoustic, UV blocking |
| Insulated (IGU) | 16-60 mm total | 2800 x 6000 mm | Thermal performance |
| Structural glass | 15-25 mm tempered | 3000 x 6000 mm | Load-bearing fins, beams |

**Processing capabilities**:
- Cutting: Straight lines and curves. Minimum internal radius for curved cuts: 50 mm. Water jet for complex shapes.
- Drilling: Minimum hole diameter = glass thickness. Minimum edge distance = 2x glass thickness. Minimum hole-to-hole distance = 2x glass thickness.
- Printing (ceramic frit): Silk-screen or digital printing. Resolution: 50-150 dpi typical for silk-screen, up to 720 dpi for digital. Coverage: 0-100% opacity.
- Coating: Low-e, solar control, self-cleaning (TiO2 photocatalytic), anti-reflective. Applied during float process (hard coat) or by magnetron sputtering (soft coat).

**Structural glass systems**:
- Point-fixed (spider fittings): Countersunk or button-head bolts through drilled holes. Requires tempered or heat-strengthened glass. Typical bolt spacing: 900-1500 mm.
- Bolted connections: Through-bolts with neoprene gaskets. Stress concentration at bolt holes requires FEA analysis.
- Channel glazing (U-profile glass): Self-supporting channel glass for translucent facades. Spans up to 7 m vertically.

#### 8.2 Metal Cladding

| Material | Thickness Range | Max Panel Size | Key Properties |
|----------|----------------|---------------|----------------|
| Aluminum composite (ACM) | 3-6 mm total (0.5 mm skins) | 1500 x 5000 mm | Lightweight, foldable, fire rating concerns |
| Zinc | 0.7-1.5 mm | 1000 x 3000 mm | Self-healing patina, long life |
| Copper | 0.6-1.5 mm | 1000 x 3000 mm | Patina development, premium |
| Stainless steel | 0.5-3.0 mm | 1500 x 6000 mm | Durable, corrosion resistant |
| Perforated metal | 0.5-6.0 mm | 1500 x 3000 mm | Shading, screening, decorative |
| Expanded metal | 1.0-6.0 mm | 1250 x 2500 mm | 3D texture, directional transparency |
| Woven metal mesh | Wire dia 0.5-4.0 mm | Custom widths | Drapeable, large spans |
| Corten steel | 2.0-12.0 mm | 2500 x 12000 mm | Weathering patina, structural |

#### 8.3 Concrete

- **GFRC (Glass Fiber Reinforced Concrete)**: 10-15 mm thick panels. Lightweight (approximately 40 kg/m²). Complex shapes via mold casting. Maximum panel size: approximately 3 x 6 m. Surface finishes: smooth, textured, exposed aggregate, polished.
- **UHPC (Ultra-High Performance Concrete)**: 20-40 mm thick panels with compressive strength > 120 MPa. Extremely thin and strong. Can be left unreinforced in many applications. Suitable for complex geometry.
- **Precast concrete**: 75-200 mm thick panels. Heavy (180-500 kg/m²). Standard sizes up to 3.5 x 9 m. Requires crane erection.
- **3D printed concrete**: Emerging technology. Layer height: 10-30 mm. Maximum overhang angle: approximately 45° without support. Surface finish: visible layer lines (may be desired aesthetic). Currently limited to non-structural cladding.

#### 8.4 Timber

- **CLT (Cross-Laminated Timber) panels**: 60-300 mm thick. Structural and enclosure in one element. Maximum panel size: 3.5 x 16 m (limited by transport). Fire performance: achieves required ratings through charring calculations.
- **Glulam mullions**: Engineered timber members for facade structure. Span capability comparable to steel for moderate loads. Requires moisture protection at connections.
- **Acetylated wood (Accoya)**: Dimensional stability class 1 (minimal swelling/shrinking). 50-year durability above ground. Suitable for exterior cladding without additional treatment.
- **Thermally modified timber**: Heat-treated to 180-230°C. Improved durability and dimensional stability. Darker color. Reduced mechanical strength (10-30% loss).

#### 8.5 Composite and Membrane Materials

- **FRP (Fiber-Reinforced Polymer)**: Fiberglass or carbon fiber in polyester/epoxy matrix. Lightweight (1.5-2.0 g/cm³ vs. 2.7 for aluminum). Moldable to complex shapes. UV-resistant gel coat surface. Typical thickness: 3-8 mm for cladding panels.
- **ETFE cushions**: Ethylene tetrafluoroethylene film inflated into cushions between aluminum extrusion frames. Weight: 1-3 kg/m² (vs. 30+ for glass). Transparency: 85-95% for clear ETFE. Printable with frit patterns (variable shading by adjusting inflation to align/offset printed layers). Maximum cushion span: approximately 5 m. Design life: 25-30 years.
- **Polycarbonate**: Solid or multiwall sheets. Excellent impact resistance. Available in clear, translucent, and opaque. UV stabilized. Multiwall sheets provide thermal insulation (U = 1.0-3.0 W/m²K depending on wall count).

#### 8.6 Connection Systems

| System | Description | Speed | Cost | Tolerance Absorption | Thermal Break |
|--------|------------|-------|------|---------------------|---------------|
| **Unitized** | Factory-assembled frames with infill, hung on floor edge brackets | Fast | High | Good (stack joint, mullion joint) | Integral |
| **Stick-built** | Mullions and transoms assembled on site, infill glazed on site | Slow | Medium | Moderate | Add-on |
| **Point-fixed** | Glass bolted to spider fittings on steel structure | Medium | High | Low (requires precise structure) | At fitting |
| **Cable-net** | Pre-tensioned cable grid with point-fixed glass | Slow | Very high | Very low | At clamp |
| **Rainscreen** | Cladding panels on brackets with open or sealed joints | Medium | Low-Med | Good (bracket adjustment) | At bracket |

#### 8.7 Tolerance Management

Facade systems must accommodate tolerances from multiple sources:

| Source | Typical Tolerance | Accumulated at 60m Height |
|--------|------------------|---------------------------|
| Structural frame (concrete) | ±20 mm per floor | ±80 mm |
| Structural frame (steel) | ±10 mm per floor | ±40 mm |
| Facade bracket | ±15 mm adjustment range | — |
| Facade mullion | ±3 mm fabrication | — |
| Glass panel | ±1 mm cutting | — |
| Gasket/sealant | ±3 mm compression range | — |
| **Total system** | Must accommodate ±25 mm | — |

**Tolerance absorption strategy**: The facade bracket (angle or channel connecting facade to structure) is the primary tolerance absorption point. It must provide adjustment in three axes: ±15-25 mm in-out, ±10-15 mm vertical, ±10-15 mm lateral. Slotted holes and shim packs are standard methods.

#### 8.8 CNC Fabrication Constraints

- **CNC cutting (metal)**: Kerf width 3-8 mm (plasma), 0.2-0.5 mm (laser), 0.8-1.5 mm (waterjet). Minimum feature size: 1x material thickness. Minimum internal radius: 0.5x material thickness for laser, 2x for plasma.
- **Waterjet cutting**: Suitable for glass, stone, metal, composite. Taper angle: 0.5-2° (compensated by head tilt on 5-axis machines). Maximum material thickness: 200 mm for metal, 100 mm for glass.
- **Laser cutting**: Metal only (reflective metals like copper require fiber laser). Maximum thickness: 25 mm for mild steel, 15 mm for stainless steel, 12 mm for aluminum. Heat-affected zone: 0.1-0.5 mm.
- **CNC milling**: For molds (foam, MDF, aluminum). 3-axis for simple curves, 5-axis for compound curves and undercuts. Surface finish depends on tool path strategy (scallop height) and tool diameter.

---

### 9. Facade Performance Metrics

#### 9.1 Thermal Performance

| Metric | Unit | Description | Typical Range |
|--------|------|-------------|---------------|
| U-value | W/(m²·K) | Overall thermal transmittance | 0.7 - 5.8 |
| R-value | (m²·K)/W | Thermal resistance (1/U) | 0.17 - 1.43 |
| SHGC | dimensionless | Solar heat gain coefficient | 0.15 - 0.70 |
| VLT | % | Visible light transmittance | 10% - 80% |
| LSG | dimensionless | Light-to-solar gain ratio (VLT/SHGC) | 0.8 - 2.5 |
| Uf | W/(m²·K) | Frame U-value | 1.0 - 7.0 |
| Ug | W/(m²·K) | Glass center-of-pane U-value | 0.5 - 5.7 |
| Psi | W/(m·K) | Linear thermal transmittance (edge spacer) | 0.03 - 0.10 |

#### 9.2 Structural Performance

| Metric | Unit | Description | Typical Design Values |
|--------|------|-------------|----------------------|
| Wind load resistance | kPa | Maximum wind pressure | 1.0 - 6.0 kPa |
| Dead load | kg/m² | Self-weight of facade assembly | 25 - 120 |
| Live load (maintenance) | kN | Point load on glass for cleaning cradle | 1.0 kN per pad |
| Seismic drift | mm | Inter-story drift accommodation | ±15 - ±75 mm |
| Impact resistance | J | Soft body / hard body impact | Cat 1-5 (EN 14019) |
| Deflection limit | span/L | Maximum mullion deflection | L/175 to L/250 |

#### 9.3 Acoustic Performance

| Metric | Unit | Description | Typical Range |
|--------|------|-------------|---------------|
| STC | dimensionless | Sound Transmission Class (US/Canada) | 28 - 55 |
| Rw | dB | Weighted sound reduction index (ISO) | 28 - 55 |
| Ctr | dB | Spectrum adaptation term (traffic noise) | -3 to -10 |
| Rw + Ctr | dB | Traffic noise adjusted rating | 25 - 48 |
| OITC | dimensionless | Outdoor-Indoor Transmission Class | 25 - 45 |

#### 9.4 Fire Performance

| Classification | Standard | Description |
|---------------|----------|-------------|
| Non-combustible | ASTM E136, EN 13501-1 A1 | Does not contribute to fire (glass, steel, stone) |
| Limited combustible | ASTM E136 alternate | Minimal contribution (some composites) |
| Class A | ASTM E84 Class A | Flame spread index 0-25 |
| B-s1,d0 | EN 13501-1 | Very limited contribution, no smoke, no droplets |
| Fire-rated | BS 476, ASTM E119, EN 1364 | EI 30/60/90/120 rating |
| Cavity barrier | Local codes | Fire stops within rainscreen cavities |

#### 9.5 Durability and Sustainability

| Metric | Unit | Description | Typical Values |
|--------|------|-------------|----------------|
| Design life | years | Expected service life | 25 - 60 |
| Maintenance interval | years | Between major maintenance events | 5 - 15 |
| Sealant life | years | Expected sealant replacement cycle | 10 - 25 |
| Embodied carbon | kgCO2e/m² | Carbon footprint of materials and fabrication | 40 - 250 |
| Recyclability | % by mass | Proportion recoverable at end of life | 30 - 95% |
| LCA impact | Various | Full life cycle assessment categories | Per EN 15804 |
| Circular design | Qualitative | Design for disassembly and reuse potential | Score 1-5 |

#### 9.6 Performance Benchmarks by Facade Type

| Facade Type | U-value (W/m²K) | SHGC | STC | Weight (kg/m²) | Cost ($/m²) |
|-------------|-----------------|------|-----|----------------|-------------|
| Single glazed curtain wall | 5.5 | 0.80 | 28 | 25 | 300-500 |
| Double glazed curtain wall | 1.6-2.0 | 0.25-0.40 | 32-36 | 35-45 | 500-900 |
| Triple glazed curtain wall | 0.7-1.0 | 0.20-0.35 | 36-42 | 55-70 | 900-1500 |
| Double-skin facade | 0.8-1.5 | 0.10-0.30 | 42-55 | 80-120 | 1200-2500 |
| Unitized curtain wall | 1.2-1.8 | 0.20-0.40 | 34-40 | 40-60 | 700-1200 |
| Stone rainscreen | 0.25-0.35 | 0 (opaque) | 45-55 | 80-150 | 800-1500 |
| Metal rainscreen | 0.20-0.30 | 0 (opaque) | 38-48 | 25-50 | 400-900 |
| ETFE cushion | 1.5-2.8 | 0.50-0.85 | 15-20 | 3-5 | 400-800 |
| Structural glass | 1.8-2.5 | 0.30-0.65 | 30-38 | 30-50 | 1500-3500 |


## digital-fabrication

### Digital Fabrication

> CNC milling, robotic fabrication, additive manufacturing, laser cutting, timber joinery, formwork design, assembly sequencing, and file preparation for digitally-fabricated AEC components

## Digital Fabrication in AEC

### File-to-Factory Paradigm

Digital fabrication represents the direct translation of computational design models into physically realized building components through numerically controlled manufacturing processes. The file-to-factory paradigm eliminates the interpretive gap between designer intent and fabricator execution. Every geometric decision encoded in the digital model propagates deterministically into machine instructions, material removal paths, or deposition trajectories.

The core promise: what you model is what you build, with quantifiable tolerances at every stage.

#### Mass Customization vs. Mass Production

Traditional construction relies on mass production: standardized components (bricks, studs, sheets) assembled according to standardized details. This constrains architectural expression to rectangular grids and repetitive modules.

Mass customization inverts this constraint. When every component is cut by a CNC machine reading unique coordinates, the cost difference between 500 identical panels and 500 unique panels approaches zero. The machine does not care whether the next cut is the same as the last. The marginal cost of geometric variation is essentially the marginal cost of generating the fabrication data, not executing it.

Key economic thresholds:
- **Laser cutting**: Customization is virtually free. Nesting efficiency matters more than geometric repetition.
- **CNC milling**: Customization adds modest cost through increased setup and tool-change frequency.
- **Robotic fabrication**: Customization cost depends on end-effector changes and calibration overhead.
- **Additive manufacturing**: Customization is inherently free. Build time is the primary cost driver.
- **Formwork**: Customization is expensive for conventional formwork, cheap for CNC-milled or 3D-printed formwork.

#### The Design-to-Fabrication Pipeline

The digital chain from design to built reality proceeds through distinct data transformations:

1. **Design Model** — Parametric geometry in Rhino/Grasshopper, Revit, or other BIM/CAD environment. Geometry is resolution-independent (NURBS, BReps).
2. **Fabrication Model** — Geometry decomposed into manufacturable components with material assignments, joint definitions, tolerances, and assembly sequences. This is the critical translation step.
3. **Fabrication Data** — Machine-specific geometry: toolpaths (CNC), robot targets (robotic), slice contours (AM), cut lines (laser). Formats: G-code, RAPID, KRL, URScript, DXF, CLI, 3MF.
4. **Machine Code** — Post-processed instructions for a specific machine controller. Includes feed rates, spindle speeds, tool changes, safety interlocks.
5. **Physical Component** — Material transformed by machine. Subject to fabrication tolerances.
6. **Assembly** — Components joined on-site or in factory. Subject to assembly tolerances.

#### Material-Informed Design

Digital fabrication demands that designers understand material behavior at the fabrication scale:

- **Wood grain direction** determines CNC cutting strategy, joint strength, and surface quality.
- **Concrete rheology** determines printability window, layer adhesion, and maximum overhang angle.
- **Metal anisotropy** in AM builds (layer-parallel vs. layer-normal mechanical properties differ by 10-30%).
- **Polymer creep** in FDM parts means load-bearing orientation must align with print layers.
- **Foam density** (EPS 15-30 kg/m3, XPS 28-45 kg/m3, PU 30-80 kg/m3) determines cutting speed and surface quality.

#### Tolerance Stack-Up

Three tolerance domains must be managed simultaneously:

| Tolerance Type | Typical Range | Managed By |
|---|---|---|
| **Design tolerance** | +/- 0.5 - 2.0 mm | Architect/engineer |
| **Fabrication tolerance** | +/- 0.05 - 1.0 mm | Machine capability |
| **Assembly tolerance** | +/- 2.0 - 10.0 mm | Connection design |

The total system tolerance is the sum of all three. A CNC-milled joint with +/- 0.1 mm fabrication tolerance assembled with +/- 5 mm site tolerance yields a system tolerance of +/- 5.1 mm. The precision of the CNC operation is wasted unless the assembly detail absorbs the site tolerance through adjustable connections, shimming, or registration features.

**Rule**: Design the connection detail to absorb the largest tolerance in the chain. Never rely on fabrication precision to compensate for assembly imprecision.

---

## CNC Milling

### Machine Types

#### 3-Axis Machines
The spindle moves in X, Y, and Z. The workpiece is fixed. All tool orientations are vertical (tool axis = Z). Suitable for 2.5D work (profiling, pocketing, drilling) and 3D surface milling of gentle curvatures. Cannot undercut.

#### 4-Axis Machines
Adds one rotary axis (typically A-axis, rotating around X). Enables milling of cylindrical workpieces, wrapping toolpaths, and limited undercut access. Common for furniture legs, columns, and elongated sculptural elements.

#### 5-Axis Machines
Adds two rotary axes (A/B or A/C configuration). The tool can approach the workpiece from any direction within the machine's angular range. Enables true 3D milling of complex doubly-curved surfaces, undercuts, and multi-face machining without re-fixturing.

- **A/B configuration**: A rotates around X, B rotates around Y. Common on large gantry machines.
- **A/C configuration**: A tilts the spindle head, C rotates the table. Common on smaller machines. Better for continuous 5-axis contouring.

#### Gantry Routers
Large-format CNC machines with a bridge (gantry) spanning the work area. Typical work envelopes: 2.5m x 1.25m (half-sheet), 3.0m x 1.5m (full-sheet), 6.0m x 2.5m (architectural scale), up to 20m+ for shipbuilding and aerospace. AEC applications typically use 3-axis or 3+2 axis gantry routers for panel processing, timber framing, and foam milling.

### Workpiece Materials

| Material | Cutting Speed (m/min) | Feed per Tooth (mm) | Notes |
|---|---|---|---|
| Softwood (pine, spruce) | 300-600 | 0.3-0.8 | Grain tearout risk on cross-grain cuts |
| Hardwood (oak, walnut) | 200-400 | 0.15-0.5 | Higher tool wear, better finish |
| Plywood (birch) | 300-500 | 0.2-0.5 | Adhesive layers increase tool wear |
| MDF | 300-600 | 0.2-0.6 | Excellent surface, high dust |
| EPS Foam | 600-1200 | 1.0-3.0 | Very fast, minimal tool wear |
| XPS Foam | 500-1000 | 0.8-2.5 | Slightly denser than EPS |
| PU Foam (modeling board) | 300-600 | 0.3-1.0 | Depends on density |
| Acrylic (PMMA) | 100-300 | 0.05-0.15 | Single-flute preferred, coolant needed |
| Aluminum 6061 | 150-300 | 0.05-0.15 | Requires flood coolant or MQL |
| Brass | 100-200 | 0.05-0.12 | Good machinability |
| Stone (marble, limestone) | 20-80 | 0.02-0.08 | Diamond tooling, water coolant |
| GFRP | 100-300 | 0.05-0.15 | Diamond-coated or PCD tools, dust extraction critical |

### Tool Types

- **Flat End Mill**: Square bottom. Produces flat surfaces and sharp internal corners (with radius = tool radius). Most common for profiling and pocketing.
- **Ball Nose**: Hemispherical tip. For 3D surface finishing. Produces scalloped surface texture. Effective cutting diameter varies with depth of cut.
- **Bull Nose (Corner Radius)**: Flat bottom with radiused corners. Stronger than flat end mill, better surface finish on 3D surfaces than flat, less scalloping than ball nose.
- **Drill Bit**: Point geometry for plunge holes. Spot drill first for accuracy. Standard twist drills, brad-point for wood.
- **Slot Cutter (T-slot)**: For cutting T-slots, undercuts in 3-axis setups using horizontal approach.
- **V-Bit**: For engraving, chamfering, and V-carving. Common angles: 60 degrees, 90 degrees, 120 degrees.
- **Compression Bit**: Up-cut on bottom, down-cut on top. For clean edges on both faces of sheet goods.

### Milling Strategies

#### 2.5D Operations
- **Profile/Contour**: Cutting along a 2D path at constant Z-depth. Outside profile (part perimeter), inside profile (pocket perimeter), on-line (for slots).
- **Pocketing**: Removing material from an enclosed area. Strategies: zigzag, offset (spiral), offset with climb), adaptive (trochoidal).
- **Drilling**: Point-to-point operations. Peck drilling for deep holes (retract to clear chips).

#### 3D Roughing
- **Adaptive (High-Efficiency) Roughing**: Trochoidal toolpath maintaining constant tool engagement angle. Reduces vibration and tool wear. Allows higher axial depth of cut. Preferred for hard materials and deep pockets.
- **Parallel Roughing**: Simple back-and-forth passes at decreasing Z-levels. Fast calculation, predictable. Leaves staircase approximation of 3D surface.
- **Waterline/Z-Level Roughing**: Horizontal slicing at constant Z. Good for steep walls. Poor for shallow areas.

#### 3D Finishing
- **Parallel Finishing**: Straight passes across the surface. Best for gently curved surfaces. Direction matters (align with longest dimension for efficiency).
- **Spiral Finishing**: Continuous spiral from outside to center (or vice versa). No retract marks. Good for radially symmetric forms.
- **Scallop Finishing**: Constant scallop height across the surface. Adapts stepover to local curvature. Most uniform surface quality but complex toolpath.
- **Pencil Finishing**: Traces the bottom of concavities and tight corners. Used as a cleanup pass after parallel or scallop finishing.
- **Flow-Line Finishing**: Follows surface UV directions. Best for surfaces with natural flow (automotive-style).

### Speed and Feed Calculation

Spindle speed (RPM):
```
RPM = (Vc * 1000) / (pi * D)
```
Where Vc = cutting speed (m/min), D = tool diameter (mm).

Feed rate (mm/min):
```
F = RPM * z * fz
```
Where z = number of flutes, fz = feed per tooth (chip load, mm).

#### Chip Load Reference Table

| Material | 6mm 2-flute (fz mm) | 10mm 2-flute (fz mm) | 12mm 3-flute (fz mm) |
|---|---|---|---|
| Softwood | 0.3-0.5 | 0.4-0.7 | 0.3-0.6 |
| Hardwood | 0.15-0.3 | 0.2-0.4 | 0.15-0.35 |
| Plywood | 0.2-0.4 | 0.3-0.5 | 0.2-0.4 |
| MDF | 0.2-0.4 | 0.3-0.5 | 0.2-0.4 |
| EPS Foam | 1.0-2.0 | 1.5-3.0 | 1.0-2.5 |
| Acrylic | 0.05-0.1 | 0.08-0.12 | 0.05-0.1 |
| Aluminum | 0.04-0.08 | 0.06-0.12 | 0.04-0.1 |

### Surface Finish

Scallop height for ball-nose finishing:
```
h = r - sqrt(r^2 - (stepover/2)^2)
```
Where r = ball nose radius (mm), stepover = distance between adjacent passes (mm).

Practical targets:
- **Rough**: h = 0.5-1.0 mm, stepover = 50-70% of tool diameter
- **Semi-finish**: h = 0.1-0.3 mm, stepover = 20-40% of tool diameter
- **Fine finish**: h = 0.02-0.05 mm, stepover = 5-15% of tool diameter

### Workholding

- **Vacuum Table**: Best for sheet goods. Requires spoilboard gasket or zone control. Minimum part size depends on vacuum force (typically > 150mm x 150mm for reliable hold).
- **Mechanical Clamps**: T-slot or fixture plate. Requires clearance around clamps for tool access. Risk of clamp collision.
- **Screws Through Spoilboard**: Drill registration holes, screw material down. Simple, reliable. Leaves screw holes in part (place outside finish area).
- **Double-Sided Tape**: For small parts or finishing operations. Limited holding force. 3M 468MP or similar.
- **Custom Jigs**: 3D-printed or CNC-milled fixtures for irregular workpieces. Essential for 5-axis work on non-prismatic parts.
- **Registration Pins**: Dowel pins in spoilboard for repeatable part placement. Critical for double-sided machining (flip operations).

### 5-Axis Considerations

- **Tool orientation vectors**: Defined by tool axis (I, J, K) at each toolpath point. Must be smooth (no sudden flips).
- **Collision avoidance**: Check tool holder, spindle housing, and machine head against workpiece and clamps. Most CAM software includes simulation.
- **Lead and lag angles**: Tilting the tool slightly (3-15 degrees) in the feed direction (lead) or perpendicular (lean) improves surface finish and avoids cutting with the tool tip (zero-velocity point on ball nose).
- **A/B vs. A/C kinematics**: Affects reachable orientations and singularity positions. A/C machines have a singularity when A = 0 (vertical). A/B machines have a singularity when the two rotary axes align.

---

## Robotic Fabrication

### Industrial Robots for AEC

#### Robot Models

| Robot | Reach (mm) | Payload (kg) | Repeatability (mm) | Typical AEC Use |
|---|---|---|---|---|
| ABB IRB 4600-60 | 2050 | 60 | +/- 0.05 | Milling, small assembly |
| ABB IRB 6700-235 | 2650 | 235 | +/- 0.05 | Heavy assembly, large milling |
| ABB IRB 7600-500 | 2550 | 500 | +/- 0.05 | Concrete printing, heavy lifting |
| KUKA KR 120 R2700 | 2701 | 120 | +/- 0.05 | General fabrication |
| KUKA KR 210 R3100 | 3100 | 210 | +/- 0.06 | Timber assembly, large components |
| KUKA KR 600 R2830 | 2826 | 600 | +/- 0.08 | Heavy payload tasks |
| UR10e | 1300 | 12.5 | +/- 0.03 | Light assembly, collaborative tasks |
| UR16e | 900 | 16 | +/- 0.03 | Heavier collaborative tasks |
| Fanuc M-20iD/25 | 1831 | 25 | +/- 0.02 | Precision assembly, welding |
| Fanuc M-710iC/50 | 2050 | 50 | +/- 0.07 | General fabrication |

#### Robot Anatomy

A standard 6-axis articulated robot has:
- **J1 (Base)**: Rotation around vertical axis. Defines the robot's rotational workspace.
- **J2 (Shoulder)**: Rotation of the lower arm. Primary reach determinant.
- **J3 (Elbow)**: Rotation of the upper arm. Works with J2 for radial reach and height.
- **J4 (Wrist 1)**: Rotation of the wrist around the forearm axis. Adds dexterity.
- **J5 (Wrist 2)**: Tilting of the wrist. Enables tool orientation changes.
- **J6 (Wrist 3)**: Rotation of the tool flange. Final orientation adjustment.

**Reach envelope**: The set of all points the tool center point (TCP) can reach. Not a simple sphere; it has dead zones near the base and at full extension. Always verify reach in simulation before programming.

**Payload**: Maximum mass at the tool flange including end effector and workpiece (if carried). Payload capacity decreases with distance from J6 axis (moment loading). Check both mass and moment of inertia.

**Repeatability vs. Accuracy**: Repeatability (+/- 0.05 mm typical) is how consistently the robot returns to a taught point. Accuracy (often +/- 0.5-2.0 mm) is how close it gets to a commanded Cartesian point. Accuracy is worse than repeatability because of kinematic model errors, gear backlash, and deflection. Calibration improves accuracy to +/- 0.2-0.5 mm.

### End Effectors

- **Spindle**: HSD, Hiteco, or Jager. 1-24 kW, 1,000-40,000 RPM. For robotic milling. Requires automatic tool changer (ATC) for multi-tool operations.
- **Extruder**: Auger, piston, or peristaltic pump. For concrete printing, clay printing, polymer printing. Temperature-controlled for thermoplastics.
- **Gripper**: Mechanical (parallel, angular), vacuum (suction cups), magnetic (for steel). For pick-and-place of bricks, blocks, panels, timber members.
- **Welding Torch**: MIG/MAG for WAAM (Wire Arc Additive Manufacturing). TIG for precision welding. Fronius CMT (Cold Metal Transfer) preferred for WAAM.
- **Hot-Wire Cutter**: Heated nichrome or kanthal wire mounted on a frame. For EPS/XPS foam cutting. Wire temperature 200-400 C. Produces smooth surfaces on foam.
- **Spray Nozzle**: For shotcrete application on mesh formwork. Requires concrete pump integration.

### Programming Approaches

#### Online Programming (Teach Pendant)
Move the robot manually to desired positions, record waypoints. Suitable for simple repetitive tasks. Not practical for complex AEC fabrication with thousands of unique targets.

#### Offline Programming (Simulation)
Model the entire workcell (robot, workpiece, fixtures, end effector) in software. Program toolpaths in the virtual environment. Simulate and verify before sending to the physical robot. Essential for AEC applications.

#### Grasshopper Plugins

**HAL Robotics** (multi-brand):
- Procedure components: define motion sequences
- Target components: Cartesian targets with tool orientation
- Solver: inverse kinematics, collision detection, singularity checking
- Export to RAPID, KRL, URScript, and others
- Real-time control mode for adaptive fabrication

**KUKA|prc** (KUKA-specific):
- Core component: defines robot cell (robot model, base, tool, external axes)
- Movement commands: LIN, PTP, CIRC, SPLINE
- Analog/digital I/O control for end effectors
- SRC/DAT file generation for KRC controller
- Virtual axis for linear track (7th axis)

**Robots by Visose** (multi-brand):
- Open-source Grasshopper plugin
- Supports ABB, KUKA, UR, Fanuc, Staubli
- Robot cell definition, target generation, simulation
- Post-processing to native robot code
- Flexible and extensible architecture

### Coordinate Systems

- **World**: Fixed reference frame of the workcell. All other frames reference this.
- **Base**: Origin of the robot (J1 base). May differ from world if robot is mounted on a track or pedestal.
- **Tool (TCP)**: The active point of the end effector. Must be calibrated precisely. For a spindle, TCP is the tool tip. For a gripper, TCP is the grasp center.
- **Workpiece (Work Object)**: The coordinate system of the part being fabricated. Define this by touching three points on the workpiece (origin, X-direction, XY-plane point).
- **User Frame**: An arbitrary reference frame for organizing targets. Useful when the same program must run on different workpieces at different locations.

### Motion Types

- **PTP (Point-to-Point / Joint)**: Each joint moves independently to reach the target. Path is not a straight line in Cartesian space. Fastest motion. Use for large repositioning moves.
- **LIN (Linear)**: TCP moves in a straight line in Cartesian space. Required for fabrication operations (milling cuts, extrusion paths, welding seams). Slower than PTP due to coordinated joint motion.
- **CIRC (Circular)**: TCP follows a circular arc through three points (start, via, end). For circular toolpaths.
- **SPLINE**: Smooth continuous motion through multiple targets. Minimizes acceleration/deceleration. Best for continuous processes like extrusion and painting.

### Singularity Avoidance

Singularities occur when the robot loses one or more degrees of freedom. Three types:
- **Overhead singularity**: J5 = 0 (wrist axes J4 and J6 align). Causes infinite solutions for J4/J6 split.
- **Extended singularity**: Robot at full reach (J2 and J3 align the lower and upper arm).
- **Base singularity**: TCP directly above J1 (J1 rotation does not change TCP position).

Avoidance strategies:
- Offset the tool orientation by a small angle to prevent J5 = 0.
- Limit the workspace to avoid full extension.
- Use PTP motion through singular zones when Cartesian path is not critical.
- In HAL/KUKA|prc, enable singularity avoidance algorithms that perturb targets near singularities.

### Safety

- **ISO 10218-1/2**: Safety requirements for industrial robots and robot systems.
- **ISO/TS 15066**: Collaborative robot safety (force and pressure limits).
- Safeguarding: physical fencing (minimum 1.4m height), light curtains, safety-rated laser scanners, pressure-sensitive mats.
- E-stop buttons within reach from all access points.
- Safety-rated monitored stop for collaborative zones.
- Risk assessment required before commissioning any robotic workcell.

### AEC Applications

- **Bricklaying**: Pick-and-place of bricks with adhesive. Projects: ETH ROB Technologies, Fastbrick Robotics.
- **Timber Assembly**: Robotic placement and fastening of timber members. Spatial timber structures.
- **Concrete Printing**: Large-scale extrusion of cementitious material. Layer-by-layer wall construction.
- **Steel Welding**: Robotic MIG/MAG for steel node fabrication and WAAM.
- **Foam Milling**: Robotic CNC of formwork from EPS/XPS blocks. Extended reach vs. gantry CNC.
- **Fiber Winding/Placement**: Carbon or glass fiber wound around a mandrel or between anchor points. ICD/ITKE research pavilions.
- **In-situ Fabrication**: Robots mounted on mobile platforms for on-site construction. NCCR Digital Fabrication.

---

## Additive Manufacturing

### Polymer AM

#### FDM/FFF (Fused Deposition Modeling / Fused Filament Fabrication)

| Material | Nozzle Temp (C) | Bed Temp (C) | Tensile Strength (MPa) | Notes |
|---|---|---|---|---|
| PLA | 190-220 | 50-60 | 50-65 | Biodegradable, low warp, brittle |
| ABS | 230-250 | 100-110 | 35-50 | Warps, needs enclosure, acetone-smoothable |
| PETG | 230-250 | 70-80 | 45-55 | Good balance of strength and printability |
| Nylon (PA6) | 250-270 | 70-90 | 70-85 | Strong, flexible, hygroscopic |
| TPU | 220-240 | 40-60 | 25-50 | Flexible, abrasion-resistant |
| PC | 260-300 | 110-130 | 55-70 | High heat resistance, tough |
| ASA | 240-260 | 90-110 | 40-55 | UV-resistant ABS alternative |
| CF-Nylon | 250-280 | 70-90 | 90-120 | Stiff, strong, abrasive to nozzles |

#### SLA (Stereolithography)
UV laser cures liquid photopolymer resin layer by layer. Resolution: 25-100 micron layers. Excellent surface finish. Brittle standard resins. Engineering resins (tough, flexible, high-temp, ceramic-filled) available. Post-curing required under UV light.

#### SLS (Selective Laser Sintering)
Laser sinters nylon powder (PA11, PA12). No support structures needed (unsintered powder supports the part). Isotropic mechanical properties. Good for functional parts. Surface texture is grainy. Resolution: 100-150 micron layers.

### Concrete AM

#### Technologies

- **Contour Crafting** (Behrokh Khoshnevis, USC): One of the earliest large-scale approaches. Trowel-smoothed extrusion.
- **D-Shape** (Enrico Dini): Binder jetting on sand. Full 3D capability (not layer-by-layer extrusion). Limited structural capacity.
- **COBOD BOD2**: Gantry-style printer. Build volume up to 12m x 45m x variable height (modular). Used commercially for housing.
- **ICON Vulcan**: Gantry printer designed for residential construction. Lavacrete proprietary material. 60-90 m2 home in days.
- **WASP Crane WASP**: Delta/crane configuration. Prints with local earth-based materials (clay, natural fibers). Sustainable approach.

#### Concrete Mix Design for Printing
- **Extrudability**: Material must flow through the pump and nozzle without blocking. Aggregate size < 40% of nozzle diameter.
- **Buildability**: Layers must support their own weight and subsequent layers without collapse. Yield stress > 1.5 kPa initially, increasing rapidly.
- **Open time**: The window during which material remains workable. Typically 30-90 minutes depending on accelerator dosage.
- **Layer adhesion**: Subsequent layers must bond chemically. Cold joint risk if interlayer time > open time. Surface moisture helps.
- **Typical mix**: OPC 500-700 kg/m3, fly ash 100-200 kg/m3, silica fume 50-80 kg/m3, sand 1000-1400 kg/m3, water/binder ratio 0.3-0.4, superplasticizer 1-2%, accelerator as needed.

### Metal AM

- **DMLS/SLM**: Laser melts metal powder layer by layer. Materials: 316L stainless, maraging steel, AlSi10Mg, Ti6Al4V, Inconel 718. Layer thickness: 20-60 microns. Build rate: 5-30 cm3/hr. Post-processing: stress relief, HIP, support removal, surface machining.
- **WAAM (Wire Arc AM)**: Robot with MIG/MAG torch deposits weld beads layer by layer. Wire feedstock (steel, aluminum, titanium, bronze). Deposition rate: 1-10 kg/hr. Near-net shape requires finish machining. Lower resolution but much faster and cheaper for large parts.
- **DED (Directed Energy Deposition)**: Laser or electron beam melts wire or powder as it is deposited. For adding material to existing parts (repair) or building large components.

### Design for AM

#### Overhang Rules
- **FDM**: Maximum unsupported overhang angle 45 degrees from vertical. Beyond this, support structures required. Bridges (horizontal spans between two supports) up to 10-20 mm possible.
- **Concrete**: Maximum overhang per layer 5-15 mm (depends on layer width and material stiffness). Cantilever angle limited to approximately 15-20 degrees without support.
- **Metal SLM**: 45 degrees standard. Some materials and machines can achieve 30 degrees. Critical for minimizing support structures in complex nodes.

#### Minimum Wall Thickness
- FDM: 0.8-1.2 mm (2-3 perimeters)
- SLA: 0.4-0.6 mm
- SLS: 0.7-1.0 mm
- Concrete: 20-60 mm (depends on aggregate size and nozzle width)
- Metal SLM: 0.3-0.5 mm

#### Build Orientation
Optimize for: minimum support, best surface quality on critical faces, strongest direction aligned with primary loads, minimum build height (= time).

### Print Parameters

| Parameter | FDM Typical | Concrete Typical |
|---|---|---|
| Layer height | 0.1-0.3 mm | 10-40 mm |
| Layer width | 0.4-0.8 mm | 30-80 mm |
| Print speed | 40-100 mm/s | 50-300 mm/s |
| Infill | 15-50% | N/A (solid walls) |
| Wall count | 2-4 | N/A |
| Temperature | 190-300 C | Ambient |
| Nozzle diameter | 0.4-1.0 mm | 20-60 mm |

#### Infill Patterns
- **Rectilinear**: Grid pattern. Fast to print. Weak on shear.
- **Honeycomb**: Hexagonal cells. Good strength-to-weight. Slower to print.
- **Gyroid**: Triply periodic minimal surface. Isotropic strength. Good for structural parts.
- **Triangular**: Strong in compression. Good for load-bearing parts.
- **Lightning**: Tree-like infill optimized for top surface support only. Lightest, fastest.

### Scale Categories

- **Desktop** (< 300 mm build volume): Prototyping, models, small components. Prusa, Bambu Lab, Formlabs.
- **Large-format** (300 mm - 1 m): Furniture, fixtures, large prototypes. BigRep, Modix, Massivit.
- **Architectural** (> 1 m): Building components and structures. Robotic arm or gantry systems. COBOD, ICON, WASP, custom robotic setups.

### Post-Processing

- **Support removal**: Break-away (FDM), dissolve (PVA/HIPS), wash (SLA), cut/grind (metal).
- **Surface finishing**: Sanding, bead blasting, vapor smoothing (acetone for ABS), coating/painting.
- **Annealing**: Heat treatment to improve crystallinity and strength (PLA, nylon). Temperature and duration vary by material.
- **Machining**: CNC finishing of AM parts for tight tolerance features (holes, mating surfaces).
- **Infiltration**: Epoxy or cyanoacrylate for SLS parts to improve surface and water resistance.

---

## Laser Cutting

### Materials and Capabilities

| Material | Max Thickness (CO2) | Kerf (mm) | Edge Quality | Notes |
|---|---|---|---|---|
| Acrylic (cast) | 25 mm | 0.15-0.25 | Flame-polished | Best laser material |
| Acrylic (extruded) | 15 mm | 0.15-0.25 | Matte | Cheaper, lower quality |
| Plywood (birch) | 18 mm | 0.15-0.30 | Charred edge | Speed limits thickness |
| MDF | 12 mm | 0.15-0.25 | Clean | Dark edge, fiber material |
| Cardboard | 3 mm | 0.10-0.20 | Clean | Fast, for models |
| Paper | 0.5 mm | 0.05-0.15 | Clean | Very fast |
| Fabric | 5 mm | 0.10-0.20 | Sealed edge | Prevents fraying |
| Mild steel | 20 mm (fiber) | 0.10-0.20 | Oxide or clean | Fiber laser preferred |
| Stainless steel | 12 mm (fiber) | 0.10-0.20 | Clean with N2 | Nitrogen assist |
| Aluminum | 10 mm (fiber) | 0.10-0.20 | Reflective, difficult | Fiber laser required |

### Design Rules

- **Minimum feature size**: Generally 1.5x material thickness for stability. Minimum kerf-width features at 0.15 mm.
- **Tab connections**: Leave small tabs (0.5-2 mm) connecting parts to the sheet to prevent small parts from falling/shifting during cutting.
- **Living hinges**: Parallel kerf cuts allowing sheet material to bend. Pattern: slots 0.5-1.0 mm wide, spaced 2-4 mm apart, offset between rows. Material: plywood, acrylic, PP.
- **Finger joints**: Interlocking rectangular tabs for box construction. Tab width = material thickness (minimum). Kerf compensation: reduce tab width by kerf/2 on each side.
- **Slot connections**: Mortise-and-tenon style joints in sheet material. Slot width = material thickness + kerf allowance.
- **Minimum distance between cuts**: 1 mm for acrylic, 2 mm for wood (heat-affected zone).

### Nesting

- **Rectangular nesting**: Simple grid arrangement. Fast to compute. 60-75% material utilization typical.
- **True-shape nesting**: Algorithm rotates and translates parts to minimize waste. Tools: DeepNest (free, open-source), SigmaNEST, NestFab. 75-90% material utilization.
- **Grain-aware nesting**: For plywood and veneer, constrain part rotation to align with grain direction (0 or 90 degrees only).
- **Common-line cutting**: Adjacent parts share a single cut line. Saves time and material. Requires careful kerf compensation.

### File Preparation

- **Format**: DXF or DWG preferred. AI (Adobe Illustrator) and SVG also accepted by many services.
- **Line colors/layers for operations**: Red = cut through, Blue = engrave (raster), Green = score (light cut), Black = mark. Convention varies by shop; always confirm.
- **Line type**: All geometry must be continuous closed polylines for cuts. No duplicate lines (double cutting wastes time and chars edges).
- **Scale**: Verify units. DXF files often lose unit information. Include a known dimension for verification.
- **Kerf compensation**: Either apply in the design file (offset outlines out by kerf/2, inlines in by kerf/2) or let the machine operator apply it. Never both.

### Laser Types

- **CO2 laser**: 10.6 micron wavelength. Cuts organics (wood, acrylic, fabric, paper) excellently. Cannot cut metals efficiently. Power: 30-400W typical.
- **Fiber laser**: 1.06 micron wavelength. Cuts metals efficiently. Can cut organics but edge quality is inferior to CO2 for non-metals. Power: 500-12,000W.
- **Diode laser**: Low power (5-20W typically). For engraving and cutting thin materials (< 5 mm wood). Desktop hobby machines.

---

## Timber Digital Fabrication

### CNC Timber Joints

Digital fabrication enables the revival and enhancement of traditional timber joinery. CNC machines cut joints with sub-millimeter precision that would require hours of hand work.

#### Joint Types

- **Mortise and Tenon**: Rectangular pocket (mortise) receives projecting member (tenon). CNC-cut mortises have radiused corners (= tool radius). Design tenon corners to match, or use overcut (dog-bone) relief.
- **Dovetail**: Angled tenon resists withdrawal. Requires 5-axis or tilted spindle for angled cuts. Through-dovetail and half-blind dovetail variations.
- **Scarf Joint**: End-to-end joining of members. Types: plain scarf, halved scarf, stop-splayed scarf, keyed scarf. CNC-cut scarf joints can include complex interlocking geometry.
- **Finger Joint**: Multiple interlocking rectangular projections. High glue surface area. Structural finger joints per EN 15497.
- **Lap Joint**: Overlapping members with half-depth housings. Cross-lap, end-lap, half-lap. Simple 3-axis CNC operation.
- **Dado / Housing**: Groove across grain to receive a perpendicular member. Common for shelving and panel-to-frame connections.
- **Through-Tenon with Wedge**: Tenon passes through the mortise and is locked by a wedge. Self-tightening joint. Visible detail.

#### Dog-Bone and T-Bone Fillets

CNC-cut internal corners have a radius equal to the tool radius. To ensure mating parts fit, add relief cuts at corners:
- **Dog-bone**: Circular relief at each corner. Radius = tool radius. Visible but effective.
- **T-bone**: Relief cut extends along one edge. Less visible than dog-bone. Choose the less visible edge.
- **Mouse-ear**: Small circular relief on the corner. Smallest visual impact. May not provide full clearance for tight fits.

### Multi-Axis Timber Processing Machines

- **Hundegger ROBOT-Drive**: 6-axis robot + spindle for complex timber joinery. Processes beams up to 1.25m wide. Automatic tool change.
- **Hundegger TURBO-Drive**: 5-axis CNC for timber frame production. High throughput. Processes entire beam libraries.
- **Weinmann WBS 120/140**: CNC bridge for timber frame wall panel production. Nailing, screwing, routing, sawing.
- **Technowood**: Specialized timber CNC machines for CLT, glulam, and solid timber. 5-axis processing.

### CLT Fabrication

Cross-Laminated Timber panels are produced in factory conditions and CNC-processed to include:
- Panel perimeter cuts (any shape, not just rectangular)
- Window and door openings
- Service penetrations (MEP rough-ins)
- Connection details (screws, dowels, dovetail surface connectors)
- Half-lap joints at panel-to-panel edges
- Inclined cuts for roof panels

CLT machines process panels up to 3.5m wide, 16m long, and 400mm thick. Processing accuracy: +/- 1 mm.

### Glulam CNC

Glued Laminated Timber beams can be CNC-processed for:
- Curved beams: laminated to curvature, then CNC-finished for precise geometry
- Double-curved members: CNC-milled from oversized blanks (significant waste)
- Connection details: bolt holes, notches, bearing surfaces
- Complex nodes: multi-member connections carved from large glulam blanks

### Timber Plate Structures

An emerging typology where thin timber plates (plywood, LVL) are CNC-cut and assembled into spatial structures without a primary frame:
- **Folded plate structures**: Plates connected along edges to form rigid folded geometry. Connections by through-tenons, screws, or integral timber connectors.
- **Interlocking plates**: Slot-based connections where plates pass through each other. No fasteners required for geometry; fasteners added for structural capacity.
- **Timber plate shells**: Doubly-curved shell structures assembled from planar plates. Each plate unique. Assembly sequence critical.

Research reference: IBOIS (EPFL), ICD/ITKE Stuttgart.

### Design for CNC Timber

- **Minimum feature size**: 3x tool diameter for pockets. Minimum 8 mm wall thickness for load-bearing elements.
- **Grain direction**: Always consider grain orientation relative to cut direction and structural loads. Cross-grain cuts weaker than parallel-grain.
- **Tool reach**: Pocket depth limited by tool length minus chuck grip. Typically max 50-80 mm for standard tools.
- **Assembly sequence**: Design joints so assembly is sequential without requiring simultaneous multi-point engagement (which is physically impossible).
- **Moisture content**: CNC timber at 10-14% MC. Dimension changes of 0.15-0.30% per 1% MC change across grain. Joint tolerances must accommodate seasonal movement.
- **Surface quality**: Climb milling produces better finish on timber. Down-cut spiral bits minimize tear-out on the top face.

---

## Formwork Design

### Conventional Formwork

- **Plywood formwork**: Birch plywood (film-faced for smooth concrete finish). Standard panels 1220 x 2440 mm. Reusable 5-20 times with care. Cost: low per use.
- **Steel formwork**: For repetitive elements (columns, walls). Very high reuse count (200+). Heavy, requires crane. Excellent surface finish. Cost: high initial, low per use at volume.
- **Aluminum formwork**: Lighter than steel. Good for slabs and walls. Moderate reuse (80-150). Growing in residential construction.

### CNC-Milled Formwork

For complex non-repetitive geometry, CNC-milling formwork from foam or MDF is cost-effective:

#### Positive Mold Workflow
1. Mill the desired concrete surface shape directly into EPS/XPS foam blocks.
2. Apply surface coating (polyurea, fiberglass, or plasticizer) for smooth finish and release.
3. Cast concrete against the coated foam.
4. Strip foam after curing. Foam is typically destroyed (single use).

#### Negative Mold Workflow
1. Mill the inverse shape into foam.
2. Vacuum-form or lay up GFRP shell against foam.
3. Use GFRP shell as the reusable formwork.
4. GFRP mold can be reused 20-100 times.

#### Cost Factors
- Foam material: $30-80/m3 (EPS), $80-200/m3 (XPS), $150-500/m3 (PU tooling board)
- CNC time: $50-200/hour depending on machine
- Coating: $20-50/m2
- Competitive with conventional formwork when more than 10-15% of panels are unique geometry

### 3D-Printed Formwork

- **Lost formwork**: Printed plastic shell filled with concrete. Shell remains as permanent casing. PLA, PETG, or sand-printed molds. Enables internal channels and complex internal geometry.
- **Reusable 3D-printed molds**: Printed from durable materials (ABS, nylon, HDPE) for repeated casting. Limited to smaller elements due to print size constraints.
- **Sand 3D printing**: Binder-jet printed sand molds (ExOne, Voxeljet). Large build volumes. Excellent for complex concrete casting. Single-use molds with recyclable sand.

### Flexible Formwork

#### Fabric-Formed Concrete
- Fabric membranes (geotextile, polypropylene, custom-woven) used as formwork. Concrete fills the fabric and cures into the membrane shape.
- Produces organic, structurally optimized forms (catenary curves, variable-section beams).
- Surface texture inherits fabric weave pattern.
- Typically requires some rigid framing to control key dimensions.
- Research: CAST (University of Manitoba), Mark West.

#### Cable-Net Formwork
- A network of cables defines a doubly-curved surface. Fabric or panels attached to cables. Concrete sprayed or cast against the surface.
- Enables large-span shell structures with minimal material.
- Requires accurate cable pre-tensioning and anchor design.

### Robotic Shotcrete on Mesh

- Steel mesh (rebar or welded wire) defines the form.
- Robot sprays shotcrete against the mesh. Layer by layer, building up thickness.
- Mesh stays inside as reinforcement.
- Enables double-curved concrete surfaces without traditional formwork.
- Research: ETH Zurich (Mesh Mould).

### Slip Forming

- Continuously moving formwork for vertical structures (cores, towers, chimneys, silos).
- Formwork rises at 150-300 mm/hour as concrete cures.
- Requires continuous concrete supply and 24-hour operation.
- Produces smooth vertical surfaces with no horizontal joints.
- Can produce tapered and curved-plan forms with adjustable formwork.

### Cost Comparison

| Formwork Type | Geometry Complexity | Cost per m2 (simple) | Cost per m2 (complex) | Reuse |
|---|---|---|---|---|
| Plywood | Low | $20-40 | $60-120 | 5-20 |
| Steel | Low | $15-30 (amortized) | N/A | 200+ |
| Aluminum | Low-Medium | $20-40 (amortized) | N/A | 80-150 |
| CNC foam (EPS) | High | $40-80 | $80-200 | 1 |
| CNC foam + GFRP | High | $100-200 | $150-400 | 20-100 |
| 3D-printed (plastic) | Very High | $80-200 | $150-500 | 1-10 |
| 3D-printed (sand) | Very High | $200-600 | $300-1000 | 1 |
| Fabric | Medium | $15-40 | $30-80 | 1-5 |

---

## Assembly and Logistics

### Assembly Sequencing

Assembly sequence determines which component is placed first, second, and so on. A valid assembly sequence must satisfy:
- **Accessibility**: Each component can be moved into position without passing through already-placed components.
- **Stability**: The partially assembled structure is stable at every step (or temporarily braced).
- **Connection feasibility**: Fasteners/adhesives can be applied in the required sequence.

#### Sequencing Algorithms
- **Reverse disassembly**: Find a valid disassembly sequence (remove one part at a time), then reverse it.
- **Precedence graph**: Directed acyclic graph (DAG) where edges represent "must be placed before" constraints. Topological sort gives valid sequences.
- **Geometric blocking analysis**: For each component, check which directions it can be moved without collision. A component is removable if it has at least one unblocked direction.

### Connection Design

| Connection Type | Speed | Adjustability | Tools Required | Reversible |
|---|---|---|---|---|
| Dry interlock | Fast | None | None | Yes |
| Bolted | Moderate | Good (slotted holes) | Wrench/impact driver | Yes |
| Screwed | Moderate | Limited | Drill driver | Partially |
| Welded | Slow | None | Welding equipment | No |
| Glued (structural) | Slow (curing) | None during cure | Clamps | No |
| Clip/snap-fit | Very fast | None | None | Some designs |

Design principle: Choose the fastest reversible connection type that meets structural requirements. Dry interlocking joints designed by CNC are fastest and most reversible.

### Transport Constraints

#### Road Transport
- **Standard truck (EU)**: 2.55m W x 3.0m H x 13.6m L, max payload 24-26 tonnes
- **Standard truck (US)**: 2.6m W x 4.1m H x 16.2m L, max payload 20-22 tonnes
- **Oversize load**: Requires special permits, escort vehicles, route planning. Cost increases significantly.
- **Standard container (20ft)**: 2.35m W x 2.39m H x 5.9m L, max payload 21.7 tonnes
- **Standard container (40ft HC)**: 2.35m W x 2.69m H x 12.03m L, max payload 26.5 tonnes

#### Design for Transport
- Maximize packing density: design component dimensions to fill truck/container efficiently.
- Stack flat panels. Nest curved panels. Bundle linear elements.
- Protect edges and surfaces: foam, cardboard, plastic wrap.
- Load order = reverse of assembly order (first-needed on top/outside).

### Lifting and Crane Selection

| Crane Type | Capacity | Reach | Use Case |
|---|---|---|---|
| Tower crane | 2-20 tonnes at tip | 30-80m | Multi-story buildings |
| Mobile crane | 5-500 tonnes | 10-100m | Single lifts, precast |
| Crawler crane | 50-3,000 tonnes | 20-120m | Heavy lifts, large precast |
| Telehandler | 3-5 tonnes | 10-20m | Low-rise, light elements |
| Manual (team lift) | < 25 kg per person | N/A | Small components |

Lifting design: embed lift anchors (Halfen, Deha) or design lift points into the component geometry. Factor of safety on lift anchors: minimum 4:1.

### Element Numbering and Marking

- **Naming convention**: Building-Level-Zone-Type-Number (e.g., B1-L03-ZA-WP-042 = Building 1, Level 3, Zone A, Wall Panel 42).
- **Physical marking**: Sticker labels, CNC-engraved text, paint/ink marks. Include: element ID, weight, orientation arrows ("this side up", "this side out"), lifting points.
- **Digital marking**: QR codes linking to digital twin, BIM model, or assembly instructions.
- **Coordinate marking**: Reference points on elements that correspond to survey points on site.

### Assembly Tolerance Management

- **Accumulation prevention**: Reset tolerances at each floor level or grid line. Do not accumulate errors across the full building height/length.
- **Adjustable connections**: Slotted holes (+/- 10-20 mm), shim stacks, leveling bolts.
- **Survey control**: Total station or robotic total station for element placement. Tolerance check before final fixing.
- **As-built recording**: 3D scan or photogrammetry of as-built positions. Compare to design model. Feed deviations back to fabrication model for subsequent elements.

### QA/QC Procedures

1. **Fabrication QA**: Dimensional check of every nth element (or every element for critical geometry). CMM, 3D scanner, or manual measurement.
2. **Surface quality**: Visual inspection. Surface roughness measurement for exposed concrete or milled surfaces.
3. **Material certification**: Mill certificates for steel, grading certificates for timber, batch test reports for concrete.
4. **Assembly QA**: Survey verification of element positions against design coordinates. Torque check on bolted connections.
5. **Documentation**: QA log per element, photographic record, deviation reports.

### Digital Twin for Assembly Tracking

- Real-time dashboard showing: which elements are fabricated, in transit, on site, installed.
- 3D model colored by status (red = not started, yellow = in fabrication, green = installed).
- Integration with fabrication shop MES (Manufacturing Execution System) and site management software.
- Deviation tracking: overlay as-built scan on design model, flag elements exceeding tolerance.

---

## File Preparation and Machine Code

### G-Code Structure

G-code is the standard language for CNC machine control. Key commands:

#### Motion Commands
```
G0 X100 Y50 Z5       ; Rapid move (non-cutting, maximum speed)
G1 X200 Y50 Z-3 F1500 ; Linear interpolation (cutting move, feed rate 1500 mm/min)
G2 X150 Y100 I50 J0   ; Clockwise arc (I,J = center offset from start)
G3 X150 Y100 I50 J0   ; Counter-clockwise arc
```

#### Machine Control
```
M3 S18000   ; Spindle on clockwise at 18000 RPM
M5          ; Spindle off
M8          ; Coolant on
M9          ; Coolant off
M6 T2       ; Tool change to tool 2
M30         ; Program end, rewind
```

#### Coordinate Systems
```
G90         ; Absolute coordinates (all positions relative to origin)
G91         ; Incremental coordinates (positions relative to current position)
G54         ; Select work coordinate system 1
G55         ; Select work coordinate system 2
```

#### Canned Cycles
```
G81 X10 Y10 Z-20 R2 F200  ; Drilling cycle
G83 X10 Y10 Z-40 R2 Q5 F200  ; Peck drilling (Q = peck depth)
```

### RAPID (ABB Robot Language) Basics

```rapid
MODULE MainModule
  PROC main()
    ! Define tool
    PERS tooldata myTool := [TRUE, [[0,0,200],[1,0,0,0]],
                              [5,[0,0,100],[1,0,0,0],0,0,0]];
    ! Define work object
    PERS wobjdata myWobj := [FALSE, TRUE, "",
                              [[500,0,0],[1,0,0,0]],
                              [[0,0,0],[1,0,0,0]]];

    ! Move to safe position
    MoveJ pHome, v1000, z50, myTool;

    ! Approach workpiece
    MoveL pApproach, v500, z10, myTool \WObj:=myWobj;

    ! Fabrication path (linear moves)
    MoveL p1, v100, fine, myTool \WObj:=myWobj;
    MoveL p2, v100, fine, myTool \WObj:=myWobj;
    MoveL p3, v100, fine, myTool \WObj:=myWobj;

    ! Retract
    MoveL pApproach, v500, z10, myTool \WObj:=myWobj;
    MoveJ pHome, v1000, z50, myTool;
  ENDPROC
ENDMODULE
```

Key concepts:
- `MoveJ`: Joint motion (PTP). Fast, non-linear path.
- `MoveL`: Linear motion. Straight TCP path.
- `MoveC`: Circular motion through via point.
- `v100`: Velocity (mm/s for TCP).
- `z10`: Zone (blend radius in mm). `fine` = stop at point exactly.
- `tooldata`: TCP position and orientation relative to flange, plus mass properties.
- `wobjdata`: Workpiece coordinate system.

### KRL (KUKA Robot Language) Basics

```krl
DEF main()
  ; Tool and base definitions
  $TOOL = TOOL_DATA[1]
  $BASE = BASE_DATA[1]

  ; Set velocity
  $VEL.CP = 0.5      ; m/s for linear motion
  $VEL_AXIS[1] = 100  ; % for joint motion

  ; Joint motion to home
  PTP HOME

  ; Linear motion to approach point
  LIN {X 500, Y 0, Z 200, A 0, B 90, C 0}

  ; Fabrication path
  LIN {X 500, Y 100, Z 50, A 0, B 90, C 0} C_DIS
  LIN {X 600, Y 100, Z 50, A 0, B 90, C 0} C_DIS
  LIN {X 600, Y 200, Z 50, A 0, B 90, C 0}

  ; Retract and home
  LIN {X 500, Y 0, Z 200, A 0, B 90, C 0}
  PTP HOME
END
```

Key concepts:
- `PTP`: Point-to-point (joint motion).
- `LIN`: Linear (Cartesian) motion.
- `CIRC`: Circular motion (via point + end point).
- `C_DIS`: Approximate positioning (blending). Omit for exact positioning.
- `A, B, C`: Euler angles for tool orientation.
- `$VEL.CP`: Cartesian velocity in m/s.

### URScript (Universal Robots) Basics

```python
def main():
  # Set TCP
  set_tcp(p[0, 0, 0.200, 0, 0, 0])

  # Move to home (joint space)
  movej([0, -1.57, 1.57, -1.57, -1.57, 0], a=1.0, v=0.5)

  # Move to approach (Cartesian)
  movel(p[0.5, 0.0, 0.3, 0, 3.14, 0], a=0.5, v=0.2)

  # Fabrication path
  movel(p[0.5, 0.1, 0.05, 0, 3.14, 0], a=0.3, v=0.1)
  movel(p[0.6, 0.1, 0.05, 0, 3.14, 0], a=0.3, v=0.1)
  movel(p[0.6, 0.2, 0.05, 0, 3.14, 0], a=0.3, v=0.1)

  # Retract
  movel(p[0.5, 0.0, 0.3, 0, 3.14, 0], a=0.5, v=0.2)
  movej([0, -1.57, 1.57, -1.57, -1.57, 0], a=1.0, v=0.5)
end
```

Key concepts:
- `movej`: Joint space motion. Arguments: joint angles (radians), acceleration (rad/s2), velocity (rad/s).
- `movel`: Linear Cartesian motion. Arguments: pose (x, y, z, rx, ry, rz in meters and radians), acceleration (m/s2), velocity (m/s).
- `movec`: Circular motion through via point to end point.
- `p[x, y, z, rx, ry, rz]`: Pose (position + axis-angle orientation).
- `set_tcp`: Define tool center point offset from flange.
- URScript is Python-like but runs on the UR controller directly.

### Post-Processor Concept

A post-processor translates generic toolpath data (from CAM software) into machine-specific code:

```
CAM Toolpath (generic)          →    Post-Processor    →    Machine Code (specific)
[X,Y,Z, feed, speed, tool]          [machine model]         G-code / RAPID / KRL
```

Post-processors handle:
- Coordinate system mapping (CAM axes → machine axes)
- Machine-specific syntax (G-code dialects vary between controllers: Fanuc, Haas, Siemens, Heidenhain)
- Tool change sequences (ATC commands vary by machine)
- Safety headers/footers (homing, warm-up, parking)
- Axis limits and soft stops
- Coolant and dust extraction control

Most CAM software ships with generic post-processors. Custom post-processors are often needed for specific machines. Fusion 360 and Mastercam have post-processor editors. RhinoCAM uses template-based post-processors.

### File Formats by Machine Type

| Machine Type | Input Geometry | Output Code | Transfer Method |
|---|---|---|---|
| 3-axis CNC router | DXF, 3DM, STEP, STL | G-code (.nc, .gcode, .tap) | USB, network, serial |
| 5-axis CNC mill | STEP, 3DM, IGES | G-code (Siemens/Heidenhain) | Network (DNC) |
| Laser cutter | DXF, DWG, AI, SVG | Machine-native | USB, network |
| FDM 3D printer | STL, 3MF, OBJ | G-code (.gcode) | SD card, USB, WiFi |
| SLA 3D printer | STL, 3MF | Machine-native slices | Network, USB |
| ABB robot | 3DM, STEP (via plugin) | RAPID (.mod, .pgf) | Network (FTP), USB |
| KUKA robot | 3DM, STEP (via plugin) | KRL (.src, .dat) | Network, USB |
| UR robot | 3DM, STEP (via plugin) | URScript (.script, .urp) | Network (TCP/IP), USB |
| Hundegger timber | BTL, BVX | Machine-native | Network |
| Concrete printer | STL, G-code | G-code or custom | Network |

### Pre-Flight Checklist

Before sending any file to a fabrication machine:

1. **Geometry verification**: Visual inspection of toolpaths in simulation. Check for gouges, collisions, air cuts.
2. **Material setup**: Correct material dimensions entered. Workpiece origin (zero point) matches physical setup.
3. **Tool verification**: Correct tool number, diameter, length, and type. Physical tool matches program.
4. **Speed and feed review**: Appropriate for material and tool. Not exceeding machine limits.
5. **Workholding check**: Material secured. Clamps do not interfere with toolpath. Vacuum zones active (if applicable).
6. **Safety perimeter**: Area clear of personnel. Guards/fencing in place. E-stop accessible.
7. **Dry run**: Run program with spindle off and Z raised (air cut) to verify motions.
8. **First article**: Run on scrap material first for new programs. Measure and verify before production.
9. **Dust/chip extraction**: Active and functioning. Critical for wood and composite machining.
10. **Communication verified**: File transferred completely. No truncation. Program loaded on controller and verified.


---

# BIM & interoperability


## bim-scripting

### BIM Scripting

> Revit API fundamentals, Dynamo for Revit, pyRevit framework, IFC schema and openBIM, model checking, automated documentation, clash detection, and BIM interoperability tools for AEC computational design

## BIM Scripting

Comprehensive reference for automating Building Information Modeling workflows
through scripting, API access, and interoperability platforms. This skill covers
the full spectrum of BIM automation --- from visual programming with Dynamo
through deep Revit API scripting, pyRevit extension development, IFC/openBIM
data exchange, model checking, automated documentation, and cross-platform
interoperability via Speckle, BHoM, and Rhino.Inside.Revit.

---

### 1. BIM Automation Philosophy

#### Why Script BIM

BIM models are databases disguised as 3D geometry. Every wall, door, room, and
duct segment carries structured data --- type, dimensions, material, cost code,
fire rating, acoustic class, phase, workset, design option. Manual manipulation
of that data does not scale. A 200-unit residential project may contain 40,000+
elements, each with 30--80 parameters. Changing a naming convention, verifying
parameter completeness, or exporting coordinated drawing sets by hand is not
just slow --- it is error-prone and unrepeatable.

Scripting BIM means treating the model as a programmable data source:

- **Read** element properties at scale (audit, validate, report).
- **Write** parameter values in batch (standards enforcement, data enrichment).
- **Create** elements procedurally (repetitive layouts, adaptive placement).
- **Transform** geometry computationally (facade panelization, structural optimization).
- **Export** deliverables automatically (sheets to PDF, models to IFC, data to dashboards).

#### Manual vs. Automated BIM Workflows

| Workflow | Manual Approach | Automated Approach | Time Savings |
|---|---|---|---|
| Parameter QA | Open each element, check value | Script scans all elements, flags violations | 95% |
| Sheet creation | Place views, adjust crops, add tags one by one | Script generates sheets from template rules | 90% |
| Clash detection | Visual inspection in section views | Navisworks / script-based interference check | 85% |
| Export to IFC | File > Export > IFC, configure, repeat per model | Batch script exports all linked models with preset mappings | 80% |
| Room finish schedule | Manual schedule, manual formatting | API-generated schedule with conditional formatting | 75% |
| Design option comparison | Duplicate views, switch options, compare | Script generates comparison report with metrics | 90% |
| Naming convention enforcement | Manual review of browser tree | FilteredElementCollector + regex validation | 98% |

#### ROI of BIM Automation

The return on investment for BIM scripting follows a clear pattern:

1. **First script** --- 2-8 hours to develop, saves 1-4 hours per use. Break-even after 2-3 uses.
2. **Script library** (20-50 tools) --- 200-500 hours to develop, saves 10-30 hours per project. Break-even within 1-2 projects.
3. **Custom application** --- 500-2000 hours to develop, saves 50-200 hours per project. Break-even within 3-5 projects.
4. **Enterprise platform** --- 2000-10,000 hours to develop, transforms entire practice workflow.

#### The Automation Spectrum

```
Level 1: Visual Programming (Dynamo, Grasshopper)
  - Lowest barrier to entry
  - Best for designers who think visually
  - Limited scalability and version control
  - Good for: one-off design explorations, parameter mapping, geometry generation

Level 2: Scripting (Python in Dynamo, pyRevit, RevitPythonShell)
  - Moderate barrier to entry
  - Full API access with Python convenience
  - Version-controllable, shareable
  - Good for: batch operations, custom tools, data workflows

Level 3: Custom Tools (C# add-ins, pyRevit extensions)
  - Higher barrier to entry
  - Compiled performance, custom UI, ribbon integration
  - Deployable to teams
  - Good for: production tools, firm-wide standards enforcement

Level 4: Full Applications (standalone apps, web dashboards, microservices)
  - Highest barrier to entry
  - Complete control over UX and data pipeline
  - Cloud-scalable, multi-user
  - Good for: enterprise BIM management, cross-project analytics
```

#### When to Automate vs. When to Model Manually

Automate when:
- The task repeats across projects or phases.
- The task involves more than 50 elements.
- Consistency and auditability are critical (QA/QC, code compliance).
- The output feeds downstream processes (cost, energy, structural analysis).
- Human error risk is high (naming, classification, spatial containment).

Model manually when:
- The task is a one-time creative act (early concept massing).
- Judgment and spatial intuition outweigh procedural logic.
- The element count is small and the rules are ambiguous.
- The cost of developing automation exceeds the cost of manual work.

#### BIM Maturity Levels and Automation

| BIM Level | Description | Automation Role |
|---|---|---|
| Level 0 | 2D CAD, no BIM | CAD scripting (AutoLISP, VBA) for drawing automation |
| Level 1 | 3D modeling, 2D documentation | Basic Dynamo scripts, parameter management |
| Level 2 | Federated models, structured data exchange | IFC workflows, clash detection, model checking |
| Level 3 | Integrated single model, full lifecycle data | API-driven analytics, real-time dashboards, AI-assisted QA |
| Level 4 (emerging) | Digital twin, IoT-connected, predictive | Continuous model sync, ML-driven optimization, autonomous agents |

---

### 2. Revit API Fundamentals

#### Architecture

The Revit API is a .NET framework (C# or VB.NET natively, Python via IronPython
or CPython with RevitPythonShell/pyRevit). The object hierarchy:

```
UIApplication
  └── Application           (Revit application-level settings, version info)
       └── Document          (the .rvt file; model database)
            ├── Elements      (everything in the model)
            ├── Views         (plans, sections, 3D views, schedules)
            ├── Phases        (existing, new construction, demolition)
            ├── DesignOptions  (option sets and options)
            ├── Worksets       (worksharing partitions)
            └── Settings       (project units, line styles, fill patterns)
```

#### Element Types

Every object in a Revit model inherits from `Element`. Key subclasses:

| Class | Description | Example |
|---|---|---|
| `FamilyInstance` | Placed instance of a loadable family | Door, window, furniture, fixture |
| `Wall` | System family: wall element | Basic Wall, Curtain Wall, Stacked Wall |
| `Floor` | System family: floor slab | Generic Floor, composite assemblies |
| `Roof` | System family: roof element | Basic Roof, extrusion roof |
| `Ceiling` | System family: ceiling element | Compound ceiling, basic ceiling |
| `FamilyInstance` (structural) | Columns, beams, braces | Steel W-shapes, concrete columns |
| `Room` | Spatial element for architectural spaces | Bounded by room-bounding elements |
| `Area` | Spatial element for area plans | Gross area, rentable area |
| `View` | Any view in the model | `ViewPlan`, `ViewSection`, `View3D`, `ViewSheet` |
| `ViewSheet` | A sheet for documentation | Contains viewport placements |
| `ViewSchedule` | A schedule/quantity takeoff | Tabular data extraction |
| `Group` | Grouped elements | Model groups, detail groups |
| `Level` | Datum: horizontal reference plane | Defines story heights |
| `Grid` | Datum: vertical reference plane | Structural grid lines |
| `ReferencePlane` | Construction plane | Alignment references |

#### Categories, Families, Types, Instances

This four-level hierarchy is central to Revit:

```
Category        (e.g., Doors)
  └── Family      (e.g., Single-Flush)
       └── Type     (e.g., 36" x 84")
            └── Instance  (placed door #1, #2, #3...)
```

- **Category**: broad classification (Walls, Doors, Floors, Furniture). Each has a `BuiltInCategory` enum.
- **Family**: a parametric definition (.rfa file for loadable families; system families are built-in).
- **Type**: a named set of parameter values within a family (dimensions, materials).
- **Instance**: a placed occurrence with instance-specific parameters (location, room, mark).

#### Parameters

Parameters store all non-geometric data on elements.

| Parameter Kind | Scope | Definition | Access |
|---|---|---|---|
| Built-in | Hardcoded by Revit | Predefined (e.g., `WALL_BASE_OFFSET`) | `element.get_Parameter(BuiltInParameter.WALL_BASE_OFFSET)` |
| Project | One project file | Defined in Project Parameters dialog | `element.LookupParameter("MyParam")` |
| Shared | Across projects/families | Defined in Shared Parameters file (.txt) | `element.get_Parameter(guid)` or by name |
| Family | Inside .rfa family | Defined in Family Editor | Exposed as type or instance parameter |
| Global | Project-wide value | Not element-bound; referenced by formulas | `GlobalParametersManager` |

Parameter storage types:
- `StorageType.String` --- text
- `StorageType.Integer` --- integers and YesNo (0/1)
- `StorageType.Double` --- real numbers (always in internal units)
- `StorageType.ElementId` --- reference to another element (material, type, level)

#### Transactions

Every model modification must occur inside a `Transaction`. Without it, the API
throws an `InvalidOperationException`.

```python
## Python (pyRevit / RevitPythonShell)
from Autodesk.Revit.DB import Transaction

doc = __revit__.ActiveUIDocument.Document
t = Transaction(doc, "Batch Update Parameters")
t.Start()

try:
    # ... modify elements ...
    t.Commit()
except Exception as e:
    t.RollBack()
    print("Error: {}".format(e))
```

Transaction types:
- **Transaction** --- standard single transaction (most common).
- **TransactionGroup** --- wraps multiple transactions; can assimilate (merge into one undo) or roll back all.
- **SubTransaction** --- nested within a Transaction; can roll back independently without aborting the parent.

#### FilteredElementCollector

The primary mechanism for querying elements in a Revit model. It operates as a
builder pattern with filters:

```python
from Autodesk.Revit.DB import (
    FilteredElementCollector, BuiltInCategory,
    ElementCategoryFilter, ElementClassFilter
)

## All walls in the model
walls = FilteredElementCollector(doc) \
    .OfCategory(BuiltInCategory.OST_Walls) \
    .WhereElementIsNotElementType() \
    .ToElements()

## All door types (not instances)
door_types = FilteredElementCollector(doc) \
    .OfCategory(BuiltInCategory.OST_Doors) \
    .WhereElementIsElementType() \
    .ToElements()

## All family instances of a specific class
instances = FilteredElementCollector(doc) \
    .OfClass(FamilyInstance) \
    .ToElements()

## Elements in a specific view
view_elements = FilteredElementCollector(doc, view.Id) \
    .OfCategory(BuiltInCategory.OST_Walls) \
    .ToElements()
```

#### Geometry Access

Extracting geometry from Revit elements:

```
Element
  └── get_Geometry(Options)
       └── GeometryElement (iterable)
            ├── Solid
            │    ├── Faces (FaceArray)
            │    │    └── Face → Surface, UV domain, normal
            │    └── Edges (EdgeArray)
            │         └── Edge → Curve
            ├── GeometryInstance (for family instances)
            │    └── GetInstanceGeometry() → GeometryElement
            ├── Curve (for line-based elements)
            ├── Point
            └── PolyLine
```

#### Units

Revit internal units are **always**:
- Length: **feet**
- Angle: **radians**
- Area: **square feet**
- Volume: **cubic feet**

Use `UnitUtils.ConvertFromInternalUnits()` and `UnitUtils.ConvertToInternalUnits()`
for conversion. In Revit 2022+, use `UnitTypeId` instead of `DisplayUnitType`.

#### Events

The Revit API provides application and document-level events:
- `Application.DocumentOpened` / `DocumentClosing` / `DocumentSaved`
- `Application.ViewActivated`
- `Application.DialogBoxShowing` (intercept and auto-dismiss dialogs)
- `Document.DocumentChanged` (react to element modifications)
- `UIApplication.Idling` (periodic background processing)

#### External Commands, Applications, Events

| Type | Purpose | Lifecycle |
|---|---|---|
| `IExternalCommand` | Single button click action | Runs once per invocation |
| `IExternalApplication` | Ribbon tab/panel setup, startup logic | Runs at Revit startup/shutdown |
| `IExternalDBApplication` | DB-level (no UI) startup logic | For services, updaters |
| `IExternalEventHandler` | Thread-safe model modification from external threads | Raised via `ExternalEvent` |

#### C# vs. Python for Revit API

| Criterion | C# | Python (IronPython/CPython) |
|---|---|---|
| Performance | Compiled; fastest | Interpreted; slower for large loops |
| Debugging | Full Visual Studio debugger | Print statements, limited debugger |
| Deployment | DLL add-in; requires compilation | Script file; instant edit-run cycle |
| Learning curve | Steeper (typed language, project setup) | Gentler (dynamic typing, REPL) |
| API coverage | 100% | 100% (same .NET API via clr) |
| Ecosystem | NuGet packages, .NET libraries | Python packages (limited in IronPython) |
| UI creation | WPF, WinForms with full designer | WPF possible but harder; rpw simplifies |
| Best for | Production add-ins, enterprise tools | Rapid prototyping, small utilities, pyRevit |

---

### 3. Dynamo for Revit

#### Core Advantages

Dynamo is a visual programming environment integrated with Revit (ships with
Revit since 2017). Key strengths:

- **Visual dataflow** --- nodes connected by wires; intuitive for non-programmers.
- **Live Revit connection** --- read/write model elements in real time.
- **Geometry preview** --- 3D preview of computational geometry before committing to Revit.
- **Extensibility** --- custom nodes in Python, C#, or DesignScript; package manager ecosystem.

#### Revit-Specific Nodes

Dynamo provides dedicated Revit node categories:

- **Selection**: Select Model Element, Select Elements by Category, All Elements of Category
- **Create**: Wall.ByCurveAndHeight, Floor.ByOutlineTypeAndLevel, FamilyInstance.ByPoint
- **Modify**: Element.SetParameterByName, Element.MoveByVector, Element.OverrideColorInView
- **Query**: Element.GetParameterValueByName, Element.BoundingBox, Room.Boundaries

#### Dynamo Player

Dynamo Player exposes Dynamo scripts as simple button-click tools for end users
who do not need to understand the graph. Configure inputs as user-facing
prompts. Best practice: design scripts specifically for Player with clear input
labels and minimal required interaction.

#### Geometry Kernels

Dynamo uses **two separate geometry engines**:

1. **DesignScript / ASM (Autodesk Shape Manager)** --- Dynamo's native geometry kernel.
   Creates Points, Curves, Surfaces, Solids in Dynamo's 3D preview.
2. **Revit geometry** --- the actual BIM model geometry.

These are **not interchangeable**. A Dynamo `Surface` is not a Revit `Face`.
Converting between them requires explicit nodes:
- `Surface.ByPatch` (Dynamo) vs. `FaceWall.Create` (Revit)
- `Curve.ByPoints` (Dynamo) vs. `ModelCurve.ByCurve` (Revit)

#### Common Revit Workflows in Dynamo

1. **Room-based floor finish placement** --- query room boundaries, offset curves, create floor elements by outline.
2. **Adaptive component placement** --- distribute families along curves or surfaces with parameter-driven spacing.
3. **Parameter read/write** --- bulk read element parameters to Excel, modify, write back.
4. **View creation** --- generate scope boxes, create dependent views per scope box, apply view templates.
5. **Sheet setup** --- create sheets from list, place viewports at coordinates, populate titleblock parameters.
6. **Keynote management** --- read keynote table, validate against model, update keynote parameters.
7. **Area analysis** --- extract room areas, calculate ratios (net-to-gross, circulation percentage), color-code by metric.

#### Essential Packages

| Package | Author | Key Capabilities |
|---|---|---|
| Clockwork | Andreas Dieckmann | 500+ utility nodes; view manipulation, element filtering, string operations |
| Rhythm | John Pierson | Revit-focused; sheet management, view manipulation, element creation |
| archi-lab | Konrad Sobon | View/sheet automation, element selection, Revit API wrappers |
| spring nodes | Dimitar Venkov | Geometry, mesh processing, FEM analysis integration |
| BimorphNodes | Bimorph | Geometry, CAD import, mesh to solid conversion |
| Genius Loci | Alban de Chasteigner | Site tools, topography, Revit element manipulation |
| Data-Shapes | Mostafa El Ayoubi | Custom UI nodes (forms, dropdowns, file pickers) |
| Orchid | Erik Falck Jorgensen | Document management, family loading, workset operations |
| LunchBox | Nathan Miller | Paneling, geometric patterns, data management |

#### Python Scripting in Dynamo

Python nodes in Dynamo provide full Revit API access:

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

## Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

## ... API operations ...

TransactionManager.Instance.TransactionTaskDone()
```

Key differences from standalone pyRevit scripts:
- Use `TransactionManager` instead of raw `Transaction`.
- Use `DocumentManager.Instance.CurrentDBDocument` instead of `__revit__`.
- Inputs come from `IN[0], IN[1], ...`; output goes to `OUT`.

#### Performance Considerations

Dynamo becomes slow when:
- Graphs exceed 200-300 nodes.
- Lists contain 10,000+ items with geometry preview on.
- Multiple levels of `List.Map` or `List@Level` create combinatorial explosions.

Alternatives when Dynamo is too slow:
- Move heavy logic into a single Python node (avoids inter-node marshalling).
- Use pyRevit for batch operations without geometry preview overhead.
- Use compiled C# add-in for maximum performance.
- Use Dynamo's `Passthrough` node to sequence operations and avoid unnecessary recalculation.

---

### 4. pyRevit Framework

#### Architecture

pyRevit is a rapid application development framework for Revit. It creates
ribbon UI elements from a folder structure:

```
MyExtension.extension/
  ├── MyTab.tab/
  │    ├── MyPanel.panel/
  │    │    ├── MyButton.pushbutton/
  │    │    │    ├── script.py          (IronPython script)
  │    │    │    ├── icon.png           (16x16, 24x24, or 32x32)
  │    │    │    └── bundle.yaml        (tooltip, author, help URL)
  │    │    ├── MySplitButton.splitbutton/
  │    │    │    ├── Option1.pushbutton/
  │    │    │    └── Option2.pushbutton/
  │    │    └── MyPullDown.pulldown/
  │    │         ├── Item1.pushbutton/
  │    │         └── Item2.pushbutton/
  │    └── AnotherPanel.panel/
  └── lib/                             (shared Python modules)
       └── my_utils.py
```

#### Script Types

- **IronPython (.py)** --- default; runs in Revit's IronPython engine. Access to .NET via `clr`.
- **CPython (.py with `#! python3`)** --- runs in CPython 3.x. Access to pip packages (pandas, numpy). Cannot access UI elements directly.
- **C# (.cs)** --- compiled at runtime. Full performance and type safety.

#### pyRevit CLI

```bash
## Install pyRevit
pyrevit install

## Clone an extension from GitHub
pyrevit extend ui MyExtension https://github.com/user/repo.git

## List installed extensions
pyrevit extensions list

## Attach to a Revit version
pyrevit attach 2024 latest

## Enable/disable extensions
pyrevit extensions enable MyExtension
pyrevit extensions disable MyExtension

## Clear caches
pyrevit caches clear --all
```

#### Built-in Tools Reference

pyRevit ships with dozens of production-ready tools:

- **Select** --- select all instances of a type, select by parameter value, select linked elements.
- **Match** --- match type properties, match graphic overrides between elements.
- **Keynotes** --- keynote manager with live editing and project keynote file management.
- **Sheets** --- batch create sheets, renumber sheets, print sheet sets.
- **Views** --- batch create views, set view templates, manage scope boxes.
- **Project** --- project parameter manager, shared parameter loader.
- **Toggles** --- quick toggles for halftone, crop regions, annotations.

#### Creating Custom Extensions

Minimum viable pyRevit button:

```python
## script.py
"""Tooltip text shown on hover."""

__title__ = "My Button"
__author__ = "Your Name"

from pyrevit import revit, DB, forms

doc = revit.doc

## Get all rooms
rooms = DB.FilteredElementCollector(doc) \
    .OfCategory(DB.BuiltInCategory.OST_Rooms) \
    .WhereElementIsNotElementType() \
    .ToElements()

## Filter rooms with no number
unnamed = [r for r in rooms if not r.get_Parameter(
    DB.BuiltInParameter.ROOM_NUMBER).AsString()]

if unnamed:
    forms.alert("{} rooms have no number assigned.".format(len(unnamed)))
else:
    forms.alert("All rooms are numbered.", title="QA Check Passed")
```

#### Transaction Handling in pyRevit

pyRevit provides a context manager for transactions:

```python
from pyrevit import revit, DB

with revit.Transaction("Update Room Names"):
    for room in rooms:
        param = room.get_Parameter(DB.BuiltInParameter.ROOM_NAME)
        current = param.AsString()
        param.Set(current.upper())
```

#### RevitPythonShell

An interactive Python REPL inside Revit. Useful for:
- Exploring the API interactively (inspect elements, test queries).
- Quick one-off operations without creating a full pyRevit script.
- Debugging: inspect element properties, test FilteredElementCollector queries.

#### Template Scripts

**Batch parameter update:**
```python
from pyrevit import revit, DB, forms

doc = revit.doc
walls = DB.FilteredElementCollector(doc) \
    .OfCategory(DB.BuiltInCategory.OST_Walls) \
    .WhereElementIsNotElementType() \
    .ToElements()

with revit.Transaction("Set Wall Comments"):
    for wall in walls:
        wall.LookupParameter("Comments").Set("Reviewed")
```

**View creation from room list:**
```python
from pyrevit import revit, DB

doc = revit.doc
rooms = DB.FilteredElementCollector(doc) \
    .OfCategory(DB.BuiltInCategory.OST_Rooms) \
    .WhereElementIsNotElementType() \
    .ToElements()

level = rooms[0].Level
vft = doc.GetDefaultElementTypeId(DB.ElementTypeGroup.ViewTypeFloorPlan)

with revit.Transaction("Create Room Views"):
    for room in rooms:
        name = room.get_Parameter(DB.BuiltInParameter.ROOM_NAME).AsString()
        view = DB.ViewPlan.Create(doc, vft, level.Id)
        view.Name = "Room - {}".format(name)
```

#### Deployment

- **Shared extension path**: configure in pyRevit settings to point to a network share.
  All team members load extensions from the same location.
- **Version control**: store extensions in Git. Use CI/CD to deploy to the shared path.
- **pyRevit CLI** can install extensions from Git repositories directly.

#### pyRevit Hooks

pyRevit supports event hooks via specially named scripts:

- `doc-changed-[hookid].py` --- fires when the document changes.
- `doc-opened-[hookid].py` --- fires when a document is opened.
- `doc-saved-[hookid].py` --- fires after a document is saved.
- `app-init-[hookid].py` --- fires when Revit starts (before any document).

Hooks live in a `hooks/` folder within the extension.

---

### 5. IFC & openBIM

#### IFC Schema Overview

IFC (Industry Foundation Classes) is an ISO-standard (ISO 16739) open data
schema for BIM data exchange. Major versions:

| Version | Status | Key Additions |
|---|---|---|
| IFC2x3 | Legacy, widely supported | Most common in practice; 650+ entities |
| IFC4 | Current standard (ISO 16739-1:2018) | Improved geometry, new MEP entities, 4D/5D support |
| IFC4.3 | Released 2024 | Infrastructure: roads, bridges, rail, tunnels, ports |

#### Key IFC Entities

```
IfcProject
  └── IfcSite
       └── IfcBuilding
            └── IfcBuildingStorey
                 ├── IfcWall / IfcWallStandardCase
                 ├── IfcSlab
                 ├── IfcBeam
                 ├── IfcColumn
                 ├── IfcDoor
                 ├── IfcWindow
                 ├── IfcSpace (equivalent of Revit Room)
                 ├── IfcCurtainWall
                 ├── IfcStair / IfcStairFlight
                 ├── IfcRamp / IfcRampFlight
                 ├── IfcRailing
                 ├── IfcRoof
                 ├── IfcCovering (finishes, ceilings)
                 ├── IfcFurnishingElement
                 └── IfcDistributionElement (MEP)
                      ├── IfcFlowSegment (pipes, ducts)
                      ├── IfcFlowTerminal (fixtures, diffusers)
                      └── IfcFlowFitting (elbows, tees)
```

#### Property Sets and Quantity Sets

IFC data is carried in standardized property sets (Psets) and quantity sets (Qtos):

- **Pset_WallCommon**: Reference, Status, IsExternal, ThermalTransmittance, FireRating, AcousticRating
- **Pset_SlabCommon**: Reference, Status, IsExternal, LoadBearing, AcousticRating
- **Pset_DoorCommon**: Reference, FireRating, IsExternal, SecurityRating, HandicapAccessible
- **Pset_SpaceCommon**: Reference, IsExternal, GrossPlannedArea, NetPlannedArea, PubliclyAccessible
- **Qto_WallBaseQuantities**: Length, Width, Height, GrossVolume, NetVolume, GrossSideArea, NetSideArea
- **Qto_SlabBaseQuantities**: Width, Length, Depth, Perimeter, GrossArea, NetArea, GrossVolume, NetVolume

#### IFC Export Settings in Revit

Critical export configuration:
- **IFC version**: IFC2x3 Coordination View 2.0 (most compatible) or IFC4 Reference View.
- **Export mapping table**: `IFC export classes` in Revit maps categories to IFC entities.
- **Property set mapping**: custom `.txt` mapping file for project-specific Psets.
- **Phase**: export only the relevant phase.
- **Base point**: shared coordinates for model federation.
- **Element selection**: current view vs. entire model.

#### MVD (Model View Definition)

MVDs define subsets of the IFC schema for specific use cases:

| MVD | Purpose | Use Case |
|---|---|---|
| Coordination View 2.0 | Geometry + basic properties | Multi-discipline coordination |
| Design Transfer View | Rich geometry + full properties | Model handover between authoring tools |
| Reference View | Lightweight reference geometry | Lightweight context for coordination |
| Quantity Takeoff View | Properties + quantities | Cost estimation data exchange |

#### BCF (BIM Collaboration Format)

BCF (ISO 21597) is a structured format for communicating issues in BIM:
- **BCF XML**: file-based (.bcfzip). Contains viewpoints (camera position, component visibility), comments, and issue metadata.
- **BCF API**: REST API for real-time issue sync between platforms.
- **Workflow**: reviewer opens federated model, creates BCF issue with snapshot, assigns to responsible party, tracks resolution.

#### IFC Tools

| Tool | Language | Capabilities |
|---|---|---|
| IfcOpenShell | Python/C++ | Read/write/validate IFC; geometry processing; most mature open-source |
| IFC.js | JavaScript | Web-based IFC viewer/parser; WebGL rendering |
| xBIM | C# (.NET) | Read/write IFC; geometry meshing; WPF viewer |
| BIMserver | Java | Model server; IFC storage; version control; plugin architecture |
| Solibri | Desktop app | Model checking; clash detection; rule-based validation |
| BIMcollab | Web/Desktop | BCF management; cloud collaboration; issue tracking |
| BlenderBIM | Python | Full IFC authoring in Blender; IfcOpenShell-based |

#### openBIM Coordination Workflow

```
Architect (Revit) ──export IFC──> Coordination Platform
Structural (Tekla) ──export IFC──>     (Solibri, BIMcollab,
MEP (Revit MEP) ──export IFC──>        Navisworks, or custom)
                                            │
                                    Federated Model
                                            │
                              ┌─────────────┼─────────────┐
                        Clash Detection   QA/QC       4D Planning
                              │             │             │
                         BCF Issues    Validation    Schedule Link
                              │          Report           │
                        ──BCF──> Author fixes ──re-export──>
```

---

### 6. Model Checking & Validation

#### Rule-Based Checking

Model checking verifies that a BIM model meets predefined rules. Categories:

1. **Data completeness** --- required parameters are filled.
2. **Naming conventions** --- element names follow organizational standards.
3. **Spatial containment** --- elements are properly hosted on levels/rooms.
4. **Classification compliance** --- elements have correct Uniclass/OmniClass codes.
5. **Geometric validity** --- no zero-thickness walls, no overlapping elements.
6. **Design standards** --- minimum room sizes, maximum corridor lengths, accessibility clearances.

#### Clash Detection Types

| Type | Description | Tolerance | Example |
|---|---|---|---|
| Hard clash | Physical intersection of elements | 0 mm | Duct passing through beam |
| Soft clash (clearance) | Insufficient clearance | Variable (50-300 mm typical) | Pipe too close to electrical cable tray |
| Workflow clash (4D) | Time-based conflict | Schedule overlap | Two trades occupying same zone simultaneously |
| Duplicate | Same element modeled twice | Position tolerance | Two identical walls overlapping |

#### Navisworks Clash Detection Setup

1. **Append** all models (Revit NWC, IFC, DWG).
2. **Create selection sets** by discipline (Arch, Struct, MEP), system, or zone.
3. **Configure clash tests**: set A vs. set B, tolerance, clash type.
4. **Apply rules**: ignore clashes between connected elements, within same system, or by specific parameter match.
5. **Group results** by grid intersection, level, or element type.
6. **Generate report**: HTML, XML, or BCF for distribution.

#### Custom Model Checking with Revit API

```python
from pyrevit import revit, DB, forms, output

doc = revit.doc
out = output.get_output()

## Check: All rooms must have a number and name
rooms = DB.FilteredElementCollector(doc) \
    .OfCategory(DB.BuiltInCategory.OST_Rooms) \
    .WhereElementIsNotElementType() \
    .ToElements()

issues = []
for room in rooms:
    number = room.get_Parameter(DB.BuiltInParameter.ROOM_NUMBER).AsString()
    name = room.get_Parameter(DB.BuiltInParameter.ROOM_NAME).AsString()
    area = room.get_Parameter(DB.BuiltInParameter.ROOM_AREA).AsDouble()

    if not number:
        issues.append(("Room {} has no number".format(room.Id), room.Id))
    if not name:
        issues.append(("Room {} has no name".format(room.Id), room.Id))
    if area == 0:
        issues.append(("Room {} is not bounded (0 area)".format(room.Id), room.Id))

out.print_md("## Room QA Report")
out.print_md("**Total rooms**: {}".format(len(rooms)))
out.print_md("**Issues found**: {}".format(len(issues)))
for msg, eid in issues:
    out.print_md("- {} [Click to select](revit://select?eid={})".format(msg, eid))
```

#### LOD/LOI Verification

BIM Execution Plans specify required Level of Development (LOD) and Level of
Information (LOI) at each project stage. Automated verification:

- **LOD 100**: massing volumes present; check that IfcBuildingElementProxy exists.
- **LOD 200**: approximate geometry; check that elements have correct category but allow generic types.
- **LOD 300**: precise geometry; verify element dimensions match design intent; all parameters from EIR filled.
- **LOD 350**: coordination geometry; verify connections between disciplines; MEP clearances maintained.
- **LOD 400**: fabrication-ready; verify manufacturer data, part numbers, installation instructions.

#### IFC Validation with IfcOpenShell

```python
import ifcopenshell
import ifcopenshell.validate

model = ifcopenshell.open("model.ifc")

## Schema validation
logger = ifcopenshell.validate.json_logger()
ifcopenshell.validate.validate(model, logger)

for error in logger.statements:
    print(error)

## Custom validation: all walls must have Pset_WallCommon
for wall in model.by_type("IfcWall"):
    psets = ifcopenshell.util.element.get_psets(wall)
    if "Pset_WallCommon" not in psets:
        print(f"Wall #{wall.id()} missing Pset_WallCommon")
```

---

### 7. Automated Documentation

#### View Creation Automation

Programmatic view generation eliminates the tedious manual setup of project
views. Common patterns:

- **Floor plans per level** --- create architectural, structural, MEP, and fire safety plans for every level.
- **Dependent views per scope box** --- subdivide large floor plates into manageable sheets.
- **Sections at every grid intersection** --- structural section cuts for detailing.
- **Enlarged plans per room** --- interior elevations and enlarged plans keyed to room boundaries.
- **3D views per zone** --- isometric views for coordination reviews.

#### Sheet Layout Automation

```python
from pyrevit import revit, DB

doc = revit.doc

## Get titleblock type
tb_type = DB.FilteredElementCollector(doc) \
    .OfCategory(DB.BuiltInCategory.OST_TitleBlocks) \
    .WhereElementIsElementType() \
    .FirstElement()

## Get all floor plan views
views = DB.FilteredElementCollector(doc) \
    .OfClass(DB.ViewPlan) \
    .WhereElementIsNotElementType() \
    .ToElements()

with revit.Transaction("Create Sheets"):
    for i, view in enumerate(views):
        if view.IsTemplate or view.Name.startswith("{"):
            continue
        # Create sheet
        sheet = DB.ViewSheet.Create(doc, tb_type.Id)
        sheet.SheetNumber = "A{:03d}".format(i + 1)
        sheet.Name = view.Name

        # Place viewport at center of sheet
        center = DB.XYZ(1.375, 0.875, 0)  # center of A1 sheet in feet
        DB.Viewport.Create(doc, sheet.Id, view.Id, center)
```

#### Tag and Annotation Automation

- **Room tags**: iterate rooms, place `IndependentTag` at room location point.
- **Door tags**: iterate doors, place tag at door midpoint with leader if needed.
- **Dimension strings**: create `Dimension` objects along gridlines or wall faces.
- **Keynotes**: assign keynote values to elements, place keynote tags in views.

#### Export Automation

```python
from pyrevit import revit, DB

doc = revit.doc

## Batch PDF export (Revit 2022+)
sheets = DB.FilteredElementCollector(doc) \
    .OfClass(DB.ViewSheet) \
    .ToElements()

pdf_options = DB.PDFExportOptions()
pdf_options.FileName = "ExportedSheets"
pdf_options.Combine = False  # separate PDF per sheet
pdf_options.PaperFormat = DB.ExportPaperFormat.Default
pdf_options.ZoomType = DB.ZoomType.FitToPage

sheet_ids = [s.Id for s in sheets if s.CanBePrinted]
doc.Export("C:/Output/", sheet_ids, pdf_options)
```

#### Drawing List Management

Automate the drawing list schedule:
- Ensure all sheets have correct sheet number, name, revision, status.
- Generate a `ViewSchedule` of sheets via API with required fields.
- Export drawing list to Excel for transmittals.
- Validate sheet numbering against organizational standard (e.g., `A-101`, `S-201`, `M-301`).

---

### 8. BIM Interoperability Platforms

#### Speckle

Speckle is an open-source data platform for AEC that treats 3D model data as
versionable, streamable, and queryable:

- **Connectors**: Revit, Rhino, Grasshopper, Blender, AutoCAD, Civil3D, Unity, Unreal, Excel, Power BI, QGIS.
- **Streams**: persistent data channels. Push model data to a stream; any connected app can receive it.
- **Commits**: every push creates a versioned commit. Full history, branching, diffing.
- **Web viewer**: browser-based 3D viewer with filtering, measurement, section cuts.
- **GraphQL API**: programmatic access to all data. Query elements, filter by properties.
- **Speckle Automate**: serverless functions triggered on new commits. Use for automated QA/QC, data enrichment, notifications.

**When to use Speckle**: cross-platform model sharing, design review with non-BIM
stakeholders, automated data pipelines, custom dashboards from model data.

#### BHoM (Buildings and Habitats object Model)

BHoM is an open-source collaborative computational framework for the built
environment:

- **Object model**: unified .NET object definitions for structural, environmental, architectural, and planning objects.
- **Adapters**: bidirectional data exchange with analysis software:
  - Structural: Robot, GSA, ETABS, SAP2000, Lusas
  - Environmental: IES, EnergyPlus, Ladybug
  - BIM: Revit, IFC
  - Geometry: Rhino, Grasshopper
- **Engine**: computational methods that operate on BHoM objects (structural analysis queries, environmental calculations, geometry operations).
- **UI**: Grasshopper components and Excel plugin for accessible interaction.

**When to use BHoM**: multi-software structural analysis workflows, computational
design pipelines that span multiple analysis tools, when you need a unified
object model across disciplines.

#### Rhino.Inside.Revit

Rhino.Inside.Revit runs the full Rhino and Grasshopper environment inside the
Revit process, enabling:

- **Grasshopper → Revit**: create Revit elements (walls, floors, roofs, adaptive components) from Grasshopper geometry.
- **Revit → Grasshopper**: query Revit elements, extract geometry, read parameters.
- **Bidirectional live link**: changes in Grasshopper update Revit elements; changes in Revit reflect in Grasshopper.
- **Rhino geometry in Revit views**: use Rhino's superior NURBS engine for complex geometry, bake to Revit as DirectShape or native elements.

Use cases:
- Complex facade panelization designed in GH, built as Revit curtain panels.
- Parametric roof geometry from GH, exported as Revit roof-by-face.
- Site grading and landscape computed in GH, placed as Revit topography.
- Structural optimization in GH (Karamba3D), results pushed to Revit structural model.

#### Comparison Table

| Feature | Speckle | BHoM | Rhino.Inside.Revit |
|---|---|---|---|
| Primary use | Data exchange & versioning | Computational workflows | Geometry & design |
| Architecture | Cloud-based streams | .NET object model + adapters | In-process (runs inside Revit) |
| Revit support | Connector (push/pull) | Adapter (read/write) | Full bidirectional live link |
| Rhino/GH support | Connector | GH components | Native (Rhino is the engine) |
| Analysis tools | Via Automate | Native adapters (Robot, GSA, etc.) | Via GH plugins (Karamba, Ladybug) |
| Open source | Yes (Apache 2.0) | Yes (LGPL 3.0) | Yes (MIT) |
| Best for | Cross-platform data flow | Multi-tool analysis pipelines | Complex geometry in Revit |

---

### 9. BIM Scripting Best Practices

#### Error Handling and Logging

```python
from pyrevit import revit, DB, forms
import traceback

doc = revit.doc
errors = []
success_count = 0

with revit.Transaction("Batch Operation"):
    for element in elements:
        try:
            # operation that might fail
            param = element.LookupParameter("Target Param")
            if param and not param.IsReadOnly:
                param.Set(new_value)
                success_count += 1
            else:
                errors.append("Element {}: parameter not found or read-only".format(element.Id))
        except Exception as e:
            errors.append("Element {}: {}".format(element.Id, str(e)))

## Report results
msg = "Processed: {}\nErrors: {}".format(success_count, len(errors))
if errors:
    msg += "\n\n" + "\n".join(errors[:20])  # limit error display
forms.alert(msg, title="Operation Complete")
```

#### Performance Best Practices

1. **Minimize FilteredElementCollector calls** --- collect once, filter in Python.
2. **Use quick filters** (OfClass, OfCategory) before slow filters (WherePasses with parameter filter).
3. **Disable regeneration** when not needed: `doc.Regenerate()` only when required.
4. **Batch element creation** --- create elements in a single transaction, not one transaction per element.
5. **Avoid `Element.Geometry` in loops** --- geometry extraction is expensive. Cache results.
6. **Use `ElementId` sets** for fast lookups instead of element lists.
7. **Turn off warning suppression wisely** --- `FailureHandlingOptions` can skip dialog boxes during batch operations.

#### User Input Patterns

```python
from pyrevit import forms

## Simple alert
forms.alert("Operation complete.", title="Success")

## Yes/No prompt
if forms.alert("Continue with operation?", yes=True, no=True):
    # proceed
    pass

## Select from list
selected = forms.SelectFromList.show(
    options,
    title="Select Elements",
    multiselect=True
)

## Text input
value = forms.ask_for_string(
    prompt="Enter new parameter value:",
    title="Parameter Update"
)
```

#### Transaction Management

| Pattern | Use Case | Undo Behavior |
|---|---|---|
| Single Transaction | Most operations | One undo step |
| TransactionGroup (assimilate) | Multi-step that should appear as one undo | One undo step |
| TransactionGroup (no assimilate) | Multi-step with individual undo | Multiple undo steps |
| SubTransaction | Tentative changes within a transaction | Roll back sub-changes without aborting main transaction |

#### Version Compatibility

Key API changes across Revit versions:

| Version | Notable API Changes |
|---|---|
| 2021 | `ForgeTypeId` begins replacing `UnitType` and `DisplayUnitType` |
| 2022 | `UnitTypeId` fully replaces `DisplayUnitType`; PDF export API added |
| 2023 | `Toposolid` replaces `TopographySurface`; analytical model API overhaul |
| 2024 | `Document.GetUnusedElements()` added; `Element.IsHidden()` improvements |
| 2025 | `ParameterFilterElement` improvements; enhanced schedule API |

#### Code Organization

```
my_extension.extension/
  ├── lib/
  │    ├── __init__.py
  │    ├── config.py           (settings, constants)
  │    ├── collectors.py       (reusable FilteredElementCollector wrappers)
  │    ├── param_utils.py      (parameter read/write helpers)
  │    ├── geom_utils.py       (geometry extraction helpers)
  │    ├── export_utils.py     (PDF, DWG, IFC export wrappers)
  │    └── report.py           (HTML report generation)
  ├── MyTab.tab/
  │    ├── QA.panel/
  │    │    ├── CheckRooms.pushbutton/
  │    │    ├── CheckNaming.pushbutton/
  │    │    └── CheckParams.pushbutton/
  │    ├── Export.panel/
  │    │    ├── BatchPDF.pushbutton/
  │    │    └── BatchIFC.pushbutton/
  │    └── Data.panel/
  │         ├── ParamWriter.pushbutton/
  │         └── ExcelSync.pushbutton/
  └── hooks/
       └── doc-opened-[audit].py
```

#### Testing Strategies

1. **Test on a dedicated test model** --- a small .rvt file with representative elements of every category.
2. **Log extensively during development** --- use `print()` or pyRevit's output module.
3. **Test edge cases** --- empty parameters, zero-area rooms, unplaced rooms, design options, phases, linked models.
4. **Version test** --- verify scripts work across target Revit versions (2022, 2023, 2024, 2025).
5. **Performance test** --- run scripts on the largest project model to identify bottlenecks.
6. **User acceptance test** --- deploy to 2-3 users before firm-wide rollout; collect feedback.
7. **Regression test** --- after Revit updates, re-run all scripts to verify continued functionality.


## interoperability

### Interoperability

> File format encyclopedia, data exchange strategies, API integration patterns, Grasshopper-to-Revit pipelines, Rhino.Inside workflows, Speckle data streams, and schema mapping for AEC computational design

## Interoperability for AEC Computational Design

### 1. The Interoperability Challenge in AEC

#### 1.1 Why Interoperability Matters

Interoperability -- the ability to exchange data between software tools without loss of meaning, geometry, or relationships -- is the single most critical infrastructure problem in the AEC industry. Every building project involves dozens of software tools, hundreds of files, and thousands of data exchanges. When those exchanges fail, the consequences are measured in millions of dollars and months of delay.

The AEC industry loses an estimated $15.8 billion annually in the United States alone due to inadequate interoperability (NIST GCR 04-867). This figure accounts for redundant data entry, manual format conversion, error correction from data loss, and delayed decision-making caused by information silos.

Unlike the manufacturing or aerospace industries, which converged on STEP/IGES decades ago, the AEC sector remains fragmented across proprietary ecosystems. Autodesk, Bentley, Trimble, Nemetschek, and dozens of smaller vendors each maintain walled gardens with varying degrees of openness. The result is a landscape where a single design decision may need to be re-entered into five or more tools before it reaches a construction site.

#### 1.2 Single-Source-of-Truth vs. Federated Model Approaches

**Single-Source-of-Truth (SSOT)**:
- One authoritative model from which all views and deliverables derive
- Revit-centric workflows often attempt this, with one central model containing architecture, structure, and MEP
- Advantages: no synchronization burden, clear ownership, simpler version control
- Disadvantages: tool lock-in, performance limits at scale, inability to leverage best-of-breed tools
- Practical limit: SSOT breaks down beyond approximately 200-300 MB models or when disciplines require specialized solvers

**Federated Model Approach**:
- Multiple discipline-specific models linked through coordination mechanisms
- Each discipline uses its optimal tool (Revit for documentation, Rhino for complex geometry, Tekla for steel detailing, ETABS for structural analysis)
- Coordination via shared coordinates, reference planes, and clash detection (Navisworks, Solibri, BIMcollab)
- Advantages: best-of-breed tooling, team autonomy, distributed workload
- Disadvantages: synchronization overhead, version mismatch risk, coordinate alignment complexity
- Industry trend: federated approaches are winning, especially with Speckle and IFC enabling richer exchange

#### 1.3 Open Standards vs. Proprietary Formats

**Open Standards**:
- IFC (Industry Foundation Classes) -- ISO 16739, the only truly open BIM exchange standard
- gbXML (Green Building XML) -- energy simulation exchange
- CityGML / CityJSON -- urban-scale 3D models
- LandXML -- civil engineering survey and design data
- BCF (BIM Collaboration Format) -- issue tracking tied to model viewpoints
- Governed by buildingSMART International, OGC, and other standards bodies

**Proprietary Formats**:
- RVT/RFA (Revit), DWG (AutoCAD), 3DM (Rhino), SKP (SketchUp), PLA/PLN (ArchiCAD)
- Offer full fidelity within their ecosystem
- Risk: vendor lock-in, obsolescence, licensing dependencies
- Some are partially documented (DWG via Open Design Alliance) but reverse-engineered support is always incomplete

**Pragmatic Reality**: Most production workflows use a hybrid. Native formats for authoring, open formats for exchange, and lightweight formats (glTF, PDF) for communication. The goal is not eliminating proprietary formats but creating robust translation layers.

#### 1.4 Data Loss Taxonomy

When data moves between tools, losses occur in four categories:

| Loss Type | Description | Example | Impact |
|-----------|-------------|---------|--------|
| **Geometry Loss** | Shape information degraded or missing | NURBS surface exported to STL loses curvature continuity | Visible faceting, dimensional inaccuracy |
| **Metadata Loss** | Properties, parameters, classifications stripped | Revit wall type info lost when exporting to OBJ | Downstream tools lack decision-critical data |
| **Relationship Loss** | Connections, hosting, spatial hierarchy broken | Wall-floor join lost in IFC export | Manual rework to re-establish element logic |
| **Appearance Loss** | Materials, textures, colors not transferred | PBR materials from Blender not mapping to Revit | Re-application of visual properties in target tool |

Additional nuanced losses:
- **Precision loss**: floating-point truncation at large coordinates
- **Semantic loss**: a "wall" becomes a generic "extrusion" in target tool
- **Topological loss**: solid body becomes disjoint surfaces
- **Behavioral loss**: parametric constraints become fixed geometry
- **Unit loss**: implicit unit assumptions cause scaling errors (mm vs. ft is a classic)

---

### 2. File Format Encyclopedia

#### 2.1 Geometry Formats

##### OBJ (Wavefront Object)
| Property | Value |
|----------|-------|
| **Extension** | `.obj` (geometry), `.mtl` (materials) |
| **Version** | Originally 1992, no formal versioning |
| **Geometry** | Polygonal mesh, free-form curves/surfaces |
| **Metadata** | Minimal -- group names, material references |
| **Max Size** | No hard limit; practical ~500 MB |
| **Typical Use** | Mesh exchange, visualization, 3D printing prep |
| **Read/Write** | Rhino, Blender, 3ds Max, SketchUp, Unity, Unreal, MeshLab, CloudCompare |
| **Strengths** | Human-readable ASCII, universal support, simple specification |
| **Limitations** | No BIM data, no solid topology, no units, large file sizes for complex models |

##### STL (Stereolithography)
| Property | Value |
|----------|-------|
| **Extension** | `.stl` |
| **Version** | Original (1987), no updates |
| **Geometry** | Triangulated mesh only |
| **Metadata** | None (only triangle normals and vertices) |
| **Max Size** | No limit; practical ~200 MB for ASCII, larger for binary |
| **Typical Use** | 3D printing, CNC machining, rapid prototyping |
| **Read/Write** | Every CAD tool, every slicer, every mesh editor |
| **Strengths** | Universal 3D printing standard, trivial to parse |
| **Limitations** | No color, no materials, no units, no metadata, triangles only, redundant vertex storage |

##### 3MF (3D Manufacturing Format)
| Property | Value |
|----------|-------|
| **Extension** | `.3mf` |
| **Version** | 1.2.3 (current) |
| **Geometry** | Triangle mesh with manifold validation |
| **Metadata** | Color, materials, print tickets, textures, build platform layout |
| **Max Size** | ZIP-compressed, efficient for large models |
| **Typical Use** | Advanced 3D printing with color/material, digital fabrication |
| **Read/Write** | Rhino, PrusaSlicer, Cura, Windows 3D Viewer, Materialise |
| **Strengths** | Modern replacement for STL, supports multi-material, compact |
| **Limitations** | Not yet universal, limited AEC adoption, no parametric data |

##### PLY (Polygon File Format / Stanford Triangle Format)
| Property | Value |
|----------|-------|
| **Extension** | `.ply` |
| **Version** | 1.0 (1994) |
| **Geometry** | Point cloud and/or polygonal mesh |
| **Metadata** | Per-vertex color, normals, custom properties |
| **Max Size** | Binary format handles billions of points |
| **Typical Use** | Point cloud storage, 3D scanning output, research |
| **Read/Write** | CloudCompare, MeshLab, Blender, Open3D, PCL |
| **Strengths** | Flexible schema, binary efficiency, extensible vertex properties |
| **Limitations** | No materials/textures in standard spec, no BIM data |

##### 3DM (Rhino 3D Model)
| Property | Value |
|----------|-------|
| **Extension** | `.3dm` |
| **Version** | openNURBS 8.x (Rhino 8) |
| **Geometry** | NURBS surfaces, curves, meshes, SubD, extrusions, points, annotations |
| **Metadata** | Layers, object attributes, user text, render materials, named views |
| **Max Size** | No hard limit; practical ~2 GB |
| **Typical Use** | Rhino native authoring, computational design output |
| **Read/Write** | Rhino, Grasshopper, openNURBS SDK (C++, .NET), Speckle, many viewers |
| **Strengths** | Full NURBS fidelity, open SDK (openNURBS), rich layer/attribute system |
| **Limitations** | No BIM semantics, limited structural metadata, Rhino-centric ecosystem |

##### DWG / DXF (AutoCAD Drawing / Drawing Exchange Format)
| Property | Value |
|----------|-------|
| **Extension** | `.dwg`, `.dxf` |
| **Version** | DWG 2018 (R2018), DXF tracks DWG versions |
| **Geometry** | 2D entities (lines, arcs, polylines, hatches), 3D solids (ACIS), meshes, surfaces |
| **Metadata** | Layers, blocks, attributes, extended data (XDATA), object properties |
| **Max Size** | Practical ~500 MB |
| **Typical Use** | 2D drafting, CAD exchange, legacy drawing archives |
| **Read/Write** | AutoCAD, BricsCAD, Rhino, Revit (import), QGIS, LibreCAD, FreeCAD |
| **Strengths** | Industry standard for 2D, massive legacy archive, block/attribute system |
| **Limitations** | DWG is proprietary (ODA reverse-engineers), DXF is verbose, 3D support limited |

##### SKP (SketchUp)
| Property | Value |
|----------|-------|
| **Extension** | `.skp` |
| **Version** | SKP 2024 |
| **Geometry** | Polygonal mesh, groups, components |
| **Metadata** | Layers (tags), component definitions, material assignments, geolocation |
| **Max Size** | Practical ~300 MB |
| **Typical Use** | Conceptual design, massing studies, early-stage visualization |
| **Read/Write** | SketchUp, Trimble Connect, various importers (Rhino, Blender via plugins) |
| **Strengths** | Intuitive modeling paradigm, large 3D Warehouse library, geolocation |
| **Limitations** | Imprecise geometry, no NURBS, no parametric constraints, limited BIM |

##### STEP / IGES (Standard for Exchange of Product Data / Initial Graphics Exchange Specification)
| Property | Value |
|----------|-------|
| **Extension** | `.step`, `.stp`, `.iges`, `.igs` |
| **Version** | STEP AP214/AP242 (ISO 10303), IGES 5.3 |
| **Geometry** | NURBS surfaces, B-rep solids, curves, wireframe |
| **Metadata** | Product structure, material (limited), PMI (AP242), assembly hierarchy |
| **Max Size** | Multi-GB for complex assemblies |
| **Typical Use** | Mechanical CAD exchange, manufacturing, CNC toolpath input |
| **Read/Write** | SolidWorks, CATIA, NX, Rhino, FreeCAD, Inventor, Fusion 360 |
| **Strengths** | Neutral CAD exchange, precise B-rep, ISO standard, AP242 adds PMI |
| **Limitations** | Large files, slow parsing, IGES is legacy (use STEP), limited AEC adoption |

##### SAT (ACIS Save As Text)
| Property | Value |
|----------|-------|
| **Extension** | `.sat`, `.sab` (binary) |
| **Version** | ACIS R2024 |
| **Geometry** | B-rep solids, NURBS surfaces, curves, sheets |
| **Metadata** | Minimal (body names, attributes) |
| **Max Size** | Practical ~500 MB |
| **Typical Use** | Solid geometry exchange between ACIS-kernel tools, Revit mass import |
| **Read/Write** | AutoCAD, Revit (import), SpaceClaim, Fusion 360, BricsCAD |
| **Strengths** | Exact B-rep, Revit can import as mass/generic model, clean geometry |
| **Limitations** | Proprietary kernel (Spatial Corp), no BIM semantics, limited ecosystem |

#### 2.2 BIM Formats

##### RVT / RFA (Revit Project / Family)
| Property | Value |
|----------|-------|
| **Extension** | `.rvt` (project), `.rfa` (family), `.rte` (template) |
| **Version** | Revit 2025 |
| **Geometry** | Parametric solids, extrusions, sweeps, blends, voids, meshes (limited) |
| **Metadata** | Rich: categories, families, types, instances, parameters, schedules, phases, worksets |
| **Max Size** | Practical ~500 MB (workshared models can exceed) |
| **Typical Use** | BIM authoring, construction documentation, coordination |
| **Read/Write** | Revit only (native), IFC export, various viewers (Navisworks, BIM360/ACC) |
| **Strengths** | Full BIM fidelity, parametric families, scheduling, documentation |
| **Limitations** | Completely proprietary, requires Revit license to edit, large file size |

##### IFC (Industry Foundation Classes)
| Property | Value |
|----------|-------|
| **Extension** | `.ifc` (STEP), `.ifcXML`, `.ifcZIP`, `.ifcJSON` |
| **Version** | IFC4.3 (ISO 16739-1:2024), IFC4x3 ADD2 |
| **Geometry** | B-rep, CSG, swept solids, tessellated (triangulated), curves, point clouds |
| **Metadata** | Complete BIM: spatial structure, element types, property sets, quantities, materials, classifications, relationships, cost, time |
| **Max Size** | Multi-GB for large projects (IFC4 has improved efficiency) |
| **Typical Use** | OpenBIM exchange, regulatory submissions, archival, coordination |
| **Read/Write** | Revit, ArchiCAD, Tekla, Solibri, BIMcollab, Navisworks, FreeCAD, BlenderBIM, xBIM, IfcOpenShell |
| **Strengths** | Only true open BIM standard, ISO-certified, rich semantic model, vendor-neutral |
| **Limitations** | Inconsistent export quality across tools, complex schema, geometry fidelity varies, round-trip editing unreliable |

##### NWD / NWC (Navisworks)
| Property | Value |
|----------|-------|
| **Extension** | `.nwd` (full), `.nwc` (cache), `.nwf` (reference) |
| **Version** | Navisworks 2025 |
| **Geometry** | Tessellated mesh (view-only, no editable geometry) |
| **Metadata** | Aggregated from source models, clash results, timeliner schedules, viewpoints |
| **Max Size** | Multi-GB (designed for large federated models) |
| **Typical Use** | Clash detection, 4D simulation, model review, coordination |
| **Read/Write** | Navisworks (native), BIM360/ACC viewer, Freedom (free viewer) |
| **Strengths** | Handles massive models, clash detection engine, 4D timeliner |
| **Limitations** | View-only (no editing), proprietary, Autodesk ecosystem only |

##### gbXML (Green Building XML)
| Property | Value |
|----------|-------|
| **Extension** | `.xml` (with gbXML schema) |
| **Version** | 7.03 |
| **Geometry** | Simplified planar surfaces (walls, floors, roofs as polygons), zones |
| **Metadata** | Thermal properties, construction assemblies, schedules, HVAC zones, location/climate |
| **Max Size** | Typically <50 MB |
| **Typical Use** | Energy simulation input (EnergyPlus, eQUEST, IES VE, Honeybee) |
| **Read/Write** | Revit (export), ArchiCAD, Trace 700, Honeybee, OpenStudio, IES VE |
| **Strengths** | Purpose-built for energy, widely supported by simulation tools |
| **Limitations** | Simplified geometry (no curved surfaces), inconsistent exports from Revit, limited to thermal model |

##### COBie (Construction Operations Building Information Exchange)
| Property | Value |
|----------|-------|
| **Extension** | `.xlsx`, `.xml`, `.ifc` (as MVD) |
| **Version** | COBie 2.4 |
| **Geometry** | None (tabular data only) |
| **Metadata** | Facility, floors, spaces, zones, types, components, systems, assemblies, connections, documents, attributes, coordinates |
| **Max Size** | Typically <10 MB (spreadsheet) |
| **Typical Use** | Facility management handover, asset data delivery |
| **Read/Write** | Excel, COBie plugins for Revit, Solibri, BIMcollab, custom tools |
| **Strengths** | Simple tabular format, clear data structure, FM integration |
| **Limitations** | No geometry, manual population often required, limited adoption outside UK/US government |

#### 2.3 Visualization Formats

##### glTF / GLB (GL Transmission Format)
| Property | Value |
|----------|-------|
| **Extension** | `.gltf` (JSON + binary), `.glb` (single binary) |
| **Version** | 2.0 (Khronos Group) |
| **Geometry** | Triangle mesh, morph targets, skinning |
| **Metadata** | Node hierarchy, PBR materials, textures, animations, cameras, lights (KHR extensions) |
| **Max Size** | Practical ~500 MB (web delivery optimized) |
| **Typical Use** | Web 3D visualization, AR/VR, digital twins, model viewers |
| **Read/Write** | Three.js, Babylon.js, Blender, Rhino 8, Speckle viewer, Cesium, Unity, Unreal |
| **Strengths** | Web-native, PBR materials, compact binary, Draco compression, universal viewer support |
| **Limitations** | Triangle mesh only (no NURBS), no BIM semantics in base spec, limited AEC tool support |

##### USD / USDZ (Universal Scene Description)
| Property | Value |
|----------|-------|
| **Extension** | `.usd`, `.usda` (ASCII), `.usdc` (binary crate), `.usdz` (package) |
| **Version** | USD 24.x (Pixar) |
| **Geometry** | Mesh, NURBS (limited), curves, points, volumes, subdivision surfaces |
| **Metadata** | Scene hierarchy, materials (MaterialX/UsdPreviewSurface), variants, layers, composition arcs |
| **Max Size** | Designed for film-scale scenes (multi-GB) |
| **Typical Use** | Film/VFX pipelines, Apple AR (USDZ), emerging AEC visualization, NVIDIA Omniverse |
| **Read/Write** | Blender, Houdini, Maya, Omniverse, Apple ecosystem, Unity, Unreal |
| **Strengths** | Composition engine (layers, variants, references), scalable, industry momentum |
| **Limitations** | Complex specification, early AEC adoption, limited BIM tool support |

##### FBX (Filmbox)
| Property | Value |
|----------|-------|
| **Extension** | `.fbx` |
| **Version** | FBX 2020.3.4 (Autodesk) |
| **Geometry** | Polygon mesh, NURBS, curves, cameras, lights |
| **Metadata** | Materials, textures, animation, skeleton/bones, blend shapes, scene hierarchy |
| **Max Size** | Multi-GB |
| **Typical Use** | Game engine exchange, animation, Revit→Unity/Unreal visualization |
| **Read/Write** | 3ds Max, Maya, Blender, Unity, Unreal, Revit (export), SketchUp |
| **Strengths** | Animation support, game engine standard, Autodesk ecosystem integration |
| **Limitations** | Proprietary (Autodesk SDK), inconsistent third-party support, no BIM data |

##### E57 (ASTM E57 3D File Format)
| Property | Value |
|----------|-------|
| **Extension** | `.e57` |
| **Version** | ASTM E2807-11 |
| **Geometry** | Point clouds (structured/unstructured), meshes (optional), images (panoramic) |
| **Metadata** | Scan positions, sensor info, intensity, color, normals, cartesian/spherical coordinates |
| **Max Size** | Multi-GB (billions of points) |
| **Typical Use** | Laser scanning data exchange, as-built documentation, heritage recording |
| **Read/Write** | CloudCompare, ReCap, Cyclone, FARO Scene, Rhino (plugin), Revit (point cloud) |
| **Strengths** | Open standard for point clouds, lossless compression, multi-scan support |
| **Limitations** | Large files, limited mesh support, no semantic classification in base spec |

#### 2.4 Data Formats for AEC

| Format | Extension | Use in AEC | Key Tools |
|--------|-----------|-----------|-----------|
| **CSV** | `.csv` | Schedule data, sensor readings, analysis results | Excel, Python, Grasshopper |
| **JSON** | `.json` | API payloads, configuration, BHoM objects, Speckle | Everything |
| **XML** | `.xml` | gbXML, IFC-XML, configuration, legacy integrations | Everything |
| **GeoJSON** | `.geojson` | GIS features, site boundaries, zoning overlays | QGIS, Mapbox, Leaflet, Grasshopper |
| **Shapefile** | `.shp/.dbf/.shx` | GIS vector data, cadastral, infrastructure | ArcGIS, QGIS, FME, Grasshopper (Heron) |
| **GeoTIFF** | `.tif` | Elevation (DEM/DSM), satellite imagery, analysis rasters | QGIS, ArcGIS, GDAL, Grasshopper |
| **LAS/LAZ** | `.las/.laz` | LiDAR point clouds (LAZ = compressed) | CloudCompare, PDAL, QGIS, ReCap |
| **CityGML** | `.gml` | Urban 3D models (LOD 0-4), smart city data | FME, 3DCityDB, QGIS, cesium |
| **CityJSON** | `.json` | Lightweight CityGML alternative | cjio, QGIS, ninja viewer |

---

### 3. Data Exchange Strategies

#### 3.1 Strategy Overview

| Strategy | Latency | Fidelity | Complexity | Best For |
|----------|---------|----------|------------|----------|
| Direct File Exchange | Minutes-hours | Medium | Low | One-time transfers, legacy tools |
| Live Linking | Real-time | High | Medium | Iterative design, parametric-to-BIM |
| Data Streaming | Seconds | High | Medium | Multi-user collaboration, CI/CD |
| Database-Mediated | Seconds-minutes | High | High | Enterprise, large teams, audit trails |
| API-to-API | Seconds | Variable | High | Custom workflows, automation |
| Manual Mapping | Hours-days | Variable | Low | Non-standard conversions, one-offs |

#### 3.2 Direct File Exchange

The simplest and most common approach: export from Tool A, import into Tool B.

**Workflow**: Author model in source tool -> Export to intermediate format (IFC, DXF, SAT, OBJ, etc.) -> Import into target tool -> Manual cleanup and re-association.

**When to use**: One-time or infrequent transfers, when live linking is not available, when tools are on different machines/networks, when a frozen snapshot is needed.

**Key considerations**:
- Always verify export settings (version, units, coordinate system, included categories)
- Document the conversion path for reproducibility
- Validate geometry and metadata in the target tool immediately after import
- Maintain a log of known data losses for your specific tool combination

#### 3.3 Live Linking

Real-time or near-real-time bidirectional connection between tools running simultaneously.

**Technologies**:
- **Rhino.Inside.Revit**: Rhino and Grasshopper running inside Revit's process, sharing geometry and data live
- **Dynamo ↔ Revit**: Dynamo scripting within Revit, direct access to Revit API
- **Grasshopper ↔ Tekla Live Link**: Real-time structural model exchange
- **Revit ↔ Robot Structural Link**: Analytical model exchange for structural analysis
- **Excel ↔ Revit (Dynamo)**: Live parameter read/write via Dynamo Excel nodes

**When to use**: Iterative design exploration requiring immediate BIM feedback, parametric facade design that must update Revit curtain panels, structural optimization with real-time analysis results.

#### 3.4 Data Streaming (Speckle and Similar)

Continuous, version-controlled data flow between tools via a cloud or self-hosted intermediary.

**Speckle** is the leading open-source platform for AEC data streaming. It provides:
- Object-level versioning (not file-level)
- Connectors for 15+ AEC tools
- GraphQL API for custom integrations
- Web-based 3D viewer for review
- Automation triggers on model changes

**When to use**: Multi-discipline teams using different tools, continuous integration for design models, when audit trail and version history are required.

#### 3.5 Database-Mediated Exchange

A shared database (relational, graph, or document) serves as the single source of truth.

**Technologies**:
- **BIMserver** (open-source, IFC-based model server)
- **PostgreSQL + PostGIS** (spatial database for GIS-BIM integration)
- **MongoDB** (document store for flexible BIM data)
- **Neo4j** (graph database for relationship-heavy BIM queries)
- **Autodesk Construction Cloud (ACC)** / **BIM 360** (proprietary cloud platform)
- **Trimble Connect** (cloud collaboration for Tekla, SketchUp ecosystem)

**When to use**: Large enterprise projects, regulatory compliance requiring audit trails, when multiple tools need read/write access to the same data, asset management and operations phase.

#### 3.6 API-to-API Integration

Direct programmatic communication between tools via their APIs.

**Patterns**:
- REST APIs for CRUD operations on model data
- GraphQL for flexible queries (Speckle, custom servers)
- Webhooks for event-driven workflows (model updated -> trigger analysis -> post results)
- WebSocket for real-time streaming (live sensor data into digital twins)

**When to use**: Custom automation pipelines, when no off-the-shelf connector exists, high-volume programmatic workflows, CI/CD for AEC.

#### 3.7 Decision Matrix

```
Need real-time feedback during design?
  YES -> Live Linking (Rhino.Inside, Dynamo)
  NO ->
    Need version history and collaboration?
      YES -> Data Streaming (Speckle)
      NO ->
        Need programmatic automation?
          YES -> API-to-API
          NO ->
            One-time transfer?
              YES -> Direct File Exchange
              NO -> Database-Mediated
```

---

### 4. Grasshopper to Revit Pipelines

#### 4.1 Rhino.Inside.Revit (Primary Method)

Rhino.Inside.Revit embeds the Rhino/Grasshopper runtime directly inside the Revit process. This enables Grasshopper definitions to read from and write to the active Revit document in real time, with full access to the Revit API through Grasshopper components.

**Setup**:
1. Install Rhino 8 (or 7) and Revit 2022+ on the same machine
2. Install the Rhino.Inside.Revit plugin from the McNeel website or Food4Rhino
3. In Revit, navigate to the Add-Ins tab -> Rhinoceros panel -> click the Rhino icon
4. Rhino and Grasshopper launch within Revit's process space
5. Grasshopper definitions can now reference Revit elements and create new ones

**Core Component Categories**:

| Category | Components | Purpose |
|----------|-----------|---------|
| **Revit Primitives** | Category, Family, Type, Element | Reference existing Revit objects |
| **Host Elements** | Add Wall, Add Floor, Add Roof, Add Ceiling | Create hosted building elements |
| **Structure** | Add Beam, Add Column, Add Brace, Add Foundation | Create structural elements |
| **Curtain Wall** | Add Curtain Grid, Add Mullion, Add Panel | Parametric facade elements |
| **MEP** | Add Duct, Add Pipe, Add Fitting | MEP element creation |
| **Site** | Add Topography, Add Building Pad | Site modeling |
| **Annotation** | Add Dimension, Add Tag, Add Text Note | Documentation elements |
| **Parameters** | Get Parameter, Set Parameter, Add Parameter | Revit parameter read/write |
| **Geometry** | DirectShape, FormIt Geometry | Freeform geometry to Revit |

**Geometry Baking Workflow**:
1. Create geometry in Grasshopper (curves, surfaces, meshes, solids)
2. Use element-creation components (Add Wall by Curve, Add Floor by Outline, etc.) to convert GH geometry into native Revit elements
3. Map Grasshopper data to Revit parameters using Set Parameter components
4. Elements are created in the active Revit document and update when GH inputs change

**Parameter Mapping Pattern**:
```
GH Number Slider -> Revit Parameter "Height"
GH Panel (text) -> Revit Parameter "Mark"
GH Boolean -> Revit Parameter "Is Structural"
GH Color -> Not directly mappable (use Dynamo or filters)
```

**Element Tracking**:
Rhino.Inside.Revit tracks which GH components created which Revit elements. When the GH definition is re-run:
- Existing elements are updated in place (geometry and parameters)
- Deleted GH outputs result in deleted Revit elements
- New GH outputs create new Revit elements
- Element IDs persist across updates for reliable referencing

**Best Practices for Rhino.Inside.Revit**:
- Always set your Revit project units before running GH definitions
- Use Revit levels, grids, and reference planes as inputs to GH for alignment
- Internalize GH data for settings that shouldn't change (material assignments, category overrides)
- Use the "Tracking Mode" to prevent element duplication on re-run
- Keep GH definitions modular: separate geometry generation from Revit element creation
- Transaction management: Rhino.Inside batches changes into single Revit transactions for undo support

#### 4.2 Speckle Pipeline

**Send from Grasshopper**:
1. Install Speckle Grasshopper connector from package manager
2. Add "Send" component to canvas
3. Connect geometry and data to input
4. Specify Speckle stream URL and branch
5. Data is serialized, converted to Speckle objects, and pushed to server

**Receive in Revit**:
1. Install Speckle Revit connector
2. Open Speckle Desktop Manager, select stream and branch
3. Click "Receive" -- objects are converted to native Revit elements
4. Conversion mapping: Speckle wall -> Revit wall, Speckle beam -> Revit structural framing, etc.
5. Non-mappable geometry arrives as DirectShape elements

**Advantages over Rhino.Inside**:
- Tools don't need to run on the same machine
- Full version history of every send
- Web viewer for non-licensed team members
- Automation triggers for CI/CD pipelines
- Works across Rhino, Revit, ArchiCAD, Blender, Unity, and more

#### 4.3 Manual Exchange Methods

When live linking is not feasible:

**SAT Export Path**:
1. Bake Grasshopper geometry to Rhino
2. Export as SAT (ACIS solid) -- Revit reads this natively
3. In Revit: Insert -> Import CAD -> select SAT file
4. Geometry arrives as ImportInstance (limited editability)
5. Optionally convert to Mass or Generic Model family in-place

**DWG Export Path**:
1. Export from Rhino as DWG (2D for plans, 3D for massing)
2. In Revit: Link CAD or Import CAD
3. Use linked geometry as reference for tracing Revit elements
4. Suitable for complex curves that will become Revit floor/roof sketches

#### 4.4 Coordinate System Alignment

**Critical**: Rhino and Revit use different coordinate conventions.

| Aspect | Rhino | Revit |
|--------|-------|-------|
| Up axis | Z-up | Z-up (internal), but Y-up in some exports |
| Origin | World 0,0,0 (arbitrary) | Project Base Point or Survey Point |
| Units | Set per file (typically mm or m) | Set per project (typically mm or ft) |
| Precision | Double precision throughout | Double precision, but UI rounds to project units |

**Alignment Procedure**:
1. Establish a shared origin point (e.g., site survey marker)
2. In Revit: set Project Base Point coordinates to match
3. In Rhino: model relative to the same origin
4. When using Rhino.Inside, coordinate systems align automatically (same process)
5. For file-based exchange: verify unit conversion (mm in Rhino -> mm in Revit, not mm -> ft)

---

### 5. Rhino.Inside Workflows

#### 5.1 Rhino.Inside.Revit -- Complete Guide

**Architecture**: Rhino.Inside uses Microsoft's COM interop and the .NET runtime to embed Rhino's geometry kernel (openNURBS + RhinoCommon) inside the host application's process. This means:
- Rhino geometry operations execute in-process (fast, no file I/O)
- Grasshopper can access the host API directly (Revit API via RhinoInside.Revit.GH)
- Both tools share the same memory space (no serialization overhead)

**Supported Hosts**:
- Revit 2019-2025+
- AutoCAD 2023+ (preview)
- Unity 2020+
- Custom .NET applications via RhinoInside NuGet package

**Key Workflows**:

1. **Complex Geometry to BIM**: Design freeform geometry in Grasshopper (SubD, NURBS lofts, panelized surfaces) -> bake as Revit floors, walls, roofs, or DirectShape elements

2. **Parametric Facade**: Define facade logic in GH (panel subdivision, attractor-based sizing, environmental response) -> create Revit curtain wall panels, mullions, and adaptive components

3. **Site Analysis to Massing**: Import terrain data in GH (Heron plugin for GIS, or direct point cloud) -> generate site-responsive massing -> bake as Revit masses for area calculations

4. **Structural Optimization**: Run Karamba3D analysis in GH within Revit -> structural results inform beam/column sizing -> updated sizes pushed to Revit structural elements

5. **Environmental Analysis**: Run Ladybug/Honeybee analysis in GH within Revit -> solar access, daylight, wind results -> inform Revit design parameters (window sizes, shading depths)

#### 5.2 Rhino.Inside.AutoCAD

Preview technology allowing Rhino geometry operations within AutoCAD:
- Access to RhinoCommon geometry library from AutoCAD .NET plugins
- Use NURBS, SubD, and mesh operations not available natively in AutoCAD
- Potential for Grasshopper-driven AutoCAD automation
- Currently limited compared to Revit integration

#### 5.3 Rhino.Inside Custom Applications

Using the RhinoInside NuGet package, developers can embed Rhino's geometry kernel in any .NET application:

```csharp
// Initialize RhinoInside in a custom .NET application
RhinoInside.Resolver.Initialize();
using var rhinoCore = new RhinoCore(new string[] { "-appmode" });

// Now use RhinoCommon geometry:
var sphere = new Rhino.Geometry.Sphere(Point3d.Origin, 5.0);
var brep = sphere.ToBrep();
var mesh = Rhino.Geometry.Mesh.CreateFromBrep(brep, MeshingParameters.Default);
```

**Use Cases**:
- Custom design tools with Rhino-quality NURBS geometry
- Headless geometry processing servers (web APIs that perform NURBS operations)
- Automated file conversion services
- Batch geometry analysis pipelines

#### 5.4 Performance Considerations

| Factor | Impact | Mitigation |
|--------|--------|-----------|
| Memory | Rhino adds ~500 MB to host process | Close unused Rhino viewports |
| Startup | 10-30 seconds to initialize Rhino kernel | Acceptable for session-based workflows |
| Large models | GH solving blocks Revit UI thread | Use async solving where possible |
| Element count | >5000 Revit elements from GH causes slowdown | Batch creation, disable preview during baking |
| Plugins | Not all GH plugins work inside Revit | Test critical plugins before committing to pipeline |

---

### 6. Speckle Platform

#### 6.1 Architecture

Speckle is an open-source data infrastructure for AEC that provides version control, real-time collaboration, and automation for 3D models.

**Core Concepts**:

| Concept | Description |
|---------|-------------|
| **Server** | Central hub hosting all data (speckle.xyz cloud or self-hosted) |
| **Stream** (Project) | Container for related data, like a Git repository |
| **Branch** (Model) | Named line of development within a stream (e.g., "architecture", "structure") |
| **Commit** (Version) | Immutable snapshot of data sent to a branch |
| **Object** | Individual data entity with unique ID, properties, and optional geometry |
| **Transport** | Mechanism for moving objects (server, SQLite, memory, disk) |
| **Connector** | Plugin for a specific tool (Revit Connector, Rhino Connector, etc.) |

#### 6.2 Connectors

| Tool | Connector Maturity | Send | Receive | Object Types |
|------|-------------------|------|---------|-------------|
| **Rhino** | Stable | Full geometry | Full geometry | Points, curves, surfaces, meshes, SubD, blocks |
| **Grasshopper** | Stable | Any data | Any data | Geometry + custom objects |
| **Revit** | Stable | Elements + params | Native elements | Walls, floors, beams, columns, MEP, rooms, views |
| **Dynamo** | Stable | Any data | Any data | Geometry + Revit elements |
| **Blender** | Stable | Full scene | Full scene | Meshes, curves, empties, materials |
| **Unity** | Stable | Limited | Full scene | GameObjects, meshes, materials |
| **Unreal** | Stable | Limited | Full scene | Actors, static meshes |
| **AutoCAD** | Stable | 2D/3D entities | 2D/3D entities | Lines, polylines, blocks, solids |
| **ArchiCAD** | Stable | BIM elements | BIM elements | Walls, slabs, columns, beams, zones |
| **Excel** | Stable | Tabular data | Tabular data | Rows/columns as Speckle objects |
| **Power BI** | Stable | N/A | Read only | Data visualization of Speckle data |
| **QGIS** | Beta | GIS features | GIS features | Vector layers, attributes |
| **Tekla** | Beta | Structural elements | Limited | Beams, columns, plates |
| **ETABS/SAP2000** | Community | Structural model | Limited | Frames, shells, loads |
| **Bentley** | Community | Limited | Limited | Varies |

#### 6.3 Object Model and Conversion

Speckle uses a neutral object model that serves as the intermediary between tools. When you send a Revit wall, it becomes a Speckle `Objects.BuiltElements.Wall` with:
- `baseLine` (Speckle Line geometry)
- `height` (number)
- `type` (string)
- `parameters` (dictionary of Revit parameters)
- `displayValue` (mesh for visualization)
- `units` (string)

When received in Rhino, the wall's `displayValue` mesh is used for visualization, and its `baseLine` creates a Rhino curve.

When received in Revit, the converter attempts to find a matching wall type and creates a native Revit wall from the baseline and height.

**Key Conversion Principle**: Speckle always carries both the semantic object (with properties) and a display mesh. If the target tool can create the native element, it does. If not, it falls back to the display mesh.

#### 6.4 Speckle Automate

Serverless functions triggered by model changes:

**Use Cases**:
- **Model checking**: Validate that all walls have fire ratings assigned
- **Quantity extraction**: Calculate material quantities on every commit
- **Clash detection**: Check for spatial conflicts between branches
- **Report generation**: Create PDF reports from model data
- **Notification**: Alert team members when specific elements change
- **Analysis triggering**: Run energy or structural analysis on model update

**Architecture**:
1. User sends data to Speckle stream
2. Automation trigger fires based on stream/branch/event
3. Serverless function (Docker container) executes
4. Function reads commit data via Speckle SDK
5. Function processes data (check, analyze, transform)
6. Function posts results back to Speckle (as new commit, report, or status)

#### 6.5 GraphQL API

Speckle exposes a full GraphQL API for custom integrations:

```graphql
## Query streams (projects) accessible to the authenticated user
query {
  streams(limit: 10) {
    items {
      id
      name
      branches {
        items {
          name
          commits(limit: 5) {
            items {
              id
              message
              createdAt
              referencedObject
            }
          }
        }
      }
    }
  }
}

## Get a specific object by ID
query {
  stream(id: "stream-id") {
    object(id: "object-id") {
      data
      children(limit: 100) {
        objects {
          data
        }
      }
    }
  }
}
```

**Authentication**: Personal access tokens or OAuth2 for applications.

#### 6.6 Self-Hosting vs. Cloud

| Factor | Speckle Cloud (speckle.xyz) | Self-Hosted |
|--------|---------------------------|-------------|
| **Setup** | Instant | Docker Compose deployment |
| **Cost** | Free tier + paid plans | Infrastructure cost only |
| **Data residency** | EU (Speckle servers) | Your servers, your jurisdiction |
| **Compliance** | SOC2 in progress | Full control |
| **Maintenance** | Managed | Your responsibility |
| **Scaling** | Automatic | Manual (Kubernetes recommended) |
| **Custom domain** | No | Yes |
| **Best for** | Small-medium teams | Enterprise, government, regulated industries |

---

### 7. API Integration Patterns

#### 7.1 REST API Fundamentals for AEC

Most AEC platform APIs follow REST conventions:

| Verb | Action | AEC Example |
|------|--------|-------------|
| GET | Read | Fetch model metadata, list elements, get parameters |
| POST | Create | Create new element, upload model, trigger analysis |
| PUT | Update | Modify element properties, update model version |
| PATCH | Partial update | Update specific parameters without replacing entire element |
| DELETE | Remove | Delete element, remove model version |

**Common Response Patterns**:
- Pagination for large result sets (offset/limit or cursor-based)
- Filtering by element category, parameter value, spatial query
- Expansion of related resources (include linked elements in response)

#### 7.2 Authentication Patterns

| Pattern | Use Case | AEC Tools Using It |
|---------|----------|-------------------|
| **API Key** | Server-to-server, scripts | Mapbox, OpenWeatherMap, most utility APIs |
| **OAuth 2.0 (3-legged)** | User-authorized access | Autodesk Platform Services, Trimble Connect |
| **OAuth 2.0 (2-legged)** | App-only access (no user) | APS for backend processing |
| **Personal Access Token** | Developer/scripting use | Speckle, GitHub, GitLab |
| **Service Account** | Automated pipelines | Google Cloud, Azure, AWS |

#### 7.3 Autodesk Platform Services (APS / Forge)

The Autodesk Platform Services (formerly Forge) API provides cloud-based access to Autodesk's design and construction data.

**Key APIs**:

| API | Purpose | Typical Use |
|-----|---------|-------------|
| **Model Derivative** | Translate RVT/DWG/IFC to SVF2 for viewing, extract metadata | Web viewer, model interrogation |
| **Data Management** | Manage files in BIM360/ACC hubs, projects, folders | Automated upload/download, file management |
| **Viewer** | Embed 3D viewer in web applications | Design review portals, client presentations |
| **Design Automation** | Run Revit/AutoCAD/Inventor headlessly in the cloud | Automated drawing generation, batch parameter updates |
| **Webhooks** | Event notifications for model changes | Trigger downstream processes on model update |
| **Reality Capture** | Process photos into 3D models (photogrammetry) | Site documentation, as-built capture |
| **BIM360/ACC** | Project management, issues, RFIs, sheets | Construction management integration |

**Authentication Flow (2-Legged)**:
```
POST https://developer.api.autodesk.com/authentication/v2/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=YOUR_ID&client_secret=YOUR_SECRET&scope=data:read
```

#### 7.4 Webhook Patterns for Event-Driven AEC

```
Model Updated in BIM360/ACC
  -> Webhook fires to your server
    -> Server fetches updated model via APS API
      -> Server runs clash detection / compliance check
        -> Results posted back as BIM360 issue
          -> Team notified via Slack/Teams
```

**Implementation considerations**:
- Webhook endpoints must be publicly accessible (use ngrok for development)
- Implement idempotency (same event delivered twice should not cause duplicate actions)
- Queue events for processing (don't block the webhook response)
- Validate webhook signatures to prevent spoofing
- Set up retry logic for failed processing

#### 7.5 Rate Limiting and Error Handling

| Platform | Rate Limit | Strategy |
|----------|-----------|----------|
| APS/Forge | 100-500 req/min depending on API | Exponential backoff, request queuing |
| Speckle | 100 req/min (cloud) | Batch operations, GraphQL to reduce calls |
| Mapbox | 100,000 req/month (free) | Cache tiles locally, use vector tiles |
| BIM360 | Varies by endpoint | Respect `Retry-After` header |

**Error Handling Pattern**:
```python
import time
import requests

def api_call_with_retry(url, headers, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:  # Rate limited
            wait = int(response.headers.get('Retry-After', 2 ** attempt))
            time.sleep(wait)
        elif response.status_code >= 500:  # Server error
            time.sleep(2 ** attempt)
        else:
            response.raise_for_status()
    raise Exception(f"Failed after {max_retries} retries")
```

---

### 8. Schema Mapping

#### 8.1 Revit Category to IFC Entity Mapping

| Revit Category | IFC Entity (IFC4) | Notes |
|---------------|-------------------|-------|
| Walls | IfcWall / IfcWallStandardCase | StandardCase for straight, uniform walls |
| Floors | IfcSlab (FLOOR) | PredefinedType = FLOOR |
| Roofs | IfcSlab (ROOF) / IfcRoof | IfcRoof for compound, IfcSlab for simple |
| Ceilings | IfcCovering (CEILING) | PredefinedType = CEILING |
| Columns | IfcColumn | Architectural and structural |
| Beams | IfcBeam | Structural framing |
| Structural Foundations | IfcFooting | Various PredefinedTypes |
| Doors | IfcDoor | Hosted in IfcWall via IfcOpeningElement |
| Windows | IfcWindow | Hosted in IfcWall via IfcOpeningElement |
| Stairs | IfcStairFlight / IfcStair | IfcStair as container |
| Ramps | IfcRamp / IfcRampFlight | Similar to stairs |
| Railings | IfcRailing | PredefinedTypes: HANDRAIL, GUARDRAIL |
| Curtain Walls | IfcCurtainWall | Contains IfcPlate (panels) and IfcMember (mullions) |
| Curtain Panels | IfcPlate | PredefinedType = CURTAIN_PANEL |
| Curtain Mullions | IfcMember | PredefinedType = MULLION |
| Generic Models | IfcBuildingElementProxy | Catch-all for unmapped elements |
| Furniture | IfcFurniture | In IfcFurnishingElement hierarchy |
| Mechanical Equipment | IfcDistributionElement | Various subtypes |
| Plumbing Fixtures | IfcSanitaryTerminal | IfcFlowTerminal subtypes |
| Electrical Equipment | IfcElectricDistributionBoard | Various IfcDistribution subtypes |
| Ducts | IfcDuctSegment | IfcFlowSegment subtypes |
| Pipes | IfcPipeSegment | IfcFlowSegment subtypes |
| Rooms | IfcSpace | Spatial element |
| Areas | IfcZone | Spatial zone (less common) |
| Topography | IfcGeographicElement | New in IFC4 |
| Site | IfcSite | Spatial structure element |

#### 8.2 Revit Parameter to IFC Property Set Mapping

| Revit Parameter | IFC Property Set | IFC Property | Type |
|----------------|-----------------|--------------|------|
| Mark | Pset_WallCommon (etc.) | Reference | IfcIdentifier |
| Comments | Pset_WallCommon (etc.) | Description | IfcText |
| Phase Created | Custom / Pset | PhaseCreated | IfcLabel |
| Fire Rating | Pset_WallCommon | FireRating | IfcLabel |
| Thermal Resistance | Pset_WallCommon | ThermalTransmittance | IfcThermalTransmittanceMeasure |
| Structural | Pset_WallCommon | LoadBearing | IfcBoolean |
| Top Constraint | Mapped to geometry | N/A (geometric) | -- |
| Base Offset | Mapped to geometry | N/A (geometric) | -- |
| Area | BaseQuantities | NetSideArea | IfcAreaMeasure |
| Volume | BaseQuantities | NetVolume | IfcVolumeMeasure |

#### 8.3 Classification Systems

| System | Jurisdiction | Use | Example Code |
|--------|-------------|-----|-------------|
| **OmniClass** | USA/Canada | General AEC classification | 23-13 21 00 (Curtain Walls) |
| **UniClass 2015** | UK | Unified classification (UK BIM mandate) | Ss_25_10_30 (Curtain walling systems) |
| **Uniclass** | International | ISO 12006-2 based | EF_25_10 (Wall and barrier elements) |
| **MasterFormat** | USA/Canada | Specification divisions | 08 44 00 (Curtain Wall and Glazed Assemblies) |
| **UniFormat** | USA/Canada | Building systems | B2010 (Exterior Walls) |
| **IFC Classification** | International | BuildingSMART | IfcClassificationReference linking to any system |

#### 8.4 COBie Data Drops

COBie (Construction Operations Building Information Exchange) defines structured handover data at key project milestones:

| Drop | Stage | Data Required |
|------|-------|--------------|
| **COBie Drop 1** | Design | Facility, floors, spaces, zones (spatial structure) |
| **COBie Drop 2** | Construction Docs | Add types, components (major equipment), systems |
| **COBie Drop 3** | Construction | Add documents, warranties, spare parts, job data |
| **COBie Drop 4** | Commissioning | Add test results, commissioning data |
| **COBie Drop 5** | Handover | Complete dataset for facility management |

---

### 9. Coordinate System Management

#### 9.1 Revit Coordinate Systems

Revit maintains three coordinate reference points:

| Reference | Purpose | Visibility |
|-----------|---------|-----------|
| **Internal Origin** | Absolute 0,0,0 (never moves) | Not directly visible; use "Startup Location" in newer versions |
| **Project Base Point** | Defines project coordinate system, shown as circle with cross | Visible in site plan, can be clipped (pinned) or unclipped (moved) |
| **Survey Point** | Real-world survey coordinates, shown as triangle | Visible in site plan, typically set to survey marker or GPS coordinate |

**Shared Coordinates**: Revit's mechanism for aligning multiple linked models. Each linked model acquires its position relative to the host model's shared coordinate system.

**Workflow for Multi-Model Coordination**:
1. Establish survey point in host model matching real-world coordinates
2. Link discipline models
3. Use "Acquire Coordinates" from linked model or "Publish Coordinates" to linked model
4. All models now share a common coordinate system for clash detection and coordination

#### 9.2 Rhino Coordinate Systems

| Concept | Description |
|---------|-------------|
| **World Origin** | Absolute 0,0,0 (always exists) |
| **World XY** | Default construction plane at Z=0 |
| **CPlane** | Active construction plane (per viewport, can be set to any orientation) |
| **Named CPlanes** | Saved construction planes for repeated use |
| **Block Origin** | Local origin for block definitions |

**Best Practice**: Model with the World Origin at a project-meaningful location (building corner, site survey marker). This simplifies exchange with Revit and GIS tools.

#### 9.3 Geographic Coordinate Systems

| System | Type | Use | Precision |
|--------|------|-----|-----------|
| **WGS84** | Geographic (lat/lon) | GPS, global mapping, web maps | ~1 cm with full decimal degrees |
| **UTM** | Projected (meters) | Regional mapping, large sites | Sub-millimeter within zone |
| **State Plane (NAD83)** | Projected (ft or m) | US survey, local government | Sub-millimeter within zone |
| **OSGB36** | Projected (meters) | UK Ordnance Survey | Sub-millimeter within UK |
| **Local Grid** | Project-specific | Construction, site layout | Arbitrary precision |

**Coordinate Transformation Chain**:
```
GPS (WGS84 lat/lon/alt)
  -> Projected (UTM/State Plane, meters or feet)
    -> Local Site Grid (rotate/translate to align with site)
      -> Revit Shared Coordinates (survey point = local grid origin)
        -> Revit Internal (project base point offset)
          -> Rhino World (match Revit internal or shared)
```

#### 9.4 Common Unit Conversions

| From | To | Factor |
|------|-----|--------|
| mm | m | 0.001 |
| mm | ft | 0.00328084 |
| mm | in | 0.0393701 |
| m | ft | 3.28084 |
| m | in | 39.3701 |
| ft | m | 0.3048 |
| ft | mm | 304.8 |
| in | mm | 25.4 |
| in | m | 0.0254 |
| cm | in | 0.393701 |

**Critical Rule**: Always verify units at every exchange boundary. The Mars Climate Orbiter was lost because of a metric/imperial unit mismatch. AEC projects regularly suffer coordinate/dimension errors from the same root cause.

#### 9.5 Large Coordinate Handling

When working with real-world coordinates (e.g., UTM easting 500,000+ meters), floating-point precision issues arise:

**Problem**: IEEE 754 double-precision floats have ~15 significant digits. At UTM easting 500,000 m, sub-millimeter precision requires 9 digits (500000.000), leaving only 6 digits for the fractional part. This is sufficient for most AEC work, but:
- Geometry operations (intersection, Boolean) accumulate error
- Display rendering at large coordinates causes "jittering" (Z-fighting equivalent)
- Some tools use single-precision floats (7 significant digits), causing visible drift

**Mitigation Strategies**:
1. **Translate to local origin**: Subtract a large offset to bring coordinates near origin
2. **Use project-relative coordinates**: Define a project origin near the site center
3. **Double-precision everywhere**: Ensure all tools in the pipeline use double-precision
4. **Round-trip validation**: After coordinate transformations, validate against known survey points
5. **Revit approach**: The Project Base Point provides this translation; model near internal origin, survey point handles real-world mapping

#### 9.6 Coordinate Alignment Between Tools

**Step-by-step alignment procedure for Rhino ↔ Revit ↔ GIS**:

1. **Establish shared reference**: Choose a physical survey marker or building corner with known real-world coordinates (UTM or State Plane)

2. **Revit setup**:
   - Move Survey Point to the known real-world coordinate
   - Set Project Base Point to a convenient location near the building (e.g., grid intersection A-1)
   - Note the offset between Survey Point and Project Base Point

3. **Rhino setup**:
   - Set Rhino World Origin to match Revit's Project Base Point (for modeling convenience)
   - Document the offset to real-world coordinates
   - Alternatively, model at real-world coordinates if precision allows

4. **GIS setup**:
   - Use the same projection (UTM zone, State Plane) as the survey
   - Import building footprint at real-world coordinates
   - Verify alignment with aerial imagery or cadastral data

5. **Verification**:
   - Export a known point from each tool
   - Compare coordinates in a spreadsheet
   - Acceptable tolerance: <5 mm for building scale, <50 mm for site scale

---

### Quick Reference: Interoperability Decision Checklist

1. **What data needs to move?** Geometry only, geometry + metadata, metadata only, or relationships?
2. **What tools are involved?** Check the format compatibility matrix in the reference file.
3. **How often?** One-time -> file exchange. Iterative -> live linking. Continuous -> streaming.
4. **What fidelity is required?** Exact NURBS -> STEP/3DM. Visual mesh -> glTF/OBJ. Full BIM -> IFC/native.
5. **Who needs access?** Licensed users -> native format. Everyone -> web viewer (Speckle, APS Viewer). Fabricators -> DXF/STEP.
6. **What can be lost?** Accept geometry simplification? Lose parametric constraints? Lose material appearance?
7. **What coordinate system?** Align on shared origin, units, and projection before any exchange.
8. **What is the fallback?** If the primary pipeline fails, what manual workaround exists?


## scripting-reference

### Scripting Reference

> Python for Rhino and Grasshopper (RhinoCommon, rhinoscriptsyntax, ghpythonlib), C# for Grasshopper components, Python for Revit (pyRevit, RevitPythonShell), JavaScript for web 3D (Three.js), and code patterns for AEC computational design

## Scripting Reference for AEC Computational Design

### 1. Scripting in AEC Computational Design

#### Why Code Beyond Visual Programming

Visual programming environments like Grasshopper, Dynamo, and Marionette have democratized computational design for architects and engineers. But they hit hard walls in practice:

- **Complexity ceiling**: Definitions beyond ~200 nodes become unreadable spaghetti, impossible to maintain or hand off.
- **Control flow limitations**: Try writing a recursive space-partitioning algorithm in pure Grasshopper. You cannot. Loops require plugins (Anemone, Hoopsnake) that add fragility.
- **Performance**: Visual node evaluation carries overhead. A Python loop processing 50,000 mesh vertices runs 5-20x faster than equivalent wired-up components.
- **Data management**: Parsing CSV, calling REST APIs, reading databases, writing Excel reports — all trivial in code, painful or impossible in visual programming.
- **Version control**: A `.gh` file is a binary blob. A `.py` file is diffable, mergeable, reviewable text.
- **Reusability**: Functions, classes, modules, packages — code is composable at every scale.
- **Testing**: You can unit-test a Python function. You cannot unit-test a Grasshopper cluster.

#### The Scripting Spectrum

| Level | Tool | Difficulty | Use Case |
|-------|------|------------|----------|
| Entry | rhinoscriptsyntax (rs) | Easy | Quick automation, batch ops, simple geometry |
| Intermediate | RhinoCommon (Python) | Medium | Complex geometry, intersections, analysis |
| Intermediate | GhPython | Medium | Custom GH components, data tree manipulation |
| Advanced | C# in GH | Hard | Performance-critical components, custom .gha |
| Advanced | pyRevit / Dynamo Python | Medium | Revit automation, BIM scripting |
| Advanced | Full .NET (C#/F#) | Hard | Production plugins, commercial tools |
| Specialist | Three.js / WebGL | Medium | Web viewers, interactive presentations |

#### Choosing the Right Language

**Python** — Use when:
- Rapid prototyping and iteration matter most
- You need quick automation scripts (Rhino or Revit)
- Working with data (CSV, JSON, API calls)
- Algorithmic design exploration in Grasshopper
- Team includes non-programmers who need to read the code

**C#** — Use when:
- Performance is paramount (10-100x faster than Python for tight loops)
- Building distributable Grasshopper plugins (.gha)
- You need strong typing to catch errors at compile time
- Integrating with .NET ecosystem libraries
- Building production-grade Revit add-ins

**JavaScript/TypeScript** — Use when:
- Building web-based viewers and dashboards
- Client-facing model presentations
- Collaborative design platforms
- AR/VR experiences via WebXR
- Integration with Speckle, IFC.js, or custom APIs

#### Python vs. C# for AEC — A Practical Comparison

```
Feature               Python                    C#
─────────────────────────────────────────────────────────────
Typing                Dynamic                   Static
Speed                 1x (baseline)             10-100x
REPL                  Yes (interactive)         No (compile required)
GH Component          GhPython node             Scripting / Visual Studio
Learning curve        Gentle                    Steeper
Error detection       Runtime                   Compile-time
Deployment            .py files                 .gha / .dll
External libraries    pip (huge ecosystem)      NuGet (large ecosystem)
Data science          Excellent (numpy, pandas) Good (MathNet, ML.NET)
String handling       Superior                  Adequate
Memory management     Automatic (GC)            Automatic (GC)
Multithreading        GIL limitation            Full parallel support
```

---

### 2. Python for Rhino (rhinoscriptsyntax)

The `rhinoscriptsyntax` module (imported as `rs`) wraps RhinoCommon in friendly, high-level functions. It is the fastest way to automate Rhino.

#### Module Overview

```python
import rhinoscriptsyntax as rs
```

#### Object Creation Patterns

```python
## Points
pt = rs.AddPoint(0, 0, 0)
pt2 = rs.AddPoint([10, 5, 3])

## Lines
line = rs.AddLine([0,0,0], [10,0,0])
line2 = rs.AddLine(rs.GetPoint("Start"), rs.GetPoint("End"))

## Polylines
pts = [[0,0,0],[5,0,0],[5,5,0],[0,5,0],[0,0,0]]
pline = rs.AddPolyline(pts)

## Curves
crv = rs.AddCurve(pts, degree=3)  # NURBS curve
interp = rs.AddInterpCurve(pts)    # interpolated through points

## Circles and Arcs
circle = rs.AddCircle([0,0,0], 5.0)
arc = rs.AddArc3Pt([0,0,0], [10,0,0], [5,5,0])
ellipse = rs.AddEllipse([0,0,0], 10, 5)

## Rectangles
rect = rs.AddRectangle([0,0,0], 10, 5)

## Surfaces
srf = rs.AddSrfPt([[0,0,0],[10,0,0],[10,10,0],[0,10,0]])
pipe = rs.AddPipe(crv, 0, 1.0)
loft = rs.AddLoftSrf([crv1, crv2])
extrusion = rs.ExtrudeCurveStraight(crv, [0,0,0], [0,0,5])
revolve = rs.AddRevSrf(profile_crv, axis_line)

## Meshes
mesh = rs.AddMesh([[0,0,0],[1,0,0],[1,1,0],[0,1,0]], [[0,1,2,3]])

## Solids
box = rs.AddBox([[0,0,0],[10,0,0],[10,10,0],[0,10,0],
                  [0,0,5],[10,0,5],[10,10,5],[0,10,5]])
sphere = rs.AddSphere([0,0,0], 5.0)
cylinder = rs.AddCylinder([0,0,0], [0,0,10], 3.0)
cone = rs.AddCone([0,0,0], [0,0,10], 5.0)

## Text and annotations
text = rs.AddText("Building A", [0,0,0], height=2.0)
dot = rs.AddTextDot("Label", [5,5,0])
leader = rs.AddLeader([[0,0,0],[5,5,0],[10,5,0]])
dim = rs.AddLinearDimension([0,0,0], [10,0,0], [5,2,0])
```

#### Object Query Patterns

```python
## Selection
objs = rs.GetObjects("Select objects")
obj = rs.GetObject("Select one curve", rs.filter.curve)
pt = rs.GetPoint("Pick a point")

## By layer
layer_objs = rs.ObjectsByLayer("Walls")

## By type
all_curves = rs.ObjectsByType(rs.filter.curve)
all_surfs = rs.ObjectsByType(rs.filter.surface)
all_meshes = rs.ObjectsByType(rs.filter.mesh)

## By group
group_objs = rs.ObjectsByGroup("FloorPlan")

## Properties
obj_type = rs.ObjectType(obj)         # integer type code
obj_name = rs.ObjectName(obj)         # user-assigned name
obj_layer = rs.ObjectLayer(obj)       # layer name
obj_color = rs.ObjectColor(obj)       # (R,G,B) tuple
```

#### Transformation Methods

```python
## Move
rs.MoveObject(obj, [10, 0, 0])
rs.MoveObjects(objs, [0, 5, 0])

## Rotate (angle in degrees)
rs.RotateObject(obj, [0,0,0], 45)
rs.RotateObject(obj, [0,0,0], 90, axis=[0,0,1])

## Scale
rs.ScaleObject(obj, [0,0,0], [2, 2, 2])         # uniform
rs.ScaleObject(obj, [0,0,0], [1, 1, 3])         # non-uniform

## Mirror
rs.MirrorObject(obj, [0,0,0], [0,1,0])

## Copy
copy = rs.CopyObject(obj, [10, 0, 0])
copies = rs.CopyObjects(objs, [5, 5, 0])

## Orient
rs.OrientObject(obj, [ref1, ref2], [target1, target2])

## Array
rs.ArrayLinear(obj, count=5, offset=[10,0,0])
rs.ArrayPolar(obj, count=6, angle=360, center=[0,0,0])
```

#### Layer Management

```python
## Create layers
rs.AddLayer("Architecture")
rs.AddLayer("Walls", color=(200, 50, 50), parent="Architecture")
rs.AddLayer("Columns", color=(50, 50, 200), parent="Architecture")

## Layer properties
rs.CurrentLayer("Walls")
rs.LayerColor("Walls", (255, 0, 0))
rs.LayerVisible("Furniture", False)
rs.LayerLocked("Base Plan", True)
rs.LayerPrintWidth("Walls", 0.5)

## Bulk operations
all_layers = rs.LayerNames()
rs.PurgeLayer("Temp Construction")

## Move objects between layers
for obj in rs.ObjectsByLayer("Old Layer"):
    rs.ObjectLayer(obj, "New Layer")
```

#### User Interaction

```python
## Input
point = rs.GetPoint("Click a point")
string = rs.GetString("Enter building name", "Default")
number = rs.GetReal("Enter floor height", 3.0, 2.5, 6.0)
integer = rs.GetInteger("Number of floors", 5, 1, 100)
boolean = rs.GetBoolean("Options", ["Visible","Yes","No"], [True])

## Output
rs.MessageBox("Operation complete!")
print("Processed {} objects".format(len(objs)))

## Selection
rs.SelectObject(obj)
rs.SelectObjects(objs)
rs.UnselectAllObjects()
```

#### Geometry Analysis

```python
length = rs.CurveLength(crv)
area = rs.SurfaceArea(srf)             # returns [area, error]
volume = rs.SurfaceVolume(closed_brep)  # returns [volume, error]
centroid = rs.SurfaceAreaCentroid(srf)  # returns [point, error]

dist = rs.Distance([0,0,0], [10,10,0])
angle = rs.Angle([0,0,0], [10,10,0])

bbox = rs.BoundingBox(obj)             # 8 corner points
is_closed = rs.IsCurveClosed(crv)
is_planar = rs.IsCurvePlanar(crv)
degree = rs.CurveDegree(crv)
domain = rs.CurveDomain(crv)
```

#### Common Recipes

```python
## Batch rename objects by layer
for obj in rs.AllObjects():
    layer = rs.ObjectLayer(obj)
    idx = rs.ObjectsByLayer(layer).index(obj)
    rs.ObjectName(obj, "{}_{}".format(layer, idx))

## Export each layer to separate file
for layer in rs.LayerNames():
    objs = rs.ObjectsByLayer(layer)
    if objs:
        rs.SelectObjects(objs)
        rs.Command("_-Export \"{}.3dm\" _Enter".format(layer))
        rs.UnselectAllObjects()

## Generate grid of points
for x in range(0, 100, 10):
    for y in range(0, 80, 10):
        rs.AddPoint(x, y, 0)

## Offset all curves on a layer inward
for crv in rs.ObjectsByLayer("Site Boundary"):
    offsets = rs.OffsetCurve(crv, rs.CurveAreaCentroid(crv)[0], 3.0)
```

---

### 3. Python for Rhino (RhinoCommon)

RhinoCommon is the full .NET geometry library. It gives precise control over every geometric operation.

#### Namespace Structure

```python
import Rhino
import Rhino.Geometry as rg
import Rhino.DocObjects as rd
import Rhino.Input as ri
import Rhino.RhinoDoc as doc

## Key classes in Rhino.Geometry:
## Point3d, Vector3d, Plane, Line, Arc, Circle, Polyline,
## NurbsCurve, PolylineCurve, BrepFace, BrepEdge,
## Surface, NurbsSurface, Brep, Mesh, Transform,
## BoundingBox, Interval, Point2d
```

#### Point3d and Vector3d Operations

```python
## Creation
p1 = rg.Point3d(0, 0, 0)
p2 = rg.Point3d(10, 5, 3)
v1 = rg.Vector3d(1, 0, 0)
v2 = rg.Vector3d(0, 1, 0)

## Arithmetic
p3 = p1 + v1              # Point + Vector = Point
v3 = p2 - p1              # Point - Point = Vector
v4 = v1 + v2              # Vector + Vector = Vector
v5 = v1 * 5.0             # scalar multiplication
v6 = v1 / 2.0             # scalar division

## Vector operations
dot = v1 * v2                        # dot product (0 = perpendicular)
cross = rg.Vector3d.CrossProduct(v1, v2)  # cross product
v1.Unitize()                         # normalize in-place
unit = v1 / v1.Length                # manual unitize
length = v1.Length
angle = rg.Vector3d.VectorAngle(v1, v2)  # radians

## Distance
dist = p1.DistanceTo(p2)

## Static members
origin = rg.Point3d.Origin           # (0,0,0)
xaxis = rg.Vector3d.XAxis            # (1,0,0)
yaxis = rg.Vector3d.YAxis            # (0,1,0)
zaxis = rg.Vector3d.ZAxis            # (0,0,1)
```

#### Curve Creation

```python
## Line
ln = rg.Line(p1, p2)
ln_crv = rg.LineCurve(ln)

## Circle
circle = rg.Circle(rg.Plane.WorldXY, 5.0)
circle_crv = circle.ToNurbsCurve()

## Arc
arc = rg.Arc(p1, p2, p3)  # through 3 points
arc_crv = arc.ToNurbsCurve()

## Polyline
pline = rg.Polyline([rg.Point3d(x, 0, 0) for x in range(11)])
pline_crv = pline.ToPolylineCurve()

## NurbsCurve by control points
pts = [rg.Point3d(i*10, (i%3)*5, 0) for i in range(6)]
nc = rg.NurbsCurve.Create(False, 3, pts)  # open, degree 3

## Interpolated curve
interp = rg.Curve.CreateInterpolatedCurve(pts, 3)

## Fillet / Chamfer
filleted = rg.Curve.CreateFilletCurves(crv1, t1, crv2, t2, radius,
                                        True, True, True, 0.001, 0.001)

## Offset
offsets = crv.Offset(rg.Plane.WorldXY, 5.0, 0.01,
                      rg.CurveOffsetCornerStyle.Sharp)

## Boolean on closed planar curves
union = rg.Curve.CreateBooleanUnion(curves, 0.001)
diff = rg.Curve.CreateBooleanDifference(crv1, crv2, 0.001)
inter = rg.Curve.CreateBooleanIntersection(crv1, crv2, 0.001)
```

#### Surface and Brep Creation

```python
## Planar surface from closed curve
breps = rg.Brep.CreatePlanarBreps(closed_crv, 0.001)

## Extrusion
ext = rg.Extrusion.Create(profile_crv, height, cap=True)
ext_brep = ext.ToBrep()

## Loft
loft = rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset,
                                rg.LoftType.Normal, False)

## Sweep
sweep1 = rg.Brep.CreateFromSweep(rail, section, closed=False, tol=0.001)

## NurbsSurface from point grid
srf = rg.NurbsSurface.CreateFromPoints(pts_2d_list, u_count, v_count,
                                         u_degree, v_degree)

## Boolean operations
union = rg.Brep.CreateBooleanUnion(breps, 0.001)
diff = rg.Brep.CreateBooleanDifference(brep1, brep2, 0.001)
inter = rg.Brep.CreateBooleanIntersection(brep1, brep2, 0.001)

## Planar surface from corner points
srf = rg.NurbsSurface.CreateFromCorners(p1, p2, p3, p4)
```

#### Mesh Creation

```python
mesh = rg.Mesh()
mesh.Vertices.Add(0, 0, 0)
mesh.Vertices.Add(10, 0, 0)
mesh.Vertices.Add(10, 10, 0)
mesh.Vertices.Add(0, 10, 0)
mesh.Faces.AddFace(0, 1, 2, 3)  # quad
mesh.Normals.ComputeNormals()
mesh.Compact()

## From Brep
meshes = rg.Mesh.CreateFromBrep(brep, rg.MeshingParameters.Default)

## Mesh operations
mesh.Weld(Math.PI)                # weld vertices
mesh.UnifyNormals()               # consistent normals
mesh.RebuildNormals()
vol = rg.VolumeMassProperties.Compute(mesh)
area = rg.AreaMassProperties.Compute(mesh)
```

#### Intersection Methods

```python
## Curve-Curve
events = rg.Intersect.Intersection.CurveCurve(crv1, crv2, 0.001, 0.001)
for e in events:
    pt = e.PointA
    param_a = e.ParameterA
    param_b = e.ParameterB
    is_overlap = e.IsOverlap

## Curve-Surface
events = rg.Intersect.Intersection.CurveSurface(crv, srf, 0.001, 0.001)
for e in events:
    pt = e.PointA

## Brep-Brep
result, curves, pts = rg.Intersect.Intersection.BrepBrep(brep1, brep2, 0.001)

## Mesh-Ray
ray = rg.Ray3d(origin_pt, direction_vec)
t = rg.Intersect.Intersection.MeshRay(mesh, ray)
if t >= 0:
    hit_pt = ray.PointAt(t)

## Line-Plane
result, t = rg.Intersect.Intersection.LinePlane(line, plane)
if result:
    hit = line.PointAt(t)

## Brep-Plane (section)
result, curves, pts = rg.Intersect.Intersection.BrepPlane(brep, plane, 0.001)
```

#### Transform Class

```python
## Translation
xform = rg.Transform.Translation(rg.Vector3d(10, 0, 0))

## Rotation (angle in radians)
xform = rg.Transform.Rotation(Math.PI / 4, rg.Vector3d.ZAxis, rg.Point3d.Origin)

## Scale
xform = rg.Transform.Scale(rg.Point3d.Origin, 2.0)        # uniform
xform = rg.Transform.Scale(rg.Plane.WorldXY, 2.0, 1.0, 3.0) # non-uniform

## PlaneToPlane
xform = rg.Transform.PlaneToPlane(source_plane, target_plane)

## Mirror
xform = rg.Transform.Mirror(rg.Plane.WorldXY)

## Apply
obj_copy = obj.Duplicate()
obj_copy.Transform(xform)

## Combine transforms
combined = xform1 * xform2  # xform2 applied first
```

#### BoundingBox, Plane, Interval

```python
## BoundingBox
bbox = obj.GetBoundingBox(True)
min_pt = bbox.Min
max_pt = bbox.Max
center = bbox.Center
diagonal = bbox.Diagonal
is_valid = bbox.IsValid

## Plane
plane = rg.Plane(origin, normal)
plane = rg.Plane(origin, x_axis, y_axis)
plane = rg.Plane.WorldXY
closest = plane.ClosestPoint(test_pt)

## Interval (parameter domain)
interval = rg.Interval(0.0, 1.0)
mid = interval.Mid
length = interval.Length
t = interval.ParameterAt(0.5)  # normalized
```

---

### 4. GhPython (Python in Grasshopper)

#### Component Setup

In the GhPython component (or Script component in GH2):

- **Inputs**: Right-click each input to set Access (Item / List / Tree) and Type Hint (Point3d, Curve, float, str, etc.)
- **Outputs**: Name outputs at the bottom of the component
- **Type hints** are critical: without them, all inputs arrive as `IGH_Goo` wrappers

#### Data Tree Handling

```python
import Grasshopper as gh
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path

## Create a data tree
tree = DataTree[object]()
for i in range(5):
    path = GH_Path(i)
    for j in range(10):
        tree.Add(rg.Point3d(i*10, j*10, 0), path)

## Iterate a data tree
for i in range(tree.BranchCount):
    path = tree.Path(i)
    branch = tree.Branch(i)
    for item in branch:
        print(item)

## Flatten
flat = tree.AllData()

## Graft (each item in its own branch)
grafted = DataTree[object]()
for i, item in enumerate(flat_list):
    grafted.Add(item, GH_Path(i))

## Output
a = tree  # assign to output parameter 'a'
```

#### Script Structure Pattern

```python
"""GhPython component: Generate Building Massing"""
import Rhino.Geometry as rg
import Grasshopper as gh
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path
import math

## ── INPUTS ──────────────────────────────
## footprint   : Curve (Item)
## floors      : int (Item)
## floor_h     : float (Item)
## setback     : float (Item)

## ── LOGIC ───────────────────────────────
masses = []
sections = []

for i in range(floors):
    z = i * floor_h
    offset_dist = setback * i

    plane = rg.Plane(rg.Point3d(0, 0, z), rg.Vector3d.ZAxis)

    if offset_dist > 0:
        offset = footprint.Offset(plane, -offset_dist, 0.01,
                                   rg.CurveOffsetCornerStyle.Sharp)
        if offset and len(offset) > 0:
            section = offset[0]
        else:
            break
    else:
        section = footprint.DuplicateCurve()
        xform = rg.Transform.Translation(0, 0, z)
        section.Transform(xform)

    sections.append(section)

    # Extrude this floor
    ext_vec = rg.Vector3d(0, 0, floor_h)
    srf = rg.Extrusion.Create(section, floor_h, True)
    if srf:
        masses.append(srf.ToBrep())

## ── OUTPUTS ─────────────────────────────
a = masses      # List of Breps
b = sections    # List of Curves
c = sum(rg.AreaMassProperties.Compute(m).Area for m in masses if m)  # Total facade area
```

#### Performance with ghpythonlib

```python
import ghpythonlib.parallel as ghp

def process_point(pt):
    """Heavy operation per point."""
    circle = rg.Circle(rg.Plane(pt, rg.Vector3d.ZAxis), radius)
    return circle.ToNurbsCurve()

## Parallel map — uses all CPU cores
results = ghp.run(process_point, points, True)
```

#### Sticky Dictionary for Persistence

```python
import scriptcontext as sc

## Store data between runs
if "my_cache" not in sc.sticky:
    sc.sticky["my_cache"] = expensive_computation()

cached = sc.sticky["my_cache"]
```

---

### 5. C# for Grasshopper

#### C# Scripting Component

```csharp
// Inputs:  pts (List<Point3d>), radius (double), height (double)
// Outputs: A (List<Brep>), B (double)

using Rhino.Geometry;
using System.Collections.Generic;
using System.Linq;

private void RunScript(List<Point3d> pts, double radius, double height,
                        ref object A, ref object B)
{
    var breps = new List<Brep>();

    foreach (var pt in pts)
    {
        var plane = new Plane(pt, Vector3d.ZAxis);
        var circle = new Circle(plane, radius);
        var crv = circle.ToNurbsCurve();
        var ext = Extrusion.Create(crv, height, true);
        if (ext != null)
            breps.Add(ext.ToBrep());
    }

    double totalVolume = breps
        .Select(b => VolumeMassProperties.Compute(b))
        .Where(v => v != null)
        .Sum(v => v.Volume);

    A = breps;
    B = totalVolume;
}
```

#### DataTree<T> in C#

```csharp
using Grasshopper;
using Grasshopper.Kernel.Data;
using Grasshopper.Kernel.Types;

var tree = new DataTree<Point3d>();

for (int i = 0; i < 5; i++)
{
    var path = new GH_Path(i);
    for (int j = 0; j < 10; j++)
    {
        tree.Add(new Point3d(i * 10, j * 10, 0), path);
    }
}

// Iterate
for (int i = 0; i < tree.BranchCount; i++)
{
    GH_Path path = tree.Path(i);
    List<Point3d> branch = tree.Branch(i);
    foreach (var pt in branch) { /* ... */ }
}
```

#### Custom GH_Component Development

```csharp
using Grasshopper.Kernel;
using Rhino.Geometry;
using System;

public class BuildingMassComponent : GH_Component
{
    public BuildingMassComponent()
        : base("Building Mass", "BldgMass",
               "Generate stepped building massing",
               "AEC Tools", "Massing")
    { }

    protected override void RegisterInputParams(GH_InputParamManager pManager)
    {
        pManager.AddCurveParameter("Footprint", "F", "Building footprint curve",
                                    GH_ParamAccess.item);
        pManager.AddIntegerParameter("Floors", "N", "Number of floors",
                                      GH_ParamAccess.item, 5);
        pManager.AddNumberParameter("Floor Height", "H", "Height per floor",
                                     GH_ParamAccess.item, 3.0);
    }

    protected override void RegisterOutputParams(GH_OutputParamManager pManager)
    {
        pManager.AddBrepParameter("Massing", "M", "Building massing breps",
                                   GH_ParamAccess.list);
        pManager.AddNumberParameter("GFA", "A", "Gross floor area",
                                     GH_ParamAccess.item);
    }

    protected override void SolveInstance(IGH_DataAccess DA)
    {
        Curve footprint = null;
        int floors = 5;
        double floorH = 3.0;

        if (!DA.GetData(0, ref footprint)) return;
        DA.GetData(1, ref floors);
        DA.GetData(2, ref floorH);

        var breps = new List<Brep>();
        double gfa = 0;

        for (int i = 0; i < floors; i++)
        {
            var moved = footprint.DuplicateCurve();
            moved.Transform(Transform.Translation(0, 0, i * floorH));
            var ext = Extrusion.Create(moved, floorH, true);
            if (ext != null)
            {
                breps.Add(ext.ToBrep());
                var area = AreaMassProperties.Compute(moved);
                if (area != null) gfa += area.Area;
            }
        }

        DA.SetDataList(0, breps);
        DA.SetData(1, gfa);
    }

    protected override System.Drawing.Bitmap Icon => null; // embed your 24x24 icon
    public override Guid ComponentGuid => new Guid("A1B2C3D4-E5F6-7890-ABCD-EF1234567890");
    public override GH_Exposure Exposure => GH_Exposure.primary;
}
```

#### Building and Deploying .gha

1. Create a Class Library (.NET Framework 4.8) project in Visual Studio
2. Add NuGet references: `Grasshopper` (includes RhinoCommon)
3. Set build output to `%APPDATA%\Grasshopper\Libraries\`
4. Build → the `.gha` file loads automatically when GH starts
5. For distribution, use the Yak package manager: `yak build` and `yak push`

---

### 6. Python for Revit

#### RevitPythonShell (RPS)

```python
## Available globals in RPS:
## __revit__  → Autodesk.Revit.UI.UIApplication
## doc        → Autodesk.Revit.DB.Document (active document)
## uidoc      → Autodesk.Revit.UI.UIDocument
## app        → Autodesk.Revit.ApplicationServices.Application

import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
```

#### pyRevit Script Structure

```python
"""pyRevit script: Select All Walls on Active View"""
## -*- coding: utf-8 -*-
__title__ = "Select Walls"
__author__ = "AEC Scripter"

from pyrevit import revit, DB, UI, script, forms

doc = revit.doc
uidoc = revit.uidoc
output = script.get_output()

## Collect all walls in active view
walls = DB.FilteredElementCollector(doc, doc.ActiveView.Id)\
          .OfClass(DB.Wall)\
          .WhereElementIsNotElementType()\
          .ToElements()

output.print_md("## Found {} walls".format(len(walls)))
for w in walls:
    output.print_md("- **{}** | Width: {} | Level: {}".format(
        w.Name,
        w.Width,
        doc.GetElement(w.LevelId).Name
    ))
```

#### Dynamo Python Script Node

```python
## CPython 3 node (Revit 2023+)
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
clr.AddReference('RevitNodes')

from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

## Inputs from Dynamo
level_name = IN[0]
```

#### FilteredElementCollector Patterns

```python
## All walls in document
walls = FilteredElementCollector(doc)\
        .OfClass(Wall)\
        .WhereElementIsNotElementType()\
        .ToElements()

## All floor plan views
plans = FilteredElementCollector(doc)\
        .OfClass(ViewPlan)\
        .WhereElementIsNotElementType()\
        .ToElements()

## All family instances of a specific category
columns = FilteredElementCollector(doc)\
          .OfCategory(BuiltInCategory.OST_StructuralColumns)\
          .OfClass(FamilyInstance)\
          .ToElements()

## Elements in a specific view
view_elements = FilteredElementCollector(doc, active_view.Id)\
                .WhereElementIsNotElementType()\
                .ToElements()

## Using parameter filters
provider = ParameterValueProvider(ElementId(BuiltInParameter.WALL_BASE_CONSTRAINT))
rule = FilterStringRule(provider, FilterStringEquals(), "Level 1")
param_filter = ElementParameterFilter(rule)
walls_on_level1 = FilteredElementCollector(doc)\
                  .OfClass(Wall)\
                  .WherePasses(param_filter)\
                  .ToElements()

## Rooms
rooms = FilteredElementCollector(doc)\
        .OfClass(SpatialElement)\
        .OfCategory(BuiltInCategory.OST_Rooms)\
        .ToElements()
```

#### Parameter Read/Write

```python
## Read parameters
wall = walls[0]

## Built-in parameter
base_offset = wall.get_Parameter(BuiltInParameter.WALL_BASE_OFFSET).AsDouble()

## Named parameter (shared or project)
param = wall.LookupParameter("Fire Rating")
if param:
    if param.StorageType == StorageType.String:
        value = param.AsString()
    elif param.StorageType == StorageType.Double:
        value = param.AsDouble()
    elif param.StorageType == StorageType.Integer:
        value = param.AsInteger()
    elif param.StorageType == StorageType.ElementId:
        value = param.AsElementId()

## Write parameter (must be inside a Transaction)
t = Transaction(doc, "Set Fire Rating")
t.Start()
try:
    for wall in walls:
        param = wall.LookupParameter("Fire Rating")
        if param and not param.IsReadOnly:
            param.Set("2 Hour")
    t.Commit()
except Exception as e:
    t.RollBack()
    print("Error: {}".format(e))
```

#### Transaction Management

```python
## Simple pattern
t = Transaction(doc, "Create Walls")
t.Start()
try:
    # ... Revit operations ...
    t.Commit()
except:
    t.RollBack()
    raise

## Transaction group (for undoable groups)
tg = TransactionGroup(doc, "Batch Operation")
tg.Start()
## ... multiple transactions ...
tg.Assimilate()  # or tg.RollBack()

## Sub-transaction (within an open Transaction)
st = SubTransaction(doc)
st.Start()
## ... operations ...
st.Commit()  # or st.RollBack()
```

#### Common Revit Automation Recipes

```python
## 1. Create a wall
line = Line.CreateBound(XYZ(0,0,0), XYZ(20,0,0))
level = FilteredElementCollector(doc).OfClass(Level).FirstElement()
wall_type = FilteredElementCollector(doc).OfClass(WallType).FirstElement()

t = Transaction(doc, "Create Wall")
t.Start()
wall = Wall.Create(doc, line, wall_type.Id, level.Id, 10.0, 0.0, False, False)
t.Commit()

## 2. Place family instance
symbol = FilteredElementCollector(doc)\
         .OfClass(FamilySymbol)\
         .FirstElement()
t = Transaction(doc, "Place Family")
t.Start()
if not symbol.IsActive:
    symbol.Activate()
instance = doc.Create.NewFamilyInstance(XYZ(10,10,0), symbol,
                                        level, StructuralType.NonStructural)
t.Commit()

## 3. Create floor
curve_loop = CurveLoop()
curve_loop.Append(Line.CreateBound(XYZ(0,0,0), XYZ(20,0,0)))
curve_loop.Append(Line.CreateBound(XYZ(20,0,0), XYZ(20,15,0)))
curve_loop.Append(Line.CreateBound(XYZ(20,15,0), XYZ(0,15,0)))
curve_loop.Append(Line.CreateBound(XYZ(0,15,0), XYZ(0,0,0)))

floor_type = FilteredElementCollector(doc).OfClass(FloorType).FirstElement()
t = Transaction(doc, "Create Floor")
t.Start()
floor = Floor.Create(doc, [curve_loop], floor_type.Id, level.Id)
t.Commit()

## 4. Create sheet and place views
t = Transaction(doc, "Create Sheet")
t.Start()
titleblock = FilteredElementCollector(doc)\
             .OfClass(FamilySymbol)\
             .OfCategory(BuiltInCategory.OST_TitleBlocks)\
             .FirstElement()
sheet = ViewSheet.Create(doc, titleblock.Id)
sheet.Name = "Floor Plans"
sheet.SheetNumber = "A-101"

## Place view on sheet
vp = Viewport.Create(doc, sheet.Id, plan_view.Id, XYZ(1.0, 0.75, 0))
t.Commit()

## 5. Export to DWG
options = DWGExportOptions()
options.MergedViews = True
views_to_export = List[ElementId]()
views_to_export.Add(active_view.Id)
doc.Export("C:\\Export", "output.dwg", views_to_export, options)

## 6. Get room boundaries
for room in rooms:
    options = SpatialElementBoundaryOptions()
    boundaries = room.GetBoundarySegments(options)
    for loop in boundaries:
        for seg in loop:
            curve = seg.GetCurve()
            # process boundary curve

## 7. Color elements by parameter value
t = Transaction(doc, "Color by Value")
t.Start()
ogs = OverrideGraphicSettings()
ogs.SetProjectionLineColor(Color(255, 0, 0))
for wall in walls:
    if wall.LookupParameter("Fire Rating").AsString() == "2 Hour":
        doc.ActiveView.SetElementOverrides(wall.Id, ogs)
t.Commit()

## 8. Schedule data extraction
schedules = FilteredElementCollector(doc)\
            .OfClass(ViewSchedule)\
            .ToElements()
for sched in schedules:
    table = sched.GetTableData()
    section = table.GetSectionData(SectionType.Body)
    for row in range(section.NumberOfRows):
        for col in range(section.NumberOfColumns):
            cell = sched.GetCellText(SectionType.Body, row, col)
```

---

### 7. JavaScript for Web 3D

#### Three.js Fundamentals

```javascript
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

// Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xf0f0f0);

// Camera
const camera = new THREE.PerspectiveCamera(
    60,                                    // FOV
    window.innerWidth / window.innerHeight, // aspect
    0.1,                                   // near
    10000                                  // far
);
camera.position.set(50, 30, 50);
camera.lookAt(0, 0, 0);

// Renderer
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
document.body.appendChild(renderer.domElement);

// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.maxPolarAngle = Math.PI / 2;  // prevent going below ground

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(50, 100, 50);
directionalLight.castShadow = true;
directionalLight.shadow.mapSize.set(2048, 2048);
directionalLight.shadow.camera.left = -100;
directionalLight.shadow.camera.right = 100;
directionalLight.shadow.camera.top = 100;
directionalLight.shadow.camera.bottom = -100;
scene.add(directionalLight);

// Ground plane
const groundGeo = new THREE.PlaneGeometry(1000, 1000);
const groundMat = new THREE.MeshStandardMaterial({ color: 0xcccccc });
const ground = new THREE.Mesh(groundGeo, groundMat);
ground.rotation.x = -Math.PI / 2;
ground.receiveShadow = true;
scene.add(ground);

// Grid helper
const grid = new THREE.GridHelper(200, 20);
scene.add(grid);

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}
animate();

// Responsive resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
```

#### Loading AEC Models

```javascript
// glTF (standard for web 3D)
const gltfLoader = new GLTFLoader();
gltfLoader.load('building.glb', (gltf) => {
    const model = gltf.scene;
    model.traverse((child) => {
        if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
        }
    });
    scene.add(model);
});

// IFC via web-ifc-three
import { IFCLoader } from 'web-ifc-three/IFCLoader';
const ifcLoader = new IFCLoader();
ifcLoader.ifcManager.setWasmPath('wasm/');
ifcLoader.load('model.ifc', (ifcModel) => {
    scene.add(ifcModel);
});
```

#### Raycasting for Selection

```javascript
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

renderer.domElement.addEventListener('click', (event) => {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(scene.children, true);

    if (intersects.length > 0) {
        const selected = intersects[0].object;
        // Highlight selected
        selected.material = selected.material.clone();
        selected.material.emissive.set(0x444444);

        console.log('Selected:', selected.name, selected.userData);
    }
});
```

#### Materials for AEC

```javascript
// Glass
const glassMat = new THREE.MeshPhysicalMaterial({
    color: 0x88ccff, transparent: true, opacity: 0.3,
    roughness: 0.0, metalness: 0.1,
    transmission: 0.9, ior: 1.5
});

// Concrete
const concreteMat = new THREE.MeshStandardMaterial({
    color: 0xaaaaaa, roughness: 0.9, metalness: 0.0
});

// Steel
const steelMat = new THREE.MeshStandardMaterial({
    color: 0x888888, roughness: 0.3, metalness: 0.8
});

// Wood
const woodMat = new THREE.MeshStandardMaterial({
    color: 0xc4955a, roughness: 0.7, metalness: 0.0
});
```

#### IFC.js / web-ifc

```javascript
import { IfcViewerAPI } from 'web-ifc-viewer';

const viewer = new IfcViewerAPI({
    container: document.getElementById('viewer-container'),
    backgroundColor: new THREE.Color(0xffffff)
});
viewer.grid.setGrid();
viewer.axes.setAxes();

const model = await viewer.IFC.loadIfcUrl('model.ifc');
viewer.shadowDropper.renderShadow(model.modelID);

// Spatial tree
const tree = await viewer.IFC.getSpatialStructure(model.modelID);

// Selection
viewer.IFC.selector.prePickIfcItem();  // highlight on hover
viewer.IFC.selector.pickIfcItem();      // select on click

// Properties
const props = await viewer.IFC.getProperties(model.modelID, expressID, true);
```

---

### 8. Cross-Platform Code Patterns

#### File I/O

```python
## CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x, y = float(row["x"]), float(row["y"])

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Area", "Volume"])
    for item in results:
        writer.writerow([item.id, item.area, item.volume])

## JSON
import json
with open("config.json", "r") as f:
    config = json.load(f)

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

## XML (for IFC, gbXML, etc.)
import xml.etree.ElementTree as ET
tree = ET.parse("energy.xml")
root = tree.getroot()
for zone in root.findall(".//Zone"):
    name = zone.get("id")
```

#### HTTP Requests

```python
import requests
## GET
response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                         params={"lat": 40.7, "lon": -74.0, "appid": key})
data = response.json()

## POST (e.g., to Speckle)
response = requests.post("https://speckle.xyz/api/streams",
                          headers={"Authorization": "Bearer " + token},
                          json={"name": "My Model"})
```

#### Geometry Libraries Comparison

| Operation | RhinoCommon | Revit API | shapely | trimesh |
|-----------|-------------|-----------|---------|---------|
| Point | Point3d | XYZ | Point | — |
| Line | LineCurve | Line | LineString | — |
| Polygon | PolylineCurve | CurveLoop | Polygon | — |
| Extrude | Extrusion.Create | — | — | trimesh.creation |
| Boolean | Brep.CreateBoolean* | BooleanOperationsUtils | .union/.difference | trimesh.boolean |
| Intersect | Intersection.* | Face.Intersect | .intersection | — |
| Area | AreaMassProperties | SpatialElement.Area | .area | mesh.area |
| Mesh | Mesh class | — | — | Trimesh class |

#### Error Handling Patterns

```python
## Python general
try:
    result = risky_operation()
except Exception as e:
    print("Error: {}".format(e))
    # Log, recover, or re-raise

## RhinoCommon-safe pattern
breps = rg.Brep.CreateBooleanUnion(inputs, 0.001)
if breps is None or len(breps) == 0:
    # Boolean failed — common with bad geometry
    print("Boolean union failed. Check input geometry.")
    breps = inputs  # fallback to originals

## Revit transaction safety
t = Transaction(doc, "Operation")
t.Start()
try:
    # operations
    t.Commit()
except Exception as e:
    if t.HasStarted() and not t.HasEnded():
        t.RollBack()
    raise
```

---

### 9. Development Environment Setup

#### VS Code for Python

**Extensions:**
- Python (Microsoft)
- Pylance (type checking)
- Rhino-Python (autocomplete stubs)
- GitLens

**Settings for Rhino Python:**
```json
{
    "python.analysis.extraPaths": [
        "C:\\Users\\<user>\\.rhinocode\\lib"
    ],
    "python.autoComplete.extraPaths": [
        "C:\\Users\\<user>\\.rhinocode\\lib"
    ]
}
```

**RhinoCommon stubs** install:
```bash
pip install Rhino-stubs
pip install Grasshopper-stubs
```

#### Visual Studio for C# GH Development

1. Install Visual Studio 2022 Community
2. Install .NET Framework 4.8 targeting pack
3. Create Class Library (.NET Framework) project
4. NuGet: `Install-Package Grasshopper`
5. Set post-build event: `copy "$(TargetPath)" "%APPDATA%\Grasshopper\Libraries\"`
6. Debug: attach to `Rhino.exe` process, set breakpoints

#### Git for AEC Scripts

```bash
## .gitignore for AEC projects
*.3dm
*.rvt
*.rfa
*.dwg
*.ghx        # large GH files (keep .gh or .ghx, not both)
__pycache__/
*.pyc
.vs/
bin/
obj/
```

#### Package Managers

```bash
## Python (pip)
pip install compas compas_rhino compas_ghpython
pip install shapely trimesh open3d numpy scipy pandas

## C# (NuGet)
Install-Package Grasshopper
Install-Package MathNet.Numerics
Install-Package Newtonsoft.Json

## JavaScript (npm)
npm install three @types/three
npm install web-ifc web-ifc-three web-ifc-viewer
npm install @speckle/viewer
```

#### Debugging Strategies

| Platform | Strategy |
|----------|----------|
| Rhino Python | `print()` to command line; `rs.MessageBox()` for breakpoints |
| GhPython | `print()` to GH panel; connect Panel component to output |
| C# GH Script | `Print()` and `Reflect.Component` for messages |
| C# Plugin | Attach Visual Studio debugger to Rhino.exe |
| pyRevit | `output.print_md()` for formatted output; `forms.alert()` |
| Dynamo | Watch nodes; Python `print()` to console |
| Three.js | Browser DevTools; `console.log()`; Scene inspector extensions |

#### RhinoCommon API Documentation

- Official: https://developer.rhino3d.com/api/rhinocommon/
- Samples: https://github.com/mcneel/rhino-developer-samples
- Discourse: https://discourse.mcneel.com/c/scripting

#### Revit API Documentation

- RevitAPIDocs: https://www.revitapidocs.com/
- Official SDK samples (installed with Revit SDK)
- The Building Coder blog: https://thebuildingcoder.typepad.com/

#### Three.js Documentation

- Official: https://threejs.org/docs/
- Examples: https://threejs.org/examples/
- IFC.js: https://ifcjs.github.io/info/

---

*This skill provides the scripting foundation for all AEC computational design work. Each referenced API has its own detailed reference document in the `references/` subdirectory for deep-dive usage.*


---

# Optimization & intelligence


## optimization-methods

### Optimization Methods

> Genetic algorithms, simulated annealing, particle swarm optimization, gradient-based methods, topology optimization, shape optimization, size optimization, and benchmark problems for AEC computational design

## Optimization Methods for AEC Computational Design

### 1. Optimization in AEC Design

#### The Role of Optimization

Optimization is the systematic process of finding the best solution from a set of feasible alternatives according to one or more criteria. In the Architecture, Engineering, and Construction (AEC) industry, optimization transforms design from an intuition-driven craft into a rigorous, evidence-based discipline that can explore thousands of alternatives in the time a human designer evaluates a handful.

Every AEC project embeds optimization problems whether practitioners recognize them or not. Selecting a column grid that minimizes steel tonnage, arranging rooms to maximize adjacency satisfaction, routing ductwork to minimize pressure loss, or shaping a facade to balance daylight and solar heat gain -- all are optimization problems with design variables, objectives, and constraints.

#### Design Optimization vs. Mathematical Optimization

Mathematical optimization seeks a global or local extremum of a function subject to constraints, governed by theorems about convexity, differentiability, and feasibility. Design optimization in AEC adds layers of complexity:

- **Multiple stakeholders** with conflicting objectives (cost vs. aesthetics vs. performance)
- **Mixed variable types**: continuous (member thickness), discrete (bolt count), categorical (material grade), topological (connectivity)
- **Expensive evaluations**: a single FEA run may take minutes; a CFD simulation hours; an energy model tens of minutes
- **Ill-defined objectives**: "architectural quality" resists quantification
- **Regulatory constraints**: building codes, zoning ordinances, fire safety -- hard constraints that cannot be relaxed
- **Manufacturing constraints**: available section catalogs, sheet sizes, fabrication tolerances
- **Uncertainty**: loads are probabilistic, material properties vary, construction tolerances exist

#### Problem Classification

| Classification Axis | Categories | AEC Examples |
|---|---|---|
| Variable type | Continuous, discrete, integer, mixed, combinatorial | Member sizing (continuous), bolt count (integer), material choice (categorical) |
| Objective count | Single-objective, multi-objective, many-objective (>3) | Weight minimization (single), weight vs. cost vs. carbon (many) |
| Constraint type | Unconstrained, equality-constrained, inequality-constrained, bound-constrained | Stress <= allowable, drift <= H/400, area = target |
| Landscape | Convex, non-convex, multi-modal, discontinuous, noisy | Topology optimization (non-convex), layout optimization (multi-modal) |
| Evaluation cost | Cheap (analytical), moderate (FEA), expensive (CFD), very expensive (coupled multi-physics) | Truss weight (cheap), building energy (expensive) |
| Determinism | Deterministic, stochastic, robust, reliability-based | Deterministic sizing, reliability-based design under seismic uncertainty |

#### NP-Hardness of Real Design Problems

Many AEC optimization problems are NP-hard or NP-complete:

- **Floor plan layout** with adjacency and area constraints maps to graph partitioning and bin packing -- both NP-hard
- **Discrete structural topology** (deciding which members exist in a ground structure) is combinatorial with 2^n candidates for n potential members
- **Construction scheduling** with resource constraints is equivalent to job-shop scheduling (NP-hard)
- **Panelization of freeform surfaces** with planarity constraints is NP-hard in the general case
- **Steel connection design** with catalog-based bolt/plate selection is combinatorial

This NP-hardness means exact solutions are intractable for realistic problem sizes. Metaheuristics provide high-quality solutions in practical time, though without guarantees of global optimality.

#### When to Optimize vs. When to Use Engineering Judgment

Optimization is not always the answer. Use engineering judgment when:

- The design space is small enough to enumerate (< 50 alternatives)
- Code-prescriptive requirements dictate a single solution
- The objective is poorly defined or rapidly changing
- Computational cost of evaluation exceeds project budget
- The problem is so constrained that only one feasible solution exists

Use formal optimization when:

- The design space is large (hundreds to millions of alternatives)
- Multiple competing objectives require trade-off analysis
- Small improvements yield significant cost or performance savings
- The problem will recur across projects (amortize setup cost)
- Regulatory compliance must be demonstrated rigorously
- You need to prove to a client that the design is near-optimal

---

### 2. Algorithm Classification

#### Complete Taxonomy

##### Gradient-Based Methods

Gradient-based methods use derivative information (first-order: gradient; second-order: Hessian) to navigate the objective landscape. They are the workhorse of smooth, continuous optimization.

**Steepest Descent (Gradient Descent)**
- Update: x_{k+1} = x_k - alpha_k * grad(f(x_k))
- Step size alpha_k found via line search (Armijo, Wolfe conditions)
- Linear convergence rate; slow near optima due to zigzagging
- Use case: simple, low-dimensional smooth problems; often a starting point for teaching

**Conjugate Gradient (CG)**
- Constructs conjugate search directions that avoid zigzagging
- Fletcher-Reeves, Polak-Ribiere, Hestenes-Stiefel variants
- Superlinear convergence for quadratic objectives; resets every n steps
- Use case: large-scale unconstrained problems where Hessian storage is prohibitive

**Newton's Method**
- Update: x_{k+1} = x_k - H(x_k)^{-1} * grad(f(x_k))
- Quadratic convergence near the optimum
- Requires Hessian computation and inversion -- O(n^3) per step
- Use case: small-to-medium problems with available second derivatives

**Quasi-Newton Methods (BFGS, L-BFGS)**
- Approximate the Hessian (or its inverse) using gradient information
- BFGS: stores dense n x n matrix; superlinear convergence
- L-BFGS: stores only m gradient pairs (m ~ 5-20); suitable for n > 10,000
- Use case: medium to large smooth unconstrained or bound-constrained problems; the default recommendation for smooth problems in scipy

**Sequential Quadratic Programming (SQP)**
- Solves a sequence of quadratic subproblems approximating the original NLP
- Handles equality and inequality constraints via active-set or interior-point strategies
- Superlinear convergence under regularity conditions
- Use case: smooth constrained optimization; structural sizing with stress/displacement constraints

##### Gradient-Free / Direct Search Methods

When gradients are unavailable, unreliable, or expensive to compute (numerical differentiation in noisy simulations), direct search methods explore the landscape using only function values.

**Nelder-Mead Simplex**
- Maintains a simplex of n+1 points in n dimensions
- Operations: reflection, expansion, contraction, shrink
- No convergence guarantee for n > 1; can stall on non-smooth landscapes
- Use case: low-dimensional (n < 10), quick prototyping, noisy functions

**Pattern Search (Generalized Pattern Search, GPS)**
- Explores along coordinate directions with adaptive step size
- Convergence guaranteed to first-order stationary point under mild conditions
- Use case: bound-constrained, non-smooth, moderate dimension

**Powell's Method**
- Successive line minimizations along conjugate directions
- No gradient required; builds up conjugate direction set
- Use case: smooth or mildly non-smooth, moderate dimension

##### Metaheuristic / Stochastic Methods

Metaheuristics are high-level strategies that guide subordinate heuristics to explore the search space. They make few or no assumptions about the problem and can handle discontinuities, discrete variables, and multi-modality.

**Genetic Algorithm (GA)** -- Inspired by natural selection. Population-based. Excellent for mixed-variable, multi-modal problems. See Section 3 for full detail.

**Simulated Annealing (SA)** -- Inspired by metallurgical annealing. Single-solution trajectory. Good at escaping local optima via probabilistic acceptance. See Section 4.

**Particle Swarm Optimization (PSO)** -- Inspired by flocking behavior. Population-based. Fast convergence in continuous spaces. See Section 5.

**Differential Evolution (DE)** -- Population-based; uses vector differences for mutation. Robust, few parameters. See Section 6.

**CMA-ES** -- Covariance Matrix Adaptation Evolution Strategy. Self-adapting step size and search distribution. State-of-the-art for continuous black-box optimization. See Section 6.

##### Surrogate-Based Methods

When a single function evaluation costs minutes to hours (FEA, CFD, energy simulation), surrogate-based optimization builds a cheap approximation model and optimizes that model instead.

**Bayesian Optimization (Gaussian Process)**
- Fits a Gaussian Process (GP) to evaluated points
- Uses acquisition function (Expected Improvement, Probability of Improvement, Upper Confidence Bound) to select next evaluation point
- Excels in low-dimensional (n < 20), very expensive problems
- Use case: optimizing building energy performance, CFD-driven facade design

**RBF-Based (Radial Basis Functions)**
- Interpolates with radial basis functions (multiquadric, thin-plate spline)
- Can handle higher dimensions than GP
- Use case: moderate-dimension expensive problems, used by Opossum in Grasshopper

**Polynomial Response Surface (RSM)**
- Fits low-order polynomial (linear, quadratic) to DOE samples
- Fast to evaluate; limited accuracy for highly nonlinear functions
- Use case: initial screening, sensitivity analysis

##### Topology Optimization Methods

Topology optimization determines the optimal material distribution within a design domain. It is fundamentally different from sizing/shape optimization because it can create and remove holes, change connectivity, and produce novel structural forms.

**SIMP (Solid Isotropic Material with Penalization)**
- Assigns a continuous density variable rho_e in [0, 1] to each element
- Penalizes intermediate densities: E_e = rho_e^p * E_0 (p typically 3)
- Solved via gradient-based optimizer (MMA, OC) using adjoint sensitivity
- Use case: 2D/3D structural topology, compliance minimization, stress-constrained

**BESO (Bi-directional Evolutionary Structural Optimization)**
- Binary (0/1) element densities; adds and removes elements iteratively
- Uses sensitivity numbers to rank elements
- Produces cleaner 0/1 designs than SIMP
- Use case: structural topology with clear member definitions

**Level-Set Method**
- Represents structural boundary as zero level set of a higher-dimensional function
- Boundary evolves via Hamilton-Jacobi equation driven by shape sensitivities
- Produces smooth boundaries; handles topological changes naturally
- Use case: problems requiring smooth boundaries, multi-physics topology optimization

#### Comparison Table

| Criterion | Gradient-Based | Direct Search | GA | SA | PSO | DE | CMA-ES | Bayesian Opt | SIMP |
|---|---|---|---|---|---|---|---|---|---|
| Convergence speed | Fast (superlinear) | Slow (linear) | Moderate | Slow | Fast | Moderate | Fast | Very fast (per eval) | Moderate |
| Global vs. local | Local | Local | Global | Global | Global (tendency) | Global | Global (local bias) | Global | Local |
| Handles discrete | No | No | Yes | Yes | With modification | Yes | No | Yes | No |
| Handles constraints | SQP, IP methods | Penalty | Penalty, repair | Penalty | Penalty | Penalty | Penalty | Constrained EI | Adjoint |
| Parallelizable | Limited | Limited | Excellent | Limited | Excellent | Excellent | Moderate | Batch | Limited |
| Parameter sensitivity | Low (step size) | Low | High (pop, pc, pm) | Moderate (T schedule) | Moderate (w, c1, c2) | Low (F, CR) | Very low | Moderate | Low (p, filter) |
| Evaluations needed | O(n) | O(n^2) | O(1000-100000) | O(1000-100000) | O(1000-50000) | O(1000-50000) | O(100-10000) | O(10-200) | O(100-500 iter) |

---

### 3. Genetic Algorithms (Detailed)

#### Encoding Schemes

The encoding (genotype representation) fundamentally determines the algorithm's performance.

**Binary encoding**: Each variable mapped to a binary string of length l, providing 2^l resolution levels. Classical but introduces Hamming cliffs where adjacent real values have very different binary representations.

**Real-valued (floating-point) encoding**: Design variables stored directly as floating-point numbers. Eliminates encoding/decoding overhead. Preferred for continuous AEC problems (member dimensions, node coordinates).

**Integer encoding**: For discrete variables like number of stories, bolt count, reinforcement bar count. Can use binary encoding or direct integer representation.

**Permutation encoding**: For sequencing problems (construction scheduling, facility layout). Each gene is a unique index; standard crossover would create invalid solutions, so specialized operators (PMX, OX, CX) are required.

**Mixed encoding**: AEC problems often combine continuous, integer, and categorical variables. The chromosome concatenates segments with different types, and operators respect type boundaries. Example: [beam_depth (real), num_bolts (int), steel_grade (categorical), brace_config (binary)].

#### Selection Operators

**Tournament selection (k)**: Randomly pick k individuals; select the fittest. k=2 is standard; k=3 increases selection pressure. Simple, parallelizable, no fitness scaling needed. Recommended as default.

**Roulette wheel (fitness-proportionate)**: Probability of selection proportional to fitness. Suffers from premature convergence when one individual dominates, and stagnation when fitness values are close.

**Stochastic Universal Sampling (SUS)**: Single spin of a wheel with n equally-spaced pointers. Reduces stochastic noise of roulette. Better diversity preservation.

**Rank-based selection**: Individuals ranked by fitness; selection probability based on rank, not raw fitness. Prevents super-individual domination. Linear or exponential ranking.

**Truncation selection**: Select top fraction tau (e.g., top 50%) of population. Deterministic. High selection pressure. Used in CMA-ES and some engineering GAs.

#### Crossover Operators

**Simulated Binary Crossover (SBX)**: For real-valued variables. Mimics single-point crossover in binary space. Distribution index eta_c controls spread: low eta_c (2-5) = exploratory; high eta_c (10-20) = exploitative. The standard for real-coded GAs. Offspring created with polynomial probability distribution centered on parents.

**BLX-alpha (Blend Crossover)**: Offspring uniformly sampled from [min(p1,p2) - alpha*range, max(p1,p2) + alpha*range]. alpha=0.5 is standard. Simple and effective.

**Uniform crossover**: Each gene independently taken from either parent with probability 0.5. Good for problems with low epistasis (gene independence).

**PMX (Partially Mapped Crossover)**: For permutation encoding. Selects a segment from parent 1, copies to offspring, maps remaining genes from parent 2 using the mapping relationship. Preserves absolute positions.

**OX (Order Crossover)**: For permutation encoding. Preserves relative order from parent 2 while inheriting a segment from parent 1. Better for problems where order matters more than position.

#### Mutation Operators

**Polynomial mutation**: For real-valued variables. Perturbation drawn from a polynomial distribution. Distribution index eta_m controls perturbation magnitude: low eta_m (5-10) = large perturbations; high eta_m (20-100) = small perturbations. The standard companion to SBX.

**Gaussian mutation**: Add N(0, sigma) noise to each gene. sigma can be fixed or adaptive (self-adaptive mutation). Intuitive but requires careful sigma tuning.

**Swap mutation**: For permutation encoding. Randomly swap two positions.

**Insert mutation**: For permutation encoding. Remove an element and insert it at a random position.

**Bit-flip mutation**: For binary encoding. Flip each bit with probability p_m (typically 1/L where L is chromosome length).

#### Constraint Handling

**Penalty methods**: Add a penalty term to the objective for constraint violation. Static penalty (fixed multiplier), dynamic penalty (increasing with generation), adaptive penalty (based on population feasibility ratio). Simple but penalty coefficient tuning is notoriously difficult.

**Repair operators**: Map infeasible solutions to the nearest feasible point. Problem-specific. Effective when a repair heuristic is available (e.g., scaling member sizes to satisfy stress).

**Feasibility rules (Deb's rules)**: (1) Feasible solution always beats infeasible. (2) Among two feasible solutions, better objective wins. (3) Among two infeasible solutions, lower total constraint violation wins. Parameter-free. Highly recommended for engineering problems.

**Epsilon-constraint**: Gradually tighten the feasibility tolerance epsilon from relaxed to zero over generations. Allows exploration of infeasible regions early, converges to feasible region.

#### Advanced GA Variants

**Island model GA**: Multiple subpopulations evolve independently on separate "islands" with periodic migration of best individuals. Excellent for parallelization (one island per CPU core). Migration rate (fraction migrating) and migration interval (generations between migrations) are key parameters.

**Adaptive operator selection (AOS)**: Track the success rate of each crossover/mutation operator and adapt selection probabilities. Credit assignment: immediate reward (fitness improvement) or extreme reward (best improvement over window). Selection: probability matching, adaptive pursuit, multi-armed bandit (UCB1).

---

### 4. Simulated Annealing

#### Physical Analogy

In metallurgy, annealing involves heating a metal to high temperature (atoms move freely, exploring many configurations) and slowly cooling it (atoms settle into a low-energy crystalline lattice). If cooled too quickly, the metal develops defects (local minimum). SA mimics this: at high temperature, worse solutions are frequently accepted (exploration); as temperature decreases, acceptance becomes increasingly selective (exploitation).

#### The Algorithm

```
Initialize solution x, temperature T = T_0
While not converged:
    Generate neighbor x' from N(x)
    Compute delta = f(x') - f(x)
    If delta < 0 (improvement): accept x'
    Else: accept x' with probability exp(-delta / T)
    Update temperature: T = cool(T)
```

#### Temperature Schedules

**Geometric (exponential) cooling**: T_{k+1} = alpha * T_k, where alpha in [0.9, 0.999]. Most common. alpha = 0.95 is a good starting point. Simple and predictable.

**Linear cooling**: T_k = T_0 - k * (T_0 - T_min) / K_max. Reaches T_min in exactly K_max steps. Less flexible than geometric.

**Adaptive cooling**: Adjusts cooling rate based on acceptance ratio. If acceptance is high (>0.5), cool faster; if low (<0.1), cool slower or reheat. Lam's schedule is a well-known adaptive scheme targeting ~44% acceptance.

**Logarithmic cooling**: T_k = T_0 / log(1 + k). Guarantees convergence to global optimum in theory, but impractically slow.

#### Initial Temperature Selection

- Run a preliminary sampling: evaluate 100-1000 random neighbors, compute average worsening delta_avg
- Set T_0 such that exp(-delta_avg / T_0) = p_0 (desired initial acceptance probability, typically 0.8-0.95)
- T_0 = -delta_avg / ln(p_0)

#### Acceptance Probability: Metropolis Criterion

P(accept) = exp(-delta / T) for delta > 0 (worsening moves). This is the Boltzmann distribution from statistical mechanics. Key properties:
- As T approaches infinity, P approaches 1 (accept everything)
- As T approaches 0, P approaches 0 (accept only improvements)
- Larger delta (bigger worsening) = lower acceptance probability at any T

#### Neighbor Generation

The neighborhood structure N(x) is problem-specific and critically important:
- **Continuous**: Perturb each variable by Gaussian noise scaled by T (larger moves at high T)
- **Discrete**: Swap two elements, flip a bit, change one variable value
- **Structural**: Add/remove a member, change a connection type
- **Layout**: Move a room, swap two rooms, resize a zone

#### Reheating Strategies

When SA stalls in a local minimum at low temperature, reheating can restart exploration:
- **Periodic reheating**: Every N iterations, reset T to a fraction (e.g., 0.5) of T_0
- **Stagnation-based**: If no improvement for M iterations, reheat
- **Non-monotonic SA**: Allow temperature to oscillate

#### Multi-Start SA

Run SA multiple times from different random starting solutions. Return the best solution found across all runs. Simple parallelization strategy. Each run is independent. Effective when single-run SA has moderate probability of finding the global basin.

#### SA vs. GA for AEC Problems

| Aspect | SA | GA |
|---|---|---|
| Population | Single solution | Population of solutions |
| Parallelization | Multi-start only | Naturally parallel |
| Discrete variables | Excellent | Excellent |
| Continuous variables | Good (with good neighbor) | Excellent (with SBX) |
| Tuning difficulty | Moderate (T_0, alpha) | High (pop, pc, pm, selection) |
| Multi-objective | Awkward (weighted sum) | Natural (NSGA-II) |
| Memory | O(1) | O(pop * n) |
| Solution diversity | Low (single trajectory) | High (population) |

---

### 5. Particle Swarm Optimization

#### Standard PSO Equations

Each particle i has position x_i and velocity v_i in the design space.

```
v_i(t+1) = w * v_i(t) + c1 * r1 * (pbest_i - x_i(t)) + c2 * r2 * (gbest - x_i(t))
x_i(t+1) = x_i(t) + v_i(t+1)
```

Where:
- w = inertia weight (controls momentum / exploration-exploitation balance)
- c1 = cognitive coefficient (attraction to personal best)
- c2 = social coefficient (attraction to global best)
- r1, r2 = uniform random numbers in [0, 1], generated independently per dimension
- pbest_i = best position found by particle i historically
- gbest = best position found by any particle in the swarm

#### Inertia Weight Strategies

**Constant w**: w = 0.729 (Clerc's constriction coefficient) with c1 = c2 = 1.49445. Theoretically derived for convergence.

**Linearly decreasing w**: w decreases from w_max (0.9) to w_min (0.4) over the run. Early exploration, late exploitation. Most common strategy.

**Adaptive w**: Adjust w based on swarm diversity or improvement rate. High diversity -> lower w (exploit); low diversity -> higher w (explore).

**Random w**: w ~ U(0.5, 1.0) each iteration. Adds stochasticity. Surprisingly competitive.

#### Cognitive and Social Parameters

- c1 = c2 = 2.0 is the classical setting (but can cause divergence without constriction)
- c1 = c2 = 1.49445 with w = 0.729 (Clerc-Kennedy constriction) is theoretically sound
- c1 > c2: more self-reliant particles, better exploration, slower convergence
- c1 < c2: more social particles, faster convergence, risk of premature convergence
- c1 + c2 should typically be around 4.0

#### Topology (Communication Structure)

**Global best (gbest)**: Every particle knows the best position of the entire swarm. Fast convergence but prone to premature convergence in multi-modal landscapes.

**Local best (lbest)**: Each particle communicates with k nearest neighbors (in index space, not position). Slower convergence but better global search. Ring topology (k=2) is the most common lbest variant.

**Von Neumann**: Particles arranged on a 2D grid; communicate with 4 neighbors (up, down, left, right). Good balance between gbest and lbest.

**Dynamic topology**: Start with lbest (exploration), gradually increase neighborhood size toward gbest (exploitation).

#### Boundary Handling

When a particle leaves the search domain [lb, ub]:

**Absorbing**: Clamp position to boundary, set velocity to zero. Simple but particles can cluster at boundaries.

**Reflecting**: Reflect position off boundary and reverse velocity component. Preserves kinetic energy.

**Damping**: Reflect position but reduce velocity by a random factor. Prevents bouncing.

**Periodic/wrapping**: Position wraps around (useful for angular variables).

#### Discrete PSO

Standard PSO operates in continuous space. For discrete AEC problems:

**Binary PSO (Kennedy-Eberhart)**: Velocity interpreted as probability of bit being 1 via sigmoid function: P(x_id = 1) = sigmoid(v_id). Used for topology optimization (member exists or not).

**Discrete PSO by rounding**: Compute continuous position, round to nearest integer. Simple but may miss good discrete solutions.

**Set-based PSO**: Redefine operators for set-valued variables. Velocity becomes a set of swaps or changes.

#### Multi-Objective PSO (MOPSO)

Extends PSO to handle multiple objectives simultaneously:
- Maintain an external archive of non-dominated solutions
- Global best selection from archive (e.g., crowding distance-based selection for diversity)
- Leader selection strategies: roulette on crowding, random from archive, grid-based
- Archive maintenance: bounded size with crowding/epsilon-dominance pruning

---

### 6. Other Metaheuristics

#### Differential Evolution (DE)

DE is a population-based optimizer that uses vector differences for mutation. It is remarkably simple and effective.

**DE/rand/1**: Mutant vector v = x_r1 + F * (x_r2 - x_r3), where r1, r2, r3 are distinct random indices and F in [0.4, 1.0] is the scale factor.

**DE/best/1**: v = x_best + F * (x_r1 - x_r2). Exploitative; converges faster but may premature.

**DE/current-to-best/1**: v = x_i + F * (x_best - x_i) + F * (x_r1 - x_r2). Balance of exploration and exploitation.

**Crossover (binomial)**: Trial vector u_ij = v_ij if rand < CR else x_ij. CR in [0.0, 1.0] controls how many dimensions come from mutant. At least one dimension always comes from mutant.

**Parameter guidelines**: F = 0.5-0.8, CR = 0.9 for separable problems, CR = 0.1-0.3 for non-separable. Population size = 5-10 times dimension. Self-adaptive variants (jDE, SHADE, L-SHADE) eliminate manual tuning.

#### CMA-ES (Covariance Matrix Adaptation Evolution Strategy)

CMA-ES is considered the state-of-the-art for continuous, black-box, non-convex optimization up to moderate dimension (n < 200).

- Samples offspring from a multivariate normal distribution N(m, sigma^2 * C)
- Adapts mean m (toward better solutions), step size sigma (cumulative step-size adaptation, CSA), and covariance matrix C (learns variable scaling and correlations)
- Nearly parameter-free: only population size lambda needs setting (default: 4 + floor(3 * ln(n)))
- Invariant to order-preserving transformations of the objective
- Handles ill-conditioning (condition numbers up to 10^10) naturally

**When CMA-ES excels**: Continuous, moderate dimension (n < 100-200), no gradient available, function evaluations not excessively expensive (can afford O(100n^2) evaluations), non-separable landscape.

#### Bayesian Optimization

**Gaussian Process (GP) surrogate**: Models objective as a GP, providing mean prediction and uncertainty estimate at any untested point.

**Acquisition functions**:
- **Expected Improvement (EI)**: Balances exploitation (high mean) and exploration (high uncertainty). EI = E[max(f_best - f(x), 0)]. The most commonly used.
- **Probability of Improvement (PI)**: P(f(x) < f_best - xi). Pure exploitation with exploration parameter xi.
- **Upper Confidence Bound (UCB)**: mu(x) - kappa * sigma(x) (for minimization). kappa controls exploration-exploitation.

**When to use**: Very expensive function evaluations (minutes to hours each). Low dimension (n < 15-20). Budget of 50-200 evaluations. Building energy optimization, CFD-driven shape optimization.

#### Harmony Search

Inspired by musical improvisation. Musicians (variables) play notes (values) to create harmonies (solutions). Harmony Memory Considering Rate (HMCR) and Pitch Adjusting Rate (PAR) control exploration. Easy to implement but theoretically equivalent to a simple evolutionary strategy. Limited advantages over DE or CMA-ES in practice.

#### Firefly Algorithm

Based on flashing behavior of fireflies. Attractiveness decreases with distance (controlled by light absorption coefficient gamma). Can be effective for multi-modal problems due to automatic subpopulation formation around multiple optima. However, performance is highly parameter-dependent.

---

### 7. Structural Optimization Types

#### Size Optimization

**Variables**: Cross-section dimensions (beam depth, flange width, web thickness), member area, plate thickness, reinforcement ratio, prestress force.

**Typical constraints**: Stress limits (allowable stress for each member), deflection limits (span/360, span/240), vibration frequency (f > f_min), stability (buckling), code-specific checks (interaction equations for steel, capacity ratios).

**Characteristics**: Design variables are typically continuous or selected from discrete catalogs (AISC W-shapes, HSS sections). The search space is moderate. Gradient-based methods work well for continuous sizing; GA or enumeration for catalog selection.

**Example**: Minimize weight of a steel frame by selecting W-shape sections for each member group, subject to AISC 360 strength checks, story drift < H/400, and first modal frequency > 1.0 Hz.

#### Shape Optimization

**Variables**: Boundary node coordinates, control point positions (B-spline, NURBS), arch rise, shell curvature parameters, truss node locations.

**Typical constraints**: Stress, displacement, frequency, geometric constraints (minimum clearance, maximum height), manufacturing constraints (minimum radius of curvature, developability).

**Characteristics**: Mesh quality can degrade as shape changes -- requires remeshing or parameterization that maintains mesh quality. Sensitivity analysis uses shape derivatives (material derivative approach). Gradient-based methods are efficient but require careful shape parameterization.

**Example**: Optimize the height profile of a truss bridge by moving interior node positions vertically, minimizing weight subject to stress and deflection constraints.

#### Topology Optimization

**Variables**: Element densities (SIMP), element existence (BESO), level-set function values, ground structure member existence.

**Typical constraints**: Volume fraction (limit total material), stress (local or global), displacement, frequency, manufacturing (minimum member size, connectivity, symmetry, overhang angle for additive manufacturing).

**Characteristics**: Highest design freedom but most complex. Produces organic, often non-intuitive forms. Post-processing required to extract clean geometry from density fields. Checkerboard filtering, minimum length scale control, and projection methods ensure manufacturability.

**Example**: Given a 2D design domain with specified loads and supports, find the optimal material distribution using at most 30% of the domain volume, minimizing compliance (maximizing stiffness).

#### Multi-Scale Optimization

**Concept**: Simultaneously optimize the macro structure (overall form and topology) and micro structure (unit cell / lattice architecture) at different scales.

**Variables**: Macro-level density/topology + micro-level unit cell parameters (strut thickness, cell type, orientation).

**Application**: Lattice-filled structures for additive manufacturing, functionally graded materials, metamaterial design for vibration isolation.

#### Comparison Table

| Aspect | Size | Shape | Topology | Multi-Scale |
|---|---|---|---|---|
| Design freedom | Low | Medium | High | Very high |
| Variable count | 10-100 | 10-1000 | 1000-1000000 | 10000+ |
| Preferred algorithm | SQP, catalog search | SQP, GA | SIMP+MMA, BESO, Level-set | Homogenization + SIMP |
| Computational cost | Low | Medium | High | Very high |
| Post-processing | Minimal | Moderate | Significant | Significant |
| Typical AEC use | Member sizing | Shell/roof form-finding | Structural nodes, brackets | Research, AM parts |

---

### 8. AEC Optimization Problem Formulation

#### Problem 1: Minimize Structural Weight (Truss)

**Design variables**: Cross-sectional area A_i for each member group i = 1..n (continuous or from catalog)
**Objective**: Minimize sum(rho * A_i * L_i) for all members
**Constraints**: sigma_i <= sigma_allow for all members (stress), delta_j <= delta_allow for critical nodes (deflection), A_min <= A_i <= A_max (bounds), buckling: P_cr_i >= N_i for compression members
**Suggested algorithm**: SQP (continuous), GA with catalog encoding (discrete), DE (continuous)

#### Problem 2: Maximize Daylight with Energy Constraint

**Design variables**: Window-to-wall ratio (WWR) per facade orientation, shading device depth, glazing U-value, glazing SHGC
**Objective**: Maximize spatial Daylight Autonomy (sDA_300/50)
**Constraints**: Annual energy use intensity (EUI) <= target (kWh/m2/yr), glare: ASE_1000/250 <= 10% of floor area, WWR in [0.2, 0.8], U-value and SHGC from available glazing catalog
**Suggested algorithm**: Bayesian Optimization (expensive energy simulation), GA if simplified daylighting model used

#### Problem 3: Minimize Facade Cost with Planarity

**Design variables**: Control point positions of freeform facade surface (NURBS), panel edge lengths
**Objective**: Minimize total facade cost = sum(panel_cost_i) where cost depends on planarity deviation, size, and curvature
**Constraints**: max planarity deviation per panel <= tolerance (e.g., 2mm), panel size within fabrication limits, visual smoothness (curvature continuity), structural glass stress limits
**Suggested algorithm**: L-BFGS (smooth surface parameterization), SQP with planarity as constraint, CMA-ES for non-smooth cost models

#### Problem 4: Floor Plan Layout Optimization

**Design variables**: Room positions (x_i, y_i), room dimensions (w_i, h_i), room orientation/rotation
**Objective**: Maximize adjacency satisfaction score = sum(w_ij * adj(i,j)) where w_ij is desired adjacency weight and adj(i,j) measures actual adjacency quality
**Constraints**: No room overlaps, all rooms within building footprint, minimum room dimensions per program, corridor access for all rooms, fire egress requirements
**Suggested algorithm**: GA with penalty-based constraint handling (highly combinatorial, discrete topology), SA with swap/move neighborhood

#### Problem 5: Material Waste Minimization (Nesting/Cutting)

**Design variables**: Position (x_i, y_i) and rotation (theta_i) of each piece on stock sheet
**Objective**: Minimize number of stock sheets used (or total waste area)
**Constraints**: No overlap between pieces, pieces within sheet boundary, grain direction (if applicable), minimum kerf width between pieces
**Suggested algorithm**: GA with permutation + placement heuristic (bottom-left, no-fit polygon), SA with piece swap/rotation moves

#### Problem 6: Multi-Objective -- Weight vs. Embodied Carbon vs. Cost

**Design variables**: Member sizes (from catalog), material choices (S235, S355, S460 steel; C30, C40, C50 concrete)
**Objectives (all minimize)**: f1 = total structural weight, f2 = total embodied carbon (kgCO2e), f3 = total material + fabrication cost
**Constraints**: All strength and serviceability checks per code, minimum fire rating, constructability (maximum member weight for crane capacity)
**Suggested algorithm**: NSGA-II (well-established multi-objective), NSGA-III for 3 objectives, MOEA/D

#### Problem 7: Parking Layout Optimization

**Design variables**: Aisle orientation angle, aisle width, stall dimensions, one-way vs. two-way traffic, ramp location
**Objective**: Maximize number of parking stalls per floor area
**Constraints**: Minimum stall dimensions per code (e.g., 2.5m x 5.0m), aisle width for vehicle turning radius, fire lane access, accessible parking count, structural column grid avoidance
**Suggested algorithm**: GA with mixed encoding (angle=continuous, layout type=categorical), parametric sweep for low-dimensional variant

#### Problem 8: HVAC Duct Routing Optimization

**Design variables**: Duct path (waypoints in 3D), duct cross-section dimensions, branch points
**Objective**: Minimize total pressure drop + material cost + installation cost
**Constraints**: Minimum velocity (to prevent settling), maximum velocity (to control noise), clearance from structure and other systems, maximum duct aspect ratio (4:1), access for maintenance, fire damper locations
**Suggested algorithm**: A* or Dijkstra on discretized grid (routing), GA for continuous path optimization, PSO for cross-section sizing

#### Problem 9: Structural Damper Placement

**Design variables**: Location (floor/bay) and capacity of viscous dampers (discrete: install or not; continuous: damping coefficient)
**Objective**: Minimize total damper cost (number * unit cost dependent on capacity)
**Constraints**: Maximum inter-story drift ratio <= 0.02 under design earthquake, maximum floor acceleration <= threshold for occupant comfort, existing structural system unchanged
**Suggested algorithm**: GA with binary encoding (placement) + continuous (capacity), SA

#### Problem 10: Solar Panel Array Layout on Roof

**Design variables**: Panel tilt angle, azimuth, row spacing, number of rows, panel type selection
**Objective**: Maximize annual energy production (kWh) or minimize levelized cost of energy (LCOE)
**Constraints**: Roof area boundary, structural load capacity, wind uplift, self-shading limits, setback from roof edges, electrical string sizing, inverter capacity
**Suggested algorithm**: DE (continuous variables, moderate dimension), PSO, Bayesian optimization if using detailed simulation

---

### 9. Implementation in AEC Tools

#### Galapagos (Grasshopper)

Galapagos is the built-in evolutionary solver in Grasshopper. It provides two solver modes:

**Evolutionary Solver (GA)**:
- Connect Number Slider components to the Genome input (these are design variables)
- Connect a single fitness value to the Fitness input (objective to maximize or minimize)
- Settings: Population size (default 50, recommend 50-200), maintain percentage (elitism, default 5%), inbreeding factor (0 = full crossover, 1 = cloning)
- Convergence: stops after N generations without improvement

**Simulated Annealing Solver**:
- Same input/output wiring as GA
- Settings: initial temperature, cooling factor, neighborhood radius
- Better for low-dimensional problems (< 10 variables)

**Limitations**: Single-objective only. No constraint handling (must embed as penalty). No Pareto front. Black-box operators (no control over crossover/mutation type). Limited to Grasshopper number sliders as variables.

#### Wallacei (Grasshopper)

Wallacei implements NSGA-II for multi-objective optimization in Grasshopper.

**Setup**: Connect gene pools (design variables with specified ranges and step sizes) to the Wallacei component. Connect multiple fitness objectives. Configure population size and generation count.

**Result interpretation**: Wallacei provides extensive analytics:
- Pareto front visualization (2D and 3D objective space)
- Standard deviation of each objective across Pareto front
- Fitness value distribution per generation
- Phenotype (design) preview for any solution on the Pareto front
- Selection of preferred solution via parallel coordinates or direct Pareto front click
- Export of selected solutions back to Grasshopper for further development

**Strengths**: Multi-objective, excellent visualization, NSGA-II is well-proven, gene pool provides integer/continuous variables.

#### Octopus (Grasshopper)

Multi-objective optimizer using SPEA-2 and HypE algorithms. Distinctive features:
- Hypervolume-based selection (HypE) for many-objective problems
- Interactive Pareto front exploration during optimization
- Elitist archive with diversity maintenance
- Supports 2+ objectives

#### Opossum (Grasshopper)

Surrogate-based optimizer using RBFOpt (Radial Basis Function Optimization):
- Builds surrogate model from evaluated samples
- Ideal for expensive simulations (energy, CFD, acoustics)
- Requires far fewer evaluations than GA/PSO (often 50-200 total)
- Single-objective; handles continuous and integer variables
- Configuration: number of evaluations budget, surrogate type, search strategy

#### scipy.optimize (Python)

The `scipy.optimize` module provides a comprehensive set of optimizers:

- `minimize(fun, x0, method=...)`: Gateway to gradient-based and gradient-free solvers. Methods include 'Nelder-Mead', 'Powell', 'CG', 'BFGS', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP', 'trust-constr'
- `differential_evolution(func, bounds)`: Global optimizer. Supports workers=-1 for parallel evaluation. Excellent default choice for continuous global optimization.
- `dual_annealing(func, bounds)`: Combines SA with local search. Good for multi-modal landscapes.
- `shgo(func, bounds)`: Simplicial homology global optimization. Guaranteed to find all local minima in bounds.
- `basinhopping(func, x0)`: Global optimizer combining random perturbation + local minimization.

#### DEAP (Python)

Distributed Evolutionary Algorithms in Python. Full-featured evolutionary computation framework.

- Define custom individuals, fitness classes, operators
- Built-in GA, GP (genetic programming), ES, PSO implementations
- Multi-objective support: NSGA-II, SPEA-2, NSGA-III
- Island model parallelization via Python multiprocessing
- Hall of Fame for tracking best individuals
- Statistics tracking and logging
- Extremely flexible but requires more setup than scipy

#### Optuna (Python)

Originally for hyperparameter tuning in ML, but fully adaptable to design optimization:

- Tree-structured Parzen Estimator (TPE) as default sampler (Bayesian-like)
- CMA-ES sampler available
- Handles mixed variable types (continuous, integer, categorical) natively
- Built-in pruning of unpromising trials (early stopping)
- Excellent dashboard visualization (Optuna Dashboard)
- Multi-objective support (NSGAIISampler, MOTPESampler)
- Database-backed study storage for resumable optimization
- Distributed optimization across machines

#### platypus-opt (Python)

Dedicated multi-objective optimization library:

- Algorithms: NSGA-II, NSGA-III, MOEA/D, IBEA, GDE3, SPEA2, EpsMOEA, OMOPSO
- Problem definition: explicit variable types, objectives, constraints
- Hypervolume indicator computation
- Pareto front visualization utilities
- Clean API for benchmarking multiple algorithms on same problem

---

### 10. Practical Guidelines

#### Starting Population Size

Rules of thumb for GA/PSO/DE:

- **Minimum**: 10 * n (n = number of design variables)
- **Recommended**: 50-200 for n < 20; 200-500 for 20 < n < 50; 500+ for n > 50
- **For discrete/combinatorial**: larger populations help (100-500)
- **For NSGA-II**: population should be at least 4 * number of objectives; 100-300 is typical
- **For CMA-ES**: 4 + floor(3 * ln(n)) is the default and usually sufficient

#### Convergence Detection

**Generation-based**: Stop after G_max generations (simple but wasteful or insufficient).

**Improvement-based**: Stop if best fitness has not improved by more than epsilon for N consecutive generations. epsilon = 0.1-1% of current best. N = 20-50 generations.

**Population diversity**: Stop if population diversity (standard deviation of fitness or genotype) falls below threshold. Low diversity = converged or premature convergence.

**Hypervolume (multi-objective)**: Stop if hypervolume improvement < epsilon for N generations.

**Budget-based**: Stop after E_max function evaluations. Important when evaluation cost is known and budget is fixed.

#### Result Validation

After optimization, always validate results:

1. **Re-evaluate** the optimal solution with the full-fidelity model (not surrogate or simplified model)
2. **Check constraints** independently -- optimizer penalty methods may allow slight violations
3. **Sensitivity analysis**: perturb optimal design variables by +/- 5-10% and check objective stability. If objective changes dramatically, the optimum is fragile
4. **Physical plausibility**: does the optimal design make engineering sense? If not, check problem formulation
5. **Multiple runs**: run the optimizer 5-10 times with different random seeds. If results vary significantly, the optimizer has not converged reliably
6. **Compare with baseline**: how much does the optimum improve over the initial/conventional design? If improvement is < 1%, optimization may not be worth the effort

#### Sensitivity Analysis Post-Optimization

**Local sensitivity**: partial derivative of objective with respect to each variable at the optimum. Identifies which variables most influence the objective. Computed via finite difference or adjoint method.

**Global sensitivity**: Sobol indices, Morris screening, or variance-based methods. Identifies which variables matter across the entire design space, not just at the optimum.

**Constraint activity**: which constraints are active (binding) at the optimum? Active constraints are the "bottleneck" -- relaxing them would improve the objective. Inactive constraints with large margins can potentially be removed to simplify the problem.

#### Reporting Optimization Results

An optimization study report should include:

1. Problem statement: objectives, variables (with ranges), constraints, evaluation method
2. Algorithm choice justification and parameter settings
3. Convergence plot (best fitness vs. generation/evaluation count)
4. For multi-objective: Pareto front plot, selected solution(s), trade-off discussion
5. Optimal design variable values and objective value(s)
6. Constraint satisfaction verification
7. Sensitivity analysis results
8. Comparison with baseline design
9. Computational cost (wall time, number of evaluations, hardware used)
10. Recommendations and limitations

#### Common Mistakes and How to Avoid Them

**Mistake 1: Over-constraining the problem**. Too many tight constraints leave no room for optimization. The optimizer finds the same feasible design regardless of initial conditions. Fix: relax non-critical constraints, increase variable ranges.

**Mistake 2: Wrong algorithm for the problem**. Using GA for a smooth, 3-variable problem (use BFGS). Using gradient descent for a discrete, multi-modal problem (use GA/DE). Fix: match algorithm to problem characteristics per the taxonomy in Section 2.

**Mistake 3: Insufficient evaluations**. Stopping too early yields suboptimal solutions presented as "optimal." Fix: run convergence study; increase budget until convergence plateaus.

**Mistake 4: Ignoring premature convergence**. Population converges to a local optimum. Fix: increase population size, use diversity-preserving mechanisms (niching, island model), increase mutation rate.

**Mistake 5: Poorly scaled variables**. Variables with vastly different ranges (e.g., beam depth in mm [100-1000] and prestress in kN [100-10000]) cause search inefficiency. Fix: normalize all variables to [0, 1] or similar range.

**Mistake 6: Black-box penalty functions**. Arbitrary penalty coefficients can make constraint handling erratic. Fix: use Deb's feasibility rules (parameter-free), adaptive penalty, or constraint-handling built into the algorithm (NSGA-II handles constraints natively).

**Mistake 7: Not validating with full-fidelity model**. Optimizing with a simplified model and assuming results hold for the real system. Fix: always re-evaluate final design with the highest-fidelity model available.

**Mistake 8: Presenting a single optimal solution without sensitivity context**. Stakeholders need to understand robustness. Fix: provide Pareto front, sensitivity analysis, and performance under perturbation.

**Mistake 9: Forgetting manufacturing/construction constraints**. An "optimal" design that cannot be built is worthless. Fix: include fabrication, erection, and construction constraints from the start.

**Mistake 10: Treating optimization as a substitute for engineering judgment**. Optimization is a tool, not a replacement for expertise. The engineer must formulate the right problem, interpret results critically, and make final decisions considering factors that resist quantification (aesthetics, precedent, client preferences, local construction practice). Fix: use optimization to inform decisions, not make them.


## ml-for-aec

### Machine Learning for AEC

> Computer vision for buildings, image-to-floorplan, generative ML models, performance prediction, structural analysis ML, energy prediction, natural language to design, and point cloud ML for AEC computational design

## Machine Learning for AEC

Machine learning is reshaping specific domains within Architecture, Engineering, and Construction, though the transformation is uneven. This skill provides a thorough, practitioner-oriented guide to where ML delivers real value in AEC today, the architectures and methods that work, the data challenges that constrain adoption, and practical pipelines for training, deploying, and maintaining ML models in production AEC workflows.

---

### 1. ML in AEC: Current State

#### 1.1 Where ML Actually Works in AEC Today

ML in AEC is most effective where three conditions converge: (a) sufficient training data exists or can be generated, (b) the task is well-defined with measurable performance metrics, and (c) the cost of errors is manageable or human review is in the loop.

**Proven, deployed applications**:
- Construction progress monitoring (photo comparison to BIM schedule)
- Safety monitoring on construction sites (PPE detection, exclusion zones)
- Defect detection (crack detection in concrete, facade inspections via drone imagery)
- Document classification (sorting drawings by discipline, type)
- Energy performance prediction (surrogate models replacing full simulation)
- Point cloud semantic segmentation (labeling structural elements from LiDAR scans)
- Cost estimation from early-stage design parameters

**Promising but not yet mature**:
- Floor plan generation from adjacency programs
- Automated scan-to-BIM conversion
- Generative massing from site constraints
- Structural topology optimization acceleration
- Natural language to BIM queries

**Overhyped or premature**:
- Fully autonomous building design from text prompts
- AI replacing architectural design judgment
- General-purpose design AI that understands building codes, physics, and aesthetics simultaneously
- End-to-end text-to-construction-documents

#### 1.2 Data Challenges in AEC

The AEC industry faces unique data challenges that limit ML adoption:

**Small datasets**: Unlike ImageNet (14M images) or web-scale text corpora, AEC datasets are small. A large architecture firm might have 5,000 floor plans in its portfolio. A structural engineering firm might have 2,000 analyzed buildings. These numbers are 3-4 orders of magnitude below what deep learning models typically require.

**Inconsistent labeling**: Building elements are labeled differently across firms, software platforms, and regions. A "wall" in one BIM model might be modeled as a "generic model" in another. Room naming conventions vary wildly. There is no universal taxonomy.

**Domain complexity**: Buildings are multi-physics systems where geometry, structure, thermal behavior, acoustics, daylight, and human experience interact. ML models that capture only one dimension produce solutions that fail on others.

**Proprietary data**: Most building data is proprietary. Firms are reluctant to share project data. Public datasets are limited in size and diversity.

**High-dimensional output**: A floor plan is not a single number or a class label; it is a complex geometric arrangement satisfying dozens of constraints simultaneously. This makes supervised learning difficult because the "ground truth" is itself a design decision, not an objective fact.

#### 1.3 ML Maturity by AEC Subdomain

| Subdomain | ML Maturity | Key Applications | Data Availability |
|-----------|-------------|-----------------|-------------------|
| Construction safety | High | PPE detection, hazard detection | Moderate (site cameras) |
| Defect inspection | High | Crack detection, moisture | Moderate (drone imagery) |
| Energy prediction | Medium-High | EUI prediction, load forecasting | Good (simulation data) |
| Document processing | Medium | Drawing classification, OCR | Moderate (drawing archives) |
| Point cloud processing | Medium | Semantic segmentation, object detection | Growing (LiDAR/photogrammetry) |
| Floor plan analysis | Medium | Recognition, evaluation | Limited (CubiCasa5K, RPLAN) |
| Structural analysis | Low-Medium | FEA acceleration, damage detection | Limited (simulation data) |
| Generative design | Low | Layout generation, massing | Very limited |
| Urban analysis | Low-Medium | Land use classification, traffic | Moderate (satellite, GIS) |

#### 1.4 Build vs. Buy Decisions

| Approach | When to Use | Examples |
|----------|------------|---------|
| **Use off-the-shelf** | Standard CV tasks (object detection, segmentation) with fine-tuning | YOLOv8, Detectron2, Segment Anything |
| **Fine-tune pre-trained** | AEC-specific tasks with moderate data (100-10,000 samples) | Fine-tuned ResNet for facade classification, ControlNet for architectural sketches |
| **Train from scratch** | Unique data modality or task with no applicable pre-trained model | Custom GNN for floor plan generation, custom PointNet for AEC-specific segmentation |
| **Buy commercial** | Mature, productized solutions where accuracy matters and in-house ML capacity is limited | OpenSpace (construction monitoring), Buildots, Avvir |

---

### 2. Computer Vision for AEC

#### 2.1 Object Detection

Detecting and localizing building elements in images, drawings, or renderings.

**Architectures**:

| Model | Speed | Accuracy | Best For |
|-------|-------|----------|----------|
| YOLOv8/v9 | Very fast (real-time) | Good | Site safety monitoring, real-time applications |
| Faster R-CNN | Moderate | Very good | Drawing element detection, precise localization |
| DETR (Detection Transformer) | Moderate | Very good | Complex scenes, variable-size objects |
| EfficientDet | Fast | Good | Mobile/edge deployment, drone imagery |

**AEC object detection tasks**:
- Detecting doors, windows, columns, stairs in architectural drawings
- Identifying structural elements (beams, columns, braces) in construction photos
- Recognizing equipment (HVAC units, electrical panels) in MEP drawings
- Detecting construction vehicles and workers on site
- Identifying signage, safety barriers, and temporary works

**Training data preparation**:
1. Collect images: site photos, drawing scans, BIM screenshots, drone footage
2. Annotate with bounding boxes using tools like LabelImg, CVAT, Roboflow, Label Studio
3. Define class taxonomy: start small (5-10 classes), expand as needed
4. Ensure diversity: different lighting, angles, scales, drawing styles
5. Split: 70% train, 15% validation, 15% test; ensure no project overlap between splits
6. Augment: rotation, flipping, brightness, contrast, noise for images; not applicable for drawings where orientation matters

#### 2.2 Semantic Segmentation

Pixel-level classification of every pixel in an image.

**Architectures**:

| Model | Parameters | Best For |
|-------|-----------|----------|
| U-Net | ~31M | Medical imaging heritage; small datasets; floor plan segmentation |
| DeepLab v3+ | ~41M | Outdoor scenes; site analysis; aerial imagery |
| SegFormer | ~13-85M | General purpose; good accuracy/speed balance |
| Segment Anything (SAM) | ~636M | Zero-shot; interactive; foundation model |

**AEC semantic segmentation tasks**:
- Floor plan segmentation: walls, rooms, doors, windows, furniture
- Facade segmentation: windows, walls, balconies, cornices, rooflines
- Site segmentation from aerial imagery: buildings, roads, vegetation, water, parking
- Construction site segmentation: excavation, structure, formwork, scaffolding
- Material segmentation: concrete, steel, glass, masonry, wood in building photos

**U-Net for floor plan segmentation**:
```
Input: RGB image of floor plan (256x256 or 512x512)
Output: Per-pixel class map (wall, room, door, window, furniture, background)

Architecture:
  Encoder: [Conv-BN-ReLU-Conv-BN-ReLU-MaxPool] x 4 (downsample path)
  Bottleneck: [Conv-BN-ReLU-Conv-BN-ReLU]
  Decoder: [UpConv-Concat(skip)-Conv-BN-ReLU-Conv-BN-ReLU] x 4 (upsample path)
  Output: 1x1 Conv → Softmax (num_classes channels)

Key: Skip connections concatenate encoder features to decoder at each level,
     preserving spatial detail for precise boundary delineation.
```

#### 2.3 Instance Segmentation

Detecting individual object instances with pixel-precise masks.

**Mask R-CNN** is the standard architecture:
1. Backbone (ResNet-50/101 + FPN) extracts multi-scale features
2. Region Proposal Network (RPN) proposes candidate regions
3. For each region: classify object, refine bounding box, predict pixel mask
4. Non-maximum suppression removes duplicate detections

**AEC applications**:
- Individual room detection in floor plans (each room as a separate instance)
- Individual facade panel detection for curtain wall analysis
- Individual crack instance detection for structural assessment
- Individual worker detection for headcount and safety

#### 2.4 Document Understanding

Processing architectural and engineering documents:

**P&ID (Piping & Instrumentation Diagram) recognition**:
- Symbol detection (valves, pumps, instruments, equipment)
- Line detection (process lines, signal lines)
- Text recognition (tag numbers, labels)
- Topology extraction (connectivity graph)

**Drawing annotation extraction**:
- Title block parsing: project name, sheet number, revision, date, scale
- Dimension text extraction
- Room name and number extraction
- Note and specification text extraction

**Models**: Combination of object detection (for symbols), line detection (for pipes), and OCR (for text). Tesseract, PaddleOCR, or EasyOCR for text; custom detectors for symbols.

#### 2.5 Construction Progress Monitoring

Comparing as-built photos to BIM model to track construction progress:

1. **Image capture**: 360-degree cameras on hard hats or fixed mounts; capture daily
2. **Pose estimation**: Determine camera position relative to BIM using visual SLAM or marker-based localization
3. **Element matching**: Match detected elements in photos to BIM elements using projected positions
4. **Progress scoring**: For each BIM element, determine installation status:
   - Not started (element not visible)
   - In progress (partially installed)
   - Complete (fully installed, matches BIM geometry)
5. **Dashboard**: Overlay progress status on BIM model; generate progress reports

Commercial solutions: OpenSpace, Buildots, Avvir, HoloBuilder

#### 2.6 Safety Monitoring

Real-time safety monitoring on construction sites:

**PPE detection**: Detect presence/absence of hard hats, safety vests, safety glasses, gloves
- Model: YOLOv8 fine-tuned on construction safety dataset
- Classes: person, hard_hat, no_hard_hat, vest, no_vest
- Inference: Real-time on edge GPU (Jetson, Intel NCS)
- Alert: If no_hard_hat or no_vest detected, trigger alert

**Unsafe behavior detection**:
- Worker in exclusion zone (geofenced dangerous areas)
- Worker near heavy equipment operating radius
- Working at height without fall protection
- Improper lifting posture

**Datasets**: COCO (general person detection), SODA (Safety Of Drivers and Automobiles), SHEL5K (Safety HElmet), Chi-SID (Construction Safety Image Dataset)

#### 2.7 Defect Detection

Automated inspection of building elements:

**Crack detection in concrete**:
- Semantic segmentation: U-Net trained on crack images; output binary mask (crack/no-crack)
- Classification: ResNet classifying image patches as cracked/uncracked
- Measurement: From segmentation mask, calculate crack width, length, orientation
- Datasets: Concrete Crack Images for Classification (40K images), SDNET2018, CrackForest

**Facade inspection from drone imagery**:
- Staining, discoloration, spalling, efflorescence detection
- Missing or damaged cladding panels
- Window seal deterioration
- Vegetation growth

**Structural damage assessment**:
- Post-earthquake damage classification (none, slight, moderate, severe, collapse)
- Fire damage assessment
- Corrosion detection on steel structures
- Timber decay and insect damage

---

### 3. Floor Plan Intelligence

#### 3.1 Floor Plan Recognition

Converting raster floor plan images to structured vector data:

**Pipeline**:
1. **Preprocessing**: Binarize image, remove noise, deskew
2. **Wall detection**: Use semantic segmentation (U-Net) or line detection (Hough transform, LSD) to identify walls
3. **Room segmentation**: Flood fill between walls to identify rooms; or use instance segmentation
4. **Opening detection**: Detect doors (arc symbols, break in wall) and windows (double line, symbol)
5. **Text extraction**: OCR for room names, dimensions, annotations
6. **Vectorization**: Convert pixel boundaries to vector polylines; simplify and orthogonalize
7. **Topology extraction**: Build room adjacency graph from shared walls

**Challenges**:
- Varying drawing conventions across firms and regions
- Different scales and resolutions
- Furniture and annotation clutter
- Curved walls and non-orthogonal geometry
- Multi-page drawings with cross-references

#### 3.2 Floor Plan Generation

Generating novel floor plan layouts using ML:

**Graph2Plan** (2020):
- Input: Room adjacency graph with room types and areas
- Process: Graph neural network encodes adjacency relationships; decoder generates room bounding boxes; retrieval module finds similar real floor plans
- Output: Bounding box layout satisfying adjacency and area constraints
- Training data: RPLAN dataset (80K floor plans)

**HouseDiffusion** (2023):
- Input: Room adjacency graph with types and areas
- Process: Denoising diffusion model conditioned on graph; iteratively denoises room positions and boundaries
- Output: Floor plan with room polygons
- Advantage: Diverse outputs from same input; controllable generation

**House-GAN++** (2021):
- Input: Bubble diagram (graph with room types)
- Process: Conditional GAN with graph-based discriminator; generator produces room layouts; discriminator evaluates realism and constraint satisfaction
- Output: Room boundary masks
- Training: LIFULL HOME'S dataset

**LayoutGAN** (2019):
- Input: Set of room types and counts
- Process: GAN with layout-specific discriminator; rooms as bounding boxes
- Output: Non-overlapping rectangular room arrangement

#### 3.3 Floor Plan Evaluation

ML models for scoring layout quality:

**Metrics that can be learned**:
- Circulation efficiency (ratio of circulation to usable area)
- Room proportion quality (aspect ratio deviation from ideal)
- Daylight access (percentage of habitable rooms on exterior wall)
- Privacy gradient (public rooms near entry, private rooms deeper)
- Structural regularity (alignment of load-bearing elements)

**Approach**: Train a regression model on architect-scored floor plans. Features: graph-based (adjacency satisfaction), geometric (room proportions, areas), topological (depth from entry, circulation loops).

#### 3.4 Key Datasets

| Dataset | Size | Content | Access |
|---------|------|---------|--------|
| CubiCasa5K | 5,000 | Finnish floor plans, SVG format, annotated | Public |
| RPLAN | 80,000 | Chinese residential floor plans, vector | Public (request) |
| HousExpo | 35,000 | Floor plans from Zillow, rasterized | Public |
| LIFULL HOME'S | 5M+ | Japanese rental listings with floor plans | Research access |
| ROBIN | 100+ | Richly annotated office building floor plans | Public |
| CVC-FP | 122 | Floor plan images with ground truth | Public |
| SESYD | 10 sets | Synthetic floor plans for symbol recognition | Public |

#### 3.5 Key Models

| Model | Year | Task | Architecture | Input | Output |
|-------|------|------|-------------|-------|--------|
| Graph2Plan | 2020 | Generation | GNN + Retrieval | Adjacency graph | Bounding boxes |
| HouseDiffusion | 2023 | Generation | Diffusion + GNN | Adjacency graph | Room polygons |
| House-GAN++ | 2021 | Generation | Conditional GAN | Bubble diagram | Room masks |
| LayoutGAN | 2019 | Generation | GAN | Room types | Bounding boxes |
| Raster-to-Vector | 2017 | Recognition | CNN + Integer Programming | Floor plan image | Vector floor plan |
| FloorplanGAN | 2020 | Generation | pix2pix variant | Building boundary | Floor plan image |

---

### 4. Generative ML Models for Design

#### 4.1 GANs (Generative Adversarial Networks)

**pix2pix** (image-to-image translation):
- Paired training data: (input, output) image pairs
- AEC applications:
  - Sketch → rendered facade
  - Zoning diagram → floor plan
  - Site plan → massing model
  - Daylight map → facade design
- Architecture: U-Net generator + PatchGAN discriminator
- Training: ~100-500 paired examples can produce usable results

**CycleGAN** (unpaired image translation):
- No paired data needed; learns mapping between two domains
- AEC applications:
  - Day → night rendering
  - Summer → winter site visualization
  - Photo → sketch style transfer
  - As-built photo → clean rendering
- Advantage: Does not require paired examples
- Limitation: Less precise than pix2pix; struggles with geometric accuracy

**StyleGAN** (style-based generation):
- Generates high-resolution images with control over style at different scales
- AEC applications:
  - Generating facade texture variations
  - Exploring interior design styles
  - Creating synthetic training images for other CV tasks
- Limitation: Generates images, not geometry; no guarantee of physical validity

**Conditional GAN**:
- Generator conditioned on additional input (class label, text, image, graph)
- AEC: condition on building program, site constraints, or style preference
- Enables controllable generation: "generate a 3-bedroom apartment with south-facing living room"

#### 4.2 VAEs (Variational Autoencoders)

**Latent space exploration**:
- Encode existing designs into a continuous latent space
- Interpolate between designs: blend floor plan A and floor plan B
- Sample from latent space to generate novel designs
- Navigate latent space dimensions to understand design variation

**AEC applications**:
- Exploring the space of possible facade designs
- Interpolating between two building massing options
- Generating design variations by perturbing latent vectors
- Design recommendation: find latent neighbors of a liked design

**Advantage over GANs**: Smoother latent space; more controllable generation; probabilistic framework (uncertainty quantification)

**Limitation**: Outputs tend to be blurrier than GANs; reconstruction quality may not be as crisp

#### 4.3 Diffusion Models

**Denoising Diffusion Probabilistic Models (DDPM)**:
- Forward process: Gradually add Gaussian noise to data until it becomes pure noise
- Reverse process: Learn to denoise step by step, recovering the original data
- Generation: Start from random noise, iteratively denoise to produce new samples

**Stable Diffusion for architecture**:
- Text-to-image generation with architectural prompts
- Fine-tuning on architectural datasets for domain-specific generation
- ControlNet: Additional conditioning on edge maps, depth maps, or floor plans
- LoRA: Lightweight fine-tuning for specific architectural styles

**ControlNet for architectural sketches**:
- Condition Stable Diffusion on Canny edge maps (from architectural sketches)
- Or on depth maps (from massing models)
- Or on segmentation maps (from zoning diagrams)
- Produces photorealistic renderings that follow the spatial structure of the control input

**AEC-specific diffusion models**:
- HouseDiffusion: Floor plan generation conditioned on room adjacency graph
- Text-to-3D (e.g., DreamFusion, Magic3D): Generating 3D building models from text descriptions (early stage, limited architectural quality)

#### 4.4 Graph Neural Networks

**GNN for building layout**:
- Represent building program as a graph: rooms = nodes, adjacencies = edges
- GNN encodes graph structure into node and edge embeddings
- Decoder predicts room positions and dimensions from embeddings

**GNN architectures for AEC**:
- GCN (Graph Convolutional Network): Aggregate neighbor features; good for room classification
- GAT (Graph Attention Network): Weighted neighbor aggregation; captures varying adjacency importance
- GraphSAGE: Sampling-based aggregation; scalable to large buildings
- Message Passing Neural Network (MPNN): General framework; custom message and update functions

**Applications beyond layout**:
- Structural frame analysis: nodes = joints, edges = members; predict forces, deflections
- Building system topology: nodes = equipment, edges = connections; predict performance
- Urban network analysis: nodes = buildings/intersections, edges = streets; predict pedestrian flow

#### 4.5 Point Cloud Generation

**3D shape generation for building massing**:
- PointFlow: Normalizing flow model generating point clouds
- Point-E (OpenAI): Text-to-3D point cloud generation
- ShapeNet: Large-scale 3D shape dataset (includes some architectural objects)

**Current limitations**: Generated shapes lack architectural precision; no structural logic; no floor plates or walls; resolution too low for detailed building geometry. Useful for early-stage massing exploration only.

#### 4.6 Current Limitations of Generative ML for AEC

1. **Physical validity**: Generated designs may violate structural, MEP, or code requirements
2. **Resolution**: Output resolution insufficient for construction documentation
3. **Geometric precision**: ML models produce fuzzy boundaries; not the crisp lines needed for architecture
4. **Constraint enforcement**: Difficult to enforce hard constraints (code compliance, structural limits) within the generation process
5. **Evaluation**: No universally accepted metric for design quality; human evaluation is expensive and subjective
6. **Data**: Small AEC datasets limit generative model quality; models trained on web images do not understand buildings
7. **Integration**: Generated outputs do not integrate directly with BIM software without significant post-processing

---

### 5. Performance Prediction Models

#### 5.1 Energy Prediction

Predicting building energy use intensity (EUI) from design parameters without running full simulation:

**Input features**:
- Geometry: floor area, surface-to-volume ratio, compactness, number of stories
- Envelope: wall U-value, roof U-value, window U-value, WWR by orientation
- Orientation: building azimuth, latitude
- Climate: HDD, CDD, solar radiation
- Systems: HVAC type, lighting power density, equipment load
- Schedule: occupancy hours, setpoint temperatures

**Target variable**: Annual EUI (kWh/m2/yr) or monthly energy consumption

**Training data generation**:
1. Create parametric building model (e.g., in OpenStudio or EnergyPlus via eppy)
2. Define parameter ranges (sampling plan: Latin Hypercube Sampling)
3. Run 1,000-10,000 simulations
4. Each simulation = one training example (parameters → EUI)

**Model comparison** (typical performance on EUI prediction):

| Model | R2 | RMSE (kWh/m2) | Training Time | Interpretability |
|-------|-----|---------------|---------------|------------------|
| Linear Regression | 0.70-0.80 | 15-25 | Seconds | High |
| Random Forest | 0.90-0.95 | 5-12 | Minutes | Medium (SHAP) |
| XGBoost | 0.92-0.97 | 4-10 | Minutes | Medium (SHAP) |
| Neural Network (MLP) | 0.93-0.97 | 4-9 | Minutes-Hours | Low |
| Gaussian Process | 0.95-0.98 | 3-7 | Hours | High (uncertainty) |

#### 5.2 Daylight Prediction

Predicting spatial Daylight Autonomy (sDA) or Annual Sunlight Exposure (ASE) from room geometry:

**Input features**:
- Room dimensions (width, depth, height)
- Window geometry (width, height, sill height, per facade)
- Window properties (VLT, SHGC)
- External obstructions (height, distance)
- Latitude, orientation
- Ceiling/wall/floor reflectance

**Surrogate model approach**: Train on Radiance/DAYSIM simulation results. Typical accuracy: R2 > 0.90 for sDA prediction.

#### 5.3 Structural Prediction

**Load prediction from architectural models**:
- Input: Architectural model geometry (floor areas, spans, facade areas)
- Output: Approximate structural loads (dead load, live load, wind load)
- Use: Early-stage structural budget without detailed analysis

**Deflection estimation**:
- Input: Span, member depth, load, material properties
- Output: Maximum deflection
- Use: Quick check against L/360, L/240 limits

**FEA acceleration**:
- Train neural network on FEA results for a parametric structural model
- Predict stress/displacement fields without running FEA
- Speedup: 1000x+ for structural optimization iterations
- Architecture: Convolutional neural network on stress field images, or graph neural network on mesh

#### 5.4 Wind Prediction (Surrogate CFD)

Training ML to replace computationally expensive CFD simulations:

**Input features**:
- Building massing (voxelized or parameterized)
- Wind direction and speed
- Surrounding context geometry
- Height above ground for evaluation points

**Output**: Wind speed, pressure coefficients, or pedestrian comfort category at evaluation points

**Approach**: Train CNN on 3D voxel grid of massing with wind direction encoding. Output: 3D field of wind speed multipliers.

**Training data**: 500-2,000 CFD simulations with varied massing and wind conditions.

**Accuracy**: Typically within 10-20% of CFD for pedestrian-level wind speed prediction; sufficient for early design screening, not for final assessment.

#### 5.5 Acoustic Prediction

**RT60 (Reverberation Time) estimation**:
- Input: Room volume, surface areas by material, absorption coefficients
- Output: RT60 in octave bands (125 Hz to 4 kHz)
- Sabine equation: RT60 = 0.161 * V / A (deterministic, no ML needed)
- ML added value: Predicting spatial distribution of sound levels, early decay time, clarity (C50/C80)

**Speech intelligibility prediction**:
- Input: Room geometry, source/receiver positions, surface treatment
- Output: STI (Speech Transmission Index) at receiver locations
- ML: CNN on room section with source/receiver marked; predict STI map

#### 5.6 Feature Engineering for AEC

Effective features for AEC ML models:

**Geometric features**:
- Area, perimeter, volume, surface area
- Compactness (Polsby-Popper: 4*pi*A/P^2)
- Aspect ratio (width/depth)
- Surface-to-volume ratio
- Convexity (area / convex hull area)
- Number of vertices (complexity)
- Minimum enclosing rectangle dimensions

**Spatial features**:
- Distance to boundary, to core, to window
- Depth from entry (graph distance)
- Isovist area, perimeter, compactness (visibility analysis)
- Sky view factor
- Solar exposure hours

**Material features**:
- Thermal resistance (R-value, U-value)
- Visible light transmittance (VLT)
- Solar heat gain coefficient (SHGC)
- Absorption coefficient (acoustic)
- Density, specific heat, thermal mass

**Topological features**:
- Connectivity (number of doors/openings)
- Graph centrality (betweenness, closeness)
- Clustering coefficient (local adjacency density)
- Path length to key spaces (entry, exit, core)

#### 5.7 Model Types Comparison

| Model | Strengths | Weaknesses | Best For |
|-------|-----------|------------|----------|
| Random Forest | Robust, handles mixed features, no scaling needed, feature importance | Slow for large datasets, no extrapolation | Tabular AEC data, initial baseline |
| XGBoost | State-of-the-art for tabular data, regularization, fast | Requires tuning, black-box | Performance prediction, classification |
| MLP Neural Network | Universal approximator, handles non-linearity | Requires more data, scaling, tuning | Large datasets, complex relationships |
| Gaussian Process | Uncertainty quantification, good with small data | O(n^3) scaling, limited to ~10K samples | Small AEC datasets, optimization |
| CNN | Spatial data (images, grids, fields) | Requires image-like input, many parameters | Image-based prediction, field prediction |
| GNN | Graph-structured data (building topology) | Relatively new, fewer tools | Structural analysis, layout evaluation |

---

### 6. Structural ML

#### 6.1 Topology Optimization Acceleration

Traditional topology optimization (SIMP, level-set) requires hundreds of FEA iterations. ML can accelerate this:

**Approach 1: Direct prediction**
- Input: Load cases, boundary conditions, volume fraction, design domain
- Output: Optimized material distribution (density field)
- Architecture: CNN (encode design domain + loads → decode density field)
- Training: 10,000-100,000 solved topology optimization problems
- Speedup: 1000x+ (single forward pass vs. 200+ FEA iterations)

**Approach 2: Neural network as FEA substitute**
- Replace FEA within the optimization loop with a neural network
- Each optimization iteration uses NN instead of FEA to evaluate compliance
- Speedup: 10-100x (still iterative, but each iteration is fast)

**Approach 3: Transfer learning**
- Train on a family of similar problems (e.g., cantilever beams with varying loads)
- Fine-tune on new problem with few iterations
- Useful when the design domain family is known in advance

#### 6.2 Connection Design Classification

Classifying structural connections for automated detailing:

- Input: Joint geometry, member sizes, load demands
- Output: Connection type (welded, bolted, end plate, angle, clip), component sizes
- Model: Decision tree or random forest (interpretable, matches engineering practice)
- Training data: Connection design databases from structural firms

#### 6.3 Damage Detection from Sensor Data

Structural health monitoring using ML:

- Input: Accelerometer, strain gauge, or displacement sensor time series
- Output: Damage presence, location, severity
- Methods:
  - Anomaly detection: Autoencoders trained on healthy data; high reconstruction error = damage
  - Classification: CNN on vibration signal spectrograms; classify damage type
  - Regression: Predict damage index from modal parameters (frequencies, mode shapes)

#### 6.4 Seismic Response Prediction

Predicting structural response to earthquake ground motions:

- Input: Building parameters (height, period, damping, ductility), ground motion intensity measures (PGA, Sa(T1), Arias intensity)
- Output: Peak inter-story drift, peak floor acceleration, residual drift
- Model: Neural network or Gaussian Process trained on nonlinear time history analysis results
- Application: Rapid loss assessment, performance-based design screening

#### 6.5 Generative Structural Design

Using ML to generate novel structural systems:

- Reinforcement learning: Agent designs truss/frame topology; reward = structural efficiency + constructability
- GAN: Generate structurally valid connection details
- Diffusion model: Generate 3D structural topologies conditioned on loads and supports
- Current state: Research-stage; not yet reliable for production design

---

### 7. Point Cloud ML

#### 7.1 3D Object Detection in Point Clouds

Detecting and localizing objects (building elements, MEP equipment) in 3D point clouds:

**VoxelNet**: Voxelize point cloud → 3D CNN → detect objects
**PointPillars**: Encode points in vertical columns (pillars) → 2D CNN → detect objects (originally for autonomous driving; adaptable to AEC)
**3DSSD**: Single-stage 3D object detection; fast; good for real-time scanning applications

AEC-specific detection:
- Detecting columns, beams, slabs in as-built scans
- Locating MEP equipment (AHUs, pumps, switchgear) in facility scans
- Identifying doors, windows, and openings in wall scans
- Detecting structural connections for inspection

#### 7.2 Semantic Segmentation

Assigning a class label to every point in the cloud:

**PointNet** (2017):
- First deep learning model operating directly on raw point clouds
- Architecture: Shared MLP per point → max pooling (global feature) → per-point classification
- Limitation: Does not capture local structure (no neighborhood information)

**PointNet++** (2017):
- Hierarchical PointNet with local grouping
- Set Abstraction layers: sample centroids → group neighbors → apply PointNet locally
- Feature Propagation: upsample features from subsampled set back to original points
- Better than PointNet for spatially complex AEC environments

**RandLA-Net** (2020):
- Designed for large-scale point clouds (millions of points)
- Random sampling (faster than FPS) + Local Feature Aggregation (attention-based)
- State-of-the-art on large outdoor datasets (Semantic3D, SemanticKITTI)
- Well-suited for AEC: building scans are large (10M-100M+ points)

**KPConv** (2019):
- Kernel Point Convolution: defines convolution kernels as sets of points in 3D
- Rigid and deformable variants
- Strong performance on indoor datasets (S3DIS, ScanNet)
- Good for detailed building interior segmentation

#### 7.3 Instance Segmentation of Building Elements

Beyond per-point classification, identify individual instances:

- **3D-BoNet**: Bounding box + binary mask per instance
- **PointGroup**: Semantic segmentation + offset prediction + clustering
- **MASC**: Multi-scale attention for instance clustering
- **SoftGroup**: Soft semantic scoring + bottom-up grouping

AEC application: Detect each individual pipe, duct, beam, column as a separate instance for BIM element creation.

#### 7.4 Scan-to-BIM Automation

The holy grail of point cloud ML for AEC: automatically converting 3D scans to BIM models:

**Pipeline**:
1. **Preprocessing**: Downsample (e.g., 1cm resolution), filter noise, register multiple scans
2. **Segmentation**: Semantic segmentation (wall, floor, ceiling, column, pipe, duct, furniture)
3. **Primitive fitting**: Fit geometric primitives to segments:
   - Planes → walls, floors, ceilings
   - Cylinders → pipes, columns
   - Boxes → beams, equipment
   - Custom shapes → MEP fittings
4. **Topology recovery**: Determine connections between elements (wall-wall intersection, pipe-fitting-pipe)
5. **BIM element creation**: Map primitives to BIM elements with attributes (type, material, dimensions)
6. **Model assembly**: Create IFC or Revit model from elements

**Current state**: Steps 1-3 are increasingly automated with ML. Steps 4-6 still require significant manual intervention. Full end-to-end scan-to-BIM automation is 3-5 years away for typical buildings.

#### 7.5 As-Built vs. As-Designed Comparison

Comparing point cloud (as-built) to BIM model (as-designed):

1. **Registration**: Align point cloud to BIM coordinate system (ICP, feature matching)
2. **Point-to-surface distance**: For each point, compute distance to nearest BIM surface
3. **Deviation mapping**: Color-code deviations (green = within tolerance, yellow = marginal, red = out of tolerance)
4. **Tolerance checking**: Flag elements exceeding tolerance (typically ±25mm for structural, ±50mm for architectural)
5. **Missing element detection**: BIM elements with no nearby points may be missing or not yet installed
6. **Extra element detection**: Point clusters not corresponding to any BIM element indicate field additions

#### 7.6 Point Cloud Datasets for AEC

| Dataset | Points | Classes | Environment | Access |
|---------|--------|---------|-------------|--------|
| S3DIS | 696M | 13 | Office buildings (6 areas) | Public |
| ScanNet | 2.5M frames | 40 | Indoor rooms (1513 scenes) | Public (request) |
| Semantic3D | 4B | 8 | Outdoor urban/rural | Public |
| SemanticKITTI | 4.5B | 28 | Outdoor driving | Public |
| Toronto3D | 78M | 8 | Urban street | Public |
| DALES | 505M | 8 | Aerial urban | Public |
| Hessigheim3D | 800M | 11 | Dense urban (aerial+terrestrial) | Public |
| SUM | 3.7B | 6 | Urban (Helsinki) | Public |
| BuildingNet | 513K meshes | 31 | 3D building models | Public |

---

### 8. NLP for AEC

#### 8.1 Building Code Parsing and Querying

Using NLP to make building codes searchable and machine-readable:

**Approaches**:
- **Information retrieval**: Index code text; retrieve relevant sections for a query (e.g., "What is the maximum travel distance for a sprinklered business occupancy?")
- **Named entity recognition**: Extract entities from code text (dimensions, occupancy types, construction types, materials)
- **Relation extraction**: Identify relationships between entities (occupancy + sprinkler status → travel distance)
- **Question answering**: LLM fine-tuned on building code corpus; answer natural language questions about code requirements
- **Semantic parsing**: Convert code text to structured rules (IF-THEN format) for automated compliance checking

**Challenges**: Building codes use dense legal language with complex cross-references, exceptions, and conditional clauses. Accuracy requirements are high (incorrect code interpretation has liability implications).

#### 8.2 Design Brief Analysis

Extracting structured information from narrative design briefs:

- Room program extraction: identify room types, areas, counts from text
- Adjacency requirement extraction: identify required spatial relationships
- Performance requirements: extract energy targets, acoustic requirements, daylight standards
- Aesthetic preferences: identify style references, material preferences
- Budget constraints: extract cost targets, phasing requirements

#### 8.3 Specification Writing Assistance

LLM-assisted specification generation:

- Generate draft specifications from BIM model data (materials, products, performance requirements)
- Check specifications against model for consistency
- Suggest specification sections based on drawing content
- Cross-reference specifications with product databases
- Format according to MasterFormat / UniFormat / NRM

#### 8.4 LLM-Powered Design Assistants

Current state of LLM assistants for AEC:

**What works today**:
- Code question answering (with appropriate RAG on code text)
- Script generation (Revit API, Grasshopper C#, Dynamo Python)
- Report writing from structured data
- Design option comparison and evaluation
- Meeting minutes summarization
- RFI response drafting

**What does not yet work reliably**:
- Direct geometry generation (LLMs do not understand spatial relationships well)
- Complex multi-step design reasoning
- Integration with live BIM models
- Real-time design feedback during modeling
- Autonomous code compliance checking (hallucination risk)

#### 8.5 Text-to-3D Model Generation

Emerging capability: generating 3D building models from text descriptions:

- Current models (DreamFusion, Magic3D, MVDream) produce generic 3D shapes, not architecturally precise geometry
- Text-to-massing (e.g., "L-shaped building, 5 stories, with courtyard") is feasible with fine-tuned models
- Text-to-detailed-building is years away from practical quality
- Intermediate approach: text → 2D sketch (Stable Diffusion) → manual 3D modeling from sketch

#### 8.6 Automated Reporting from BIM Data

Generating narrative reports from structured BIM data:

- Area schedules → written area report with analysis
- Energy simulation results → sustainability narrative for planning application
- Clash detection results → coordination report with prioritized action items
- Cost model data → cost report with variance analysis
- Construction schedule data → progress narrative

---

### 9. Practical ML Pipeline for AEC

#### 9.1 Data Collection and Preparation

**AEC data sources**:
- BIM models (Revit, ArchiCAD, IFC exports)
- CAD drawings (DWG, DXF)
- Point cloud scans (LAS, E57, PLY)
- Construction photos (JPEG, PNG from site cameras)
- Sensor data (CSV, JSON from IoT devices)
- GIS data (Shapefile, GeoJSON, raster)
- Simulation results (EnergyPlus output, FEA results)

**Data preprocessing for AEC**:
1. **Standardize units**: Ensure consistent metric/imperial
2. **Coordinate system alignment**: Align all data to common coordinate system
3. **Missing data handling**: AEC data is often incomplete; impute or flag missing values
4. **Outlier detection**: Identify and handle anomalous values (e.g., room with 0 area, wall with 100m thickness)
5. **Class balancing**: AEC datasets are often imbalanced (many walls, few stairs); use oversampling, undersampling, or class weights

#### 9.2 Feature Engineering for AEC Data

See Section 5.6 for detailed feature types. Key principles:
- Use domain knowledge to create meaningful features (architects and engineers know what matters)
- Normalize features to similar scales (StandardScaler, MinMaxScaler)
- Handle categorical features (one-hot encoding for room types, occupancy types)
- Create interaction features (WWR * orientation = directional solar gain proxy)
- Dimensionless ratios often work better than raw dimensions (compactness, aspect ratio vs. raw width/height)

#### 9.3 Model Selection Decision Tree

```
Is the output a category or a number?
├── Category (classification)
│   ├── Structured/tabular data → XGBoost or Random Forest
│   ├── Image data → CNN (ResNet, EfficientNet) or ViT
│   ├── Point cloud data → PointNet++ or KPConv
│   └── Graph data → GNN (GCN, GAT)
│
└── Number (regression)
    ├── Structured/tabular data
    │   ├── Small dataset (<1000) → Gaussian Process or Random Forest
    │   ├── Medium dataset (1K-100K) → XGBoost or MLP
    │   └── Large dataset (>100K) → Deep learning (MLP, CNN)
    ├── Image/field output → U-Net or encoder-decoder CNN
    ├── Sequence output → Transformer or LSTM
    └── Generative (create new designs)
        ├── Image-like output → GAN, VAE, or Diffusion Model
        ├── Graph-conditioned → GNN + Decoder
        └── Point cloud output → PointFlow or Point-E
```

#### 9.4 Training Infrastructure

| Scale | Hardware | Cost | Use Case |
|-------|----------|------|----------|
| Prototype | Consumer GPU (RTX 4070-4090) | $800-2000 one-time | Small models, experimentation |
| Development | Workstation GPU (A5000, A6000) | $3000-7000 one-time | Medium models, production training |
| Production | Cloud GPU (A100, H100) | $2-5/hr (AWS, GCP, Azure) | Large models, multi-GPU training |
| Inference | CPU or edge GPU (Jetson) | $200-500 per device | Deployed model serving |

#### 9.5 Validation Methodology

**Standard k-fold cross-validation**: Split data into k folds (typically 5 or 10); train on k-1, test on 1; rotate and average.

**Spatial cross-validation** (important for AEC): Buildings from the same project or site should not appear in both training and test sets. Group by project, not by individual samples.

**Temporal cross-validation**: For construction monitoring or operational data, use time-based splits (train on earlier data, test on later data).

**Domain shift testing**: Test on data from a different building type, climate zone, or country to assess generalization.

#### 9.6 Deployment Options

| Deployment | Method | Latency | Integration |
|-----------|--------|---------|-------------|
| REST API | Flask/FastAPI + Docker | 100-500ms | Any platform via HTTP |
| Grasshopper plugin | GH_CPython, Hops | 200ms-5s | Rhino/Grasshopper |
| Revit add-in | .NET + ONNX Runtime | 100-500ms | Revit |
| Edge device | TensorRT, ONNX, TFLite | 10-100ms | Site cameras, IoT |
| Batch processing | Airflow, Prefect | Minutes-hours | Simulation pipelines |
| Web application | Streamlit, Gradio, React | 200ms-2s | Browser-based tools |

#### 9.7 MLOps for AEC

- **Model versioning**: Track model versions with DVC, MLflow, or Weights & Biases
- **Data versioning**: Track training data versions (DVC, lakeFS)
- **Experiment tracking**: Log hyperparameters, metrics, artifacts (MLflow, W&B)
- **Model monitoring**: Track prediction quality in production; detect drift
- **Retraining triggers**: New data available, performance degradation detected, code edition changed
- **CI/CD for ML**: Automated testing, validation, and deployment pipelines

#### 9.8 Tools and Frameworks

| Category | Tools |
|----------|-------|
| Deep learning | PyTorch, TensorFlow, JAX |
| Classical ML | scikit-learn, XGBoost, LightGBM |
| Computer vision | torchvision, Detectron2, MMDetection, Ultralytics (YOLO) |
| Point cloud | Open3D, PyTorch Geometric, torch-points3d |
| NLP/LLM | Hugging Face Transformers, LangChain, LlamaIndex |
| Generative | Diffusers (Hugging Face), StyleGAN3, NVIDIA NeMo |
| Model serving | ONNX Runtime, TorchServe, Triton Inference Server |
| Experiment tracking | MLflow, Weights & Biases, Neptune |
| Data | DVC, Label Studio, Roboflow, CVAT |
| Deployment | Docker, FastAPI, Gradio, Streamlit |

---

### 10. Ethical Considerations

#### 10.1 Bias in Training Data

- Floor plan datasets are dominated by specific cultures (Chinese residential in RPLAN, Finnish in CubiCasa5K). Models trained on these produce culturally biased layouts.
- Construction safety datasets may underrepresent certain demographics, leading to biased PPE detection.
- Energy models trained on one climate zone do not generalize to others.
- Mitigation: Diversify training data, test across populations and regions, document training data composition.

#### 10.2 Liability for ML-Driven Design Decisions

- Who is liable when an ML model suggests a non-compliant design? The architect? The software vendor? The ML developer?
- Professional responsibility still rests with the licensed professional who signs and seals the documents.
- ML outputs must be reviewed and validated by qualified professionals before use in construction documents.
- Document the role of ML in the design process; maintain audit trails.

#### 10.3 Explainability Requirements

- Regulatory bodies may require explanations for design decisions (especially for code compliance and structural safety).
- Black-box models (deep neural networks) are difficult to explain. Prefer interpretable models (Random Forest, decision trees) for safety-critical applications.
- Use SHAP values, partial dependence plots, and attention visualization to explain model behavior.
- For generative models, provide constraint satisfaction scores alongside generated designs.

#### 10.4 Building Code Compliance of ML Outputs

- ML-generated designs are not automatically code-compliant. All generated layouts, structures, and systems must be checked against applicable codes.
- Do not represent ML outputs as code-compliant without explicit verification.
- ML can assist code compliance checking but should not be the sole authority.

#### 10.5 Professional Responsibility

- Architects and engineers have professional and legal obligations that cannot be delegated to ML.
- ML is a tool; professional judgment is the final authority.
- Training in ML literacy should be part of professional education.
- Firms should develop AI/ML use policies aligned with professional practice standards.

#### 10.6 Data Privacy

- Building data may contain personally identifiable information (occupant data, access patterns, energy usage).
- Construction site photos may capture worker faces and activities.
- Comply with GDPR, CCPA, and local privacy regulations when collecting and using AEC data.
- Anonymize data where possible; limit data retention; obtain consent for data collection.

---

### Key Takeaways for AEC Practitioners

1. **Start with the problem, not the model**: Define the design or engineering problem precisely before selecting an ML approach.
2. **Data is the bottleneck**: Invest in data collection, cleaning, and annotation. Without good data, no model will perform well.
3. **Use simulation to generate training data**: Parametric simulation (energy, structural, daylight) can generate thousands of training examples.
4. **Tabular models first**: For structured AEC data, XGBoost and Random Forest often outperform deep learning with less effort.
5. **Validate rigorously**: Use domain-appropriate cross-validation; test on projects not in the training set.
6. **Keep humans in the loop**: ML augments; it does not replace professional judgment.
7. **Deploy simply**: A FastAPI endpoint or Grasshopper component is often sufficient; avoid over-engineering the deployment.
8. **Monitor in production**: Track prediction quality and retrain when performance degrades.
9. **Document everything**: Training data, model version, validation results, and deployment configuration.
10. **Ethical awareness**: Understand bias, liability, and privacy implications of ML in AEC.


## cd-calculator

### Computational Design Calculator

> Python calculators for geometry analysis, structural checking, solar calculations, panel optimization, mesh analysis, material estimation, and fabrication cost estimation for AEC computational design

## Computational Design Calculator

### Calculator Overview

This skill provides **7 production-grade Python calculators** purpose-built for computational design workflows in Architecture, Engineering, and Construction (AEC). Each calculator is a standalone command-line tool that accepts domain-specific parameters and returns precise, well-formatted results.

All calculators share common design principles:

- **Human-readable output by default** with clear section headers, formatted tables, and summary statistics.
- **`--json` flag** on every calculator for structured machine-readable output, enabling pipeline integration with parametric design tools, Grasshopper scripts, Dynamo graphs, or custom automation.
- **Strict input validation** with meaningful error messages that guide the user toward correct usage.
- **SI units throughout** (millimeters for geometry, kilonewtons for forces, degrees for angles) with Imperial equivalents noted where relevant.
- **Deterministic calculations** based on published engineering formulas (Eurocode, ASCE, ASHRAE) so results can be cross-checked and audited.

#### Calculator Index

| # | Calculator | Script | Primary Domain |
|---|-----------|--------|---------------|
| 1 | Geometry Calculator | `geometry_calculator.py` | Cross-section properties |
| 2 | Structural Checker | `structural_checker.py` | Member sizing & verification |
| 3 | Solar Calculator | `solar_calculator.py` | Solar position & radiation |
| 4 | Panel Optimizer | `panel_optimizer.py` | Facade rationalization |
| 5 | Mesh Analyzer | `mesh_analyzer.py` | Mesh quality & topology |
| 6 | Material Estimator | `material_estimator.py` | Quantity takeoff & carbon |
| 7 | Fabrication Calculator | `fabrication_calculator.py` | CNC / 3D print / laser costing |

#### Directory Structure

```
cd-calculator/
  SKILL.md                          # This file
  references/
    formulas.md                     # Complete formula reference
  scripts/
    geometry_calculator.py          # Cross-section geometry
    structural_checker.py           # Beam/column/deflection checks
    solar_calculator.py             # Solar position & radiation
    panel_optimizer.py              # Panel clustering & waste
    mesh_analyzer.py                # OBJ mesh quality analysis
    material_estimator.py           # Material quantity takeoff
    fabrication_calculator.py       # Fabrication time & cost
```

---

### 1. Geometry Calculator

**Script:** `scripts/geometry_calculator.py`

Computes cross-section properties for common AEC shapes used in structural analysis, fabrication planning, and parametric design. All inputs are in millimeters; all outputs are in mm-based units (mm^2, mm^4, etc.).

#### Supported Shapes

| Shape | Description | Key Parameters |
|-------|------------|----------------|
| `rectangle` | Solid rectangular section | width, height |
| `circle` | Solid circular section | radius |
| `triangle` | Solid triangular section | base, height |
| `i-beam` | Standard I/H section | width, height, flange thickness, web thickness |
| `hollow-rect` | Rectangular hollow section (RHS) | width, height, wall thickness |
| `hollow-circle` | Circular hollow section (CHS) | outer radius, inner radius |
| `l-shape` | L-angle section | width, height, thickness |
| `t-shape` | T-section | width, height, flange thickness, web thickness |
| `polygon` | Arbitrary polygon | vertex coordinates |

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--shape` | string | -- | Shape type (required) |
| `--width` | float | mm | Overall width |
| `--height` | float | mm | Overall height |
| `--radius` | float | mm | Radius for circular sections |
| `--outer-radius` | float | mm | Outer radius for hollow circle |
| `--inner-radius` | float | mm | Inner radius for hollow circle |
| `--base` | float | mm | Base width for triangle |
| `--flange-thickness` | float | mm | Flange thickness for I-beam / T-shape |
| `--web-thickness` | float | mm | Web thickness for I-beam / T-shape |
| `--wall-thickness` | float | mm | Wall thickness for hollow sections |
| `--thickness` | float | mm | Leg thickness for L-shape |
| `--vertices` | string | mm | Comma-separated x,y pairs for polygon |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## Solid rectangle 300 x 500 mm
python geometry_calculator.py --shape rectangle --width 300 --height 500

## Circular section with 150 mm radius
python geometry_calculator.py --shape circle --radius 150

## Standard I-beam
python geometry_calculator.py --shape i-beam --width 200 --height 400 --flange-thickness 15 --web-thickness 10

## Hollow rectangular section
python geometry_calculator.py --shape hollow-rect --width 300 --height 300 --wall-thickness 12

## JSON output for pipeline integration
python geometry_calculator.py --shape rectangle --width 300 --height 500 --json
```

#### Sample Output

```
========================================
  GEOMETRY CALCULATOR - Rectangle
========================================

  Dimensions:
    Width  (b) :   300.00 mm
    Height (h) :   500.00 mm

  Section Properties:
    Area             :   150,000.00 mm²
    Perimeter        :     1,600.00 mm
    Centroid (x, y)  :   (150.00, 250.00) mm

  Second Moment of Area:
    Ix (about x-axis):   3,125,000,000.00 mm⁴
    Iy (about y-axis):   1,125,000,000.00 mm⁴

  Section Modulus:
    Sx               :    12,500,000.00 mm³
    Sy               :     7,500,000.00 mm³

  Radius of Gyration:
    rx               :       144.34 mm
    ry               :        86.60 mm
========================================
```

---

### 2. Structural Checker

**Script:** `scripts/structural_checker.py`

Performs quick structural sizing and verification checks for steel members based on simplified Eurocode 3 and ASCE 7 formulas. Designed for early-stage feasibility assessments, not detailed design.

#### Check Types

| Check | Description | Key Inputs |
|-------|------------|------------|
| `beam` | Bending capacity and section sizing | span, UDL, steel grade |
| `column` | Axial capacity and buckling check | axial load, height, steel grade |
| `deflection` | Serviceability deflection check | span, UDL, section properties |

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--check` | string | -- | Check type: beam, column, deflection |
| `--span` | float | mm | Beam span or effective length |
| `--load` | float | kN/m or kN | UDL for beams, axial for columns |
| `--steel-grade` | string | -- | S235, S275, S355 |
| `--height` | float | mm | Column height |
| `--buckling-length-factor` | float | -- | Effective length factor (default 1.0) |
| `--moment-of-inertia` | float | mm^4 | Section Ix for deflection check |
| `--section` | string | -- | Named section (e.g., IPE300) |
| `--deflection-limit` | string | -- | L/250, L/360, or custom (default L/250) |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## Size a beam: 6m span, 15 kN/m UDL, S355 steel
python structural_checker.py --check beam --span 6000 --load 15 --steel-grade S355

## Check a column: 2000 kN axial, 4m height, S355
python structural_checker.py --check column --load 2000 --height 4000 --steel-grade S355

## Deflection check with named section
python structural_checker.py --check deflection --span 8000 --load 10 --section IPE300
```

#### Sample Output

```
========================================
  STRUCTURAL CHECKER - Beam Sizing
========================================

  Input:
    Span             :  6,000 mm (6.00 m)
    UDL              :  15.00 kN/m
    Steel Grade      :  S355 (fy = 355 MPa)

  Bending Analysis:
    Max Moment (M)   :  67.50 kN·m
    Required Sx      :  190,141 mm³
    Suggested Section:  IPE 270 (Sx = 429,000 mm³)

  Shear Analysis:
    Max Shear (V)    :  45.00 kN
    Shear Utilization:  0.12  [OK]

  Deflection:
    Max Deflection   :  10.82 mm
    Limit (L/250)    :  24.00 mm
    Utilization      :  0.45  [OK]

  Overall Status:    PASS
========================================
```

---

### 3. Solar Calculator

**Script:** `scripts/solar_calculator.py`

Computes solar geometry, shadow projections, and photovoltaic parameters for any location on Earth at any date and time. Essential for daylighting analysis, shadow studies, and PV system sizing in early-stage design.

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--latitude` | float | deg | Site latitude (-90 to 90) |
| `--longitude` | float | deg | Site longitude (-180 to 180) |
| `--date` | string | -- | Date in YYYY-MM-DD format |
| `--time` | string | -- | Solar time in HH:MM format |
| `--annual-summary` | flag | -- | Monthly solar data summary |
| `--shadow-analysis` | flag | -- | Shadow length computation |
| `--object-height` | float | m | Object height for shadow analysis |
| `--pv-tilt` | flag | -- | Optimal PV tilt calculation |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## Solar position for London at noon on summer solstice
python solar_calculator.py --latitude 51.5 --longitude -0.12 --date 2025-06-21 --time 12:00

## Annual summary for Dubai
python solar_calculator.py --latitude 25.2 --longitude 55.3 --annual-summary

## Shadow analysis for a 30m building in New York
python solar_calculator.py --latitude 40.7 --longitude -74.0 --shadow-analysis --object-height 30

## Optimal PV tilt for Berlin
python solar_calculator.py --latitude 52.5 --longitude 13.4 --pv-tilt
```

#### Sample Output

```
========================================
  SOLAR CALCULATOR - Position
========================================

  Location:
    Latitude         :   51.500° N
    Longitude        :   -0.120° W
    Date             :   2025-06-21

  Solar Position at 12:00:
    Altitude         :   62.07°
    Azimuth          :  180.00° (South)

  Day Information:
    Sunrise          :   03:43 solar time
    Sunset           :   20:21 solar time
    Day Length       :   16h 38m

  Shadow (per 1m object):
    Shadow Length    :    0.53 m
    Shadow Direction :    0.00° (North)
========================================
```

---

### 4. Panel Optimizer

**Script:** `scripts/panel_optimizer.py`

Rationalizes facade panel inventories by clustering similar panel dimensions within a configurable tolerance, then estimates material waste and cost impacts. Critical for design-for-manufacture workflows in curtain wall and cladding systems.

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--panels` | string | mm | Comma-separated WxH panel dimensions |
| `--tolerance` | float | mm | Grouping tolerance (default 10) |
| `--sheet-width` | float | mm | Raw sheet/stock width |
| `--sheet-height` | float | mm | Raw sheet/stock height |
| `--cost-per-unique` | float | $ | Cost premium per unique type (default 500) |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## Basic panel clustering
python panel_optimizer.py --panels "1200x800,1200x810,1205x800,1200x800,1190x795,1200x800,2400x800,2400x810"

## With sheet size for waste estimation
python panel_optimizer.py --panels "1200x800,1200x810,1205x800" --tolerance 15 --sheet-width 3000 --sheet-height 2000

## Cost-focused analysis
python panel_optimizer.py --panels "1200x800,1200x810,1205x800,1500x900,1510x895" --cost-per-unique 750
```

#### Sample Output

```
========================================
  PANEL OPTIMIZER - Clustering
========================================

  Input Summary:
    Total Panels     :   8
    Raw Unique Sizes :   5
    Tolerance        :  10 mm

  Panel Families:
    Family 1 (1200 x 800 mm):
      Members: 1200x800, 1200x810, 1205x800, 1190x795, 1200x800, 1200x800
      Count: 6
    Family 2 (2400 x 800 mm):
      Members: 2400x800, 2400x810
      Count: 2

  Rationalization:
    Unique types (before) :   5
    Unique types (after)  :   2
    Reduction             :  60.0%

  Cost Impact:
    Uniqueness premium    :  $1,000.00
    Savings vs. raw       :  $1,500.00
========================================
```

---

### 5. Mesh Analyzer

**Script:** `scripts/mesh_analyzer.py`

Evaluates mesh quality and topological properties for architectural meshes. Reads standard OBJ files or accepts inline vertex/face data. Essential for assessing mesh suitability for FEA, fabrication unfolding, and rendering.

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--file` | string | -- | Path to OBJ file |
| `--vertices` | string | -- | Inline vertices: "x,y,z;x,y,z;..." |
| `--faces` | string | -- | Inline faces: "i,j,k;i,j,k;..." |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## Analyze an OBJ file
python mesh_analyzer.py --file model.obj

## Analyze inline mesh data (a simple quad split into two triangles)
python mesh_analyzer.py --vertices "0,0,0;1,0,0;1,1,0;0,1,0" --faces "0,1,2;0,2,3"

## JSON output
python mesh_analyzer.py --file facade_mesh.obj --json
```

#### Sample Output

```
========================================
  MESH ANALYZER
========================================

  Topology:
    Vertices         :       4
    Faces            :       2
    Edges            :       5
    Euler Char. (V-E+F):    1
    Genus            :       0
    Is Manifold      :     Yes
    Boundary Edges   :       4

  Face Area Statistics:
    Min Area         :   0.500 units²
    Max Area         :   0.500 units²
    Mean Area        :   0.500 units²
    Std Dev          :   0.000 units²
    Total Area       :   1.000 units²

  Aspect Ratio Statistics:
    Min              :   1.000
    Max              :   1.414
    Mean             :   1.207
    Faces > 3.0      :       0  (0.0%)

  Normal Consistency  :   PASS (all normals consistent)

  Bounding Box:
    X range          :   0.000 to 1.000 (1.000)
    Y range          :   0.000 to 1.000 (1.000)
    Z range          :   0.000 to 0.000 (0.000)
========================================
```

---

### 6. Material Estimator

**Script:** `scripts/material_estimator.py`

Estimates material quantities, weights, and embodied carbon for buildings at the early design stage. Operates in two modes: **parametric** (from building type and GFA) or **direct** (from explicit material quantities).

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--building-type` | string | -- | residential, office, industrial, retail |
| `--gfa` | float | m^2 | Gross floor area |
| `--floors` | int | -- | Number of floors |
| `--concrete-volume` | float | m^3 | Direct concrete volume |
| `--steel-ratio` | float | kg/m^3 | Reinforcement ratio |
| `--glass-area` | float | m^2 | Direct glass area |
| `--timber-volume` | float | m^3 | Direct timber volume |
| `--waste-factor` | float | -- | Override waste factor (e.g. 1.10) |
| `--include-embodied-carbon` | flag | -- | Calculate embodied carbon |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## Parametric estimate for a residential building
python material_estimator.py --building-type residential --gfa 5000 --floors 8

## Direct material quantities with embodied carbon
python material_estimator.py --concrete-volume 450 --steel-ratio 120 --glass-area 2000 --include-embodied-carbon

## Office building with custom waste factor
python material_estimator.py --building-type office --gfa 12000 --floors 20 --waste-factor 1.12 --include-embodied-carbon
```

#### Sample Output

```
========================================
  MATERIAL ESTIMATOR - Parametric
========================================

  Building Parameters:
    Type             :  Residential
    Gross Floor Area :  5,000.00 m²
    Floors           :       8
    Floor Area/Floor :    625.00 m²

  Material Quantities (incl. waste):
    Concrete         :    750.00 m³  (1,800.00 tonnes)
    Rebar Steel      :     67.50 tonnes
    Structural Steel :     50.00 tonnes
    Glass            :    500.00 m²  (6.25 tonnes)
    Timber           :     75.00 m³  (33.75 tonnes)

  Total Weight       :  1,957.50 tonnes

  Embodied Carbon:
    Concrete         :  187,500 kgCO2e
    Rebar Steel      :  101,250 kgCO2e
    Structural Steel :   75,000 kgCO2e
    Glass            :    6,875 kgCO2e
    Timber           :  -10,125 kgCO2e (carbon stored)
    ─────────────────────────────────
    Total            :  360,500 kgCO2e
    Per m² GFA       :    72.10 kgCO2e/m²
========================================
```

---

### 7. Fabrication Calculator

**Script:** `scripts/fabrication_calculator.py`

Estimates fabrication time and cost for three digital fabrication processes: CNC milling, FDM 3D printing, and laser cutting. Uses industry-standard feed rates, material costs, and process parameters.

#### Parameters

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `--process` | string | -- | cnc-milling, 3d-print, laser-cut |
| `--path-length` | float | mm | CNC tool path length |
| `--tool-changes` | int | -- | Number of CNC tool changes |
| `--material` | string | -- | Material type (varies by process) |
| `--feed-rate` | float | mm/min | Override default feed rate |
| `--volume` | float | cm^3 | 3D print volume |
| `--height` | float | mm | 3D print height |
| `--layer-height` | float | mm | 3D print layer height |
| `--infill` | float | % | 3D print infill (default 20) |
| `--cut-length` | float | mm | Laser cut total path length |
| `--thickness` | float | mm | Material thickness for laser |
| `--hourly-rate` | float | $/hr | Machine/labor rate (default 75) |
| `--json` | flag | -- | Output as JSON |

#### Example Usage

```bash
## CNC milling job in wood
python fabrication_calculator.py --process cnc-milling --path-length 5000 --tool-changes 3 --material wood

## 3D print estimate
python fabrication_calculator.py --process 3d-print --volume 500 --height 200 --layer-height 0.2

## Laser cutting acrylic
python fabrication_calculator.py --process laser-cut --cut-length 8000 --material acrylic --thickness 6

## Custom hourly rate
python fabrication_calculator.py --process cnc-milling --path-length 12000 --tool-changes 5 --material aluminum --hourly-rate 120
```

#### Sample Output

```
========================================
  FABRICATION CALCULATOR - CNC Milling
========================================

  Process Parameters:
    Material         :  Wood (Hardwood)
    Path Length       :  5,000.00 mm
    Feed Rate        :  3,000 mm/min
    Tool Changes     :       3
    Change Time      :    2.00 min each

  Time Estimate:
    Cutting Time     :    1.67 min
    Tool Change Time :    6.00 min
    Setup Time       :   15.00 min
    Total Time       :   22.67 min (0.38 hr)

  Cost Estimate:
    Machine Time     :   $28.33
    Material (est.)  :   $15.00
    ─────────────────────────────
    Total            :   $43.33

========================================
```

---

### Usage Notes

#### Integration with Parametric Tools

All calculators support `--json` output for integration with parametric design pipelines:

```python
import subprocess, json

result = subprocess.run(
    ["python", "geometry_calculator.py", "--shape", "rectangle",
     "--width", "300", "--height", "500", "--json"],
    capture_output=True, text=True
)
data = json.loads(result.stdout)
area = data["area"]
```

#### Chaining Calculators

Calculators can be chained for multi-step workflows. For example, compute section properties, then verify structural adequacy:

```bash
## Step 1: Get section properties
python geometry_calculator.py --shape i-beam --width 200 --height 400 \
  --flange-thickness 15 --web-thickness 10 --json > section.json

## Step 2: Check deflection with computed Ix
python structural_checker.py --check deflection --span 8000 --load 10 \
  --moment-of-inertia 198540000
```

#### Error Handling

All calculators validate inputs and return meaningful error messages:

```
ERROR: --radius must be a positive number.
ERROR: --shape 'hexagon' is not supported. Choose from: rectangle, circle, triangle,
       i-beam, hollow-rect, hollow-circle, l-shape, t-shape, polygon.
ERROR: --inner-radius (160 mm) must be less than --outer-radius (150 mm).
```

Exit codes: `0` for success, `1` for input errors, `2` for computation errors.

#### Units Convention

| Quantity | Unit | Notes |
|----------|------|-------|
| Length / dimensions | mm | All geometry inputs |
| Area | mm^2 | Cross-section areas |
| Volume (geometry) | mm^3 | Section volumes per unit length |
| Moment of inertia | mm^4 | Second moment of area |
| Section modulus | mm^3 | Elastic section modulus |
| Force | kN | Structural loads |
| Stress | MPa (N/mm^2) | Steel yield, concrete fck |
| Moment | kN*m | Bending moments |
| Angle | degrees | Solar angles, bearings |
| Building area | m^2 | GFA, floor areas |
| Material volume | m^3 | Concrete, timber |
| Mass | tonnes (1000 kg) | Material weights |
| Carbon | kgCO2e | Embodied carbon |
| Fabrication length | mm | Tool paths, cut lengths |
| Cost | $ (currency units) | Fabrication costs |
| Time | minutes | Fabrication time |

---

### Formula Reference

For the complete mathematical formulas behind every calculation, see `references/formulas.md`. This includes derivations, source standards, and unit conversion tables.

---

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-23 | Initial release with 7 calculators |
