import bpy
from bpy.types import Operator
from bpy.props import StringProperty


class HOLTALYST_OT_SaveSnapshot(Operator):
    bl_idname = "holtalyst.save_snapshot"
    bl_label = "Save Snapshot"
    bl_description = "Save current scene state (visibility, transforms, modifiers) as a snapshot"
    bl_options = {'REGISTER'}

    snapshot_name: StringProperty(name="Snapshot Name", default="Snapshot")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.presets import save_preset, get_snapshot_dict
        data = get_snapshot_dict()
        save_preset(self.snapshot_name, data, subdir="snapshots")
        self.report({'INFO'}, f"Saved snapshot: {self.snapshot_name}")
        return {'FINISHED'}


class HOLTALYST_OT_LoadSnapshot(Operator):
    bl_idname = "holtalyst.load_snapshot"
    bl_label = "Load Snapshot"
    bl_description = "Restore a saved scene snapshot"
    bl_options = {'REGISTER', 'UNDO'}

    snapshot_name: StringProperty(name="Snapshot Name", default="")

    def execute(self, context):
        from ..utils.presets import load_preset, apply_snapshot_dict
        data = load_preset(self.snapshot_name, subdir="snapshots")
        if data is None:
            self.report({'ERROR'}, f"Snapshot not found: {self.snapshot_name}")
            return {'CANCELLED'}
        apply_snapshot_dict(data)
        self.report({'INFO'}, f"Loaded snapshot: {self.snapshot_name}")
        return {'FINISHED'}


class HOLTALYST_OT_DeleteSnapshot(Operator):
    bl_idname = "holtalyst.delete_snapshot"
    bl_label = "Delete Snapshot"
    bl_description = "Delete a saved snapshot"
    bl_options = {'REGISTER'}

    snapshot_name: StringProperty(name="Snapshot Name", default="")

    def execute(self, context):
        from ..utils.presets import delete_preset
        if delete_preset(self.snapshot_name, subdir="snapshots"):
            self.report({'INFO'}, f"Deleted snapshot: {self.snapshot_name}")
        else:
            self.report({'ERROR'}, f"Snapshot not found: {self.snapshot_name}")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SaveSnapshot,
    HOLTALYST_OT_LoadSnapshot,
    HOLTALYST_OT_DeleteSnapshot,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
