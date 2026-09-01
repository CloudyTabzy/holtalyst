import bpy
from bpy.types import Panel


class HOLTALYST_PT_Lighting_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Lighting_Panel"
    bl_label = "Lighting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="LIGHT")

    def draw(self, context):
        pass


class HOLTALYST_PT_Lighting_Power(Panel):
    bl_idname = "HOLTALYST_PT_Lighting_Power"
    bl_label = "Power"
    bl_parent_id = "HOLTALYST_PT_Lighting_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="LIGHT_SUN")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.label(text="Global Lighting Mode")
        row = col.row(align=True)
        row.prop(holtalyst, "light_mode", text="")
        row = col.row(align=True)
        row.label(text="Target")
        row = col.row(align=True)
        row.prop(holtalyst, "light_target", text="")
        row = col.row(align=True)
        if holtalyst.light_target in ("EMISSIVE_MATERIALS", "BOTH"):
            row.label(text="Material Name Includes:")
            row = col.row(align=True)
            row.prop(holtalyst, "light_mat_includes", text="")
            row = col.row(align=True)
            row.label(text="Node Name Includes:")
            row = col.row(align=True)
            row.prop(holtalyst, "light_node_includes", text="")
        row = col.row(align=True)
        row.separator()
        if holtalyst.light_mode == "ADDITIVE":
            row = col.row(align=True)
            row.prop(holtalyst, "light_add_global", text="")
            row = col.row(align=True)
            row.operator("object.subtract_light_intensity_global", text="-")
            row.operator("object.add_light_intensity_global", text="+")
        if holtalyst.light_mode == "MULTIPLICATIVE":
            row = col.row(align=True)
            row.scale_x = 20
            row.prop(holtalyst, "light_multiply_global", text="")
            row.scale_x = 0
            row.operator("object.multiply_light_intensity_global", text="X")


class HOLTALYST_PT_Lighting_Color(Panel):
    bl_idname = "HOLTALYST_PT_Lighting_Color"
    bl_label = "Color"
    bl_parent_id = "HOLTALYST_PT_Lighting_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="COLOR")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.prop(holtalyst, "color", text="")
        row = col.row(align=True)
        row.prop(holtalyst, "color_selected_only", text="Selected Only")
        row = col.row(align=True)
        row.operator("object.set_light_color", text="Set Light Color")
        row = col.row(align=True)
        row.operator("object.randomize_light_color", text="Randomize Light Color")


classes = (
    HOLTALYST_PT_Lighting_Panel,
    HOLTALYST_PT_Lighting_Power,
    HOLTALYST_PT_Lighting_Color,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
