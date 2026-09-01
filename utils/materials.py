import bpy
from .common import is_string, get_object, ao, get_objects


def create_material(name):
    return bpy.data.materials.new(name)


def material_exists(ref):
    if is_string(ref):
        return ref in bpy.data.materials
    return ref.name in bpy.data.materials


def delete_material(ref):
    matref = get_material(ref) if is_string(ref) else ref
    bpy.data.materials.remove(matref)


def get_material(matname=None):
    if matname is None:
        active = ao()
        if len(active.material_slots) > 0:
            return active.material_slots[0].material
    else:
        for m in bpy.data.materials:
            if m.name == matname:
                return m
    return None


def add_material_to_object(ref, mat):
    objref = get_object(ref) if is_string(ref) else ref
    matref = get_material(mat) if is_string(mat) else mat
    if matref is not None:
        objref.data.materials.append(matref)


def remove_material_from_object(ref, matname):
    objref = get_object(ref) if is_string(ref) else ref
    matindex = objref.data.materials.find(matname)
    if matname in objref.data.materials:
        objref.data.materials.pop(index=matindex)


def remove_material(ref, matname):
    return remove_material_from_object(ref, matname)


def remove_materials(ref=None):
    objrefs = get_objects(ref)
    for o in objrefs:
        if len(o.material_slots) > 0:
            names = [m.name for m in o.material_slots]
            for n in names:
                remove_material_from_object(o, n)


def remove_all_materials(ref=None):
    remove_materials(ref)


def remove_unused_material_slots(ref=None):
    objrefs = get_objects(ref)
    for o in objrefs:
        data = o.data
        tmp = data.materials.items()
        data.materials.clear()
        for item in tmp:
            data.materials.append(item[1])


def remove_unused_slots(ref=None):
    remove_unused_material_slots(ref)


def get_all_materials():
    return bpy.data.materials


def get_materials(ref=None):
    if ref is not None:
        return get_materials_from_object(ref)
    return bpy.data.materials


def get_material_from_object(ref):
    objref = get_object(ref)
    return objref.material_slots[0].material


def get_materials_from_object(ref):
    objref = get_object(ref)
    return [m.material for m in objref.material_slots]


def get_material_names_from_object(ref):
    objref = get_object(ref)
    return [m.name for m in objref.material_slots]


def get_materials_containing(name, ref=None):
    results = []
    if ref is not None:
        mats = get_materials_from_object(ref)
        for m in mats:
            if name in m.name:
                results.append(m)
    else:
        for m in bpy.data.materials:
            if name in m.name:
                results.append(m)
    return results
