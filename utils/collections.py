import bpy
from .common import (
    is_string,
    get_object,
    get_objects,
    so,
    deselect_all_objects,
    select_object,
    delete_selected_objects,
)


def create_collection(name):
    if not collection_exists(name):
        bpy.data.collections.new(name)
        colref = bpy.data.collections[name]
        bpy.context.scene.collection.children.link(colref)
        return colref
    return False


def delete_collection(col, delete_objects=False, link_objects=False):
    colref = get_collection(col) if is_string(col) else col
    if delete_objects:
        deselect_all_objects()
        if len(colref.objects) > 0:
            for co in colref.objects:
                if co.name in bpy.context.view_layer.objects:
                    co.select_set(True)
            delete_selected_objects()
    else:
        deselect_all_objects()
        if len(colref.objects) > 0 and link_objects:
            for co in colref.objects:
                bpy.context.scene.collection.objects.link(co)
    bpy.data.collections.remove(colref)


def delete_objects_in_collection(col):
    colref = get_collection(col) if is_string(col) else col
    deselect_all_objects()
    for co in colref.objects:
        co.select_set(True)
    delete_selected_objects()


def delete_hierarchy(col):
    colref = get_collection(col) if is_string(col) else col
    for co in colref.children:
        if isinstance(co, bpy.types.Collection):
            delete_hierarchy(co)
    deselect_all_objects()
    delete_objects_in_collection(colref)
    delete_collection(colref, False)


def duplicate_collection(col):
    colref = get_collection(col) if is_string(col) else col
    new_name = "Copy of " + colref.name
    new_col = create_collection(new_name)
    to_copy = get_objects_from_collection(colref.name)
    for o in to_copy:
        from .objects import copy_object
        copy_object(o, new_col)
    return get_collection(new_name)


def get_objects_from_collection(col):
    if is_string(col):
        return bpy.data.collections[col].objects
    return col.objects


def get_collection(ref=None):
    if ref is None:
        return bpy.context.view_layer.active_layer_collection.collection
    if is_string(ref):
        if ref in bpy.data.collections:
            return bpy.data.collections[ref]
        return False
    return ref


def get_col(ref=None):
    return get_collection(ref)


def get_active_collection():
    return bpy.context.view_layer.active_layer_collection.collection


def set_active_collection(ref):
    colref = get_collection(ref) if is_string(ref) else ref
    hir = bpy.context.view_layer.layer_collection
    _search_layer_collection_and_set_active(colref, hir)


def select_collection(ref):
    set_active_collection(ref)


def hide_collection_viewport(ref=None):
    col = get_collection(ref)
    col.hide_viewport = True


def hide_collection(ref=None):
    hide_collection_viewport(ref)


def hide_collection_render(ref=None):
    col = get_collection(ref)
    col.hide_render = True


def hide_collection_select(ref=None):
    col = get_collection(ref)
    col.hide_select = True


def show_collection_viewport(ref=None):
    col = get_collection(ref)
    col.hide_viewport = False


def show_collection(ref=None):
    show_collection_viewport(ref)


def show_collection_render(ref=None):
    col = get_collection(ref)
    col.hide_render = False


def show_collection_select(ref=None):
    col = get_collection(ref)
    col.hide_select = False


def unhide_collection_viewport(ref=None):
    show_collection_viewport(ref)


def unhide_collection(ref=None):
    unhide_collection_viewport(ref)


def unhide_collection_render(ref=None):
    show_collection_render(ref)


def unhide_collection_select(ref=None):
    show_collection_select(ref)


def _search_layer_collection_and_set_active(colref, hir):
    if isinstance(hir, bpy.types.LayerCollection):
        if hir.collection == colref:
            bpy.context.view_layer.active_layer_collection = hir
        else:
            for child in hir.children:
                _search_layer_collection_and_set_active(colref, child)


def get_all_collections():
    return bpy.data.collections


def get_list_of_collections():
    return get_all_collections()


def link_object_to_collection(ref, col):
    if is_string(col):
        objref = get_object(ref)
        bpy.data.collections[col].objects.link(objref)
    else:
        if not isinstance(col, bool):
            objref = get_object(ref)
            col.objects.link(objref)


def link_objects_to_collection(ref, col):
    objs = get_objects(ref)
    if is_string(col):
        for o in objs:
            bpy.data.collections[col].objects.link(o)
    else:
        for o in objs:
            col.objects.link(o)


def unlink_object_from_collection(ref, col):
    objref = get_object(ref)
    if is_string(col):
        bpy.data.collections[col].objects.unlink(objref)
    else:
        col.objects.unlink(objref)


def unlink_objects_from_collection(ref, col):
    objs = get_objects(ref)
    colref = get_collection(col) if is_string(col) else col
    for o in objs:
        colref.objects.unlink(o)


def move_object_to_collection(ref, col):
    objref = get_object(ref)
    colref = get_collection(col) if is_string(col) else col
    for c in objref.users_collection:
        c.objects.unlink(objref)
    link_object_to_collection(objref, colref)


def move_objects_to_collection(ref, col):
    objs = get_objects(ref)
    colref = get_collection(col) if is_string(col) else col
    for o in objs:
        if o.is_editable:
            for c in o.users_collection:
                c.objects.unlink(o)
            link_object_to_collection(o, colref)


def get_object_collection(ref):
    objref = get_object(ref)
    return objref.users_collection[0]


def get_object_collections(ref):
    objref = get_object(ref)
    return objref.users_collection


def collection_exists(col):
    if is_string(col):
        return col in bpy.data.collections
    return col.name in bpy.data.collections
