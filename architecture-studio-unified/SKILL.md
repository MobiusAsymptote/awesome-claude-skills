---
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
---

# Architecture Studio — Complete AEC Skill Framework

A unified, local-first framework for architecture firms to standardize AI-assisted workflows. This master skill consolidates **46+ professional capabilities** across product research, project management, site & regulatory analysis, and design operations.

Created by Federico Negro (2026), Alpaca Design Lab LLC. MIT-licensed.

---

## Quick Navigation

**Dispatch on keywords or use the full skill name:**

### 📊 **EPD & Product Data** (8 skills)
- **`epd-parser`** — Extract GWP, impact metrics from EPD PDFs
- **`epd-research`** — Search & find industry-standard EPDs
- **`epd-compare`** — Compare GWP and environmental metrics across products
- **`epd-to-spec`** — Write spec language from EPD data
- **`product-research`** — Research building products by category or brand
- **`product-data-import`** — Import & normalize product datasets
- **`product-data-cleanup`** — Clean messy product data into standard schema
- **`product-spec-pdf-parser`** — Extract specs from manufacturer PDFs

### 🏗️ **Project Management** (8 skills)
- **`master-schedule`** — Create & manage project timelines (CSV-based)
- **`meeting-minutes`** — Template & structure meeting documentation
- **`site-visit-report`** — Document site conditions & findings
- **`project`** — Initialize & manage project workspace (records, templates, context)
- **`tasklist`** — Create task lists & assignment tracking
- **`timetracker`** — Log project time by phase/discipline
- **`workplan`** — Plan phases, deliverables, resource allocation
- **`studio`** — Set up firm-wide studio workspace & preferences

### 🗽 **NYC Zoning & Regulatory** (8 skills)
- **`nyc-bsa`** — Board of Standards & Appeals: variances, appeals, precedent
- **`nyc-landmarks`** — Landmarks Preservation Commission rules & procedures
- **`nyc-dob-permits`** — NYC DOB permit types, filing requirements, timelines
- **`nyc-dob-violations`** — Search & interpret DOB violation records
- **`nyc-hpd`** — Housing Preservation Dept.: registrations, violations, compliance
- **`nyc-acris`** — ACRIS property transaction & deed data
- **`nyc-property-report`** — Generate property reports: zoning, lot, tax info
- **`zoning-analysis-nyc`** — Zoning compliance, FAR, use groups, restrictions

### 🌍 **Site & Environmental Analysis** (7 skills)
- **`demographics-analysis`** — Census data, neighborhood profiles, market analysis
- **`environmental-analysis`** — Site remediation, flood risk, environmental assessment
- **`mobility-analysis`** — Transit, walkability, commute patterns
- **`occupancy-calculator`** — Egress, occupancy load, life safety compliance
- **`site-history`** — Property history, prior uses, ownership records
- **`zoning-envelope`** — FAR modeling, massing envelope generation
- **`workplace-programmer`** — Space programming by use type & occupancy

### 🎨 **Design & Specification** (9 skills)
- **`spec-writer`** — Write CSI-formatted specifications (2-part, 3-part)
- **`slide-deck-generator`** — Create presentation decks from structured content
- **`color-palette-generator`** — Design color schemes for interiors/branding
- **`product-match`** — Match finishes, colors, materials across vendors
- **`product-pair`** — Find compatible products (wood/finish combos, etc.)
- **`product-enrich`** — Add images, specs, sourcing to product records
- **`product-image-processor`** — Resize, optimize product images for specs/web
- **`resize-images`** — Batch image resizing & format conversion
- **`studio-feedback`** — Evaluate design work against studio standards

### 📈 **Data & Schema Management** (5 skills)
- **`csv-to-sif`** — Convert product CSVs to Sustainability Initiatives Framework
- **`sif-to-csv`** — Export SIF data back to spreadsheet format
- **`product-spec-bulk-fetch`** — Download specs in bulk from manufacturer APIs
- **`tool-catalog`** — Maintain & search firm's tool & software inventory
- **`learn`** — Learn by example: browse templates, examples, sandbox projects

### 🛠️ **Infrastructure & Governance** (2 skills)
- **`skill-maker`** — Create, validate, test new custom skills for your firm
- **`skill-creator-advanced`** — Optimize & benchmark skill performance

---

## How to Use This Unified Skill

### Option 1: Direct Dispatch by Name
State the skill name and task:
```
Use epd-parser to extract GWP from this EPD PDF.
Use master-schedule to create a project timeline.
Use nyc-zoning-analysis to check lot coverage.
```

### Option 2: Describe Your Task (Smart Routing)
Describe what you need; this skill routes to the right tool:
```
I need to compare environmental impact between these 3 concrete products.
→ Routes to: epd-compare

I want to set up a new project with phases and deliverables.
→ Routes to: project + workplan + master-schedule

What's the zoning for this Manhattan lot?
→ Routes to: nyc-property-report + zoning-analysis-nyc
```

### Option 3: Chaining Skills
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

## Core Concepts Across All Skills

### 1. **Local-First Data Storage**
- **Studio workspace**: Firm-wide shared data in `~/.as/studio/`
- **Project workspaces**: Project-specific records in `<project-root>/`
- **Portable CSV**: All tabular data uses standardized CSV contracts (epd, ffe, schedule, etc.)
- **No cloud sync**: Records stay local; you control distribution

### 2. **Data Schemas & Contracts**
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

### 3. **CSI & Professional Formatting**
Specs and technical documentation follow CSI standards:
- **2-part specs**: General + Technical (concise)
- **3-part specs**: General + Products + Execution (detailed)
- **Proper terminology**: Consistent material names, abbreviations, units
- **Citations**: Track product sources, EPDs, test standards

### 4. **Governance & Rules**
Every output is validated against firm standards:
- **Terminology rules**: Consistent naming (e.g., "ReadyMix Concrete" not "ready mix" or "RMC")
- **Units & measurements**: Imperial (US), metric, or both with conversion
- **Professional disclaimers**: Liability language for regulatory/structural advice
- **Output formatting**: Markdown, CSI, or spreadsheet
- **Code citations**: Proper reference formatting (IBC, NYC Building Code, ASTM, ISO, etc.)

### 5. **Multi-Product & Bulk Operations**
Skills handle single items and bulk batches:
- **EPD parser**: One PDF or a whole folder (processes each separately)
- **Product import**: Single item or 100-row CSV (normalized automatically)
- **Image processor**: One image or batch resizing
- **Bulk spec fetch**: Single product or batch download from manufacturers

---

## Skill Groups Explained

### EPD & Sustainability (8 skills)
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

### Project Management (8 skills)
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

### NYC Zoning & Regulatory (8 skills)
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

### Site & Environmental Analysis (7 skills)
**Use case:** Understand neighborhood context, check site constraints, calculate occupancy & egress.

- **demographics-analysis**: Census data, population, income, household composition, employment. Contextualizes location for market feasibility or community engagement.
- **environmental-analysis**: Site environmental constraints: flood zone (FEMA), contamination risk, vapor intrusion, environmental justice, CEQR screening (if in NYC). Flags remediation needs.
- **mobility-analysis**: Transit access (subway, bus), bike infrastructure, walkability score, parking supply. Contextualizes commute patterns.
- **occupancy-calculator**: Life-safety calculations per NYC Building Code (or IBC). Calculates: occupant load by use type (sq ft per person), egress width requirements (0.15 sq in. per person stairwell, 0.1 sq in. doors), stair count, emergency lighting, accessible routes.
- **site-history**: Property history: prior uses, demolitions, ownership chains, historical documents. Useful for contamination assessment or context narrative.
- **zoning-envelope**: Massing envelopes for a lot. Applies FAR limit, setback rules, lot coverage. Shows maximum buildable volume given zoning.
- **workplace-programmer**: Space program generation. Inputs occupancy or org chart; outputs: sq ft per department, total program, common areas, phasing.

**Common workflow:** Address → demographics + environmental + mobility → zoning-envelope for massing → occupancy-calculator for egress → workplace-programmer for space planning

### Design & Specification (9 skills)
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

### Data & Schema Management (5 skills)
**Use case:** Manage firm data, export to different formats, catalog tools & resources.

- **csv-to-sif**: Convert product data CSV to Sustainability Initiatives Framework (SIF) format. Standardizes environmental data for LEED, Embodied Carbon reporting.
- **sif-to-csv**: Export SIF data back to spreadsheet for analysis, filtering, or re-import to other tools.
- **product-spec-bulk-fetch**: Bulk-download product specs from manufacturer websites (if APIs available). Saves manual PDF hunting.
- **tool-catalog**: Maintains firm's tool & software inventory. Tracks: software name, version, licenses (seats, expiration), cost, purpose, team owner.
- **learn**: Browse templates, examples, sandbox projects. Onboard new team members. Explore Architecture Studio patterns & conventions.

### Infrastructure (2 skills)
- **skill-maker**: Create custom skills for your firm. Templates, validation, testing framework. Turn firm workflows into reusable AI tools.
- **skill-creator-advanced** (implied): Optimize & benchmark skill performance. Runs evals, measures accuracy, suggests improvements.

---

## Data & File Conventions

All skills follow these conventions for **portability** and **interoperability**:

### Workspace Structure
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

### CSV Schemas (Import/Export)
All CSV data uses documented schemas:
- **EPD Schema** (`epd-library.csv`): 42 columns — GWP, ODP, AP, EP, POCP, resource use, metadata
- **FF&E Schema** (`product-library.csv`): 33 columns — product name, category, manufacturer, finish, cost, specs, certifications
- **Schedule Schema** (`master-schedule.csv`): phases, tasks, start/end, duration, dependencies, % complete, assignee
- **Meeting Minutes** (Markdown template) — attendees, agenda, decisions, actions, next meeting

Schemas ensure data portability across skills.

---

## Triggering This Skill

This unified skill activates on:

### Explicit Skill Names
```
Use epd-parser to…
Run product-research on…
Launch master-schedule for…
```

### Keywords by Domain
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

### Full Descriptions
*"I need to set up a new NYC commercial project with regulatory checks and a schedule."*
→ Routes to: project init → nyc-property-report → zoning-analysis-nyc → workplan → master-schedule

---

## Key Features

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

## Getting Started

1. **Review available skills**: Ask *"What skills are available?"* — this file lists all 46+.
2. **Choose a domain**: Pick a workflow (project setup, product specification, zoning analysis).
3. **Invoke a skill by name**: *"Use master-schedule to create a timeline for phases Design, BD, DD, CD, Permit."*
4. **Chain skills**: Skills reference each other; follow the suggested workflows above.
5. **Explore templates**: Use **`learn`** skill to browse examples & sandbox projects.
6. **Customize**: Use **`skill-maker`** to create firm-specific tools (e.g., a standard site-visit template).

---

## Support & Attribution

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

## Consolidated Skill Reference (46 Skills)

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
