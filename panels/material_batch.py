import bpy
from bpy.types import Panel


class HOLTALYST_PT_MaterialBatch_Panel(Panel):
    bl_idname = "HOLTALYST_PT_MaterialBatch_Panel"
    bl_label = "Material Batch Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="MATERIAL")

    def draw(self, context):
        pass


class HOLTALYST_PT_MaterialBatch_Replace(Panel):
    bl_idname = "HOLTALYST_PT_MaterialBatch_Replace"
    bl_label = "Replace"
    bl_parent_id = "HOLTALYST_PT_MaterialBatch_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="FILE_REFRESH")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.replace_material", text="Replace Material")
        row = col.row(align=True)
        row.operator("holtalyst.replace_all_materials", text="Replace All With...")
        row = col.row(align=True)
        row.operator("holtalyst.merge_duplicate_materials", text="Merge Duplicates")


class HOLTALYST_PT_MaterialBatch_Assign(Panel):
    bl_idname = "HOLTALYST_PT_MaterialBatch_Assign"
    bl_label = "Assign / Remove"
    bl_parent_id = "HOLTALYST_PT_MaterialBatch_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="ADD")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.add_material_to_selection", text="Add Material to Selection")
        row = col.row(align=True)
        row.operator("holtalyst.remove_material_from_selection", text="Remove Material from Selection")


classes = (
    HOLTALYST_PT_MaterialBatch_Panel,
    HOLTALYST_PT_MaterialBatch_Replace,
    HOLTALYST_PT_MaterialBatch_Assign,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
