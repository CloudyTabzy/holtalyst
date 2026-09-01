import bpy
from bpy.types import Operator


class HOLTALYST_OT_AddLightIntensityGlobal(Operator):
    bl_idname = "object.add_light_intensity_global"
    bl_label = "Add Light Intensity Global"
    bl_description = "Adds intensity to all lights in the scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import select_all_lights, light_power_add, get_all_materials, get_nodes, get_index_of_input
        holtalyst = context.scene.holtalyst
        if holtalyst.light_target in ("LIGHT_OBJECTS", "BOTH"):
            select_all_lights()
            light_power_add(holtalyst.light_add_global)
        if holtalyst.light_target in ("EMISSIVE_MATERIALS", "BOTH"):
            for m in get_all_materials():
                if holtalyst.light_mat_includes in m.name:
                    for n in get_nodes(m):
                        if n.type == 'EMISSION' and holtalyst.light_node_includes in n.name:
                            n.inputs[1].default_value += holtalyst.light_add_global
                        if n.type == 'BSDF_PRINCIPLED' and holtalyst.light_node_includes in n.name:
                            s_index = get_index_of_input(n, "Emission Strength")
                            n.inputs[s_index].default_value += holtalyst.light_add_global
        return {'FINISHED'}


class HOLTALYST_OT_SubtractLightIntensityGlobal(Operator):
    bl_idname = "object.subtract_light_intensity_global"
    bl_label = "Subtract Light Intensity Global"
    bl_description = "Subtracts intensity from all lights in the scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import select_all_lights, light_power_add, get_all_materials, get_nodes, get_index_of_input
        holtalyst = context.scene.holtalyst
        if holtalyst.light_target in ("LIGHT_OBJECTS", "BOTH"):
            select_all_lights()
            light_power_add(-holtalyst.light_add_global)
        if holtalyst.light_target in ("EMISSIVE_MATERIALS", "BOTH"):
            for m in get_all_materials():
                if holtalyst.light_mat_includes in m.name:
                    for n in get_nodes(m):
                        if n.type == 'EMISSION' and holtalyst.light_node_includes in n.name:
                            n.inputs[1].default_value -= holtalyst.light_add_global
                        if n.type == 'BSDF_PRINCIPLED' and holtalyst.light_node_includes in n.name:
                            s_index = get_index_of_input(n, "Emission Strength")
                            n.inputs[s_index].default_value -= holtalyst.light_add_global
        return {'FINISHED'}


class HOLTALYST_OT_MultiplyLightIntensityGlobal(Operator):
    bl_idname = "object.multiply_light_intensity_global"
    bl_label = "Multiply Light Intensity Global"
    bl_description = "Multiplies intensity of all lights in the scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import select_all_lights, light_power_multiply, get_all_materials, get_nodes, get_index_of_input
        holtalyst = context.scene.holtalyst
        if holtalyst.light_target in ("LIGHT_OBJECTS", "BOTH"):
            select_all_lights()
            light_power_multiply(holtalyst.light_multiply_global)
        if holtalyst.light_target in ("EMISSIVE_MATERIALS", "BOTH"):
            for m in get_all_materials():
                if holtalyst.light_mat_includes in m.name:
                    for n in get_nodes(m):
                        if n.type == 'EMISSION' and holtalyst.light_node_includes in n.name:
                            n.inputs[1].default_value *= holtalyst.light_multiply_global
                        if n.type == 'BSDF_PRINCIPLED' and holtalyst.light_node_includes in n.name:
                            s_index = get_index_of_input(n, "Emission Strength")
                            n.inputs[s_index].default_value *= holtalyst.light_multiply_global
        return {'FINISHED'}


class HOLTALYST_OT_SetLightColor(Operator):
    bl_idname = "object.set_light_color"
    bl_label = "Set Light Color"
    bl_description = "Sets the color of selected lights to the RGB property"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import so
        holtalyst = context.scene.holtalyst
        if holtalyst.color_selected_only:
            for o in so():
                if o.type == "LIGHT":
                    o.data.color = holtalyst.color
        else:
            for l in bpy.data.lights:
                l.color = holtalyst.color
        return {'FINISHED'}


class HOLTALYST_OT_RandomizeLightColor(Operator):
    bl_idname = "object.randomize_light_color"
    bl_label = "Randomize Light Color"
    bl_description = "Randomizes the light color for selected light objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from random import uniform
        from ..utils import so
        holtalyst = context.scene.holtalyst
        if holtalyst.color_selected_only:
            for o in so():
                if o.type == "LIGHT":
                    o.data.color.r = uniform(0, 1)
                    o.data.color.g = uniform(0, 1)
                    o.data.color.b = uniform(0, 1)
        else:
            for l in bpy.data.lights:
                l.color.r = uniform(0, 1)
                l.color.g = uniform(0, 1)
                l.color.b = uniform(0, 1)
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_AddLightIntensityGlobal,
    HOLTALYST_OT_SubtractLightIntensityGlobal,
    HOLTALYST_OT_MultiplyLightIntensityGlobal,
    HOLTALYST_OT_SetLightColor,
    HOLTALYST_OT_RandomizeLightColor,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
