import bpy
from .common import is_string, get_object, deselect_all_objects, select_object
from ..compat import GREASE_PENCIL_TYPE


def select_all_meshes():
    bpy.ops.object.select_by_type(type='MESH')


def select_all_curves():
    bpy.ops.object.select_by_type(type='CURVE')


def select_all_surfaces():
    bpy.ops.object.select_by_type(type='SURFACE')


def select_all_metas():
    bpy.ops.object.select_by_type(type='META')


def select_all_text():
    bpy.ops.object.select_by_type(type='FONT')


def select_all_hair():
    bpy.ops.object.select_by_type(type='CURVES')


def select_all_point_clouds():
    bpy.ops.object.select_by_type(type='POINTCLOUD')


def select_all_volumes():
    bpy.ops.object.select_by_type(type='VOLUME')


def select_all_armatures():
    bpy.ops.object.select_by_type(type='ARMATURE')


def select_all_lattices():
    bpy.ops.object.select_by_type(type='LATTICE')


def select_all_empties():
    bpy.ops.object.select_by_type(type='EMPTY')


def select_all_grease_pencils():
    bpy.ops.object.select_by_type(type=GREASE_PENCIL_TYPE)


def select_all_cameras():
    bpy.ops.object.select_by_type(type='CAMERA')


def select_all_lights():
    bpy.ops.object.select_by_type(type='LIGHT')


def select_all_speakers():
    bpy.ops.object.select_by_type(type='SPEAKER')


def select_all_light_probes():
    bpy.ops.object.select_by_type(type='LIGHT_PROBE')


def invert_selection():
    bpy.ops.object.select_all(action='INVERT')


def get_objects_with_modifiers():
    objlist = []
    for obj in bpy.data.objects:
        if len(obj.modifiers) > 0:
            objlist.append(obj)
    return objlist


def select_objects_with_modifiers():
    deselect_all_objects()
    for obj in bpy.data.objects:
        if len(obj.modifiers) > 0:
            select_object(obj)


def get_objects_including(include, case_sensitive=True):
    objlist = []
    for o in bpy.context.view_layer.objects:
        if case_sensitive:
            if include in o.name:
                objlist.append(o)
        else:
            if include.lower() in o.name.lower():
                objlist.append(o)
    return objlist


def select_objects_including(include, case_sensitive=True):
    for o in bpy.context.view_layer.objects:
        if case_sensitive:
            if include in o.name:
                o.select_set(True)
        else:
            if include.lower() in o.name.lower():
                o.select_set(True)


def get_objects_by_vertex(count=0, mode="EQUAL"):
    cmode = mode.upper()
    objlist = []
    for o in bpy.data.objects:
        if isinstance(o.data, bpy.types.Mesh):
            if cmode in ("EQUAL", "SAME"):
                if len(o.data.vertices) == count:
                    objlist.append(o)
            if cmode in ("GREATER", "MORE"):
                if len(o.data.vertices) > count:
                    objlist.append(o)
            if cmode in ("LESS", "FEWER"):
                if len(o.data.vertices) < count:
                    objlist.append(o)
    return objlist


def select_objects_by_vertex(count=0, mode="EQUAL"):
    objs = get_objects_by_vertex(count, mode)
    for o in objs:
        o.select_set(True)
