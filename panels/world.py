import bpy
from bpy.types import Panel


class HOLTALYST_PT_World_Panel(Panel):
    bl_idname = "HOLTALYST_PT_World_Panel"
    bl_label = "World"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_world")

    def draw_header(self, context):
        self.layout.label(text="", icon="WORLD")

    def draw(self, context):
        pass


class HOLTALYST_PT_World_Volume(Panel):
    bl_idname = "HOLTALYST_PT_World_Volume"
    bl_label = "Volume"
    bl_parent_id = "HOLTALYST_PT_World_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="VOLUME_DATA")

    def draw(self, context):
        layout = self.layout
        b = layout.box()
        column = b.column()
        row = column.row()
        row.operator("object.toggle_world_volume", text="Toggle World Volume")


classes = (
    HOLTALYST_PT_World_Panel,
    HOLTALYST_PT_World_Volume,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
