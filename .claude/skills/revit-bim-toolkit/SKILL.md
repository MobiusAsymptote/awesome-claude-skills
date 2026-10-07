---
name: revit-bim-toolkit
description: >
  Revit BIM automation toolkit — 25 routed skills in one file covering Dynamo Python and
  Revit API code generation, model auditing and parameter validation, clash detection,
  room/area analysis, schedules, Excel and IFC export, parameter and workset management,
  batch renaming and element editing, view filters, project and sheet setup, and Autodesk
  Construction Cloud (APS) API workflows. Load at the start of any Revit automation, QA,
  data, or ACC task; find the matching skill in the router table and follow its section.
source: https://github.com/Utopia5327/claude-plugin-for-revit-bim (MIT, Manas Bhatia)
version: 1.0
---

# Revit BIM Toolkit — 25 skills, one file

Compiled from Utopia5327/claude-plugin-for-revit-bim v1.0 (MIT). Skills generate Dynamo Python (IronPython 2.7 / Dynamo 2.x) or C#/pyRevit code; pair with a live Revit MCP connector for two-way interaction.

## Router

Match the user's request to a skill, then jump to its section.

| Skill | Use when |
|---|---|
| **Scripting & code generation** | |
| [generate-dynamo](#generate-dynamo) | Generate a complete, ready-to-run Dynamo Python script for Autodesk Revit from plain language. |
| [export-dynamo-file](#export-dynamo-file) | Generate a ready-to-open Dynamo graph file (.dyn) for Revit — not just code to paste, but an actual .dyn file the user can double-click and run immediately in Dynamo. |
| [revit-api-code](#revit-api-code) | Generate Revit API code in C# or Python for macros, external commands, add-ins, or pyRevit scripts — production-ready, beyond what Dynamo can do. |
| **Model QA & coordination** | |
| [query-model](#query-model) | Query, filter, list, and extract data from a Revit model database using Dynamo Python. |
| [audit-model](#audit-model) | Audit and analyze Revit model health, quality, and BIM standards compliance. |
| [validate-parameters](#validate-parameters) | Validate that required Revit element parameters are filled in, non-empty, and within acceptable values — then generate a compliance report. |
| [linked-model-check](#linked-model-check) | Check the status, coordinates, and health of all RVT and CAD linked files in a Revit model. Generates a coordination report showing which links are loaded, unloaded, missing, or have coordinate mismatches. |
| [workset-manager](#workset-manager) | Audit workset assignments across a Revit model, identify elements on the wrong workset, and move elements between worksets using Dynamo Python. |
| [clash-detection](#clash-detection) | Detect and report geometric clashes and interferences between Revit model elements using Dynamo Python and the Revit API's Boolean intersection tools. |
| **Rooms, schedules & export** | |
| [analyze-rooms](#analyze-rooms) | Analyze rooms, spaces, and areas in a Revit model — GIA calculations, space program comparison, department breakdowns, unbounded/unplaced room audits, and CSV export. |
| [create-schedule](#create-schedule) | Create, configure, or automate Revit schedules, quantity takeoffs, and material takeoffs using Dynamo Python. |
| [export-to-excel](#export-to-excel) | Export Revit model data — element parameters, room data, door/window schedules, family instances, or any category — to a CSV or Excel-compatible file using Dynamo Python. |
| [export-ifc](#export-ifc) | Export a Revit model to IFC format with proper settings, class mapping, and property sets using Dynamo Python. |
| **Parameters & element editing** | |
| [manage-parameters](#manage-parameters) | Read, write, batch-update, or validate Revit element parameters using Dynamo Python. |
| [shared-parameters](#shared-parameters) | Create, bind, and manage Revit shared parameters using Dynamo Python — load a shared parameter file, add new parameter definitions to groups, bind parameters to element categories, and verify parameter bindings. |
| [batch-rename-elements](#batch-rename-elements) | Batch rename Revit elements across any category using prefixes, suffixes, numbering sequences, or parameter-driven naming rules. |
| [manipulate-elements](#manipulate-elements) | Move, rotate, copy, delete, modify types, or batch-edit Revit model elements using Dynamo Python. |
| [create-view-filters](#create-view-filters) | Create, configure, and apply Revit view filters and graphic overrides using Dynamo Python. |
| **Project & sheet setup** | |
| [project-setup](#project-setup) | Automate Revit project setup — create worksets, levels, grids, view templates, browser organization schemes, and standard views from a project brief or BIM Execution Plan. |
| [manage-sheets](#manage-sheets) | Create, organise, and manage Revit drawing sheets and views using Dynamo Python. Use this skill when creating sheets from a list (e.g. |
| **Autodesk Construction Cloud (APS)** | |
| [acc-api-setup](#acc-api-setup) | Set up Python authentication and a reusable client for the Autodesk Platform Services (APS) API to access Autodesk Construction Cloud (ACC). |
| [acc-docs](#acc-docs) | Manage Autodesk Construction Cloud (ACC) Docs — list folders and files, upload documents, download files, create folder structures, manage transmittals, reviews, and packages via the APS Data Management API and ACC Docs . |
| [acc-coordinate](#acc-coordinate) | Work with Autodesk Construction Cloud (ACC) Coordinate — list and inspect model sets, retrieve clash results, create clash issues, manage model activation for coordination, and export coordination reports via the APS Mod. |
| [acc-design-collaboration](#acc-design-collaboration) | Guide Revit ↔ ACC Design Collaboration workflows — setting up cloud worksharing, creating and consuming design packages, shared views, Design Collaboration setup, model publishing, and Revit cloud model best practices. |
| [acc-reports](#acc-reports) | Export ACC project data to CSV or Excel — issues, RFIs, document logs, clash summaries, transmittals, and project activity reports — using the APS REST API with Python. |


---

# Scripting & code generation


## generate-dynamo

> Generate a complete, ready-to-run Dynamo Python script for Autodesk Revit from plain language. Use this skill whenever a Revit user, architect, or BIM manager asks to automate anything in Revit — renaming elements, filtering by parameters, exporting data, modifying families, checking model health, batch-editing anything, or any other scripting task. Trigger on phrases like "write a Dynamo script", "create a script for Revit", "automate in Revit", "Dynamo Python", or whenever someone describes a repetitive Revit workflow that would benefit from automation — even if they don't say the word "script". Proactively offer to generate a script when you detect a tedious manual workflow.

## Generate Dynamo Script

Generate a complete, ready-to-use Dynamo Python script for Revit based on:

**"$ARGUMENTS"**

### Before writing code

Make sure you understand:
1. **What elements** are involved? (walls, rooms, doors, families, sheets, views, etc.)
2. **What action** needs to happen? (read, rename, filter, export, create, modify, etc.)
3. **Which parameters** are involved? Ask for exact names if mentioned — they're case-sensitive.
4. **What's the desired output?** (modified model, printed list, CSV file, count, etc.)

If the request is ambiguous, ask **one focused question** before proceeding. Architects are busy.

### Output format

Always structure the response in this exact order:

#### 1. What this script does (2–4 sentences)
Plain English. No jargon. If it modifies the model, say so clearly. If it's read-only, reassure them.

#### 2. How to use it
Numbered steps:
1. Open Dynamo (Manage → Dynamo)
2. Create a new graph, place a **Python Script** node
3. Paste the code into the node
4. Connect any Dynamo inputs (explain what each `IN[0]`, `IN[1]` should be)
5. Click **Run**

#### 3. The script
Complete, runnable code in a `python` code block. See writing guidelines below.

#### 4. Customization tips (optional)
Call out obvious tweaks: parameter names, output paths, category filters, date formats, etc.

---

### Script writing guidelines

#### Default: IronPython 2.7 (Dynamo 2.x)
Most firms are on Dynamo 2.x. Switch to CPython 3 only if the user asks for Dynamo 3+.
- IronPython: use `clr`, `TransactionManager`, no f-strings, `DisplayUnitType` for unit conversion
- CPython 3: f-strings OK, use `UnitTypeId` instead of `DisplayUnitType`

#### Standard boilerplate — always include

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

doc  = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
```

#### Transactions — required for any model modification

```python
TransactionManager.Instance.EnsureInTransaction(doc)
try:
    # ... your modifications ...
    TransactionManager.Instance.TransactionTaskDone()
except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    raise e
```

Read-only scripts (querying / exporting) don't need a transaction.

#### Accessing elements

```python
## All elements of a category
collector = FilteredElementCollector(doc) \
    .OfCategory(BuiltInCategory.OST_Rooms) \
    .WhereElementIsNotElementType() \
    .ToElements()

## Common BuiltInCategory values:
## Rooms:OST_Rooms  Walls:OST_Walls  Doors:OST_Doors  Windows:OST_Windows
## Floors:OST_Floors  Ceilings:OST_Ceilings  Stairs:OST_Stairs
## Sheets:OST_Sheets  Views:OST_Views  Levels:OST_Levels  Grids:OST_Grids
## StructuralColumns:OST_StructuralColumns  Families:OST_Families
```

#### Reading and writing parameters

```python
## Read
param = element.LookupParameter("Parameter Name")  # user-defined
param = element.get_Parameter(BuiltInParameter.ROOM_NUMBER)  # built-in
if param:
    value = param.AsString()    # text
    value = param.AsDouble()    # number (internal feet — convert!)
    value = param.AsInteger()   # integer / Yes-No (1/0)

## Write
param = element.LookupParameter("Parameter Name")
if param and not param.IsReadOnly:
    param.Set("new value")   # text
    param.Set(3.28084 * m)   # length in feet (Revit internal unit)
```

#### Unit conversion (IronPython)
Revit stores lengths in **decimal feet** internally.

```python
from Autodesk.Revit.DB import UnitUtils, DisplayUnitType
feet = UnitUtils.Convert(value_mm, DisplayUnitType.DUT_MILLIMETERS,
                          DisplayUnitType.DUT_DECIMAL_FEET)
mm   = UnitUtils.Convert(value_ft, DisplayUnitType.DUT_DECIMAL_FEET,
                          DisplayUnitType.DUT_MILLIMETERS)
## Simple shorthand: multiply feet × 304.8 to get mm
```

#### Error handling — always wrap the main logic

```python
try:
    # main logic
    OUT = result
except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

#### Always end with OUT

```python
OUT = result  # count, list, message, or data — give the user confirmation it worked
```

#### Comment generously
The person running this may not be a programmer. Explain what each block does and why.

---

### Quality checklist (run before every output)
- [ ] Correct imports for the Dynamo version?
- [ ] Transaction wrapper if the model is modified?
- [ ] Parameter names flagged as case-sensitive if uncertain?
- [ ] try/except with ForceCloseTransaction in the except?
- [ ] OUT = ... at the end?
- [ ] Comments on each key block?
- [ ] Unit conversions handled (feet ↔ mm)?
- [ ] Edge cases: null level, missing parameter, no elements found, exterior doors?


## export-dynamo-file

> Generate a ready-to-open Dynamo graph file (.dyn) for Revit — not just code to paste, but an actual .dyn file the user can double-click and run immediately in Dynamo. Use this skill whenever a user wants a Dynamo script saved as a file, wants to avoid copy-pasting code, asks "can you save it as a Dynamo file", "give me the .dyn file", "I want to open it directly in Dynamo", or "export the Dynamo graph". Also offer this proactively after generating a script if the user seems less technical or is asking for a "plug and play" solution. Produces IronPython 2.7 scripts by default (Dynamo 2.x compatible). If in Cowork or Claude Code with file system access, save directly to the user's machine. Otherwise, present the .dyn JSON for the user to save manually.

## Export Dynamo Graph File (.dyn)

Generate a complete, openable Dynamo `.dyn` file for:

**"$ARGUMENTS"**

### What this produces

A `.dyn` file is a Dynamo graph saved as JSON. When the user opens it in Dynamo
(File → Open or double-click), they get a ready-to-run graph with a Python Script node
pre-filled with the generated code — no manual node creation or copy-pasting required.

### Workflow

1. First, generate the Python script for the task (follow all guidelines from
   `generate-dynamo` skill — boilerplate imports, transactions, error handling, OUT=result).

2. Then wrap it in a valid `.dyn` file using the template below.

3. If you have file system access (Cowork / Claude Code), save the `.dyn` file
   directly to the user's desktop or a path they specify. Otherwise, output the
   complete JSON so they can save it manually as `scriptname.dyn`.

### .dyn file template

Build the JSON programmatically — never try to manually JSON-escape multi-line Python
code by hand. Instead, use Python's `json.dumps()` to produce the correct JSON string,
or build the structure as a dict and serialize it. Here is the canonical template:

```python
import json, uuid

## The Python script to embed (write the full script as a normal Python string here)
python_code = """
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    # --- generated logic here ---
    result = []
    OUT = result
except Exception as e:
    import traceback
    OUT = 'ERROR: ' + str(e) + '\\n' + traceback.format_exc()
""".strip()

## Unique IDs for the graph and nodes
graph_id   = str(uuid.uuid4())
node_id    = str(uuid.uuid4())

graph = {
    "Uuid": graph_id,
    "IsCustomNode": False,
    "Description": "Generated by revit-bim Claude plugin",
    "Name": "BIM Script",          # ← set to a meaningful name based on the task
    "ElementResolver": {"ResolutionMap": {}},
    "Inputs": [],
    "Outputs": [],
    "Nodes": [
        {
            "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
            "NodeType": "PythonScriptNode",
            "Code": python_code,    # json.dumps handles escaping automatically
            "Engine": "IronPython2",
            "EngineName": "IronPython2",
            "VariableInputPorts": True,
            "Id": node_id,
            "Inputs": [
                {
                    "Id": "in0",
                    "Name": "IN[0]",
                    "Description": "Input #0",
                    "UsingDefaultValue": False,
                    "Level": 2,
                    "UseLevels": False,
                    "KeepListStructure": False
                }
            ],
            "Outputs": [
                {
                    "Id": "out0",
                    "Name": "OUT",
                    "Description": "Result of the python script",
                    "UsingDefaultValue": False,
                    "Level": 2,
                    "UseLevels": False,
                    "KeepListStructure": False
                }
            ],
            "Replication": "Disabled",
            "Description": "Runs an embedded Python script."
        }
    ],
    "Connectors": [],
    "Dependencies": [],
    "NodeLibraryDependencies": [],
    "EnableLaceByDefault": True,
    "Bindings": [],
    "View": {
        "Dynamo": {
            "ScaleFactor": 1.0,
            "HasRunWithoutCrash": False,
            "IsVisibleInDynamoLibrary": True,
            "Version": "2.13.1.3887",
            "RunType": "Manual",
            "RunPeriod": "1000"
        },
        "Camera": {
            "Name": "Background Preview",
            "EyeX": -17.0, "EyeY": 24.0, "EyeZ": 50.0,
            "LookX": 12.0, "LookY": -13.0, "LookZ": -58.0,
            "UpX": 0.0, "UpY": 1.0, "UpZ": 0.0
        },
        "NodeViews": [
            {
                "Name": "Python Script",
                "ShowGeometry": True,
                "Id": node_id,
                "IsSetAsInput": False,
                "IsSetAsOutput": False,
                "Excluded": False,
                "X": 250.0,
                "Y": 100.0
            }
        ],
        "Annotations": [],
        "X": -100.0,
        "Y": -50.0,
        "Zoom": 1.0
    }
}

## Serialize to JSON with proper indentation and escaping
dyn_json = json.dumps(graph, indent=2, ensure_ascii=False)

## Save to file
output_path = r"C:\Users\YourName\Desktop\script_name.dyn"  # ← ask user or use a sensible default
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(dyn_json)

print("Saved: " + output_path)
```

### How to use it for a task

When the user asks for a `.dyn` file:

1. **Write the full Python script** for their task (use `generate-dynamo` guidelines).
2. **Plug it into `python_code`** in the template above.
3. **Set `"Name"`** in the graph dict to something descriptive (e.g. `"Rename Rooms by Level"`).
4. **Save the file:**
   - In Cowork: write the `.dyn` file directly to a path the user specifies, or default to their Desktop.
   - In Claude.ai / no filesystem: output the full JSON in a code block so they can save it as `filename.dyn`.
5. **Tell the user** how to open it: `File → Open` in Dynamo, or double-click if Dynamo is associated with `.dyn` files.

### Adding inputs (optional)

If the script uses `IN[0]`, `IN[1]`, etc., add corresponding input entries to the `"Inputs"`
list and `"NodeViews"` section, and mention in the response that the user needs to wire up
those input nodes (e.g. a String node for a parameter name, a Number node for a value).

For most scripts that collect directly from the document, no inputs are needed and `IN[0]`
can be left disconnected — the script won't use it.

### CPython 3 (Dynamo 3.x)

If the user specifies Dynamo 3 or CPython, change:
```json
"Engine": "CPython3",
"EngineName": "CPython3"
```
And update the script to use CPython syntax (f-strings OK, `UnitTypeId` for units).


## revit-api-code

> Generate Revit API code in C# or Python for macros, external commands, add-ins, or pyRevit scripts — production-ready, beyond what Dynamo can do. Use this skill when the user needs C# Revit macros, IExternalCommand boilerplate, .addin manifest files, pyRevit button scripts, or any code that runs outside of Dynamo. Trigger on phrases like "Revit macro", "external command", "add-in", "C# Revit", "pyRevit script", "Revit API code", "IExternalCommand", "ribbon button", "addin", or when a user asks for Revit automation that needs to be deployed as a standalone tool rather than a Dynamo graph. Also offer this when users want persistent tools that run without opening Dynamo each time.

## Generate Revit API Code

Generate Revit API code for:

**"$ARGUMENTS"**

### Clarify the target

Before writing code, confirm:
1. **C# or Python?**
   - C# → Revit macro (internal, `.cs` file in Revit's SharpDevelop IDE) or add-in (`.dll`)
   - Python → pyRevit script (`.py` file in a pyRevit extension bundle)
2. **Where will it run?**
   - Macro: runs from Manage → Macros, no installation needed
   - External command: compiled `.dll`, registered in `.addin` file
   - pyRevit: drop into extension folder, appears as ribbon button automatically
3. **Revit version?** Affects API availability.

---

### C# External Command (Add-in)

Complete, production-ready boilerplate for an `IExternalCommand`:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;

namespace RevitBIMPlugin
{
    [Transaction(TransactionMode.Manual)]
    [Regeneration(RegenerationOption.Manual)]
    public class MyCommand : IExternalCommand
    {
        public Result Execute(
            ExternalCommandData commandData,
            ref string message,
            ElementSet elements)
        {
            UIApplication uiapp = commandData.Application;
            UIDocument    uidoc = uiapp.ActiveUIDocument;
            Document      doc   = uidoc.Document;

            try
            {
                using (Transaction tx = new Transaction(doc, "My BIM Operation"))
                {
                    tx.Start();

                    // ── Your code here ────────────────────────────────
                    // Example: count all walls
                    var walls = new FilteredElementCollector(doc)
                        .OfCategory(BuiltInCategory.OST_Walls)
                        .WhereElementIsNotElementType()
                        .ToElements();

                    tx.Commit();

                    TaskDialog.Show("BIM Manager",
                        $"Operation completed. Found {walls.Count} walls.");
                }

                return Result.Succeeded;
            }
            catch (Exception ex)
            {
                message = ex.Message;
                return Result.Failed;
            }
        }
    }
}
```

**Corresponding `.addin` manifest** (save as `MyPlugin.addin` in `%AppData%\Autodesk\Revit\Addins\20XX\`):
```xml
<?xml version="1.0" encoding="utf-8"?>
<RevitAddIns>
  <AddIn Type="Command">
    <Name>My BIM Command</Name>
    <Assembly>C:\Path\To\MyPlugin.dll</Assembly>
    <FullClassName>RevitBIMPlugin.MyCommand</FullClassName>
    <ClientId>YOUR-GUID-HERE</ClientId>
    <VendorId>YOURINITIALS</VendorId>
    <VendorDescription>Your Company</VendorDescription>
  </AddIn>
</RevitAddIns>
```

---

### C# Revit Macro

For quick scripts run directly from Revit without compiling a DLL:

```csharp
// In Revit: Manage → Macros → Module → add this method
public void MyMacro()
{
    Document doc = this.ActiveUIDocument.Document;

    using (Transaction tx = new Transaction(doc, "Macro Operation"))
    {
        tx.Start();

        // ── Your code here ────────────────────────────────────────
        var rooms = new FilteredElementCollector(doc)
            .OfCategory(BuiltInCategory.OST_Rooms)
            .WhereElementIsNotElementType()
            .ToElements();

        TaskDialog.Show("Macro", $"Found {rooms.Count} rooms.");

        tx.Commit();
    }
}
```

---

### pyRevit Script (Python)

For ribbon button scripts using the pyRevit framework:

```python
## -*- coding: utf-8 -*-
"""BIM Manager — pyRevit Script.
tooltip: Brief description shown on hover
"""
from pyrevit import revit, DB, UI, script, forms

doc   = revit.doc
uidoc = revit.uidoc
output = script.get_output()

## ── Your code here ───────────────────────────────────────────────────────────
## Read elements
rooms = list(DB.FilteredElementCollector(doc)
             .OfCategory(DB.BuiltInCategory.OST_Rooms)
             .WhereElementIsNotElementType()
             .ToElements())

## Modify with transaction
with revit.Transaction('BIM Operation'):
    pass  # ← your modifications

## Output to pyRevit's output panel (supports HTML/markdown)
output.print_md('## Done!')
output.print_table(
    table_data=[[r.Number, r.get_Parameter(DB.BuiltInParameter.ROOM_NAME).AsString()]
                for r in rooms],
    columns=['Number', 'Name']
)
```

**pyRevit extension structure:**
```
MyExtension.extension/
├── MyPanel.panel/
│   └── MyButton.pushbutton/
│       ├── script.py        ← your code above
│       └── icon.png         ← 32×32 PNG
└── extension.json
```

---

### Useful API snippets

**Show a TaskDialog with user options:**
```csharp
TaskDialogResult result = TaskDialog.Show("Confirm",
    "This will modify all wall types. Proceed?",
    TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No);
if (result != TaskDialogResult.Yes) return Result.Cancelled;
```

**Select elements in the UI:**
```csharp
IList<Reference> refs = uidoc.Selection.PickObjects(
    ObjectType.Element, "Select elements to process");
var selected = refs.Select(r => doc.GetElement(r.ElementId)).ToList();
```

**Print to Output window (pyRevit):**
```python
output.print_md('**Found** {} walls'.format(len(walls)))
output.print_table(data, columns=['ID', 'Type', 'Length'])
```


---

# Model QA & coordination


## query-model

> Query, filter, list, and extract data from a Revit model database using Dynamo Python. Use this skill when a user wants to list elements, count elements by category, filter by parameter value, find elements meeting a condition, extract data for a report, or answer "how many X are in my model" type questions. Trigger on phrases like "list all", "filter elements", "find all walls", "get all rooms", "extract data", "how many", "show me all elements where", or any request to inspect or report on model content without modifying it. This skill produces read-only query scripts — safe on any model.

## Query Revit Model

Write a Dynamo Python script to query the Revit model for:

**"$ARGUMENTS"**

### Read-only query script template

No transaction needed — this script only reads data, it doesn't modify the model.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    # ── Build a filtered element collector ──────────────────────────────────
    # Modify the category or class filter to match what you need:
    collector = (FilteredElementCollector(doc)
                 .OfCategory(BuiltInCategory.OST_Walls)   # ← change category
                 .WhereElementIsNotElementType()
                 .ToElements())

    # ── Extract data from each element ──────────────────────────────────────
    results = []
    for el in collector:
        try:
            row = {
                'Id':       el.Id.IntegerValue,
                'Name':     el.Name if hasattr(el, 'Name') else 'N/A',
                'Category': el.Category.Name if el.Category else 'N/A',
                # Add more fields here, e.g.:
                # 'Mark': el.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString(),
                # 'Type': doc.GetElement(el.GetTypeId()).Name,
            }
            results.append(row)
        except Exception as row_e:
            results.append({'Id': el.Id.IntegerValue, 'Error': str(row_e)})

    OUT = results

except Exception as e:
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Common collector patterns

**Filter by parameter value:**
```python
matching = [el for el in collector
            if el.LookupParameter('Fire Rating')
            and el.LookupParameter('Fire Rating').AsString() == '2HR']
```

**Filter elements on a specific level:**
```python
from Autodesk.Revit.DB import ElementLevelFilter, ElementId
level_id = ElementId(12345)  # get this from LookupTable or Dynamo input
level_filter = ElementLevelFilter(level_id)
collector.WherePasses(level_filter)
```

**Get element type name:**
```python
type_id = el.GetTypeId()
if type_id != ElementId.InvalidElementId:
    type_name = doc.GetElement(type_id).Name
```

**Common BuiltInCategory values:**
```
OST_Walls       OST_Floors      OST_Roofs       OST_Ceilings
OST_Doors       OST_Windows     OST_Rooms       OST_Stairs
OST_Sheets      OST_Views       OST_Levels      OST_Grids
OST_StructuralColumns           OST_StructuralFraming
OST_DuctCurves  OST_PipeCurves  OST_Families
```

### Exporting query results to CSV

If the user wants to save the results:

```python
import csv
output_path = r'C:\Reports\query_output.csv'
if results:
    with open(output_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    OUT = ['Saved ' + str(len(results)) + ' rows to: ' + output_path, results]
```

Always mention the output path in customization tips so the user knows where to edit it.


## audit-model

> Audit and analyze Revit model health, quality, and BIM standards compliance. Use this skill when checking model file size, warning counts, element counts by category, redundant or in-place families, unused views, workset structure, model warnings, or any model performance or quality-control question. Trigger on phrases like "audit my model", "check model health", "how many warnings", "is my model clean", "model performance", "BIM QC", "quality check", or whenever someone wants a summary of what's in their Revit model. Proactively offer an audit when users mention slow model performance or submission deadlines.

## Revit Model Audit

Audit the Revit model for:

**"$ARGUMENTS"**

### Approach

Before scripting, clarify:
- Is this a **comprehensive health report** or a **targeted audit** (e.g. just warnings, just families)?
- Does the user want a **Dynamo script** to run inside Revit, or just guidance on what to look for?

Default to producing a complete Dynamo audit script unless the user asks otherwise.

### Comprehensive model health script

This read-only script collects a full health report — no model modifications, safe to run on any project.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument
report = {}

try:
    # ── 1. Project information ──────────────────────────────────────────────
    pi = doc.ProjectInformation
    report['Project Name']   = pi.Name
    report['Project Number'] = pi.Number
    report['Client']         = pi.ClientName
    report['Revit Version']  = doc.Application.VersionName

    # ── 2. Element counts by category ──────────────────────────────────────
    cats = [
        ('Walls',            BuiltInCategory.OST_Walls),
        ('Floors',           BuiltInCategory.OST_Floors),
        ('Roofs',            BuiltInCategory.OST_Roofs),
        ('Ceilings',         BuiltInCategory.OST_Ceilings),
        ('Doors',            BuiltInCategory.OST_Doors),
        ('Windows',          BuiltInCategory.OST_Windows),
        ('Rooms',            BuiltInCategory.OST_Rooms),
        ('Stairs',           BuiltInCategory.OST_Stairs),
        ('Struct. Columns',  BuiltInCategory.OST_StructuralColumns),
        ('Struct. Framing',  BuiltInCategory.OST_StructuralFraming),
        ('MEP Ducts',        BuiltInCategory.OST_DuctCurves),
        ('MEP Pipes',        BuiltInCategory.OST_PipeCurves),
        ('Levels',           BuiltInCategory.OST_Levels),
        ('Grids',            BuiltInCategory.OST_Grids),
    ]
    counts = {}
    for name, cat in cats:
        n = (FilteredElementCollector(doc)
             .OfCategory(cat)
             .WhereElementIsNotElementType()
             .GetElementCount())
        counts[name] = n
    report['Element Counts'] = counts

    # ── 3. Families ─────────────────────────────────────────────────────────
    families = list(FilteredElementCollector(doc).OfClass(Family).ToElements())
    report['Total Families']    = len(families)
    report['In-Place Families'] = sum(1 for f in families if f.IsInPlace)

    # ── 4. Views and sheets ─────────────────────────────────────────────────
    all_views = list(FilteredElementCollector(doc).OfClass(View).ToElements())
    sheets    = [v for v in all_views if isinstance(v, ViewSheet)]
    not_on_sheet = [v for v in all_views
                    if not isinstance(v, ViewSheet)
                    and not v.IsTemplate
                    and v.CanBePrinted]
    report['Total Views']       = len(all_views)
    report['Total Sheets']      = len(sheets)
    report['Printable Views']   = len(not_on_sheet)

    # ── 5. Model warnings ───────────────────────────────────────────────────
    warnings = list(doc.GetWarnings())
    report['Model Warnings'] = len(warnings)

    # ── 6. Worksets ─────────────────────────────────────────────────────────
    report['Is Workshared'] = doc.IsWorkshared
    if doc.IsWorkshared:
        wt = (FilteredWorksetCollector(doc)
              .OfKind(WorksetKind.UserWorkset)
              .ToWorksets())
        report['User Worksets'] = len(list(wt))

    OUT = report

except Exception as e:
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Interpreting results

Guide the user on what the numbers mean:

- **Warnings > 50**: investigate — common culprits are duplicate rooms, overlapping elements, unresolved references
- **In-place families > 10**: performance risk; recommend converting to loadable families
- **Warnings > 500**: flag as a model health issue requiring cleanup before submission
- **Printable views not on sheets**: opportunity to clean up unused views

### Targeted audit variants

If the user wants something specific, tailor the script:

- **Warnings only**: `doc.GetWarnings()` — iterate and group by `GetDescriptionText()`
- **Unused families**: compare `FilteredElementCollector(doc).OfClass(Family)` against `FilteredElementCollector(doc).OfClass(FamilyInstance)`
- **Linked files**: `FilteredElementCollector(doc).OfClass(RevitLinkInstance)`
- **Import CAD links**: `FilteredElementCollector(doc).OfClass(ImportInstance)`

### Output

Always recommend the user export the report to CSV or paste it into a spreadsheet for distribution:

```python
import csv, os
output_path = r'C:\Reports\model_audit.csv'
with open(output_path, 'w') as f:
    writer = csv.writer(f)
    for k, v in report.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                writer.writerow([k, sub_k, sub_v])
        else:
            writer.writerow([k, '', v])
OUT = 'Report saved to: ' + output_path
```


## validate-parameters

> Validate that required Revit element parameters are filled in, non-empty, and within acceptable values — then generate a compliance report. Use this skill for BEP (BIM Execution Plan) data validation, pre-submission QA checks, COBie data readiness, checking that all rooms have departments assigned, all doors have fire ratings, or any "are all my parameters filled in?" question. Trigger on phrases like "validate parameters", "check parameters", "missing parameters", "BEP compliance", "data completeness", "parameter QA", "are all fields filled", "COBie validation", "pre- submission check", "parameter audit", "empty parameters", or any request to verify that element data is complete and correct.

## Validate Revit Parameters

Run a BIM data completeness check for:

**"$ARGUMENTS"**

### Before writing code

Ask (one question if ambiguous):
1. **Which category and which parameters** must be filled? (e.g. all Rooms must have Name, Number, Department, Occupancy)
2. **What counts as valid?** Non-empty? A value from a specific list? A number above zero?
3. **Output format?** Dynamo OUT list, or also export to CSV?

Read-only — no model modifications.

---

### Script: Required parameter completeness check

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import csv, os

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
## Define which categories and which parameters are REQUIRED
VALIDATION_RULES = {
    BuiltInCategory.OST_Rooms: [
        "Name", "Number", "Department", "Occupancy"
    ],
    BuiltInCategory.OST_Doors: [
        "Mark", "Fire Rating", "Width", "Height"
    ],
    BuiltInCategory.OST_Windows: [
        "Mark", "Width", "Height"
    ],
}

## Optional: allowed value lists (leave empty dict {} to skip)
ALLOWED_VALUES = {
    # "Fire Rating": ["30", "60", "90", "120", "FD30", "FD60", "FD90"],
    # "Occupancy": ["Office", "Meeting", "Circulation", "WC", "Stair"],
}

## Export report to CSV? Set to None to skip file export.
OUTPUT_CSV = r"C:\Exports\parameter_validation_report.csv"
## ─────────────────────────────────────────────────────────────────────────────

def get_str_value(el, param_name):
    """Return parameter value as string, or None if missing/unset."""
    param = el.LookupParameter(param_name)
    if not param:
        return None  # Parameter doesn't exist on this element
    st = param.StorageType
    if st == StorageType.String:
        v = param.AsString()
        return v if v else ""
    elif st == StorageType.Double:
        v = param.AsDouble()
        return str(round(v, 4)) if v is not None else ""
    elif st == StorageType.Integer:
        return str(param.AsInteger())
    elif st == StorageType.ElementId:
        eid = param.AsElementId()
        ref = doc.GetElement(eid)
        return ref.Name if ref else ""
    return ""

try:
    all_issues = []
    summary = {}

    for category, required_params in VALIDATION_RULES.items():
        elements = list(FilteredElementCollector(doc)
                        .OfCategory(category)
                        .WhereElementIsNotElementType()
                        .ToElements())

        cat_name = doc.Settings.Categories.get_Item(category).Name
        issues = []
        passed = 0

        for el in elements:
            el_issues = []
            el_id = str(el.Id.IntegerValue)

            # Try to get a display name for the element
            name_param = el.LookupParameter("Name") or el.LookupParameter("Mark")
            el_name = (name_param.AsString() if name_param else None) or el_id

            for param_name in required_params:
                value = get_str_value(el, param_name)

                if value is None:
                    el_issues.append(param_name + ": PARAMETER NOT FOUND")
                elif value.strip() == "":
                    el_issues.append(param_name + ": EMPTY")
                elif param_name in ALLOWED_VALUES:
                    allowed = ALLOWED_VALUES[param_name]
                    if value not in allowed:
                        el_issues.append(param_name + ": '" + value +
                                         "' not in allowed list " + str(allowed))

            if el_issues:
                issues.append({
                    "Category": cat_name,
                    "ElementId": el_id,
                    "Element": el_name,
                    "Issues": " | ".join(el_issues)
                })
            else:
                passed += 1

        summary[cat_name] = {
            "Total": len(elements),
            "Passed": passed,
            "Failed": len(issues),
            "Pass Rate": (str(round(100 * passed / len(elements))) + "%") if elements else "N/A"
        }
        all_issues.extend(issues)

    # Write CSV report
    if OUTPUT_CSV and all_issues:
        os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
        with open(OUTPUT_CSV, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Category", "ElementId", "Element", "Issues"])
            writer.writeheader()
            writer.writerows(all_issues)

    OUT = {
        "Summary": summary,
        "Total Issues": len(all_issues),
        "Issues": all_issues[:50],   # show first 50 in Dynamo
        "Report": OUTPUT_CSV if OUTPUT_CSV else "No file export configured"
    }

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Pre-built validation profiles

#### BEP-standard room data

```python
VALIDATION_RULES = {
    BuiltInCategory.OST_Rooms: [
        "Name", "Number", "Department", "Occupancy",
        "Base Finish", "Ceiling Finish", "Wall Finish", "Comments"
    ]
}
```

#### COBie-ready asset data (doors/equipment)

```python
VALIDATION_RULES = {
    BuiltInCategory.OST_Doors: [
        "Mark", "Type Comments", "Fire Rating", "Manufacturer", "Model",
        "Warranty Duration Parts", "Warranty Duration Labor"
    ],
    BuiltInCategory.OST_MechanicalEquipment: [
        "Mark", "Manufacturer", "Model", "Serial Number", "Warranty Duration Parts"
    ]
}
```

#### Structural submission check

```python
VALIDATION_RULES = {
    BuiltInCategory.OST_StructuralColumns: ["Mark", "Structural Material", "Comments"],
    BuiltInCategory.OST_StructuralFraming:  ["Mark", "Structural Material", "Cut Length"],
    BuiltInCategory.OST_StructuralFoundation: ["Mark", "Structural Material"],
}
```

---

### Interpreting results

Guide the user on what to do with failures:

- **PARAMETER NOT FOUND**: the parameter may not be bound to this category — check Shared Parameters
- **EMPTY**: element exists but data hasn't been filled in — filter by ElementId in Revit to locate them
- **Not in allowed list**: data is filled but doesn't conform to the project standard — may need a lookup table

### Output

Always tell the user:
- Pass rate per category (e.g. "Rooms: 48/52 passed — 92%")
- The top 3 most common failing parameters
- Location of the CSV report if generated


## linked-model-check

> Check the status, coordinates, and health of all RVT and CAD linked files in a Revit model. Generates a coordination report showing which links are loaded, unloaded, missing, or have coordinate mismatches. Use this skill before coordination meetings, model submissions, or federated model reviews. Trigger on phrases like "linked model", "check links", "RVT links", "CAD links", "link status", "coordinate check", "shared coordinates", "model federation", "are all links loaded", "missing links", "linked file health", "unloaded links", "link report", or any request to inspect the status of files linked into a Revit model. Also offer this proactively before IFC export or Navisworks federation.

## Linked Model Health Check

Audit linked files and coordination status for:

**"$ARGUMENTS"**

### Approach

Default to a comprehensive read-only report covering:
- All RVT links (loaded, unloaded, missing, not found)
- All CAD imports/links (DWG, DXF, DGN)
- Coordinate system status (shared coordinates, survey point)
- Linked model bounding boxes (detect obvious coordinate outliers)

---

### Script: Comprehensive linked file report (read-only)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import csv, os

doc  = DocumentManager.Instance.CurrentDBDocument
MM_TO_FT = 1.0 / 304.8

def ft_to_mm(ft_val):
    return round(ft_val * 304.8, 1)

try:
    report = {}

    # ── 1. RVT Links ──────────────────────────────────────────────────────────
    rvt_link_types = list(FilteredElementCollector(doc)
                          .OfClass(RevitLinkType).ToElements())
    rvt_link_instances = list(FilteredElementCollector(doc)
                              .OfClass(RevitLinkInstance).ToElements())

    rvt_report = []
    for lt in rvt_link_types:
        load_state = lt.GetLinkedFileStatus()
        path_info  = lt.GetExternalFileReference()
        path_str   = ""
        try:
            path_str = ModelPathUtils.ConvertModelPathToUserVisiblePath(
                path_info.GetAbsolutePath())
        except Exception:
            path_str = "Path unavailable"

        # Find matching instances
        instances = [li for li in rvt_link_instances
                     if li.GetTypeId() == lt.Id]

        for inst in instances:
            xform = inst.GetTransform()
            origin = xform.Origin
            link_doc = inst.GetLinkDocument()

            entry = {
                "Name":           lt.Name,
                "Status":         str(load_state),
                "Path":           path_str,
                "Instance Count": len(instances),
                "Origin X (mm)":  ft_to_mm(origin.X),
                "Origin Y (mm)":  ft_to_mm(origin.Y),
                "Origin Z (mm)":  ft_to_mm(origin.Z),
                "Is Identity":    xform.IsIdentity,
                "Linked Doc":     link_doc.Title if link_doc else "NOT LOADED",
            }

            # Coordinate warning
            if abs(origin.X) > 328 or abs(origin.Y) > 328:  # > 100m offset
                entry["WARNING"] = "Link origin > 100m from project origin — check shared coordinates"
            else:
                entry["WARNING"] = ""

            rvt_report.append(entry)

    # If no instances (type exists but not placed)
    for lt in rvt_link_types:
        instances = [li for li in rvt_link_instances if li.GetTypeId() == lt.Id]
        if not instances:
            rvt_report.append({
                "Name":     lt.Name,
                "Status":   str(lt.GetLinkedFileStatus()),
                "Path":     "Type exists but not placed as instance",
                "WARNING":  "No instance placed in model"
            })

    report["RVT Links"] = rvt_report

    # ── 2. CAD Links & Imports ────────────────────────────────────────────────
    cad_items = list(FilteredElementCollector(doc)
                     .OfClass(ImportInstance).ToElements())
    cad_report = []
    for ci in cad_items:
        try:
            cat_name = ci.Category.Name if ci.Category else "Unknown"
            is_linked = ci.IsLinked
            xform     = ci.GetTransform()
            origin    = xform.Origin

            entry = {
                "Category":      cat_name,
                "Is Linked":     is_linked,
                "Origin X (mm)": ft_to_mm(origin.X),
                "Origin Y (mm)": ft_to_mm(origin.Y),
                "Origin Z (mm)": ft_to_mm(origin.Z),
            }
            try:
                ext_ref = ci.GetExternalFileReference()
                entry["Path"] = ModelPathUtils.ConvertModelPathToUserVisiblePath(
                    ext_ref.GetAbsolutePath())
            except Exception:
                entry["Path"] = "Embedded / no path"

            cad_report.append(entry)
        except Exception:
            pass

    report["CAD Links/Imports"] = cad_report

    # ── 3. Coordinate summary ─────────────────────────────────────────────────
    # Project Base Point and Survey Point
    base_pts   = list(FilteredElementCollector(doc)
                      .OfClass(BasePoint)
                      .ToElements())
    coord_info = []
    for bp in base_pts:
        try:
            is_survey = bp.IsShared
            pos       = bp.Position
            coord_info.append({
                "Type":       "Survey Point" if is_survey else "Project Base Point",
                "X (mm)":     ft_to_mm(pos.X),
                "Y (mm)":     ft_to_mm(pos.Y),
                "Z (mm)":     ft_to_mm(pos.Z),
            })
        except Exception:
            pass

    report["Coordinate Points"] = coord_info

    # ── 4. Summary ───────────────────────────────────────────────────────────
    loaded   = sum(1 for r in rvt_report
                   if "LinkedFileStatus_Loaded" in str(r.get("Status", "")))
    unloaded = sum(1 for r in rvt_report
                   if "LinkedFileStatus_Loaded" not in str(r.get("Status", ""))
                   and r.get("Status"))
    warnings = sum(1 for r in rvt_report if r.get("WARNING"))

    report["Summary"] = {
        "Total RVT Links":   len(rvt_link_types),
        "Instances placed":  len(rvt_link_instances),
        "Loaded":            loaded,
        "Unloaded/Missing":  unloaded,
        "Coordinate Warnings": warnings,
        "CAD Items":         len(cad_items),
    }

    OUT = report

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script: Reload all unloaded RVT links

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    link_types = list(FilteredElementCollector(doc)
                      .OfClass(RevitLinkType).ToElements())
    reloaded = []
    failed   = []

    TransactionManager.Instance.EnsureInTransaction(doc)

    for lt in link_types:
        status = lt.GetLinkedFileStatus()
        if str(status) != "LinkedFileStatus_Loaded":
            try:
                result = lt.Reload()
                if str(result) == "LinkLoadResultType_Success":
                    reloaded.append(lt.Name)
                else:
                    failed.append(lt.Name + " (" + str(result) + ")")
            except Exception as ex:
                failed.append(lt.Name + " (Exception: " + str(ex) + ")")

    TransactionManager.Instance.TransactionTaskDone()
    OUT = {"Reloaded": reloaded, "Failed": failed}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Interpreting the report

Guide the user on key red flags:

- **Status ≠ Loaded**: find the file on the server and use Manage Links → Reload From to fix path
- **Origin > 100m from project origin**: shared coordinates are likely wrong — check Survey Point vs Project Base Point
- **Is Identity = False**: the link has been moved from its reference point — may cause coordination issues
- **CAD import (not linked)**: imported DWGs bloat the model — recommend converting to linked CAD
- **No instance placed**: the link type exists in the file but wasn't placed — it's still taking up file size

### What to tell the user

Always summarise:
1. How many links are loaded vs unloaded
2. Any coordinate warnings
3. Whether any CAD files are imported (not linked) — these should be converted to links
4. Next steps: who owns each link and needs to fix their model


## workset-manager

> Audit workset assignments across a Revit model, identify elements on the wrong workset, and move elements between worksets using Dynamo Python. Use this skill when checking model workset structure before submission, finding walls on the MEP workset, moving elements to the correct workset based on category rules, generating a workset assignment report, or cleaning up workset mistakes before issuing. Trigger on phrases like "workset", "wrong workset", "move to workset", "workset audit", "workset report", "workset assignment", "elements on wrong workset", "workset cleanup", "check worksets", "workset structure", or any request involving workset management and auditing.

## Workset Manager — Audit & Fix

Audit and manage worksets for:

**"$ARGUMENTS"**

### Before writing code

Ask (one question if ambiguous):
1. **Audit or fix?** Just report which elements are on wrong worksets, or also move them?
2. **What are the workset rules?** (e.g. Walls/Floors/Roofs → Architecture, Ducts/Pipes → MEP)
3. **Scope?** Entire model, or one level/phase?

Always run the audit script first, then the move script if needed.

---

### Script 1: Workset audit report (read-only)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import csv, os

doc = DocumentManager.Instance.CurrentDBDocument

try:
    if not doc.IsWorkshared:
        OUT = "This model is not workshared — worksets are not applicable."
    else:
        # Get all user worksets
        worksets = {ws.Id: ws.Name for ws in
                    FilteredWorksetCollector(doc)
                    .OfKind(WorksetKind.UserWorkset)
                    .ToWorksets()}

        # Categories to audit and their expected workset (partial match OK)
        EXPECTED_WORKSETS = {
            "Walls":                  "Architecture",
            "Floors":                 "Architecture",
            "Roofs":                  "Architecture",
            "Ceilings":               "Architecture",
            "Stairs":                 "Architecture",
            "Railings":               "Architecture",
            "Curtain Panels":         "Architecture",
            "Structural Columns":     "Structure",
            "Structural Framing":     "Structure",
            "Structural Foundations": "Structure",
            "Duct Curves":            "MEP",
            "Pipe Curves":            "MEP",
            "Conduits":               "MEP",
            "Cable Trays":            "MEP",
            "Mechanical Equipment":   "MEP",
            "Plumbing Fixtures":      "MEP",
            "Lighting Fixtures":      "MEP",
        }

        BIC_MAP = {
            "Walls":                  BuiltInCategory.OST_Walls,
            "Floors":                 BuiltInCategory.OST_Floors,
            "Roofs":                  BuiltInCategory.OST_Roofs,
            "Ceilings":               BuiltInCategory.OST_Ceilings,
            "Stairs":                 BuiltInCategory.OST_Stairs,
            "Railings":               BuiltInCategory.OST_StairsRailing,
            "Curtain Panels":         BuiltInCategory.OST_CurtainWallPanels,
            "Structural Columns":     BuiltInCategory.OST_StructuralColumns,
            "Structural Framing":     BuiltInCategory.OST_StructuralFraming,
            "Structural Foundations": BuiltInCategory.OST_StructuralFoundation,
            "Duct Curves":            BuiltInCategory.OST_DuctCurves,
            "Pipe Curves":            BuiltInCategory.OST_PipeCurves,
            "Conduits":               BuiltInCategory.OST_Conduit,
            "Cable Trays":            BuiltInCategory.OST_CableTray,
            "Mechanical Equipment":   BuiltInCategory.OST_MechanicalEquipment,
            "Plumbing Fixtures":      BuiltInCategory.OST_PlumbingFixtures,
            "Lighting Fixtures":      BuiltInCategory.OST_LightingFixtures,
        }

        misplaced = []
        summary   = {}

        for cat_name, bic in BIC_MAP.items():
            expected_partial = EXPECTED_WORKSETS.get(cat_name, "")
            elements = list(FilteredElementCollector(doc)
                            .OfCategory(bic)
                            .WhereElementIsNotElementType()
                            .ToElements())
            wrong = 0
            for el in elements:
                ws_param = el.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)
                if not ws_param:
                    continue
                ws_id   = WorksetId(ws_param.AsInteger())
                ws_name = worksets.get(ws_id, "Unknown")
                if expected_partial and expected_partial.lower() not in ws_name.lower():
                    misplaced.append({
                        "Category":        cat_name,
                        "ElementId":       str(el.Id.IntegerValue),
                        "Current Workset": ws_name,
                        "Expected":        expected_partial,
                    })
                    wrong += 1

            summary[cat_name] = {
                "Total":     len(elements),
                "Misplaced": wrong,
                "Expected":  expected_partial,
            }

        OUT = {
            "Summary":          summary,
            "Misplaced count":  len(misplaced),
            "Misplaced (first 50)": misplaced[:50],
            "Available worksets": list(worksets.values()),
        }

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 2: Move elements to correct worksets by category rule

**⚠ This modifies the model. Test on a detached copy first.**

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
## Maps BuiltInCategory → target workset name (partial match)
REASSIGNMENT_RULES = [
    (BuiltInCategory.OST_Walls,              "Architecture"),
    (BuiltInCategory.OST_Floors,             "Architecture"),
    (BuiltInCategory.OST_Roofs,              "Architecture"),
    (BuiltInCategory.OST_Ceilings,           "Architecture"),
    (BuiltInCategory.OST_StructuralColumns,  "Structure"),
    (BuiltInCategory.OST_StructuralFraming,  "Structure"),
    (BuiltInCategory.OST_DuctCurves,         "MEP"),
    (BuiltInCategory.OST_PipeCurves,         "MEP"),
    (BuiltInCategory.OST_MechanicalEquipment,"MEP"),
    (BuiltInCategory.OST_PlumbingFixtures,   "MEP"),
    (BuiltInCategory.OST_LightingFixtures,   "MEP"),
]
## ─────────────────────────────────────────────────────────────────────────────

try:
    if not doc.IsWorkshared:
        OUT = "This model is not workshared."
    else:
        # Build workset lookup: name fragment → WorksetId
        all_worksets = {ws.Name: ws.Id for ws in
                        FilteredWorksetCollector(doc)
                        .OfKind(WorksetKind.UserWorkset)
                        .ToWorksets()}

        def find_workset_id(partial_name):
            for ws_name, ws_id in all_worksets.items():
                if partial_name.lower() in ws_name.lower():
                    return ws_id
            return None

        moved   = []
        skipped = []

        TransactionManager.Instance.EnsureInTransaction(doc)

        for bic, target_name in REASSIGNMENT_RULES:
            target_id = find_workset_id(target_name)
            if not target_id:
                skipped.append("Workset matching '" + target_name + "' not found")
                continue

            elements = list(FilteredElementCollector(doc)
                            .OfCategory(bic)
                            .WhereElementIsNotElementType()
                            .ToElements())

            for el in elements:
                ws_param = el.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)
                if ws_param and not ws_param.IsReadOnly:
                    current_id = WorksetId(ws_param.AsInteger())
                    if current_id != target_id:
                        ws_param.Set(target_id.IntegerValue)
                        moved.append(str(el.Id.IntegerValue) + " → " + target_name)

        TransactionManager.Instance.TransactionTaskDone()
        OUT = {
            "Moved":   len(moved),
            "Skipped": skipped,
            "Details (first 50)": moved[:50]
        }

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 3: List all worksets and element counts per workset (read-only)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    if not doc.IsWorkshared:
        OUT = "Not a workshared model."
    else:
        worksets = list(FilteredWorksetCollector(doc)
                        .OfKind(WorksetKind.UserWorkset)
                        .ToWorksets())

        # Count elements per workset
        ws_counts = {ws.Id: {"Name": ws.Name, "Count": 0, "Owner": ws.Owner or "Not checked out"}
                     for ws in worksets}

        all_elements = list(FilteredElementCollector(doc)
                            .WhereElementIsNotElementType()
                            .ToElements())

        for el in all_elements:
            ws_param = el.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)
            if ws_param:
                ws_id = WorksetId(ws_param.AsInteger())
                if ws_id in ws_counts:
                    ws_counts[ws_id]["Count"] += 1

        result = sorted(ws_counts.values(), key=lambda x: -x["Count"])
        OUT = result

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Workset best practices to share with users

- **Shared Levels and Grids**: always keep levels and grids on a dedicated workset — never on Architecture or Structure
- **Linked Models**: all `RevitLinkInstance` objects should go on a "Linked Models" workset
- **Ownership**: remind users to relinquish all worksets after a session (Collaborate → Relinquish All)
- **Naming**: use consistent names across projects — "Architecture" not "Arch", "ARCH", or "01-Architecture"


## clash-detection

> Detect and report geometric clashes and interferences between Revit model elements using Dynamo Python and the Revit API's Boolean intersection tools. Use this skill when checking for MEP vs Structure clashes, discipline coordination, overlapping element checks, or any geometric interference between two sets of elements. Trigger on phrases like "clash detection", "interference check", "find clashes", "MEP coordination", "structural clash", "duct vs beam", "pipe vs column", "coordination report", or any request to find elements that overlap or intersect in 3D space. Also offer this skill when users mention coordination meetings or model submission reviews.

## Clash Detection & Coordination

Perform clash detection for:

**"$ARGUMENTS"**

### Before scripting

Clarify:
1. **Which two disciplines** are you checking? (e.g. structural columns vs MEP ducts)
2. **How should clashes be reported?** (list of IDs, CSV export, isolate in view?)
3. **Minimum clash volume?** Default threshold is very small (1e-6 ft³) to catch all contacts.

Note: for large models, Boolean intersection on every element pair is slow. Recommend running on a specific level or workset, or using Navisworks for production-scale clash detection.

### Clash detection script

Read-only — no model modifications.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Define the two element sets to check ────────────────────────────────────
## Modify these categories for your discipline combination:
set_a = list(FilteredElementCollector(doc)
             .OfCategory(BuiltInCategory.OST_StructuralColumns)
             .WhereElementIsNotElementType()
             .ToElements())

set_b = list(FilteredElementCollector(doc)
             .OfCategory(BuiltInCategory.OST_DuctCurves)
             .WhereElementIsNotElementType()
             .ToElements())

## ── Helper: extract solid geometry from an element ──────────────────────────
def get_solid(element):
    opts = Options()
    opts.ComputeReferences = False
    opts.DetailLevel = ViewDetailLevel.Fine
    geo = element.get_Geometry(opts)
    if geo is None:
        return None
    for obj in geo:
        if isinstance(obj, Solid) and obj.Volume > 1e-9:
            return obj
        if isinstance(obj, GeometryInstance):
            for sub in obj.GetInstanceGeometry():
                if isinstance(sub, Solid) and sub.Volume > 1e-9:
                    return sub
    return None

## ── Run clash detection ──────────────────────────────────────────────────────
clashes = []

try:
    for el_a in set_a:
        solid_a = get_solid(el_a)
        if solid_a is None:
            continue

        # Get type name once per el_a (minor optimisation)
        type_id_a = el_a.GetTypeId()
        type_name_a = (doc.GetElement(type_id_a).Name
                       if type_id_a != ElementId.InvalidElementId else 'N/A')

        for el_b in set_b:
            solid_b = get_solid(el_b)
            if solid_b is None:
                continue
            try:
                intersection = BooleanOperationsUtils.ExecuteBooleanOperation(
                    solid_a, solid_b, BooleanOperationsType.Intersect)

                if intersection and intersection.Volume > 1e-6:
                    type_id_b = el_b.GetTypeId()
                    type_name_b = (doc.GetElement(type_id_b).Name
                                   if type_id_b != ElementId.InvalidElementId else 'N/A')
                    clashes.append({
                        'Element A ID':   el_a.Id.IntegerValue,
                        'Element A Type': type_name_a,
                        'Element B ID':   el_b.Id.IntegerValue,
                        'Element B Type': type_name_b,
                        'Clash Volume (ft3)': round(intersection.Volume, 6),
                        'Clash Volume (cm3)': round(intersection.Volume * 28316.8, 2),
                    })
            except:
                # Boolean operation failed — elements may share a face (contact, not clash)
                pass

    OUT = [len(clashes), clashes]

except Exception as e:
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Isolating clashing elements in a view

Once you have the clash IDs, show the user how to isolate them:

```python
## IN[0] = list of element IDs from the clash report (integers)
## This script isolates clashing elements in the active view
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc   = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
view  = uidoc.ActiveView

clash_ids = [ElementId(int(i)) for i in IN[0]]

TransactionManager.Instance.EnsureInTransaction(doc)
view.IsolateElementsTemporary(clash_ids)
TransactionManager.Instance.TransactionTaskDone()
OUT = 'Isolated ' + str(len(clash_ids)) + ' elements in active view'
```

### Exporting clash report to CSV

```python
import csv
output_path = r'C:\Reports\clash_report.csv'
if clashes:
    with open(output_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=clashes[0].keys())
        writer.writeheader()
        writer.writerows(clashes)
    OUT = 'Clash report saved: ' + output_path + ' (' + str(len(clashes)) + ' clashes)'
```

### Performance note

For models with thousands of elements, the pairwise Boolean check can be slow. Recommend:
- Running on a single level at a time (use `ElementLevelFilter`)
- Using Autodesk Navisworks for production-scale coordination
- This script is best for targeted checks (e.g. new structural additions vs existing MEP)


---

# Rooms, schedules & export


## analyze-rooms

> Analyze rooms, spaces, and areas in a Revit model — GIA calculations, space program comparison, department breakdowns, unbounded/unplaced room audits, and CSV export. Use this skill when a user wants to calculate total floor area, check room areas against a brief, export a room data table, find unplaced or unbounded rooms, or produce a GIA (Gross Internal Area) report. Trigger on phrases like "room areas", "GIA", "space program", "analyze rooms", "unbounded rooms", "area schedule", "room data", "floor area summary", "net internal area", or any request involving Revit room/space quantities. Also use when someone mentions area validation before planning submission.

## Analyze Revit Rooms & Spaces

Perform room/space analysis for:

**"$ARGUMENTS"**

### Room data extraction script

Read-only — no model modifications.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## Unit conversion constants
SQ_FT_TO_SQ_M    = 0.092903   # Revit stores area in square feet internally
CUBIC_FT_TO_M3   = 0.0283168
FT_TO_M          = 0.3048

try:
    # Collect all placed rooms
    rooms = (FilteredElementCollector(doc)
             .OfCategory(BuiltInCategory.OST_Rooms)
             .WhereElementIsNotElementType()
             .ToElements())

    room_data = []
    unplaced   = []

    for room in rooms:
        area_sqft = room.Area

        if area_sqft <= 0:
            # Unplaced or unbounded room — flag it
            unplaced.append({
                'Id':     room.Id.IntegerValue,
                'Number': room.Number,
                'Name':   room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString() or '',
                'Issue':  'Unplaced or Unbounded'
            })
            continue

        # Pull all useful fields
        dept_param  = room.get_Parameter(BuiltInParameter.ROOM_DEPARTMENT)
        phase_param = room.get_Parameter(BuiltInParameter.ROOM_PHASE)

        data = {
            'Room Number':   room.Number,
            'Room Name':     room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString() or '',
            'Department':    dept_param.AsString()  if dept_param  else '',
            'Level':         room.Level.Name         if room.Level  else 'N/A',
            'Area (m2)':     round(area_sqft * SQ_FT_TO_SQ_M, 2),
            'Area (ft2)':    round(area_sqft, 2),
            'Volume (m3)':   round(room.Volume * CUBIC_FT_TO_M3, 2),
            'Perimeter (m)': round(room.Perimeter * FT_TO_M, 2),
            'Phase':         phase_param.AsValueString() if phase_param else '',
            'Element Id':    room.Id.IntegerValue,
        }
        room_data.append(data)

    # Sort by level, then room number
    room_data.sort(key=lambda x: (x['Level'], x['Room Number']))

    # Calculate totals
    gia_m2 = sum(r['Area (m2)'] for r in room_data)

    OUT = [
        room_data,                             # full data table
        unplaced,                              # rooms to fix
        round(gia_m2, 2),                      # total GIA in m²
        len(room_data),                        # placed room count
        len(unplaced),                         # unplaced count
    ]

except Exception as e:
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Exporting to CSV

```python
import csv
output_path = r'C:\Reports\room_analysis.csv'
if room_data:
    with open(output_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=room_data[0].keys())
        writer.writeheader()
        writer.writerows(room_data)
    print('Saved to: ' + output_path)
```

### Fixing unplaced / unbounded rooms

Guide the user:
1. Open **Room Separation Lines** view — confirm boundary lines form a closed loop
2. In Revit, go to **Architecture → Room** and check the room boundary visibility
3. Unbounded rooms often mean boundary lines are missing or the room is placed outside a boundary
4. Delete truly unneeded rooms (they appear as "Not Placed" in schedules)

### GIA / NIA breakdown by department

If the user wants breakdown by department or level:

```python
from collections import defaultdict
by_dept = defaultdict(float)
by_level = defaultdict(float)
for r in room_data:
    by_dept[r['Department'] or 'Unassigned'] += r['Area (m2)']
    by_level[r['Level']] += r['Area (m2)']
OUT = [dict(by_dept), dict(by_level), round(gia_m2, 2)]
```

### Space program comparison

If the user has a brief (target areas), accept it as a Dynamo input:

```python
## IN[0] = list of [room_name, target_area_m2] pairs from an Excel node
brief = {row[0]: row[1] for row in IN[0]}
comparison = []
for r in room_data:
    target = brief.get(r['Room Name'])
    if target:
        delta = round(r['Area (m2)'] - float(target), 2)
        comparison.append({
            'Room': r['Room Name'],
            'Actual (m2)': r['Area (m2)'],
            'Target (m2)': float(target),
            'Delta (m2)': delta,
            'Status': 'Over' if delta > 0 else 'Under' if delta < 0 else 'OK'
        })
OUT = comparison
```


## create-schedule

> Create, configure, or automate Revit schedules, quantity takeoffs, and material takeoffs using Dynamo Python. Use this skill when creating element schedules programmatically, configuring schedule fields and filters via script, automating schedule creation from a list, or producing quantity reports. Trigger on phrases like "create a schedule", "make a schedule", "add schedule fields", "automate schedules", "quantity takeoff", "door schedule", "wall schedule", "room schedule", or any request to generate or configure a Revit schedule via Dynamo. Also offer this skill when users want to batch-create multiple schedules at once.

## Create Revit Schedule

Create a Revit schedule for:

**"$ARGUMENTS"**

### Before scripting

Clarify:
- **Which category?** (Doors, Walls, Rooms, Windows, etc.)
- **Which fields** should appear in the schedule? (Mark, Type, Width, Height, Area, etc.)
- **Should it be placed on a sheet?** If so, which sheet number?
- **Any filters?** (e.g. only doors on Level 2, only walls with Fire Rating = 2HR)

### Schedule creation script

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration — edit these ───────────────────────────────────────────────
SCHEDULE_NAME = 'BIM Manager - Door Schedule'
CATEGORY      = BuiltInCategory.OST_Doors   # ← change category as needed

## Built-in parameters to add as schedule fields
## (comment out the ones you don't need, add others)
DESIRED_PARAMS = [
    BuiltInParameter.ALL_MODEL_MARK,
    BuiltInParameter.ALL_MODEL_TYPE_NAME,
    BuiltInParameter.DOOR_WIDTH,
    BuiltInParameter.DOOR_HEIGHT,
    BuiltInParameter.ALL_MODEL_DESCRIPTION,
    BuiltInParameter.ALL_MODEL_MANUFACTURER,
]

TransactionManager.Instance.EnsureInTransaction(doc)
try:
    # ── Create the schedule ──────────────────────────────────────────────────
    category_id = ElementId(CATEGORY)
    schedule    = ViewSchedule.CreateSchedule(doc, category_id)
    schedule.Name = SCHEDULE_NAME

    # ── Get all schedulable fields ───────────────────────────────────────────
    all_fields = list(schedule.Definition.GetSchedulableFields())

    # ── Add desired parameter fields ─────────────────────────────────────────
    desired_ids = set(ElementId(p) for p in DESIRED_PARAMS)
    added = 0
    for sf in all_fields:
        if sf.ParameterId in desired_ids:
            schedule.Definition.AddField(sf)
            added += 1

    # Fallback: if none matched, add the first 6 available fields
    if added == 0:
        for sf in all_fields[:6]:
            schedule.Definition.AddField(sf)

    # ── Add sorting by the first field ──────────────────────────────────────
    if all_fields:
        sort_field = ScheduleSortGroupField(all_fields[0].FieldId)
        schedule.Definition.AddSortGroupField(sort_field)

    TransactionManager.Instance.TransactionTaskDone()
    OUT = 'Schedule created: ' + schedule.Name + ' (Id: ' + str(schedule.Id.IntegerValue) + ')'

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Adding a filter to the schedule

After creating the schedule, add a filter to show only elements matching a condition:

```python
## Example: show only doors wider than 900mm (≈ 2.95 ft)
min_width_ft = 900 / 304.8

## Get the Width field
width_field = next((f for f in schedule.Definition.GetFields()
                    if f.GetName() == 'Width'), None)
if width_field:
    rule = ScheduleFilterValueRule(
        width_field.FieldId,
        ScheduleFilterType.GreaterThanOrEqual,
        min_width_ft
    )
    flt = ScheduleFilter(rule)
    schedule.Definition.AddFilter(flt)
```

### Placing the schedule on a sheet

```python
## IN[0] = sheet number string (e.g. "A-001")
sheet_number = IN[0]
sheet = next((v for v in FilteredElementCollector(doc)
              .OfClass(ViewSheet).ToElements()
              if v.SheetNumber == sheet_number), None)

if sheet:
    TransactionManager.Instance.EnsureInTransaction(doc)
    # Place at a point on the sheet (adjust coordinates as needed)
    placement_point = XYZ(0.1, 0.1, 0)
    ScheduleSheetInstance.Create(doc, sheet.Id, schedule.Id, placement_point)
    TransactionManager.Instance.TransactionTaskDone()
    OUT = 'Schedule placed on sheet: ' + sheet_number
else:
    OUT = 'Sheet not found: ' + sheet_number
```

### Batch-create multiple schedules

If the user wants several schedules at once (one per level, or one per discipline):

```python
## IN[0] = list of [schedule_name, category_bic_name] pairs
## Example: [["Level 1 Doors", "OST_Doors"], ["Level 1 Rooms", "OST_Rooms"]]
schedule_defs = IN[0]
created = []

TransactionManager.Instance.EnsureInTransaction(doc)
for name, bic_name in schedule_defs:
    bic   = getattr(BuiltInCategory, bic_name)
    sched = ViewSchedule.CreateSchedule(doc, ElementId(bic))
    sched.Name = name
    # Add first 5 fields automatically
    for sf in list(sched.Definition.GetSchedulableFields())[:5]:
        sched.Definition.AddField(sf)
    created.append(name)
TransactionManager.Instance.TransactionTaskDone()
OUT = 'Created: ' + str(created)
```


## export-to-excel

> Export Revit model data — element parameters, room data, door/window schedules, family instances, or any category — to a CSV or Excel-compatible file using Dynamo Python. Use this skill when a user wants to get model data out of Revit into a spreadsheet for reporting, cost estimation, client delivery, or BIM data validation. Trigger on phrases like "export to Excel", "export to CSV", "get data out of Revit", "export parameters", "export schedule", "export room data", "extract model data", "create a data dump", "export family list", "export door schedule", or any request to pull Revit data into a tabular file format.

## Export Revit Model Data to Excel / CSV

Export model data to a spreadsheet for:

**"$ARGUMENTS"**

### Before writing code

Ask (one question if ambiguous):
1. **Which category?** Rooms, Doors, Windows, Walls, Families, Sheets, or a custom one?
2. **Which parameters?** List them, or default to the most useful set for that category.
3. **Output path?** Default to `C:\Exports\revit_export.csv` — user can change it.

Read-only — no model modifications. Safe to run on any model.

---

### Script: Universal parameter export to CSV

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import csv, os, System

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
CATEGORY    = BuiltInCategory.OST_Rooms   # change to target category
OUTPUT_PATH = r"C:\Exports\revit_export.csv"

## Parameters to export — exact names, case-sensitive
## Leave empty [] to export ALL available parameters (creates wide table)
PARAMS = [
    "Name",
    "Number",
    "Level",
    "Area",
    "Department",
    "Occupancy",
    "Comments",
]
## ─────────────────────────────────────────────────────────────────────────────

def get_param_value(el, param_name):
    """Safely read any parameter as a display string."""
    param = el.LookupParameter(param_name)
    if not param:
        return ""
    storage = param.StorageType
    if storage == StorageType.String:
        return param.AsString() or ""
    elif storage == StorageType.Double:
        # Return in display units (mm² for area, mm for length)
        try:
            return str(round(param.AsDouble() * 0.0929, 3))  # ft² → m²
        except Exception:
            return str(param.AsDouble())
    elif storage == StorageType.Integer:
        return str(param.AsInteger())
    elif storage == StorageType.ElementId:
        eid = param.AsElementId()
        ref_el = doc.GetElement(eid)
        return ref_el.Name if ref_el else str(eid.IntegerValue)
    return ""

try:
    elements = list(FilteredElementCollector(doc)
                    .OfCategory(CATEGORY)
                    .WhereElementIsNotElementType()
                    .ToElements())

    if not elements:
        OUT = "No elements found in the specified category."
    else:
        # Determine headers
        if PARAMS:
            headers = ["ElementId"] + PARAMS
        else:
            # Auto-discover all parameters from first element
            headers = ["ElementId"]
            for p in elements[0].Parameters:
                if p.Definition:
                    headers.append(p.Definition.Name)

        # Ensure output directory exists
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

        # Write CSV
        with open(OUTPUT_PATH, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

            for el in elements:
                row = [str(el.Id.IntegerValue)]
                for param_name in headers[1:]:   # skip ElementId
                    row.append(get_param_value(el, param_name))
                writer.writerow(row)

        OUT = {
            "Exported": len(elements),
            "Fields": headers,
            "File": OUTPUT_PATH
        }

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Pre-built export recipes

#### Rooms export (area in m², department, level)

```python
CATEGORY = BuiltInCategory.OST_Rooms
PARAMS   = ["Name", "Number", "Level", "Area", "Department",
            "Occupancy", "Base Finish", "Ceiling Finish", "Comments"]
```

#### Door schedule export

```python
CATEGORY = BuiltInCategory.OST_Doors
PARAMS   = ["Mark", "Level", "Width", "Height", "Type Comments",
            "Frame Type", "Fire Rating", "Manufacturer", "Model"]
```

#### Window schedule export

```python
CATEGORY = BuiltInCategory.OST_Windows
PARAMS   = ["Mark", "Level", "Width", "Height", "Type Comments",
            "Fire Rating", "U-Value", "SHGC"]
```

#### Structural columns

```python
CATEGORY = BuiltInCategory.OST_StructuralColumns
PARAMS   = ["Mark", "Level", "Base Level", "Top Level",
            "Structural Material", "Comments"]
```

#### All family instances (flat list)

```python
CATEGORY = BuiltInCategory.OST_GenericModel
PARAMS   = ["Family", "Type", "Mark", "Level", "Comments"]
```

---

### Linked models

To export data from **linked models**, add this before the collector:

```python
## Get all loaded RVT links
links = FilteredElementCollector(doc).OfClass(RevitLinkInstance).ToElements()
for link in links:
    link_doc = link.GetLinkDocument()
    if link_doc:
        elements += list(FilteredElementCollector(link_doc)
                         .OfCategory(CATEGORY)
                         .WhereElementIsNotElementType()
                         .ToElements())
```

### Unit handling

Revit stores lengths in **decimal feet** internally. Common conversions:
- Area: `ft² × 0.0929 = m²`
- Length: `ft × 304.8 = mm`

For Revit 2022+, use `UnitUtils.ConvertFromInternalUnits(value, UnitTypeId.Meters)` instead.

### Customization tips

- Change `OUTPUT_PATH` to any folder with write access (mapped drive, project server, etc.)
- For large models, add a `Level` filter: `.WhereElementIsNotElementType().ToElements()` after adding a `LevelFilter`
- Open the CSV in Excel → Data → Text to Columns if formatting looks off


## export-ifc

> Export a Revit model to IFC format with proper settings, class mapping, and property sets using Dynamo Python. Use this skill when exporting to IFC 2x3 or IFC 4, configuring IFC export options, preparing a model for open BIM workflows, or generating IFC files for coordination, submission, or client delivery. Trigger on phrases like "export IFC", "IFC export", "open BIM", "IFC 2x3", "IFC 4", "BIM submission", "COBie", "IFC coordination", or when users mention needing to share the model with contractors, engineers, or clients using different software. Also offer this when users mention planning or building permit submissions that require open BIM formats.

## Export Revit Model to IFC

Configure and export IFC for:

**"$ARGUMENTS"**

### Before scripting

Clarify:
- **IFC version?** IFC 2x3 CV2 (most compatible) or IFC 4 (newer, for Revit 2019+)?
- **Whole model or active view only?** (`VisibleElementsOfCurrentView`)
- **Include linked files?** (`ExportLinkedFiles`)
- **Base quantities?** (area, volume, length — usually yes for quantity takeoffs)
- **Where to save?** Get the output folder from user

### Pre-export checklist

Tell the user to verify before running:
- [ ] All rooms/spaces are placed and bounded (unbounded rooms won't export correctly)
- [ ] Elements are properly categorised (generic models won't map to IFC classes)
- [ ] Project location and coordinates are set (`Manage → Location`)
- [ ] Levels are named consistently
- [ ] Linked files are loaded if `ExportLinkedFiles = True`

### IFC export script

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Inputs from Dynamo ───────────────────────────────────────────────────────
## IN[0] = export folder path (string), e.g. r"C:\Projects\MyProject\IFC"
## IN[1] = file name (string, no extension), e.g. "MyProject_Architecture_v01"
export_folder   = IN[0]
export_filename = IN[1]

try:
    # ── Configure IFC export options ─────────────────────────────────────────
    ifc_options = IFCExportOptions()

    # IFC version — change to IFCVersion.IFC4 for newer workflows
    ifc_options.FileVersion = IFCVersion.IFC2x3CV2

    # Export settings
    ifc_options.SpaceBoundaryLevel          = 1      # 0=None, 1=1st level, 2=2nd level
    ifc_options.ExportBaseQuantities        = True   # area, volume, length
    ifc_options.WallAndColumnSplitting      = True   # split at levels
    ifc_options.VisibleElementsOfCurrentView = False # False = entire model
    ifc_options.Export2DElements            = False
    ifc_options.ExportLinkedFiles           = False
    ifc_options.ExportSolidModelRep         = False

    # ── Run export ───────────────────────────────────────────────────────────
    doc.Export(export_folder, export_filename, ifc_options)

    full_path = export_folder + '\\' + export_filename + '.ifc'
    OUT = 'IFC exported successfully to: ' + full_path

except Exception as e:
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### IFC class mapping by discipline

Explain to the user how Revit categories map to IFC entities:

| Revit Category        | IFC Entity                  |
|-----------------------|-----------------------------|
| Walls                 | IfcWall / IfcWallStandardCase |
| Floors                | IfcSlab (FloorType)         |
| Roofs                 | IfcRoof                     |
| Columns (Arch)        | IfcColumn                   |
| Structural Columns    | IfcColumn                   |
| Structural Framing    | IfcBeam                     |
| Doors                 | IfcDoor                     |
| Windows               | IfcWindow                   |
| Rooms                 | IfcSpace                    |
| Ducts                 | IfcDuctSegment              |
| Pipes                 | IfcPipeSegment              |
| Generic Models        | IfcBuildingElementProxy     |

If elements appear as `IfcBuildingElementProxy` in the IFC file, they need to be
recategorised in Revit or their IFC export class needs to be overridden via a shared
parameter `IFCExportAs`.

### Post-export validation

Recommend free tools:
- **BIMvision** (free): open IFC file, check hierarchy and properties
- **Solibri Anywhere** (free): validate model health and IFC structure
- **Navisworks Freedom** (free): combine IFC with other disciplines for visual check

### IFC 4 differences

If the user needs IFC 4:
```python
ifc_options.FileVersion = IFCVersion.IFC4
## Also: use IFCVersion.IFC4RV for Reference View (design coordination)
## or IFCVersion.IFC4DTV for Design Transfer View (full geometry)
```

IFC 4 requires Revit 2019 or later.


---

# Parameters & element editing


## manage-parameters

> Read, write, batch-update, or validate Revit element parameters using Dynamo Python. Use this skill when modifying parameter values across many elements, batch-setting data from Excel, creating project or shared parameters, mapping parameters between fields, checking for missing or empty parameters, or copying values from one parameter to another. Trigger on phrases like "set parameter", "update parameters", "batch edit", "fill in", "parameter value", "shared parameter", "copy parameter", "parameter missing", or any request to read or write Revit element data at scale.

## Manage Revit Parameters

Perform parameter operation:

**"$ARGUMENTS"**

### Clarify before scripting

- **Read or write?** Read-only queries don't need a transaction.
- **Which elements?** All elements of a category, or a filtered subset?
- **Which parameter?** Ask for the exact name (case-sensitive) if the user mentions one.
- **What value?** String, number, yes/no, or element reference?

### Read/write parameter script

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

## Unwrap Dynamo-wrapped elements if needed
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

doc = DocumentManager.Instance.CurrentDBDocument

## ── Dynamo inputs ────────────────────────────────────────────────────────────
## IN[0] = list of Revit elements (from a Collector or upstream node)
## IN[1] = parameter name (string)
## IN[2] = new value (string/number) — omit or set to None for read-only
elements   = IN[0] if isinstance(IN[0], list) else [IN[0]]
param_name = IN[1]
new_value  = IN[2] if len(IN) > 2 else None

write_mode = new_value is not None
results    = []

try:
    if write_mode:
        TransactionManager.Instance.EnsureInTransaction(doc)

    for el in elements:
        # Unwrap Dynamo wrapper to native Revit element
        revit_el = el.InternalElement if hasattr(el, 'InternalElement') else el

        param = revit_el.LookupParameter(param_name)

        if param is None:
            results.append({'Id': revit_el.Id.IntegerValue, 'Status': 'NOT FOUND'})
            continue

        if not write_mode:
            # ── Read mode ───────────────────────────────────────────────────
            val = (param.AsValueString()
                   or param.AsString()
                   or str(param.AsDouble()))
            results.append({'Id': revit_el.Id.IntegerValue, param_name: val})
        else:
            # ── Write mode ──────────────────────────────────────────────────
            if param.IsReadOnly:
                results.append({'Id': revit_el.Id.IntegerValue, 'Status': 'READ ONLY'})
                continue

            st = param.StorageType
            if   st == StorageType.String:  param.Set(str(new_value))
            elif st == StorageType.Double:  param.Set(float(new_value))
            elif st == StorageType.Integer: param.Set(int(new_value))
            else:
                results.append({'Id': revit_el.Id.IntegerValue,
                                'Status': 'UNSUPPORTED TYPE: ' + str(st)})
                continue

            results.append({'Id': revit_el.Id.IntegerValue,
                            'Status': 'OK',
                            'New Value': new_value})

    if write_mode:
        TransactionManager.Instance.TransactionTaskDone()

    OUT = results

except Exception as e:
    if write_mode:
        TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Common parameter patterns

**Check for empty parameters (compliance check):**
```python
missing = []
for el in collector:
    p = el.LookupParameter('Description')
    if not p or not p.AsString() or p.AsString().strip() == '':
        missing.append({'Id': el.Id.IntegerValue,
                        'Mark': el.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString()})
OUT = missing
```

**Copy value from one parameter to another:**
```python
TransactionManager.Instance.EnsureInTransaction(doc)
for el in collector:
    source = el.LookupParameter('Old Param Name')
    target = el.LookupParameter('New Param Name')
    if source and target and not target.IsReadOnly:
        target.Set(source.AsString())
TransactionManager.Instance.TransactionTaskDone()
```

**Batch-set from Excel (via Data.ImportExcel node):**
```python
## IN[0] = 2D list from Excel: [[element_id, new_value], ...]
data = IN[0]
id_value_map = {int(row[0]): row[1] for row in data if row[0]}

TransactionManager.Instance.EnsureInTransaction(doc)
for el_id_int, val in id_value_map.items():
    el = doc.GetElement(ElementId(el_id_int))
    if el:
        p = el.LookupParameter('Target Param')
        if p and not p.IsReadOnly:
            p.Set(str(val))
TransactionManager.Instance.TransactionTaskDone()
```

### Customization tips

- Parameter names are **case-sensitive** — double-check against the Revit properties panel
- For built-in parameters use `element.get_Parameter(BuiltInParameter.ROOM_NUMBER)` for better reliability
- If `AsValueString()` returns `None`, try `AsString()` then `AsDouble()` — storage type varies by parameter


## shared-parameters

> Create, bind, and manage Revit shared parameters using Dynamo Python — load a shared parameter file, add new parameter definitions to groups, bind parameters to element categories, and verify parameter bindings. Use this skill when a user needs to add shared parameters to their project, bind COBie parameters, set up BEP-required data fields, add parameters to families, or troubleshoot missing shared parameters. Trigger on phrases like "shared parameters", "add parameter", "bind parameter", "shared param file", "project parameters", "create parameter", "COBie fields", "parameter binding", "add fields to schedule", "parameter group", or any request to add new data fields to Revit elements that don't exist yet.

## Shared Parameters — Create, Bind & Manage

Manage shared parameters for:

**"$ARGUMENTS"**

### Before writing code

Ask (one question if ambiguous):
1. **Do you have an existing shared parameter file** (`.txt`), or do you need a new one created?
2. **Which parameters** do you want to add, and to **which categories**?
3. **Instance or Type parameter?** (Instance = per-element, Type = per-family type)

---

### Script 1: Inspect what shared parameters are already bound (read-only)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    binding_map = doc.ParameterBindings
    it = binding_map.ForwardIterator()
    results = []

    while it.MoveNext():
        defn    = it.Key
        binding = it.Current
        cats    = []
        try:
            for cat in binding.Categories:
                cats.append(cat.Name)
        except Exception:
            pass

        results.append({
            "Name":       defn.Name,
            "Type":       "Instance" if isinstance(binding, InstanceBinding) else "Type",
            "Categories": ", ".join(sorted(cats))
        })

    results.sort(key=lambda x: x["Name"])
    OUT = results if results else "No shared or project parameters found."

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 2: Load shared parameter file and bind parameters to categories

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument
app = doc.Application

## ── Configuration ────────────────────────────────────────────────────────────
SHARED_PARAM_FILE = r"C:\BIM\SharedParameters\ProjectSharedParams.txt"

## Parameters to bind: (group_name_in_file, param_name, is_instance, categories_list)
PARAMS_TO_BIND = [
    ("COBie",    "COBie.Type.AssetType",    False,  [BuiltInCategory.OST_Doors,
                                                     BuiltInCategory.OST_Windows,
                                                     BuiltInCategory.OST_MechanicalEquipment]),
    ("COBie",    "COBie.Component.TagNumber", True, [BuiltInCategory.OST_Doors,
                                                     BuiltInCategory.OST_MechanicalEquipment]),
    ("BIM Data", "BIM_Status",              True,   [BuiltInCategory.OST_Walls,
                                                     BuiltInCategory.OST_Floors,
                                                     BuiltInCategory.OST_Rooms]),
    ("BIM Data", "BIM_ResponsibleParty",    True,   [BuiltInCategory.OST_Rooms]),
]
## ─────────────────────────────────────────────────────────────────────────────

def get_or_open_sp_file(app, path):
    """Set the shared parameter file and return it."""
    app.SharedParametersFilename = path
    return app.OpenSharedParameterFile()

try:
    import os
    if not os.path.exists(SHARED_PARAM_FILE):
        OUT = ("ERROR: Shared parameter file not found: " + SHARED_PARAM_FILE +
               "\nCreate the file first or check the path.")
    else:
        sp_file = get_or_open_sp_file(app, SHARED_PARAM_FILE)
        if not sp_file:
            OUT = "ERROR: Could not open shared parameter file."
        else:
            bound_params = []
            skipped = []

            TransactionManager.Instance.EnsureInTransaction(doc)

            for group_name, param_name, is_instance, cat_list in PARAMS_TO_BIND:

                # Find the group
                group = sp_file.Groups.get_Item(group_name)
                if not group:
                    skipped.append(param_name + " (group '" + group_name + "' not found in file)")
                    continue

                # Find the definition in the group
                defn = group.Definitions.get_Item(param_name)
                if not defn:
                    skipped.append(param_name + " (not found in group '" + group_name + "')")
                    continue

                # Check if already bound
                existing = doc.ParameterBindings.get_Item(defn)
                if existing:
                    skipped.append(param_name + " (already bound)")
                    continue

                # Build category set
                cat_set = app.Create.NewCategorySet()
                for bic in cat_list:
                    cat = doc.Settings.Categories.get_Item(bic)
                    if cat and cat.AllowsBoundParameters:
                        cat_set.Insert(cat)

                # Create binding
                if is_instance:
                    binding = app.Create.NewInstanceBinding(cat_set)
                else:
                    binding = app.Create.NewTypeBinding(cat_set)

                # Insert into document
                group_defn = BuiltInParameterGroup.PG_DATA  # show under "Data" in Properties
                doc.ParameterBindings.Insert(defn, binding, group_defn)
                bound_params.append(param_name)

            TransactionManager.Instance.TransactionTaskDone()
            OUT = {"Bound": bound_params, "Skipped": skipped}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 3: Create a new shared parameter file with definitions

Use this when no shared parameter file exists yet.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument
app = doc.Application

## ── Configuration ────────────────────────────────────────────────────────────
NEW_SP_FILE = r"C:\BIM\SharedParameters\NewProjectParams.txt"

## (group_name, param_name, param_type)
## ParameterType options: Text, Integer, Number, Length, Area, YesNo, URL, Material, etc.
PARAMS_TO_CREATE = [
    ("BIM Data", "BIM_Status",             ParameterType.Text),
    ("BIM Data", "BIM_ResponsibleParty",   ParameterType.Text),
    ("BIM Data", "BIM_SubmissionDate",     ParameterType.Text),
    ("COBie",    "COBie.Type.AssetType",   ParameterType.Text),
    ("COBie",    "COBie.Component.TagNumber", ParameterType.Text),
]
## ─────────────────────────────────────────────────────────────────────────────

try:
    import os
    os.makedirs(os.path.dirname(NEW_SP_FILE), exist_ok=True)

    # Create new empty shared parameter file
    app.SharedParametersFilename = NEW_SP_FILE
    # Writing a blank file first so Revit can open it
    if not os.path.exists(NEW_SP_FILE):
        with open(NEW_SP_FILE, 'w') as f:
            f.write("# This is a Revit shared parameter file.\n")
            f.write("# Do not edit manually.\n")
            f.write("*META\tVERSION\tMINVERSION\n")
            f.write("META\t2\t1\n")
            f.write("*GROUP\tID\tNAME\n")
            f.write("*PARAM\tGUID\tNAME\tDATATYPE\tDATACATEGORY\tGROUP\tVISIBLE\tDESCRIPTION\tUSERMODIFIABLE\tHIDEWHENNOVALUE\n")

    sp_file = app.OpenSharedParameterFile()

    created = []
    for group_name, param_name, param_type in PARAMS_TO_CREATE:
        # Get or create group
        group = sp_file.Groups.get_Item(group_name)
        if not group:
            group = sp_file.Groups.Create(group_name)

        # Check if param already exists
        existing = group.Definitions.get_Item(param_name)
        if not existing:
            opts = ExternalDefinitionCreationOptions(param_name, param_type)
            opts.Visible = True
            group.Definitions.Create(opts)
            created.append(group_name + " > " + param_name)

    OUT = {
        "File created": NEW_SP_FILE,
        "Parameters created": created,
        "Next step": "Use Script 2 to bind these parameters to Revit categories."
    }

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Common BuiltInParameterGroup values

| Display name in Properties | BuiltInParameterGroup           |
|----------------------------|---------------------------------|
| Data                       | `PG_DATA`                       |
| Identity Data              | `PG_IDENTITY_DATA`              |
| Other                      | `PG_OTHER`                      |
| Construction               | `PG_CONSTRUCTION`               |
| Mechanical                 | `PG_MECHANICAL`                 |
| Energy Analysis            | `PG_ENERGY_ANALYSIS`            |

### Troubleshooting

- **"AllowsBoundParameters is false"**: Some categories (e.g. Lines, Detail Items) can't have instance parameters bound via the API — use Type binding or a different category.
- **Parameter not appearing in schedules**: Shared parameters appear in schedules; project parameters do not. Make sure you're using a shared parameter file, not `doc.ParameterBindings.Insert` with an `InternalDefinition`.
- **GUID conflicts**: Each shared parameter has a unique GUID. Never duplicate a GUID across files — Revit uses it to match parameters across projects.


## batch-rename-elements

> Batch rename Revit elements across any category using prefixes, suffixes, numbering sequences, or parameter-driven naming rules. Use this skill when a user needs to rename rooms, sheets, views, doors, levels, grids, or any other elements en masse — following a naming convention, BEP standard, or project numbering scheme. Trigger on phrases like "rename elements", "bulk rename", "batch rename", "add prefix", "add suffix", "renumber rooms", "rename views", "rename sheets", "apply naming convention", "fix names", or any request to systematically change element names at scale.

## Batch Rename Elements

Rename Revit elements in bulk for:

**"$ARGUMENTS"**

### Before writing code

Ask (one question only if ambiguous):
1. **Which category?** Rooms, Views, Sheets, Doors, Levels, Grids, or another?
2. **What's the naming pattern?** Prefix + number? Parameter-driven? Find & replace? Sequential?
3. **What parameter holds the name?** Usually `Name` for rooms/views, `Sheet Number`+`Sheet Name` for sheets.

Default: produce a complete, ready-to-run Dynamo script.

---

### Standard rename patterns

#### Pattern A — Add prefix/suffix to all elements in a category

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
CATEGORY    = BuiltInCategory.OST_Rooms   # change to target category
PARAM_NAME  = "Name"                       # parameter that holds the name
PREFIX      = "A-"                         # set "" to skip
SUFFIX      = ""                           # set "" to skip
## ─────────────────────────────────────────────────────────────────────────────

try:
    elements = (FilteredElementCollector(doc)
                .OfCategory(CATEGORY)
                .WhereElementIsNotElementType()
                .ToElements())

    renamed = []
    skipped = []

    TransactionManager.Instance.EnsureInTransaction(doc)

    for el in elements:
        param = el.LookupParameter(PARAM_NAME)
        if param and not param.IsReadOnly:
            old_name = param.AsString() or ""
            # Avoid double-prefixing on re-runs
            if not old_name.startswith(PREFIX):
                new_name = PREFIX + old_name + SUFFIX
                param.Set(new_name)
                renamed.append(old_name + " → " + new_name)
            else:
                skipped.append(old_name + " (already prefixed)")

    TransactionManager.Instance.TransactionTaskDone()

    OUT = {
        "Renamed": renamed,
        "Skipped (already prefixed)": skipped,
        "Total renamed": len(renamed)
    }

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

#### Pattern B — Sequential numbering (e.g. Room 001, Room 002 …)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
CATEGORY     = BuiltInCategory.OST_Rooms
PARAM_NAME   = "Number"          # parameter to write to
BASE_PREFIX  = "R"               # e.g. "R" → R001, R002 …
START_NUMBER = 1
ZERO_PAD     = 3                 # digits to pad: 3 → 001
SORT_PARAM   = "Name"            # sort elements by this before numbering
## ─────────────────────────────────────────────────────────────────────────────

try:
    elements = list(FilteredElementCollector(doc)
                    .OfCategory(CATEGORY)
                    .WhereElementIsNotElementType()
                    .ToElements())

    # Sort alphabetically by name for consistent numbering
    def get_sort_key(el):
        p = el.LookupParameter(SORT_PARAM)
        return p.AsString() if p else ""

    elements.sort(key=get_sort_key)

    results = []
    TransactionManager.Instance.EnsureInTransaction(doc)

    for i, el in enumerate(elements):
        param = el.LookupParameter(PARAM_NAME)
        if param and not param.IsReadOnly:
            number = BASE_PREFIX + str(START_NUMBER + i).zfill(ZERO_PAD)
            old_val = param.AsString() or ""
            param.Set(number)
            results.append(old_val + " → " + number)

    TransactionManager.Instance.TransactionTaskDone()
    OUT = {"Renumbered": results, "Total": len(results)}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

#### Pattern C — Find & Replace in names

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
CATEGORY     = BuiltInCategory.OST_Views
PARAM_NAME   = "Name"
FIND         = "Copy of "         # text to find
REPLACE_WITH = ""                 # replace with (empty = remove it)
CASE_SENS    = False              # True = case-sensitive match
## ─────────────────────────────────────────────────────────────────────────────

try:
    elements = (FilteredElementCollector(doc)
                .OfCategory(CATEGORY)
                .WhereElementIsNotElementType()
                .ToElements())

    results = []
    TransactionManager.Instance.EnsureInTransaction(doc)

    for el in elements:
        param = el.LookupParameter(PARAM_NAME)
        if param and not param.IsReadOnly:
            old_name = param.AsString() or ""
            check_name = old_name if CASE_SENS else old_name.lower()
            check_find = FIND if CASE_SENS else FIND.lower()
            if check_find in check_name:
                if CASE_SENS:
                    new_name = old_name.replace(FIND, REPLACE_WITH)
                else:
                    import re
                    new_name = re.sub(re.escape(FIND), REPLACE_WITH, old_name, flags=re.IGNORECASE)
                param.Set(new_name)
                results.append('"' + old_name + '" → "' + new_name + '"')

    TransactionManager.Instance.TransactionTaskDone()
    OUT = {"Renamed": results, "Count": len(results)}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Category reference

| Target         | BuiltInCategory              | Name param       |
|----------------|------------------------------|------------------|
| Rooms          | `OST_Rooms`                  | `Name`, `Number` |
| Views          | `OST_Views`                  | `Name`           |
| Sheets         | `OST_Sheets`                 | `Name`, `Sheet Number` |
| Doors          | `OST_Doors`                  | `Mark`           |
| Windows        | `OST_Windows`                | `Mark`           |
| Levels         | `OST_Levels`                 | `Name`           |
| Grids          | `OST_Grids`                  | `Name`           |
| Areas          | `OST_Areas`                  | `Name`, `Number` |

### Safety notes

- Always warn the user this **modifies the model** — recommend testing on a detached copy first.
- The prefix-check (`startswith`) prevents double-prefixing on re-runs.
- For sheets, `Sheet Number` and `Name` are separate parameters — handle both if needed.

### Output

Tell the user:
- How many elements were renamed
- A sample of the before/after pairs
- Which elements were skipped and why


## manipulate-elements

> Move, rotate, copy, delete, modify types, or batch-edit Revit model elements using Dynamo Python. Use this skill when performing actions and geometric transformations on elements — translating elements, changing their type, batch-editing families, swapping types, mirroring, rotating, or any operation that modifies element geometry or identity. Trigger on phrases like "move elements", "rotate", "copy elements", "change type", "batch edit", "swap family", "modify elements", "transform", "mirror elements", or any request to programmatically manipulate existing Revit elements. Always warn the user to test on a copy of the model first before running destructive operations.

## Manipulate Revit Elements

Perform the following action on Revit elements:

**"$ARGUMENTS"**

### Before scripting

Important: **always warn the user** — this type of script modifies the model. Recommend:
1. Save a local backup first (Save As → make a copy)
2. Test on a small set of elements before running on the whole model
3. Ctrl+Z works in Revit after Dynamo runs — but only if the transaction closed cleanly

Clarify:
- **Which elements?** Collect by category, or receive from an upstream Dynamo node?
- **What transformation?** Move (vector), rotate (axis + angle), change type (new type ID), etc.
- **How are elements passed in?** As Dynamo-wrapped objects (from nodes) or native Revit elements?

### Element modification template

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

## Unwrap Dynamo-wrapped elements to native Revit elements
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

doc = DocumentManager.Instance.CurrentDBDocument

## IN[0] = list of elements from upstream Dynamo node
elements = IN[0] if isinstance(IN[0], list) else [IN[0]]

modified = []
errors   = []

TransactionManager.Instance.EnsureInTransaction(doc)
try:
    for el in elements:
        # Unwrap if element came from a Dynamo node
        revit_el = el.InternalElement if hasattr(el, 'InternalElement') else el

        # ── Your modification here ───────────────────────────────────────────
        # Example A: Move element 1m in the X direction
        # translation = XYZ(3.28084, 0, 0)  # 1 metre in X (Revit uses feet)
        # ElementTransformUtils.MoveElement(doc, revit_el.Id, translation)

        # Example B: Change element type
        # new_type_id = ElementId(123456)  # get from a Type Collector node
        # revit_el.ChangeTypeId(new_type_id)

        # Example C: Rotate 90° around element's Z axis
        # from Autodesk.Revit.DB import Line
        # origin = revit_el.Location.Point
        # axis   = Line.CreateBound(origin, origin + XYZ.BasisZ)
        # import math
        # ElementTransformUtils.RotateElement(doc, revit_el.Id, axis, math.pi / 2)

        modified.append(revit_el.Id.IntegerValue)

    TransactionManager.Instance.TransactionTaskDone()

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    errors.append(str(e))

OUT = [modified, errors]
```

### Common transformation patterns

**Move all elements in a category by a vector:**
```python
## Shift everything 500mm in Z (e.g. raise a floor level)
z_shift_ft = 500 / 304.8  # convert mm to feet
vector = XYZ(0, 0, z_shift_ft)

collector = (FilteredElementCollector(doc)
             .OfCategory(BuiltInCategory.OST_Floors)
             .WhereElementIsNotElementType()
             .ToElements())

TransactionManager.Instance.EnsureInTransaction(doc)
for el in collector:
    ElementTransformUtils.MoveElement(doc, el.Id, vector)
TransactionManager.Instance.TransactionTaskDone()
OUT = 'Moved ' + str(len(list(collector))) + ' floors by 500mm'
```

**Batch change family type:**
```python
## IN[0] = list of elements
## IN[1] = new type name (string)
## IN[2] = category (e.g. "OST_Doors")
elements   = IN[0]
type_name  = IN[1]
bic        = getattr(BuiltInCategory, IN[2])

new_type = next((t for t in FilteredElementCollector(doc)
                 .OfCategory(bic)
                 .WhereElementIsElementType().ToElements()
                 if t.Name == type_name), None)

if not new_type:
    OUT = 'Type not found: ' + type_name
else:
    TransactionManager.Instance.EnsureInTransaction(doc)
    count = 0
    for el in elements:
        revit_el = el.InternalElement if hasattr(el, 'InternalElement') else el
        revit_el.ChangeTypeId(new_type.Id)
        count += 1
    TransactionManager.Instance.TransactionTaskDone()
    OUT = 'Changed ' + str(count) + ' elements to type: ' + type_name
```

**Mirror elements about a vertical plane:**
```python
## Mirror about the X-axis through the model origin
mirror_plane = Plane.CreateByNormalAndOrigin(XYZ.BasisX, XYZ.Zero)
ids_to_mirror = [el.Id for el in elements]

TransactionManager.Instance.EnsureInTransaction(doc)
ElementTransformUtils.MirrorElements(doc, ids_to_mirror, mirror_plane, True)
TransactionManager.Instance.TransactionTaskDone()
```

### Unit conversion reminder

Revit's internal unit for length is **decimal feet**. Always convert:
- `mm → ft`: divide by 304.8
- `m → ft`: divide by 0.3048
- `ft → mm`: multiply by 304.8

Example: `XYZ(1000 / 304.8, 0, 0)` moves 1000mm in X.


## create-view-filters

> Create, configure, and apply Revit view filters and graphic overrides using Dynamo Python. Use this skill when a user wants to color-code elements by parameter value, create filters based on phase, status, type, department, workset, or any custom parameter, apply those filters to multiple views at once, or override element visibility by rule. Trigger on phrases like "view filter", "color code elements", "graphic overrides", "color by parameter", "filter by phase", "highlight elements", "visibility graphics", "create filters", "apply filters to views", or any request to visually distinguish elements in Revit views.

## Create View Filters & Graphic Overrides

Create and apply Revit view filters for:

**"$ARGUMENTS"**

### Before writing code

Clarify (one question if ambiguous):
1. **Which parameter** drives the filter? (e.g. Phase, Status, Department, Type Mark, Workset)
2. **Which views** should filters be applied to? (Active view, all floor plans, specific view names?)
3. **What colors/overrides?** (Specific colors per value, or just hide/show?)

---

### Script: Create parametric filter and apply to views

This script creates ParameterFilterElement rules and applies graphic overrides. **Modifies the model.**

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import List

doc  = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ────────────────────────────────────────────────────────────
## Categories the filter applies to
TARGET_CATEGORIES = [
    BuiltInCategory.OST_Walls,
    BuiltInCategory.OST_Floors,
    BuiltInCategory.OST_Roofs,
]

## Parameter to filter on (exact name, case-sensitive)
FILTER_PARAM_NAME = "Phase Created"   # or use a BuiltInParameter below

## Filter rules: each entry = (filter_name, param_value_to_match, RGB_color_tuple)
## The script creates one filter per rule.
FILTER_RULES = [
    ("Phase - New Construction", "New Construction", (0, 150, 255)),   # blue
    ("Phase - Existing",         "Existing",         (180, 180, 180)), # grey
    ("Phase - Demolished",       "Demolished",       (255, 80, 80)),   # red
]

## Apply filters to ALL floor plan views? Set to False to use APPLY_TO_VIEW_NAMES list.
APPLY_TO_ALL_FLOOR_PLANS = True
APPLY_TO_VIEW_NAMES = ["Level 1", "Level 2"]   # used only if above is False
## ─────────────────────────────────────────────────────────────────────────────

def make_color(r, g, b):
    return Color(r, g, b)

def get_param_id(doc, cat_ids, param_name):
    """Return the ElementId of a shared/project parameter by name."""
    # Try BuiltInParameter first for common phase params
    bp_map = {
        "Phase Created": BuiltInParameter.PHASE_CREATED,
        "Phase Demolished": BuiltInParameter.PHASE_DEMOLISHED,
    }
    if param_name in bp_map:
        return ElementId(bp_map[param_name])
    # Fall back to iterating shared parameters
    binding_map = doc.ParameterBindings
    it = binding_map.ForwardIterator()
    while it.MoveNext():
        defn = it.Key
        if defn.Name == param_name:
            # Get ElementId via ParameterElement
            for pe in FilteredElementCollector(doc).OfClass(ParameterElement).ToElements():
                if pe.GetDefinition().Name == param_name:
                    return pe.Id
    return None

try:
    # Collect category IDs
    cat_id_list = List[ElementId]()
    for bic in TARGET_CATEGORIES:
        cat = doc.Settings.Categories.get_Item(bic)
        if cat:
            cat_id_list.Add(cat.Id)

    # Get the target views
    all_views = list(FilteredElementCollector(doc).OfClass(View).ToElements())
    if APPLY_TO_ALL_FLOOR_PLANS:
        target_views = [v for v in all_views
                        if v.ViewType == ViewType.FloorPlan and not v.IsTemplate]
    else:
        target_views = [v for v in all_views
                        if v.Name in APPLY_TO_VIEW_NAMES and not v.IsTemplate]

    param_id = get_param_id(doc, cat_id_list, FILTER_PARAM_NAME)
    if not param_id:
        OUT = "ERROR: Could not find parameter '" + FILTER_PARAM_NAME + "'. Check the exact name."
    else:
        created_filters = []
        TransactionManager.Instance.EnsureInTransaction(doc)

        for filter_name, match_value, (r, g, b) in FILTER_RULES:
            # Check if filter already exists — delete and recreate to update
            existing = [f for f in FilteredElementCollector(doc)
                            .OfClass(ParameterFilterElement).ToElements()
                        if f.Name == filter_name]
            for old in existing:
                doc.Delete(old.Id)

            # Build the filter rule: parameter equals string value
            rule = ParameterFilterRuleFactory.CreateEqualsRule(
                param_id,
                match_value,
                True   # case-sensitive
            )
            elem_filter = ElementParameterFilter(rule)

            # Create the ParameterFilterElement
            pf = ParameterFilterElement.Create(doc, filter_name, cat_id_list, elem_filter)

            # Build graphic overrides
            ogs = OverrideGraphicSettings()
            col = make_color(r, g, b)
            ogs.SetProjectionLineColor(col)
            ogs.SetSurfaceForegroundPatternColor(col)
            ogs.SetSurfaceForegroundPatternVisible(True)

            # Apply to each target view
            for view in target_views:
                try:
                    view.AddFilter(pf.Id)
                    view.SetFilterOverrides(pf.Id, ogs)
                    view.SetFilterVisibility(pf.Id, True)
                except Exception:
                    pass  # skip views that don't support the filter

            created_filters.append(filter_name)

        TransactionManager.Instance.TransactionTaskDone()
        OUT = {
            "Filters created": created_filters,
            "Applied to views": [v.Name for v in target_views],
            "Parameter used": FILTER_PARAM_NAME
        }

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script: List existing filters in the model (read-only)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    filters = list(FilteredElementCollector(doc)
                   .OfClass(ParameterFilterElement).ToElements())
    result = []
    for f in filters:
        cats = [doc.Settings.Categories.get_Item(cid).Name
                for cid in f.GetCategories()
                if doc.Settings.Categories.get_Item(cid) is not None]
        result.append({"Name": f.Name, "Categories": ", ".join(cats)})
    OUT = result if result else "No view filters found in this model."
except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Common filter parameters

| Goal                        | Parameter name          | BuiltInParameter               |
|-----------------------------|-------------------------|--------------------------------|
| Filter by phase             | `Phase Created`         | `PHASE_CREATED`                |
| Filter by phase demolished  | `Phase Demolished`      | `PHASE_DEMOLISHED`             |
| Filter by workset           | `Workset`               | `ELEM_PARTITION_PARAM`         |
| Filter by type mark         | `Type Mark`             | `WINDOW_TYPE_ID` (doors/wins)  |
| Filter by department        | `Department`            | `ROOM_DEPARTMENT`              |
| Filter by design option     | `Design Option`         | `DESIGN_OPTION_ID`             |

### Customization tips

- **Multiple categories**: add more `BuiltInCategory` entries to `TARGET_CATEGORIES`
- **Solid fill**: also call `ogs.SetSurfaceForegroundPatternId(solid_fill_pattern_id)` with the filled-region pattern Id
- **Halftone / transparency**: `ogs.SetHalftone(True)` or `ogs.SetSurfaceTransparency(50)`
- **String vs Integer parameters**: use `CreateEqualsRule` for strings, `CreateGreaterOrEqualRule` for numbers


---

# Project & sheet setup


## project-setup

> Automate Revit project setup — create worksets, levels, grids, view templates, browser organization schemes, and standard views from a project brief or BIM Execution Plan. Use this skill at project start when a user needs to set up a new Revit model from scratch or bring an existing model up to BIM standards. Trigger on phrases like "project setup", "set up the model", "create worksets", "add levels", "set up grids", "create view templates", "BEP setup", "model template", "create standard views", "set up browser organisation", "new project setup", "initialise the model", or any request to configure a Revit model for a new project. Also offer this skill when a user complains their model doesn't have proper worksets or is missing standard views.

## Revit Project Setup Automation

Set up the Revit model for:

**"$ARGUMENTS"**

### Before writing code

Ask (one question if ambiguous):
1. **What project type?** Residential, commercial, mixed-use, infrastructure?
2. **Which components?** Worksets, levels, grids, view templates, standard views — or all?
3. **Any specific names/numbers?** (e.g. level heights, grid spacing, workset names from BEP)

Each script below is standalone — run only what's needed.

---

### Script 1: Create worksets from a list

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ─────────────────────────────────────────────────────────
WORKSET_NAMES = [
    "Architecture",
    "Structure",
    "MEP",
    "Site",
    "Interiors",
    "Shared Levels and Grids",
    "Linked Models",
    "CAD Links",
]
## ─────────────────────────────────────────────────────────────────────────

try:
    if not doc.IsWorkshared:
        OUT = "ERROR: This model is not workshared. Enable worksharing first (Collaborate > Worksets)."
    else:
        existing = [ws.Name for ws in
                    FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()]
        created = []
        skipped = []

        TransactionManager.Instance.EnsureInTransaction(doc)

        for name in WORKSET_NAMES:
            if name not in existing:
                Workset.Create(doc, name)
                created.append(name)
            else:
                skipped.append(name + " (already exists)")

        TransactionManager.Instance.TransactionTaskDone()
        OUT = {"Created": created, "Skipped": skipped}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 2: Create levels at specified heights

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ─────────────────────────────────────────────────────────
## (name, height in mm above datum)
LEVELS = [
    ("00 Ground Floor",   0),
    ("01 First Floor",    3600),
    ("02 Second Floor",   7200),
    ("03 Third Floor",    10800),
    ("04 Fourth Floor",   14400),
    ("Roof Level",        18000),
]

MM_TO_FT = 1.0 / 304.8   # Revit stores lengths in decimal feet
## ─────────────────────────────────────────────────────────────────────────

try:
    existing_names = [l.Name for l in
                      FilteredElementCollector(doc).OfClass(Level).ToElements()]
    created = []
    skipped = []

    TransactionManager.Instance.EnsureInTransaction(doc)

    for level_name, height_mm in LEVELS:
        if level_name in existing_names:
            skipped.append(level_name + " (already exists)")
            continue

        height_ft = height_mm * MM_TO_FT
        new_level = Level.Create(doc, height_ft)
        new_level.Name = level_name
        created.append(level_name + " @ " + str(height_mm) + " mm")

    TransactionManager.Instance.TransactionTaskDone()
    OUT = {"Created levels": created, "Skipped": skipped}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 3: Create a grid layout (orthogonal)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ─────────────────────────────────────────────────────────
## Vertical grids (along X axis) — positions in mm from origin
VERTICAL_GRID_POSITIONS = [0, 6000, 12000, 18000, 24000]
VERTICAL_GRID_LABELS    = ["A", "B", "C", "D", "E"]

## Horizontal grids (along Y axis) — positions in mm from origin
HORIZONTAL_GRID_POSITIONS = [0, 7500, 15000, 22500]
HORIZONTAL_GRID_LABELS    = ["1", "2", "3", "4"]

GRID_LENGTH_MM = 30000   # total length of grid lines
MM_TO_FT = 1.0 / 304.8
## ─────────────────────────────────────────────────────────────────────────

def ft(mm):
    return mm * MM_TO_FT

try:
    created_grids = []
    TransactionManager.Instance.EnsureInTransaction(doc)

    # Vertical grids (run top to bottom, i.e. in Y direction)
    for i, x_mm in enumerate(VERTICAL_GRID_POSITIONS):
        x = ft(x_mm)
        start = XYZ(x, ft(-2000), 0)
        end   = XYZ(x, ft(GRID_LENGTH_MM), 0)
        line  = Line.CreateBound(start, end)
        grid  = Grid.Create(doc, line)
        label = VERTICAL_GRID_LABELS[i] if i < len(VERTICAL_GRID_LABELS) else str(i+1)
        grid.Name = label
        created_grids.append("Vertical " + label + " @ X=" + str(x_mm) + "mm")

    # Horizontal grids (run left to right, i.e. in X direction)
    for j, y_mm in enumerate(HORIZONTAL_GRID_POSITIONS):
        y = ft(y_mm)
        start = XYZ(ft(-2000), y, 0)
        end   = XYZ(ft(GRID_LENGTH_MM), y, 0)
        line  = Line.CreateBound(start, end)
        grid  = Grid.Create(doc, line)
        label = HORIZONTAL_GRID_LABELS[j] if j < len(HORIZONTAL_GRID_LABELS) else str(j+1)
        grid.Name = label
        created_grids.append("Horizontal " + label + " @ Y=" + str(y_mm) + "mm")

    TransactionManager.Instance.TransactionTaskDone()
    OUT = {"Grids created": created_grids, "Total": len(created_grids)}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Script 4: Create standard floor plan views for all levels

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Configuration ─────────────────────────────────────────────────────────
## View types to create per level
VIEW_SUFFIXES = ["_ARCH", "_STRUCT", "_MEP"]
VIEW_FAMILY   = ViewFamily.FloorPlan    # or ViewFamily.CeilingPlan
## ─────────────────────────────────────────────────────────────────────────

try:
    levels     = list(FilteredElementCollector(doc).OfClass(Level).ToElements())
    view_types = list(FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements())
    fp_type    = next((vt for vt in view_types if vt.ViewFamily == VIEW_FAMILY), None)

    if not fp_type:
        OUT = "ERROR: No Floor Plan view family type found in document."
    else:
        existing_view_names = {v.Name for v in
                               FilteredElementCollector(doc).OfClass(View).ToElements()}
        created = []

        TransactionManager.Instance.EnsureInTransaction(doc)

        for level in levels:
            for suffix in VIEW_SUFFIXES:
                view_name = level.Name + suffix
                if view_name not in existing_view_names:
                    new_view = ViewPlan.Create(doc, fp_type.Id, level.Id)
                    new_view.Name = view_name
                    created.append(view_name)

        TransactionManager.Instance.TransactionTaskDone()
        OUT = {"Views created": created, "Total": len(created)}

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Recommended setup sequence

Tell the user to run scripts in this order:
1. **Script 1** — Create worksets (model must already be workshared)
2. **Script 2** — Create levels
3. **Script 3** — Create grids
4. **Script 4** — Create standard views per level
5. Then: use `manage-sheets` skill to create the drawing register

### Safety notes

- Workset creation requires a workshared model. If not workshared, instruct the user to go to Collaborate → Worksets first.
- Level and grid creation modifies the model — recommend running on a fresh model or a detached copy.
- View names must be unique — the scripts check for duplicates before creating.


## manage-sheets

> Create, organise, and manage Revit drawing sheets and views using Dynamo Python. Use this skill when creating sheets from a list (e.g. from Excel), placing views onto sheets, applying view templates, renaming or renumbering sheets, automating sheet set creation, or reorganising the drawing register. Trigger on phrases like "create sheets", "batch create sheets", "add views to sheets", "sheet setup", "drawing register", "sheet numbering", "place views", "apply view template", "sheets from Excel", or any request involving Revit sheet management. Also offer this skill when users are setting up a new project or preparing for a drawing issue.

## Manage Revit Sheets & Views

Perform sheet/view operation:

**"$ARGUMENTS"**

### Clarify before scripting

- **Create new sheets** or **modify existing ones?**
- **Where does the sheet list come from?** (Dynamo input, Excel, hardcoded in script?)
- **Which title block** should be used? (Get the first available one, or ask for the name?)
- **Place views on sheets?** If so, which views, at which positions?

### Batch sheet creation script

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## ── Dynamo inputs ────────────────────────────────────────────────────────────
## IN[0] = list of sheet numbers (strings), e.g. ["A-001", "A-002", "A-003"]
## IN[1] = list of sheet names (strings),   e.g. ["Ground Floor Plan", "Roof Plan", "Sections"]
sheet_numbers = IN[0] if isinstance(IN[0], list) else [IN[0]]
sheet_names   = IN[1] if isinstance(IN[1], list) else [IN[1]]

## ── Get the first available title block type ─────────────────────────────────
tb_types = list(FilteredElementCollector(doc)
                .OfCategory(BuiltInCategory.OST_TitleBlocks)
                .WhereElementIsElementType()
                .ToElements())
tb_id = tb_types[0].Id if tb_types else ElementId.InvalidElementId

TransactionManager.Instance.EnsureInTransaction(doc)
created = []
skipped = []

try:
    for number, name in zip(sheet_numbers, sheet_names):
        # Check if sheet number already exists
        existing = [v for v in FilteredElementCollector(doc)
                    .OfClass(ViewSheet).ToElements()
                    if v.SheetNumber == number]
        if existing:
            skipped.append({'Number': number, 'Status': 'Already exists'})
            continue

        sheet = ViewSheet.Create(doc, tb_id)
        sheet.SheetNumber = number
        sheet.Name = name
        created.append({
            'Number': number,
            'Name':   name,
            'Id':     sheet.Id.IntegerValue,
            'Status': 'Created'
        })

    TransactionManager.Instance.TransactionTaskDone()
    OUT = [created, skipped]

except Exception as e:
    TransactionManager.Instance.ForceCloseTransaction()
    import traceback
    OUT = 'ERROR: ' + str(e) + '\n' + traceback.format_exc()
```

### Place a view onto a sheet

```python
## IN[0] = sheet number (string)
## IN[1] = view name (string)
## IN[2] = placement point [x, y] in sheet coordinates (optional, defaults to centre)
sheet_number = IN[0]
view_name    = IN[1]
point_xy     = IN[2] if len(IN) > 2 else [0.3, 0.3]

sheet = next((v for v in FilteredElementCollector(doc)
              .OfClass(ViewSheet).ToElements()
              if v.SheetNumber == sheet_number), None)

view = next((v for v in FilteredElementCollector(doc)
             .OfClass(View).ToElements()
             if v.Name == view_name
             and not v.IsTemplate), None)

if sheet and view:
    if Viewport.CanAddViewToSheet(doc, sheet.Id, view.Id):
        TransactionManager.Instance.EnsureInTransaction(doc)
        placement = XYZ(point_xy[0], point_xy[1], 0)
        vp = Viewport.Create(doc, sheet.Id, view.Id, placement)
        TransactionManager.Instance.TransactionTaskDone()
        OUT = 'Placed view "' + view_name + '" on sheet ' + sheet_number
    else:
        OUT = 'View is already on a sheet or cannot be placed'
else:
    OUT = 'Sheet or view not found'
```

### Apply a view template to multiple views

```python
## IN[0] = view template name (string)
## IN[1] = list of view names to apply it to
template_name = IN[0]
view_names    = IN[1]

template = next((v for v in FilteredElementCollector(doc)
                 .OfClass(View).ToElements()
                 if v.IsTemplate and v.Name == template_name), None)

if not template:
    OUT = 'Template not found: ' + template_name
else:
    TransactionManager.Instance.EnsureInTransaction(doc)
    applied = []
    for vname in view_names:
        v = next((vw for vw in FilteredElementCollector(doc)
                  .OfClass(View).ToElements()
                  if vw.Name == vname and not vw.IsTemplate), None)
        if v:
            v.ViewTemplateId = template.Id
            applied.append(vname)
    TransactionManager.Instance.TransactionTaskDone()
    OUT = 'Applied template to: ' + str(applied)
```

### Rename / renumber sheets from Excel

If the user has a spreadsheet with new numbers and names:

```python
## IN[0] = 2D list from Excel: [[old_number, new_number, new_name], ...]
data = IN[0]

TransactionManager.Instance.EnsureInTransaction(doc)
results = []
for old_num, new_num, new_name in data:
    sheet = next((v for v in FilteredElementCollector(doc)
                  .OfClass(ViewSheet).ToElements()
                  if v.SheetNumber == str(old_num)), None)
    if sheet:
        sheet.SheetNumber = str(new_num)
        sheet.Name        = str(new_name)
        results.append({'Old': old_num, 'New': new_num, 'Status': 'OK'})
    else:
        results.append({'Old': old_num, 'New': new_num, 'Status': 'NOT FOUND'})
TransactionManager.Instance.TransactionTaskDone()
OUT = results
```

### Customisation tips

- **Title block**: if `tb_types` returns empty, the model has no loaded title block family — load one first from `Insert → Load Family`
- **Sheet coordinates**: Revit sheet coordinates are in feet; `XYZ(0.3, 0.3, 0)` places the view roughly in the lower-left area of a standard sheet
- **Viewport positions**: after placing, use `vp.SetBoxCenter()` to reposition precisely


---

# Autodesk Construction Cloud (APS)


## acc-api-setup

> Set up Python authentication and a reusable client for the Autodesk Platform Services (APS) API to access Autodesk Construction Cloud (ACC). Use this skill first before any other ACC API script — it handles OAuth2 token acquisition (2-legged and 3-legged), environment configuration, hub/project discovery, and the Python boilerplate that all ACC API scripts depend on. Trigger on phrases like "ACC API setup", "authenticate with APS", "get an APS token", "connect to ACC", "Autodesk API token", "APS credentials", "set up Forge API", "configure ACC API", "get access token Autodesk", or whenever a user is starting to write ACC/APS API scripts and needs the authentication foundation. Always offer this skill before any other ACC API skill if the user hasn't authenticated yet.

## ACC / APS API Setup & Authentication

Set up Python access to Autodesk Construction Cloud for:

**"$ARGUMENTS"**

### Prerequisites

Before writing any code, the user needs:
1. An APS app registered at [APS Developer Portal](https://aps.autodesk.com/)
2. A **Client ID** and **Client Secret** from their app
3. The app provisioned to their ACC account (ACC Admin → Apps & Integrations → Custom Integrations)
4. Python 3.8+ with `requests` installed (`pip install requests`)

Ask the user which flow they need:
- **2-legged** (server-to-server, no user login) — for automation scripts, reporting, data extraction
- **3-legged** (user authorises in browser) — for user-specific data: issues, RFIs, personal ACC content

---

### Script 1: 2-Legged Token (Client Credentials — most common for automation)

```python
import os
import requests
import base64
import time

## ── Configuration — use environment variables, never hardcode secrets ─────────
CLIENT_ID     = os.environ.get("APS_CLIENT_ID", "YOUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("APS_CLIENT_SECRET", "YOUR_CLIENT_SECRET")

## Scopes for typical ACC read/write operations
SCOPES = "data:read data:write account:read"

APS_AUTH_URL = "https://developer.api.autodesk.com/authentication/v2/token"
## ─────────────────────────────────────────────────────────────────────────────

class APSClient:
    """Reusable APS client that auto-refreshes the 2-legged token."""

    def __init__(self, client_id, client_secret, scopes):
        self.client_id     = client_id
        self.client_secret = client_secret
        self.scopes        = scopes
        self._token        = None
        self._expires_at   = 0

    def _credentials_header(self):
        """Base64-encode client_id:client_secret for Basic auth (OAuth2 v2)."""
        creds = base64.b64encode(
            (self.client_id + ":" + self.client_secret).encode()
        ).decode()
        return "Basic " + creds

    def get_token(self):
        """Return a valid access token, refreshing if needed."""
        if self._token and time.time() < self._expires_at - 60:
            return self._token

        resp = requests.post(
            APS_AUTH_URL,
            headers={
                "Authorization": self._credentials_header(),
                "Content-Type":  "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "client_credentials",
                "scope":      self.scopes,
            }
        )
        resp.raise_for_status()
        data = resp.json()
        self._token      = data["access_token"]
        self._expires_at = time.time() + data["expires_in"]
        return self._token

    def headers(self):
        """Return headers dict ready to pass to any APS API call."""
        return {
            "Authorization": "Bearer " + self.get_token(),
            "Content-Type":  "application/json",
        }

    def get(self, url, params=None):
        r = requests.get(url, headers=self.headers(), params=params)
        r.raise_for_status()
        return r.json()

    def post(self, url, payload):
        r = requests.post(url, headers=self.headers(), json=payload)
        r.raise_for_status()
        return r.json()

    def patch(self, url, payload):
        r = requests.patch(url, headers=self.headers(), json=payload)
        r.raise_for_status()
        return r.json()


## ── Usage example ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    client = APSClient(CLIENT_ID, CLIENT_SECRET, SCOPES)
    print("Token acquired:", client.get_token()[:20] + "...")
```

---

### Script 2: Discover your Hub ID and Project IDs

Run this after authentication to find the IDs you need for all other scripts.

```python
import requests, os
## Assumes APSClient class from Script 1 is available

BASE_URL = "https://developer.api.autodesk.com"

def list_hubs(client):
    """List all accessible hubs (ACC accounts)."""
    data = client.get(BASE_URL + "/project/v1/hubs")
    hubs = []
    for h in data.get("data", []):
        hubs.append({
            "Hub Name": h["attributes"]["name"],
            "Hub ID":   h["id"],           # Use this as HUB_ID in other scripts
            "Region":   h["attributes"].get("region", ""),
        })
    return hubs

def list_projects(client, hub_id):
    """List all projects in a hub."""
    data = client.get(BASE_URL + f"/project/v1/hubs/{hub_id}/projects")
    projects = []
    for p in data.get("data", []):
        # ACC project IDs start with "b." — strip it for Model Coordination API calls
        projects.append({
            "Project Name": p["attributes"]["name"],
            "Project ID":   p["id"],       # Use this (with b. prefix) for Data Management API
            "ACC ID":       p["id"].replace("b.", ""),  # Use this for Model Coord, Issues APIs
            "Status":       p["attributes"].get("status", ""),
        })
    return projects

if __name__ == "__main__":
    client = APSClient(CLIENT_ID, CLIENT_SECRET, SCOPES)

    print("=== HUBS ===")
    hubs = list_hubs(client)
    for h in hubs:
        print(f"  {h['Hub Name']}  →  Hub ID: {h['Hub ID']}")

    if hubs:
        hub_id = hubs[0]["Hub ID"]
        print(f"\n=== PROJECTS IN {hubs[0]['Hub Name']} ===")
        projects = list_projects(client, hub_id)
        for p in projects:
            print(f"  {p['Project Name']}")
            print(f"    Data Mgmt ID: {p['Project ID']}")
            print(f"    ACC ID:       {p['ACC ID']}")
```

---

### Script 3: 3-Legged Token (for user-scoped APIs — Issues, RFIs, Submittals)

Use this when the ACC API requires a user identity (not a service account).

```python
import os, webbrowser, urllib.parse, http.server, threading, requests, base64

CLIENT_ID     = os.environ.get("APS_CLIENT_ID")
CLIENT_SECRET = os.environ.get("APS_CLIENT_SECRET")
REDIRECT_URI  = "http://localhost:8080/callback"
SCOPES        = "data:read data:write"

## Step 1: Build the authorization URL and open it in the browser
AUTH_URL = "https://developer.api.autodesk.com/authentication/v2/authorize"
params = {
    "response_type": "code",
    "client_id":     CLIENT_ID,
    "redirect_uri":  REDIRECT_URI,
    "scope":         SCOPES,
}
auth_url = AUTH_URL + "?" + urllib.parse.urlencode(params)
print("Opening browser for authorization...")
webbrowser.open(auth_url)

## Step 2: Local server to catch the callback code
auth_code = {"value": None}

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        auth_code["value"] = qs.get("code", [None])[0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"<h2>Auth complete. You can close this window.</h2>")
    def log_message(self, *args): pass

server = http.server.HTTPServer(("localhost", 8080), CallbackHandler)
t = threading.Thread(target=server.handle_request)
t.start()
t.join(timeout=60)

## Step 3: Exchange code for access token
creds = base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode()).decode()
resp = requests.post(
    "https://developer.api.autodesk.com/authentication/v2/token",
    headers={"Authorization": "Basic " + creds,
             "Content-Type": "application/x-www-form-urlencoded"},
    data={"grant_type": "authorization_code",
          "code": auth_code["value"],
          "redirect_uri": REDIRECT_URI}
)
resp.raise_for_status()
token_data = resp.json()
ACCESS_TOKEN  = token_data["access_token"]
REFRESH_TOKEN = token_data["refresh_token"]
print("3-legged token acquired:", ACCESS_TOKEN[:20] + "...")
```

---

### Key API base URLs and ID conventions

| API                   | Base URL                                              | Auth     |
|-----------------------|-------------------------------------------------------|----------|
| Authentication v2     | `https://developer.api.autodesk.com/authentication/v2` | —        |
| Data Management v1    | `https://developer.api.autodesk.com/data/v1`          | 2-legged |
| Project v1 (hubs)     | `https://developer.api.autodesk.com/project/v1`       | 2-legged |
| ACC Issues v1         | `https://developer.api.autodesk.com/construction/issues/v1` | 3-legged |
| Model Coordination v2 | `https://developer.api.autodesk.com/modelcoordination/modelset/v2` | 2-legged |
| ACC Sheets v1         | `https://developer.api.autodesk.com/construction/sheets/v1` | 2-legged |

### ID convention guide

- **Hub ID**: `b.{account_id}` — used in `/project/v1/hubs/{hub_id}`
- **Project ID (Data Mgmt)**: `b.{project_id}` — used in `/data/v1/projects/{project_id}`
- **Project ID (Issues/Model Coord)**: `{project_id}` — **without** the `b.` prefix
- **Container ID** (Model Coordination): same as raw project ID without `b.`

### Environment variable setup

Always store credentials as environment variables — never hardcode:

```bash
## Windows (PowerShell)
$env:APS_CLIENT_ID     = "your_client_id"
$env:APS_CLIENT_SECRET = "your_client_secret"

## Mac/Linux
export APS_CLIENT_ID="your_client_id"
export APS_CLIENT_SECRET="your_client_secret"
```

Or use a `.env` file with `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()   # reads .env file automatically
```


## acc-docs

> Manage Autodesk Construction Cloud (ACC) Docs — list folders and files, upload documents, download files, create folder structures, manage transmittals, reviews, and packages via the APS Data Management API and ACC Docs REST API. Use this skill when a user needs to automate document control workflows in ACC: bulk uploading drawing sets, creating folder structures, listing published files, downloading specific versions, setting up transmittals, creating document packages, or writing reports of what's in their ACC Docs library. Trigger on phrases like "ACC Docs", "upload to ACC", "download from ACC", "list files in ACC", "document control", "ACC folder", "transmittal", "document package", "file versions", "publish drawings", "drawing register", "ACC file management", or any request to read, write, or organise files in Autodesk Construction Cloud Docs.

## ACC Docs — Document Management via APS API

Manage ACC Docs for:

**"$ARGUMENTS"**

### Prerequisites

- APS credentials set up (use `acc-api-setup` skill first)
- `APSClient` class available (from acc-api-setup)
- Hub ID and Project ID known (run the discovery script in acc-api-setup)
- `pip install requests`

---

### Script 1: List all files in a folder (recursive)

```python
import os, requests

## ── Configuration ─────────────────────────────────────────────────────────────
HUB_ID     = os.environ.get("APS_HUB_ID",     "b.YOUR_HUB_ID")
PROJECT_ID = os.environ.get("APS_PROJECT_ID", "b.YOUR_PROJECT_ID")   # with b. prefix

BASE_URL = "https://developer.api.autodesk.com"
## ─────────────────────────────────────────────────────────────────────────────

def get_top_folders(client, hub_id, project_id):
    """Get the top-level folders in an ACC project."""
    url  = f"{BASE_URL}/project/v1/hubs/{hub_id}/projects/{project_id}/topFolders"
    data = client.get(url)
    return data.get("data", [])

def list_folder_contents(client, project_id, folder_id, depth=0, results=None):
    """Recursively list all items in a folder."""
    if results is None:
        results = []
    url  = f"{BASE_URL}/data/v1/projects/{project_id}/folders/{folder_id}/contents"

    page_url = url
    while page_url:
        data    = client.get(page_url)
        items   = data.get("data", [])
        links   = data.get("links", {})

        for item in items:
            item_type = item["type"]   # "folders" or "items"
            attrs     = item["attributes"]
            indent    = "  " * depth

            if item_type == "folders":
                results.append({
                    "type":     "Folder",
                    "name":     attrs["name"],
                    "id":       item["id"],
                    "depth":    depth,
                    "path":     indent + "📁 " + attrs["name"],
                })
                # Recurse into subfolder
                list_folder_contents(client, project_id, item["id"], depth + 1, results)

            elif item_type == "items":
                # Get the latest version info
                version = item.get("relationships", {}).get("tip", {}).get("data", {})
                results.append({
                    "type":        "File",
                    "name":        attrs["displayName"],
                    "id":          item["id"],
                    "version_id":  version.get("id", ""),
                    "depth":       depth,
                    "path":        indent + "📄 " + attrs["displayName"],
                })

        # Handle pagination
        next_link = links.get("next", {})
        page_url  = next_link.get("href") if next_link else None

    return results

## ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # client = APSClient(...)  # from acc-api-setup

    folders = get_top_folders(client, HUB_ID, PROJECT_ID)
    all_files = []

    for folder in folders:
        print(f"\n=== {folder['attributes']['name']} ===")
        contents = list_folder_contents(client, PROJECT_ID, folder["id"])
        for item in contents:
            print(item["path"])
        all_files.extend(contents)

    print(f"\nTotal items: {len(all_files)}")
```

---

### Script 2: List file versions and download a specific version

```python
import os, requests

BASE_URL = "https://developer.api.autodesk.com"

def get_versions(client, project_id, item_id):
    """List all versions of a file."""
    url  = f"{BASE_URL}/data/v1/projects/{project_id}/items/{item_id}/versions"
    data = client.get(url)
    versions = []
    for v in data.get("data", []):
        attrs = v["attributes"]
        versions.append({
            "version_number": attrs.get("versionNumber", ""),
            "version_id":     v["id"],
            "file_name":      attrs.get("name", ""),
            "file_size_mb":   round(attrs.get("storageSize", 0) / 1048576, 2),
            "last_modified":  attrs.get("lastModifiedTime", ""),
            "created_by":     attrs.get("lastModifiedUserName", ""),
        })
    return versions

def download_version(client, project_id, version_id, output_path):
    """Download a specific file version."""
    # Step 1: Get the storage location (S3/OSS signed URL)
    url  = f"{BASE_URL}/data/v1/projects/{project_id}/versions/{version_id}"
    data = client.get(url)
    download_url = (data.get("relationships", {})
                        .get("storage", {})
                        .get("meta", {})
                        .get("link", {})
                        .get("href"))

    if not download_url:
        print("No direct download URL. File may require OSS signed URL.")
        return False

    # Step 2: Stream download
    resp = requests.get(download_url, headers=client.headers(), stream=True)
    resp.raise_for_status()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded: {output_path}")
    return True

## Example usage:
## versions = get_versions(client, PROJECT_ID, ITEM_ID)
## for v in versions:
##     print(f"v{v['version_number']} — {v['last_modified']} by {v['created_by']}")
```

---

### Script 3: Upload a file to an ACC Docs folder

Uploading to ACC requires three steps: create a storage object, upload binary data, then create a new item/version.

```python
import os, requests, math

BASE_URL = "https://developer.api.autodesk.com"

def upload_file_to_acc(client, project_id, folder_id, local_file_path):
    """Upload a file to an ACC Docs folder. Returns the new item ID."""
    file_name = os.path.basename(local_file_path)
    file_size = os.path.getsize(local_file_path)

    # ── Step 1: Create a storage location (OSS object) ───────────────────────
    storage_resp = client.post(
        f"{BASE_URL}/data/v1/projects/{project_id}/storage",
        {
            "jsonapi": {"version": "1.0"},
            "data": {
                "type": "objects",
                "attributes": {"name": file_name},
                "relationships": {
                    "target": {
                        "data": {"type": "folders", "id": folder_id}
                    }
                }
            }
        }
    )
    object_id  = storage_resp["data"]["id"]
    upload_url = storage_resp["data"]["relationships"]["storage"]["meta"]["link"]["href"]

    # ── Step 2: Upload the binary to OSS ─────────────────────────────────────
    # For files >5 MB, use resumable upload. For simplicity, single-part shown here.
    with open(local_file_path, "rb") as f:
        file_data = f.read()

    upload_resp = requests.put(
        upload_url,
        headers={"Authorization": "Bearer " + client.get_token(),
                 "Content-Type":  "application/octet-stream"},
        data=file_data
    )
    upload_resp.raise_for_status()
    print(f"Uploaded binary: {file_name} ({file_size} bytes)")

    # ── Step 3a: Create a new Item (first upload of this file) ───────────────
    create_resp = client.post(
        f"{BASE_URL}/data/v1/projects/{project_id}/items",
        {
            "jsonapi": {"version": "1.0"},
            "data": {
                "type": "items",
                "attributes": {
                    "displayName": file_name,
                    "extension": {
                        "type":    "items:autodesk.core:File",
                        "version": "1.0"
                    }
                },
                "relationships": {
                    "tip": {
                        "data": {"type": "versions", "id": "1"}
                    },
                    "parent": {
                        "data": {"type": "folders", "id": folder_id}
                    }
                }
            },
            "included": [{
                "type": "versions",
                "id":   "1",
                "attributes": {
                    "name": file_name,
                    "extension": {
                        "type":    "versions:autodesk.core:File",
                        "version": "1.0"
                    }
                },
                "relationships": {
                    "storage": {
                        "data": {"type": "objects", "id": object_id}
                    }
                }
            }]
        }
    )
    item_id = create_resp["data"]["id"]
    print(f"Item created in ACC: {item_id}")
    return item_id

## Usage:
## item_id = upload_file_to_acc(client, PROJECT_ID, FOLDER_ID, r"C:\Drawings\A-DR-001.pdf")
```

---

### Script 4: Create a folder structure

```python
BASE_URL = "https://developer.api.autodesk.com"

def create_folder(client, project_id, parent_folder_id, folder_name):
    """Create a subfolder under an existing folder. Returns new folder ID."""
    resp = client.post(
        f"{BASE_URL}/data/v1/projects/{project_id}/folders",
        {
            "jsonapi": {"version": "1.0"},
            "data": {
                "type": "folders",
                "attributes": {
                    "name": folder_name,
                    "extension": {
                        "type":    "folders:autodesk.core:Folder",
                        "version": "1.0"
                    }
                },
                "relationships": {
                    "parent": {
                        "data": {"type": "folders", "id": parent_folder_id}
                    }
                }
            }
        }
    )
    new_id = resp["data"]["id"]
    print(f"Created folder: {folder_name} → {new_id}")
    return new_id

def create_folder_tree(client, project_id, root_folder_id, tree):
    """
    Create a nested folder structure from a dict.
    tree = {
        "01 Architecture": {
            "Drawings": {},
            "Models": {}
        },
        "02 Structure": {}
    }
    """
    def recurse(parent_id, subtree):
        for name, children in subtree.items():
            new_id = create_folder(client, project_id, parent_id, name)
            if children:
                recurse(new_id, children)

    recurse(root_folder_id, tree)

## Example:
## STANDARD_STRUCTURE = {
##     "01 Architecture": {"Drawings": {}, "Models": {}, "Reports": {}},
##     "02 Structure":    {"Drawings": {}, "Models": {}},
##     "03 MEP":          {"Drawings": {}, "Models": {}},
##     "04 Coordination": {"Clash Reports": {}, "Issue Log": {}},
##     "99 Admin":        {"BEP": {}, "Contracts": {}},
## }
## create_folder_tree(client, PROJECT_ID, ROOT_FOLDER_ID, STANDARD_STRUCTURE)
```

---

### Transmittals, Reviews & Packages (ACC Docs API)

For **Transmittals** (formally issuing document sets):

```
GET  /construction/transmittals/v1/projects/{projectId}/transmittals
POST /construction/transmittals/v1/projects/{projectId}/transmittals
GET  /construction/transmittals/v1/projects/{projectId}/transmittals/{transmittalId}
```

For **Document Reviews**:

```
GET  /construction/reviews/v1/projects/{projectId}/reviews
POST /construction/reviews/v1/projects/{projectId}/reviews
```

For **Packages** (bundled document sets):

```
GET  /construction/packages/v1/projects/{projectId}/packages
POST /construction/packages/v1/projects/{projectId}/packages
```

All require: `Authorization: Bearer {3-legged-token}` and `x-ads-region: US` (or `EU`)

---

### Common ACC Docs patterns

| Task                          | Approach                                      |
|-------------------------------|-----------------------------------------------|
| List drawings on a sheet set  | Traverse top folders → "Project Files" → discipline folder |
| Find latest PDF of a drawing  | `GET /items/{id}/versions` → filter by `.pdf` extension |
| Create a transmittal          | POST to transmittals API with file version IDs |
| Bulk upload from local folder | Loop `upload_file_to_acc()` with `os.walk()`  |
| Mirror local folder to ACC    | Compare file names + sizes before uploading   |


## acc-coordinate

> Work with Autodesk Construction Cloud (ACC) Coordinate — list and inspect model sets, retrieve clash results, create clash issues, manage model activation for coordination, and export coordination reports via the APS Model Coordination API. Use this skill when a user needs to automate clash detection workflows, pull clash data from ACC for reporting, create ACC issues from clashes, check which models are active in a model set, or integrate ACC coordination data with other tools. Trigger on phrases like "ACC Coordinate", "model coordination", "model set", "clash results", "clash data", "ACC clashes", "coordination space", "activated models", "clash issues", "federated model", "coordination report", "BIM coordination", or any request to work with ACC's model coordination module via API. Also offer this when users want to export or report on clash data from ACC.

## ACC Coordinate — Model Coordination API

Automate ACC Coordinate workflows for:

**"$ARGUMENTS"**

### Prerequisites

- APS credentials configured (see `acc-api-setup` skill)
- Project container ID = ACC project ID **without** the `b.` prefix
- `pip install requests`

---

### API base URL and key concepts

```
Base:  https://developer.api.autodesk.com/modelcoordination/modelset/v3
Auth:  2-legged token (data:read scope)
```

**Key objects:**
- **Container**: the coordination space for a project (ID = project ID without `b.`)
- **Model Set**: a named collection of activated Revit/IFC models grouped for clash testing
- **Clash Set**: the result of a clash test between two model sets or within one
- **Clash Group**: a group of related clashes (e.g. all ducts vs all beams)
- **Clash Instance**: a single clash between two specific elements

---

### Script 1: List all model sets in a project

```python
import os, requests

CONTAINER_ID = os.environ.get("APS_CONTAINER_ID")  # project ID without b.
BASE_MC = "https://developer.api.autodesk.com/modelcoordination/modelset/v3"

def list_model_sets(client, container_id):
    """List all model sets (coordination spaces) in an ACC project."""
    url  = f"{BASE_MC}/containers/{container_id}/modelsets"
    data = client.get(url)
    model_sets = []
    for ms in data.get("results", []):
        model_sets.append({
            "Model Set Name": ms.get("name", ""),
            "Model Set ID":   ms.get("modelSetId", ""),
            "Created":        ms.get("createTime", ""),
            "Status":         ms.get("status", ""),
            "Model Count":    len(ms.get("modelSetVersions", [{}])[-1:][0].get("models", []))
                              if ms.get("modelSetVersions") else 0,
        })
    return model_sets

if __name__ == "__main__":
    # client = APSClient(...)
    model_sets = list_model_sets(client, CONTAINER_ID)
    for ms in model_sets:
        print(f"  {ms['Model Set Name']:30} ID: {ms['Model Set ID']}")
```

---

### Script 2: Get clash results for a model set

```python
BASE_MC = "https://developer.api.autodesk.com/modelcoordination/modelset/v3"

def get_model_set_versions(client, container_id, model_set_id):
    """Get all versions of a model set (each version = a clash test run)."""
    url  = f"{BASE_MC}/containers/{container_id}/modelsets/{model_set_id}/versions"
    data = client.get(url)
    versions = []
    for v in data.get("results", []):
        versions.append({
            "version_id":    v.get("modelSetVersionId", ""),
            "version_num":   v.get("versionNumber", 0),
            "created":       v.get("createTime", ""),
            "clash_count":   v.get("clashCount", 0),
            "status":        v.get("status", ""),
        })
    # Sort by version number descending (latest first)
    return sorted(versions, key=lambda x: -x["version_num"])

def get_clash_groups(client, container_id, model_set_id, version_id):
    """Get grouped clashes for a model set version."""
    url  = f"{BASE_MC}/containers/{container_id}/modelsets/{model_set_id}/versions/{version_id}/clashes/grouped"
    data = client.get(url)
    groups = []
    for group in data.get("groups", []):
        groups.append({
            "Clash Group":    group.get("clashGroupId", ""),
            "Discipline A":   group.get("documentGroupA", {}).get("name", ""),
            "Discipline B":   group.get("documentGroupB", {}).get("name", ""),
            "Count":          group.get("clashCount", 0),
            "Status":         group.get("status", "open"),
        })
    return sorted(groups, key=lambda x: -x["Count"])

def get_clash_instances(client, container_id, model_set_id, version_id, group_id, limit=100):
    """Get individual clash instances in a clash group."""
    url    = (f"{BASE_MC}/containers/{container_id}/modelsets/{model_set_id}"
              f"/versions/{version_id}/clashes")
    params = {"groupId": group_id, "limit": limit}
    data   = client.get(url, params=params)
    clashes = []
    for clash in data.get("clashes", []):
        clashes.append({
            "Clash ID":    clash.get("clashId", ""),
            "Status":      clash.get("status", ""),
            "Element A ID": clash.get("ldId", ""),
            "Element B ID": clash.get("rdId", ""),
            "Position X":  clash.get("clashPoint", {}).get("x", 0),
            "Position Y":  clash.get("clashPoint", {}).get("y", 0),
            "Position Z":  clash.get("clashPoint", {}).get("z", 0),
        })
    return clashes

if __name__ == "__main__":
    # Get latest version
    versions = get_model_set_versions(client, CONTAINER_ID, MODEL_SET_ID)
    latest   = versions[0]
    print(f"Latest version: v{latest['version_num']} — {latest['clash_count']} clashes")

    # Get clash groups (discipline pairs)
    groups = get_clash_groups(client, CONTAINER_ID, MODEL_SET_ID, latest["version_id"])
    for g in groups[:10]:
        print(f"  {g['Discipline A']:25} vs {g['Discipline B']:25} → {g['Count']} clashes")
```

---

### Script 3: Export clash data to CSV

```python
import csv, os
from datetime import datetime

def export_clashes_to_csv(client, container_id, model_set_id, output_path=None):
    """Export all clash groups and totals to a CSV report."""

    if not output_path:
        ts = datetime.now().strftime("%Y%m%d_%H%M")
        output_path = f"C:\\Reports\\acc_clashes_{ts}.csv"

    # Get latest version
    versions = get_model_set_versions(client, container_id, model_set_id)
    if not versions:
        print("No versions found.")
        return

    latest_version = versions[0]
    groups = get_clash_groups(client, container_id, model_set_id, latest_version["version_id"])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Report Date", datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Model Set ID", model_set_id,
            "Version", latest_version["version_num"],
        ])
        writer.writerow([])
        writer.writerow(["Clash Group", "Discipline A", "Discipline B", "Count", "Status"])

        total = 0
        for g in groups:
            writer.writerow([
                g["Clash Group"],
                g["Discipline A"],
                g["Discipline B"],
                g["Count"],
                g["Status"],
            ])
            total += g["Count"]

        writer.writerow([])
        writer.writerow(["TOTAL", "", "", total, ""])

    print(f"Clash report saved to: {output_path} ({total} total clashes)")
    return output_path
```

---

### Script 4: List activated models in a model set

```python
def get_activated_models(client, container_id, model_set_id):
    """List all Revit/IFC models activated in the latest model set version."""
    versions = get_model_set_versions(client, container_id, model_set_id)
    if not versions:
        return []

    latest_v_id = versions[0]["version_id"]
    url  = f"{BASE_MC}/containers/{container_id}/modelsets/{model_set_id}/versions/{latest_v_id}"
    data = client.get(url)

    models = []
    for model in data.get("models", []):
        models.append({
            "Model Name":   model.get("name", ""),
            "Document ID":  model.get("documentId", ""),
            "Version URN":  model.get("versionUrn", ""),
            "Discipline":   model.get("documentGroup", {}).get("name", ""),
            "Status":       model.get("status", ""),
        })
    return models
```

---

### What to tell the user about ACC Coordinate

#### Model set setup (no API needed — ACC UI)
1. Go to ACC → **Coordinate** → **Model Coordination**
2. Create a new Model Set, give it a name (e.g. "Full Building — All Disciplines")
3. Select folders from ACC Docs to include (Revit and IFC models from each discipline)
4. **Activate** the models in the set
5. Run a clash test — ACC generates results within minutes to hours

#### Model activation best practices
- Activate only **coordination models** (not design working files)
- Use **IFC** exports for cross-authoring-tool coordination
- Separate model sets by zone or level for complex projects
- Re-run clash tests after every model update/publish

#### Clash triage workflow
1. Export clash groups CSV (Script 3 above)
2. Sort by count → address highest-density clashes first
3. Assign clashes to discipline owners as ACC Issues
4. Track resolution in weekly coordination meetings
5. Re-run clash test and compare delta to previous version


## acc-design-collaboration

> Guide Revit ↔ ACC Design Collaboration workflows — setting up cloud worksharing, creating and consuming design packages, shared views, Design Collaboration setup, model publishing, and Revit cloud model best practices. Also covers the API for querying shared views and design package status. Use this skill when a user needs help with Revit cloud models, BIM 360 Design / ACC Design Collaboration, creating or receiving design packages, activating models for coordination, or troubleshooting cloud worksharing issues. Trigger on phrases like "Design Collaboration", "cloud worksharing", "Revit cloud model", "design package", "shared views", "consume package", "publish model to ACC", "BIM 360 Design", "Revit cloud", "cloud model", "collaboration workflow", "ACC Revit workflow", or any request involving the Revit-to-ACC publishing and collaboration pipeline.

## ACC Design Collaboration — Revit Cloud Workflow

Set up and manage Design Collaboration for:

**"$ARGUMENTS"**

### Overview

ACC Design Collaboration connects Revit teams working on cloud-hosted models. The workflow has two modes:

| Mode                        | When to use                                                  |
|-----------------------------|--------------------------------------------------------------|
| **Cloud Worksharing**       | Multiple Revit users on the same model simultaneously        |
| **Design Packages**         | Sharing a frozen snapshot of your model with other disciplines|

---

### Part 1: Cloud Worksharing Setup (Revit UI — no API needed)

#### Step-by-step: Moving a local model to ACC

1. **Open the Revit model** you want to migrate.
2. Go to **Collaborate** tab → **Collaborate** button.
3. Select **"In BIM 360 / Autodesk Construction Cloud"**.
4. Sign in with your Autodesk ID if prompted.
5. Choose the **ACC project** and **folder** — place it in the Design Collaboration folder (usually `Project Files > [Discipline]`).
6. Click **OK** — Revit saves the model to ACC and creates a local cache file.
7. All team members open the model from ACC using **Open → BIM 360 / ACC** in Revit.

#### Workset best practices for cloud models
- Keep **"Shared Levels and Grids"** on its own workset — other disciplines will borrow from it.
- Each discipline should own one workset (Architecture, Structure, MEP, etc.)
- All team members should **Synchronize with Central (SWC)** at start and end of each session.
- Use **Relinquish All Mine** before closing.
- Never use **Save As** on a cloud model — it detaches from the cloud.

#### Who should use Cloud Worksharing?
- Same discipline, multiple users (e.g. 3 architects in the same Revit model)
- Teams working concurrently with live updates

---

### Part 2: Design Packages — Sharing with other disciplines

Design Packages let you send a **frozen snapshot** of your model to other teams for reference.

#### Create a Design Package (Revit UI)

1. In Revit, go to **Collaborate** tab → **Design Collaboration**.
2. In the Design Collaboration panel, select your project.
3. Under **Packages**, click **Create Package**.
4. Name the package (e.g. "ARCH-P01-2024-03-01" — use your project's naming convention).
5. Select the **views/models** to include.
6. Add a description / change summary.
7. Click **Publish**.
8. ACC sends a notification to the receiving teams.

#### Consume a package from another discipline (Revit UI)

1. In Revit → **Collaborate** → **Design Collaboration**.
2. Under **Incoming Packages**, you will see new packages from other teams.
3. Click **Review** to see what changed.
4. Click **Accept** to update your local reference files.
5. The incoming model appears as a linked Revit file in your project.

#### Design Package naming convention (recommended)

```
{Discipline}-{Status}-{Date}-{Revision}
Examples:
  ARCH-WIP-2024-03-01-R01         ← work in progress share
  STRUCT-S1-2024-03-15-C01        ← suitable for coordination
  MEP-S2-2024-04-01-C03           ← suitable for information
```

---

### Part 3: Shared Views

Shared Views let you publish a **non-downloadable 3D/2D view** to ACC for review by non-Revit users (clients, contractors, planners).

#### Create a Shared View (Revit UI)

1. Open the 3D view or sheet you want to share.
2. Go to **Collaborate** → **Share**.
3. Choose **Send Link** — Revit publishes the view to ACC Docs.
4. Copy the link and send to reviewers. They open it in a browser with no Revit needed.
5. Shared Views expire after **30 days** by default (configurable).

---

### Part 4: API — Query Shared Views and Design Package status

#### Get shared views via APS API

```python
import os, requests

## Shared Views are stored in ACC Docs — query via Data Management API
## They appear in the "Shared Views" folder in the project

BASE_URL   = "https://developer.api.autodesk.com"
PROJECT_ID = os.environ.get("APS_PROJECT_ID")  # with b. prefix

def find_shared_views_folder(client, hub_id, project_id):
    """Find the Shared Views folder in an ACC project."""
    url   = f"{BASE_URL}/project/v1/hubs/{hub_id}/projects/{project_id}/topFolders"
    data  = client.get(url)
    for folder in data.get("data", []):
        if "shared" in folder["attributes"]["name"].lower():
            return folder["id"]
    return None

def list_shared_views(client, project_id, folder_id):
    """List all shared views in the Shared Views folder."""
    url  = f"{BASE_URL}/data/v1/projects/{project_id}/folders/{folder_id}/contents"
    data = client.get(url)
    views = []
    for item in data.get("data", []):
        if item["type"] == "items":
            attrs = item["attributes"]
            views.append({
                "Name":          attrs.get("displayName", ""),
                "Item ID":       item["id"],
                "Created":       attrs.get("createTime", ""),
                "Last Modified": attrs.get("lastModifiedTime", ""),
                "Created By":    attrs.get("createUserName", ""),
            })
    return views
```

#### Check Design Collaboration package status via Revit API

ACC Design Collaboration doesn't have a fully public REST API for packages (as of 2025), but you can check package status using the **Revit API** inside Dynamo:

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

try:
    # Check if this model is a cloud model
    cloud_path = doc.GetCloudModelPath()
    if cloud_path:
        OUT = {
            "Is Cloud Model":  True,
            "Project GUID":    str(cloud_path.GetProjectGUID()),
            "Model GUID":      str(cloud_path.GetModelGUID()),
            "Region":          cloud_path.Region if hasattr(cloud_path, "Region") else "N/A",
        }
    else:
        OUT = {"Is Cloud Model": False}

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Part 5: Revit publish to ACC from Dynamo (automatic sync)

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc   = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

try:
    if not doc.IsWorkshared:
        OUT = "Model is not workshared — cannot synchronise."
    else:
        # Build sync options
        opts = SynchronizeWithCentralOptions()
        opts.SetRelinquishOptions(RelinquishOptions(True))  # relinquish all on sync
        opts.SaveLocalBefore = True
        opts.SaveLocalAfter  = True
        opts.Comment         = "Auto-sync via Dynamo script"

        doc.SynchronizeWithCentral(TransactWithCentralOptions(), opts)
        OUT = "Synchronised with Central successfully."

except Exception as e:
    import traceback
    OUT = "ERROR: " + str(e) + "\n" + traceback.format_exc()
```

---

### Common Design Collaboration problems & fixes

| Problem                               | Fix                                                              |
|---------------------------------------|------------------------------------------------------------------|
| Can't open model — "not found"        | Check you're signed into the correct Autodesk account            |
| "Central model out of date"           | Another user is saving — wait and retry SWC                      |
| Missing linked files after sync       | Reload Links from cloud path, not local path                     |
| Package not visible to other team     | Check permissions — receiving team needs at least "View" access  |
| Model performance slow on cloud       | Use "Specify" workset opening — don't open all worksets          |
| Changes not reflecting in packages    | Create a new package — packages are snapshots, not live links    |
| SWC failing with ownership errors     | Run "Relinquish All Mine" then retry SWC                         |

---

### Design Collaboration checklist for project start

- [ ] Create ACC project with correct permissions (Design Collaboration role assigned)
- [ ] Set up discipline folders in ACC Docs (Architecture, Structure, MEP, etc.)
- [ ] Migrate each model to ACC cloud via Collaborate → Collaborate
- [ ] Establish workset naming convention and assign ownership
- [ ] Configure Design Collaboration settings: who can create packages, package naming
- [ ] Define package sharing frequency (weekly sprints, milestone-based, etc.)
- [ ] Test that all disciplines can consume each other's packages
- [ ] Set up Model Coordination model set and activate discipline models


## acc-reports

> Export ACC project data to CSV or Excel — issues, RFIs, document logs, clash summaries, transmittals, and project activity reports — using the APS REST API with Python. Use this skill when a user needs to report on ACC project health, export an issues register, pull RFI status into a spreadsheet, generate a document transmittal log, create a clash trend report, or produce any data export from Autodesk Construction Cloud. Trigger on phrases like "export issues", "issues report", "RFI report", "ACC report", "export from ACC", "document log", "clash report", "ACC data export", "project status report", "pull data from ACC", "ACC Excel export", "transmittal log", or any request to extract or report on data stored in Autodesk Construction Cloud.

## ACC Data Reports & Exports

Export ACC project data for:

**"$ARGUMENTS"**

### Prerequisites

- APS credentials configured (see `acc-api-setup` skill)
- For Issues/RFIs: **3-legged token** required
- For Docs/Clash data: 2-legged token is sufficient
- `pip install requests openpyxl`

---

### Script 1: Export all ACC Issues to CSV

Issues API requires a 3-legged token (user context).

```python
import os, csv, requests
from datetime import datetime

## ── Configuration ─────────────────────────────────────────────────────────────
PROJECT_ID  = os.environ.get("APS_PROJECT_ID_RAW")   # WITHOUT b. prefix
OUTPUT_PATH = r"C:\Reports\acc_issues_export.csv"

BASE_ISSUES = "https://developer.api.autodesk.com/construction/issues/v1"
## ─────────────────────────────────────────────────────────────────────────────

def get_all_issues(client, project_id):
    """Fetch all issues from ACC using pagination."""
    all_issues = []
    offset     = 0
    limit      = 100

    while True:
        url    = f"{BASE_ISSUES}/projects/{project_id}/issues"
        params = {"limit": limit, "offset": offset,
                  "filterType": "all"}   # include all statuses
        data   = client.get(url, params=params)

        issues = data.get("results", [])
        total  = data.get("pagination", {}).get("totalResults", 0)

        all_issues.extend(issues)
        offset += limit

        if offset >= total or not issues:
            break

    return all_issues, total

def issues_to_csv(issues, output_path):
    """Write issues list to CSV."""
    if not issues:
        print("No issues found.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fieldnames = [
        "Issue Number", "Title", "Status", "Assigned To",
        "Due Date", "Created By", "Created Date",
        "Root Cause", "Type", "Sub-type",
        "Location", "Description", "Closed Date",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()

        for issue in issues:
            attrs = issue.get("attributes", {})
            writer.writerow({
                "Issue Number":  attrs.get("displayId", ""),
                "Title":         attrs.get("title", ""),
                "Status":        attrs.get("status", ""),
                "Assigned To":   (attrs.get("assignedTo", {}) or {}).get("displayName", ""),
                "Due Date":      attrs.get("dueDate", ""),
                "Created By":    (attrs.get("createdBy", {}) or {}).get("displayName", ""),
                "Created Date":  attrs.get("createdAt", ""),
                "Root Cause":    attrs.get("rootCauseLabel", ""),
                "Type":          attrs.get("issueTypeLabel", ""),
                "Sub-type":      attrs.get("issueSubTypeLabel", ""),
                "Location":      attrs.get("locationDetails", ""),
                "Description":   attrs.get("description", "")[:200] if attrs.get("description") else "",
                "Closed Date":   attrs.get("closedAt", ""),
            })

    print(f"Issues exported: {len(issues)} → {output_path}")

if __name__ == "__main__":
    # client must use a 3-legged token
    issues, total = get_all_issues(client, PROJECT_ID)
    print(f"Fetched {len(issues)} of {total} issues")
    issues_to_csv(issues, OUTPUT_PATH)
```

---

### Script 2: Issues summary dashboard (pivot by status, type, assignee)

```python
import os, csv
from collections import Counter, defaultdict

def issues_summary(issues, output_path=r"C:\Reports\acc_issues_summary.csv"):
    """Generate a pivot summary of issues by status, type, and assignee."""

    status_count  = Counter()
    type_count    = Counter()
    assignee_count = Counter()
    overdue_count = 0

    today = datetime.now().date()

    for issue in issues:
        attrs = issue.get("attributes", {})

        status   = attrs.get("status", "unknown")
        iss_type = attrs.get("issueTypeLabel", "unknown")
        assignee = (attrs.get("assignedTo", {}) or {}).get("displayName", "Unassigned")
        due_str  = attrs.get("dueDate", "")

        status_count[status]     += 1
        type_count[iss_type]     += 1
        assignee_count[assignee] += 1

        if due_str and status not in ("closed", "void"):
            try:
                due_date = datetime.fromisoformat(due_str.split("T")[0]).date()
                if due_date < today:
                    overdue_count += 1
            except Exception:
                pass

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["=== ISSUES BY STATUS ==="])
        writer.writerow(["Status", "Count"])
        for status, count in status_count.most_common():
            writer.writerow([status, count])

        writer.writerow([])
        writer.writerow(["=== ISSUES BY TYPE ==="])
        writer.writerow(["Type", "Count"])
        for typ, count in type_count.most_common():
            writer.writerow([typ, count])

        writer.writerow([])
        writer.writerow(["=== ISSUES BY ASSIGNEE ==="])
        writer.writerow(["Assignee", "Count"])
        for assignee, count in assignee_count.most_common():
            writer.writerow([assignee, count])

        writer.writerow([])
        writer.writerow(["=== SUMMARY ==="])
        writer.writerow(["Total Issues",   sum(status_count.values())])
        writer.writerow(["Open",           status_count.get("open", 0)])
        writer.writerow(["In Review",      status_count.get("in_review", 0)])
        writer.writerow(["Closed",         status_count.get("closed", 0)])
        writer.writerow(["Overdue (open)", overdue_count])

    print(f"Summary saved: {output_path}")

## Usage:
## issues_summary(issues)
```

---

### Script 3: Export ACC Docs file register to CSV

```python
import os, csv

BASE_URL = "https://developer.api.autodesk.com"

def export_doc_register(client, hub_id, project_id, output_path=r"C:\Reports\acc_doc_register.csv"):
    """Export a flat file register of all documents in ACC Docs."""

    # Get top folders
    folders = client.get(
        f"{BASE_URL}/project/v1/hubs/{hub_id}/projects/{project_id}/topFolders"
    ).get("data", [])

    all_files = []

    def traverse(folder_id, folder_path):
        url  = f"{BASE_URL}/data/v1/projects/{project_id}/folders/{folder_id}/contents"
        page = url
        while page:
            data  = client.get(page)
            items = data.get("data", [])
            next_ = data.get("links", {}).get("next", {})
            for item in items:
                attrs = item["attributes"]
                if item["type"] == "folders":
                    traverse(item["id"], folder_path + "/" + attrs["name"])
                elif item["type"] == "items":
                    all_files.append({
                        "File Name":     attrs.get("displayName", ""),
                        "Folder Path":   folder_path,
                        "Item ID":       item["id"],
                        "Last Modified": attrs.get("lastModifiedTime", ""),
                        "Modified By":   attrs.get("lastModifiedUserName", ""),
                        "Created":       attrs.get("createTime", ""),
                        "Created By":    attrs.get("createUserName", ""),
                    })
            page = next_.get("href") if next_ else None

    for folder in folders:
        traverse(folder["id"], folder["attributes"]["name"])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_files[0].keys()) if all_files else [])
        writer.writeheader()
        writer.writerows(all_files)

    print(f"Doc register: {len(all_files)} files → {output_path}")
    return all_files
```

---

### Script 4: Clash trend report (compare current vs previous version)

```python
import csv, os
from datetime import datetime

BASE_MC = "https://developer.api.autodesk.com/modelcoordination/modelset/v3"

def clash_trend_report(client, container_id, model_set_id,
                        output_path=r"C:\Reports\acc_clash_trend.csv"):
    """Compare clash counts across all model set versions to show trend."""

    url   = f"{BASE_MC}/containers/{container_id}/modelsets/{model_set_id}/versions"
    data  = client.get(url)
    versions = sorted(
        data.get("results", []),
        key=lambda v: v.get("versionNumber", 0)
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Version", "Date", "Total Clashes", "Delta vs Previous"])

        prev_count = None
        for v in versions:
            count = v.get("clashCount", 0)
            delta = ""
            if prev_count is not None:
                diff  = count - prev_count
                delta = ("+" if diff > 0 else "") + str(diff)
            writer.writerow([
                "v" + str(v.get("versionNumber", "")),
                v.get("createTime", "")[:10],
                count,
                delta,
            ])
            prev_count = count

    print(f"Clash trend saved: {output_path}")

## Usage:
## clash_trend_report(client, CONTAINER_ID, MODEL_SET_ID)
```

---

### Combined project health report

```python
def full_project_report(client, hub_id, project_id, container_id, model_set_id):
    """Generate a complete ACC project health snapshot."""
    from datetime import datetime

    report = {
        "Generated":    datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Project ID":   project_id,
    }

    # Issues
    try:
        issues, total = get_all_issues(client, project_id.replace("b.", ""))
        open_issues   = sum(1 for i in issues
                            if i.get("attributes", {}).get("status") == "open")
        report["Total Issues"]  = total
        report["Open Issues"]   = open_issues
        report["Closed Issues"] = total - open_issues
    except Exception as e:
        report["Issues Error"] = str(e)

    # Docs
    try:
        files = export_doc_register(client, hub_id, project_id,
                                    output_path=r"C:\Reports\doc_register.csv")
        report["Total Documents"] = len(files)
    except Exception as e:
        report["Docs Error"] = str(e)

    # Clashes
    try:
        versions = get_model_set_versions(client, container_id, model_set_id)
        if versions:
            report["Latest Clash Count"] = versions[0]["clash_count"]
            report["Latest Model Set Version"] = versions[0]["version_num"]
    except Exception as e:
        report["Clash Error"] = str(e)

    return report
```

---

### Quick reference: ACC report types and which token they need

| Report                 | API                        | Token     | Scope          |
|------------------------|----------------------------|-----------|----------------|
| Issues register        | Issues API v1              | 3-legged  | data:read      |
| Document log           | Data Management API v1     | 2-legged  | data:read      |
| Clash summary          | Model Coordination API v3  | 2-legged  | data:read      |
| Project list           | Project API v1             | 2-legged  | account:read   |
| Transmittal log        | Construction Transmittals  | 2-legged  | data:read      |
| Sheets register        | Sheets API v1              | 2-legged  | data:read      |
