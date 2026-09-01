import bpy
from .common import (
    is_string,
    get_object,
    get_objects,
    ao,
    so,
    select_object,
    deselect_all_objects,
    object_exists,
    make_obj_list,
)
from ..compat import GREASE_PENCIL_TYPE


def get_all_objects():
    return bpy.data.objects


def select_objects(ref):
    objref = get_objects(ref)
    for o in objref:
        o.select_set(True)


def selected_object():
    return ao()


def select_all_objects(col=None):
    if col is None:
        for co in bpy.context.scene.objects:
            co.select_set(True)
    else:
        from .collections import collection_exists, get_collection
        col_ref = col
        if is_string(col):
            if collection_exists(col):
                col_ref = get_collection(col)
        for c in col_ref.objects:
            c.select_set(True)


def select_only(ref=None):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref, True)


def deselect_object(ref):
    objref = get_object(ref)
    objref.select_set(False)


def delete_selected_objects():
    bpy.ops.object.delete()


def delete_object(ref=None):
    objref = get_object(ref)
    bpy.data.objects.remove(objref, do_unlink=True)


def delete_objects(objlist=None):
    if objlist is None:
        objlist = get_objects()
    for obj in objlist:
        ref = get_object(obj)
        bpy.data.objects.remove(ref, do_unlink=True)


def duplicate_object(tocopy, col):
    return copy_object(tocopy, col)


def copy_object(tocopy, col=None):
    from .collections import (
        get_active_collection,
        collection_exists,
        get_collection,
        create_collection,
    )
    new_obj = None
    to_copy = get_object(tocopy)
    col_ref = None
    if col is None:
        col_ref = get_active_collection()
    elif is_string(col):
        if collection_exists(col):
            col_ref = get_collection(col)
        else:
            col_ref = create_collection(col)
    else:
        col_ref = col
    new_obj = to_copy.copy()
    if new_obj.data is not None:
        new_obj.data = to_copy.data.copy()
    new_obj.animation_data_clear()
    col_ref.objects.link(new_obj)
    return new_obj


def instance_object(ref, newname=None, col=None):
    from .collections import link_object_to_collection
    deselect_all_objects()
    select_object(ref)
    bpy.ops.object.duplicate_move_linked()
    o = selected_object()
    if newname is not None:
        o.name = newname
    if col is not None:
        link_object_to_collection(o, col)
    return o


def rename_object(obj, newname):
    objref = get_object(obj) if is_string(obj) else obj
    if is_string(newname):
        objref.name = newname
        return True
    return False


def get_parent(ref=None):
    return get_object(ref).parent


def get_children(ref=None):
    return get_object(ref).children


def set_parent(child=None, parent=None):
    child = get_object(child)
    parent = get_object(parent)
    child.parent = parent
    child.matrix_parent_inverse = parent.matrix_world.inverted()


def clear_parent(ref=None, keep_location=True):
    ref = get_object(ref)
    loc = ref.matrix_world.to_translation()
    ref.parent = None
    if keep_location:
        ref.location = loc


def get_bounding_box(ref=None):
    return get_object(ref).bound_box


def get_bounding_box_corners(ref=None):
    from mathutils import Vector
    return [ref.matrix_world @ Vector(corner) for corner in get_bounding_box(ref)]


def convert_to_mesh(ref):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.convert(target='MESH')


def convert_to_grease_pencil(ref):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.convert(target=GREASE_PENCIL_TYPE)


def convert_to_curve(ref):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.convert(target='CURVE')


def create_object(name=None, col=None):
    from .collections import create_collection
    if name is None:
        name = "New Object"
    m = bpy.data.meshes.new(name)
    o = bpy.data.objects.new(name, m)
    col_ref = None
    if col is None:
        col_ref = bpy.context.view_layer.active_layer_collection.collection
    elif is_string(col):
        if col in bpy.data.collections:
            col_ref = bpy.data.collections[col]
        else:
            col_ref = create_collection(col)
    else:
        col_ref = col
    col_ref.objects.link(o)
    return o


def hide_object(ref=None):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_set(True)


def hide(ref=None):
    hide_object(ref)


def show_object(ref=None):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_set(False)


def show(ref=None):
    show_object(ref)


def unhide(ref=None):
    show_object(ref)


def hide_in_viewport(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_viewport = True


def show_in_viewport(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_viewport = False


def hide_in_render(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_render = True


def show_in_render(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_render = False


def display_as_bounds(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'BOUNDS'


def display_as_textured(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'TEXTURED'


def display_as_solid(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'SOLID'


def display_as_wire(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'WIRE'


def set_mode(ref=None, newmode=None):
    if newmode is not None:
        objref = get_object(ref)
        bpy.context.view_layer.objects.active = objref
        bpy.ops.object.mode_set(mode=newmode)


def get_mode():
    return bpy.context.mode


def set_object_mode(ref=None):
    set_mode(ref, 'OBJECT')


def object_mode(ref=None):
    set_object_mode(ref)


def set_edit_mode(ref=None):
    set_mode(ref, 'EDIT')


def edit_mode(ref=None):
    set_edit_mode(ref)


def set_sculpt_mode(ref=None):
    set_mode(ref, 'SCULPT')


def sculpt_mode(ref=None):
    set_sculpt_mode(ref)


def set_vertex_paint_mode(ref=None):
    set_mode(ref, 'VERTEX_PAINT')


def vertex_paint_mode(ref=None):
    set_vertex_paint_mode(ref)


def set_weight_paint_mode(ref=None):
    set_mode(ref, 'WEIGHT_PAINT')


def weight_paint_mode(ref=None):
    set_weight_paint_mode(ref)


def set_texture_paint_mode(ref=None):
    set_mode(ref, 'TEXTURE_PAINT')


def texture_paint_mode(ref=None):
    set_texture_paint_mode(ref)


def set_pose_mode(ref=None):
    set_mode(ref, 'POSE')


def pose_mode(ref=None):
    set_pose_mode(ref)


def shade_object_smooth(ref=None):
    objref = None
    if ref is not None:
        objref = get_object(ref) if is_string(ref) else ref
    else:
        objref = selected_object()
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.shade_smooth()


def shade_smooth(ref=None):
    shade_object_smooth(ref)


def shade_object_flat(ref=None):
    objref = None
    if ref is not None:
        objref = get_object(ref) if is_string(ref) else ref
    else:
        objref = selected_object()
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.shade_flat()


def shade_flat(ref=None):
    shade_object_flat(ref)


def set_smooth_angle(ref, degrees=60):
    import math
    objref = get_object(ref) if is_string(ref) else ref
    if not objref.data.use_auto_smooth:
        objref.data.use_auto_smooth = True
    objref.data.auto_smooth_angle = math.radians(degrees)


def set_fake_user(ref, use=True):
    ref.use_fake_user = use


def use_fake_user(ref, use=True):
    ref.use_fake_user = use


def is_any_selected_object_editable():
    return any(obj.is_editable for obj in bpy.context.selected_objects)


def get_objects_containing(ref):
    result = []
    for o in bpy.data.objects:
        if ref in o.name:
            result.append(o)
    return result


def select_objects_containing(ref):
    select_objects(get_objects_containing(ref))


def add_prefix_to_name(ref, prefix, delim="_"):
    objlist = make_obj_list(ref)
    for o in objlist:
        o.name = prefix + delim + o.name


def add_suffix_to_name(ref, suffix, delim="_"):
    objlist = make_obj_list(ref)
    for o in objlist:
        o.name = o.name + delim + suffix
