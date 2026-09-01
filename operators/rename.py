import bpy
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty, IntProperty, EnumProperty


class HOLTALYST_OT_BatchRenameFindReplace(Operator):
    bl_idname = "holtalyst.batch_rename_find_replace"
    bl_label = "Find & Replace"
    bl_description = "Find and replace text in names of selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    find: StringProperty(name="Find", default="")
    replace: StringProperty(name="Replace", default="")
    case_sensitive: BoolProperty(name="Case Sensitive", default=True)
    data_type: EnumProperty(
        name="Data Type",
        items=[
            ('OBJECT', "Objects", ""),
            ('MATERIAL', "Materials", ""),
            ('MESH', "Meshes", ""),
            ('COLLECTION', "Collections", ""),
        ],
        default='OBJECT',
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.rename import (
            batch_rename_objects,
            batch_rename_materials,
            batch_rename_meshes,
            batch_rename_collections,
        )
        fn_map = {
            'OBJECT': batch_rename_objects,
            'MATERIAL': batch_rename_materials,
            'MESH': batch_rename_meshes,
            'COLLECTION': batch_rename_collections,
        }
        fn = fn_map[self.data_type]
        count = fn(self.find, self.replace, self.case_sensitive)
        self.report({'INFO'}, f"Renamed {count} {self.data_type.lower()}s")
        return {'FINISHED'}


class HOLTALYST_OT_BatchAddPrefix(Operator):
    bl_idname = "holtalyst.batch_add_prefix"
    bl_label = "Add Prefix"
    bl_description = "Add a prefix to selected object names"
    bl_options = {'REGISTER', 'UNDO'}

    prefix: StringProperty(name="Prefix", default="")
    delimiter: StringProperty(name="Delimiter", default="_")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.rename import add_prefix_to_selected
        count = add_prefix_to_selected(self.prefix, self.delimiter)
        self.report({'INFO'}, f"Added prefix to {count} objects")
        return {'FINISHED'}


class HOLTALYST_OT_BatchAddSuffix(Operator):
    bl_idname = "holtalyst.batch_add_suffix"
    bl_label = "Add Suffix"
    bl_description = "Add a suffix to selected object names"
    bl_options = {'REGISTER', 'UNDO'}

    suffix: StringProperty(name="Suffix", default="")
    delimiter: StringProperty(name="Delimiter", default="_")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.rename import add_suffix_to_selected
        count = add_suffix_to_selected(self.suffix, self.delimiter)
        self.report({'INFO'}, f"Added suffix to {count} objects")
        return {'FINISHED'}


class HOLTALYST_OT_BatchNumbering(Operator):
    bl_idname = "holtalyst.batch_numbering"
    bl_label = "Rename with Numbering"
    bl_description = "Rename selected objects with sequential numbering"
    bl_options = {'REGISTER', 'UNDO'}

    base_name: StringProperty(name="Base Name", default="Object")
    start: IntProperty(name="Start", default=1, min=0)
    step: IntProperty(name="Step", default=1, min=1)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.rename import rename_with_numbering
        count = rename_with_numbering(self.base_name, self.start, self.step)
        self.report({'INFO'}, f"Renamed {count} objects")
        return {'FINISHED'}


class HOLTALYST_OT_StripTrailingNumbers(Operator):
    bl_idname = "holtalyst.strip_trailing_numbers"
    bl_label = "Strip Trailing Numbers"
    bl_description = "Remove .001, .002 suffixes from object names"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.rename import strip_trailing_numbers
        count = strip_trailing_numbers()
        self.report({'INFO'}, f"Stripped numbers from {count} objects")
        return {'FINISHED'}


class HOLTALYST_OT_RenameDataToMatch(Operator):
    bl_idname = "holtalyst.rename_data_to_match"
    bl_label = "Sync Data Names"
    bl_description = "Rename mesh/data blocks to match their object names"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils.rename import rename_data_to_match
        count = rename_data_to_match()
        self.report({'INFO'}, f"Synced {count} data blocks")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_BatchRenameFindReplace,
    HOLTALYST_OT_BatchAddPrefix,
    HOLTALYST_OT_BatchAddSuffix,
    HOLTALYST_OT_BatchNumbering,
    HOLTALYST_OT_StripTrailingNumbers,
    HOLTALYST_OT_RenameDataToMatch,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
