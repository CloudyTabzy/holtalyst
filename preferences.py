import bpy
from bpy.types import AddonPreferences
from bpy.props import (
    StringProperty,
    BoolProperty,
    FloatProperty,
    EnumProperty,
)


class HOLTALYST_Preferences(AddonPreferences):
    bl_idname = "holtalyst"

    default_export_path: StringProperty(
        name="Default Export Path",
        description="Default directory for batch exports",
        subtype='DIR_PATH',
        default="//exports/",
    )
    default_export_format: EnumProperty(
        name="Default Export Format",
        description="Default format for batch exports",
        items=[
            ('GLTF', "glTF 2.0 (.glb)", ""),
            ('FBX', "FBX (.fbx)", ""),
            ('OBJ', "Wavefront (.obj)", ""),
            ('STL', "STL (.stl)", ""),
        ],
        default='GLTF',
    )
    apply_transforms_on_export: BoolProperty(
        name="Apply Transforms on Export",
        description="Automatically apply transforms before exporting",
        default=True,
    )
    preset_autosave: BoolProperty(
        name="Auto-save Presets",
        description="Automatically save presets when modified",
        default=True,
    )
    show_snapshot_notifications: BoolProperty(
        name="Snapshot Notifications",
        description="Show notifications when saving/loading snapshots",
        default=True,
    )
    autosmooth_default_angle: FloatProperty(
        name="Default Auto Smooth Angle",
        description="Default angle for auto smooth operations",
        default=60.0,
        min=0.0,
        max=180.0,
    )

    show_cleanup: BoolProperty(name="Cleanup", default=True, description="Show Cleanup panel")
    show_selection: BoolProperty(name="Selection", default=True, description="Show Selection panel")
    show_rename: BoolProperty(name="Batch Rename", default=True, description="Show Batch Rename panel")
    show_lighting: BoolProperty(name="Lighting", default=True, description="Show Lighting panel")
    show_optimization: BoolProperty(name="Optimization", default=True, description="Show Optimization panel")
    show_interface: BoolProperty(name="Interface", default=True, description="Show Interface panel")
    show_world: BoolProperty(name="World", default=True, description="Show World panel")
    show_world_hdri: BoolProperty(name="World / HDRI", default=True, description="Show World/HDRI panel")
    show_render_presets: BoolProperty(name="Render Presets", default=True, description="Show Render Presets panel")
    show_export: BoolProperty(name="Batch Export", default=True, description="Show Batch Export panel")
    show_snapshots: BoolProperty(name="Scene Snapshots", default=True, description="Show Scene Snapshots panel")
    show_transforms: BoolProperty(name="Smart Transforms", default=True, description="Show Smart Transforms panel")
    show_material_batch: BoolProperty(name="Material Batch Tools", default=True, description="Show Material Batch Tools panel")
    show_viewport: BoolProperty(name="Viewport Display", default=True, description="Show Viewport Display panel")
    show_visibility: BoolProperty(name="Visibility Sets", default=True, description="Show Visibility Sets panel")
    show_cameras: BoolProperty(name="Camera Manager", default=True, description="Show Camera Manager panel")
    show_collection_templates: BoolProperty(name="Collection Templates", default=True, description="Show Collection Templates panel")
    show_mesh_stats: BoolProperty(name="Mesh Statistics", default=True, description="Show Mesh Statistics panel")
    show_modifier_presets: BoolProperty(name="Modifier Presets", default=True, description="Show Modifier Presets panel")
    show_normals: BoolProperty(name="Normal Tools", default=True, description="Show Normal Tools panel")

    def draw(self, context):
        layout = self.layout

        layout.label(text="Panel Visibility", icon='RESTRICT_VIEW_OFF')
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Toggle which panels appear in the sidebar:", icon='PREFERENCES')

        col.separator()
        col.label(text="Core Tools", icon='TOOL_SETTINGS')
        row = col.row(align=True)
        row.prop(self, "show_cleanup", toggle=True)
        row.prop(self, "show_selection", toggle=True)
        row.prop(self, "show_rename", toggle=True)
        row = col.row(align=True)
        row.prop(self, "show_lighting", toggle=True)
        row.prop(self, "show_optimization", toggle=True)
        row.prop(self, "show_interface", toggle=True)

        col.separator()
        col.label(text="Scene & Rendering", icon='SCENE_DATA')
        row = col.row(align=True)
        row.prop(self, "show_world", toggle=True)
        row.prop(self, "show_world_hdri", toggle=True)
        row.prop(self, "show_render_presets", toggle=True)
        row = col.row(align=True)
        row.prop(self, "show_export", toggle=True)
        row.prop(self, "show_snapshots", toggle=True)
        row.prop(self, "show_cameras", toggle=True)

        col.separator()
        col.label(text="Object Tools", icon='OBJECT_DATA')
        row = col.row(align=True)
        row.prop(self, "show_transforms", toggle=True)
        row.prop(self, "show_material_batch", toggle=True)
        row.prop(self, "show_normals", toggle=True)
        row = col.row(align=True)
        row.prop(self, "show_viewport", toggle=True)
        row.prop(self, "show_visibility", toggle=True)
        row.prop(self, "show_collection_templates", toggle=True)

        col.separator()
        col.label(text="Analysis", icon='VIEWZOOM')
        row = col.row(align=True)
        row.prop(self, "show_mesh_stats", toggle=True)
        row.prop(self, "show_modifier_presets", toggle=True)

        from .compat import IS_BLENDER_5
        if not IS_BLENDER_5:
            col.separator()
            layout.label(text="General", icon='PREFERENCES')
            box = layout.box()
            col = box.column()
            col.prop(self, "autosmooth_default_angle")

        layout.label(text="Export", icon='EXPORT')
        box = layout.box()
        col = box.column()
        col.prop(self, "default_export_path")
        col.prop(self, "default_export_format")
        col.prop(self, "apply_transforms_on_export")

        layout.label(text="Presets & Snapshots", icon='PRESET')
        box = layout.box()
        col = box.column()
        col.prop(self, "preset_autosave")
        col.prop(self, "show_snapshot_notifications")


def get_preferences():
    addon = bpy.context.preferences.addons.get("holtalyst")
    if addon:
        return addon.preferences
    return None


def is_panel_enabled(panel_key):
    prefs = get_preferences()
    if prefs is None:
        return True
    return getattr(prefs, panel_key, True)


def register():
    bpy.utils.register_class(HOLTALYST_Preferences)


def unregister():
    bpy.utils.unregister_class(HOLTALYST_Preferences)
