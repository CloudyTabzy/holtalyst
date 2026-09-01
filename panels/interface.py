import bpy
from bpy.types import Panel


class HOLTALYST_PT_Interface_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Interface_Panel"
    bl_label = "Interface"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="PROPERTIES")

    def draw(self, context):
        pass


class HOLTALYST_PT_Interface_Theme(Panel):
    bl_idname = "HOLTALYST_PT_Interface_Theme"
    bl_label = "Theme"
    bl_parent_id = "HOLTALYST_PT_Interface_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="PRESET")

    def draw(self, context):
        layout = self.layout
        b = layout.box()
        column = b.column()
        row = column.row()
        row.menu("USERPREF_MT_interface_theme_presets")


classes = (
    HOLTALYST_PT_Interface_Panel,
    HOLTALYST_PT_Interface_Theme,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
