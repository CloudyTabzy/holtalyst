# Holtalyst

Workflow tools for Blender — cleanup, selection, lighting, optimization, batch rename, render presets, export, and scene snapshots.

## Features

### Cleanup
- **Organize Outliner** — Auto-sort objects into collections by type (Cameras, Lights, Meshes, etc.)
- **Convert Suffixes** — Convert `.001` style suffixes to `_1` format
- **Purge Unused Data** — Remove orphaned meshes, materials, textures, images
- **Deep Clean** — Organize + convert suffixes in one click
- **Auto Smooth** — Set auto smooth angle on selected objects
- **Sync Mesh Names** — Match mesh data names to object names
- **Remove Unused Material Slots** — Clean empty material slots
- **Fix Duplicate Node Groups** — Re-link duplicated node groups to originals

### Selection
- **Select All Including** — Select objects by name substring (case-sensitive option)
- **Select By Type** — Select all objects of a given type (Mesh, Light, Camera, etc.)
- **Select By Vertex Count** — Select objects above/below/equal to a vertex threshold
- **Form Collections** — Create collections from any selection query
- **Tag Objects** — Add prefixes or suffixes with custom delimiters

### Batch Rename
- **Find & Replace** — Rename objects, materials, meshes, or collections
- **Add Prefix / Suffix** — Batch tag selected objects
- **Rename with Numbering** — Sequential naming with configurable start/step
- **Strip Trailing Numbers** — Remove `.001`, `.002` suffixes
- **Sync Data Names** — Match data blocks to their object names

### Lighting
- **Add / Subtract / Multiply Intensity** — Global light power control
- **Target Modes** — Light objects, emissive materials, or both
- **Set / Randomize Light Color** — Apply or randomize RGB on selected lights

### Render Presets
- **Save / Load / Delete Presets** — Named render settings stored as JSON
- **Quick Render** — Render current frame or full animation from the sidebar
- **Settings Overview** — See engine, resolution, and frame range at a glance

### Batch Export
- **Export Selected Objects** — Each object as a separate file
- **Export Collections** — Each collection as a separate file
- **Formats** — OBJ, glTF (.glb), FBX, STL
- **Apply Transforms** — Optional transform application before export

### Scene Snapshots
- **Save Snapshot** — Capture visibility, transforms, modifiers, cursor position
- **Load Snapshot** — Restore any saved state
- **Delete Snapshot** — Remove saved snapshots

### Optimization
- **Quick Decimate** — Decimate selected objects with configurable ratio

### World
- **Toggle World Volume** — Mute/unmute volume shaders in world nodes

## Compatibility

| Blender Version | Status |
|---|---|
| 4.2 LTS | ✅ Supported |
| 4.3 | ✅ Supported |
| 4.4 | ✅ Supported |
| 4.5 LTS | ✅ Supported |
| 5.0 | ✅ Supported |
| 5.1 | ✅ Supported |
| 5.2 | ✅ Supported |

Version-specific differences (EEVEE engine identifier, Grease Pencil types) are handled automatically via the compatibility layer.

## Installation

### From GitHub
1. Download the latest release or clone this repository
2. In Blender: **Edit → Preferences → Get Extensions**
3. Click the dropdown arrow → **Install from Disk**
4. Select the `holtalyst` folder or `.zip` file
5. Enable **Holtalyst** in the addon list

### From Extensions Platform
1. In Blender: **Edit → Preferences → Get Extensions**
2. Search for **Holtalyst**
3. Click **Install**

## Usage

Open the **3D Viewport Sidebar** (press `N`) and look for the **Holtalyst** tab.

## Project Structure

```
holtalyst/
├── __init__.py              # Addon entry point
├── blender_manifest.toml    # Extension manifest
├── compat.py                # Version compatibility layer
├── preferences.py           # AddonPreferences (persistent settings)
├── properties.py            # Scene properties
├── utils/                   # Utility modules
│   ├── common.py            # Core helpers
│   ├── render.py            # Render settings
│   ├── objects.py           # Object operations
│   ├── selection.py         # Selection helpers
│   ├── collections.py       # Collection management
│   ├── materials.py         # Material operations
│   ├── nodes.py             # Node helpers
│   ├── modifiers.py         # Modifier shortcuts
│   ├── lighting.py          # Light controls
│   ├── transforms.py        # Transform operations
│   ├── animation.py         # Keyframes & drivers
│   ├── mesh.py              # Mesh & shape keys
│   ├── cursor.py            # 3D cursor & pivot
│   ├── textures.py          # Texture & image ops
│   ├── physics.py           # Physics helpers
│   ├── presets.py           # JSON preset save/load
│   ├── rename.py            # Batch rename logic
│   └── export.py            # Batch export helpers
├── operators/               # Blender operators
│   ├── cleanup.py
│   ├── selection.py
│   ├── lighting.py
│   ├── optimization.py
│   ├── world.py
│   ├── rename.py
│   ├── render_presets.py
│   ├── export.py
│   └── snapshots.py
└── panels/                  # UI panels
    ├── cleanup.py
    ├── selection.py
    ├── lighting.py
    ├── optimization.py
    ├── interface.py
    ├── world.py
    ├── rename.py
    ├── render_presets.py
    ├── export.py
    └── snapshots.py
```

## License

[GPL-3.0-or-later](LICENSE)

## Credits

Originally created by Curtis Holt as **Holt Tools**.
Maintained by CloudyTabzy.
