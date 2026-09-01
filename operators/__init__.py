from . import cleanup, selection, lighting, optimization, world, rename, render_presets, export, snapshots

submodules = [cleanup, selection, lighting, optimization, world, rename, render_presets, export, snapshots]


def register():
    for mod in submodules:
        mod.register()


def unregister():
    for mod in reversed(submodules):
        mod.unregister()
