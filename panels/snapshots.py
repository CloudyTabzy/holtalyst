import bpy
from bpy.types import Panel


class HOLTALYST_PT_Snapshots_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Snapshots_Panel"
    bl_label = "Scene Snapshots"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_snapshots")

    def draw_header(self, context):
        self.layout.label(text="", icon="IMAGE_DATA")

    def draw(self, context):
        pass


class HOLTALYST_PT_Snapshots_Manage(Panel):
    bl_idname = "HOLTALYST_PT_Snapshots_Manage"
    bl_label = "Snapshots"
    bl_parent_id = "HOLTALYST_PT_Snapshots_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="FILE_IMAGE")

    def draw(self, context):
        layout = self.layout
        from ..utils.presets import list_presets
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("holtalyst.save_snapshot", text="Save Current State", icon='ADD')

        snapshots = list_presets(subdir="snapshots")
        if snapshots:
            col.separator()
            for name in snapshots:
                row = col.row(align=True)
                row.label(text=name, icon='FILE_TICK')
                op_load = row.operator("holtalyst.load_snapshot", text="", icon='FILE_REFRESH')
                op_load.snapshot_name = name
                op_del = row.operator("holtalyst.delete_snapshot", text="", icon='TRASH')
                op_del.snapshot_name = name
        else:
            col.label(text="No snapshots saved yet")


classes = (
    HOLTALYST_PT_Snapshots_Panel,
    HOLTALYST_PT_Snapshots_Manage,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
