import bpy
from bpy.types import Panel


class HOLTALYST_PT_Selection_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Selection_Panel"
    bl_label = "Selection"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_selection")

    def draw_header(self, context):
        self.layout.label(text="", icon="RESTRICT_SELECT_OFF")

    def draw(self, context):
        pass


class HOLTALYST_PT_Selection_AllIncluding(Panel):
    bl_idname = "HOLTALYST_PT_Selection_AllIncluding"
    bl_label = "Select All Including"
    bl_parent_id = "HOLTALYST_PT_Selection_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="FONT_DATA")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.label(text="Select all objects including:")
        row = col.row(align=True)
        row.prop(holtalyst, "select_string", text="")
        row = col.row(align=True)
        row.prop(holtalyst, "is_case_sensitive", text="Case Sensitive")
        row = col.row(align=True)
        row.operator("object.select_all_including", text="^ Select All Including ^")
        row = col.row(align=True)
        row.operator("object.form_collection_string", text="Form Collection")
        box2 = box.box()
        col = box2.column()
        row = col.row(align=True)
        row.label(text="Tag Objects")
        row = col.row(align=True)
        row.prop(holtalyst, "tag_string", text="")
        row.prop(holtalyst, "delimiter_string", text="")
        row = col.row(align=True)
        row.operator("object.name_add_prefix", text="Prefix")
        row.operator("object.name_add_suffix", text="Suffix")


class HOLTALYST_PT_Selection_ByType(Panel):
    bl_idname = "HOLTALYST_PT_Selection_ByType"
    bl_label = "Select By Type"
    bl_parent_id = "HOLTALYST_PT_Selection_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="MESH_DATA")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.label(text="Select all objects of this type:")
        row = col.row(align=True)
        row.prop(holtalyst, "select_types", text="")
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.operator("object.select_all_type", text="^ Select All Type ^")
        row = col.row(align=True)
        row.operator("object.form_collection_type", text="Form Collection")


class HOLTALYST_PT_Selection_ByVertexCount(Panel):
    bl_idname = "HOLTALYST_PT_Selection_ByVertexCount"
    bl_label = "Select By Vertex Count"
    bl_parent_id = "HOLTALYST_PT_Selection_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="SNAP_VERTEX")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.label(text="Comparison:")
        row = col.row(align=True)
        row.prop(holtalyst, "comparison_mode", text="")
        row = col.row(align=True)
        row.label(text="Vertex Count:")
        row = col.row(align=True)
        row.prop(holtalyst, "vertex_count", text="")
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.operator("object.select_by_vertex_count", text="^ Select ^")
        row = col.row(align=True)
        row.operator("object.form_collection_vertices", text="Form Collection")


classes = (
    HOLTALYST_PT_Selection_Panel,
    HOLTALYST_PT_Selection_AllIncluding,
    HOLTALYST_PT_Selection_ByType,
    HOLTALYST_PT_Selection_ByVertexCount,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
