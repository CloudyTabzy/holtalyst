import bpy
from bpy.types import Panel


class HOLTALYST_PT_Cleanup_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Cleanup_Panel"
    bl_label = "Cleanup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    @classmethod
    def poll(cls, context):
        from ..preferences import is_panel_enabled
        return is_panel_enabled("show_cleanup")

    def draw_header(self, context):
        self.layout.label(text="", icon="BRUSH_DATA")

    def draw(self, context):
        pass


class HOLTALYST_PT_Cleanup_Outliner(Panel):
    bl_idname = "HOLTALYST_PT_Cleanup_Outliner"
    bl_label = "Outliner"
    bl_parent_id = "HOLTALYST_PT_Cleanup_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="OUTLINER")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.operator("outliner.organize_outliner")
        row = col.row(align=True)
        row.operator("object.convert_suffixes")
        row = col.row(align=True)
        row.operator("object.purge_unwanted_data")
        row = col.row(align=True)
        row.operator("outliner.deep_clean", text="^ Deep Clean ^")


class HOLTALYST_PT_Cleanup_Objects(Panel):
    bl_idname = "HOLTALYST_PT_Cleanup_Objects"
    bl_label = "Objects"
    bl_parent_id = "HOLTALYST_PT_Cleanup_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_DATA")

    def draw(self, context):
        layout = self.layout
        holtalyst = context.scene.holtalyst
        box = layout.box()
        col = box.column()
        if context.active_object is not None:
            if context.active_object.mode == 'EDIT':
                row = col.row()
                row.separator()
                row = col.row()
                row.operator("mesh.normals_make_consistent", text="Recalculate Normals")
                row = col.row()
                row.operator("mesh.remove_doubles", text="Merge By Distance")
                row = col.row()
                row.operator("object.shift_to_world_origin", text="Shift to World Origin")
                row = col.row()
                row.separator()
            if context.active_object.mode == 'OBJECT':
                row = col.row()
                row.label(text="( more in edit mode )")
        row = col.row()
        row.operator("mesh.customdata_custom_splitnormals_clear", text="Clean Custom Split Normals")
        row = col.row()
        row.operator("anim.keyframe_clear_v3d", text="Clear Keyframes")
        from ..compat import IS_BLENDER_5
        if not IS_BLENDER_5:
            row = col.row()
            row.label(text="Auto Smooth")
            row = col.row()
            row.prop(holtalyst, "autosmooth_angle", text="")
            row = col.row()
            row.operator("object.set_auto_smooth", text="^ Set Auto Smooth ^")
        row = col.row()
        row.label(text="Other Operations")
        row = col.row()
        row.operator("object.sync_mesh_name", text="Sync Mesh Name")
        row = col.row()
        row.operator("object.transform_apply", text="Apply Transforms")


class HOLTALYST_PT_Cleanup_Materials(Panel):
    bl_idname = "HOLTALYST_PT_Cleanup_Materials"
    bl_label = "Materials"
    bl_parent_id = "HOLTALYST_PT_Cleanup_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="MATERIAL")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()
        row = col.row()
        row.operator("object.remove_unused_slots", text="Remove Unused Slots")
        row = col.row()
        row.operator("object.fix_duplicate_node_groups", text="Fix Duplicate Node Groups")
        box2 = layout.box()
        col = box2.column()
        row = col.row()
        row.label(text="( select node groups )")
        row = col.row()
        row.operator("object.set_node_group_defaults", text="Set Defaults")
        row = col.row()
        row.operator("object.get_node_group_defaults", text="Get Defaults")


classes = (
    HOLTALYST_PT_Cleanup_Panel,
    HOLTALYST_PT_Cleanup_Outliner,
    HOLTALYST_PT_Cleanup_Objects,
    HOLTALYST_PT_Cleanup_Materials,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
