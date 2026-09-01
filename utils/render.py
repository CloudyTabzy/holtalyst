from ..compat import EEVEE_ENGINE
from .common import get_scene


def set_render_engine_to_eevee():
    get_scene().render.engine = EEVEE_ENGINE


def set_render_engine_eevee():
    set_render_engine_to_eevee()


def set_render_engine_to_cycles():
    get_scene().render.engine = 'CYCLES'


def set_render_engine_cycles():
    set_render_engine_to_cycles()


def render_image(use_view=False):
    import bpy
    bpy.ops.render.render(use_viewport=use_view)
    return bpy.data.images['Render Result']


def render_animation(use_view=False):
    import bpy
    bpy.ops.render.render(animation=True, use_viewport=use_view)


def set_render_resolution(x, y):
    scene = get_scene()
    scene.render.resolution_x = x
    scene.render.resolution_y = y


def get_render_resolution():
    scene = get_scene()
    return [scene.render.resolution_x, scene.render.resolution_y]


def render_resolution(x=None, y=None):
    if x is not None and y is not None:
        set_render_resolution(x, y)
    else:
        return get_render_resolution()


def set_render_resolution_percentage(percent):
    get_scene().render.resolution_percentage = percent


def set_render_percentage(percent=None):
    set_render_resolution_percentage(percent)


def set_render_percent(percent=None):
    set_render_resolution_percentage(percent)


def get_render_resolution_percentage():
    return get_scene().render.resolution_percentage


def render_resolution_percentage(percent=None):
    if percent is not None:
        set_render_resolution_percentage(percent)
    else:
        return get_render_resolution_percentage()


def set_render_pixel_aspect_ratio(x, y):
    scene = get_scene()
    scene.render.pixel_aspect_x = x
    scene.render.pixel_aspect_y = y


def get_render_pixel_aspect_ratio():
    scene = get_scene()
    return [scene.render.pixel_aspect_x, scene.render.pixel_aspect_ratio]


def render_aspect_ratio(x=None, y=None):
    if x is not None and y is not None:
        set_render_pixel_aspect_ratio(x, y)
    else:
        return get_render_pixel_aspect_ratio()


def current_frame(val=None):
    scene = get_scene()
    if val is None:
        return scene.frame_current
    else:
        scene.frame_current = val


def set_frame(val=None):
    current_frame(val)


def frame_start(val=None):
    scene = get_scene()
    if val is None:
        return scene.frame_start
    else:
        scene.frame_start = val


def frame_end(val=None):
    scene = get_scene()
    if val is None:
        return scene.frame_end
    else:
        scene.frame_end = val


def set_current_frame(val=None):
    current_frame(val)


def set_frame_start(val=None):
    frame_start(val)


def set_frame_end(val=None):
    frame_end(val)


def set_start_frame(val=None):
    frame_start(val)


def set_end_frame(val=None):
    frame_end(val)


def set_frame_interval(start=None, end=None):
    frame_start(start)
    frame_end(end)


def set_frame_step(val):
    get_scene().frame_step = val


def set_render_fps(val, base=1.0):
    scene = get_scene()
    scene.render.fps = val
    scene.render.fps_base = base
