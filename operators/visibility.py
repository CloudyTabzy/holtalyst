import bpy
from bpy.types import Operator
from bpy.props import StringProperty


class HOLTALYST_OT_SaveVisibilitySet(Operator):
    bl_idname = "holtalyst.save_visibility_set"
    bl_label = "Save Visibility Set"
    bl_description = "Save current object visibility states as a named set"
    bl_options = {'REGISTER'}

    set_name: StringProperty(name="Set Name", default="Visibility Set")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.presets import save_preset
        data = {}
        for obj in bpy.data.objects:
            data[obj.name] = {
                'hide_viewport': obj.hide_viewport,
                'hide_render': obj.hide_render,
                'hide_get': obj.hide_get(),
            }
        save_preset(self.set_name, data, subdir="visibility_sets")
        self.report({'INFO'}, f"Saved visibility set: {self.set_name}")
        return {'FINISHED'}


class HOLTALYST_OT_LoadVisibilitySet(Operator):
    bl_idname = "holtalyst.load_visibility_set"
    bl_label = "Load Visibility Set"
    bl_description = "Restore a saved visibility set"
    bl_options = {'REGISTER', 'UNDO'}

    set_name: StringProperty(name="Set Name", default="")

    def execute(self, context):
        from ..utils.presets import load_preset
        data = load_preset(self.set_name, subdir="visibility_sets")
        if data is None:
            self.report({'ERROR'}, f"Set not found: {self.set_name}")
            return {'CANCELLED'}
        for obj_name, vis in data.items():
            if obj_name in bpy.data.objects:
                obj = bpy.data.objects[obj_name]
                if 'hide_viewport' in vis:
                    obj.hide_viewport = vis['hide_viewport']
                if 'hide_render' in vis:
                    obj.hide_render = vis['hide_render']
                if 'hide_get' in vis:
                    obj.hide_set(vis['hide_get'])
        self.report({'INFO'}, f"Loaded visibility set: {self.set_name}")
        return {'FINISHED'}


class HOLTALYST_OT_DeleteVisibilitySet(Operator):
    bl_idname = "holtalyst.delete_visibility_set"
    bl_label = "Delete Visibility Set"
    bl_description = "Delete a saved visibility set"
    bl_options = {'REGISTER'}

    set_name: StringProperty(name="Set Name", default="")

    def execute(self, context):
        from ..utils.presets import delete_preset
        if delete_preset(self.set_name, subdir="visibility_sets"):
            self.report({'INFO'}, f"Deleted visibility set: {self.set_name}")
        else:
            self.report({'ERROR'}, f"Set not found: {self.set_name}")
        return {'FINISHED'}


class HOLTALYST_OT_HideSelected(Operator):
    bl_idname = "holtalyst.hide_selected"
    bl_label = "Hide Selected"
    bl_description = "Hide selected objects in viewport"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            obj.hide_set(True)
        return {'FINISHED'}


class HOLTALYST_OT_UnhideAll(Operator):
    bl_idname = "holtalyst.unhide_all"
    bl_label = "Unhide All"
    bl_description = "Reveal all hidden objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.data.objects:
            obj.hide_set(False)
            obj.hide_viewport = False
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SaveVisibilitySet,
    HOLTALYST_OT_LoadVisibilitySet,
    HOLTALYST_OT_DeleteVisibilitySet,
    HOLTALYST_OT_HideSelected,
    HOLTALYST_OT_UnhideAll,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
