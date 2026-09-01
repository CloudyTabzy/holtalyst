import bpy
from bpy.types import Panel


class HOLTALYST_PT_Visibility_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Visibility_Panel"
    bl_label = "Visibility Sets"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_visibility")

    def draw_header(self, context):
        self.layout.label(text="", icon="HIDE_OFF")

    def draw(self, context):
        pass


class HOLTALYST_PT_Visibility_Manage(Panel):
    bl_idname = "HOLTALYST_PT_Visibility_Manage"
    bl_label = "Saved Sets"
    bl_parent_id = "HOLTALYST_PT_Visibility_Panel"
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
        row = col.row(align=True)
        row.operator("holtalyst.save_visibility_set", text="Save Current", icon='ADD')

        sets = list_presets(subdir="visibility_sets")
        if sets:
            col.separator()
            for name in sets:
                row = col.row(align=True)
                row.label(text=name, icon='FILE_TICK')
                op_load = row.operator("holtalyst.load_visibility_set", text="", icon='FILE_REFRESH')
                op_load.set_name = name
                op_del = row.operator("holtalyst.delete_visibility_set", text="", icon='TRASH')
                op_del.set_name = name
        else:
            col.label(text="No visibility sets saved yet")


class HOLTALYST_PT_Visibility_Quick(Panel):
    bl_idname = "HOLTALYST_PT_Visibility_Quick"
    bl_label = "Quick Actions"
    bl_parent_id = "HOLTALYST_PT_Visibility_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="RESTRICT_VIEW_OFF")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator("holtalyst.hide_selected", text="Hide Selected")
        row.operator("holtalyst.unhide_all", text="Unhide All")


classes = (
    HOLTALYST_PT_Visibility_Panel,
    HOLTALYST_PT_Visibility_Manage,
    HOLTALYST_PT_Visibility_Quick,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
