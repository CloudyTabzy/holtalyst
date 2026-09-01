import bpy
from bpy.types import Operator


class HOLTALYST_OT_QuickDecimate(Operator):
    bl_idname = "object.quick_decimate"
    bl_label = "Quick Decimate"
    bl_description = "Quickly decimates object based on decimate rate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import so, add_decimate, apply_all_modifiers
        holtalyst = context.scene.holtalyst
        for o in so():
            mod = add_decimate(o)
            mod.ratio = holtalyst.decimate_rate
            apply_all_modifiers(o)
        return {'FINISHED'}


classes = (HOLTALYST_OT_QuickDecimate,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
