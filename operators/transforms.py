import bpy
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty


class HOLTALYST_OT_SmartApplyLocation(Operator):
    bl_idname = "holtalyst.smart_apply_location"
    bl_label = "Apply Location"
    bl_description = "Apply location transform to selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import smart_apply_location
        smart_apply_location()
        return {'FINISHED'}


class HOLTALYST_OT_SmartApplyRotation(Operator):
    bl_idname = "holtalyst.smart_apply_rotation"
    bl_label = "Apply Rotation"
    bl_description = "Apply rotation transform to selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import smart_apply_rotation
        smart_apply_rotation()
        return {'FINISHED'}


class HOLTALYST_OT_SmartApplyScale(Operator):
    bl_idname = "holtalyst.smart_apply_scale"
    bl_label = "Apply Scale"
    bl_description = "Apply scale transform to selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import smart_apply_scale
        smart_apply_scale()
        return {'FINISHED'}


class HOLTALYST_OT_SmartApplyRotScale(Operator):
    bl_idname = "holtalyst.smart_apply_rot_scale"
    bl_label = "Apply Rotation & Scale"
    bl_description = "Apply rotation and scale transforms to selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import smart_apply_rotation_scale
        smart_apply_rotation_scale()
        return {'FINISHED'}


class HOLTALYST_OT_SmartApplyAll(Operator):
    bl_idname = "holtalyst.smart_apply_all"
    bl_label = "Apply All Transforms"
    bl_description = "Apply all transforms to selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import smart_apply_all
        smart_apply_all()
        return {'FINISHED'}


class HOLTALYST_OT_ApplyTransformsKeepChildren(Operator):
    bl_idname = "holtalyst.apply_transforms_keep_children"
    bl_label = "Apply Transforms (Keep Children)"
    bl_description = "Apply transforms while preserving child object world positions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import apply_transforms_keep_children
        apply_transforms_keep_children()
        return {'FINISHED'}


class HOLTALYST_OT_ClearLocation(Operator):
    bl_idname = "holtalyst.clear_location"
    bl_label = "Clear Location"
    bl_description = "Reset location to world origin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import clear_location
        clear_location()
        return {'FINISHED'}


class HOLTALYST_OT_ClearRotation(Operator):
    bl_idname = "holtalyst.clear_rotation"
    bl_label = "Clear Rotation"
    bl_description = "Reset rotation to zero"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import clear_rotation
        clear_rotation()
        return {'FINISHED'}


class HOLTALYST_OT_ClearScale(Operator):
    bl_idname = "holtalyst.clear_scale"
    bl_label = "Clear Scale"
    bl_description = "Reset scale to 1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.transforms import clear_scale
        clear_scale()
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SmartApplyLocation,
    HOLTALYST_OT_SmartApplyRotation,
    HOLTALYST_OT_SmartApplyScale,
    HOLTALYST_OT_SmartApplyRotScale,
    HOLTALYST_OT_SmartApplyAll,
    HOLTALYST_OT_ApplyTransformsKeepChildren,
    HOLTALYST_OT_ClearLocation,
    HOLTALYST_OT_ClearRotation,
    HOLTALYST_OT_ClearScale,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
