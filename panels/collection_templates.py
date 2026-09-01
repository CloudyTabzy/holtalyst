import bpy
from bpy.types import Panel


class HOLTALYST_PT_CollectionTemplates_Panel(Panel):
    bl_idname = "HOLTALYST_PT_CollectionTemplates_Panel"
    bl_label = "Collection Templates"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="OUTLINER_COLLECTION")

    def draw(self, context):
        pass


class HOLTALYST_PT_CollectionTemplates_Apply(Panel):
    bl_idname = "HOLTALYST_PT_CollectionTemplates_Apply"
    bl_label = "Templates"
    bl_parent_id = "HOLTALYST_PT_CollectionTemplates_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="PRESET")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Create collection hierarchy:")
        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.apply_collection_template", text="Game Asset").template = 'GAME_ASSET'
        row.operator("holtalyst.apply_collection_template", text="Archviz").template = 'ARCHVIZ'
        row = col.row(align=True)
        row.operator("holtalyst.apply_collection_template", text="Character").template = 'CHARACTER'
        row.operator("holtalyst.apply_collection_template", text="Product Shot").template = 'PRODUCT'
        row = col.row(align=True)
        row.operator("holtalyst.apply_collection_template", text="Scene Layout").template = 'SCENE'


class HOLTALYST_PT_CollectionTemplates_Move(Panel):
    bl_idname = "HOLTALYST_PT_CollectionTemplates_Move"
    bl_label = "Move Objects"
    bl_parent_id = "HOLTALYST_PT_CollectionTemplates_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="FORWARD")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.move_selected_to_collection", text="Move Selected to Collection")


classes = (
    HOLTALYST_PT_CollectionTemplates_Panel,
    HOLTALYST_PT_CollectionTemplates_Apply,
    HOLTALYST_PT_CollectionTemplates_Move,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
