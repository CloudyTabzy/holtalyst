import bpy

BLENDER_VERSION = bpy.app.version

IS_BLENDER_5 = BLENDER_VERSION >= (5, 0, 0)
IS_BLENDER_4_5 = BLENDER_VERSION >= (4, 5, 0)

EEVEE_ENGINE = 'BLENDER_EEVEE' if IS_BLENDER_5 else 'BLENDER_EEVEE_NEXT'

GREASE_PENCIL_TYPE = 'GREASEPENCIL' if IS_BLENDER_4_5 else 'GPENCIL'


def get_annotation_type():
    if IS_BLENDER_5:
        return bpy.types.Annotation
    return bpy.types.GreasePencil


def get_node_interface_items(node_group):
    return list(node_group.interface.items_tree)


def get_node_input_items(node_group):
    return [
        item for item in node_group.interface.items_tree
        if item.in_out == 'INPUT'
    ]


def get_node_output_items(node_group):
    return [
        item for item in node_group.interface.items_tree
        if item.in_out == 'OUTPUT'
    ]
