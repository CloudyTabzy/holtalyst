import bpy
from bpy.types import Panel


class HOLTALYST_PT_Viewport_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Viewport_Panel"
    bl_label = "Viewport Display"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="RESTRICT_VIEW_OFF")

    def draw(self, context):
        pass


class HOLTALYST_PT_Viewport_Shading(Panel):
    bl_idname = "HOLTALYST_PT_Viewport_Shading"
    bl_label = "Shading Mode"
    bl_parent_id = "HOLTALYST_PT_Viewport_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="SHADING_RENDERED")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("holtalyst.set_viewport_shading", text="Wireframe", icon='SHADING_WIRE').shading_type = 'WIREFRAME'
        row.operator("holtalyst.set_viewport_shading", text="Solid", icon='SHADING_SOLID').shading_type = 'SOLID'
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("holtalyst.set_viewport_shading", text="Material", icon='MATERIAL').shading_type = 'MATERIAL'
        row.operator("holtalyst.set_viewport_shading", text="Rendered", icon='SHADING_RENDERED').shading_type = 'RENDERED'


class HOLTALYST_PT_Viewport_DisplayType(Panel):
    bl_idname = "HOLTALYST_PT_Viewport_DisplayType"
    bl_label = "Object Display Type"
    bl_parent_id = "HOLTALYST_PT_Viewport_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_DATA")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator("holtalyst.set_display_type", text="Bounds").display_type = 'BOUNDS'
        row.operator("holtalyst.set_display_type", text="Wire").display_type = 'WIRE'
        row = col.row(align=True)
        row.operator("holtalyst.set_display_type", text="Solid").display_type = 'SOLID'
        row.operator("holtalyst.set_display_type", text="Textured").display_type = 'TEXTURED'
        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.set_wireframe_all", text="All Wireframe On")
        row.operator("holtalyst.set_solid_all", text="All Wireframe Off")


classes = (
    HOLTALYST_PT_Viewport_Panel,
    HOLTALYST_PT_Viewport_Shading,
    HOLTALYST_PT_Viewport_DisplayType,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
