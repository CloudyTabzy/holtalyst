import bpy


def selection_to_cursor_without_offset():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


def selection_to_cursor_with_offset():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)


def cursor_to_world_origin():
    bpy.ops.view3d.snap_cursor_to_center()


def cursor_to_selection():
    bpy.ops.view3d.snap_cursor_to_selected()


def cursor_to_active():
    bpy.ops.view3d.snap_cursor_to_selected()


def selection_to_grid():
    bpy.ops.view3d.snap_selected_to_grid()


def selection_to_active():
    bpy.ops.view3d.snap_selected_to_active()


def cursor_to_grid():
    bpy.ops.view3d.snap_cursor_to_grid()


def get_cursor_location():
    return bpy.context.scene.cursor.location


def set_cursor_location(newloc):
    bpy.context.scene.cursor.location = newloc


def get_cursor_rotation():
    return bpy.context.scene.cursor.rotation_euler


def get_cursor_rotation_mode():
    return bpy.context.scene.cursor.rotation_mode


def set_pivot_point_to_cursor():
    from .common import get_scene
    get_scene().tool_settings.transform_pivot_point = 'CURSOR'


def set_pivot_point_to_median():
    from .common import get_scene
    get_scene().tool_settings.transform_pivot_point = 'MEDIAN_POINT'


def set_pivot_point_to_individual_origins():
    from .common import get_scene
    get_scene().tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'


def set_pivot_point_to_active_element():
    from .common import get_scene
    get_scene().tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'


def set_pivot_point_to_bounding_box_center():
    from .common import get_scene
    get_scene().tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
