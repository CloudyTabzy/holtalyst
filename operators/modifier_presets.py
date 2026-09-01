import bpy
from bpy.types import Operator
from bpy.props import StringProperty


class HOLTALYST_OT_SaveModifierPreset(Operator):
    bl_idname = "holtalyst.save_modifier_preset"
    bl_label = "Save Modifier Preset"
    bl_description = "Save the modifier stack of the active object as a preset"
    bl_options = {'REGISTER'}

    preset_name: StringProperty(name="Preset Name", default="Modifier Preset")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'ERROR'}, "No active object")
            return {'CANCELLED'}
        if len(obj.modifiers) == 0:
            self.report({'ERROR'}, "Active object has no modifiers")
            return {'CANCELLED'}

        from ..utils.presets import save_preset
        data = []
        for mod in obj.modifiers:
            mod_data = {
                'name': mod.name,
                'type': mod.type,
                'show_viewport': mod.show_viewport,
                'show_render': mod.show_render,
            }
            if mod.type == 'DECIMATE':
                mod_data['ratio'] = mod.ratio
                mod_data['decimate_type'] = mod.decimate_type
            elif mod.type == 'SUBSURF':
                mod_data['levels'] = mod.levels
                mod_data['render_levels'] = mod.render_levels
            elif mod.type == 'BEVEL':
                mod_data['width'] = mod.width
                mod_data['segments'] = mod.segments
            elif mod.type == 'MIRROR':
                mod_data['use_axis'] = [mod.use_axis[0], mod.use_axis[1], mod.use_axis[2]]
            elif mod.type == 'SOLIDIFY':
                mod_data['thickness'] = mod.thickness
            elif mod.type == 'ARRAY':
                mod_data['count'] = mod.count
            data.append(mod_data)

        save_preset(self.preset_name, data, subdir="modifier_presets")
        self.report({'INFO'}, f"Saved modifier preset: {self.preset_name}")
        return {'FINISHED'}


class HOLTALYST_OT_LoadModifierPreset(Operator):
    bl_idname = "holtalyst.load_modifier_preset"
    bl_label = "Load Modifier Preset"
    bl_description = "Apply a saved modifier preset to the active object"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(name="Preset Name", default="")

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'ERROR'}, "No active object")
            return {'CANCELLED'}

        from ..utils.presets import load_preset
        data = load_preset(self.preset_name, subdir="modifier_presets")
        if data is None:
            self.report({'ERROR'}, f"Preset not found: {self.preset_name}")
            return {'CANCELLED'}

        for mod_data in data:
            mod = obj.modifiers.new(name=mod_data['name'], type=mod_data['type'])
            if 'show_viewport' in mod_data:
                mod.show_viewport = mod_data['show_viewport']
            if 'show_render' in mod_data:
                mod.show_render = mod_data['show_render']
            if mod_data['type'] == 'DECIMATE':
                if 'ratio' in mod_data:
                    mod.ratio = mod_data['ratio']
                if 'decimate_type' in mod_data:
                    mod.decimate_type = mod_data['decimate_type']
            elif mod_data['type'] == 'SUBSURF':
                if 'levels' in mod_data:
                    mod.levels = mod_data['levels']
                if 'render_levels' in mod_data:
                    mod.render_levels = mod_data['render_levels']
            elif mod_data['type'] == 'BEVEL':
                if 'width' in mod_data:
                    mod.width = mod_data['width']
                if 'segments' in mod_data:
                    mod.segments = mod_data['segments']
            elif mod_data['type'] == 'MIRROR':
                if 'use_axis' in mod_data:
                    for i, val in enumerate(mod_data['use_axis']):
                        mod.use_axis[i] = val
            elif mod_data['type'] == 'SOLIDIFY':
                if 'thickness' in mod_data:
                    mod.thickness = mod_data['thickness']
            elif mod_data['type'] == 'ARRAY':
                if 'count' in mod_data:
                    mod.count = mod_data['count']

        self.report({'INFO'}, f"Loaded modifier preset: {self.preset_name}")
        return {'FINISHED'}


class HOLTALYST_OT_DeleteModifierPreset(Operator):
    bl_idname = "holtalyst.delete_modifier_preset"
    bl_label = "Delete Modifier Preset"
    bl_description = "Delete a saved modifier preset"
    bl_options = {'REGISTER'}

    preset_name: StringProperty(name="Preset Name", default="")

    def execute(self, context):
        from ..utils.presets import delete_preset
        if delete_preset(self.preset_name, subdir="modifier_presets"):
            self.report({'INFO'}, f"Deleted modifier preset: {self.preset_name}")
        else:
            self.report({'ERROR'}, f"Preset not found: {self.preset_name}")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SaveModifierPreset,
    HOLTALYST_OT_LoadModifierPreset,
    HOLTALYST_OT_DeleteModifierPreset,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
