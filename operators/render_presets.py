import bpy
from bpy.types import Operator
from bpy.props import StringProperty, EnumProperty


class HOLTALYST_OT_SaveRenderPreset(Operator):
    bl_idname = "holtalyst.save_render_preset"
    bl_label = "Save Render Preset"
    bl_description = "Save current render settings as a named preset"
    bl_options = {'REGISTER'}

    preset_name: StringProperty(name="Preset Name", default="My Preset")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.presets import save_preset, get_render_settings_dict
        data = get_render_settings_dict()
        save_preset(self.preset_name, data, subdir="render_presets")
        self.report({'INFO'}, f"Saved render preset: {self.preset_name}")
        return {'FINISHED'}


class HOLTALYST_OT_LoadRenderPreset(Operator):
    bl_idname = "holtalyst.load_render_preset"
    bl_label = "Load Render Preset"
    bl_description = "Load a saved render preset"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(name="Preset Name", default="")

    def execute(self, context):
        from ..utils.presets import load_preset, apply_render_settings_dict
        data = load_preset(self.preset_name, subdir="render_presets")
        if data is None:
            self.report({'ERROR'}, f"Preset not found: {self.preset_name}")
            return {'CANCELLED'}
        apply_render_settings_dict(data)
        self.report({'INFO'}, f"Loaded render preset: {self.preset_name}")
        return {'FINISHED'}


class HOLTALYST_OT_DeleteRenderPreset(Operator):
    bl_idname = "holtalyst.delete_render_preset"
    bl_label = "Delete Render Preset"
    bl_description = "Delete a saved render preset"
    bl_options = {'REGISTER'}

    preset_name: StringProperty(name="Preset Name", default="")

    def execute(self, context):
        from ..utils.presets import delete_preset
        if delete_preset(self.preset_name, subdir="render_presets"):
            self.report({'INFO'}, f"Deleted render preset: {self.preset_name}")
        else:
            self.report({'ERROR'}, f"Preset not found: {self.preset_name}")
        return {'FINISHED'}


class HOLTALYST_OT_QuickRender(Operator):
    bl_idname = "holtalyst.quick_render"
    bl_label = "Quick Render"
    bl_description = "Render the current frame and save to output path"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.ops.render.render(write_still=True)
        self.report({'INFO'}, "Render complete")
        return {'FINISHED'}


class HOLTALYST_OT_QuickRenderAnim(Operator):
    bl_idname = "holtalyst.quick_render_anim"
    bl_label = "Quick Render Animation"
    bl_description = "Render the full animation range"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.ops.render.render(animation=True)
        self.report({'INFO'}, "Animation render complete")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SaveRenderPreset,
    HOLTALYST_OT_LoadRenderPreset,
    HOLTALYST_OT_DeleteRenderPreset,
    HOLTALYST_OT_QuickRender,
    HOLTALYST_OT_QuickRenderAnim,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
