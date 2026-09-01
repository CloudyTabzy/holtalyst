import os
import bpy
from ..compat import IS_BLENDER_5


def _ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path


def get_export_path(base_dir, filename, ext):
    _ensure_dir(base_dir)
    return os.path.join(base_dir, f"{filename}{ext}")


def export_selected_obj(filepath, use_selection=True, apply_transforms=False, **kwargs):
    if apply_transforms:
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.wm.obj_export(
        filepath=filepath,
        export_selected_objects=use_selection,
        **kwargs,
    )


def export_selected_gltf(filepath, use_selection=True, apply_transforms=False, **kwargs):
    if apply_transforms:
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.export_scene.gltf(
        filepath=filepath,
        use_selection=use_selection,
        **kwargs,
    )


def export_selected_fbx(filepath, use_selection=True, apply_transforms=False, **kwargs):
    if apply_transforms:
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        use_selection=use_selection,
        **kwargs,
    )


def export_selected_stl(filepath, use_selection=True, apply_transforms=False, **kwargs):
    if apply_transforms:
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.wm.stl_export(
        filepath=filepath,
        export_selected_objects=use_selection,
        **kwargs,
    )


EXPORT_FORMATS = {
    'OBJ': {
        'ext': '.obj',
        'fn': export_selected_obj,
        'label': 'Wavefront (.obj)',
    },
    'GLTF': {
        'ext': '.glb',
        'fn': export_selected_gltf,
        'label': 'glTF 2.0 (.glb)',
    },
    'FBX': {
        'ext': '.fbx',
        'fn': export_selected_fbx,
        'label': 'FBX (.fbx)',
    },
    'STL': {
        'ext': '.stl',
        'fn': export_selected_stl,
        'label': 'STL (.stl)',
    },
}


def batch_export_objects(base_dir, fmt='OBJ', apply_transforms=False, selected_only=True):
    fmt_info = EXPORT_FORMATS.get(fmt)
    if fmt_info is None:
        return 0, []

    ext = fmt_info['ext']
    fn = fmt_info['fn']
    _ensure_dir(base_dir)

    targets = bpy.context.selected_objects if selected_only else bpy.data.objects
    exported = []
    for obj in targets:
        if obj.type not in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            continue
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        filepath = os.path.join(base_dir, f"{obj.name}{ext}")
        fn(filepath, use_selection=True, apply_transforms=apply_transforms)
        exported.append(filepath)

    return len(exported), exported


def batch_export_collections(base_dir, fmt='OBJ', apply_transforms=False):
    fmt_info = EXPORT_FORMATS.get(fmt)
    if fmt_info is None:
        return 0, []

    ext = fmt_info['ext']
    fn = fmt_info['fn']
    _ensure_dir(base_dir)

    exported = []
    for col in bpy.data.collections:
        if len(col.objects) == 0:
            continue
        bpy.ops.object.select_all(action='DESELECT')
        for obj in col.objects:
            obj.select_set(True)
        filepath = os.path.join(base_dir, f"{col.name}{ext}")
        fn(filepath, use_selection=True, apply_transforms=apply_transforms)
        exported.append(filepath)

    return len(exported), exported
