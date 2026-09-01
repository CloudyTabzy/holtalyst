import bpy
from bpy.props import (
    EnumProperty,
    IntProperty,
    StringProperty,
    BoolProperty,
    FloatProperty,
    FloatVectorProperty,
)
from bpy.types import PropertyGroup


class HTProperties(PropertyGroup):
    cleanup_mode: EnumProperty(
        name="Cleanup Mode",
        description="The mode of cleanup",
        items=[
            ('OUTLINER', "Outliner", ""),
            ('OBJECT', "Object", ""),
            ('MATERIALS', "Materials", ""),
        ],
        default="OUTLINER"
    )
    autosmooth_angle: IntProperty(
        name="Autosmooth Angle",
        description="The angle for autosmoothing",
        default=60,
        min=0,
        max=180
    )
    material_name: StringProperty(
        name="Material Name",
        description="The material to perform cleanup operations on",
        default="Material Name"
    )
    selection_mode: EnumProperty(
        name="Selection Mode",
        description="The mode of selection",
        items=[
            ('SELECT_ALLINCLUDING', "Select All Including", ""),
            ('SELECT_ALL_TYPE', "Select By Type", ""),
            ('SELECT_BY_VERTEX', "Select By Vertex Count", "")
        ],
        default="SELECT_ALLINCLUDING"
    )
    select_string: StringProperty(
        name="Select Similar String",
        description="Used for finding objects that include this in their name",
        default="Cube"
    )
    is_scene_only: BoolProperty(
        name="Is Scene Only",
        description="Toggles whether to only search in the active scene",
        default=False
    )
    is_case_sensitive: BoolProperty(
        name="Is Case Sensitive",
        description="Toggles whether to consider case when comparing names",
        default=True
    )
    select_types: EnumProperty(
        name="Select Types",
        description="Different types of object to select",
        items=[
            ('ARMATURES', "Armatures", ""),
            ('CAMERAS', "Cameras", ""),
            ('CURVES', "Curves", ""),
            ('EMPTIES', "Empties", ""),
            ('GREASE_PENCILS', "Grease Pencils", ""),
            ('HAIR', "Hair", ""),
            ('LATTICES', "Lattices", ""),
            ('LIGHTS', "Lights", ""),
            ('LIGHT_PROBES', "Light Probes", ""),
            ('MESHES', "Meshes", ""),
            ('METAS', "Metas", ""),
            ('POINT_CLOUDS', "Point Clouds", ""),
            ('SURFACES', "Surfaces", ""),
            ('TEXT', "Text", ""),
            ('VOLUMES', "Volumes", ""),
        ],
        default="MESHES"
    )
    tag_string: StringProperty(
        name="Tag String",
        description="Tag to be added as a prefix or suffix",
        default="Tag"
    )
    delimiter_string: StringProperty(
        name="Delimiter String",
        description="Delimiter to use for prefixes and suffixes",
        default="_"
    )
    vertex_count: IntProperty(
        name="Vertex Count",
        description="Vertex count for comparing objects to choose selection",
        default=10000
    )
    comparison_mode: EnumProperty(
        name="Comparison Mode",
        description="Mode to compare the vertex count",
        items=[
            ('GREATER', "Greater Than", ""),
            ('LESS', "Less Than", ""),
            ('EQUAL', "Equal To", "")
        ],
        default="GREATER"
    )
    light_add_global: FloatProperty(
        name="Light Add Global",
        description="Value to add to all lights globally",
        default=5.0
    )
    light_multiply_global: FloatProperty(
        name="Light Multiply Global",
        description="Value to multiply light sources by",
        default=1.5
    )
    light_mode: EnumProperty(
        name="Light Mode",
        description="The mode for modifying light strength",
        items=[
            ('ADDITIVE', "Additive", ""),
            ('MULTIPLICATIVE', "Multiplicative", "")
        ],
        default="ADDITIVE"
    )
    light_target: EnumProperty(
        name="Light Target",
        description="The target for lighting changes",
        items=[
            ('LIGHT_OBJECTS', "Light Objects", ""),
            ('EMISSIVE_MATERIALS', "Emissive Materials", ""),
            ('BOTH', "Both", "")
        ],
        default="LIGHT_OBJECTS"
    )
    light_mat_includes: StringProperty(
        name="Material Name Includes",
        description="A string that must be included in a material name",
        default="Emis_"
    )
    light_node_includes: StringProperty(
        name="Node Name Includes",
        description="A string that must be included in a node name",
        default="Light_"
    )
    color: FloatVectorProperty(
        subtype="COLOR",
        min=0,
        max=1,
        default=[1.0, 1.0, 1.0]
    )
    color_selected_only: BoolProperty(
        name="Selected Only",
        description="Only change color of selected light objects",
        default=True
    )
    decimate_rate: FloatProperty(
        name="Decimate Rate",
        description="The rate to quickly decimate selected object",
        default=0.1,
        min=0.0,
        max=1.0
    )


def register():
    bpy.utils.register_class(HTProperties)
    bpy.types.Scene.holtalyst = bpy.props.PointerProperty(type=HTProperties)


def unregister():
    del bpy.types.Scene.holtalyst
    bpy.utils.unregister_class(HTProperties)
