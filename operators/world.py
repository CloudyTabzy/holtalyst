import bpy
from bpy.types import Operator


class HOLTALYST_OT_ToggleWorldVolume(Operator):
    bl_idname = "object.toggle_world_volume"
    bl_label = "Toggle World Volume"
    bl_description = "Toggles volume shaders in the world nodes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import get_world_nodes
        for n in get_world_nodes():
            if n.type in ("PRINCIPLED_VOLUME", "VOLUME_SCATTER"):
                n.mute = not n.mute
        return {'FINISHED'}


classes = (HOLTALYST_OT_ToggleWorldVolume,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
