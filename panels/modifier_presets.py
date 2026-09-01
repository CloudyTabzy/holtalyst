import bpy
from bpy.types import Panel


class HOLTALYST_PT_ModifierPresets_Panel(Panel):
    bl_idname = "HOLTALYST_PT_ModifierPresets_Panel"
    bl_label = "Modifier Presets"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="MODIFIER")

    def draw(self, context):
        pass


class HOLTALYST_PT_ModifierPresets_Manage(Panel):
    bl_idname = "HOLTALYST_PT_ModifierPresets_Manage"
    bl_label = "Presets"
    bl_parent_id = "HOLTALYST_PT_ModifierPresets_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="PRESET")

    def draw(self, context):
        layout = self.layout
        from ..utils.presets import list_presets
        box = layout.box()
        col = box.column()

        obj = context.active_object
        if obj:
            col.label(text=f"Active: {obj.name} ({len(obj.modifiers)} mods)")
        else:
            col.label(text="No active object")

        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.save_modifier_preset", text="Save Stack", icon='ADD')

        presets = list_presets(subdir="modifier_presets")
        if presets:
            col.separator()
            for name in presets:
                row = col.row(align=True)
                row.label(text=name, icon='FILE_TICK')
                op_load = row.operator("holtalyst.load_modifier_preset", text="", icon='FILE_REFRESH')
                op_load.preset_name = name
                op_del = row.operator("holtalyst.delete_modifier_preset", text="", icon='TRASH')
                op_del.preset_name = name
        else:
            col.separator()
            col.label(text="No modifier presets saved yet")


classes = (
    HOLTALYST_PT_ModifierPresets_Panel,
    HOLTALYST_PT_ModifierPresets_Manage,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
