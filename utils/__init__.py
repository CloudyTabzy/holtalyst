from .common import *
from .render import *
from .objects import *
from .selection import *
from .collections import *
from .materials import *
from .nodes import *
from .modifiers import *
from .lighting import *
from .transforms import *
from .animation import *
from .mesh import *
from .cursor import *
from .textures import *
from .physics import *
from .text_objects import *
from .presets import *
from .rename import *
from .export import *


def organize_outliner():
    from .objects import (
        deselect_all_objects,
        select_object,
        is_any_selected_object_editable,
    )
    from .selection import (
        select_all_cameras,
        select_all_lights,
        select_all_empties,
        select_all_meshes,
        select_all_curves,
        select_all_surfaces,
        select_all_metas,
        select_all_text,
        select_all_volumes,
        select_all_armatures,
        select_all_lattices,
        select_all_grease_pencils,
        select_all_light_probes,
    )
    from .collections import (
        create_collection,
        collection_exists,
        get_collection,
        move_objects_to_collection,
    )

    import bpy

    if bpy.context.active_object is not None:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

    categories = [
        ("Cameras", select_all_cameras),
        ("Lights", select_all_lights),
        ("Empties", select_all_empties),
        ("Objects", select_all_meshes),
        ("Curves", select_all_curves),
        ("Surfaces", select_all_surfaces),
        ("Metas", select_all_metas),
        ("Text", select_all_text),
        ("Volumes", select_all_volumes),
        ("Armatures", select_all_armatures),
        ("Lattices", select_all_lattices),
        ("Grease Pencils", select_all_grease_pencils),
        ("Light Probes", select_all_light_probes),
    ]

    for colname, select_fn in categories:
        deselect_all_objects()
        select_fn()
        if is_any_selected_object_editable() and len(so()) > 0:
            col = get_collection(colname) if collection_exists(colname) else create_collection(colname)
            move_objects_to_collection(so(), col)

    deselect_all_objects()


def suffix_convert_dataset(data):
    for d in data:
        nn = d.name
        if '_' in d.name:
            r = d.name.split('_')
            if '.' in r[-1]:
                r2 = r[-1].split('.')
                if r2[0].isdigit():
                    val = int(r2[0]) + int(r2[1])
                    nn = r[0] + '_' + str(val)
                    i = 1
                    while nn in data:
                        nn = r[0] + '_' + str(val + i)
                        i += 1
                else:
                    if r2[1].isdigit():
                        val = int(r2[1])
                        i = 0
                        nn = ""
                        while i < len(r) - 1:
                            nn = nn + r[i] + "_"
                            i += 1
                        nn = nn + r2[0] + "_" + str(val)
        else:
            if '.' in d.name:
                r = d.name.split('.')
                if r[-1].isdigit():
                    val = int(r[-1])
                    nn = r[0] + '_' + str(val)
                    i = 1
                    while nn in data:
                        nn = r[0] + '_' + str(val + i)
                        i += 1
        d.name = nn


def convert_suffixes_underscore():
    import bpy
    suffix_convert_dataset(bpy.data.meshes)
    suffix_convert_dataset(bpy.data.objects)
    suffix_convert_dataset(bpy.data.textures)
    suffix_convert_dataset(bpy.data.images)
    suffix_convert_dataset(bpy.data.materials)


def convert_suffixes():
    convert_suffixes_underscore()


def trim_view_layer_suffixes():
    import bpy
    for o in bpy.context.view_layer.objects:
        if o is None:
            continue
        if o.name.endswith(".001"):
            newname = o.name[:-4]
            if newname in bpy.data.objects:
                conflicting_object = bpy.data.objects[newname]
                if conflicting_object.is_editable:
                    conflicting_object.name = newname + "_old"
                    o.name = newname


def debug_test():
    print("EasyBPY debug output")
