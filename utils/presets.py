import json
import os
import bpy


def _get_presets_dir(subdir="presets"):
    user_scripts = bpy.utils.user_resource('SCRIPTS', path="holtalyst", create=True)
    path = os.path.join(user_scripts, subdir)
    os.makedirs(path, exist_ok=True)
    return path


def save_preset(name, data, subdir="presets"):
    path = _get_presets_dir(subdir)
    filepath = os.path.join(path, f"{name}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return filepath


def load_preset(name, subdir="presets"):
    path = _get_presets_dir(subdir)
    filepath = os.path.join(path, f"{name}.json")
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def delete_preset(name, subdir="presets"):
    path = _get_presets_dir(subdir)
    filepath = os.path.join(path, f"{name}.json")
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False


def list_presets(subdir="presets"):
    path = _get_presets_dir(subdir)
    if not os.path.exists(path):
        return []
    return [
        os.path.splitext(f)[0]
        for f in os.listdir(path)
        if f.endswith('.json')
    ]


def preset_exists(name, subdir="presets"):
    return name in list_presets(subdir)


def get_render_settings_dict():
    scene = bpy.context.scene
    render = scene.render
    cycles = scene.cycles if hasattr(scene, 'cycles') else None
    data = {
        "engine": render.engine,
        "resolution_x": render.resolution_x,
        "resolution_y": render.resolution_y,
        "resolution_percentage": render.resolution_percentage,
        "fps": render.fps,
        "fps_base": render.fps_base,
        "frame_start": scene.frame_start,
        "frame_end": scene.frame_end,
        "file_format": render.image_settings.file_format,
        "color_mode": render.image_settings.color_mode,
        "filepath": render.filepath,
    }
    if cycles:
        data["cycles_samples"] = cycles.samples
        data["cycles_use_denoising"] = cycles.use_denoising
    return data


def apply_render_settings_dict(data):
    scene = bpy.context.scene
    render = scene.render
    cycles = scene.cycles if hasattr(scene, 'cycles') else None

    if "engine" in data:
        render.engine = data["engine"]
    if "resolution_x" in data:
        render.resolution_x = data["resolution_x"]
    if "resolution_y" in data:
        render.resolution_y = data["resolution_y"]
    if "resolution_percentage" in data:
        render.resolution_percentage = data["resolution_percentage"]
    if "fps" in data:
        render.fps = data["fps"]
    if "fps_base" in data:
        render.fps_base = data["fps_base"]
    if "frame_start" in data:
        scene.frame_start = data["frame_start"]
    if "frame_end" in data:
        scene.frame_end = data["frame_end"]
    if "file_format" in data:
        render.image_settings.file_format = data["file_format"]
    if "color_mode" in data:
        render.image_settings.color_mode = data["color_mode"]
    if "filepath" in data:
        render.filepath = data["filepath"]
    if cycles:
        if "cycles_samples" in data:
            cycles.samples = data["cycles_samples"]
        if "cycles_use_denoising" in data:
            cycles.use_denoising = data["cycles_use_denoising"]


def get_snapshot_dict():
    snapshot = {
        "objects": {},
        "scene": {
            "frame_current": bpy.context.scene.frame_current,
            "cursor_location": list(bpy.context.scene.cursor.location),
        },
    }
    for obj in bpy.data.objects:
        obj_data = {
            "hide_viewport": obj.hide_viewport,
            "hide_render": obj.hide_render,
            "hide_get": obj.hide_get(),
            "location": list(obj.location),
            "rotation_euler": list(obj.rotation_euler),
            "scale": list(obj.scale),
            "display_type": obj.display_type,
        }
        if obj.type == 'MESH' and obj.data:
            obj_data["modifiers"] = {}
            for mod in obj.modifiers:
                obj_data["modifiers"][mod.name] = {
                    "type": mod.type,
                    "show_viewport": mod.show_viewport,
                    "show_render": mod.show_render,
                }
        snapshot["objects"][obj.name] = obj_data
    return snapshot


def apply_snapshot_dict(snapshot):
    if "scene" in snapshot:
        scene_data = snapshot["scene"]
        if "frame_current" in scene_data:
            bpy.context.scene.frame_current = scene_data["frame_current"]
        if "cursor_location" in scene_data:
            bpy.context.scene.cursor.location = scene_data["cursor_location"]

    if "objects" in snapshot:
        for obj_name, obj_data in snapshot["objects"].items():
            if obj_name not in bpy.data.objects:
                continue
            obj = bpy.data.objects[obj_name]
            if "hide_viewport" in obj_data:
                obj.hide_viewport = obj_data["hide_viewport"]
            if "hide_render" in obj_data:
                obj.hide_render = obj_data["hide_render"]
            if "hide_get" in obj_data:
                obj.hide_set(obj_data["hide_get"])
            if "location" in obj_data:
                obj.location = obj_data["location"]
            if "rotation_euler" in obj_data:
                obj.rotation_euler = obj_data["rotation_euler"]
            if "scale" in obj_data:
                obj.scale = obj_data["scale"]
            if "display_type" in obj_data:
                obj.display_type = obj_data["display_type"]
            if "modifiers" in obj_data:
                for mod_name, mod_data in obj_data["modifiers"].items():
                    if mod_name in obj.modifiers:
                        mod = obj.modifiers[mod_name]
                        if "show_viewport" in mod_data:
                            mod.show_viewport = mod_data["show_viewport"]
                        if "show_render" in mod_data:
                            mod.show_render = mod_data["show_render"]
