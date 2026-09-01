import bpy
from bpy.types import Panel


class HOLTALYST_PT_Rename_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Rename_Panel"
    bl_label = "Batch Rename"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_rename")

    def draw_header(self, context):
        self.layout.label(text="", icon="FONT_DATA")

    def draw(self, context):
        pass


class HOLTALYST_PT_Rename_FindReplace(Panel):
    bl_idname = "HOLTALYST_PT_Rename_FindReplace"
    bl_label = "Find & Replace"
    bl_parent_id = "HOLTALYST_PT_Rename_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="VIEWZOOM")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.batch_rename_find_replace", text="Find & Replace")


class HOLTALYST_PT_Rename_Tagging(Panel):
    bl_idname = "HOLTALYST_PT_Rename_Tagging"
    bl_label = "Prefix / Suffix"
    bl_parent_id = "HOLTALYST_PT_Rename_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="BOOKMARKS")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.batch_add_prefix", text="Add Prefix")
        row.operator("holtalyst.batch_add_suffix", text="Add Suffix")


class HOLTALYST_PT_Rename_Numbering(Panel):
    bl_idname = "HOLTALYST_PT_Rename_Numbering"
    bl_label = "Numbering & Cleanup"
    bl_parent_id = "HOLTALYST_PT_Rename_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="LINENUMBERS_ON")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.batch_numbering", text="Rename with Numbering")
        row = col.row(align=True)
        row.operator("holtalyst.strip_trailing_numbers", text="Strip .001 Suffixes")
        row = col.row(align=True)
        row.operator("holtalyst.rename_data_to_match", text="Sync Data Names")


classes = (
    HOLTALYST_PT_Rename_Panel,
    HOLTALYST_PT_Rename_FindReplace,
    HOLTALYST_PT_Rename_Tagging,
    HOLTALYST_PT_Rename_Numbering,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
