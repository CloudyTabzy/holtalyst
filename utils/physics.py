import bpy
from .common import get_object


def add_force_field_physics(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref
    if objref.field.type == 'NONE':
        bpy.ops.object.forcefield_toggle()


def add_collision_physics(ref=None):
    from .modifiers import add_collision
    add_collision(ref)


def add_cloth_physics(ref=None):
    from .modifiers import add_cloth
    add_cloth(ref)


def add_dynamic_paint_physics(ref=None):
    from .modifiers import add_dynamic_paint
    add_dynamic_paint(ref)


def add_soft_body_physics(ref=None):
    from .modifiers import add_soft_body
    add_soft_body(ref)


def add_fluid_physics(ref=None):
    from .modifiers import add_fluid
    add_fluid(ref)


def add_rigid_body_physics(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref
    bpy.ops.rigidbody.object_add()


def add_rigid_body_constraint_physics(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref
    bpy.ops.rigidbody.constraint_add()


def collision_use(value=True):
    bpy.context.object.collision.use = value


def use_collision(value=True):
    collision_use(value)


def collision_field_absorption(value):
    bpy.context.object.collision.absorption = float(value)


def collision_particle_permeability(value):
    bpy.context.object.collision.permeability = float(value)


def collision_particle_stickiness(value):
    bpy.context.object.collision.stickiness = float(value)


def collision_particle_kill(value=True):
    bpy.context.object.collision.use_particle_kill = value


def collision_particle_friction(value):
    bpy.context.object.collision.friction_factor = float(value)


def collision_particle_friction_random(value):
    bpy.context.object.collision.friction_random = float(value)


def collision_particle_damping(value):
    bpy.context.object.collision.damping_factor = float(value)


def collision_particle_damping_random(value):
    bpy.context.object.collision.damping_random = float(value)


def collision_soft_cloth_damping(value):
    bpy.context.object.collision.damping = float(value)


def collision_soft_cloth_friction(value):
    bpy.context.object.collision.cloth_friction = float(value)


def collision_soft_cloth_thick_out(value):
    bpy.context.object.collision.thickness_outer = float(value)


def collision_soft_cloth_thick_in(value):
    bpy.context.object.collision.thickness_inner = float(value)


def collision_soft_cloth_single_side(value=True):
    bpy.context.object.collision.use_culling = value


def collision_soft_cloth_override_normals(value=True):
    bpy.context.object.collision.use_normal = value
