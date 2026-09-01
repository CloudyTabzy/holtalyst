import bpy
from bpy.types import Panel


class HOLTALYST_PT_RenderPresets_Panel(Panel):
    bl_idname = "HOLTALYST_PT_RenderPresets_Panel"
    bl_label = "Render Presets"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="SCENE")

    def draw(self, context):
        pass


class HOLTALYST_PT_RenderPresets_Manage(Panel):
    bl_idname = "HOLTALYST_PT_RenderPresets_Manage"
    bl_label = "Presets"
    bl_parent_id = "HOLTALYST_PT_RenderPresets_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="PRESET")

    def draw(self, context):
        layout = self.layout
        from ..utils.presets import list_presets
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.save_render_preset", text="Save Current", icon='ADD')

        presets = list_presets(subdir="render_presets")
        if presets:
            col.separator()
            for name in presets:
                row = col.row(align=True)
                row.label(text=name, icon='FILE_TICK')
                op_load = row.operator("holtalyst.load_render_preset", text="", icon='FILE_REFRESH')
                op_load.preset_name = name
                op_del = row.operator("holtalyst.delete_render_preset", text="", icon='TRASH')
                op_del.preset_name = name
        else:
            col.label(text="No presets saved yet")


class HOLTALYST_PT_RenderPresets_QuickActions(Panel):
    bl_idname = "HOLTALYST_PT_RenderPresets_QuickActions"
    bl_label = "Quick Render"
    bl_parent_id = "HOLTALYST_PT_RenderPresets_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="RENDER_STILL")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render = scene.render
        box = layout.box()
        col = box.column()
        col.label(text=f"Engine: {render.engine}")
        col.label(text=f"Resolution: {render.resolution_x}x{render.resolution_y} @ {render.resolution_percentage}%")
        col.label(text=f"Frame Range: {scene.frame_start}-{scene.frame_end}")
        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator("holtalyst.quick_render", text="Render Frame", icon='RENDER_STILL')
        row.operator("holtalyst.quick_render_anim", text="Render Animation", icon='RENDER_ANIMATION')


classes = (
    HOLTALYST_PT_RenderPresets_Panel,
    HOLTALYST_PT_RenderPresets_Manage,
    HOLTALYST_PT_RenderPresets_QuickActions,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
