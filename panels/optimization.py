import bpy
from bpy.types import Panel


class HOLTALYST_PT_Optimization_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Optimization_Panel"
    bl_label = "Optimization"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="MOD_DECIM")

    def draw(self, context):
        pass


class HOLTALYST_PT_Optimization_Mesh(Panel):
    bl_idname = "HOLTALYST_PT_Optimization_Mesh"
    bl_label = "Mesh"
    bl_parent_id = "HOLTALYST_PT_Optimization_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="MESH_DATA")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        b = layout.box()
        b.label(text="Quick Decimation")
        column = b.column()
        row = column.row()
        row.prop(holtalyst, "decimate_rate", text="")
        row = column.row()
        row.operator("object.quick_decimate", text="Quick Decimate")


classes = (
    HOLTALYST_PT_Optimization_Panel,
    HOLTALYST_PT_Optimization_Mesh,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
