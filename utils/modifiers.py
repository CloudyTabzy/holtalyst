import bpy
import random
from .common import get_object, get_objects, select_object


def add_modifier(ref=None, name="Modifier", id="SUBSURF"):
    objrefs = get_objects(ref)
    new_mods = []
    for o in objrefs:
        new_mod = o.modifiers.new(name, id)
        new_mods.append(new_mod)
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            area.tag_redraw()
    if len(new_mods) > 1:
        return new_mods
    return new_mods[0]


def get_modifier(ref, name):
    objref = get_object(ref)
    if name in objref.modifiers:
        return objref.modifiers[name]
    return False


def remove_modifier(ref=None, name=None):
    from .common import is_string
    objref = get_object(ref)
    if name is not None:
        if is_string(name):
            if name in objref.modifiers:
                mod = get_modifier(objref, name)
                objref.modifiers.remove(mod)
        else:
            objref.modifiers.remove(name)
    else:
        objref.modifiers.remove(objref.modifiers[0])
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            area.tag_redraw()


def remove_modifiers(ref=None):
    objref = get_objects(ref)
    for o in objref:
        for m in o.modifiers:
            o.modifiers.remove(m)


def remove_all_modifiers(ref=None):
    remove_modifiers(ref)


def apply_all_modifiers(ref=None):
    objref = get_object(ref)
    select_object(objref)
    for mod in objref.modifiers:
        bpy.ops.object.modifier_apply(modifier=mod.name)


def apply_modifiers(ref=None):
    apply_all_modifiers(ref)


def add_data_transfer(ref=None, modname="DataTransfer"):
    return add_modifier(ref, modname, 'DATA_TRANSFER')


def add_mesh_cache(ref=None, modname="MeshCache"):
    return add_modifier(ref, modname, 'MESH_CACHE')


def add_mesh_sequence_cache(ref=None, modname="MeshSequenceCache"):
    return add_modifier(ref, modname, 'MESH_SEQUENCE_CACHE')


def add_normal_edit(ref=None, modname="NormalEdit"):
    return add_modifier(ref, modname, 'NORMAL_EDIT')


def add_weighted_normal(ref=None, modname="WeightedNormal"):
    return add_modifier(ref, modname, 'WEIGHTED_NORMAL')


def add_uv_project(ref=None, modname="UVProject"):
    return add_modifier(ref, modname, 'UV_PROJECT')


def add_uv_warp(ref=None, modname="Warp"):
    return add_modifier(ref, modname, 'UV_WARP')


def add_vertex_weight_edit(ref=None, modname="VertexWeightEdit"):
    return add_modifier(ref, modname, 'VERTEX_WEIGHT_EDIT')


def add_vertex_weight_mix(ref=None, modname="VertexWeightMix"):
    return add_modifier(ref, modname, 'VERTEX_WEIGHT_MIX')


def add_vertex_weight_proximity(ref=None, modname="VertexWeightProximity"):
    return add_modifier(ref, modname, 'VERTEX_WEIGHT_PROXIMITY')


def add_array(ref=None, modname="Array"):
    return add_modifier(ref, modname, 'ARRAY')


def add_bevel(ref=None, modname="Bevel"):
    return add_modifier(ref, modname, 'BEVEL')


def add_boolean(ref=None, modname="Boolean"):
    return add_modifier(ref, modname, 'BOOLEAN')


def add_build(ref=None, modname="Build"):
    return add_modifier(ref, modname, 'BUILD')


def add_decimate(ref=None, modname="Decimate"):
    return add_modifier(ref, modname, 'DECIMATE')


def add_edge_split(ref=None, modname="EdgeSplit"):
    return add_modifier(ref, modname, 'EDGE_SPLIT')


def add_mask(ref=None, modname="Mask"):
    return add_modifier(ref, modname, 'MASK')


def add_mirror(ref=None, modname="Mirror"):
    return add_modifier(ref, modname, 'MIRROR')


def add_multires(ref=None, modname="Multires"):
    return add_modifier(ref, modname, 'MULTIRES')


def add_remesh(ref=None, modname="Remesh"):
    return add_modifier(ref, modname, 'REMESH')


def add_screw(ref=None, modname="Screw"):
    return add_modifier(ref, modname, 'SCREW')


def add_skin(ref=None, modname="Skin"):
    return add_modifier(ref, modname, 'SKIN')


def add_solidify(ref=None, modname="Solidify"):
    return add_modifier(ref, modname, 'SOLIDIFY')


def add_subsurf(ref=None, modname="Subsurf"):
    return add_modifier(ref, modname, 'SUBSURF')


def add_triangulate(ref=None, modname="Triangulate"):
    return add_modifier(ref, modname, 'TRIANGULATE')


def add_weld(ref=None, modname="Weld"):
    return add_modifier(ref, modname, 'WELD')


def add_wireframe(ref=None, modname="Wireframe"):
    return add_modifier(ref, modname, 'WIREFRAME')


def add_armature(ref=None, modname="Armature"):
    return add_modifier(ref, modname, 'ARMATURE')


def add_cast(ref=None, modname="Cast"):
    return add_modifier(ref, modname, 'CAST')


def add_curve(ref=None, modname="Curve"):
    return add_modifier(ref, modname, 'CURVE')


def add_displace(ref=None, modname="Displace"):
    return add_modifier(ref, modname, 'DISPLACE')


def add_hook(ref=None, modname="Hook"):
    return add_modifier(ref, modname, 'HOOK')


def add_laplacian_deform(ref=None, modname="LaplacianDeform"):
    return add_modifier(ref, modname, 'LAPLACIANDEFORM')


def add_lattice(ref=None, modname="Lattice"):
    return add_modifier(ref, modname, 'LATTICE')


def add_mesh_deform(ref=None, modname="Deform"):
    return add_modifier(ref, modname, 'MESH_DEFORM')


def add_shrinkwrap(ref=None, modname="Shrinkwrap"):
    return add_modifier(ref, modname, 'SHRINKWRAP')


def add_simple_deform(ref=None, modname="SimpleDeform"):
    return add_modifier(ref, modname, 'SIMPLE_DEFORM')


def add_smooth(ref=None, modname="Smooth"):
    return add_modifier(ref, modname, 'SMOOTH')


def add_corrective_smooth(ref=None, modname="CorrectiveSmooth"):
    return add_modifier(ref, modname, 'CORRECTIVE_SMOOTH')


def add_laplacian_smooth(ref=None, modname="LaplacianSmooth"):
    return add_modifier(ref, modname, 'LAPLACIANSMOOTH')


def add_surface_deform(ref=None, modname="SurfaceDeform"):
    return add_modifier(ref, modname, 'SURFACE_DEFORM')


def add_warp(ref=None, modname="Warp"):
    return add_modifier(ref, modname, 'WARP')


def add_wave(ref=None, modname="Wave"):
    from .common import get_scene
    mod = add_modifier(ref, modname, 'WAVE')
    mod.time_offset = random.random() * get_scene().render.fps
    return mod


def add_cloth(ref=None, modname="Cloth"):
    return add_modifier(ref, modname, 'CLOTH')


def add_collision(ref=None, modname="Collision"):
    return add_modifier(ref, modname, 'COLLISION')


def add_dynamic_paint(ref=None, modname="DynamicPaint"):
    return add_modifier(ref, modname, 'DYNAMIC_PAINT')


def add_explode(ref=None, modname="Explode"):
    return add_modifier(ref, modname, 'EXPLODE')


def add_fluid(ref=None, modname="Fluid"):
    return add_modifier(ref, modname, 'FLUID')


def add_ocean(ref=None, modname="Ocean"):
    return add_modifier(ref, modname, 'OCEAN')


def add_particle_instance(ref=None, modname="ParticleInstance"):
    return add_modifier(ref, modname, 'PARTICLE_INSTANCE')


def add_particle_system(ref=None, modname="ParticleSystem"):
    return add_modifier(ref, modname, 'PARTICLE_SYSTEM')


def add_soft_body(ref=None, modname="SoftBody"):
    return add_modifier(ref, modname, 'SOFT_BODY')


def add_surface(ref=None, modname=""):
    return add_modifier(ref, modname, 'SURFACE')


def add_simulation(ref=None, modname=""):
    return add_modifier(ref, modname, 'SIMULATION')
