import bpy
from bpy.types import Operator
from bpy.props import StringProperty, FloatProperty


class HOLTALYST_OT_AddCamera(Operator):
    bl_idname = "holtalyst.add_camera"
    bl_label = "Add Camera"
    bl_description = "Add a new camera to the scene"
    bl_options = {'REGISTER', 'UNDO'}

    camera_name: StringProperty(name="Camera Name", default="Camera")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        bpy.ops.object.camera_add()
        cam = context.active_object
        cam.name = self.camera_name
        if cam.data:
            cam.data.name = self.camera_name
        self.report({'INFO'}, f"Added camera: {self.camera_name}")
        return {'FINISHED'}


class HOLTALYST_OT_SwitchCamera(Operator):
    bl_idname = "holtalyst.switch_camera"
    bl_label = "Switch Camera"
    bl_description = "Switch to a specific camera"
    bl_options = {'REGISTER'}

    camera_name: StringProperty(name="Camera Name", default="")

    def execute(self, context):
        if self.camera_name not in bpy.data.objects:
            self.report({'ERROR'}, f"Camera not found: {self.camera_name}")
            return {'CANCELLED'}
        cam = bpy.data.objects[self.camera_name]
        if cam.type != 'CAMERA':
            self.report({'ERROR'}, f"Not a camera: {self.camera_name}")
            return {'CANCELLED'}
        context.scene.camera = cam
        self.report({'INFO'}, f"Switched to: {self.camera_name}")
        return {'FINISHED'}


class HOLTALYST_OT_SetActiveCamera(Operator):
    bl_idname = "holtalyst.set_active_camera"
    bl_label = "Set Active as Camera"
    bl_description = "Set the active object as the scene camera"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.active_object
        if obj is None or obj.type != 'CAMERA':
            self.report({'ERROR'}, "Active object is not a camera")
            return {'CANCELLED'}
        context.scene.camera = obj
        self.report({'INFO'}, f"Scene camera set to: {obj.name}")
        return {'FINISHED'}


class HOLTALYST_OT_CameraToViewSelected(Operator):
    bl_idname = "holtalyst.camera_to_view_selected"
    bl_label = "Camera to View Selected"
    bl_description = "Move the camera to frame selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.camera is None:
            self.report({'ERROR'}, "No active camera in scene")
            return {'CANCELLED'}
        bpy.ops.view3d.camera_to_view_selected()
        return {'FINISHED'}


class HOLTALYST_OT_RenderFromCamera(Operator):
    bl_idname = "holtalyst.render_from_camera"
    bl_label = "Render from Camera"
    bl_description = "Render the scene from the specified camera"
    bl_options = {'REGISTER'}

    camera_name: StringProperty(name="Camera Name", default="")

    def execute(self, context):
        if self.camera_name not in bpy.data.objects:
            self.report({'ERROR'}, f"Camera not found: {self.camera_name}")
            return {'CANCELLED'}
        cam = bpy.data.objects[self.camera_name]
        if cam.type != 'CAMERA':
            self.report({'ERROR'}, f"Not a camera: {self.camera_name}")
            return {'CANCELLED'}
        old_cam = context.scene.camera
        context.scene.camera = cam
        bpy.ops.render.render(write_still=True)
        context.scene.camera = old_cam
        self.report({'INFO'}, f"Rendered from: {self.camera_name}")
        return {'FINISHED'}


class HOLTALYST_OT_ListCameras(Operator):
    bl_idname = "holtalyst.list_cameras"
    bl_label = "List Cameras"
    bl_description = "Print all cameras in the scene"
    bl_options = {'REGISTER'}

    def execute(self, context):
        cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
        if not cameras:
            self.report({'INFO'}, "No cameras in scene")
        else:
            names = ", ".join(c.name for c in cameras)
            self.report({'INFO'}, f"Cameras: {names}")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_AddCamera,
    HOLTALYST_OT_SwitchCamera,
    HOLTALYST_OT_SetActiveCamera,
    HOLTALYST_OT_CameraToViewSelected,
    HOLTALYST_OT_RenderFromCamera,
    HOLTALYST_OT_ListCameras,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
