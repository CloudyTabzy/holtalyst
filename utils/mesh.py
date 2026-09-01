import bpy
from .common import is_string, get_object


def create_mesh(name):
    return bpy.data.meshes.new(name)


def get_all_meshes():
    return bpy.data.meshes


def get_vertices(ref):
    if is_string(ref):
        return get_object(ref).data.vertices
    return ref.data.vertices


def get_edges(ref):
    if is_string(ref):
        return get_object(ref).data.edges
    return ref.data.edges


def get_faces(ref):
    return get_polygons(ref)


def get_polygons(ref):
    if is_string(ref):
        return get_object(ref).data.polygons
    return ref.data.polygons


def get_mesh_from_object(ref):
    objref = get_object(ref) if is_string(ref) else ref
    return objref.data


def get_selected_vertices(ref=None):
    ref = get_object(ref)
    tmp_mode = ref.mode
    from .objects import select_object
    select_object(ref)
    bpy.ops.object.mode_set(mode='OBJECT')
    selected_vertices = [v for v in ref.data.vertices if v.select]
    bpy.ops.object.mode_set(mode=tmp_mode)
    return selected_vertices


def get_selected_verts(ref=None):
    return get_selected_vertices(ref)


def get_selected_edges(ref=None):
    ref = get_object(ref)
    tmp_mode = ref.mode
    from .objects import select_object
    select_object(ref)
    bpy.ops.object.mode_set(mode='OBJECT')
    selected_edges = [e for e in ref.data.edges if e.select]
    bpy.ops.object.mode_set(mode=tmp_mode)
    return selected_edges


def get_selected_faces(ref=None):
    ref = get_object(ref)
    tmp_mode = ref.mode
    from .objects import select_object
    select_object(ref)
    bpy.ops.object.mode_set(mode='OBJECT')
    selected_faces = [f for f in ref.data.polygons if f.select]
    bpy.ops.object.mode_set(mode=tmp_mode)
    return selected_faces


def get_curve_points(ref=None):
    obj = get_object(ref)
    points = []
    for spline in obj.data.splines:
        for point in (*spline.points, *spline.bezier_points):
            points.append(point)
    return points


def get_selected_curve_points(ref=None):
    obj = get_object(ref)
    points = []
    for spline in obj.data.splines:
        if spline.type == "NURBS":
            for point in spline.points:
                if point.select:
                    points.append(point)
        if spline.type == "BEZIER":
            for point in spline.points:
                if point.select_control_point:
                    points.append(point)
    return points


def add_shape_key(name=None, ref=None):
    objref = get_object(ref)
    if name:
        return objref.shape_key_add(name=name)
    return objref.shape_key_add()


def get_shape_key(name_or_index=0, ref=None):
    objref = get_object(ref)
    if objref.data.shape_keys:
        return objref.data.shape_keys.key_blocks[name_or_index]
    return None


def get_all_shape_keys(ref=None):
    objref = get_object(ref)
    return list(objref.data.shape_keys.key_blocks)


def remove_shape_key(shape_key, ref=None):
    objref = get_object(ref)
    if isinstance(shape_key, bpy.types.ShapeKey):
        objref.shape_key_remove(shape_key)
    elif isinstance(shape_key, (str, int)):
        sk_ref = get_shape_key(shape_key, objref)
        objref.shape_key_remove(sk_ref)


def remove_all_shape_keys(ref=None):
    objref = get_object(ref)
    objref.shape_key_clear()


def get_active_shape_key(ref=None):
    objref = get_object(ref)
    return objref.active_shape_key


def get_shape_keys(ref=None):
    return get_all_shape_keys(ref)


def remove_shape_keys(ref=None):
    return remove_all_shape_keys(ref)


def get_particle_systems(ref):
    objref = get_object(ref)
    return objref.particle_systems


def get_particle_systems_containing(name, ref):
    result = []
    ps = get_particle_systems(ref)
    for p in ps:
        if name in p.name:
            result.append(p)
    return result
