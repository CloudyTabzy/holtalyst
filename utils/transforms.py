import math
from mathutils import Vector, Matrix
from .common import (
    get_object,
    get_objects,
    make_obj_list,
    deselect_all_objects,
    select_object,
    get_median_point_of_objects,
    get_scene,
)


def location(ref=None, loc=None):
    objref = get_object(ref)
    if loc is not None:
        objref.location = Vector((loc[0], loc[1], loc[2]))
    else:
        return objref.location


def rotation(ref=None, rot=None):
    objref = get_object(ref)
    if rot is not None:
        objref.rotation_euler = Vector((rot[0], rot[1], rot[2]))
    else:
        return objref.rotation_euler


def scale(ref=None, scale=None):
    objref = get_object(ref)
    if scale is not None:
        objref.scale = Vector((scale[0], scale[1], scale[2]))
    else:
        return objref.scale


def dimensions(ref=None, dim=None):
    objref = get_object(ref)
    if dim is not None:
        objref.dimensions = Vector((dim[0], dim[1], dim[2]))
    else:
        return objref.dimensions


def apply_location(ref=None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    import bpy
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


def apply_rotation(ref=None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    import bpy
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


def apply_scale(ref=None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    import bpy
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)


def apply_all_transforms(ref=None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    import bpy
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


def apply_rotation_and_scale(ref=None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    import bpy
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)


def translate_vector(vec=Vector(), ref=None):
    objs = make_obj_list(ref)
    for obj in objs:
        obj.location[0] += vec[0]
        obj.location[1] += vec[1]
        obj.location[2] += vec[2]


def translate_along_axis(val, axis, ref=None):
    objs = make_obj_list(ref)
    axis.normalize()
    for obj in objs:
        obj.location[0] += (val * axis[0])
        obj.location[1] += (val * axis[1])
        obj.location[2] += (val * axis[2])


def move_along_axis(val, axis, ref=None):
    translate_along_axis(val, axis, ref)


def translate_along_x(val, ref=None):
    translate_along_axis(val, Vector((1.0, 0.0, 0.0)), ref)


def move_along_x(val, ref=None):
    translate_along_x(val, ref)


def translate_along_y(val, ref=None):
    translate_along_axis(val, Vector((0.0, 1.0, 0.0)), ref)


def move_along_y(val, ref=None):
    translate_along_y(val, ref)


def translate_along_z(val, ref=None):
    translate_along_axis(val, Vector((0.0, 0.0, 1.0)), ref)


def move_along_z(val, ref=None):
    translate_along_z(val, ref)


def translate_along_local_axis(val, axis, ref=None):
    objs = make_obj_list(ref)
    axis.normalize()
    for obj in objs:
        tempaxis = axis.copy()
        tempaxis.rotate(obj.rotation_euler)
        obj.location[0] += (val * tempaxis[0])
        obj.location[1] += (val * tempaxis[1])
        obj.location[2] += (val * tempaxis[2])


def translate_along_local_x(val, ref=None):
    translate_along_local_axis(val, Vector((1.0, 0.0, 0.0)), ref)


def move_along_local_x(val, ref=None):
    translate_along_local_x(val, ref)


def translate_along_local_y(val, ref=None):
    translate_along_local_axis(val, Vector((0.0, 1.0, 0.0)), ref)


def move_along_local_y(val, ref=None):
    translate_along_local_y(val, ref)


def translate_along_local_z(val, ref=None):
    translate_along_local_axis(val, Vector((0.0, 0.0, 1.0)), ref)


def move_along_local_z(val, ref=None):
    translate_along_local_z(val, ref)


def rotate_vector(vec=Vector(), ref=None):
    objs = make_obj_list(ref)
    for obj in objs:
        obj.rotation_euler[0] += vec[0]
        obj.rotation_euler[1] += vec[1]
        obj.rotation_euler[2] += vec[2]


def rotate_around_axis(deg, axis=Vector(), ref=None, point=None):
    from .cursor import get_cursor_location
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    axis.normalize()
    for obj in objs:
        mat = (Matrix.Translation(pointref) @ Matrix.Rotation(math.radians(deg), 4, axis) @ Matrix.Translation(-pointref))
        obj.matrix_world = mat @ obj.matrix_world


def rotate_around_global_x(deg, ref=None, point=None):
    rotate_around_axis(deg, Vector((1.0, 0.0, 0.0)), ref, point)


def rotate_around_global_y(deg, ref=None, point=None):
    rotate_around_axis(deg, Vector((0.0, 1.0, 0.0)), ref, point)


def rotate_around_global_z(deg, ref=None, point=None):
    rotate_around_axis(deg, Vector((0.0, 0.0, 1.0)), ref, point)


def rotate_around_x(deg, ref=None, point=None):
    rotate_around_global_x(deg, ref, point)


def rotate_around_y(deg, ref=None, point=None):
    rotate_around_global_y(deg, ref, point)


def rotate_around_z(deg, ref=None, point=None):
    rotate_around_global_z(deg, ref, point)


def rotate_around_local_axis(deg, axis=Vector(), ref=None, point=None):
    from .cursor import get_cursor_location
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    axis.normalize()
    for obj in objs:
        tempaxis = axis.copy()
        tempaxis.rotate(obj.rotation_euler)
        mat = (Matrix.Translation(pointref) @ Matrix.Rotation(math.radians(deg), 4, tempaxis) @ Matrix.Translation(-pointref))
        obj.matrix_world = mat @ obj.matrix_world


def rotate_around_local_x(deg, ref=None, point=None):
    rotate_around_local_axis(deg, Vector((1.0, 0.0, 0.0)), ref, point)


def rotate_around_local_y(deg, ref=None, point=None):
    rotate_around_local_axis(deg, Vector((0.0, 1.0, 0.0)), ref, point)


def rotate_around_local_z(deg, ref=None, point=None):
    rotate_around_local_axis(deg, Vector((0.0, 0.0, 1.0)), ref, point)


def scale_vector(vec, ref=None):
    objs = make_obj_list(ref)
    for obj in objs:
        obj.scale[0] *= vec[0]
        obj.scale[1] *= vec[1]
        obj.scale[2] *= vec[2]


def scale_uniform(val, ref=None):
    scale_vector(Vector((val, val, val)), ref)


def set_geometry_to_origin(ref=None):
    import bpy
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')


def geometry_to_origin(ref=None):
    set_geometry_to_origin(ref)


def set_origin_to_geometry(ref=None):
    import bpy
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


def origin_to_geometry(ref=None):
    set_origin_to_geometry(ref)


def set_origin_to_cursor(ref=None):
    import bpy
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')


def origin_to_cursor(ref=None):
    set_origin_to_cursor(ref)


def set_origin_to_centermass_surface(ref=None):
    import bpy
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')


def origin_to_centermass_surface(ref=None):
    set_origin_to_centermass_surface(ref)


def set_origin_to_centermass_volume(ref=None):
    import bpy
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')


def origin_to_centermass_volume(ref=None):
    set_origin_to_centermass_volume(ref)


def smart_apply_location(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


def smart_apply_rotation(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


def smart_apply_scale(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)


def smart_apply_rotation_scale(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)


def smart_apply_all(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


def apply_transforms_keep_children(ref=None):
    import bpy
    objref = get_object(ref)
    if objref is None:
        return
    children = list(objref.children)
    child_offsets = {}
    for child in children:
        child_offsets[child.name] = {
            'location': child.location.copy(),
            'matrix': child.matrix_world.copy(),
        }
    select_object(objref)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    for child in children:
        if child.name in child_offsets:
            child.matrix_world = child_offsets[child.name]['matrix']


def clear_location(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.location_clear()


def clear_rotation(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.rotation_clear()


def clear_scale(ref=None):
    import bpy
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.scale_clear()
