---
name: ddc-bim-data-validation
description: >
  BIM data toolkit — 14 routed skills from DataDrivenConstruction covering RVT-to-IFC
  conversion, IFC-to-Excel and Excel-to-BIM round trips, IFC data and quantity extraction,
  BIM quantity takeoff, clash detection and clash resolution analysis, BIM validation
  pipelines and reports, model consistency checking, IDS checking, and Dynamo/visual-
  programming automation. Load for any task that gets data in or out of a Revit/IFC model
  or validates model quality; use the router to find the section.
---

# DDC BIM Data Exchange, QTO & Validation Toolkit

Compiled from https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction (MIT, DataDrivenConstruction / Artem Boiko) — a 14-skill subset selected for Revit/IFC data workflows. Several skills call DDC's RvtExporter / converter binaries and Python scripts that are not included here.

## Router

| Skill | Use when |
|---|---|
| **Data exchange** | |
| [rvt-to-ifc](#rvt-to-ifc) | Convert RVT files to IFC format. Support IFC2x3, IFC4, IFC4.3 with customizable export settings. |
| [ifc-to-excel](#ifc-to-excel) | Convert IFC files (2x3, 4x1, 4x3) to Excel databases using IfcExporter CLI. Extract BIM data, properties, and geometry without proprietary software. |
| [excel-to-bim](#excel-to-bim) | Push Excel data back to BIM models. Update parameters, properties, and attributes from structured spreadsheets. |
| [ifc-data-extraction](#ifc-data-extraction) | Extract structured data from IFC (Industry Foundation Classes) files using IfcOpenShell. Parse BIM models, extract quantities, properties, spatial relationships, and export to various formats. |
| **Quantities** | |
| [ifc-qto-extraction](#ifc-qto-extraction) | Extract quantities from IFC/Revit models for quantity takeoff. Uses DDC converters to get element counts, areas, volumes, lengths with grouping and reporting. |
| [bim-qto](#bim-qto) | Extract quantities from BIM/CAD data for cost estimation. Group by type, level, zone. Generate QTO reports. |
| **Clash detection** | |
| [bim-clash-detection](#bim-clash-detection) | Detect and analyze geometric clashes in BIM models. Identify MEP, structural, and architectural conflicts before construction. |
| [clash-detection-analysis](#clash-detection-analysis) | Detect and analyze geometric clashes between BIM elements. Identify hard clashes, soft clashes, and workflow conflicts using spatial analysis and rule-based detection. |
| [clash-resolution-analyzer](#clash-resolution-analyzer) | Analyze BIM clash detection results and suggest resolutions. Prioritize clashes, identify patterns, assign responsibility, and track resolution status. |
| **Validation** | |
| [bim-validation-pipeline](#bim-validation-pipeline) | Build automated BIM validation pipelines for IFC/Revit data. Continuous validation against IDS, LOD requirements, COBie, and project-specific BEP standards. |
| [bim-consistency-checker](#bim-consistency-checker) | Check BIM model consistency: naming conventions, parameter completeness, spatial relationships, and data integrity across model elements. |
| [ids-checker](#ids-checker) | Check BIM data against IDS (Information Delivery Specification). Validate model information requirements and compliance. |
| [bim-validation-report](#bim-validation-report) | Generate comprehensive BIM model validation reports. Check data quality, completeness, and compliance with standards. |
| **Automation** | |
| [bim-visual-programming-automation](#bim-visual-programming-automation) | Automate BIM workflows using visual programming and Python. Create parametric schedules, export data, batch modify elements, and integrate with external data sources. |

---

# Data exchange


## rvt-to-ifc

> Convert RVT files to IFC format. Support IFC2x3, IFC4, IFC4.3 with customizable export settings.

## RVT to IFC Conversion

> **Note:** RVT is the file format. IFC is an open standard by buildingSMART International.

### Business Case

#### Problem Statement
IFC is the open BIM standard for interoperability, but:
- Native Revit IFC export requires Autodesk license
- Export settings significantly affect data quality
- Batch processing is manual and time-consuming

#### Solution
RVT2IFCconverter.exe converts Revit files to IFC offline, without licenses, with full control over export settings.

#### Business Value
- **No license required** - Works without Autodesk software
- **Multiple IFC versions** - IFC2x3, IFC4, IFC4.3 support
- **Batch processing** - Convert thousands of files
- **Consistent quality** - Standardized export settings

### Technical Implementation

#### CLI Syntax
```bash
RVT2IFCconverter.exe <input.rvt> [<output.ifc>] [preset=<name>] [config="..."]
```

#### IFC Versions
| Version | Use Case |
|---------|----------|
| IFC2x3 | Legacy compatibility, most software |
| IFC4 | Enhanced properties, modern BIM |
| IFC4.3 | Infrastructure, latest standard |

#### Export Presets
| Preset | Description |
|--------|-------------|
| `standard` | Default balanced export |
| `extended` | Maximum detail and properties |
| `custom` | User-defined configuration |

#### Examples

```bash
## Standard IFC export
RVT2IFCconverter.exe "C:\Projects\Building.rvt"

## IFC4 with extended settings
RVT2IFCconverter.exe "C:\Projects\Building.rvt" preset=extended

## Custom output path
RVT2IFCconverter.exe "C:\Projects\Building.rvt" "D:\Export\model.ifc"

## Custom configuration
RVT2IFCconverter.exe "C:\Projects\Building.rvt" config="ExportBaseQuantities=true; SitePlacement=Shared"
```

#### Python Integration

```python
import subprocess
from pathlib import Path
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum


class IFCVersion(Enum):
    """IFC schema versions."""
    IFC2X3 = "IFC2x3"
    IFC4 = "IFC4"
    IFC4X3 = "IFC4x3"


class ExportPreset(Enum):
    """Export presets."""
    STANDARD = "standard"
    EXTENDED = "extended"
    CUSTOM = "custom"


@dataclass
class IFCExportConfig:
    """IFC export configuration."""
    ifc_version: IFCVersion = IFCVersion.IFC4
    export_base_quantities: bool = True
    site_placement: str = "Shared"
    split_walls_and_columns: bool = False
    include_steel_elements: bool = True
    export_2d_elements: bool = False
    export_linked_files: bool = False
    export_rooms: bool = True
    export_schedules: bool = True

    def to_config_string(self) -> str:
        """Convert to CLI config string."""
        parts = [
            f"ExportBaseQuantities={str(self.export_base_quantities).lower()}",
            f"SitePlacement={self.site_placement}",
            f"SplitWallsAndColumns={str(self.split_walls_and_columns).lower()}",
            f"IncludeSteelElements={str(self.include_steel_elements).lower()}",
            f"Export2DElements={str(self.export_2d_elements).lower()}",
            f"ExportLinkedFiles={str(self.export_linked_files).lower()}",
            f"ExportRooms={str(self.export_rooms).lower()}"
        ]
        return "; ".join(parts)


class RevitToIFCConverter:
    """Convert Revit files to IFC format."""

    def __init__(self, converter_path: str = "RVT2IFCconverter.exe"):
        self.converter = Path(converter_path)
        if not self.converter.exists():
            raise FileNotFoundError(f"Converter not found: {converter_path}")

    def convert(self, rvt_file: str,
                output_path: Optional[str] = None,
                preset: ExportPreset = ExportPreset.STANDARD,
                config: Optional[IFCExportConfig] = None) -> Path:
        """Convert Revit file to IFC."""

        rvt_path = Path(rvt_file)
        if not rvt_path.exists():
            raise FileNotFoundError(f"Revit file not found: {rvt_file}")

        # Build command
        cmd = [str(self.converter), str(rvt_path)]

        # Add output path if specified
        if output_path:
            cmd.append(output_path)

        # Add preset
        cmd.append(f"preset={preset.value}")

        # Add custom config if provided
        if config:
            cmd.append(f'config="{config.to_config_string()}"')

        # Execute
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Conversion failed: {result.stderr}")

        # Return output path
        if output_path:
            return Path(output_path)
        return rvt_path.with_suffix('.ifc')

    def batch_convert(self, folder: str,
                      output_folder: Optional[str] = None,
                      preset: ExportPreset = ExportPreset.STANDARD,
                      config: Optional[IFCExportConfig] = None) -> List[Dict[str, Any]]:
        """Convert all Revit files in folder."""

        folder_path = Path(folder)
        results = []

        for rvt_file in folder_path.glob("**/*.rvt"):
            try:
                # Determine output path
                if output_folder:
                    out_dir = Path(output_folder)
                    out_dir.mkdir(parents=True, exist_ok=True)
                    output_path = str(out_dir / rvt_file.with_suffix('.ifc').name)
                else:
                    output_path = None

                ifc_path = self.convert(str(rvt_file), output_path, preset, config)
                results.append({
                    'input': str(rvt_file),
                    'output': str(ifc_path),
                    'status': 'success'
                })
                print(f"✓ Converted: {rvt_file.name}")

            except Exception as e:
                results.append({
                    'input': str(rvt_file),
                    'output': None,
                    'status': 'failed',
                    'error': str(e)
                })
                print(f"✗ Failed: {rvt_file.name} - {e}")

        return results

    def validate_output(self, ifc_file: str) -> Dict[str, Any]:
        """Basic validation of generated IFC."""

        ifc_path = Path(ifc_file)
        if not ifc_path.exists():
            return {'valid': False, 'error': 'File not found'}

        # Basic file checks
        file_size = ifc_path.stat().st_size

        if file_size < 1000:
            return {'valid': False, 'error': 'File too small'}

        # Read header
        with open(ifc_file, 'r', errors='ignore') as f:
            header = f.read(1000)

        # Check IFC format
        if 'ISO-10303-21' not in header:
            return {'valid': False, 'error': 'Not a valid IFC file'}

        # Detect version
        version = 'Unknown'
        if 'IFC4X3' in header:
            version = 'IFC4.3'
        elif 'IFC4' in header:
            version = 'IFC4'
        elif 'IFC2X3' in header:
            version = 'IFC2x3'

        return {
            'valid': True,
            'file_size': file_size,
            'ifc_version': version
        }


class IFCQualityChecker:
    """Check quality of IFC exports."""

    def __init__(self, converter: RevitToIFCConverter):
        self.converter = converter

    def compare_presets(self, rvt_file: str) -> Dict[str, Any]:
        """Compare different export presets."""

        results = {}

        for preset in [ExportPreset.STANDARD, ExportPreset.EXTENDED]:
            try:
                output = Path(rvt_file).with_suffix(f'.{preset.value}.ifc')
                self.converter.convert(rvt_file, str(output), preset)

                validation = self.converter.validate_output(str(output))
                results[preset.value] = {
                    'file_size': validation.get('file_size', 0),
                    'valid': validation.get('valid', False)
                }
            except Exception as e:
                results[preset.value] = {'error': str(e)}

        return results


## Convenience functions
def convert_revit_to_ifc(rvt_file: str,
                         converter_path: str = "RVT2IFCconverter.exe") -> str:
    """Quick conversion of Revit to IFC."""
    converter = RevitToIFCConverter(converter_path)
    output = converter.convert(rvt_file)
    return str(output)


def batch_convert_to_ifc(folder: str,
                         converter_path: str = "RVT2IFCconverter.exe") -> List[str]:
    """Batch convert all Revit files to IFC."""
    converter = RevitToIFCConverter(converter_path)
    results = converter.batch_convert(folder)
    return [r['output'] for r in results if r['status'] == 'success']
```

### Quick Start

```python
## Initialize converter
converter = RevitToIFCConverter("C:/DDC/RVT2IFCconverter.exe")

## Basic conversion
ifc = converter.convert("building.rvt")
print(f"Created: {ifc}")

## With custom config
config = IFCExportConfig(
    ifc_version=IFCVersion.IFC4,
    export_base_quantities=True,
    export_rooms=True
)
ifc = converter.convert("building.rvt", preset=ExportPreset.CUSTOM, config=config)
```

### Common Use Cases

#### 1. Batch Processing
```python
converter = RevitToIFCConverter()
results = converter.batch_convert(
    folder="C:/Projects",
    output_folder="C:/IFC_Export",
    preset=ExportPreset.EXTENDED
)
print(f"Converted {len([r for r in results if r['status'] == 'success'])} files")
```

#### 2. Quality Check
```python
validation = converter.validate_output("model.ifc")
print(f"Valid: {validation['valid']}, Version: {validation['ifc_version']}")
```

#### 3. Compare Presets
```python
checker = IFCQualityChecker(converter)
comparison = checker.compare_presets("building.rvt")
print(comparison)
```

### Resources

- **GitHub**: [cad2data Pipeline](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)
- **buildingSMART IFC**: https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/


## ifc-to-excel

> Convert IFC files (2x3, 4x1, 4x3) to Excel databases using IfcExporter CLI. Extract BIM data, properties, and geometry without proprietary software.

## IFC to Excel Conversion

### Business Case

#### Problem Statement
IFC (Industry Foundation Classes) is the open BIM standard, but:
- Reading IFC requires specialized software
- Property extraction needs programming knowledge
- Batch processing is manual and time-consuming
- Integration with analytics tools is complex

#### Solution
IfcExporter.exe converts IFC files to structured Excel databases, making BIM data accessible for analysis, validation, and reporting.

#### Business Value
- **Open standard** - Process any IFC file (2x3, 4x, 4.3)
- **No licenses** - Works offline without BIM software
- **Data extraction** - All properties, quantities, materials
- **3D geometry** - Export to Collada DAE format
- **Pipeline ready** - Integrate with ETL workflows

### Technical Implementation

#### CLI Syntax
```bash
IfcExporter.exe <input_ifc> [options]
```

#### Supported IFC Versions
| Version | Schema | Description |
|---------|--------|-------------|
| IFC2x3 | MVD | Most common exchange format |
| IFC4 | ADD1 | Enhanced properties |
| IFC4x1 | Alignment | Infrastructure support |
| IFC4x3 | Latest | Full infrastructure |

#### Output Formats
| Output | Description |
|--------|-------------|
| `.xlsx` | Excel database with elements and properties |
| `.dae` | Collada 3D geometry with matching IDs |

#### Options
| Option | Description |
|--------|-------------|
| `bbox` | Include element bounding boxes |
| `-no-xlsx` | Skip Excel export |
| `-no-collada` | Skip 3D geometry export |

#### Examples

```bash
## Basic conversion (XLSX + DAE)
IfcExporter.exe "C:\Models\Building.ifc"

## With bounding boxes
IfcExporter.exe "C:\Models\Building.ifc" bbox

## Excel only (no 3D geometry)
IfcExporter.exe "C:\Models\Building.ifc" -no-collada

## Batch processing
for /R "C:\IFC_Models" %f in (*.ifc) do IfcExporter.exe "%f" bbox
```

#### Python Integration

```python
import subprocess
import pandas as pd
from pathlib import Path
from typing import List, Optional, Dict, Any, Set
from dataclasses import dataclass, field
from enum import Enum
import json


class IFCVersion(Enum):
    """IFC schema versions."""
    IFC2X3 = "IFC2X3"
    IFC4 = "IFC4"
    IFC4X1 = "IFC4X1"
    IFC4X3 = "IFC4X3"


class IFCEntityType(Enum):
    """Common IFC entity types."""
    IFCWALL = "IfcWall"
    IFCWALLSTANDARDCASE = "IfcWallStandardCase"
    IFCSLAB = "IfcSlab"
    IFCCOLUMN = "IfcColumn"
    IFCBEAM = "IfcBeam"
    IFCDOOR = "IfcDoor"
    IFCWINDOW = "IfcWindow"
    IFCROOF = "IfcRoof"
    IFCSTAIR = "IfcStair"
    IFCRAILING = "IfcRailing"
    IFCFURNISHINGELEMENT = "IfcFurnishingElement"
    IFCSPACE = "IfcSpace"
    IFCBUILDINGSTOREY = "IfcBuildingStorey"
    IFCBUILDING = "IfcBuilding"
    IFCSITE = "IfcSite"


@dataclass
class IFCElement:
    """Represents an IFC element."""
    global_id: str
    ifc_type: str
    name: str
    description: Optional[str]
    object_type: Optional[str]
    level: Optional[str]

    # Quantities
    area: Optional[float] = None
    volume: Optional[float] = None
    length: Optional[float] = None
    height: Optional[float] = None
    width: Optional[float] = None

    # Bounding box (if exported)
    bbox_min_x: Optional[float] = None
    bbox_min_y: Optional[float] = None
    bbox_min_z: Optional[float] = None
    bbox_max_x: Optional[float] = None
    bbox_max_y: Optional[float] = None
    bbox_max_z: Optional[float] = None

    # Properties
    properties: Dict[str, Any] = field(default_factory=dict)
    materials: List[str] = field(default_factory=list)


@dataclass
class IFCProperty:
    """Represents an IFC property."""
    pset_name: str
    property_name: str
    value: Any
    value_type: str


@dataclass
class IFCMaterial:
    """Represents an IFC material."""
    name: str
    category: Optional[str]
    thickness: Optional[float]
    layer_position: Optional[int]


class IFCExporter:
    """IFC to Excel converter using DDC IfcExporter CLI."""

    def __init__(self, exporter_path: str = "IfcExporter.exe"):
        self.exporter = Path(exporter_path)
        if not self.exporter.exists():
            raise FileNotFoundError(f"IfcExporter not found: {exporter_path}")

    def convert(self, ifc_file: str,
                include_bbox: bool = True,
                export_xlsx: bool = True,
                export_collada: bool = True) -> Path:
        """Convert IFC file to Excel."""
        ifc_path = Path(ifc_file)
        if not ifc_path.exists():
            raise FileNotFoundError(f"IFC file not found: {ifc_file}")

        cmd = [str(self.exporter), str(ifc_path)]

        if include_bbox:
            cmd.append("bbox")
        if not export_xlsx:
            cmd.append("-no-xlsx")
        if not export_collada:
            cmd.append("-no-collada")

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Export failed: {result.stderr}")

        return ifc_path.with_suffix('.xlsx')

    def batch_convert(self, folder: str,
                      include_subfolders: bool = True,
                      include_bbox: bool = True) -> List[Dict[str, Any]]:
        """Convert all IFC files in folder."""
        folder_path = Path(folder)
        pattern = "**/*.ifc" if include_subfolders else "*.ifc"

        results = []
        for ifc_file in folder_path.glob(pattern):
            try:
                output = self.convert(str(ifc_file), include_bbox)
                results.append({
                    'input': str(ifc_file),
                    'output': str(output),
                    'status': 'success'
                })
                print(f"✓ Converted: {ifc_file.name}")
            except Exception as e:
                results.append({
                    'input': str(ifc_file),
                    'output': None,
                    'status': 'failed',
                    'error': str(e)
                })
                print(f"✗ Failed: {ifc_file.name} - {e}")

        return results

    def read_elements(self, xlsx_file: str) -> pd.DataFrame:
        """Read converted Excel as DataFrame."""
        return pd.read_excel(xlsx_file, sheet_name="Elements")

    def get_element_types(self, xlsx_file: str) -> pd.DataFrame:
        """Get element type summary."""
        df = self.read_elements(xlsx_file)

        if 'IfcType' not in df.columns:
            raise ValueError("IfcType column not found")

        summary = df.groupby('IfcType').agg({
            'GlobalId': 'count',
            'Volume': 'sum' if 'Volume' in df.columns else 'count',
            'Area': 'sum' if 'Area' in df.columns else 'count'
        }).reset_index()

        summary.columns = ['IFC_Type', 'Count', 'Total_Volume', 'Total_Area']
        return summary.sort_values('Count', ascending=False)

    def get_levels(self, xlsx_file: str) -> pd.DataFrame:
        """Get building level summary."""
        df = self.read_elements(xlsx_file)

        level_col = None
        for col in ['Level', 'BuildingStorey', 'IfcBuildingStorey']:
            if col in df.columns:
                level_col = col
                break

        if level_col is None:
            return pd.DataFrame(columns=['Level', 'Element_Count'])

        summary = df.groupby(level_col).agg({
            'GlobalId': 'count'
        }).reset_index()
        summary.columns = ['Level', 'Element_Count']
        return summary

    def get_materials(self, xlsx_file: str) -> pd.DataFrame:
        """Get material summary."""
        df = self.read_elements(xlsx_file)

        if 'Material' not in df.columns:
            return pd.DataFrame(columns=['Material', 'Count'])

        summary = df.groupby('Material').agg({
            'GlobalId': 'count'
        }).reset_index()
        summary.columns = ['Material', 'Element_Count']
        return summary.sort_values('Element_Count', ascending=False)

    def get_quantities(self, xlsx_file: str,
                       group_by: str = 'IfcType') -> pd.DataFrame:
        """Get quantity takeoff summary."""
        df = self.read_elements(xlsx_file)

        if group_by not in df.columns:
            raise ValueError(f"Column {group_by} not found")

        agg_dict = {'GlobalId': 'count'}

        # Add numeric columns for aggregation
        numeric_cols = ['Volume', 'Area', 'Length', 'Width', 'Height']
        for col in numeric_cols:
            if col in df.columns:
                agg_dict[col] = 'sum'

        summary = df.groupby(group_by).agg(agg_dict).reset_index()
        return summary

    def filter_by_type(self, xlsx_file: str,
                       ifc_types: List[str]) -> pd.DataFrame:
        """Filter elements by IFC type."""
        df = self.read_elements(xlsx_file)
        return df[df['IfcType'].isin(ifc_types)]

    def get_properties(self, xlsx_file: str,
                       element_id: str) -> Dict[str, Any]:
        """Get all properties for specific element."""
        df = self.read_elements(xlsx_file)
        element = df[df['GlobalId'] == element_id]

        if element.empty:
            return {}

        # Convert row to dictionary, excluding NaN values
        props = element.iloc[0].dropna().to_dict()
        return props

    def validate_ifc_data(self, xlsx_file: str) -> Dict[str, Any]:
        """Validate IFC data quality."""
        df = self.read_elements(xlsx_file)

        validation = {
            'total_elements': len(df),
            'issues': []
        }

        # Check for missing GlobalIds
        if 'GlobalId' in df.columns:
            missing_ids = df['GlobalId'].isna().sum()
            if missing_ids > 0:
                validation['issues'].append(f"{missing_ids} elements missing GlobalId")

        # Check for missing names
        if 'Name' in df.columns:
            missing_names = df['Name'].isna().sum()
            if missing_names > 0:
                validation['issues'].append(f"{missing_names} elements missing Name")

        # Check for zero quantities
        for col in ['Volume', 'Area']:
            if col in df.columns:
                zero_qty = (df[col] == 0).sum()
                if zero_qty > 0:
                    validation['issues'].append(f"{zero_qty} elements with zero {col}")

        # Check for duplicate GlobalIds
        if 'GlobalId' in df.columns:
            duplicates = df['GlobalId'].duplicated().sum()
            if duplicates > 0:
                validation['issues'].append(f"{duplicates} duplicate GlobalIds")

        validation['is_valid'] = len(validation['issues']) == 0
        return validation


class IFCQuantityTakeoff:
    """Quantity takeoff from IFC data."""

    def __init__(self, exporter: IFCExporter):
        self.exporter = exporter

    def generate_qto(self, ifc_file: str) -> Dict[str, pd.DataFrame]:
        """Generate complete quantity takeoff."""
        xlsx = self.exporter.convert(ifc_file, include_bbox=True)
        df = self.exporter.read_elements(str(xlsx))

        qto = {}

        # Walls
        walls = df[df['IfcType'].str.contains('Wall', case=False, na=False)]
        if not walls.empty:
            qto['Walls'] = self._summarize_elements(walls, 'Type Name')

        # Slabs
        slabs = df[df['IfcType'].str.contains('Slab', case=False, na=False)]
        if not slabs.empty:
            qto['Slabs'] = self._summarize_elements(slabs, 'Type Name')

        # Columns
        columns = df[df['IfcType'].str.contains('Column', case=False, na=False)]
        if not columns.empty:
            qto['Columns'] = self._summarize_elements(columns, 'Type Name')

        # Beams
        beams = df[df['IfcType'].str.contains('Beam', case=False, na=False)]
        if not beams.empty:
            qto['Beams'] = self._summarize_elements(beams, 'Type Name')

        # Doors
        doors = df[df['IfcType'].str.contains('Door', case=False, na=False)]
        if not doors.empty:
            qto['Doors'] = self._summarize_elements(doors, 'Type Name')

        # Windows
        windows = df[df['IfcType'].str.contains('Window', case=False, na=False)]
        if not windows.empty:
            qto['Windows'] = self._summarize_elements(windows, 'Type Name')

        return qto

    def _summarize_elements(self, df: pd.DataFrame,
                            group_col: str) -> pd.DataFrame:
        """Summarize elements by grouping column."""
        if group_col not in df.columns:
            group_col = 'IfcType'

        agg_dict = {'GlobalId': 'count'}
        for col in ['Volume', 'Area', 'Length']:
            if col in df.columns:
                agg_dict[col] = 'sum'

        summary = df.groupby(group_col).agg(agg_dict).reset_index()
        summary.rename(columns={'GlobalId': 'Count'}, inplace=True)
        return summary

    def export_to_excel(self, qto: Dict[str, pd.DataFrame],
                        output_file: str):
        """Export QTO to multi-sheet Excel."""
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for sheet_name, df in qto.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)


## Convenience functions
def convert_ifc_to_excel(ifc_file: str,
                         exporter_path: str = "IfcExporter.exe") -> str:
    """Quick conversion of IFC to Excel."""
    exporter = IFCExporter(exporter_path)
    output = exporter.convert(ifc_file)
    return str(output)


def get_ifc_summary(xlsx_file: str) -> Dict[str, Any]:
    """Get summary of converted IFC data."""
    df = pd.read_excel(xlsx_file, sheet_name="Elements")

    return {
        'total_elements': len(df),
        'ifc_types': df['IfcType'].nunique() if 'IfcType' in df.columns else 0,
        'levels': df['Level'].nunique() if 'Level' in df.columns else 0,
        'total_volume': df['Volume'].sum() if 'Volume' in df.columns else 0,
        'total_area': df['Area'].sum() if 'Area' in df.columns else 0
    }
```

### Output Structure

#### Excel Sheets
| Sheet | Content |
|-------|---------|
| Elements | All IFC elements with properties |
| Types | Element types summary |
| Levels | Building storey data |
| Materials | Material assignments |
| PropertySets | IFC property sets |

#### Element Columns
| Column | Type | Description |
|--------|------|-------------|
| GlobalId | string | IFC GUID |
| IfcType | string | IFC entity type |
| Name | string | Element name |
| Description | string | Element description |
| Level | string | Building storey |
| Material | string | Primary material |
| Volume | float | Volume (m³) |
| Area | float | Surface area (m²) |
| Length | float | Length (m) |
| Height | float | Height (m) |
| Width | float | Width (m) |

### Quick Start

```python
## Initialize exporter
exporter = IFCExporter("C:/DDC/IfcExporter.exe")

## Convert IFC to Excel
xlsx = exporter.convert("C:/Models/Building.ifc", include_bbox=True)

## Read elements
df = exporter.read_elements(str(xlsx))
print(f"Total elements: {len(df)}")

## Get element types
types = exporter.get_element_types(str(xlsx))
print(types)

## Get quantities by type
qto = exporter.get_quantities(str(xlsx), group_by='IfcType')
print(qto)
```

### Common Use Cases

#### 1. Model Validation
```python
exporter = IFCExporter()
xlsx = exporter.convert("model.ifc")
validation = exporter.validate_ifc_data(str(xlsx))

if not validation['is_valid']:
    print("Issues found:")
    for issue in validation['issues']:
        print(f"  - {issue}")
```

#### 2. Quantity Takeoff
```python
qto_generator = IFCQuantityTakeoff(exporter)
qto = qto_generator.generate_qto("building.ifc")

for category, data in qto.items():
    print(f"\n{category}:")
    print(data.to_string(index=False))
```

#### 3. Material Schedule
```python
xlsx = exporter.convert("building.ifc")
materials = exporter.get_materials(str(xlsx))
print(materials)
```

### Integration with DDC Pipeline

```python
## Full pipeline: IFC → Excel → Validation → Cost Estimate
exporter = IFCExporter("C:/DDC/IfcExporter.exe")

## 1. Convert IFC
xlsx = exporter.convert("project.ifc", include_bbox=True)

## 2. Validate data
validation = exporter.validate_ifc_data(str(xlsx))
print(f"Valid: {validation['is_valid']}")

## 3. Generate QTO
qto = IFCQuantityTakeoff(exporter)
quantities = qto.generate_qto("project.ifc")

## 4. Export for cost estimation
qto.export_to_excel(quantities, "project_qto.xlsx")
```

### Resources

- **GitHub**: [cad2data Pipeline](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)
- **IFC Standard**: [buildingSMART](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/)
- **DDC Book**: Chapter 2.4 - CAD/BIM Data Extraction


## excel-to-bim

> Push Excel data back to BIM models. Update parameters, properties, and attributes from structured spreadsheets.

## Excel to BIM Update

### Business Case

#### Problem Statement
After extracting BIM data to Excel and enriching it (cost codes, classifications, custom data):
- Changes need to flow back to the BIM model
- Manual re-entry is error-prone
- Updates must match by element ID

#### Solution
Push Excel data back to BIM models, updating element parameters and properties from spreadsheet changes.

#### Business Value
- **Bi-directional workflow** - BIM → Excel → BIM
- **Bulk updates** - Change thousands of parameters
- **Data enrichment** - Add classifications, codes, costs
- **Consistency** - Spreadsheet as single source of truth

### Technical Implementation

#### Workflow
```
BIM Model (Revit/IFC) → Excel Export → Data Enrichment → Excel Update → BIM Model
```

#### Python Implementation

```python
import pandas as pd
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import json


class UpdateType(Enum):
    """Type of BIM parameter update."""
    TEXT = "text"
    NUMBER = "number"
    BOOLEAN = "boolean"
    ELEMENT_ID = "element_id"


@dataclass
class ParameterMapping:
    """Mapping between Excel column and BIM parameter."""
    excel_column: str
    bim_parameter: str
    update_type: UpdateType
    transform: Optional[str] = None  # Optional transformation


@dataclass
class UpdateResult:
    """Result of single element update."""
    element_id: str
    parameters_updated: List[str]
    success: bool
    error: Optional[str] = None


@dataclass
class BatchUpdateResult:
    """Result of batch update operation."""
    total_elements: int
    updated: int
    failed: int
    skipped: int
    results: List[UpdateResult]


class ExcelToBIMUpdater:
    """Update BIM models from Excel data."""

    # Standard ID column names
    ID_COLUMNS = ['ElementId', 'GlobalId', 'GUID', 'Id', 'UniqueId']

    def __init__(self):
        self.mappings: List[ParameterMapping] = []

    def add_mapping(self, excel_col: str, bim_param: str,
                    update_type: UpdateType = UpdateType.TEXT):
        """Add column to parameter mapping."""
        self.mappings.append(ParameterMapping(
            excel_column=excel_col,
            bim_parameter=bim_param,
            update_type=update_type
        ))

    def load_excel(self, file_path: str,
                   sheet_name: str = None) -> pd.DataFrame:
        """Load Excel data for update."""
        if sheet_name:
            return pd.read_excel(file_path, sheet_name=sheet_name)
        return pd.read_excel(file_path)

    def detect_id_column(self, df: pd.DataFrame) -> Optional[str]:
        """Detect element ID column in DataFrame."""
        for col in self.ID_COLUMNS:
            if col in df.columns:
                return col
            # Case-insensitive check
            for df_col in df.columns:
                if df_col.lower() == col.lower():
                    return df_col
        return None

    def prepare_updates(self, df: pd.DataFrame,
                        id_column: str = None) -> List[Dict[str, Any]]:
        """Prepare update instructions from DataFrame."""

        if id_column is None:
            id_column = self.detect_id_column(df)
            if id_column is None:
                raise ValueError("Cannot detect ID column")

        updates = []

        for _, row in df.iterrows():
            element_id = str(row[id_column])

            params = {}
            for mapping in self.mappings:
                if mapping.excel_column in df.columns:
                    value = row[mapping.excel_column]

                    # Convert value based on type
                    if mapping.update_type == UpdateType.NUMBER:
                        value = float(value) if pd.notna(value) else 0
                    elif mapping.update_type == UpdateType.BOOLEAN:
                        value = bool(value) if pd.notna(value) else False
                    elif mapping.update_type == UpdateType.TEXT:
                        value = str(value) if pd.notna(value) else ""

                    params[mapping.bim_parameter] = value

            if params:
                updates.append({
                    'element_id': element_id,
                    'parameters': params
                })

        return updates

    def generate_dynamo_script(self, updates: List[Dict],
                               output_path: str) -> str:
        """Generate Dynamo script for Revit updates."""

        # Generate Python code for Dynamo
        script = '''
## Dynamo Python Script for Revit Parameter Updates
## Generated by DDC Excel-to-BIM

import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

## Update data
updates = '''
        script += json.dumps(updates, indent=2)
        script += '''

## Apply updates
TransactionManager.Instance.EnsureInTransaction(doc)

results = []
for update in updates:
    try:
        element_id = int(update['element_id'])
        element = doc.GetElement(ElementId(element_id))

        if element:
            for param_name, value in update['parameters'].items():
                param = element.LookupParameter(param_name)
                if param and not param.IsReadOnly:
                    if isinstance(value, (int, float)):
                        param.Set(float(value))
                    elif isinstance(value, bool):
                        param.Set(1 if value else 0)
                    else:
                        param.Set(str(value))
            results.append({'id': element_id, 'status': 'success'})
        else:
            results.append({'id': element_id, 'status': 'not found'})
    except Exception as e:
        results.append({'id': update['element_id'], 'status': str(e)})

TransactionManager.Instance.TransactionTaskDone()

OUT = results
'''

        with open(output_path, 'w') as f:
            f.write(script)

        return output_path

    def generate_ifc_updates(self, updates: List[Dict],
                             original_ifc: str,
                             output_ifc: str) -> str:
        """Generate updated IFC file (requires IfcOpenShell)."""

        try:
            import ifcopenshell
        except ImportError:
            raise ImportError("IfcOpenShell required for IFC updates")

        ifc = ifcopenshell.open(original_ifc)

        for update in updates:
            guid = update['element_id']

            # Find element by GUID
            element = ifc.by_guid(guid)
            if not element:
                continue

            # Update properties
            for param_name, value in update['parameters'].items():
                # This is simplified - actual IFC property handling is more complex
                # Would need to find/create property sets and properties
                pass

        ifc.write(output_ifc)
        return output_ifc

    def generate_update_report(self, original_df: pd.DataFrame,
                               updates: List[Dict],
                               output_path: str) -> str:
        """Generate report of planned updates."""

        report_data = []
        for update in updates:
            for param, value in update['parameters'].items():
                report_data.append({
                    'element_id': update['element_id'],
                    'parameter': param,
                    'new_value': value
                })

        report_df = pd.DataFrame(report_data)
        report_df.to_excel(output_path, index=False)
        return output_path


class RevitExcelUpdater(ExcelToBIMUpdater):
    """Specialized updater for Revit via ImportExcelToRevit."""

    def __init__(self, tool_path: str = "ImportExcelToRevit.exe"):
        super().__init__()
        self.tool_path = Path(tool_path)

    def update_revit(self, excel_file: str,
                     rvt_file: str,
                     sheet_name: str = "Elements") -> BatchUpdateResult:
        """Update Revit file from Excel using CLI tool."""

        import subprocess

        # This assumes ImportExcelToRevit CLI tool
        cmd = [
            str(self.tool_path),
            rvt_file,
            excel_file,
            sheet_name
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        # Parse results (format depends on tool output)
        if result.returncode == 0:
            return BatchUpdateResult(
                total_elements=0,  # Would parse from output
                updated=0,
                failed=0,
                skipped=0,
                results=[]
            )
        else:
            raise RuntimeError(f"Update failed: {result.stderr}")


class DataEnrichmentWorkflow:
    """Complete workflow for data enrichment and update."""

    def __init__(self):
        self.updater = ExcelToBIMUpdater()

    def enrich_and_update(self, original_excel: str,
                          enrichment_excel: str,
                          merge_column: str) -> pd.DataFrame:
        """Merge enrichment data with original export."""

        original = pd.read_excel(original_excel)
        enrichment = pd.read_excel(enrichment_excel)

        # Merge on specified column
        merged = original.merge(enrichment, on=merge_column, how='left',
                                suffixes=('', '_enriched'))

        return merged

    def create_classification_mapping(self, df: pd.DataFrame,
                                      type_column: str,
                                      classification_file: str) -> pd.DataFrame:
        """Map BIM types to classification codes."""

        classifications = pd.read_excel(classification_file)

        # Fuzzy matching could be added here
        merged = df.merge(classifications,
                          left_on=type_column,
                          right_on='type_description',
                          how='left')

        return merged
```

### Quick Start

```python
## Initialize updater
updater = ExcelToBIMUpdater()

## Define mappings
updater.add_mapping('Classification_Code', 'OmniClassCode', UpdateType.TEXT)
updater.add_mapping('Unit_Cost', 'Cost', UpdateType.NUMBER)

## Load enriched Excel
df = updater.load_excel("enriched_model.xlsx")

## Prepare updates
updates = updater.prepare_updates(df)
print(f"Prepared {len(updates)} updates")

## Generate Dynamo script for Revit
updater.generate_dynamo_script(updates, "update_parameters.py")
```

### Common Use Cases

#### 1. Add Classification Codes
```python
updater = ExcelToBIMUpdater()
updater.add_mapping('Omniclass', 'OmniClass_Number', UpdateType.TEXT)
updater.add_mapping('Uniclass', 'Uniclass_Code', UpdateType.TEXT)

df = updater.load_excel("classified_elements.xlsx")
updates = updater.prepare_updates(df)
```

#### 2. Cost Data Integration
```python
updater.add_mapping('Material_Cost', 'Pset_MaterialCost', UpdateType.NUMBER)
updater.add_mapping('Labor_Cost', 'Pset_LaborCost', UpdateType.NUMBER)
```

#### 3. Generate Update Report
```python
report = updater.generate_update_report(df, updates, "planned_updates.xlsx")
```

### Integration with DDC Pipeline

```python
## Full round-trip: Revit → Excel → Enrich → Update → Revit

## 1. Export from Revit
## RvtExporter.exe model.rvt complete

## 2. Enrich in Python/Excel
df = pd.read_excel("model.xlsx")
## Add classifications, costs, etc.
df['OmniClass'] = df['Type Name'].map(classification_dict)
df.to_excel("enriched_model.xlsx")

## 3. Generate update script
updater = ExcelToBIMUpdater()
updater.add_mapping('OmniClass', 'OmniClass_Number')
updates = updater.prepare_updates(df)
updater.generate_dynamo_script(updates, "apply_updates.py")

## 4. Run in Dynamo to update Revit
```

### Resources
- **GitHub**: [DDC Update Revit from Excel](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/tree/main/DDC_Update_Revit_from_Excel)
- **DDC Book**: Chapter 2.4 - Bidirectional Data Flow


## ifc-data-extraction

> Extract structured data from IFC (Industry Foundation Classes) files using IfcOpenShell. Parse BIM models, extract quantities, properties, spatial relationships, and export to various formats.

## IFC Data Extraction

### Overview

This skill provides comprehensive IFC file parsing and data extraction using IfcOpenShell. Extract element data, quantities, properties, and relationships from BIM models for analysis and reporting.

**Based on Open BIM Standards** - Working with vendor-neutral IFC format for maximum interoperability.

> "IFC является открытым стандартом для обмена BIM-данными, позволяющим извлекать информацию независимо от программного обеспечения."
> — DDC Methodology

### Quick Start

```python
import ifcopenshell
import ifcopenshell.util.element as element_util
import pandas as pd

## Open IFC file
ifc = ifcopenshell.open("model.ifc")

## Get project info
project = ifc.by_type("IfcProject")[0]
print(f"Project: {project.Name}")

## Extract all walls
walls = ifc.by_type("IfcWall")
print(f"Total walls: {len(walls)}")

## Get wall data
wall_data = []
for wall in walls:
    psets = element_util.get_psets(wall)
    wall_data.append({
        'GlobalId': wall.GlobalId,
        'Name': wall.Name,
        'Type': wall.is_a(),
        'Level': get_level(wall),
        'Properties': psets
    })

df = pd.DataFrame(wall_data)
print(df.head())
```

### Core Extraction Functions

#### Element Extractor Class

```python
import ifcopenshell
import ifcopenshell.util.element as element_util
import ifcopenshell.util.placement as placement_util
import ifcopenshell.geom
import pandas as pd
from typing import List, Dict, Optional, Any

class IFCExtractor:
    """Extract data from IFC files"""

    def __init__(self, ifc_path: str):
        self.model = ifcopenshell.open(ifc_path)
        self.settings = ifcopenshell.geom.settings()

    def get_project_info(self) -> Dict:
        """Extract project metadata"""
        project = self.model.by_type("IfcProject")[0]
        site = self.model.by_type("IfcSite")
        building = self.model.by_type("IfcBuilding")

        return {
            'project_id': project.GlobalId,
            'project_name': project.Name,
            'description': project.Description,
            'site_count': len(site),
            'building_count': len(building),
            'schema': self.model.schema
        }

    def get_all_elements(self, element_types: List[str] = None) -> pd.DataFrame:
        """Extract all elements of specified types"""
        if element_types is None:
            element_types = [
                'IfcWall', 'IfcSlab', 'IfcColumn', 'IfcBeam',
                'IfcDoor', 'IfcWindow', 'IfcStair', 'IfcRoof'
            ]

        all_elements = []

        for ifc_type in element_types:
            elements = self.model.by_type(ifc_type)

            for elem in elements:
                data = self._extract_element_data(elem)
                data['IFC_Type'] = ifc_type
                all_elements.append(data)

        return pd.DataFrame(all_elements)

    def _extract_element_data(self, element) -> Dict:
        """Extract data from single element"""
        # Basic info
        data = {
            'GlobalId': element.GlobalId,
            'Name': element.Name,
            'Description': element.Description,
            'ObjectType': element.ObjectType if hasattr(element, 'ObjectType') else None
        }

        # Get level/storey
        data['Level'] = self._get_element_level(element)

        # Get material
        data['Material'] = self._get_element_material(element)

        # Get type
        data['TypeName'] = self._get_element_type(element)

        # Get all property sets
        psets = element_util.get_psets(element)
        data['PropertySets'] = psets

        # Extract common quantities
        base_quantities = psets.get('BaseQuantities', {})
        data.update({
            'Length': base_quantities.get('Length'),
            'Width': base_quantities.get('Width'),
            'Height': base_quantities.get('Height'),
            'Area': base_quantities.get('NetSideArea') or base_quantities.get('GrossArea'),
            'Volume': base_quantities.get('NetVolume') or base_quantities.get('GrossVolume')
        })

        return data

    def _get_element_level(self, element) -> Optional[str]:
        """Get the building storey for an element"""
        if hasattr(element, 'ContainedInStructure'):
            for rel in element.ContainedInStructure or []:
                if rel.RelatingStructure.is_a('IfcBuildingStorey'):
                    return rel.RelatingStructure.Name
        return None

    def _get_element_material(self, element) -> Optional[str]:
        """Get material name for element"""
        if hasattr(element, 'HasAssociations'):
            for rel in element.HasAssociations or []:
                if rel.is_a('IfcRelAssociatesMaterial'):
                    material = rel.RelatingMaterial
                    if hasattr(material, 'Name'):
                        return material.Name
                    elif hasattr(material, 'ForLayerSet'):
                        layers = material.ForLayerSet.MaterialLayers
                        if layers:
                            return layers[0].Material.Name
        return None

    def _get_element_type(self, element) -> Optional[str]:
        """Get element type name"""
        if hasattr(element, 'IsTypedBy'):
            for rel in element.IsTypedBy or []:
                return rel.RelatingType.Name
        return None

    def extract_quantities(self) -> pd.DataFrame:
        """Extract quantities for all elements"""
        elements = self.get_all_elements()

        # Group by category and level
        quantities = elements.groupby(['IFC_Type', 'Level']).agg({
            'GlobalId': 'count',
            'Volume': 'sum',
            'Area': 'sum',
            'Length': 'sum'
        }).rename(columns={'GlobalId': 'Count'}).reset_index()

        return quantities

    def extract_levels(self) -> pd.DataFrame:
        """Extract building levels/storeys"""
        storeys = self.model.by_type("IfcBuildingStorey")

        level_data = []
        for storey in storeys:
            level_data.append({
                'GlobalId': storey.GlobalId,
                'Name': storey.Name,
                'Elevation': storey.Elevation,
                'Description': storey.Description
            })

        return pd.DataFrame(level_data).sort_values('Elevation')

    def extract_spaces(self) -> pd.DataFrame:
        """Extract spaces/rooms"""
        spaces = self.model.by_type("IfcSpace")

        space_data = []
        for space in spaces:
            psets = element_util.get_psets(space)
            base_qty = psets.get('BaseQuantities', {})

            space_data.append({
                'GlobalId': space.GlobalId,
                'Name': space.Name,
                'LongName': space.LongName,
                'Level': self._get_element_level(space),
                'Area': base_qty.get('NetFloorArea'),
                'Volume': base_qty.get('NetVolume'),
                'Height': base_qty.get('Height')
            })

        return pd.DataFrame(space_data)

    def extract_materials(self) -> pd.DataFrame:
        """Extract material summary"""
        materials = {}

        for elem in self.model.by_type("IfcProduct"):
            material = self._get_element_material(elem)
            if material:
                if material not in materials:
                    materials[material] = {'count': 0, 'volume': 0}

                materials[material]['count'] += 1

                psets = element_util.get_psets(elem)
                volume = psets.get('BaseQuantities', {}).get('NetVolume', 0)
                if volume:
                    materials[material]['volume'] += volume

        return pd.DataFrame.from_dict(materials, orient='index').reset_index()

    def extract_relationships(self) -> pd.DataFrame:
        """Extract element relationships"""
        relationships = []

        # Spatial containment
        for rel in self.model.by_type("IfcRelContainedInSpatialStructure"):
            for elem in rel.RelatedElements:
                relationships.append({
                    'Element': elem.GlobalId,
                    'Element_Type': elem.is_a(),
                    'Relationship': 'ContainedIn',
                    'Related_To': rel.RelatingStructure.GlobalId,
                    'Related_Type': rel.RelatingStructure.is_a()
                })

        # Aggregation
        for rel in self.model.by_type("IfcRelAggregates"):
            for part in rel.RelatedObjects:
                relationships.append({
                    'Element': part.GlobalId,
                    'Element_Type': part.is_a(),
                    'Relationship': 'PartOf',
                    'Related_To': rel.RelatingObject.GlobalId,
                    'Related_Type': rel.RelatingObject.is_a()
                })

        return pd.DataFrame(relationships)
```

### Geometry Extraction

#### Extract Geometry Data

```python
import numpy as np

class IFCGeometryExtractor:
    """Extract geometry data from IFC elements"""

    def __init__(self, ifc_path: str):
        self.model = ifcopenshell.open(ifc_path)
        self.settings = ifcopenshell.geom.settings()
        self.settings.set(self.settings.USE_WORLD_COORDS, True)

    def get_element_geometry(self, element) -> Dict:
        """Extract geometry for single element"""
        try:
            shape = ifcopenshell.geom.create_shape(self.settings, element)

            verts = shape.geometry.verts
            faces = shape.geometry.faces

            # Calculate bounding box
            vertices = np.array(verts).reshape(-1, 3)
            min_coords = vertices.min(axis=0)
            max_coords = vertices.max(axis=0)
            dimensions = max_coords - min_coords

            return {
                'GlobalId': element.GlobalId,
                'vertices_count': len(vertices),
                'faces_count': len(faces) // 3,
                'min_x': min_coords[0],
                'min_y': min_coords[1],
                'min_z': min_coords[2],
                'max_x': max_coords[0],
                'max_y': max_coords[1],
                'max_z': max_coords[2],
                'length': dimensions[0],
                'width': dimensions[1],
                'height': dimensions[2],
                'center_x': (min_coords[0] + max_coords[0]) / 2,
                'center_y': (min_coords[1] + max_coords[1]) / 2,
                'center_z': (min_coords[2] + max_coords[2]) / 2
            }
        except:
            return {'GlobalId': element.GlobalId, 'error': 'Geometry extraction failed'}

    def get_bounding_boxes(self, element_type: str) -> pd.DataFrame:
        """Get bounding boxes for all elements of type"""
        elements = self.model.by_type(element_type)
        boxes = [self.get_element_geometry(e) for e in elements]
        return pd.DataFrame(boxes)

    def calculate_volumes(self, element_type: str) -> pd.DataFrame:
        """Calculate volumes using geometry"""
        elements = self.model.by_type(element_type)
        volumes = []

        for elem in elements:
            try:
                shape = ifcopenshell.geom.create_shape(self.settings, elem)
                # Calculate volume from mesh (simplified)
                verts = np.array(shape.geometry.verts).reshape(-1, 3)
                bbox_volume = np.prod(verts.max(axis=0) - verts.min(axis=0))

                volumes.append({
                    'GlobalId': elem.GlobalId,
                    'Name': elem.Name,
                    'BBox_Volume': bbox_volume
                })
            except:
                pass

        return pd.DataFrame(volumes)
```

### Export Functions

#### Export to Various Formats

```python
class IFCExporter:
    """Export IFC data to various formats"""

    def __init__(self, extractor: IFCExtractor):
        self.extractor = extractor

    def to_excel(self, output_path: str, include_all: bool = True):
        """Export to Excel with multiple sheets"""
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Project info
            project_info = pd.DataFrame([self.extractor.get_project_info()])
            project_info.to_excel(writer, sheet_name='Project', index=False)

            # All elements
            if include_all:
                elements = self.extractor.get_all_elements()
                elements.to_excel(writer, sheet_name='Elements', index=False)

            # Quantities
            quantities = self.extractor.extract_quantities()
            quantities.to_excel(writer, sheet_name='Quantities', index=False)

            # Levels
            levels = self.extractor.extract_levels()
            levels.to_excel(writer, sheet_name='Levels', index=False)

            # Spaces
            spaces = self.extractor.extract_spaces()
            spaces.to_excel(writer, sheet_name='Spaces', index=False)

            # Materials
            materials = self.extractor.extract_materials()
            materials.to_excel(writer, sheet_name='Materials', index=False)

        return output_path

    def to_csv(self, output_dir: str):
        """Export to multiple CSV files"""
        import os
        os.makedirs(output_dir, exist_ok=True)

        exports = {
            'elements.csv': self.extractor.get_all_elements(),
            'quantities.csv': self.extractor.extract_quantities(),
            'levels.csv': self.extractor.extract_levels(),
            'spaces.csv': self.extractor.extract_spaces(),
            'materials.csv': self.extractor.extract_materials()
        }

        for filename, df in exports.items():
            df.to_csv(os.path.join(output_dir, filename), index=False)

        return output_dir

    def to_json(self, output_path: str):
        """Export to JSON"""
        import json

        data = {
            'project': self.extractor.get_project_info(),
            'elements': self.extractor.get_all_elements().to_dict('records'),
            'quantities': self.extractor.extract_quantities().to_dict('records'),
            'levels': self.extractor.extract_levels().to_dict('records'),
            'materials': self.extractor.extract_materials().to_dict('records')
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)

        return output_path

    def to_database(self, connection_string: str, table_prefix: str = 'ifc_'):
        """Export to SQL database"""
        from sqlalchemy import create_engine

        engine = create_engine(connection_string)

        tables = {
            f'{table_prefix}elements': self.extractor.get_all_elements(),
            f'{table_prefix}quantities': self.extractor.extract_quantities(),
            f'{table_prefix}levels': self.extractor.extract_levels(),
            f'{table_prefix}spaces': self.extractor.extract_spaces(),
            f'{table_prefix}materials': self.extractor.extract_materials()
        }

        for table_name, df in tables.items():
            # Remove complex columns for database storage
            simple_df = df.select_dtypes(exclude=['object']).copy()
            for col in df.columns:
                if df[col].dtype == 'object':
                    simple_df[col] = df[col].astype(str)

            simple_df.to_sql(table_name, engine, if_exists='replace', index=False)

        return list(tables.keys())
```

### Quick Reference

| Element Type | Common Properties | Quantities |
|-------------|-------------------|------------|
| IfcWall | IsExternal, FireRating | Length, Height, Area, Volume |
| IfcSlab | IsExternal, LoadBearing | Area, Volume, Perimeter |
| IfcColumn | LoadBearing | Height, CrossSectionArea |
| IfcBeam | LoadBearing | Length, CrossSectionArea |
| IfcDoor | FireRating, AcousticRating | Width, Height |
| IfcWindow | ThermalTransmittance | Width, Height, Area |

### Property Set Lookup

```python
## Common IFC Property Sets
PSETS = {
    'Pset_WallCommon': ['IsExternal', 'LoadBearing', 'FireRating'],
    'Pset_SlabCommon': ['IsExternal', 'LoadBearing', 'AcousticRating'],
    'Pset_ColumnCommon': ['IsExternal', 'LoadBearing'],
    'Pset_BeamCommon': ['LoadBearing', 'FireRating'],
    'Pset_DoorCommon': ['FireRating', 'AcousticRating', 'SecurityRating'],
    'Pset_WindowCommon': ['ThermalTransmittance', 'GlazingType'],
    'BaseQuantities': ['Length', 'Width', 'Height', 'Area', 'Volume']
}
```

### Resources

- **IfcOpenShell**: https://ifcopenshell.org
- **IFC Standard**: https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
- **DDC Website**: https://datadrivenconstruction.io

### Next Steps

- See `bim-validation-pipeline` for validating extracted data
- See `qto-report` for quantity take-off reports
- See `4d-simulation` for linking to schedules


---

# Quantities


## ifc-qto-extraction

> Extract quantities from IFC/Revit models for quantity takeoff. Uses DDC converters to get element counts, areas, volumes, lengths with grouping and reporting.

## IFC Quantity Takeoff Extraction

Extract structured quantity data from BIM models (IFC, Revit) for cost estimation, material ordering, and progress tracking.

### Business Case

**Problem**: Manual quantity takeoff is:
- Time-consuming (40-80 hours for medium project)
- Error-prone (human counting mistakes)
- Not repeatable (changes require full rework)
- Disconnected from design (no live updates)

**Solution**: Automated QTO from BIM that:
- Extracts all quantities in minutes
- Groups by type, level, zone
- Updates instantly with model changes
- Exports to Excel for pricing

**ROI**: 90% reduction in QTO time, near-zero counting errors

### DDC Tools Used

```
┌──────────────────────────────────────────────────────────────────────┐
│                      QTO EXTRACTION PIPELINE                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   INPUT                 CONVERT                 ANALYZE               │
│   ┌─────────┐          ┌─────────┐            ┌─────────┐            │
│   │ .rvt    │          │ DDC     │            │ Python  │            │
│   │ .ifc    │─────────►│Converter│───────────►│ pandas  │            │
│   │ .dwg    │          │         │            │         │            │
│   └─────────┘          └─────────┘            └─────────┘            │
│                              │                      │                 │
│                              ▼                      ▼                 │
│                        ┌─────────┐            ┌─────────┐            │
│                        │ .xlsx   │            │ Grouped │            │
│                        │ raw data│            │ QTO     │            │
│                        └─────────┘            └─────────┘            │
│                                                    │                  │
│   OUTPUT                                           ▼                  │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  QTO Report                                                  │   │
│   │  • Element counts by type                                    │   │
│   │  • Areas (m², ft²)                                           │   │
│   │  • Volumes (m³, ft³)                                         │   │
│   │  • Lengths (m, ft)                                           │   │
│   │  • Weights (kg, tons)                                        │   │
│   │  • Grouped by level/zone/system                              │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

### CLI Commands

#### Revit to Excel (with BBox for volumes)

```bash
## Basic extraction
RvtExporter.exe "C:\Models\Building.rvt"

## Full extraction with bounding boxes (for volume calculations)
RvtExporter.exe "C:\Models\Building.rvt" complete bbox

## Include schedules (Revit's built-in QTO)
RvtExporter.exe "C:\Models\Building.rvt" complete bbox schedule
```

#### IFC to Excel

```bash
## Extract IFC data
IfcExporter.exe "C:\Models\Building.ifc"

## Output: Building.xlsx with all IFC entities
```

#### DWG to Excel (2D areas)

```bash
## Extract DWG blocks and areas
DwgExporter.exe "C:\Drawings\FloorPlan.dwg"
```

### Python Implementation

```python
import pandas as pd
import numpy as np
from pathlib import Path
import subprocess
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class QuantityItem:
    """Single quantity line item"""
    category: str
    type_name: str
    count: int
    area: float = 0.0
    volume: float = 0.0
    length: float = 0.0
    weight: float = 0.0
    unit_area: str = "m²"
    unit_volume: str = "m³"
    unit_length: str = "m"
    level: str = ""
    zone: str = ""


class BIMQuantityExtractor:
    """Extract quantities from BIM models using DDC converters"""

    def __init__(self, converter_path: str):
        self.converter_path = Path(converter_path)

    def convert_model(self, model_path: str, options: List[str] = None) -> Path:
        """Convert BIM model to Excel"""

        model = Path(model_path)
        options = options or ["complete", "bbox"]

        # Determine converter
        ext = model.suffix.lower()
        converters = {
            '.rvt': 'RvtExporter.exe',
            '.rfa': 'RvtExporter.exe',
            '.ifc': 'IfcExporter.exe',
            '.dwg': 'DwgExporter.exe',
            '.dgn': 'DgnExporter.exe'
        }

        converter = self.converter_path / converters.get(ext, 'RvtExporter.exe')

        # Build command
        cmd = [str(converter), str(model)] + options

        # Execute
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Conversion failed: {result.stderr}")

        # Return path to generated Excel
        xlsx_path = model.with_suffix('.xlsx')
        return xlsx_path

    def load_bim_data(self, xlsx_path: str) -> pd.DataFrame:
        """Load converted BIM data from Excel"""

        xlsx = Path(xlsx_path)
        if not xlsx.exists():
            raise FileNotFoundError(f"Excel file not found: {xlsx}")

        # Read main data sheet
        df = pd.read_excel(xlsx, sheet_name=0)

        # Clean column names
        df.columns = df.columns.str.strip()

        return df

    def extract_quantities(
        self,
        df: pd.DataFrame,
        group_by: str = "Type Name",
        include_categories: List[str] = None
    ) -> List[QuantityItem]:
        """Extract quantities grouped by type"""

        # Filter categories if specified
        if include_categories and 'Category' in df.columns:
            df = df[df['Category'].isin(include_categories)]

        # Group and aggregate
        quantities = []

        for (category, type_name), group in df.groupby(['Category', group_by]):
            item = QuantityItem(
                category=str(category),
                type_name=str(type_name),
                count=len(group)
            )

            # Extract area
            area_cols = ['Area', 'Surface Area', 'Gross Area', 'Net Area']
            for col in area_cols:
                if col in group.columns:
                    item.area = group[col].sum()
                    break

            # Extract volume
            vol_cols = ['Volume', 'Gross Volume', 'Net Volume']
            for col in vol_cols:
                if col in group.columns:
                    item.volume = group[col].sum()
                    break

            # Extract length
            len_cols = ['Length', 'Curve Length', 'Unconnected Height']
            for col in len_cols:
                if col in group.columns:
                    item.length = group[col].sum()
                    break

            # Extract level if available
            if 'Level' in group.columns:
                levels = group['Level'].dropna().unique()
                item.level = ', '.join(str(l) for l in levels)

            quantities.append(item)

        return quantities

    def extract_by_level(
        self,
        df: pd.DataFrame,
        group_by: str = "Type Name"
    ) -> Dict[str, List[QuantityItem]]:
        """Extract quantities grouped by level"""

        result = {}

        if 'Level' not in df.columns:
            result['All Levels'] = self.extract_quantities(df, group_by)
            return result

        for level, level_df in df.groupby('Level'):
            level_name = str(level) if pd.notna(level) else 'Unassigned'
            result[level_name] = self.extract_quantities(level_df, group_by)

        return result

    def calculate_concrete_quantities(self, df: pd.DataFrame) -> dict:
        """Calculate concrete quantities for typical elements"""

        concrete_categories = [
            'Floors', 'Structural Floors',
            'Walls', 'Structural Walls',
            'Structural Foundations', 'Foundation',
            'Structural Columns', 'Columns',
            'Structural Framing', 'Beams'
        ]

        concrete_df = df[df['Category'].isin(concrete_categories)]

        return {
            'total_volume_m3': concrete_df['Volume'].sum() if 'Volume' in concrete_df.columns else 0,
            'by_category': concrete_df.groupby('Category')['Volume'].sum().to_dict() if 'Volume' in concrete_df.columns else {},
            'element_count': len(concrete_df)
        }

    def calculate_wall_quantities(self, df: pd.DataFrame) -> dict:
        """Calculate wall quantities"""

        wall_categories = ['Walls', 'Basic Wall', 'Curtain Wall']
        walls = df[df['Category'].isin(wall_categories)]

        result = {
            'total_area_m2': 0,
            'total_length_m': 0,
            'by_type': {}
        }

        if 'Area' in walls.columns:
            result['total_area_m2'] = walls['Area'].sum()

        if 'Length' in walls.columns:
            result['total_length_m'] = walls['Length'].sum()

        if 'Type Name' in walls.columns:
            for type_name, group in walls.groupby('Type Name'):
                result['by_type'][type_name] = {
                    'count': len(group),
                    'area': group['Area'].sum() if 'Area' in group.columns else 0,
                    'length': group['Length'].sum() if 'Length' in group.columns else 0
                }

        return result

    def generate_qto_report(
        self,
        quantities: List[QuantityItem],
        output_path: str,
        project_name: str = "Project"
    ) -> str:
        """Generate QTO Excel report"""

        # Convert to DataFrame
        records = []
        for q in quantities:
            records.append({
                'Category': q.category,
                'Type': q.type_name,
                'Count': q.count,
                'Area (m²)': round(q.area, 2),
                'Volume (m³)': round(q.volume, 3),
                'Length (m)': round(q.length, 2),
                'Level': q.level
            })

        df = pd.DataFrame(records)

        # Sort by category and type
        df = df.sort_values(['Category', 'Type'])

        # Write to Excel with formatting
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Summary sheet
            summary = df.groupby('Category').agg({
                'Count': 'sum',
                'Area (m²)': 'sum',
                'Volume (m³)': 'sum',
                'Length (m)': 'sum'
            }).round(2)
            summary.to_excel(writer, sheet_name='Summary')

            # Detail sheet
            df.to_excel(writer, sheet_name='Detail', index=False)

            # By Level sheet
            if 'Level' in df.columns and df['Level'].notna().any():
                level_summary = df.groupby(['Level', 'Category']).agg({
                    'Count': 'sum',
                    'Area (m²)': 'sum',
                    'Volume (m³)': 'sum'
                }).round(2)
                level_summary.to_excel(writer, sheet_name='By Level')

        return output_path

    def generate_html_report(
        self,
        quantities: List[QuantityItem],
        output_path: str,
        project_name: str = "Project"
    ) -> str:
        """Generate interactive HTML QTO report"""

        # Group by category
        by_category = {}
        for q in quantities:
            if q.category not in by_category:
                by_category[q.category] = []
            by_category[q.category].append(q)

        # Calculate totals
        total_count = sum(q.count for q in quantities)
        total_area = sum(q.area for q in quantities)
        total_volume = sum(q.volume for q in quantities)

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>QTO Report - {project_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; margin-bottom: 20px; }}
        .summary {{ display: flex; gap: 20px; margin-bottom: 20px; }}
        .summary-card {{ background: #ecf0f1; padding: 15px; border-radius: 5px; flex: 1; }}
        .summary-card h3 {{ margin: 0 0 10px 0; color: #7f8c8d; font-size: 14px; }}
        .summary-card .value {{ font-size: 24px; font-weight: bold; color: #2c3e50; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th {{ background: #34495e; color: white; padding: 10px; text-align: left; }}
        td {{ padding: 8px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background: #f5f5f5; }}
        .category-header {{ background: #3498db; color: white; font-weight: bold; }}
        .number {{ text-align: right; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Quantity Takeoff Report</h1>
        <p>Project: {project_name}</p>
    </div>

    <div class="summary">
        <div class="summary-card">
            <h3>Total Elements</h3>
            <div class="value">{total_count:,}</div>
        </div>
        <div class="summary-card">
            <h3>Total Area</h3>
            <div class="value">{total_area:,.2f} m²</div>
        </div>
        <div class="summary-card">
            <h3>Total Volume</h3>
            <div class="value">{total_volume:,.3f} m³</div>
        </div>
        <div class="summary-card">
            <h3>Categories</h3>
            <div class="value">{len(by_category)}</div>
        </div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Category / Type</th>
                <th class="number">Count</th>
                <th class="number">Area (m²)</th>
                <th class="number">Volume (m³)</th>
                <th class="number">Length (m)</th>
            </tr>
        </thead>
        <tbody>
"""

        for category, items in sorted(by_category.items()):
            cat_count = sum(i.count for i in items)
            cat_area = sum(i.area for i in items)
            cat_volume = sum(i.volume for i in items)

            html += f"""
            <tr class="category-header">
                <td>{category}</td>
                <td class="number">{cat_count:,}</td>
                <td class="number">{cat_area:,.2f}</td>
                <td class="number">{cat_volume:,.3f}</td>
                <td class="number">-</td>
            </tr>
"""
            for item in sorted(items, key=lambda x: x.type_name):
                html += f"""
            <tr>
                <td>&nbsp;&nbsp;&nbsp;{item.type_name}</td>
                <td class="number">{item.count:,}</td>
                <td class="number">{item.area:,.2f}</td>
                <td class="number">{item.volume:,.3f}</td>
                <td class="number">{item.length:,.2f}</td>
            </tr>
"""

        html += """
        </tbody>
    </table>
</body>
</html>
"""

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        return output_path


## Usage Example
def extract_qto_from_model(
    model_path: str,
    converter_path: str,
    output_dir: str = None
) -> dict:
    """Complete QTO extraction workflow"""

    from datetime import datetime

    extractor = BIMQuantityExtractor(converter_path)

    # Convert model
    print(f"Converting: {model_path}")
    xlsx_path = extractor.convert_model(model_path, ["complete", "bbox"])

    # Load data
    print(f"Loading data from: {xlsx_path}")
    df = extractor.load_bim_data(xlsx_path)

    # Extract quantities
    quantities = extractor.extract_quantities(df)

    # Generate reports
    output_dir = output_dir or Path(model_path).parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    excel_path = Path(output_dir) / f"QTO_{timestamp}.xlsx"
    html_path = Path(output_dir) / f"QTO_{timestamp}.html"

    extractor.generate_qto_report(quantities, str(excel_path))
    extractor.generate_html_report(quantities, str(html_path))

    # Calculate specific quantities
    concrete = extractor.calculate_concrete_quantities(df)
    walls = extractor.calculate_wall_quantities(df)

    return {
        'excel_report': str(excel_path),
        'html_report': str(html_path),
        'summary': {
            'total_elements': len(df),
            'categories': df['Category'].nunique() if 'Category' in df.columns else 0,
            'types': df['Type Name'].nunique() if 'Type Name' in df.columns else 0
        },
        'concrete': concrete,
        'walls': walls
    }


if __name__ == "__main__":
    result = extract_qto_from_model(
        model_path=r"C:\Projects\Building.rvt",
        converter_path=r"C:\DDC\Converters",
        output_dir=r"C:\Projects\QTO"
    )

    print(f"Excel: {result['excel_report']}")
    print(f"HTML: {result['html_report']}")
    print(f"Concrete Volume: {result['concrete']['total_volume_m3']:.2f} m³")
```

### n8n Workflow Integration

```yaml
name: BIM QTO Extraction
trigger:
  type: webhook
  path: /qto-extract

steps:
  - convert_model:
      node: Execute Command
      command: |
        "C:\DDC\RvtExporter.exe" "{{$json.model_path}}" complete bbox schedule

  - load_excel:
      node: Spreadsheet File
      operation: read
      file: "={{$json.model_path.replace('.rvt', '.xlsx')}}"

  - group_quantities:
      node: Code
      code: |
        const grouped = {};
        items.forEach(item => {
          const type = item.json['Type Name'];
          if (!grouped[type]) {
            grouped[type] = {
              count: 0,
              area: 0,
              volume: 0
            };
          }
          grouped[type].count++;
          grouped[type].area += parseFloat(item.json['Area'] || 0);
          grouped[type].volume += parseFloat(item.json['Volume'] || 0);
        });
        return Object.entries(grouped).map(([type, data]) => ({
          type,
          ...data
        }));

  - generate_report:
      node: Code
      code: |
        // Generate HTML report
        return generateHTMLReport(items);

  - save_report:
      node: Write Binary File
      path: "={{$json.output_path}}"
```

### Best Practices

1. **Model Quality**: Ensure BIM model has proper levels and types assigned
2. **Units**: Verify model units match expected output units
3. **Categories**: Use consistent category naming for grouping
4. **Updates**: Re-run QTO after design changes
5. **Validation**: Cross-check totals against manual spot checks

### Common Quantity Formulas

```python
## Concrete formwork area (approximate)
formwork_area = concrete_volume * 6  # m² per m³ of concrete

## Rebar quantity (approximate)
rebar_weight = concrete_volume * 100  # kg per m³ (typical)

## Paint area from wall area
paint_area = wall_area * 2  # both sides

## Ceiling area from floor area
ceiling_area = floor_area * 0.95  # typical ratio
```

---

*"Measure twice, cut once. Or better yet, measure automatically from the model."*


## bim-qto

> Extract quantities from BIM/CAD data for cost estimation. Group by type, level, zone. Generate QTO reports.

## BIM Quantity Takeoff

### Overview
Quantity Takeoff (QTO) extracts measurable quantities from BIM models. This skill processes BIM exports to generate grouped quantity reports for cost estimation.

### Python Implementation

```python
import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class QTOUnit(Enum):
    """Quantity takeoff measurement units."""
    COUNT = "ea"
    LENGTH = "m"
    AREA = "m2"
    VOLUME = "m3"
    WEIGHT = "kg"
    LINEAR_FOOT = "lf"
    SQUARE_FOOT = "sf"
    CUBIC_YARD = "cy"


@dataclass
class QTOItem:
    """Single QTO line item."""
    category: str
    type_name: str
    description: str
    quantity: float
    unit: str
    level: Optional[str] = None
    material: Optional[str] = None
    element_count: int = 0


@dataclass
class QTOReport:
    """Complete QTO report."""
    project_name: str
    items: List[QTOItem]
    total_elements: int
    categories: int
    generated_date: str


class BIMQuantityTakeoff:
    """Extract quantities from BIM data."""

    # Column mappings for different BIM exports
    COLUMN_MAPPINGS = {
        'type': ['Type Name', 'TypeName', 'type_name', 'Family and Type', 'IfcType'],
        'category': ['Category', 'category', 'IfcClass', 'Element Category'],
        'level': ['Level', 'level', 'Building Storey', 'BuildingStorey', 'Floor'],
        'volume': ['Volume', 'volume', 'Volume (m³)', 'Qty_Volume'],
        'area': ['Area', 'area', 'Surface Area', 'Area (m²)', 'Qty_Area'],
        'length': ['Length', 'length', 'Length (m)', 'Qty_Length'],
        'count': ['Count', 'count', 'Quantity', 'ElementCount'],
        'material': ['Material', 'material', 'Structural Material', 'MaterialName']
    }

    def __init__(self, df: pd.DataFrame):
        """Initialize with BIM data DataFrame."""
        self.df = df
        self.column_map = self._detect_columns()

    def _detect_columns(self) -> Dict[str, str]:
        """Detect which columns exist in data."""
        mapping = {}

        for standard, variants in self.COLUMN_MAPPINGS.items():
            for variant in variants:
                if variant in self.df.columns:
                    mapping[standard] = variant
                    break

        return mapping

    def get_column(self, standard_name: str) -> Optional[str]:
        """Get actual column name from standard name."""
        return self.column_map.get(standard_name)

    def group_by_type(self, sum_column: str = 'volume') -> pd.DataFrame:
        """Group quantities by type name."""

        type_col = self.get_column('type')
        qty_col = self.get_column(sum_column)

        if type_col is None:
            raise ValueError("Type column not found")

        if qty_col is None:
            # Fall back to count
            result = self.df.groupby(type_col).size().reset_index(name='count')
        else:
            result = self.df.groupby(type_col).agg({
                qty_col: 'sum'
            }).reset_index()
            result['count'] = self.df.groupby(type_col).size().values

        result.columns = ['Type', 'Quantity', 'Count'] if len(result.columns) == 3 else ['Type', 'Count']
        return result.sort_values('Count', ascending=False)

    def group_by_category(self, sum_column: str = 'volume') -> pd.DataFrame:
        """Group quantities by category."""

        cat_col = self.get_column('category')
        qty_col = self.get_column(sum_column)

        if cat_col is None:
            raise ValueError("Category column not found")

        agg_dict = {}
        if qty_col:
            agg_dict[qty_col] = 'sum'

        if agg_dict:
            result = self.df.groupby(cat_col).agg(agg_dict).reset_index()
            result['count'] = self.df.groupby(cat_col).size().values
        else:
            result = self.df.groupby(cat_col).size().reset_index(name='count')

        return result.sort_values('count', ascending=False)

    def group_by_level(self, sum_column: str = 'volume') -> pd.DataFrame:
        """Group quantities by building level."""

        level_col = self.get_column('level')
        qty_col = self.get_column(sum_column)

        if level_col is None:
            raise ValueError("Level column not found")

        agg_dict = {}
        if qty_col:
            agg_dict[qty_col] = 'sum'

        if agg_dict:
            result = self.df.groupby(level_col).agg(agg_dict).reset_index()
            result['count'] = self.df.groupby(level_col).size().values
        else:
            result = self.df.groupby(level_col).size().reset_index(name='count')

        return result

    def pivot_by_level_and_type(self) -> pd.DataFrame:
        """Create pivot table: levels as rows, types as columns."""

        level_col = self.get_column('level')
        type_col = self.get_column('type')

        if level_col is None or type_col is None:
            raise ValueError("Level or Type column not found")

        pivot = pd.crosstab(
            self.df[level_col],
            self.df[type_col],
            margins=True
        )

        return pivot

    def filter_by_category(self, categories: List[str]) -> 'BIMQuantityTakeoff':
        """Filter to specific categories."""

        cat_col = self.get_column('category')
        if cat_col is None:
            raise ValueError("Category column not found")

        filtered_df = self.df[self.df[cat_col].isin(categories)]
        return BIMQuantityTakeoff(filtered_df)

    def filter_by_level(self, levels: List[str]) -> 'BIMQuantityTakeoff':
        """Filter to specific levels."""

        level_col = self.get_column('level')
        if level_col is None:
            raise ValueError("Level column not found")

        filtered_df = self.df[self.df[level_col].isin(levels)]
        return BIMQuantityTakeoff(filtered_df)

    def get_walls(self) -> pd.DataFrame:
        """Get wall quantities."""
        cat_col = self.get_column('category')
        if cat_col:
            walls = self.df[self.df[cat_col].str.contains('Wall', case=False, na=False)]
            return BIMQuantityTakeoff(walls).group_by_type()
        return pd.DataFrame()

    def get_floors(self) -> pd.DataFrame:
        """Get floor/slab quantities."""
        cat_col = self.get_column('category')
        if cat_col:
            floors = self.df[self.df[cat_col].str.contains('Floor|Slab', case=False, na=False)]
            return BIMQuantityTakeoff(floors).group_by_type()
        return pd.DataFrame()

    def get_doors(self) -> pd.DataFrame:
        """Get door quantities."""
        cat_col = self.get_column('category')
        if cat_col:
            doors = self.df[self.df[cat_col].str.contains('Door', case=False, na=False)]
            return BIMQuantityTakeoff(doors).group_by_type()
        return pd.DataFrame()

    def get_windows(self) -> pd.DataFrame:
        """Get window quantities."""
        cat_col = self.get_column('category')
        if cat_col:
            windows = self.df[self.df[cat_col].str.contains('Window', case=False, na=False)]
            return BIMQuantityTakeoff(windows).group_by_type()
        return pd.DataFrame()

    def generate_report(self, project_name: str = "Project") -> QTOReport:
        """Generate complete QTO report."""

        from datetime import datetime

        items = []
        type_col = self.get_column('type')
        cat_col = self.get_column('category')
        level_col = self.get_column('level')
        vol_col = self.get_column('volume')
        area_col = self.get_column('area')
        mat_col = self.get_column('material')

        # Group by type
        grouped = self.df.groupby(type_col if type_col else self.df.columns[0])

        for type_name, group in grouped:
            # Determine primary quantity
            qty = 0
            unit = QTOUnit.COUNT.value

            if vol_col and vol_col in group.columns:
                qty = group[vol_col].sum()
                unit = QTOUnit.VOLUME.value
            elif area_col and area_col in group.columns:
                qty = group[area_col].sum()
                unit = QTOUnit.AREA.value
            else:
                qty = len(group)
                unit = QTOUnit.COUNT.value

            # Get category and material
            category = group[cat_col].iloc[0] if cat_col and cat_col in group.columns else ""
            material = group[mat_col].iloc[0] if mat_col and mat_col in group.columns else ""
            level = group[level_col].iloc[0] if level_col and level_col in group.columns else ""

            items.append(QTOItem(
                category=str(category),
                type_name=str(type_name),
                description=str(type_name),
                quantity=round(qty, 2),
                unit=unit,
                level=str(level) if level else None,
                material=str(material) if material else None,
                element_count=len(group)
            ))

        return QTOReport(
            project_name=project_name,
            items=items,
            total_elements=len(self.df),
            categories=self.df[cat_col].nunique() if cat_col else 0,
            generated_date=datetime.now().isoformat()
        )

    def to_excel(self, output_path: str, project_name: str = "Project"):
        """Export QTO to Excel with multiple sheets."""

        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Summary by category
            self.group_by_category().to_excel(
                writer, sheet_name='By Category', index=False)

            # Summary by type
            self.group_by_type().to_excel(
                writer, sheet_name='By Type', index=False)

            # Level breakdown
            try:
                self.pivot_by_level_and_type().to_excel(
                    writer, sheet_name='Level-Type Matrix')
            except:
                pass

            # Walls
            walls = self.get_walls()
            if not walls.empty:
                walls.to_excel(writer, sheet_name='Walls', index=False)

            # Doors and Windows
            doors = self.get_doors()
            if not doors.empty:
                doors.to_excel(writer, sheet_name='Doors', index=False)

            windows = self.get_windows()
            if not windows.empty:
                windows.to_excel(writer, sheet_name='Windows', index=False)

        return output_path
```

### Quick Start

```python
## Load BIM export
df = pd.read_excel("revit_export.xlsx")

## Initialize QTO
qto = BIMQuantityTakeoff(df)

## Get quantities by type
by_type = qto.group_by_type()
print(by_type.head(10))

## Get wall schedule
walls = qto.get_walls()
print(walls)
```

### Common Use Cases

#### 1. Full QTO Report
```python
qto = BIMQuantityTakeoff(df)
report = qto.generate_report("Office Building")
print(f"Elements: {report.total_elements}")
for item in report.items[:5]:
    print(f"{item.type_name}: {item.quantity} {item.unit}")
```

#### 2. Level-by-Level Analysis
```python
pivot = qto.pivot_by_level_and_type()
print(pivot)
```

#### 3. Export to Excel
```python
qto.to_excel("qto_report.xlsx", "My Project")
```

### Resources
- **DDC Book**: Chapter 3.2 - Quantity Take-Off


---

# Clash detection


## bim-clash-detection

> Detect and analyze geometric clashes in BIM models. Identify MEP, structural, and architectural conflicts before construction.

## BIM Clash Detection

### Business Case

#### Problem Statement
Coordination issues cause significant rework:
- MEP vs structural conflicts discovered on site
- Late design changes increase costs
- Manual clash review is time-consuming
- No standardized clash categorization

#### Solution
Automated clash detection and analysis system that identifies conflicts between building systems and provides prioritized resolution recommendations.

#### Business Value
- **Cost savings** - Detect issues before construction
- **Time reduction** - Automated clash identification
- **Better coordination** - Systematic conflict resolution
- **Quality improvement** - Fewer field issues

### Technical Implementation

```python
import pandas as pd
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math


class ClashType(Enum):
    """Types of clashes."""
    HARD = "hard"           # Physical intersection
    SOFT = "soft"           # Clearance violation
    WORKFLOW = "workflow"   # Sequencing conflict
    DUPLICATE = "duplicate" # Duplicated elements


class ClashStatus(Enum):
    """Clash resolution status."""
    NEW = "new"
    ACTIVE = "active"
    RESOLVED = "resolved"
    APPROVED = "approved"
    IGNORED = "ignored"


class ClashSeverity(Enum):
    """Clash severity level."""
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    INFO = "info"


class Discipline(Enum):
    """BIM disciplines."""
    ARCHITECTURAL = "architectural"
    STRUCTURAL = "structural"
    MECHANICAL = "mechanical"
    ELECTRICAL = "electrical"
    PLUMBING = "plumbing"
    FIRE_PROTECTION = "fire_protection"
    CIVIL = "civil"


@dataclass
class BoundingBox:
    """3D bounding box."""
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float

    def intersects(self, other: 'BoundingBox') -> bool:
        """Check if boxes intersect."""
        return (self.min_x <= other.max_x and self.max_x >= other.min_x and
                self.min_y <= other.max_y and self.max_y >= other.min_y and
                self.min_z <= other.max_z and self.max_z >= other.min_z)

    def volume(self) -> float:
        """Calculate bounding box volume."""
        return ((self.max_x - self.min_x) *
                (self.max_y - self.min_y) *
                (self.max_z - self.min_z))

    def center(self) -> Tuple[float, float, float]:
        """Get center point."""
        return (
            (self.min_x + self.max_x) / 2,
            (self.min_y + self.max_y) / 2,
            (self.min_z + self.max_z) / 2
        )


@dataclass
class BIMElement:
    """BIM element representation."""
    element_id: str
    name: str
    discipline: Discipline
    category: str  # e.g., "Duct", "Beam", "Pipe"
    level: str
    bounding_box: BoundingBox
    properties: Dict[str, Any] = field(default_factory=dict)

    def distance_to(self, other: 'BIMElement') -> float:
        """Calculate distance between element centers."""
        c1 = self.bounding_box.center()
        c2 = other.bounding_box.center()
        return math.sqrt(
            (c2[0] - c1[0])**2 +
            (c2[1] - c1[1])**2 +
            (c2[2] - c1[2])**2
        )


@dataclass
class Clash:
    """Clash between two elements."""
    clash_id: str
    element_a: BIMElement
    element_b: BIMElement
    clash_type: ClashType
    severity: ClashSeverity
    status: ClashStatus
    distance: float  # Penetration depth (negative) or clearance gap
    location: Tuple[float, float, float]
    detected_at: datetime
    resolved_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            'clash_id': self.clash_id,
            'element_a_id': self.element_a.element_id,
            'element_a_name': self.element_a.name,
            'element_a_discipline': self.element_a.discipline.value,
            'element_b_id': self.element_b.element_id,
            'element_b_name': self.element_b.name,
            'element_b_discipline': self.element_b.discipline.value,
            'clash_type': self.clash_type.value,
            'severity': self.severity.value,
            'status': self.status.value,
            'distance': round(self.distance, 3),
            'location_x': self.location[0],
            'location_y': self.location[1],
            'location_z': self.location[2],
            'level': self.element_a.level,
            'detected_at': self.detected_at.isoformat(),
            'assigned_to': self.assigned_to,
            'notes': self.notes
        }


@dataclass
class ClashTest:
    """Clash test configuration."""
    name: str
    discipline_a: Discipline
    discipline_b: Discipline
    clash_type: ClashType
    tolerance: float = 0.0  # Clearance tolerance in meters
    enabled: bool = True


class BIMClashDetector:
    """Detect and manage BIM clashes."""

    def __init__(self):
        self.elements: List[BIMElement] = []
        self.clashes: List[Clash] = []
        self.clash_tests: List[ClashTest] = []
        self._clash_counter = 0

    def load_elements(self, elements_df: pd.DataFrame) -> int:
        """Load BIM elements from DataFrame."""
        loaded = 0
        for _, row in elements_df.iterrows():
            element = BIMElement(
                element_id=str(row.get('element_id', '')),
                name=str(row.get('name', '')),
                discipline=Discipline(row.get('discipline', 'architectural')),
                category=str(row.get('category', '')),
                level=str(row.get('level', '')),
                bounding_box=BoundingBox(
                    min_x=float(row.get('min_x', 0)),
                    min_y=float(row.get('min_y', 0)),
                    min_z=float(row.get('min_z', 0)),
                    max_x=float(row.get('max_x', 0)),
                    max_y=float(row.get('max_y', 0)),
                    max_z=float(row.get('max_z', 0))
                )
            )
            self.elements.append(element)
            loaded += 1
        return loaded

    def add_clash_test(self, test: ClashTest):
        """Add clash test configuration."""
        self.clash_tests.append(test)

    def setup_standard_tests(self):
        """Setup standard MEP coordination tests."""
        standard_tests = [
            ClashTest("MEP vs Structure", Discipline.MECHANICAL, Discipline.STRUCTURAL, ClashType.HARD),
            ClashTest("Electrical vs Structure", Discipline.ELECTRICAL, Discipline.STRUCTURAL, ClashType.HARD),
            ClashTest("Plumbing vs Structure", Discipline.PLUMBING, Discipline.STRUCTURAL, ClashType.HARD),
            ClashTest("MEP vs MEP", Discipline.MECHANICAL, Discipline.ELECTRICAL, ClashType.HARD),
            ClashTest("Duct Clearance", Discipline.MECHANICAL, Discipline.MECHANICAL, ClashType.SOFT, tolerance=0.05),
            ClashTest("Fire Protection", Discipline.FIRE_PROTECTION, Discipline.STRUCTURAL, ClashType.HARD),
        ]
        for test in standard_tests:
            self.add_clash_test(test)

    def run_clash_detection(self) -> List[Clash]:
        """Run all clash tests."""
        new_clashes = []

        for test in self.clash_tests:
            if not test.enabled:
                continue

            # Filter elements by discipline
            elements_a = [e for e in self.elements if e.discipline == test.discipline_a]
            elements_b = [e for e in self.elements if e.discipline == test.discipline_b]

            # Check all pairs
            for elem_a in elements_a:
                for elem_b in elements_b:
                    if elem_a.element_id == elem_b.element_id:
                        continue

                    clash = self._check_clash(elem_a, elem_b, test)
                    if clash:
                        new_clashes.append(clash)

        self.clashes.extend(new_clashes)
        return new_clashes

    def _check_clash(self, elem_a: BIMElement, elem_b: BIMElement,
                     test: ClashTest) -> Optional[Clash]:
        """Check if two elements clash."""

        # Expand bounding box by tolerance for soft clashes
        box_a = elem_a.bounding_box
        box_b = elem_b.bounding_box

        if test.clash_type == ClashType.SOFT:
            # Add clearance tolerance
            expanded_a = BoundingBox(
                box_a.min_x - test.tolerance, box_a.min_y - test.tolerance, box_a.min_z - test.tolerance,
                box_a.max_x + test.tolerance, box_a.max_y + test.tolerance, box_a.max_z + test.tolerance
            )
            intersects = expanded_a.intersects(box_b)
        else:
            intersects = box_a.intersects(box_b)

        if not intersects:
            return None

        # Calculate clash point and severity
        self._clash_counter += 1
        clash_id = f"CLH-{self._clash_counter:05d}"

        # Clash location (center of intersection)
        location = (
            (max(box_a.min_x, box_b.min_x) + min(box_a.max_x, box_b.max_x)) / 2,
            (max(box_a.min_y, box_b.min_y) + min(box_a.max_y, box_b.max_y)) / 2,
            (max(box_a.min_z, box_b.min_z) + min(box_a.max_z, box_b.max_z)) / 2
        )

        # Calculate penetration depth
        distance = elem_a.distance_to(elem_b)

        # Determine severity
        if test.clash_type == ClashType.HARD:
            severity = ClashSeverity.CRITICAL if distance < 0.1 else ClashSeverity.MAJOR
        else:
            severity = ClashSeverity.MINOR if distance > test.tolerance else ClashSeverity.MAJOR

        return Clash(
            clash_id=clash_id,
            element_a=elem_a,
            element_b=elem_b,
            clash_type=test.clash_type,
            severity=severity,
            status=ClashStatus.NEW,
            distance=distance,
            location=location,
            detected_at=datetime.now()
        )

    def get_summary(self) -> Dict[str, Any]:
        """Get clash detection summary."""
        by_severity = {}
        by_discipline = {}
        by_status = {}

        for clash in self.clashes:
            # By severity
            sev = clash.severity.value
            by_severity[sev] = by_severity.get(sev, 0) + 1

            # By discipline pair
            pair = f"{clash.element_a.discipline.value} vs {clash.element_b.discipline.value}"
            by_discipline[pair] = by_discipline.get(pair, 0) + 1

            # By status
            stat = clash.status.value
            by_status[stat] = by_status.get(stat, 0) + 1

        return {
            'total_clashes': len(self.clashes),
            'by_severity': by_severity,
            'by_discipline': by_discipline,
            'by_status': by_status,
            'elements_checked': len(self.elements),
            'tests_run': len([t for t in self.clash_tests if t.enabled])
        }

    def export_to_dataframe(self) -> pd.DataFrame:
        """Export clashes to DataFrame."""
        return pd.DataFrame([c.to_dict() for c in self.clashes])

    def resolve_clash(self, clash_id: str, resolution_note: str):
        """Mark clash as resolved."""
        for clash in self.clashes:
            if clash.clash_id == clash_id:
                clash.status = ClashStatus.RESOLVED
                clash.resolved_at = datetime.now()
                clash.notes = resolution_note
                break

    def assign_clash(self, clash_id: str, assignee: str):
        """Assign clash to team member."""
        for clash in self.clashes:
            if clash.clash_id == clash_id:
                clash.assigned_to = assignee
                clash.status = ClashStatus.ACTIVE
                break
```

### Quick Start

```python
## Initialize detector
detector = BIMClashDetector()

## Setup standard MEP tests
detector.setup_standard_tests()

## Load elements from DataFrame
elements_df = pd.read_excel("bim_elements.xlsx")
detector.load_elements(elements_df)

## Run detection
clashes = detector.run_clash_detection()
print(f"Found {len(clashes)} clashes")

## Get summary
summary = detector.get_summary()
print(f"Critical: {summary['by_severity'].get('critical', 0)}")
```

### Common Use Cases

#### 1. MEP Coordination
```python
## Focus on MEP vs Structure
mep_clashes = [c for c in detector.clashes
               if c.element_a.discipline in [Discipline.MECHANICAL, Discipline.ELECTRICAL]]
```

#### 2. Export for Review
```python
df = detector.export_to_dataframe()
df.to_excel("clash_report.xlsx", index=False)
```

#### 3. Assign to Teams
```python
for clash in detector.clashes:
    if clash.element_a.discipline == Discipline.MECHANICAL:
        detector.assign_clash(clash.clash_id, "MEP Team")
```

### Resources
- **DDC Book**: Chapter 2.4 - BIM Coordination
- **Reference**: ISO 19650 BIM Standards


## clash-detection-analysis

> Detect and analyze geometric clashes between BIM elements. Identify hard clashes, soft clashes, and workflow conflicts using spatial analysis and rule-based detection.

## Clash Detection Analysis

### Overview

This skill implements automated clash detection for BIM models. Identify conflicts between building elements before construction to prevent costly rework and delays.

**Types of Clashes:**
- **Hard Clash**: Physical intersection of elements
- **Soft Clash**: Clearance/tolerance violations
- **Workflow Clash**: Scheduling/sequencing conflicts

> "Обнаружение коллизий на этапе проектирования может сократить затраты на исправление ошибок до 10 раз по сравнению с исправлением на стройплощадке."

### Quick Start

```python
import ifcopenshell
import ifcopenshell.geom
import numpy as np
from itertools import combinations

## Open model
ifc = ifcopenshell.open("model.ifc")

## Get structural and MEP elements
structural = ifc.by_type("IfcColumn") + ifc.by_type("IfcBeam")
mep = ifc.by_type("IfcPipeSegment") + ifc.by_type("IfcDuctSegment")

## Simple bounding box clash check
settings = ifcopenshell.geom.settings()

def get_bbox(element):
    try:
        shape = ifcopenshell.geom.create_shape(settings, element)
        verts = np.array(shape.geometry.verts).reshape(-1, 3)
        return verts.min(axis=0), verts.max(axis=0)
    except:
        return None, None

def check_bbox_clash(bbox1, bbox2):
    min1, max1 = bbox1
    min2, max2 = bbox2
    if min1 is None or min2 is None:
        return False
    return np.all(max1 >= min2) and np.all(max2 >= min1)

## Find clashes
clashes = []
for s_elem in structural:
    for m_elem in mep:
        bbox1 = get_bbox(s_elem)
        bbox2 = get_bbox(m_elem)
        if check_bbox_clash(bbox1, bbox2):
            clashes.append({
                'element1': s_elem.GlobalId,
                'element2': m_elem.GlobalId,
                'type': 'Structure-MEP'
            })

print(f"Found {len(clashes)} potential clashes")
```

### Clash Detection Engine

#### Core Detector Class

```python
import ifcopenshell
import ifcopenshell.geom
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from itertools import combinations
from scipy.spatial import cKDTree

@dataclass
class Clash:
    element1_id: str
    element1_type: str
    element1_name: str
    element2_id: str
    element2_type: str
    element2_name: str
    clash_type: str
    distance: float
    location: Tuple[float, float, float]
    severity: str

class ClashDetector:
    """Detect clashes between BIM elements"""

    def __init__(self, ifc_path: str):
        self.model = ifcopenshell.open(ifc_path)
        self.settings = ifcopenshell.geom.settings()
        self.settings.set(self.settings.USE_WORLD_COORDS, True)

        self._geometry_cache = {}
        self.clashes: List[Clash] = []

    def _get_geometry(self, element):
        """Get or compute element geometry"""
        if element.GlobalId in self._geometry_cache:
            return self._geometry_cache[element.GlobalId]

        try:
            shape = ifcopenshell.geom.create_shape(self.settings, element)
            verts = np.array(shape.geometry.verts).reshape(-1, 3)
            faces = np.array(shape.geometry.faces).reshape(-1, 3)

            geom = {
                'vertices': verts,
                'faces': faces,
                'min': verts.min(axis=0),
                'max': verts.max(axis=0),
                'center': verts.mean(axis=0)
            }
            self._geometry_cache[element.GlobalId] = geom
            return geom
        except:
            return None

    def detect_hard_clashes(self, group1_types: List[str],
                            group2_types: List[str]) -> List[Clash]:
        """Detect hard clashes (physical intersections) between two groups"""
        group1 = []
        for ifc_type in group1_types:
            group1.extend(self.model.by_type(ifc_type))

        group2 = []
        for ifc_type in group2_types:
            group2.extend(self.model.by_type(ifc_type))

        clashes = []

        for elem1 in group1:
            geom1 = self._get_geometry(elem1)
            if geom1 is None:
                continue

            for elem2 in group2:
                if elem1.GlobalId == elem2.GlobalId:
                    continue

                geom2 = self._get_geometry(elem2)
                if geom2 is None:
                    continue

                # Bounding box check (fast filter)
                if not self._bbox_intersect(geom1, geom2):
                    continue

                # Detailed check
                intersection = self._check_intersection(geom1, geom2)
                if intersection['intersects']:
                    clash = Clash(
                        element1_id=elem1.GlobalId,
                        element1_type=elem1.is_a(),
                        element1_name=elem1.Name or '',
                        element2_id=elem2.GlobalId,
                        element2_type=elem2.is_a(),
                        element2_name=elem2.Name or '',
                        clash_type='Hard',
                        distance=intersection['distance'],
                        location=tuple(intersection['point']),
                        severity=self._classify_severity(intersection['distance'])
                    )
                    clashes.append(clash)

        self.clashes.extend(clashes)
        return clashes

    def detect_soft_clashes(self, group1_types: List[str],
                            group2_types: List[str],
                            clearance: float = 0.1) -> List[Clash]:
        """Detect soft clashes (clearance violations)"""
        group1 = []
        for ifc_type in group1_types:
            group1.extend(self.model.by_type(ifc_type))

        group2 = []
        for ifc_type in group2_types:
            group2.extend(self.model.by_type(ifc_type))

        clashes = []

        for elem1 in group1:
            geom1 = self._get_geometry(elem1)
            if geom1 is None:
                continue

            for elem2 in group2:
                if elem1.GlobalId == elem2.GlobalId:
                    continue

                geom2 = self._get_geometry(elem2)
                if geom2 is None:
                    continue

                # Check if within clearance distance
                distance = self._min_distance(geom1, geom2)

                if distance < clearance and distance > 0:
                    clash = Clash(
                        element1_id=elem1.GlobalId,
                        element1_type=elem1.is_a(),
                        element1_name=elem1.Name or '',
                        element2_id=elem2.GlobalId,
                        element2_type=elem2.is_a(),
                        element2_name=elem2.Name or '',
                        clash_type='Soft',
                        distance=distance,
                        location=tuple((geom1['center'] + geom2['center']) / 2),
                        severity='Medium' if distance < clearance/2 else 'Low'
                    )
                    clashes.append(clash)

        self.clashes.extend(clashes)
        return clashes

    def _bbox_intersect(self, geom1: Dict, geom2: Dict) -> bool:
        """Check if bounding boxes intersect"""
        return (np.all(geom1['max'] >= geom2['min']) and
                np.all(geom2['max'] >= geom1['min']))

    def _check_intersection(self, geom1: Dict, geom2: Dict) -> Dict:
        """Check for actual geometry intersection"""
        # Simplified check using closest points
        tree1 = cKDTree(geom1['vertices'])
        distances, _ = tree1.query(geom2['vertices'], k=1)

        min_dist = distances.min()

        if min_dist < 0.001:  # Intersection threshold
            intersection_idx = np.argmin(distances)
            return {
                'intersects': True,
                'distance': min_dist,
                'point': geom2['vertices'][intersection_idx]
            }

        return {'intersects': False, 'distance': min_dist, 'point': None}

    def _min_distance(self, geom1: Dict, geom2: Dict) -> float:
        """Calculate minimum distance between geometries"""
        tree1 = cKDTree(geom1['vertices'])
        distances, _ = tree1.query(geom2['vertices'], k=1)
        return distances.min()

    def _classify_severity(self, distance: float) -> str:
        """Classify clash severity"""
        if distance < 0.01:
            return 'Critical'
        elif distance < 0.05:
            return 'High'
        elif distance < 0.1:
            return 'Medium'
        else:
            return 'Low'

    def get_clash_report(self) -> pd.DataFrame:
        """Generate clash report as DataFrame"""
        if not self.clashes:
            return pd.DataFrame()

        return pd.DataFrame([
            {
                'Element1_ID': c.element1_id,
                'Element1_Type': c.element1_type,
                'Element1_Name': c.element1_name,
                'Element2_ID': c.element2_id,
                'Element2_Type': c.element2_type,
                'Element2_Name': c.element2_name,
                'Clash_Type': c.clash_type,
                'Distance_m': c.distance,
                'Location_X': c.location[0],
                'Location_Y': c.location[1],
                'Location_Z': c.location[2],
                'Severity': c.severity
            }
            for c in self.clashes
        ])

    def get_summary(self) -> Dict:
        """Get clash detection summary"""
        df = self.get_clash_report()
        if df.empty:
            return {'total': 0}

        return {
            'total': len(self.clashes),
            'by_type': df['Clash_Type'].value_counts().to_dict(),
            'by_severity': df['Severity'].value_counts().to_dict(),
            'critical_count': len(df[df['Severity'] == 'Critical']),
            'element_types_involved': df['Element1_Type'].unique().tolist() +
                                     df['Element2_Type'].unique().tolist()
        }
```

### Clash Sets Configuration

#### Common Clash Test Sets

```python
## Define common clash test configurations
CLASH_SETS = {
    'structure_vs_mep': {
        'group1': ['IfcColumn', 'IfcBeam', 'IfcWall', 'IfcSlab'],
        'group2': ['IfcPipeSegment', 'IfcDuctSegment', 'IfcCableSegment'],
        'clearance': 0.05,
        'description': 'Structural elements vs MEP systems'
    },
    'piping_vs_hvac': {
        'group1': ['IfcPipeSegment', 'IfcPipeFitting'],
        'group2': ['IfcDuctSegment', 'IfcDuctFitting'],
        'clearance': 0.10,
        'description': 'Plumbing vs HVAC conflicts'
    },
    'doors_clearance': {
        'group1': ['IfcDoor'],
        'group2': ['IfcColumn', 'IfcWall'],
        'clearance': 0.90,  # Door swing clearance
        'description': 'Door opening clearances'
    },
    'electrical_vs_plumbing': {
        'group1': ['IfcCableSegment', 'IfcElectricDistributionBoard'],
        'group2': ['IfcPipeSegment', 'IfcSanitaryTerminal'],
        'clearance': 0.15,
        'description': 'Electrical safety clearance from water'
    },
    'ceiling_vs_mep': {
        'group1': ['IfcCovering'],
        'group2': ['IfcPipeSegment', 'IfcDuctSegment', 'IfcCableCarrierSegment'],
        'clearance': 0.05,
        'description': 'Ceiling clearance for MEP'
    }
}

def run_all_clash_tests(detector: ClashDetector, clash_sets: Dict = None) -> Dict:
    """Run all configured clash tests"""
    if clash_sets is None:
        clash_sets = CLASH_SETS

    results = {}

    for test_name, config in clash_sets.items():
        print(f"Running: {config['description']}...")

        # Hard clashes
        hard = detector.detect_hard_clashes(config['group1'], config['group2'])

        # Soft clashes
        soft = detector.detect_soft_clashes(
            config['group1'],
            config['group2'],
            config['clearance']
        )

        results[test_name] = {
            'description': config['description'],
            'hard_clashes': len(hard),
            'soft_clashes': len(soft),
            'total': len(hard) + len(soft)
        }

    return results
```

### Report Generation

#### Export Clash Report

```python
def export_clash_report(detector: ClashDetector, output_path: str):
    """Export comprehensive clash report to Excel"""
    df = detector.get_clash_report()
    summary = detector.get_summary()

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # Summary sheet
        summary_df = pd.DataFrame([{
            'Total Clashes': summary['total'],
            'Critical': summary.get('critical_count', 0),
            'Hard Clashes': summary['by_type'].get('Hard', 0),
            'Soft Clashes': summary['by_type'].get('Soft', 0)
        }])
        summary_df.to_excel(writer, sheet_name='Summary', index=False)

        # All clashes
        if not df.empty:
            df.to_excel(writer, sheet_name='All_Clashes', index=False)

            # By severity
            for severity in ['Critical', 'High', 'Medium', 'Low']:
                severity_df = df[df['Severity'] == severity]
                if not severity_df.empty:
                    severity_df.to_excel(writer, sheet_name=severity, index=False)

    return output_path

def generate_clash_html_report(detector: ClashDetector, output_path: str):
    """Generate HTML report with visualizations"""
    df = detector.get_clash_report()
    summary = detector.get_summary()

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Clash Detection Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .summary {{ background: #f5f5f5; padding: 20px; border-radius: 8px; }}
            .critical {{ background: #ffebee; }}
            .high {{ background: #fff3e0; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background: #4CAF50; color: white; }}
        </style>
    </head>
    <body>
        <h1>Clash Detection Report</h1>

        <div class="summary">
            <h2>Summary</h2>
            <p><strong>Total Clashes:</strong> {summary['total']}</p>
            <p><strong>Critical:</strong> {summary.get('critical_count', 0)}</p>
        </div>

        <h2>Clash Details</h2>
        {df.to_html(index=False) if not df.empty else '<p>No clashes found</p>'}
    </body>
    </html>
    """

    with open(output_path, 'w') as f:
        f.write(html)

    return output_path
```

### Quick Reference

| Clash Type | Description | Typical Clearance |
|------------|-------------|-------------------|
| Hard Clash | Physical intersection | 0 mm |
| Soft Clash | Clearance violation | 50-150 mm |
| Workflow | Schedule conflict | N/A |

| Severity | Distance | Action Required |
|----------|----------|-----------------|
| Critical | < 10 mm | Immediate redesign |
| High | 10-50 mm | Priority fix |
| Medium | 50-100 mm | Review needed |
| Low | > 100 mm | Monitor |

### Resources

- **IfcOpenShell**: https://ifcopenshell.org
- **DDC Website**: https://datadrivenconstruction.io

### Next Steps

- See `4d-simulation` for time-based clash analysis
- See `bim-validation-pipeline` for validation workflows
- See `ifc-data-extraction` for element data


## clash-resolution-analyzer

> Analyze BIM clash detection results and suggest resolutions. Prioritize clashes, identify patterns, assign responsibility, and track resolution status.

## Clash Resolution Analyzer for Construction

### Overview

Analyze clash detection results from BIM coordination. Prioritize clashes by impact, identify patterns, suggest resolutions, assign responsibility, and track resolution progress.

### Business Case

Clash resolution analysis enables:
- **Efficient Coordination**: Focus on critical clashes first
- **Pattern Recognition**: Fix root causes, not symptoms
- **Clear Accountability**: Assign responsibility by trade
- **Progress Tracking**: Monitor resolution status

### Technical Implementation

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum
from datetime import datetime
from collections import defaultdict

class ClashPriority(Enum):
    CRITICAL = 1  # Must resolve before construction
    HIGH = 2      # Resolve in next coordination cycle
    MEDIUM = 3    # Resolve before trade starts
    LOW = 4       # Minor, can resolve in field

class ClashStatus(Enum):
    NEW = "new"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    APPROVED = "approved"
    VOID = "void"  # Not a real clash

class ResolutionType(Enum):
    ROUTE_AROUND = "Route around obstruction"
    RAISE_LOWER = "Raise or lower element"
    RESIZE = "Resize element"
    RELOCATE = "Relocate element"
    STRUCTURAL_MOD = "Structural modification required"
    DESIGN_CHANGE = "Design change required"
    NO_CLASH = "Not a real clash (tolerance)"
    SEQUENCE = "Resolve by construction sequence"

@dataclass
class ClashElement:
    id: str
    name: str
    category: str
    discipline: str
    level: str
    system: str

@dataclass
class Clash:
    id: str
    name: str
    element1: ClashElement
    element2: ClashElement
    location: Tuple[float, float, float]
    distance: float  # Negative = hard clash, positive = clearance violation
    clash_type: str  # hard, clearance, duplicate
    priority: ClashPriority = ClashPriority.MEDIUM
    status: ClashStatus = ClashStatus.NEW
    assigned_to: str = ""
    resolution_type: Optional[ResolutionType] = None
    resolution_notes: str = ""
    created_date: datetime = field(default_factory=datetime.now)
    resolved_date: Optional[datetime] = None

@dataclass
class ClashPattern:
    pattern_type: str
    disciplines: Tuple[str, str]
    systems: Tuple[str, str]
    clash_count: int
    example_clashes: List[str]
    suggested_resolution: str
    root_cause: str

@dataclass
class ClashReport:
    report_name: str
    total_clashes: int
    new_clashes: int
    resolved_clashes: int
    clashes_by_priority: Dict[str, int]
    clashes_by_discipline: Dict[str, int]
    clashes_by_status: Dict[str, int]
    patterns: List[ClashPattern]
    resolution_rate: float

class ClashResolutionAnalyzer:
    """Analyze and manage BIM clash detection results."""

    # Discipline priority for resolution responsibility
    DISCIPLINE_PRIORITY = {
        'Structural': 1,
        'Architectural': 2,
        'Mechanical': 3,
        'Plumbing': 4,
        'Electrical': 5,
        'Fire Protection': 6,
    }

    # Common resolution strategies by clash type
    RESOLUTION_STRATEGIES = {
        ('Mechanical', 'Structural'): {
            'strategy': ResolutionType.ROUTE_AROUND,
            'responsible': 'Mechanical',
            'notes': 'MEP typically routes around structure'
        },
        ('Plumbing', 'Structural'): {
            'strategy': ResolutionType.ROUTE_AROUND,
            'responsible': 'Plumbing',
            'notes': 'Coordinate sleeves/penetrations with SE'
        },
        ('Electrical', 'Mechanical'): {
            'strategy': ResolutionType.RAISE_LOWER,
            'responsible': 'Electrical',
            'notes': 'Conduit typically more flexible than ductwork'
        },
        ('Mechanical', 'Mechanical'): {
            'strategy': ResolutionType.RESIZE,
            'responsible': 'Mechanical',
            'notes': 'Review duct sizing and routing options'
        },
        ('Fire Protection', 'Mechanical'): {
            'strategy': ResolutionType.ROUTE_AROUND,
            'responsible': 'Fire Protection',
            'notes': 'Sprinkler typically routes around major duct'
        },
    }

    def __init__(self):
        self.clashes: Dict[str, Clash] = {}
        self.patterns: List[ClashPattern] = []
        self.history: List[Dict] = []

    def import_clashes(self, clash_data: List[Dict]) -> int:
        """Import clashes from Navisworks or other clash detection software."""
        count = 0

        for data in clash_data:
            clash = Clash(
                id=data.get('id', f'CLH-{count}'),
                name=data.get('name', ''),
                element1=ClashElement(
                    id=data.get('element1_id', ''),
                    name=data.get('element1_name', ''),
                    category=data.get('element1_category', ''),
                    discipline=data.get('element1_discipline', ''),
                    level=data.get('element1_level', ''),
                    system=data.get('element1_system', '')
                ),
                element2=ClashElement(
                    id=data.get('element2_id', ''),
                    name=data.get('element2_name', ''),
                    category=data.get('element2_category', ''),
                    discipline=data.get('element2_discipline', ''),
                    level=data.get('element2_level', ''),
                    system=data.get('element2_system', '')
                ),
                location=(
                    data.get('x', 0),
                    data.get('y', 0),
                    data.get('z', 0)
                ),
                distance=data.get('distance', 0),
                clash_type=data.get('clash_type', 'hard')
            )

            # Auto-prioritize
            clash.priority = self._auto_prioritize(clash)

            # Auto-assign
            clash.assigned_to = self._auto_assign(clash)

            self.clashes[clash.id] = clash
            count += 1

        return count

    def _auto_prioritize(self, clash: Clash) -> ClashPriority:
        """Automatically prioritize clash based on characteristics."""
        # Hard clashes with structure are critical
        if clash.element1.discipline == 'Structural' or clash.element2.discipline == 'Structural':
            if clash.clash_type == 'hard':
                return ClashPriority.CRITICAL

        # Large penetration clashes
        if abs(clash.distance) > 0.1:  # More than 100mm overlap
            return ClashPriority.HIGH

        # MEP-MEP clashes
        mep_disciplines = ['Mechanical', 'Electrical', 'Plumbing', 'Fire Protection']
        if clash.element1.discipline in mep_disciplines and clash.element2.discipline in mep_disciplines:
            return ClashPriority.MEDIUM

        # Clearance violations
        if clash.clash_type == 'clearance':
            return ClashPriority.LOW

        return ClashPriority.MEDIUM

    def _auto_assign(self, clash: Clash) -> str:
        """Automatically assign responsibility based on discipline priority."""
        d1 = clash.element1.discipline
        d2 = clash.element2.discipline

        # Check for known resolution strategy
        key = (d1, d2) if (d1, d2) in self.RESOLUTION_STRATEGIES else (d2, d1)
        if key in self.RESOLUTION_STRATEGIES:
            return self.RESOLUTION_STRATEGIES[key]['responsible']

        # Default to lower priority discipline (typically more flexible)
        p1 = self.DISCIPLINE_PRIORITY.get(d1, 10)
        p2 = self.DISCIPLINE_PRIORITY.get(d2, 10)

        return d2 if p2 > p1 else d1

    def analyze_patterns(self) -> List[ClashPattern]:
        """Identify patterns in clashes."""
        patterns = []

        # Group by discipline pair
        discipline_pairs = defaultdict(list)
        for clash in self.clashes.values():
            pair = tuple(sorted([clash.element1.discipline, clash.element2.discipline]))
            discipline_pairs[pair].append(clash)

        for (d1, d2), clashes in discipline_pairs.items():
            if len(clashes) >= 3:  # Pattern threshold
                # Further group by system
                system_pairs = defaultdict(list)
                for clash in clashes:
                    sys_pair = tuple(sorted([clash.element1.system, clash.element2.system]))
                    system_pairs[sys_pair].append(clash)

                for (s1, s2), sys_clashes in system_pairs.items():
                    if len(sys_clashes) >= 2:
                        # Get resolution strategy
                        key = (d1, d2) if (d1, d2) in self.RESOLUTION_STRATEGIES else (d2, d1)
                        strategy = self.RESOLUTION_STRATEGIES.get(key, {})

                        patterns.append(ClashPattern(
                            pattern_type=f"{d1} vs {d2}",
                            disciplines=(d1, d2),
                            systems=(s1, s2),
                            clash_count=len(sys_clashes),
                            example_clashes=[c.id for c in sys_clashes[:3]],
                            suggested_resolution=strategy.get('strategy', ResolutionType.ROUTE_AROUND).value,
                            root_cause=f"Coordination needed between {s1} and {s2} systems"
                        ))

        self.patterns = sorted(patterns, key=lambda p: -p.clash_count)
        return self.patterns

    def suggest_resolution(self, clash_id: str) -> Dict:
        """Suggest resolution for a specific clash."""
        if clash_id not in self.clashes:
            return {'error': 'Clash not found'}

        clash = self.clashes[clash_id]
        d1, d2 = clash.element1.discipline, clash.element2.discipline

        # Get strategy
        key = (d1, d2) if (d1, d2) in self.RESOLUTION_STRATEGIES else (d2, d1)
        strategy = self.RESOLUTION_STRATEGIES.get(key, {})

        suggestion = {
            'clash_id': clash_id,
            'resolution_type': strategy.get('strategy', ResolutionType.ROUTE_AROUND),
            'responsible_discipline': strategy.get('responsible', self._auto_assign(clash)),
            'notes': strategy.get('notes', 'Review and coordinate'),
            'similar_clashes': [],
        }

        # Find similar clashes
        for pattern in self.patterns:
            if d1 in pattern.disciplines and d2 in pattern.disciplines:
                suggestion['similar_clashes'] = pattern.example_clashes
                suggestion['pattern_root_cause'] = pattern.root_cause
                break

        return suggestion

    def update_clash_status(self, clash_id: str, status: ClashStatus,
                            resolution_type: ResolutionType = None,
                            notes: str = "") -> bool:
        """Update clash status."""
        if clash_id not in self.clashes:
            return False

        clash = self.clashes[clash_id]
        old_status = clash.status

        clash.status = status
        if resolution_type:
            clash.resolution_type = resolution_type
        if notes:
            clash.resolution_notes = notes
        if status in [ClashStatus.RESOLVED, ClashStatus.APPROVED]:
            clash.resolved_date = datetime.now()

        # Track history
        self.history.append({
            'clash_id': clash_id,
            'timestamp': datetime.now(),
            'old_status': old_status.value,
            'new_status': status.value,
            'notes': notes
        })

        return True

    def get_clashes_by_discipline(self, discipline: str) -> List[Clash]:
        """Get all clashes assigned to a discipline."""
        return [c for c in self.clashes.values() if c.assigned_to == discipline]

    def get_clashes_by_level(self, level: str) -> List[Clash]:
        """Get all clashes on a specific level."""
        return [c for c in self.clashes.values()
                if c.element1.level == level or c.element2.level == level]

    def generate_coordination_matrix(self) -> Dict[str, Dict[str, int]]:
        """Generate matrix showing clashes between disciplines."""
        matrix = defaultdict(lambda: defaultdict(int))

        for clash in self.clashes.values():
            d1 = clash.element1.discipline
            d2 = clash.element2.discipline
            matrix[d1][d2] += 1
            if d1 != d2:
                matrix[d2][d1] += 1

        return dict(matrix)

    def generate_report(self) -> ConsistencyReport:
        """Generate comprehensive clash analysis report."""
        clashes_by_priority = defaultdict(int)
        clashes_by_discipline = defaultdict(int)
        clashes_by_status = defaultdict(int)

        for clash in self.clashes.values():
            clashes_by_priority[clash.priority.name] += 1
            clashes_by_discipline[clash.assigned_to] += 1
            clashes_by_status[clash.status.value] += 1

        resolved = clashes_by_status.get('resolved', 0) + clashes_by_status.get('approved', 0)
        resolution_rate = resolved / len(self.clashes) * 100 if self.clashes else 0

        return ClashReport(
            report_name=f"Clash Report {datetime.now().strftime('%Y-%m-%d')}",
            total_clashes=len(self.clashes),
            new_clashes=clashes_by_status.get('new', 0),
            resolved_clashes=resolved,
            clashes_by_priority=dict(clashes_by_priority),
            clashes_by_discipline=dict(clashes_by_discipline),
            clashes_by_status=dict(clashes_by_status),
            patterns=self.patterns,
            resolution_rate=resolution_rate
        )

    def generate_report_markdown(self) -> str:
        """Generate markdown report."""
        report = self.generate_report()

        lines = ["# Clash Resolution Report", ""]
        lines.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
        lines.append(f"**Total Clashes:** {report.total_clashes}")
        lines.append(f"**Resolution Rate:** {report.resolution_rate:.1f}%")
        lines.append("")

        # By status
        lines.append("## Status Summary")
        for status, count in report.clashes_by_status.items():
            lines.append(f"- {status}: {count}")
        lines.append("")

        # By priority
        lines.append("## Priority Breakdown")
        for priority, count in sorted(report.clashes_by_priority.items()):
            lines.append(f"- {priority}: {count}")
        lines.append("")

        # By discipline
        lines.append("## By Responsible Discipline")
        for disc, count in sorted(report.clashes_by_discipline.items(), key=lambda x: -x[1]):
            lines.append(f"- {disc}: {count}")
        lines.append("")

        # Patterns
        if report.patterns:
            lines.append("## Clash Patterns Identified")
            for pattern in report.patterns[:5]:
                lines.append(f"\n### {pattern.pattern_type}")
                lines.append(f"- **Count:** {pattern.clash_count} clashes")
                lines.append(f"- **Systems:** {pattern.systems[0]} vs {pattern.systems[1]}")
                lines.append(f"- **Root Cause:** {pattern.root_cause}")
                lines.append(f"- **Suggested Resolution:** {pattern.suggested_resolution}")

        # Critical clashes
        critical = [c for c in self.clashes.values() if c.priority == ClashPriority.CRITICAL and c.status == ClashStatus.NEW]
        if critical:
            lines.append("\n## Critical Unresolved Clashes")
            for clash in critical[:10]:
                lines.append(f"- **{clash.id}**: {clash.element1.name} vs {clash.element2.name}")
                lines.append(f"  - Location: Level {clash.element1.level}")
                lines.append(f"  - Assigned: {clash.assigned_to}")

        return "\n".join(lines)
```

### Quick Start

```python
## Initialize analyzer
analyzer = ClashResolutionAnalyzer()

## Import clashes (from Navisworks export)
clash_data = [
    {
        'id': 'CLH-001',
        'name': 'Duct vs Beam',
        'element1_discipline': 'Mechanical',
        'element1_system': 'Supply Air',
        'element1_level': 'Level 2',
        'element2_discipline': 'Structural',
        'element2_system': 'Steel Frame',
        'element2_level': 'Level 2',
        'distance': -0.15,
        'clash_type': 'hard'
    }
]

count = analyzer.import_clashes(clash_data)
print(f"Imported {count} clashes")

## Analyze patterns
patterns = analyzer.analyze_patterns()
for pattern in patterns:
    print(f"Pattern: {pattern.pattern_type} - {pattern.clash_count} clashes")

## Get resolution suggestion
suggestion = analyzer.suggest_resolution('CLH-001')
print(f"Suggested resolution: {suggestion['resolution_type'].value}")
print(f"Responsible: {suggestion['responsible_discipline']}")

## Update status
analyzer.update_clash_status(
    'CLH-001',
    ClashStatus.RESOLVED,
    ResolutionType.ROUTE_AROUND,
    'Duct rerouted below beam'
)

## Generate report
print(analyzer.generate_report_markdown())
```

### Dependencies

```bash
pip install (no external dependencies)
```


---

# Validation


## bim-validation-pipeline

> Build automated BIM validation pipelines for IFC/Revit data. Continuous validation against IDS, LOD requirements, COBie, and project-specific BEP standards.

## BIM Validation Pipeline

### Overview

Based on DDC methodology (Chapter 4.3), this skill provides automated BIM data validation pipelines. Validate BIM models against Information Delivery Specification (IDS), Level of Development (LOD) requirements, and project standards.

**Book Reference:** "Автоматический ETL конвейер для валидации данных" / "Automated ETL Pipeline for Data Validation"

> "Автоматизированная валидация BIM-данных позволяет выявлять ошибки на ранних стадиях и обеспечивать соответствие требованиям BEP."
> — DDC Book, Chapter 4.3

### Quick Start

```python
import ifcopenshell
import pandas as pd

## Load IFC model
ifc_model = ifcopenshell.open("model.ifc")

## Quick validation checks
walls = ifc_model.by_type("IfcWall")
print(f"Total walls: {len(walls)}")

## Check for required properties
issues = []
for wall in walls:
    # Check if wall has material
    if not wall.HasAssociations:
        issues.append(f"Wall {wall.GlobalId}: No material assigned")

print(f"Issues found: {len(issues)}")
```

### BIM Validation Framework

#### Core Validator Class

```python
import ifcopenshell
import ifcopenshell.util.element as element_util
import pandas as pd
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum

class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

@dataclass
class ValidationIssue:
    element_id: str
    element_type: str
    rule_id: str
    severity: Severity
    message: str
    location: Optional[str] = None

class BIMValidator:
    """Comprehensive BIM model validator"""

    def __init__(self, ifc_path: str):
        self.model = ifcopenshell.open(ifc_path)
        self.issues: List[ValidationIssue] = []
        self.stats = {}

    def validate_all(self):
        """Run all validation checks"""
        self.validate_geometry()
        self.validate_properties()
        self.validate_relationships()
        self.validate_naming()
        self.validate_classification()
        return self.get_report()

    def validate_geometry(self):
        """Check geometry validity"""
        elements_with_geometry = [
            e for e in self.model.by_type("IfcProduct")
            if e.Representation
        ]

        for element in elements_with_geometry:
            # Check for zero volume
            try:
                settings = ifcopenshell.geom.settings()
                shape = ifcopenshell.geom.create_shape(settings, element)
                # Volume check would go here
            except:
                self.issues.append(ValidationIssue(
                    element_id=element.GlobalId,
                    element_type=element.is_a(),
                    rule_id="GEO-001",
                    severity=Severity.ERROR,
                    message="Invalid or missing geometry"
                ))

        self.stats['elements_with_geometry'] = len(elements_with_geometry)

    def validate_properties(self, required_psets: Dict[str, List[str]] = None):
        """Check required property sets and properties"""
        if required_psets is None:
            required_psets = {
                'IfcWall': ['Pset_WallCommon', 'BaseQuantities'],
                'IfcSlab': ['Pset_SlabCommon', 'BaseQuantities'],
                'IfcColumn': ['Pset_ColumnCommon', 'BaseQuantities'],
                'IfcBeam': ['Pset_BeamCommon', 'BaseQuantities']
            }

        for ifc_type, psets in required_psets.items():
            elements = self.model.by_type(ifc_type)

            for element in elements:
                element_psets = element_util.get_psets(element)

                for required_pset in psets:
                    if required_pset not in element_psets:
                        self.issues.append(ValidationIssue(
                            element_id=element.GlobalId,
                            element_type=ifc_type,
                            rule_id="PROP-001",
                            severity=Severity.WARNING,
                            message=f"Missing PropertySet: {required_pset}"
                        ))

    def validate_relationships(self):
        """Check spatial containment and relationships"""
        products = self.model.by_type("IfcProduct")

        for product in products:
            # Check spatial containment
            if hasattr(product, 'ContainedInStructure'):
                if not product.ContainedInStructure:
                    self.issues.append(ValidationIssue(
                        element_id=product.GlobalId,
                        element_type=product.is_a(),
                        rule_id="REL-001",
                        severity=Severity.WARNING,
                        message="Element not assigned to building storey"
                    ))

            # Check material assignment
            if hasattr(product, 'HasAssociations'):
                has_material = any(
                    rel.is_a('IfcRelAssociatesMaterial')
                    for rel in (product.HasAssociations or [])
                )
                if not has_material and product.is_a() in ['IfcWall', 'IfcSlab', 'IfcColumn']:
                    self.issues.append(ValidationIssue(
                        element_id=product.GlobalId,
                        element_type=product.is_a(),
                        rule_id="MAT-001",
                        severity=Severity.WARNING,
                        message="No material assigned"
                    ))

    def validate_naming(self, patterns: Dict[str, str] = None):
        """Validate element naming conventions"""
        import re

        if patterns is None:
            patterns = {
                'IfcBuildingStorey': r'^(Level|L|Floor|Уровень)\s*[-]?\d+',
                'IfcWall': r'^W[-_]?\d{3,}|^Wall[-_]',
                'IfcColumn': r'^C[-_]?\d{3,}|^Column[-_]',
                'IfcSpace': r'^Room[-_]|^Space[-_]'
            }

        for ifc_type, pattern in patterns.items():
            elements = self.model.by_type(ifc_type)

            for element in elements:
                name = element.Name or ""
                if not re.match(pattern, name, re.IGNORECASE):
                    self.issues.append(ValidationIssue(
                        element_id=element.GlobalId,
                        element_type=ifc_type,
                        rule_id="NAME-001",
                        severity=Severity.INFO,
                        message=f"Name '{name}' doesn't match convention"
                    ))

    def validate_classification(self, required_systems: List[str] = None):
        """Check classification system assignments"""
        if required_systems is None:
            required_systems = ['Uniclass', 'OmniClass', 'Uniformat']

        elements = self.model.by_type("IfcProduct")

        for element in elements:
            if hasattr(element, 'HasAssociations'):
                has_classification = any(
                    rel.is_a('IfcRelAssociatesClassification')
                    for rel in (element.HasAssociations or [])
                )

                if not has_classification:
                    self.issues.append(ValidationIssue(
                        element_id=element.GlobalId,
                        element_type=element.is_a(),
                        rule_id="CLASS-001",
                        severity=Severity.INFO,
                        message="No classification assigned"
                    ))

    def get_report(self):
        """Generate validation report"""
        by_severity = {s: [] for s in Severity}
        by_type = {}
        by_rule = {}

        for issue in self.issues:
            by_severity[issue.severity].append(issue)

            if issue.element_type not in by_type:
                by_type[issue.element_type] = []
            by_type[issue.element_type].append(issue)

            if issue.rule_id not in by_rule:
                by_rule[issue.rule_id] = []
            by_rule[issue.rule_id].append(issue)

        return {
            'total_issues': len(self.issues),
            'errors': len(by_severity[Severity.ERROR]),
            'warnings': len(by_severity[Severity.WARNING]),
            'info': len(by_severity[Severity.INFO]),
            'by_type': {k: len(v) for k, v in by_type.items()},
            'by_rule': {k: len(v) for k, v in by_rule.items()},
            'issues': self.issues,
            'stats': self.stats
        }
```

### LOD Validation

#### Level of Development Checker

```python
class LODValidator:
    """Validate Level of Development (LOD) requirements"""

    # LOD requirements by element type
    LOD_REQUIREMENTS = {
        'LOD100': {
            'geometry': False,
            'properties': [],
            'description': 'Conceptual'
        },
        'LOD200': {
            'geometry': True,
            'approximate_size': True,
            'properties': ['Category'],
            'description': 'Schematic Design'
        },
        'LOD300': {
            'geometry': True,
            'exact_size': True,
            'properties': ['Category', 'Material', 'Type'],
            'quantities': ['Length', 'Area', 'Volume'],
            'description': 'Design Development'
        },
        'LOD350': {
            'geometry': True,
            'exact_size': True,
            'properties': ['Category', 'Material', 'Type', 'Manufacturer'],
            'quantities': ['Length', 'Area', 'Volume', 'Weight'],
            'connections': True,
            'description': 'Construction Documentation'
        },
        'LOD400': {
            'geometry': True,
            'fabrication_ready': True,
            'properties': ['Category', 'Material', 'Type', 'Manufacturer',
                          'Model', 'Serial', 'InstallationDate'],
            'quantities': ['All'],
            'connections': True,
            'description': 'Fabrication & Assembly'
        }
    }

    def __init__(self, model, target_lod='LOD300'):
        self.model = model
        self.target_lod = target_lod
        self.requirements = self.LOD_REQUIREMENTS.get(target_lod, {})
        self.results = []

    def validate_element(self, element):
        """Validate single element against LOD requirements"""
        issues = []
        element_guid = element.GlobalId
        psets = element_util.get_psets(element)

        # Check geometry
        if self.requirements.get('geometry'):
            if not element.Representation:
                issues.append({
                    'element': element_guid,
                    'issue': 'Missing geometry',
                    'required_for': self.target_lod
                })

        # Check required properties
        required_props = self.requirements.get('properties', [])
        all_props = {}
        for pset_name, props in psets.items():
            all_props.update(props)

        for prop in required_props:
            if prop not in all_props or all_props[prop] is None:
                issues.append({
                    'element': element_guid,
                    'issue': f'Missing property: {prop}',
                    'required_for': self.target_lod
                })

        # Check quantities
        required_quantities = self.requirements.get('quantities', [])
        if required_quantities != ['All']:
            qsets = psets.get('BaseQuantities', {})
            for qty in required_quantities:
                if qty not in qsets:
                    issues.append({
                        'element': element_guid,
                        'issue': f'Missing quantity: {qty}',
                        'required_for': self.target_lod
                    })

        return issues

    def validate_model(self, element_types=None):
        """Validate entire model"""
        if element_types is None:
            element_types = ['IfcWall', 'IfcSlab', 'IfcColumn', 'IfcBeam',
                            'IfcDoor', 'IfcWindow', 'IfcStair']

        all_issues = []
        summary = {}

        for ifc_type in element_types:
            elements = self.model.by_type(ifc_type)
            type_issues = []

            for element in elements:
                issues = self.validate_element(element)
                type_issues.extend(issues)

            summary[ifc_type] = {
                'total': len(elements),
                'issues': len(type_issues),
                'compliance': ((len(elements) - len(type_issues)) /
                              len(elements) * 100) if elements else 100
            }
            all_issues.extend(type_issues)

        return {
            'target_lod': self.target_lod,
            'total_issues': len(all_issues),
            'summary': summary,
            'issues': all_issues
        }
```

### IDS Validation

#### Information Delivery Specification

```python
import xml.etree.ElementTree as ET

class IDSValidator:
    """Validate against IDS (Information Delivery Specification)"""

    def __init__(self, ids_path: str):
        self.ids = self._parse_ids(ids_path)

    def _parse_ids(self, path):
        """Parse IDS XML file"""
        tree = ET.parse(path)
        root = tree.getroot()

        specifications = []
        for spec in root.findall('.//specification'):
            specifications.append({
                'name': spec.get('name'),
                'applicability': self._parse_facets(spec.find('applicability')),
                'requirements': self._parse_facets(spec.find('requirements'))
            })

        return specifications

    def _parse_facets(self, element):
        """Parse IDS facets"""
        if element is None:
            return []

        facets = []
        for child in element:
            facet = {
                'type': child.tag,
                'constraints': {}
            }
            for attr, value in child.attrib.items():
                facet['constraints'][attr] = value
            facets.append(facet)

        return facets

    def validate(self, model):
        """Validate IFC model against IDS"""
        results = []

        for spec in self.ids:
            applicable_elements = self._find_applicable_elements(
                model, spec['applicability']
            )

            for element in applicable_elements:
                issues = self._check_requirements(element, spec['requirements'])
                if issues:
                    results.append({
                        'specification': spec['name'],
                        'element': element.GlobalId,
                        'issues': issues
                    })

        return results

    def _find_applicable_elements(self, model, applicability):
        """Find elements matching applicability criteria"""
        elements = []

        for facet in applicability:
            if facet['type'] == 'entity':
                ifc_type = facet['constraints'].get('name')
                if ifc_type:
                    elements.extend(model.by_type(ifc_type))

        return elements

    def _check_requirements(self, element, requirements):
        """Check element against requirements"""
        issues = []
        psets = element_util.get_psets(element)

        for req in requirements:
            if req['type'] == 'property':
                pset_name = req['constraints'].get('propertySet')
                prop_name = req['constraints'].get('name')

                if pset_name and prop_name:
                    pset = psets.get(pset_name, {})
                    if prop_name not in pset:
                        issues.append(f"Missing property: {pset_name}.{prop_name}")

        return issues
```

### Pipeline Automation

#### Automated Validation Pipeline

```python
import os
from datetime import datetime
import json

class BIMValidationPipeline:
    """Automated BIM validation pipeline"""

    def __init__(self, config_path=None):
        self.config = self._load_config(config_path)
        self.results_history = []

    def _load_config(self, path):
        if path and os.path.exists(path):
            with open(path) as f:
                return json.load(f)

        return {
            'lod_target': 'LOD300',
            'required_psets': {
                'IfcWall': ['Pset_WallCommon'],
                'IfcSlab': ['Pset_SlabCommon']
            },
            'naming_patterns': {},
            'fail_on_errors': True,
            'warn_threshold': 50
        }

    def run(self, ifc_path):
        """Run complete validation pipeline"""
        start_time = datetime.now()

        # Initialize validators
        validator = BIMValidator(ifc_path)
        lod_validator = LODValidator(
            validator.model,
            self.config['lod_target']
        )

        # Run validations
        bim_report = validator.validate_all()
        lod_report = lod_validator.validate_model()

        # Compile results
        result = {
            'file': ifc_path,
            'timestamp': start_time.isoformat(),
            'duration_seconds': (datetime.now() - start_time).total_seconds(),
            'bim_validation': bim_report,
            'lod_validation': lod_report,
            'passed': self._evaluate_pass(bim_report, lod_report)
        }

        self.results_history.append(result)
        return result

    def _evaluate_pass(self, bim_report, lod_report):
        """Determine if validation passed"""
        if self.config['fail_on_errors'] and bim_report['errors'] > 0:
            return False

        if bim_report['warnings'] > self.config['warn_threshold']:
            return False

        return True

    def run_batch(self, ifc_paths):
        """Run validation on multiple files"""
        results = []
        for path in ifc_paths:
            try:
                result = self.run(path)
                results.append(result)
            except Exception as e:
                results.append({
                    'file': path,
                    'error': str(e),
                    'passed': False
                })

        return {
            'total': len(results),
            'passed': sum(1 for r in results if r.get('passed', False)),
            'failed': sum(1 for r in results if not r.get('passed', True)),
            'results': results
        }

    def export_report(self, output_path):
        """Export validation results to Excel"""
        if not self.results_history:
            return None

        latest = self.results_history[-1]

        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Summary
            summary = pd.DataFrame({
                'Metric': ['File', 'Timestamp', 'Passed', 'Errors', 'Warnings'],
                'Value': [
                    latest['file'],
                    latest['timestamp'],
                    latest['passed'],
                    latest['bim_validation']['errors'],
                    latest['bim_validation']['warnings']
                ]
            })
            summary.to_excel(writer, sheet_name='Summary', index=False)

            # Issues
            if latest['bim_validation']['issues']:
                issues_df = pd.DataFrame([
                    {
                        'Element': i.element_id,
                        'Type': i.element_type,
                        'Rule': i.rule_id,
                        'Severity': i.severity.value,
                        'Message': i.message
                    }
                    for i in latest['bim_validation']['issues']
                ])
                issues_df.to_excel(writer, sheet_name='Issues', index=False)

        return output_path
```

### Quick Reference

| Rule ID | Description | Severity |
|---------|-------------|----------|
| GEO-001 | Invalid/missing geometry | ERROR |
| PROP-001 | Missing PropertySet | WARNING |
| REL-001 | No spatial containment | WARNING |
| MAT-001 | No material assigned | WARNING |
| NAME-001 | Invalid naming convention | INFO |
| CLASS-001 | No classification | INFO |

### LOD Requirements Summary

| LOD | Geometry | Properties | Quantities |
|-----|----------|------------|------------|
| 100 | No | - | - |
| 200 | Approximate | Category | - |
| 300 | Exact | Material, Type | L, A, V |
| 350 | Exact + connections | Manufacturer | All |
| 400 | Fabrication-ready | All details | All |

### Resources

- **Book**: "Data-Driven Construction" by Artem Boiko, Chapter 4.3
- **Website**: https://datadrivenconstruction.io
- **IDS Standard**: https://technical.buildingsmart.org/projects/information-delivery-specification-ids/
- **IfcOpenShell**: https://ifcopenshell.org

### Next Steps

- See `ifc-data-extraction` for extracting data from IFC
- See `data-quality-check` for general data validation
- See `qto-report` for quantity take-off from validated models


## bim-consistency-checker

> Check BIM model consistency: naming conventions, parameter completeness, spatial relationships, and data integrity across model elements.

## BIM Consistency Checker for Construction

### Overview

Validate BIM model consistency including naming conventions, parameter completeness, spatial relationships, classification compliance, and cross-reference integrity.

### Business Case

BIM consistency checking ensures:
- **Data Quality**: Complete and accurate model data
- **Interoperability**: Models work across platforms
- **Coordination**: Consistent information for all trades
- **Deliverable Compliance**: Meet BIM execution plan requirements

### Technical Implementation

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Set
from enum import Enum
import re

class CheckSeverity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

class CheckCategory(Enum):
    NAMING = "naming"
    PARAMETERS = "parameters"
    SPATIAL = "spatial"
    CLASSIFICATION = "classification"
    GEOMETRY = "geometry"
    RELATIONSHIPS = "relationships"

@dataclass
class ConsistencyIssue:
    element_id: str
    element_name: str
    category: CheckCategory
    severity: CheckSeverity
    rule: str
    message: str
    suggestion: str = ""

@dataclass
class ConsistencyReport:
    model_name: str
    total_elements: int
    elements_checked: int
    issues: List[ConsistencyIssue]
    issues_by_category: Dict[str, int]
    issues_by_severity: Dict[str, int]
    pass_rate: float

@dataclass
class NamingConvention:
    element_type: str
    pattern: str
    description: str
    examples: List[str]

class BIMConsistencyChecker:
    """Check BIM model consistency and data quality."""

    # Default naming conventions
    DEFAULT_NAMING_RULES = [
        NamingConvention(
            element_type='Level',
            pattern=r'^(L|Level)\s*\d{1,2}$|^(B|Basement)\s*\d?$|^(R|Roof)$',
            description='Levels should follow L01, Level 1, B1, Roof pattern',
            examples=['L01', 'Level 1', 'B1', 'Roof']
        ),
        NamingConvention(
            element_type='Grid',
            pattern=r'^[A-Z]$|^\d{1,2}$|^[A-Z]\.\d$',
            description='Grids should be single letters (A-Z) or numbers',
            examples=['A', '1', 'A.1']
        ),
        NamingConvention(
            element_type='Room',
            pattern=r'^\d{3,4}[A-Z]?\s*-?\s*.+',
            description='Rooms should have number and name (101 - Office)',
            examples=['101 - Office', '201A Conference']
        ),
        NamingConvention(
            element_type='Wall',
            pattern=r'^(INT|EXT|CW|CMU|GYP)[-_].+',
            description='Walls should have type prefix',
            examples=['INT-GYP-1HR', 'EXT-CMU-8IN']
        ),
        NamingConvention(
            element_type='Door',
            pattern=r'^[A-Z]?\d{2,3}[A-Z]?$',
            description='Doors should follow type numbering',
            examples=['101', 'A101', '101A']
        ),
    ]

    # Required parameters by element type
    REQUIRED_PARAMETERS = {
        'Wall': ['Fire Rating', 'Function', 'Structural'],
        'Door': ['Fire Rating', 'Width', 'Height', 'Frame Material'],
        'Room': ['Name', 'Number', 'Area', 'Department'],
        'Window': ['Width', 'Height', 'Glass Type'],
        'Floor': ['Structural', 'Fire Rating'],
        'Ceiling': ['Height', 'Type'],
        'Column': ['Structural Material', 'Shape'],
        'Beam': ['Structural Material', 'Size'],
    }

    def __init__(self):
        self.naming_rules: List[NamingConvention] = list(self.DEFAULT_NAMING_RULES)
        self.required_params: Dict[str, List[str]] = dict(self.REQUIRED_PARAMETERS)
        self.issues: List[ConsistencyIssue] = []

    def add_naming_rule(self, rule: NamingConvention):
        """Add custom naming convention rule."""
        self.naming_rules.append(rule)

    def set_required_parameters(self, element_type: str, parameters: List[str]):
        """Set required parameters for an element type."""
        self.required_params[element_type] = parameters

    def check_model(self, elements: List[Dict]) -> ConsistencyReport:
        """Run all consistency checks on model elements."""
        self.issues = []

        for element in elements:
            self._check_naming(element)
            self._check_parameters(element)
            self._check_spatial(element)
            self._check_classification(element)
            self._check_geometry(element)

        # Cross-element checks
        self._check_relationships(elements)
        self._check_duplicates(elements)

        # Calculate statistics
        issues_by_category = {}
        issues_by_severity = {}

        for issue in self.issues:
            cat = issue.category.value
            sev = issue.severity.value
            issues_by_category[cat] = issues_by_category.get(cat, 0) + 1
            issues_by_severity[sev] = issues_by_severity.get(sev, 0) + 1

        elements_with_issues = len(set(i.element_id for i in self.issues))
        pass_rate = (len(elements) - elements_with_issues) / len(elements) * 100 if elements else 100

        return ConsistencyReport(
            model_name='Model',
            total_elements=len(elements),
            elements_checked=len(elements),
            issues=self.issues,
            issues_by_category=issues_by_category,
            issues_by_severity=issues_by_severity,
            pass_rate=pass_rate
        )

    def _check_naming(self, element: Dict):
        """Check element naming conventions."""
        element_type = element.get('type', '')
        name = element.get('name', '')
        element_id = element.get('id', '')

        if not name:
            self.issues.append(ConsistencyIssue(
                element_id=element_id,
                element_name='(no name)',
                category=CheckCategory.NAMING,
                severity=CheckSeverity.ERROR,
                rule='Name Required',
                message='Element has no name',
                suggestion='Assign a descriptive name following conventions'
            ))
            return

        # Check against naming rules
        for rule in self.naming_rules:
            if rule.element_type.lower() in element_type.lower():
                if not re.match(rule.pattern, name, re.IGNORECASE):
                    self.issues.append(ConsistencyIssue(
                        element_id=element_id,
                        element_name=name,
                        category=CheckCategory.NAMING,
                        severity=CheckSeverity.WARNING,
                        rule=f'{rule.element_type} Naming',
                        message=f'Name "{name}" does not follow convention',
                        suggestion=f'{rule.description}. Examples: {", ".join(rule.examples)}'
                    ))

        # Check for special characters
        if re.search(r'[<>:"/\\|?*]', name):
            self.issues.append(ConsistencyIssue(
                element_id=element_id,
                element_name=name,
                category=CheckCategory.NAMING,
                severity=CheckSeverity.ERROR,
                rule='Invalid Characters',
                message='Name contains invalid characters',
                suggestion='Remove special characters: < > : " / \\ | ? *'
            ))

    def _check_parameters(self, element: Dict):
        """Check parameter completeness."""
        element_type = element.get('type', '')
        element_id = element.get('id', '')
        name = element.get('name', '')
        params = element.get('parameters', {})

        # Check required parameters
        required = self.required_params.get(element_type, [])
        for param in required:
            if param not in params or params[param] in [None, '', 'None']:
                self.issues.append(ConsistencyIssue(
                    element_id=element_id,
                    element_name=name,
                    category=CheckCategory.PARAMETERS,
                    severity=CheckSeverity.WARNING,
                    rule='Required Parameter',
                    message=f'Missing required parameter: {param}',
                    suggestion=f'Set value for {param}'
                ))

        # Check for default/placeholder values
        placeholder_values = ['TBD', 'XXX', 'TODO', 'CHANGE', '<default>']
        for param, value in params.items():
            if str(value).upper() in placeholder_values:
                self.issues.append(ConsistencyIssue(
                    element_id=element_id,
                    element_name=name,
                    category=CheckCategory.PARAMETERS,
                    severity=CheckSeverity.WARNING,
                    rule='Placeholder Value',
                    message=f'Parameter "{param}" has placeholder value: {value}',
                    suggestion='Replace with actual value'
                ))

    def _check_spatial(self, element: Dict):
        """Check spatial consistency."""
        element_id = element.get('id', '')
        name = element.get('name', '')
        element_type = element.get('type', '')

        # Check level assignment
        level = element.get('level')
        requires_level = element_type in ['Wall', 'Door', 'Window', 'Room', 'Floor', 'Ceiling']

        if requires_level and not level:
            self.issues.append(ConsistencyIssue(
                element_id=element_id,
                element_name=name,
                category=CheckCategory.SPATIAL,
                severity=CheckSeverity.ERROR,
                rule='Level Assignment',
                message='Element not assigned to a level',
                suggestion='Assign element to appropriate level'
            ))

        # Check room bounding
        if element_type == 'Wall':
            room_bounding = element.get('room_bounding', True)
            if not room_bounding:
                self.issues.append(ConsistencyIssue(
                    element_id=element_id,
                    element_name=name,
                    category=CheckCategory.SPATIAL,
                    severity=CheckSeverity.INFO,
                    rule='Room Bounding',
                    message='Wall is not room bounding',
                    suggestion='Verify this is intentional'
                ))

    def _check_classification(self, element: Dict):
        """Check classification codes."""
        element_id = element.get('id', '')
        name = element.get('name', '')
        params = element.get('parameters', {})

        # Check for classification
        classification = params.get('Classification') or params.get('OmniClass') or params.get('UniFormat')

        if not classification:
            self.issues.append(ConsistencyIssue(
                element_id=element_id,
                element_name=name,
                category=CheckCategory.CLASSIFICATION,
                severity=CheckSeverity.INFO,
                rule='Classification Required',
                message='Element has no classification code',
                suggestion='Assign OmniClass, UniFormat, or other classification'
            ))
        else:
            # Validate format
            if not re.match(r'^\d{2}[-\s]?\d{2}[-\s]?\d{2}', str(classification)):
                self.issues.append(ConsistencyIssue(
                    element_id=element_id,
                    element_name=name,
                    category=CheckCategory.CLASSIFICATION,
                    severity=CheckSeverity.WARNING,
                    rule='Classification Format',
                    message=f'Invalid classification format: {classification}',
                    suggestion='Use standard format (XX XX XX)'
                ))

    def _check_geometry(self, element: Dict):
        """Check geometry validity."""
        element_id = element.get('id', '')
        name = element.get('name', '')
        geometry = element.get('geometry', {})

        # Check for zero area/volume
        area = geometry.get('area', 0)
        volume = geometry.get('volume', 0)

        if area == 0 and volume == 0 and element.get('type') not in ['Grid', 'Level', 'ReferencePlane']:
            self.issues.append(ConsistencyIssue(
                element_id=element_id,
                element_name=name,
                category=CheckCategory.GEOMETRY,
                severity=CheckSeverity.ERROR,
                rule='Zero Geometry',
                message='Element has zero area and volume',
                suggestion='Check element geometry is valid'
            ))

        # Check for extremely small elements
        if 0 < area < 0.01:  # Less than 0.01 m² or ft²
            self.issues.append(ConsistencyIssue(
                element_id=element_id,
                element_name=name,
                category=CheckCategory.GEOMETRY,
                severity=CheckSeverity.WARNING,
                rule='Tiny Element',
                message=f'Element has very small area: {area}',
                suggestion='Verify element is intentional and not a modeling error'
            ))

    def _check_relationships(self, elements: List[Dict]):
        """Check cross-element relationships."""
        # Build lookup
        elements_by_id = {e['id']: e for e in elements}
        elements_by_type = {}
        for e in elements:
            t = e.get('type', '')
            if t not in elements_by_type:
                elements_by_type[t] = []
            elements_by_type[t].append(e)

        # Check door-wall relationships
        for door in elements_by_type.get('Door', []):
            host_wall = door.get('host_id')
            if host_wall and host_wall not in elements_by_id:
                self.issues.append(ConsistencyIssue(
                    element_id=door['id'],
                    element_name=door.get('name', ''),
                    category=CheckCategory.RELATIONSHIPS,
                    severity=CheckSeverity.ERROR,
                    rule='Invalid Host',
                    message=f'Door references non-existent wall: {host_wall}',
                    suggestion='Rehost door to valid wall'
                ))

        # Check room enclosure
        for room in elements_by_type.get('Room', []):
            if not room.get('is_bounded', True):
                self.issues.append(ConsistencyIssue(
                    element_id=room['id'],
                    element_name=room.get('name', ''),
                    category=CheckCategory.RELATIONSHIPS,
                    severity=CheckSeverity.ERROR,
                    rule='Unbounded Room',
                    message='Room is not properly bounded',
                    suggestion='Check room boundary walls'
                ))

    def _check_duplicates(self, elements: List[Dict]):
        """Check for duplicate elements."""
        seen: Dict[str, List[Dict]] = {}

        for element in elements:
            # Create signature for duplicate detection
            sig_parts = [
                element.get('type', ''),
                str(element.get('geometry', {}).get('location', '')),
                element.get('name', '')
            ]
            signature = '|'.join(sig_parts)

            if signature in seen:
                for dup in seen[signature]:
                    self.issues.append(ConsistencyIssue(
                        element_id=element['id'],
                        element_name=element.get('name', ''),
                        category=CheckCategory.RELATIONSHIPS,
                        severity=CheckSeverity.WARNING,
                        rule='Duplicate Element',
                        message=f'Possible duplicate of element {dup["id"]}',
                        suggestion='Review and remove duplicate if confirmed'
                    ))

            if signature not in seen:
                seen[signature] = []
            seen[signature].append(element)

    def generate_report(self, report: ConsistencyReport) -> str:
        """Generate consistency check report."""
        lines = ["# BIM Consistency Check Report", ""]
        lines.append(f"**Model:** {report.model_name}")
        lines.append(f"**Elements Checked:** {report.elements_checked}")
        lines.append(f"**Pass Rate:** {report.pass_rate:.1f}%")
        lines.append("")

        # Summary
        lines.append("## Summary")
        lines.append(f"- **Total Issues:** {len(report.issues)}")
        lines.append(f"- Errors: {report.issues_by_severity.get('error', 0)}")
        lines.append(f"- Warnings: {report.issues_by_severity.get('warning', 0)}")
        lines.append(f"- Info: {report.issues_by_severity.get('info', 0)}")
        lines.append("")

        # By category
        lines.append("## Issues by Category")
        for cat, count in sorted(report.issues_by_category.items()):
            lines.append(f"- {cat}: {count}")
        lines.append("")

        # Critical issues
        errors = [i for i in report.issues if i.severity == CheckSeverity.ERROR]
        if errors:
            lines.append("## Critical Issues (Errors)")
            for issue in errors[:20]:
                lines.append(f"\n### {issue.element_name} ({issue.element_id})")
                lines.append(f"- **Rule:** {issue.rule}")
                lines.append(f"- **Issue:** {issue.message}")
                lines.append(f"- **Fix:** {issue.suggestion}")

        return "\n".join(lines)
```

### Quick Start

```python
## Initialize checker
checker = BIMConsistencyChecker()

## Sample model elements
elements = [
    {
        'id': 'wall-001',
        'type': 'Wall',
        'name': 'INT-GYP-1HR',
        'level': 'Level 1',
        'parameters': {'Fire Rating': '1 Hour', 'Function': 'Interior'},
        'geometry': {'area': 50.5}
    },
    {
        'id': 'door-001',
        'type': 'Door',
        'name': '101',
        'level': 'Level 1',
        'host_id': 'wall-001',
        'parameters': {'Width': 36, 'Height': 84}
    }
]

## Run checks
report = checker.check_model(elements)

print(f"Pass Rate: {report.pass_rate:.1f}%")
print(f"Issues Found: {len(report.issues)}")

## Generate report
print(checker.generate_report(report))
```

### Dependencies

```bash
pip install (no external dependencies)
```


## ids-checker

> Check BIM data against IDS (Information Delivery Specification). Validate model information requirements and compliance.

## IDS Checker

### Business Case

#### Problem Statement
BIM data validation challenges:
- Inconsistent model information
- Missing required properties
- Non-compliant data deliveries
- Manual validation is time-consuming

#### Solution
Automated IDS (Information Delivery Specification) checking system to validate BIM models against defined requirements.

### Technical Implementation

```python
import pandas as pd
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import re


class RequirementType(Enum):
    PROPERTY = "property"
    CLASSIFICATION = "classification"
    MATERIAL = "material"
    ATTRIBUTE = "attribute"
    RELATION = "relation"


class Facet(Enum):
    ENTITY = "entity"
    PROPERTY_SET = "property_set"
    PROPERTY = "property"
    CLASSIFICATION = "classification"
    MATERIAL = "material"
    PART_OF = "part_of"


class Cardinality(Enum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    PROHIBITED = "prohibited"


class CheckResult(Enum):
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    NOT_APPLICABLE = "n/a"


@dataclass
class IDSRequirement:
    req_id: str
    name: str
    description: str
    applicability: Dict[str, Any]  # Which elements this applies to
    requirements: List[Dict[str, Any]]  # What is required
    cardinality: Cardinality = Cardinality.REQUIRED


@dataclass
class ValidationResult:
    element_id: str
    element_type: str
    requirement_id: str
    result: CheckResult
    message: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class IDSSpecification:
    spec_id: str
    name: str
    version: str
    purpose: str
    requirements: List[IDSRequirement] = field(default_factory=list)


class IDSChecker:
    """Check BIM data against IDS (Information Delivery Specification)."""

    def __init__(self, spec_name: str):
        self.spec_name = spec_name
        self.specifications: Dict[str, IDSSpecification] = {}
        self.results: List[ValidationResult] = []

    def create_specification(self, spec_id: str, name: str,
                             version: str = "1.0", purpose: str = "") -> IDSSpecification:
        """Create new IDS specification."""

        spec = IDSSpecification(
            spec_id=spec_id,
            name=name,
            version=version,
            purpose=purpose
        )
        self.specifications[spec_id] = spec
        return spec

    def add_requirement(self, spec_id: str, requirement: IDSRequirement):
        """Add requirement to specification."""

        if spec_id in self.specifications:
            self.specifications[spec_id].requirements.append(requirement)

    def add_property_requirement(self, spec_id: str, req_id: str, name: str,
                                  entity_type: str, property_set: str,
                                  property_name: str, data_type: str = None,
                                  value_pattern: str = None,
                                  cardinality: Cardinality = Cardinality.REQUIRED):
        """Add property requirement."""

        requirement = IDSRequirement(
            req_id=req_id,
            name=name,
            description=f"Property {property_name} in {property_set}",
            applicability={'entity': entity_type},
            requirements=[{
                'type': RequirementType.PROPERTY.value,
                'property_set': property_set,
                'property_name': property_name,
                'data_type': data_type,
                'value_pattern': value_pattern
            }],
            cardinality=cardinality
        )
        self.add_requirement(spec_id, requirement)

    def add_classification_requirement(self, spec_id: str, req_id: str, name: str,
                                        entity_type: str, system: str,
                                        value_pattern: str = None,
                                        cardinality: Cardinality = Cardinality.REQUIRED):
        """Add classification requirement."""

        requirement = IDSRequirement(
            req_id=req_id,
            name=name,
            description=f"Classification from {system}",
            applicability={'entity': entity_type},
            requirements=[{
                'type': RequirementType.CLASSIFICATION.value,
                'system': system,
                'value_pattern': value_pattern
            }],
            cardinality=cardinality
        )
        self.add_requirement(spec_id, requirement)

    def create_standard_cobie_spec(self) -> str:
        """Create standard COBie specification."""

        spec = self.create_specification(
            "COBIE_BASIC",
            "COBie Basic Requirements",
            "1.0",
            "Basic COBie data requirements for facility handover"
        )

        # Space requirements
        self.add_property_requirement("COBIE_BASIC", "CB-SP-01", "Space Name",
                                       "IfcSpace", "Pset_SpaceCommon", "Name")
        self.add_property_requirement("COBIE_BASIC", "CB-SP-02", "Space Number",
                                       "IfcSpace", "COBie_Space", "SpaceNumber")
        self.add_property_requirement("COBIE_BASIC", "CB-SP-03", "Room Tag",
                                       "IfcSpace", "COBie_Space", "RoomTag")

        # Component requirements
        self.add_property_requirement("COBIE_BASIC", "CB-CO-01", "Component Name",
                                       "IfcElement", "COBie_Component", "Name")
        self.add_property_requirement("COBIE_BASIC", "CB-CO-02", "Component Type",
                                       "IfcElement", "COBie_Component", "TypeName")
        self.add_property_requirement("COBIE_BASIC", "CB-CO-03", "Serial Number",
                                       "IfcElement", "COBie_Component", "SerialNumber",
                                       cardinality=Cardinality.OPTIONAL)

        # Type requirements
        self.add_property_requirement("COBIE_BASIC", "CB-TY-01", "Type Name",
                                       "IfcTypeObject", "COBie_Type", "Name")
        self.add_property_requirement("COBIE_BASIC", "CB-TY-02", "Manufacturer",
                                       "IfcTypeObject", "COBie_Type", "Manufacturer")
        self.add_property_requirement("COBIE_BASIC", "CB-TY-03", "Model Number",
                                       "IfcTypeObject", "COBie_Type", "ModelNumber")

        return "COBIE_BASIC"

    def create_standard_lod_spec(self, lod_level: int = 300) -> str:
        """Create standard LOD specification."""

        spec_id = f"LOD_{lod_level}"
        spec = self.create_specification(
            spec_id,
            f"LOD {lod_level} Requirements",
            "1.0",
            f"Level of Development {lod_level} requirements"
        )

        if lod_level >= 200:
            self.add_property_requirement(spec_id, f"LOD-{lod_level}-01",
                                           "Element must have type",
                                           "IfcElement", "Pset_ElementCommon", "Type")

        if lod_level >= 300:
            self.add_property_requirement(spec_id, f"LOD-{lod_level}-02",
                                           "Element must have dimensions",
                                           "IfcElement", "BaseQuantities", "Length")
            self.add_property_requirement(spec_id, f"LOD-{lod_level}-03",
                                           "Material assignment",
                                           "IfcElement", "Pset_MaterialCommon", "Material")

        if lod_level >= 350:
            self.add_property_requirement(spec_id, f"LOD-{lod_level}-04",
                                           "Fire rating",
                                           "IfcElement", "Pset_ElementCommon", "FireRating",
                                           cardinality=Cardinality.OPTIONAL)
            self.add_classification_requirement(spec_id, f"LOD-{lod_level}-05",
                                                 "Uniformat classification",
                                                 "IfcElement", "Uniformat")

        return spec_id

    def check_element(self, element: Dict[str, Any],
                      spec_id: str) -> List[ValidationResult]:
        """Check single element against specification."""

        results = []

        if spec_id not in self.specifications:
            return results

        spec = self.specifications[spec_id]

        for req in spec.requirements:
            # Check applicability
            if not self._matches_applicability(element, req.applicability):
                continue

            # Check requirements
            for req_def in req.requirements:
                result = self._check_requirement(element, req, req_def)
                results.append(result)

        return results

    def _matches_applicability(self, element: Dict[str, Any],
                                applicability: Dict[str, Any]) -> bool:
        """Check if element matches applicability criteria."""

        entity_filter = applicability.get('entity')
        if entity_filter:
            element_type = element.get('type', '')
            if entity_filter not in element_type:
                return False

        return True

    def _check_requirement(self, element: Dict[str, Any],
                           req: IDSRequirement,
                           req_def: Dict[str, Any]) -> ValidationResult:
        """Check single requirement."""

        req_type = req_def.get('type')

        if req_type == RequirementType.PROPERTY.value:
            return self._check_property_requirement(element, req, req_def)
        elif req_type == RequirementType.CLASSIFICATION.value:
            return self._check_classification_requirement(element, req, req_def)

        return ValidationResult(
            element_id=element.get('id', ''),
            element_type=element.get('type', ''),
            requirement_id=req.req_id,
            result=CheckResult.NOT_APPLICABLE,
            message="Unknown requirement type"
        )

    def _check_property_requirement(self, element: Dict[str, Any],
                                     req: IDSRequirement,
                                     req_def: Dict[str, Any]) -> ValidationResult:
        """Check property requirement."""

        pset_name = req_def.get('property_set')
        prop_name = req_def.get('property_name')
        value_pattern = req_def.get('value_pattern')

        # Get property value
        properties = element.get('properties', {})
        pset = properties.get(pset_name, {})
        value = pset.get(prop_name)

        result = ValidationResult(
            element_id=element.get('id', ''),
            element_type=element.get('type', ''),
            requirement_id=req.req_id,
            result=CheckResult.PASS,
            message="",
            details={'property_set': pset_name, 'property': prop_name, 'value': value}
        )

        # Check if property exists
        if value is None:
            if req.cardinality == Cardinality.REQUIRED:
                result.result = CheckResult.FAIL
                result.message = f"Missing required property: {pset_name}.{prop_name}"
            elif req.cardinality == Cardinality.PROHIBITED:
                result.result = CheckResult.PASS
                result.message = "Prohibited property correctly absent"
            else:
                result.result = CheckResult.WARNING
                result.message = f"Optional property missing: {pset_name}.{prop_name}"
            return result

        # Check if property should not exist
        if req.cardinality == Cardinality.PROHIBITED:
            result.result = CheckResult.FAIL
            result.message = f"Prohibited property exists: {pset_name}.{prop_name}"
            return result

        # Check value pattern
        if value_pattern:
            if not re.match(value_pattern, str(value)):
                result.result = CheckResult.FAIL
                result.message = f"Value '{value}' does not match pattern '{value_pattern}'"
                return result

        result.message = f"Property {prop_name} = {value}"
        return result

    def _check_classification_requirement(self, element: Dict[str, Any],
                                           req: IDSRequirement,
                                           req_def: Dict[str, Any]) -> ValidationResult:
        """Check classification requirement."""

        system = req_def.get('system')
        value_pattern = req_def.get('value_pattern')

        classifications = element.get('classifications', {})
        value = classifications.get(system)

        result = ValidationResult(
            element_id=element.get('id', ''),
            element_type=element.get('type', ''),
            requirement_id=req.req_id,
            result=CheckResult.PASS,
            message="",
            details={'system': system, 'value': value}
        )

        if value is None:
            if req.cardinality == Cardinality.REQUIRED:
                result.result = CheckResult.FAIL
                result.message = f"Missing classification: {system}"
            else:
                result.result = CheckResult.WARNING
                result.message = f"Optional classification missing: {system}"
            return result

        if value_pattern and not re.match(value_pattern, str(value)):
            result.result = CheckResult.FAIL
            result.message = f"Classification '{value}' does not match pattern"
            return result

        result.message = f"Classification {system} = {value}"
        return result

    def check_model(self, elements: List[Dict[str, Any]],
                    spec_id: str) -> Dict[str, Any]:
        """Check all elements against specification."""

        self.results = []

        for element in elements:
            element_results = self.check_element(element, spec_id)
            self.results.extend(element_results)

        # Summarize results
        pass_count = sum(1 for r in self.results if r.result == CheckResult.PASS)
        fail_count = sum(1 for r in self.results if r.result == CheckResult.FAIL)
        warning_count = sum(1 for r in self.results if r.result == CheckResult.WARNING)

        return {
            'specification': spec_id,
            'elements_checked': len(elements),
            'total_checks': len(self.results),
            'passed': pass_count,
            'failed': fail_count,
            'warnings': warning_count,
            'compliance_rate': round(pass_count / len(self.results) * 100, 1) if self.results else 0,
            'status': 'COMPLIANT' if fail_count == 0 else 'NON-COMPLIANT'
        }

    def get_failed_checks(self) -> List[Dict[str, Any]]:
        """Get list of failed checks."""

        return [
            {
                'element_id': r.element_id,
                'element_type': r.element_type,
                'requirement': r.requirement_id,
                'message': r.message,
                'details': r.details
            }
            for r in self.results if r.result == CheckResult.FAIL
        ]

    def export_to_excel(self, output_path: str) -> str:
        """Export validation results to Excel."""

        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Summary
            summary = {
                'Total Checks': len(self.results),
                'Passed': sum(1 for r in self.results if r.result == CheckResult.PASS),
                'Failed': sum(1 for r in self.results if r.result == CheckResult.FAIL),
                'Warnings': sum(1 for r in self.results if r.result == CheckResult.WARNING)
            }
            summary_df = pd.DataFrame([summary])
            summary_df.to_excel(writer, sheet_name='Summary', index=False)

            # All results
            results_df = pd.DataFrame([{
                'Element ID': r.element_id,
                'Element Type': r.element_type,
                'Requirement': r.requirement_id,
                'Result': r.result.value,
                'Message': r.message
            } for r in self.results])
            results_df.to_excel(writer, sheet_name='All Results', index=False)

            # Failed only
            failed_df = pd.DataFrame(self.get_failed_checks())
            if not failed_df.empty:
                failed_df.to_excel(writer, sheet_name='Failed', index=False)

        return output_path
```

### Quick Start

```python
## Create IDS checker
checker = IDSChecker("Project BIM Validation")

## Create COBie specification
cobie_spec = checker.create_standard_cobie_spec()

## Sample BIM elements
elements = [
    {
        'id': 'Space_001',
        'type': 'IfcSpace',
        'properties': {
            'Pset_SpaceCommon': {'Name': 'Office 101'},
            'COBie_Space': {'SpaceNumber': 'SP-101', 'RoomTag': 'A101'}
        }
    },
    {
        'id': 'Door_001',
        'type': 'IfcDoor',
        'properties': {
            'COBie_Component': {'Name': 'Door 1', 'TypeName': 'Single Door'}
        }
    }
]

## Check model
results = checker.check_model(elements, cobie_spec)
print(f"Compliance: {results['compliance_rate']}%")
print(f"Status: {results['status']}")
```

### Common Use Cases

#### 1. LOD Validation
```python
lod_spec = checker.create_standard_lod_spec(350)
results = checker.check_model(elements, lod_spec)
```

#### 2. Custom Requirement
```python
checker.add_property_requirement(
    "COBIE_BASIC", "CB-CUSTOM-01", "Fire Rating Required",
    "IfcWall", "Pset_WallCommon", "FireRating",
    value_pattern=r"^\d+\s*hr$"
)
```

#### 3. Get Failed Items
```python
failed = checker.get_failed_checks()
for item in failed:
    print(f"{item['element_id']}: {item['message']}")
```

### Resources
- **DDC Book**: Chapter 4.3 - Automated ETL Pipeline for Data Validation
- **buildingSMART IDS**: https://technical.buildingsmart.org/projects/information-delivery-specification-ids/
- **Website**: https://datadrivenconstruction.io


## bim-validation-report

> Generate comprehensive BIM model validation reports. Check data quality, completeness, and compliance with standards.

## BIM Validation Report Generator

### Business Case

#### Problem Statement
BIM models often have quality issues:
- Missing required properties
- Invalid or inconsistent data
- Non-compliant with project standards
- Incomplete model information

#### Solution
Automated BIM validation system that checks models against configurable rules and generates detailed compliance reports.

#### Business Value
- **Quality assurance** - Catch issues early
- **Standards compliance** - Meet project requirements
- **Automation** - Reduce manual QC effort
- **Transparency** - Clear validation results

### Technical Implementation

```python
import pandas as pd
from datetime import datetime
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum


class ValidationSeverity(Enum):
    """Validation issue severity."""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class ValidationStatus(Enum):
    """Overall validation status."""
    PASSED = "passed"
    PASSED_WITH_WARNINGS = "passed_with_warnings"
    FAILED = "failed"


class RuleCategory(Enum):
    """Validation rule categories."""
    REQUIRED_PROPERTIES = "required_properties"
    DATA_FORMAT = "data_format"
    NAMING_CONVENTION = "naming_convention"
    GEOMETRIC = "geometric"
    CLASSIFICATION = "classification"
    RELATIONSHIPS = "relationships"


@dataclass
class ValidationRule:
    """Single validation rule."""
    rule_id: str
    name: str
    category: RuleCategory
    description: str
    severity: ValidationSeverity
    check_function: Callable
    applicable_categories: List[str] = field(default_factory=list)
    enabled: bool = True


@dataclass
class ValidationIssue:
    """Single validation issue."""
    issue_id: str
    rule_id: str
    rule_name: str
    element_id: str
    element_name: str
    element_category: str
    severity: ValidationSeverity
    message: str
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'issue_id': self.issue_id,
            'rule_id': self.rule_id,
            'rule_name': self.rule_name,
            'element_id': self.element_id,
            'element_name': self.element_name,
            'element_category': self.element_category,
            'severity': self.severity.value,
            'message': self.message
        }


@dataclass
class ValidationReport:
    """Complete validation report."""
    project_name: str
    model_name: str
    validated_at: datetime
    status: ValidationStatus
    total_elements: int
    elements_with_issues: int
    issues: List[ValidationIssue]
    rules_checked: int
    summary_by_severity: Dict[str, int]
    summary_by_category: Dict[str, int]


class BIMValidationEngine:
    """BIM model validation engine."""

    def __init__(self, project_name: str, model_name: str):
        self.project_name = project_name
        self.model_name = model_name
        self.rules: List[ValidationRule] = []
        self.issues: List[ValidationIssue] = []
        self._issue_counter = 0

        # Load default rules
        self._load_default_rules()

    def _load_default_rules(self):
        """Load standard validation rules."""

        # Required properties rules
        self.add_rule(ValidationRule(
            rule_id="REQ-001",
            name="Element Name Required",
            category=RuleCategory.REQUIRED_PROPERTIES,
            description="All elements must have a name",
            severity=ValidationSeverity.ERROR,
            check_function=lambda e: bool(e.get('name'))
        ))

        self.add_rule(ValidationRule(
            rule_id="REQ-002",
            name="Level Assignment Required",
            category=RuleCategory.REQUIRED_PROPERTIES,
            description="Elements must be assigned to a level",
            severity=ValidationSeverity.WARNING,
            check_function=lambda e: bool(e.get('level')),
            applicable_categories=["Walls", "Floors", "Doors", "Windows"]
        ))

        self.add_rule(ValidationRule(
            rule_id="REQ-003",
            name="Material Required",
            category=RuleCategory.REQUIRED_PROPERTIES,
            description="Structural elements must have material defined",
            severity=ValidationSeverity.ERROR,
            check_function=lambda e: bool(e.get('material')),
            applicable_categories=["Structural Columns", "Structural Framing", "Floors"]
        ))

        # Naming convention rules
        self.add_rule(ValidationRule(
            rule_id="NAM-001",
            name="No Special Characters",
            category=RuleCategory.NAMING_CONVENTION,
            description="Names should not contain special characters",
            severity=ValidationSeverity.WARNING,
            check_function=self._check_no_special_chars
        ))

        self.add_rule(ValidationRule(
            rule_id="NAM-002",
            name="Name Length Check",
            category=RuleCategory.NAMING_CONVENTION,
            description="Names should be between 3 and 100 characters",
            severity=ValidationSeverity.INFO,
            check_function=lambda e: 3 <= len(e.get('name', '')) <= 100
        ))

        # Classification rules
        self.add_rule(ValidationRule(
            rule_id="CLS-001",
            name="Classification Code Present",
            category=RuleCategory.CLASSIFICATION,
            description="Elements should have classification code",
            severity=ValidationSeverity.WARNING,
            check_function=lambda e: bool(e.get('classification_code') or e.get('uniformat'))
        ))

        # Geometric rules
        self.add_rule(ValidationRule(
            rule_id="GEO-001",
            name="Non-Zero Volume",
            category=RuleCategory.GEOMETRIC,
            description="3D elements must have non-zero volume",
            severity=ValidationSeverity.ERROR,
            check_function=lambda e: float(e.get('volume', 0)) > 0,
            applicable_categories=["Walls", "Floors", "Structural Columns", "Structural Framing"]
        ))

        self.add_rule(ValidationRule(
            rule_id="GEO-002",
            name="Valid Bounding Box",
            category=RuleCategory.GEOMETRIC,
            description="Elements must have valid bounding box",
            severity=ValidationSeverity.ERROR,
            check_function=self._check_valid_bbox
        ))

    def _check_no_special_chars(self, element: Dict[str, Any]) -> bool:
        """Check name for special characters."""
        import re
        name = element.get('name', '')
        return bool(re.match(r'^[\w\s\-\.]+$', name))

    def _check_valid_bbox(self, element: Dict[str, Any]) -> bool:
        """Check for valid bounding box."""
        try:
            min_x = float(element.get('min_x', 0))
            max_x = float(element.get('max_x', 0))
            min_y = float(element.get('min_y', 0))
            max_y = float(element.get('max_y', 0))
            min_z = float(element.get('min_z', 0))
            max_z = float(element.get('max_z', 0))
            return max_x > min_x and max_y > min_y and max_z > min_z
        except (ValueError, TypeError):
            return False

    def add_rule(self, rule: ValidationRule):
        """Add validation rule."""
        self.rules.append(rule)

    def add_custom_rule(self, rule_id: str, name: str, category: RuleCategory,
                       check_function: Callable, severity: ValidationSeverity = ValidationSeverity.WARNING,
                       description: str = "", categories: List[str] = None):
        """Add custom validation rule."""
        rule = ValidationRule(
            rule_id=rule_id,
            name=name,
            category=category,
            description=description,
            severity=severity,
            check_function=check_function,
            applicable_categories=categories or []
        )
        self.add_rule(rule)

    def validate_element(self, element: Dict[str, Any]) -> List[ValidationIssue]:
        """Validate single element against all rules."""
        issues = []
        element_category = element.get('category', '')

        for rule in self.rules:
            if not rule.enabled:
                continue

            # Check if rule applies to this category
            if rule.applicable_categories and element_category not in rule.applicable_categories:
                continue

            try:
                passed = rule.check_function(element)
                if not passed:
                    self._issue_counter += 1
                    issue = ValidationIssue(
                        issue_id=f"ISS-{self._issue_counter:05d}",
                        rule_id=rule.rule_id,
                        rule_name=rule.name,
                        element_id=str(element.get('element_id', '')),
                        element_name=str(element.get('name', '')),
                        element_category=element_category,
                        severity=rule.severity,
                        message=rule.description
                    )
                    issues.append(issue)
            except Exception as e:
                # Rule check failed
                self._issue_counter += 1
                issue = ValidationIssue(
                    issue_id=f"ISS-{self._issue_counter:05d}",
                    rule_id=rule.rule_id,
                    rule_name=rule.name,
                    element_id=str(element.get('element_id', '')),
                    element_name=str(element.get('name', '')),
                    element_category=element_category,
                    severity=ValidationSeverity.ERROR,
                    message=f"Rule check error: {str(e)}"
                )
                issues.append(issue)

        return issues

    def validate_model(self, elements_df: pd.DataFrame) -> ValidationReport:
        """Validate entire BIM model."""
        self.issues = []
        elements_with_issues = set()

        for _, row in elements_df.iterrows():
            element = row.to_dict()
            element_issues = self.validate_element(element)

            if element_issues:
                elements_with_issues.add(element.get('element_id'))
                self.issues.extend(element_issues)

        # Calculate summaries
        summary_by_severity = {
            'error': sum(1 for i in self.issues if i.severity == ValidationSeverity.ERROR),
            'warning': sum(1 for i in self.issues if i.severity == ValidationSeverity.WARNING),
            'info': sum(1 for i in self.issues if i.severity == ValidationSeverity.INFO)
        }

        summary_by_category = {}
        for issue in self.issues:
            cat = issue.element_category
            summary_by_category[cat] = summary_by_category.get(cat, 0) + 1

        # Determine overall status
        if summary_by_severity['error'] > 0:
            status = ValidationStatus.FAILED
        elif summary_by_severity['warning'] > 0:
            status = ValidationStatus.PASSED_WITH_WARNINGS
        else:
            status = ValidationStatus.PASSED

        return ValidationReport(
            project_name=self.project_name,
            model_name=self.model_name,
            validated_at=datetime.now(),
            status=status,
            total_elements=len(elements_df),
            elements_with_issues=len(elements_with_issues),
            issues=self.issues,
            rules_checked=len([r for r in self.rules if r.enabled]),
            summary_by_severity=summary_by_severity,
            summary_by_category=summary_by_category
        )

    def export_report(self, report: ValidationReport, output_path: str):
        """Export validation report to Excel."""
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Summary sheet
            summary_data = {
                'Metric': ['Project', 'Model', 'Validated At', 'Status',
                          'Total Elements', 'Elements with Issues', 'Rules Checked',
                          'Errors', 'Warnings', 'Info'],
                'Value': [report.project_name, report.model_name,
                         report.validated_at.isoformat(), report.status.value,
                         report.total_elements, report.elements_with_issues,
                         report.rules_checked, report.summary_by_severity['error'],
                         report.summary_by_severity['warning'], report.summary_by_severity['info']]
            }
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='Summary', index=False)

            # Issues sheet
            issues_df = pd.DataFrame([i.to_dict() for i in report.issues])
            if not issues_df.empty:
                issues_df.to_excel(writer, sheet_name='Issues', index=False)

            # By Category sheet
            cat_df = pd.DataFrame([
                {'Category': k, 'Issue Count': v}
                for k, v in report.summary_by_category.items()
            ])
            if not cat_df.empty:
                cat_df.to_excel(writer, sheet_name='By Category', index=False)

        return output_path


def generate_validation_report(elements_df: pd.DataFrame,
                               project_name: str,
                               model_name: str,
                               output_path: str = None) -> ValidationReport:
    """Quick function to generate validation report."""
    engine = BIMValidationEngine(project_name, model_name)
    report = engine.validate_model(elements_df)

    if output_path:
        engine.export_report(report, output_path)

    return report
```

### Quick Start

```python
## Load BIM elements
elements = pd.read_excel("bim_elements.xlsx")

## Run validation
report = generate_validation_report(
    elements,
    project_name="Office Tower",
    model_name="Architectural Model v3.2",
    output_path="validation_report.xlsx"
)

print(f"Status: {report.status.value}")
print(f"Errors: {report.summary_by_severity['error']}")
print(f"Warnings: {report.summary_by_severity['warning']}")
```

### Common Use Cases

#### 1. Custom Validation Rules
```python
engine = BIMValidationEngine("Project", "Model")

## Add custom rule
engine.add_custom_rule(
    rule_id="CUSTOM-001",
    name="Fire Rating Required",
    category=RuleCategory.REQUIRED_PROPERTIES,
    check_function=lambda e: bool(e.get('fire_rating')),
    severity=ValidationSeverity.ERROR,
    categories=["Walls", "Doors"]
)
```

#### 2. Filter Issues
```python
## Get only errors
errors = [i for i in report.issues if i.severity == ValidationSeverity.ERROR]

## Get issues for specific category
wall_issues = [i for i in report.issues if i.element_category == "Walls"]
```

#### 3. Automated QC Pipeline
```python
report = engine.validate_model(elements)
if report.status == ValidationStatus.FAILED:
    send_notification("BIM validation failed", report.summary_by_severity)
```

### Resources
- **DDC Book**: Chapter 4.3 - BIM Validation
- **Reference**: ISO 19650, buildingSMART IDS


---

# Automation


## bim-visual-programming-automation

> Automate BIM workflows using visual programming and Python. Create parametric schedules, export data, batch modify elements, and integrate with external data sources.

## BIM Visual Programming Automation

### Overview

This skill provides visual programming scripts and Python nodes for automating BIM workflows. Extract data, modify elements in batch, generate schedules, and integrate with external systems.

> **Note:** Examples use Autodesk® Revit® and Dynamo™ APIs. Autodesk, Revit, and Dynamo are registered trademarks of Autodesk, Inc.

**Key Capabilities:**
- Batch element modification
- Data export/import
- Schedule generation
- Parameter management
- External data integration
- Automated QTO

### Quick Start (Dynamo Python)

```python
## Dynamo Python Script - Export all walls to Excel
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

## Get all walls
collector = FilteredElementCollector(doc)
walls = collector.OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

## Extract data
wall_data = []
for wall in walls:
    wall_data.append({
        'id': wall.Id.IntegerValue,
        'name': wall.Name,
        'length': wall.get_Parameter(BuiltInParameter.CURVE_ELEM_LENGTH).AsDouble() * 0.3048,
        'area': wall.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsDouble() * 0.0929
    })

OUT = wall_data
```

### Element Data Extraction

#### Comprehensive Element Extractor

```python
## Dynamo Python Node - Extract all element data
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
clr.AddReference('RevitNodes')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import *
import Revit
clr.ImportExtensions(Revit.Elements)

doc = DocumentManager.Instance.CurrentDBDocument

def get_element_data(element):
    """Extract data from Revit element"""
    data = {
        'id': element.Id.IntegerValue,
        'category': element.Category.Name if element.Category else None,
        'name': element.Name,
        'level': None,
        'parameters': {}
    }

    # Get level
    level_param = element.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM)
    if level_param:
        level_id = level_param.AsElementId()
        if level_id.IntegerValue > 0:
            level = doc.GetElement(level_id)
            data['level'] = level.Name if level else None

    # Get all parameters
    for param in element.Parameters:
        try:
            if param.HasValue:
                if param.StorageType == StorageType.Double:
                    data['parameters'][param.Definition.Name] = param.AsDouble()
                elif param.StorageType == StorageType.Integer:
                    data['parameters'][param.Definition.Name] = param.AsInteger()
                elif param.StorageType == StorageType.String:
                    data['parameters'][param.Definition.Name] = param.AsString()
        except:
            pass

    return data

def extract_category(category_enum):
    """Extract all elements of a category"""
    collector = FilteredElementCollector(doc)
    elements = collector.OfCategory(category_enum).WhereElementIsNotElementType().ToElements()
    return [get_element_data(e) for e in elements]

## Extract structural elements
categories = [
    BuiltInCategory.OST_Walls,
    BuiltInCategory.OST_Floors,
    BuiltInCategory.OST_StructuralColumns,
    BuiltInCategory.OST_StructuralFraming,
    BuiltInCategory.OST_Doors,
    BuiltInCategory.OST_Windows
]

all_data = {}
for cat in categories:
    cat_name = cat.ToString().replace('OST_', '')
    all_data[cat_name] = extract_category(cat)

OUT = all_data
```

#### Quantity Take-Off Script

```python
## Dynamo Python - QTO Export
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

def get_qto_data():
    """Generate QTO data from model"""
    qto = {}

    # Walls
    walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)\
        .WhereElementIsNotElementType().ToElements()

    wall_qto = {}
    for wall in walls:
        wall_type = doc.GetElement(wall.GetTypeId())
        type_name = wall_type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()

        if type_name not in wall_qto:
            wall_qto[type_name] = {'count': 0, 'area': 0, 'length': 0}

        wall_qto[type_name]['count'] += 1

        area_param = wall.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED)
        if area_param:
            wall_qto[type_name]['area'] += area_param.AsDouble() * 0.0929  # sqft to m2

        length_param = wall.get_Parameter(BuiltInParameter.CURVE_ELEM_LENGTH)
        if length_param:
            wall_qto[type_name]['length'] += length_param.AsDouble() * 0.3048  # ft to m

    qto['Walls'] = wall_qto

    # Floors
    floors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors)\
        .WhereElementIsNotElementType().ToElements()

    floor_qto = {}
    for floor in floors:
        floor_type = doc.GetElement(floor.GetTypeId())
        type_name = floor_type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()

        if type_name not in floor_qto:
            floor_qto[type_name] = {'count': 0, 'area': 0, 'volume': 0}

        floor_qto[type_name]['count'] += 1

        area_param = floor.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED)
        if area_param:
            floor_qto[type_name]['area'] += area_param.AsDouble() * 0.0929

        vol_param = floor.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED)
        if vol_param:
            floor_qto[type_name]['volume'] += vol_param.AsDouble() * 0.0283  # cuft to m3

    qto['Floors'] = floor_qto

    return qto

OUT = get_qto_data()
```

### Batch Modification

#### Batch Parameter Update

```python
## Dynamo Python - Batch update parameters
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

def batch_update_parameter(elements, param_name, values):
    """Update parameter for multiple elements"""
    TransactionManager.Instance.EnsureInTransaction(doc)

    results = []
    for elem, value in zip(elements, values):
        try:
            param = elem.LookupParameter(param_name)
            if param and not param.IsReadOnly:
                if param.StorageType == StorageType.String:
                    param.Set(str(value))
                elif param.StorageType == StorageType.Double:
                    param.Set(float(value))
                elif param.StorageType == StorageType.Integer:
                    param.Set(int(value))
                results.append(True)
            else:
                results.append(False)
        except Exception as e:
            results.append(str(e))

    TransactionManager.Instance.TransactionTaskDone()
    return results

## Input from Dynamo nodes
elements = IN[0]  # List of elements
param_name = IN[1]  # Parameter name (string)
values = IN[2]  # List of values

OUT = batch_update_parameter(elements, param_name, values)
```

#### Batch Copy Elements

```python
## Dynamo Python - Copy elements to levels
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import *
from System.Collections.Generic import List

doc = DocumentManager.Instance.CurrentDBDocument

def copy_to_levels(elements, target_levels):
    """Copy elements to multiple levels"""
    TransactionManager.Instance.EnsureInTransaction(doc)

    copied = []
    element_ids = List[ElementId]([e.Id for e in elements])

    for level in target_levels:
        # Calculate offset
        source_level = doc.GetElement(elements[0].LevelId)
        offset = XYZ(0, 0, level.Elevation - source_level.Elevation)

        # Copy
        new_ids = ElementTransformUtils.CopyElements(
            doc, element_ids, offset
        )

        copied.extend([doc.GetElement(id) for id in new_ids])

    TransactionManager.Instance.TransactionTaskDone()
    return copied

elements = IN[0]
target_levels = IN[1]

OUT = copy_to_levels(elements, target_levels)
```

### Schedule Generation

#### Create Custom Schedule

```python
## Dynamo Python - Create view schedule
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

def create_wall_schedule(schedule_name):
    """Create a wall schedule with QTO fields"""
    TransactionManager.Instance.EnsureInTransaction(doc)

    # Create schedule
    schedule = ViewSchedule.CreateSchedule(
        doc,
        ElementId(BuiltInCategory.OST_Walls)
    )
    schedule.Name = schedule_name

    # Add fields
    definition = schedule.Definition
    schedulable = definition.GetSchedulableFields()

    # Find and add specific fields
    field_names = ['Type', 'Level', 'Length', 'Area', 'Volume']

    for sf in schedulable:
        if sf.GetName(doc) in field_names:
            definition.AddField(sf)

    # Add sorting/grouping
    type_field = None
    for field in definition.GetFieldOrder():
        if definition.GetField(field).GetName() == 'Type':
            type_field = field
            break

    if type_field:
        sorting = ScheduleSortGroupField(type_field, ScheduleSortOrder.Ascending)
        sorting.ShowHeader = True
        sorting.ShowFooter = True
        definition.AddSortGroupField(sorting)

    TransactionManager.Instance.TransactionTaskDone()
    return schedule

schedule_name = IN[0]
OUT = create_wall_schedule(schedule_name)
```

### External Data Integration

#### Import Data from Excel

```python
## Dynamo Python - Import Excel and update Revit
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import *

## Requires Excel data as input from Dynamo Excel nodes
doc = DocumentManager.Instance.CurrentDBDocument

def update_from_excel(excel_data, id_column, param_columns):
    """Update Revit elements from Excel data"""
    TransactionManager.Instance.EnsureInTransaction(doc)

    results = []

    for row in excel_data:
        try:
            # Get element by ID
            elem_id = ElementId(int(row[id_column]))
            element = doc.GetElement(elem_id)

            if element:
                row_result = {'id': elem_id.IntegerValue, 'updates': {}}

                for col_name, col_index in param_columns.items():
                    param = element.LookupParameter(col_name)
                    if param and not param.IsReadOnly:
                        value = row[col_index]
                        if param.StorageType == StorageType.String:
                            param.Set(str(value))
                        elif param.StorageType == StorageType.Double:
                            param.Set(float(value))
                        row_result['updates'][col_name] = value

                results.append(row_result)
        except Exception as e:
            results.append({'error': str(e)})

    TransactionManager.Instance.TransactionTaskDone()
    return results

excel_data = IN[0]  # 2D list from Excel
id_column = IN[1]   # Column index for element ID
param_columns = IN[2]  # Dict: param_name -> column_index

OUT = update_from_excel(excel_data, id_column, param_columns)
```

### Dynamo Package Workflow

#### Full QTO Pipeline (Dynamo Graph Nodes)

```
1. Categories (Input)
   |
2. All Elements of Category (Revit)
   |
3. Element.GetParameterValueByName (Multiple parameters)
   |
4. Python Script (Process and calculate)
   |
5. List.Transpose
   |
6. Data.ExportExcel
   |
7. File Path (Output)
```

### Quick Reference

| Task | Method | Performance |
|------|--------|-------------|
| Get Elements | FilteredElementCollector | Fast |
| Get Parameter | element.LookupParameter() | Fast |
| Set Parameter | TransactionManager required | Moderate |
| Copy Elements | ElementTransformUtils | Moderate |
| Create Views | ViewSchedule.CreateSchedule | Slow |
| Delete Elements | Document.Delete | Fast |

### Common Parameter Names

```python
## Built-in parameters for quantities
QUANTITY_PARAMS = {
    'Length': BuiltInParameter.CURVE_ELEM_LENGTH,
    'Area': BuiltInParameter.HOST_AREA_COMPUTED,
    'Volume': BuiltInParameter.HOST_VOLUME_COMPUTED,
    'Height': BuiltInParameter.WALL_USER_HEIGHT_PARAM,
    'Width': BuiltInParameter.DOOR_WIDTH,
    'Level': BuiltInParameter.SCHEDULE_LEVEL_PARAM
}

## Unit conversion (Imperial to Metric)
CONVERSIONS = {
    'feet_to_meters': 0.3048,
    'sqft_to_sqm': 0.0929,
    'cuft_to_cum': 0.0283
}
```

### Resources

- **Dynamo Primer**: https://primer.dynamobim.org
- **Revit API Docs**: https://www.revitapidocs.com
- **DDC Website**: https://datadrivenconstruction.io

### Next Steps

- See `ifc-data-extraction` for IFC export
- See `qto-report` for advanced quantity reports
- See `n8n-workflow-automation` for external integration
