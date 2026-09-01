import bpy
from .common import get_object, get_objects, so
from .render import current_frame


def add_keyframe(path, property, frame=None):
    if frame is None:
        frame = current_frame()
    path.keyframe_insert(data_path=property, frame=frame)
    keyframes = []
    for i in range(len(path.animation_data.action.fcurves)):
        fcurve = path.animation_data.action.fcurves.find(property, index=i)
        if fcurve is not None:
            for keyframe in fcurve.keyframe_points:
                if keyframe.co[0] == frame:
                    keyframes.append(keyframe)
    for area in bpy.context.screen.areas:
        area.tag_redraw()
    return keyframes if len(keyframes) > 1 else keyframes[0]


def remove_keyframe(keyframes):
    if not isinstance(keyframes, list):
        keyframes = [keyframes]
    for keyframe in keyframes:
        fcurves = keyframe.id_data.fcurves
        for fcurve in fcurves:
            for kf in fcurve.keyframe_points:
                if kf == keyframe:
                    fcurve.keyframe_points.remove(kf)
            if len(fcurve.keyframe_points) == 0:
                fcurves.remove(fcurve)
        for area in bpy.context.screen.areas:
            area.tag_redraw()


def delete_animation_data(ref=None):
    objs = get_objects(ref)
    for obj in objs:
        obj.animation_data_clear()


def add_driver(path, property, index=-1):
    fcurves = path.driver_add(property, index)
    for area in bpy.context.screen.areas:
        area.tag_redraw()
    if isinstance(fcurves, list):
        return [fcurve.driver for fcurve in fcurves]
    return fcurves.driver


def remove_driver(driver):
    for fcurve in driver.id_data.animation_data.drivers:
        if fcurve.driver == driver:
            driver.id_data.animation_data.drivers.remove(fcurve)
