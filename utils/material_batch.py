import bpy
from .common import is_string, get_object, get_objects, ao, so


def replace_material_on_objects(old_mat, new_mat, selected_only=True):
    old_ref = bpy.data.materials.get(old_mat) if is_string(old_mat) else old_mat
    new_ref = bpy.data.materials.get(new_mat) if is_string(new_mat) else new_mat
    if old_ref is None or new_ref is None:
        return 0
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        for i, slot in enumerate(obj.material_slots):
            if slot.material == old_ref:
                slot.material = new_ref
                count += 1
    return count


def replace_all_materials_on_objects(new_mat, selected_only=True):
    new_ref = bpy.data.materials.get(new_mat) if is_string(new_mat) else new_mat
    if new_ref is None:
        return 0
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        for slot in obj.material_slots:
            if slot.material is not None:
                slot.material = new_ref
                count += 1
    return count


def merge_duplicate_materials(selected_only=True):
    seen = {}
    merge_map = {}
    for mat in bpy.data.materials:
        base_name = mat.name.split('.')[0]
        if base_name in seen:
            merge_map[mat.name] = seen[base_name]
        else:
            seen[base_name] = mat

    if not merge_map:
        return 0

    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        for slot in obj.material_slots:
            if slot.material and slot.material.name in merge_map:
                slot.material = merge_map[slot.material.name]
                count += 1

    for old_name, new_mat in merge_map.items():
        if old_name in bpy.data.materials:
            bpy.data.materials.remove(bpy.data.materials[old_name])

    return count


def get_material_usage():
    usage = {}
    for obj in bpy.data.objects:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        for slot in obj.material_slots:
            if slot.material:
                name = slot.material.name
                if name not in usage:
                    usage[name] = []
                usage[name].append(obj.name)
    return usage


def remove_material_from_selection(mat_name, selected_only=True):
    mat_ref = bpy.data.materials.get(mat_name)
    if mat_ref is None:
        return 0
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        for i, slot in enumerate(obj.material_slots):
            if slot.material == mat_ref:
                obj.data.materials.pop(index=i)
                count += 1
                break
    return count


def add_material_to_selection(mat_name, selected_only=True):
    mat_ref = bpy.data.materials.get(mat_name)
    if mat_ref is None:
        mat_ref = bpy.data.materials.new(name=mat_name)
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        obj.data.materials.append(mat_ref)
        count += 1
    return count
