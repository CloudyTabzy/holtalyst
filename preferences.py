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

    def draw(self, context):
        layout = self.layout
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


def register():
    bpy.utils.register_class(HOLTALYST_Preferences)


def unregister():
    bpy.utils.unregister_class(HOLTALYST_Preferences)
