import bpy
from bpy.types import Operator
from bpy.props import EnumProperty


TEMPLATES = {
    'GAME_ASSET': {
        'label': 'Game Asset',
        'collections': ['Meshes', 'Textures', 'Rigs', 'Animations', 'Export'],
    },
    'ARCHVIZ': {
        'label': 'Architectural Visualization',
        'collections': ['Structure', 'Furniture', 'Lighting', 'Materials', 'Cameras'],
    },
    'CHARACTER': {
        'label': 'Character',
        'collections': ['Body', 'Clothing', 'Hair', 'Accessories', 'Rig', 'Shapes'],
    },
    'PRODUCT': {
        'label': 'Product Shot',
        'collections': ['Product', 'Environment', 'Lighting', 'Cameras', 'Render'],
    },
    'SCENE': {
        'label': 'Scene Layout',
        'collections': ['Foreground', 'Midground', 'Background', 'Atmosphere', 'Lights', 'Cameras'],
    },
    'EMPTY': {
        'label': 'Empty (No Collections)',
        'collections': [],
    },
}


class HOLTALYST_OT_ApplyCollectionTemplate(Operator):
    bl_idname = "holtalyst.apply_collection_template"
    bl_label = "Apply Collection Template"
    bl_description = "Create a predefined collection hierarchy"
    bl_options = {'REGISTER', 'UNDO'}

    template: EnumProperty(
        name="Template",
        items=[
            ('GAME_ASSET', "Game Asset", ""),
            ('ARCHVIZ', "Architectural Visualization", ""),
            ('CHARACTER', "Character", ""),
            ('PRODUCT', "Product Shot", ""),
            ('SCENE', "Scene Layout", ""),
            ('EMPTY', "Empty", ""),
        ],
        default='GAME_ASSET',
    )

    def execute(self, context):
        tmpl = TEMPLATES.get(self.template)
        if tmpl is None:
            self.report({'ERROR'}, "Unknown template")
            return {'CANCELLED'}
        created = 0
        for col_name in tmpl['collections']:
            if col_name not in bpy.data.collections:
                col = bpy.data.collections.new(col_name)
                context.scene.collection.children.link(col)
                created += 1
        self.report({'INFO'}, f"Created {created} collections from '{tmpl['label']}' template")
        return {'FINISHED'}


class HOLTALYST_OT_MoveSelectedToCollection(Operator):
    bl_idname = "holtalyst.move_selected_to_collection"
    bl_label = "Move to Collection"
    bl_description = "Move selected objects to a specified collection"
    bl_options = {'REGISTER', 'UNDO'}

    collection_name: EnumProperty(
        name="Collection",
        items=lambda self, context: [
            (col.name, col.name, "") for col in bpy.data.collections
        ],
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if self.collection_name not in bpy.data.collections:
            self.report({'ERROR'}, f"Collection not found: {self.collection_name}")
            return {'CANCELLED'}
        col = bpy.data.collections[self.collection_name]
        for obj in context.selected_objects:
            for c in obj.users_collection:
                c.objects.unlink(obj)
            col.objects.link(obj)
        self.report({'INFO'}, f"Moved {len(context.selected_objects)} objects to {self.collection_name}")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_ApplyCollectionTemplate,
    HOLTALYST_OT_MoveSelectedToCollection,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
