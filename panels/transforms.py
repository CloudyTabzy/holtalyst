import bpy
from bpy.types import Panel


class HOLTALYST_PT_Transforms_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Transforms_Panel"
    bl_label = "Smart Transforms"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_DATA")

    def draw(self, context):
        pass


class HOLTALYST_PT_Transforms_Apply(Panel):
    bl_idname = "HOLTALYST_PT_Transforms_Apply"
    bl_label = "Apply Transforms"
    bl_parent_id = "HOLTALYST_PT_Transforms_Panel"
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
        row.operator("holtalyst.smart_apply_location", text="Location")
        row.operator("holtalyst.smart_apply_rotation", text="Rotation")
        row.operator("holtalyst.smart_apply_scale", text="Scale")
        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("holtalyst.smart_apply_rot_scale", text="Rotation & Scale")
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("holtalyst.smart_apply_all", text="All Transforms")
        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.apply_transforms_keep_children", text="Apply (Keep Children)")


class HOLTALYST_PT_Transforms_Clear(Panel):
    bl_idname = "HOLTALYST_PT_Transforms_Clear"
    bl_label = "Clear Transforms"
    bl_parent_id = "HOLTALYST_PT_Transforms_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="X")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator("holtalyst.clear_location", text="Clear Location")
        row.operator("holtalyst.clear_rotation", text="Clear Rotation")
        row.operator("holtalyst.clear_scale", text="Clear Scale")


classes = (
    HOLTALYST_PT_Transforms_Panel,
    HOLTALYST_PT_Transforms_Apply,
    HOLTALYST_PT_Transforms_Clear,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
