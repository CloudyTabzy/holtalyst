import bpy
from bpy.types import Panel


class HOLTALYST_PT_WorldHDRI_Panel(Panel):
    bl_idname = "HOLTALYST_PT_WorldHDRI_Panel"
    bl_label = "World / HDRI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_world_hdri")

    def draw_header(self, context):
        self.layout.label(text="", icon="WORLD")

    def draw(self, context):
        pass


class HOLTALYST_PT_WorldHDRI_Switch(Panel):
    bl_idname = "HOLTALYST_PT_WorldHDRI_Switch"
    bl_label = "Switch World"
    bl_parent_id = "HOLTALYST_PT_WorldHDRI_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="FILE_REFRESH")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        box = layout.box()
        col = box.column()

        if scene.world:
            col.label(text=f"Active: {scene.world.name}", icon='WORLD')
        else:
            col.label(text="No world set", icon='ERROR')

        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("holtalyst.cycle_world_prev", text="", icon='TRIA_LEFT')
        row.operator("holtalyst.cycle_world_next", text="", icon='TRIA_RIGHT')

        worlds = list(bpy.data.worlds)
        if len(worlds) > 1:
            col.separator()
            for w in worlds:
                row = col.row(align=True)
                icon = 'RADIOBUT_ON' if scene.world and w.name == scene.world.name else 'RADIOBUT_OFF'
                row.label(text=w.name, icon=icon)
                op = row.operator("holtalyst.switch_world", text="", icon='RESTRICT_SELECT_OFF')
                op.world_name = w.name


class HOLTALYST_PT_WorldHDRI_Actions(Panel):
    bl_idname = "HOLTALYST_PT_WorldHDRI_Actions"
    bl_label = "World Actions"
    bl_parent_id = "HOLTALYST_PT_WorldHDRI_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="TOOL_SETTINGS")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator("holtalyst.set_world_color", text="Reset World Color")
        row = col.row(align=True)
        row.operator("holtalyst.list_worlds", text="List All Worlds")


classes = (
    HOLTALYST_PT_WorldHDRI_Panel,
    HOLTALYST_PT_WorldHDRI_Switch,
    HOLTALYST_PT_WorldHDRI_Actions,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
