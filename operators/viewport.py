import bpy
from bpy.types import Operator
from bpy.props import EnumProperty


class HOLTALYST_OT_SetViewportShading(Operator):
    bl_idname = "holtalyst.set_viewport_shading"
    bl_label = "Set Viewport Shading"
    bl_description = "Set the viewport shading mode"
    bl_options = {'REGISTER'}

    shading_type: EnumProperty(
        name="Shading Type",
        items=[
            ('WIREFRAME', "Wireframe", ""),
            ('SOLID', "Solid", ""),
            ('MATERIAL', "Material Preview", ""),
            ('RENDERED', "Rendered", ""),
        ],
        default='SOLID',
    )

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = self.shading_type
        return {'FINISHED'}


class HOLTALYST_OT_SetDisplayType(Operator):
    bl_idname = "holtalyst.set_display_type"
    bl_label = "Set Display Type"
    bl_description = "Set the display type for selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    display_type: EnumProperty(
        name="Display Type",
        items=[
            ('BOUNDS', "Bounds", ""),
            ('WIRE', "Wireframe", ""),
            ('SOLID', "Solid", ""),
            ('TEXTURED', "Textured", ""),
        ],
        default='SOLID',
    )

    def execute(self, context):
        for obj in context.selected_objects:
            obj.display_type = self.display_type
        return {'FINISHED'}


class HOLTALYST_OT_SetWireframeAll(Operator):
    bl_idname = "holtalyst.set_wireframe_all"
    bl_label = "Show All Wireframe"
    bl_description = "Show wireframe overlay on all objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.data.objects:
            obj.show_wire = True
        return {'FINISHED'}


class HOLTALYST_OT_SetSolidAll(Operator):
    bl_idname = "holtalyst.set_solid_all"
    bl_label = "Show All Solid"
    bl_description = "Show solid overlay on all objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.data.objects:
            obj.show_wire = False
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SetViewportShading,
    HOLTALYST_OT_SetDisplayType,
    HOLTALYST_OT_SetWireframeAll,
    HOLTALYST_OT_SetSolidAll,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
