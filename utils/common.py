import bpy
from mathutils import Vector


def is_string(ref):
    return isinstance(ref, str)


def get_scene():
    return bpy.context.scene


def get_active_object():
    return bpy.context.active_object


def ao():
    return get_active_object()


def get_selected_objects():
    return bpy.context.selected_objects


def so():
    return get_selected_objects()


def get_object(ref):
    if ref is None:
        return ao()
    if is_string(ref):
        if ref in bpy.data.objects:
            return bpy.data.objects[ref]
        return None
    return ref


def get_objects(ref=None):
    if ref is None:
        return so()
    if isinstance(ref, list):
        if len(ref) > 0:
            if isinstance(ref[0], bpy.types.Object):
                return ref
            elif isinstance(ref[0], str):
                return [bpy.data.objects[n] for n in ref if n in bpy.data.objects]
    if is_string(ref):
        if ref in bpy.data.objects:
            return [bpy.data.objects[ref]]
        return []
    if isinstance(ref, bpy.types.Object):
        return [ref]
    return []


def make_obj_list(ref):
    if ref is None:
        return [get_object(ref)]
    return get_objects(ref)


def make_vector(data):
    from mathutils import Vector
    return Vector((data[0], data[1], data[2]))


def object_exists(ref):
    if is_string(ref):
        return ref in bpy.data.objects
    return ref.name in bpy.data.objects


def select_object(ref, make_active=True):
    objref = get_object(ref)
    objref.select_set(True)
    if make_active:
        bpy.context.view_layer.objects.active = objref


def deselect_all_objects():
    for ob in so():
        ob.select_set(False)


def set_active_object(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref


def get_median_point_of_objects(objs):
    point_loc = Vector()
    for obj in objs:
        point_loc += obj.location
    point_loc /= len(objs)
    return point_loc


def clear_unwanted_data():
    for block in bpy.data.lights:
        if block.users == 0:
            bpy.data.lights.remove(block)
    for block in bpy.data.curves:
        if block.users == 0:
            bpy.data.curves.remove(block)
    for block in bpy.data.cameras:
        if block.users == 0:
            bpy.data.cameras.remove(block)
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)
    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)


def delete_selected_objects():
    bpy.ops.object.delete()
