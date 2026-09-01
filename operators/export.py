import bpy
from bpy.types import Operator
from bpy.props import StringProperty, EnumProperty, BoolProperty


class HOLTALYST_OT_BatchExportSelected(Operator):
    bl_idname = "holtalyst.batch_export_selected"
    bl_label = "Batch Export Selected"
    bl_description = "Export each selected object as a separate file"
    bl_options = {'REGISTER'}

    directory: StringProperty(
        name="Export Directory",
        description="Directory to export files to",
        subtype='DIR_PATH',
        default="//exports/",
    )
    export_format: EnumProperty(
        name="Format",
        items=[
            ('OBJ', "OBJ", "Wavefront OBJ"),
            ('GLTF', "glTF", "glTF 2.0 (.glb)"),
            ('FBX', "FBX", "FBX"),
            ('STL', "STL", "STL"),
        ],
        default='OBJ',
    )
    apply_transforms: BoolProperty(
        name="Apply Transforms",
        description="Apply transforms before exporting",
        default=True,
    )

    def invoke(self, context, event):
        from ..preferences import get_preferences
        prefs = get_preferences()
        if prefs:
            self.directory = prefs.default_export_path
            self.export_format = prefs.default_export_format
            self.apply_transforms = prefs.apply_transforms_on_export
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.export import batch_export_objects
        count, files = batch_export_objects(
            self.directory,
            fmt=self.export_format,
            apply_transforms=self.apply_transforms,
            selected_only=True,
        )
        self.report({'INFO'}, f"Exported {count} objects to {self.directory}")
        return {'FINISHED'}


class HOLTALYST_OT_BatchExportCollections(Operator):
    bl_idname = "holtalyst.batch_export_collections"
    bl_label = "Batch Export Collections"
    bl_description = "Export each collection as a separate file"
    bl_options = {'REGISTER'}

    directory: StringProperty(
        name="Export Directory",
        description="Directory to export files to",
        subtype='DIR_PATH',
        default="//exports/",
    )
    export_format: EnumProperty(
        name="Format",
        items=[
            ('OBJ', "OBJ", "Wavefront OBJ"),
            ('GLTF', "glTF", "glTF 2.0 (.glb)"),
            ('FBX', "FBX", "FBX"),
            ('STL', "STL", "STL"),
        ],
        default='OBJ',
    )
    apply_transforms: BoolProperty(
        name="Apply Transforms",
        description="Apply transforms before exporting",
        default=True,
    )

    def invoke(self, context, event):
        from ..preferences import get_preferences
        prefs = get_preferences()
        if prefs:
            self.directory = prefs.default_export_path
            self.export_format = prefs.default_export_format
            self.apply_transforms = prefs.apply_transforms_on_export
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        from ..utils.export import batch_export_collections
        count, files = batch_export_collections(
            self.directory,
            fmt=self.export_format,
            apply_transforms=self.apply_transforms,
        )
        self.report({'INFO'}, f"Exported {count} collections to {self.directory}")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_BatchExportSelected,
    HOLTALYST_OT_BatchExportCollections,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
