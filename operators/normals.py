import bpy
from bpy.types import Operator
from bpy.props import FloatProperty


class HOLTALYST_OT_RecalculateNormals(Operator):
    bl_idname = "holtalyst.recalculate_normals"
    bl_label = "Recalculate Normals"
    bl_description = "Recalculate normals outside (consistent face orientation)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.normals_make_consistent(inside=False)
        self.report({'INFO'}, "Normals recalculated")
        return {'FINISHED'}


class HOLTALYST_OT_RecalculateNormalsInside(Operator):
    bl_idname = "holtalyst.recalculate_normals_inside"
    bl_label = "Recalculate Normals (Inside)"
    bl_description = "Recalculate normals inside"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.normals_make_consistent(inside=True)
        self.report({'INFO'}, "Normals recalculated (inside)")
        return {'FINISHED'}


class HOLTALYST_OT_SmoothNormals(Operator):
    bl_idname = "holtalyst.smooth_normals"
    bl_label = "Smooth Normals"
    bl_description = "Smooth custom normals based on adjacent vertices"
    bl_options = {'REGISTER', 'UNDO'}

    factor: FloatProperty(name="Factor", default=1.0, min=0.0, max=1.0)

    def execute(self, context):
        bpy.ops.mesh.smooth_normals(factor=self.factor)
        self.report({'INFO'}, f"Smoothed normals (factor: {self.factor})")
        return {'FINISHED'}


class HOLTALYST_OT_SplitNormals(Operator):
    bl_idname = "holtalyst.split_normals"
    bl_label = "Split Normals"
    bl_description = "Split custom normals of selected vertices"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.split_normals()
        self.report({'INFO'}, "Normals split")
        return {'FINISHED'}


class HOLTALYST_OT_AddCustomNormals(Operator):
    bl_idname = "holtalyst.add_custom_normals"
    bl_label = "Add Custom Split Normals"
    bl_description = "Add a custom split normals data layer"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.customdata_custom_splitnormals_add()
        self.report({'INFO'}, "Custom split normals layer added")
        return {'FINISHED'}


class HOLTALYST_OT_ClearCustomNormals(Operator):
    bl_idname = "holtalyst.clear_custom_normals"
    bl_label = "Clear Custom Split Normals"
    bl_description = "Remove the custom split normals data layer"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.customdata_custom_splitnormals_clear()
        self.report({'INFO'}, "Custom split normals layer removed")
        return {'FINISHED'}


class HOLTALYST_OT_FlipNormals(Operator):
    bl_idname = "holtalyst.flip_normals"
    bl_label = "Flip Normals"
    bl_description = "Flip normals of selected faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.flip_normals()
        self.report({'INFO'}, "Normals flipped")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_RecalculateNormals,
    HOLTALYST_OT_RecalculateNormalsInside,
    HOLTALYST_OT_SmoothNormals,
    HOLTALYST_OT_SplitNormals,
    HOLTALYST_OT_AddCustomNormals,
    HOLTALYST_OT_ClearCustomNormals,
    HOLTALYST_OT_FlipNormals,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
