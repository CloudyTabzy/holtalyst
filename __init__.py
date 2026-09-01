import bpy

if "preferences" in locals():
    import importlib
    importlib.reload(preferences)
    importlib.reload(properties)
    importlib.reload(operators)
    importlib.reload(panels)
else:
    from . import preferences, properties, operators, panels

register, unregister = bpy.utils.register_submodule_factory(__name__, [
    "preferences",
    "properties",
    "operators",
    "panels",
])


if __name__ == "__main__":
    register()
