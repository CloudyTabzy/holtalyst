import bpy
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty


class HOLTALYST_OT_ReplaceMaterial(Operator):
    bl_idname = "holtalyst.replace_material"
    bl_label = "Replace Material"
    bl_description = "Replace one material with another on selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    old_material: StringProperty(name="Old Material", default="")
    new_material: StringProperty(name="New Material", default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.material_batch import replace_material_on_objects
        count = replace_material_on_objects(self.old_material, self.new_material)
        self.report({'INFO'}, f"Replaced {count} material slots")
        return {'FINISHED'}


class HOLTALYST_OT_ReplaceAllMaterials(Operator):
    bl_idname = "holtalyst.replace_all_materials"
    bl_label = "Replace All Materials"
    bl_description = "Replace all materials on selected objects with one material"
    bl_options = {'REGISTER', 'UNDO'}

    new_material: StringProperty(name="New Material", default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.material_batch import replace_all_materials_on_objects
        count = replace_all_materials_on_objects(self.new_material)
        self.report({'INFO'}, f"Replaced {count} material slots")
        return {'FINISHED'}


class HOLTALYST_OT_MergeDuplicateMaterials(Operator):
    bl_idname = "holtalyst.merge_duplicate_materials"
    bl_label = "Merge Duplicate Materials"
    bl_description = "Merge materials with .001 suffixes back to their originals"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.material_batch import merge_duplicate_materials
        count = merge_duplicate_materials()
        self.report({'INFO'}, f"Merged {count} duplicate material references")
        return {'FINISHED'}


class HOLTALYST_OT_AddMaterialToSelection(Operator):
    bl_idname = "holtalyst.add_material_to_selection"
    bl_label = "Add Material"
    bl_description = "Add a material to all selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    material_name: StringProperty(name="Material Name", default="Material")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.material_batch import add_material_to_selection
        count = add_material_to_selection(self.material_name)
        self.report({'INFO'}, f"Added material to {count} objects")
        return {'FINISHED'}


class HOLTALYST_OT_RemoveMaterialFromSelection(Operator):
    bl_idname = "holtalyst.remove_material_from_selection"
    bl_label = "Remove Material"
    bl_description = "Remove a material from all selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    material_name: StringProperty(name="Material Name", default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.material_batch import remove_material_from_selection
        count = remove_material_from_selection(self.material_name)
        self.report({'INFO'}, f"Removed material from {count} objects")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_ReplaceMaterial,
    HOLTALYST_OT_ReplaceAllMaterials,
    HOLTALYST_OT_MergeDuplicateMaterials,
    HOLTALYST_OT_AddMaterialToSelection,
    HOLTALYST_OT_RemoveMaterialFromSelection,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
