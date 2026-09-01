from . import cleanup, selection, lighting, optimization, interface, world, rename, render_presets, export, snapshots, transforms, material_batch, viewport, visibility, cameras, collection_templates, mesh_stats, modifier_presets, world_hdri, normals

submodules = [cleanup, selection, lighting, optimization, interface, world, rename, render_presets, export, snapshots, transforms, material_batch, viewport, visibility, cameras, collection_templates, mesh_stats, modifier_presets, world_hdri, normals]


def register():
    for mod in submodules:
        mod.register()


def unregister():
    for mod in reversed(submodules):
        mod.unregister()
