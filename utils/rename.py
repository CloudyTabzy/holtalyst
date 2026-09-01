import bpy
from .common import is_string, get_object, get_objects


def batch_rename_objects(find, replace, case_sensitive=True, selected_only=False):
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        old_name = obj.name
        if case_sensitive:
            new_name = old_name.replace(find, replace)
        else:
            import re
            new_name = re.sub(re.escape(find), replace, old_name, flags=re.IGNORECASE)
        if new_name != old_name:
            obj.name = new_name
            count += 1
    return count


def batch_rename_materials(find, replace, case_sensitive=True):
    count = 0
    for mat in bpy.data.materials:
        old_name = mat.name
        if case_sensitive:
            new_name = old_name.replace(find, replace)
        else:
            import re
            new_name = re.sub(re.escape(find), replace, old_name, flags=re.IGNORECASE)
        if new_name != old_name:
            mat.name = new_name
            count += 1
    return count


def batch_rename_meshes(find, replace, case_sensitive=True):
    count = 0
    for mesh in bpy.data.meshes:
        old_name = mesh.name
        if case_sensitive:
            new_name = old_name.replace(find, replace)
        else:
            import re
            new_name = re.sub(re.escape(find), replace, old_name, flags=re.IGNORECASE)
        if new_name != old_name:
            mesh.name = new_name
            count += 1
    return count


def batch_rename_collections(find, replace, case_sensitive=True):
    count = 0
    for col in bpy.data.collections:
        old_name = col.name
        if case_sensitive:
            new_name = old_name.replace(find, replace)
        else:
            import re
            new_name = re.sub(re.escape(find), replace, old_name, flags=re.IGNORECASE)
        if new_name != old_name:
            col.name = new_name
            count += 1
    return count


def add_prefix_to_selected(prefix, delim="_"):
    count = 0
    for obj in bpy.context.selected_objects:
        obj.name = prefix + delim + obj.name
        count += 1
    return count


def add_suffix_to_selected(suffix, delim="_"):
    count = 0
    for obj in bpy.context.selected_objects:
        obj.name = obj.name + delim + suffix
        count += 1
    return count


def rename_with_numbering(base_name, start=1, step=1, selected_only=True):
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    for i, obj in enumerate(targets):
        obj.name = f"{base_name}_{start + i * step:03d}"
    return len(targets)


def strip_trailing_numbers(selected_only=True):
    import re
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        new_name = re.sub(r'\.\d+$', '', obj.name)
        if new_name != obj.name:
            if new_name not in bpy.data.objects:
                obj.name = new_name
                count += 1
    return count


def rename_data_to_match(selected_only=True):
    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    count = 0
    for obj in targets:
        if obj.data and obj.data.name != obj.name:
            obj.data.name = obj.name
            count += 1
    return count
