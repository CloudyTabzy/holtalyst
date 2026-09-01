import bpy
from bpy.types import Panel


class HOLTALYST_PT_Export_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Export_Panel"
    bl_label = "Batch Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="EXPORT")

    def draw(self, context):
        pass


class HOLTALYST_PT_Export_Objects(Panel):
    bl_idname = "HOLTALYST_PT_Export_Objects"
    bl_label = "Export Objects"
    bl_parent_id = "HOLTALYST_PT_Export_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_DATA")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        col.label(text="Export each selected object as a separate file")
        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator("holtalyst.batch_export_selected", text="Export Selected Objects")


class HOLTALYST_PT_Export_Collections(Panel):
    bl_idname = "HOLTALYST_PT_Export_Collections"
    bl_label = "Export Collections"
    bl_parent_id = "HOLTALYST_PT_Export_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="OUTLINER_COLLECTION")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        col.label(text="Export each collection as a separate file")
        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator("holtalyst.batch_export_collections", text="Export All Collections")


classes = (
    HOLTALYST_PT_Export_Panel,
    HOLTALYST_PT_Export_Objects,
    HOLTALYST_PT_Export_Collections,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
