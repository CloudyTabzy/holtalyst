import bpy
from bpy.types import Panel


class HOLTALYST_PT_Cameras_Panel(Panel):
    bl_idname = "HOLTALYST_PT_Cameras_Panel"
    bl_label = "Camera Manager"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="CAMERA_DATA")

    def draw(self, context):
        pass


class HOLTALYST_PT_Cameras_List(Panel):
    bl_idname = "HOLTALYST_PT_Cameras_List"
    bl_label = "Cameras"
    bl_parent_id = "HOLTALYST_PT_Cameras_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="OUTLINER_OB_CAMERA")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        box = layout.box()
        col = box.column()

        row = col.row(align=True)
        row.operator("holtalyst.add_camera", text="Add Camera", icon='ADD')

        cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
        if cameras:
            col.separator()
            active_cam = scene.camera
            for cam in cameras:
                row = col.row(align=True)
                is_active = active_cam and cam.name == active_cam.name
                icon = 'RADIOBUT_ON' if is_active else 'RADIOBUT_OFF'
                row.label(text=cam.name, icon=icon)
                op = row.operator("holtalyst.switch_camera", text="", icon='RESTRICT_SELECT_OFF')
                op.camera_name = cam.name
                op_render = row.operator("holtalyst.render_from_camera", text="", icon='RENDER_STILL')
                op_render.camera_name = cam.name
        else:
            col.label(text="No cameras in scene")


class HOLTALYST_PT_Cameras_Actions(Panel):
    bl_idname = "HOLTALYST_PT_Cameras_Actions"
    bl_label = "Camera Actions"
    bl_parent_id = "HOLTALYST_PT_Cameras_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="TOOL_SETTINGS")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        box = layout.box()
        col = box.column()

        if scene.camera:
            col.label(text=f"Active: {scene.camera.name}", icon='CAMERA_DATA')
        else:
            col.label(text="No active camera", icon='ERROR')

        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.set_active_camera", text="Set Active Object as Camera")
        row = col.row(align=True)
        row.operator("holtalyst.camera_to_view_selected", text="Camera to View Selected")


classes = (
    HOLTALYST_PT_Cameras_Panel,
    HOLTALYST_PT_Cameras_List,
    HOLTALYST_PT_Cameras_Actions,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
