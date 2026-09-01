import bpy
from bpy.types import Panel


class HOLTALYST_PT_Normals_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Normals_Panel"
    bl_label = "Normal Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="NORMALS_FACE")

    def draw(self, context):
        pass


class HOLTALYST_PT_Normals_Basic(Panel):
    bl_idname = "HOLTALYST_PT_Normals_Basic"
    bl_label = "Basic"
    bl_parent_id = "HOLTALYST_PT_Normals_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="CHECKMARK")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("holtalyst.recalculate_normals", text="Recalculate Outside")
        row.operator("holtalyst.recalculate_normals_inside", text="Recalculate Inside")
        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.flip_normals", text="Flip Normals")


class HOLTALYST_PT_Normals_Custom(Panel):
    bl_idname = "HOLTALYST_PT_Normals_Custom"
    bl_label = "Custom Split Normals"
    bl_parent_id = "HOLTALYST_PT_Normals_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="MODIFIER")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator("holtalyst.smooth_normals", text="Smooth Normals")
        row = col.row(align=True)
        row.operator("holtalyst.split_normals", text="Split Normals")
        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.add_custom_normals", text="Add Custom Layer")
        row.operator("holtalyst.clear_custom_normals", text="Clear Custom Layer")


classes = (
    HOLTALYST_PT_Normals_Panel,
    HOLTALYST_PT_Normals_Basic,
    HOLTALYST_PT_Normals_Custom,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
