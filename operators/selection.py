import bpy
from bpy.types import Operator


class HOLTALYST_OT_SelectAllIncluding(Operator):
    bl_idname = "object.select_all_including"
    bl_label = "Select All Including"
    bl_description = "Selects all objects including the select string"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import select_objects_including
        holtalyst = context.scene.holtalyst
        select_objects_including(holtalyst.select_string, holtalyst.is_case_sensitive)
        return {'FINISHED'}


class HOLTALYST_OT_FormCollectionString(Operator):
    bl_idname = "object.form_collection_string"
    bl_label = "Form Collection"
    bl_description = "Form a collection with the found objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import (
            collection_exists, get_collection, create_collection,
            get_objects_including, move_objects_to_collection,
        )
        holtalyst = context.scene.holtalyst
        col = get_collection(holtalyst.select_string) if collection_exists(holtalyst.select_string) else create_collection(holtalyst.select_string)
        obj_list = get_objects_including(holtalyst.select_string, holtalyst.is_case_sensitive)
        move_objects_to_collection(obj_list, col)
        return {'FINISHED'}


class HOLTALYST_OT_SelectAllType(Operator):
    bl_idname = "object.select_all_type"
    bl_label = "Select All Type"
    bl_description = "Selects all objects of the selected type"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import (
            select_all_meshes, select_all_curves, select_all_surfaces,
            select_all_metas, select_all_text, select_all_hair,
            select_all_point_clouds, select_all_volumes, select_all_armatures,
            select_all_lattices, select_all_empties, select_all_grease_pencils,
            select_all_cameras, select_all_lights, select_all_light_probes,
        )
        holtalyst = context.scene.holtalyst
        type_map = {
            "MESHES": select_all_meshes,
            "CURVES": select_all_curves,
            "SURFACES": select_all_surfaces,
            "METAS": select_all_metas,
            "TEXT": select_all_text,
            "HAIR": select_all_hair,
            "POINT_CLOUDS": select_all_point_clouds,
            "VOLUMES": select_all_volumes,
            "ARMATURES": select_all_armatures,
            "LATTICES": select_all_lattices,
            "EMPTIES": select_all_empties,
            "GREASE_PENCILS": select_all_grease_pencils,
            "CAMERAS": select_all_cameras,
            "LIGHTS": select_all_lights,
            "LIGHT_PROBES": select_all_light_probes,
        }
        fn = type_map.get(holtalyst.select_types)
        if fn:
            fn()
        return {'FINISHED'}


class HOLTALYST_OT_FormCollectionType(Operator):
    bl_idname = "object.form_collection_type"
    bl_label = "Form Collection"
    bl_description = "Form a collection with the found objects of a type"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import (
            so, collection_exists, get_collection, create_collection,
            move_objects_to_collection,
            select_all_meshes, select_all_curves, select_all_surfaces,
            select_all_metas, select_all_text, select_all_hair,
            select_all_point_clouds, select_all_volumes, select_all_armatures,
            select_all_lattices, select_all_empties, select_all_grease_pencils,
            select_all_cameras, select_all_lights, select_all_light_probes,
        )
        holtalyst = context.scene.holtalyst
        type_map = {
            "MESHES": ("Meshes", select_all_meshes),
            "CURVES": ("Curves", select_all_curves),
            "SURFACES": ("Surfaces", select_all_surfaces),
            "METAS": ("Metas", select_all_metas),
            "TEXT": ("Text", select_all_text),
            "HAIR": ("Hair", select_all_hair),
            "POINT_CLOUDS": ("Point Clouds", select_all_point_clouds),
            "VOLUMES": ("Volumes", select_all_volumes),
            "ARMATURES": ("Armatures", select_all_armatures),
            "LATTICES": ("Lattices", select_all_lattices),
            "EMPTIES": ("Empties", select_all_empties),
            "GREASE_PENCILS": ("Grease Pencils", select_all_grease_pencils),
            "CAMERAS": ("Cameras", select_all_cameras),
            "LIGHTS": ("Lights", select_all_lights),
            "LIGHT_PROBES": ("Light Probes", select_all_light_probes),
        }
        entry = type_map.get(holtalyst.select_types)
        if entry:
            colname, select_fn = entry
            select_fn()
            col = get_collection(colname) if collection_exists(colname) else create_collection(colname)
            move_objects_to_collection(so(), col)
        return {'FINISHED'}


class HOLTALYST_OT_NameAddPrefix(Operator):
    bl_idname = "object.name_add_prefix"
    bl_label = "Name Add Prefix"
    bl_description = "Adds the tag string as a prefix"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import so, add_prefix_to_name
        holtalyst = context.scene.holtalyst
        add_prefix_to_name(so(), holtalyst.tag_string, holtalyst.delimiter_string)
        return {'FINISHED'}


class HOLTALYST_OT_NameAddSuffix(Operator):
    bl_idname = "object.name_add_suffix"
    bl_label = "Name Add Suffix"
    bl_description = "Adds the tag string as a suffix"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import so, add_suffix_to_name
        holtalyst = context.scene.holtalyst
        add_suffix_to_name(so(), holtalyst.tag_string, holtalyst.delimiter_string)
        return {'FINISHED'}


class HOLTALYST_OT_SelectByVertexCount(Operator):
    bl_idname = "object.select_by_vertex_count"
    bl_label = "Select By Vertex Count"
    bl_description = "Selects objects by comparing given vertex count"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import select_objects_by_vertex
        holtalyst = context.scene.holtalyst
        select_objects_by_vertex(holtalyst.vertex_count, holtalyst.comparison_mode)
        return {'FINISHED'}


class HOLTALYST_OT_FormCollectionVertices(Operator):
    bl_idname = "object.form_collection_vertices"
    bl_label = "Form Collection"
    bl_description = "Form a collection with the found objects depending on vertex count"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import (
            so, collection_exists, get_collection, create_collection,
            select_objects_by_vertex, move_objects_to_collection,
        )
        holtalyst = context.scene.holtalyst
        cmode = holtalyst.comparison_mode.upper()
        if cmode in ("EQUAL", "SAME"):
            colname = "Equal to " + str(holtalyst.vertex_count)
        elif cmode in ("GREATER", "MORE"):
            colname = "Greater than " + str(holtalyst.vertex_count)
        elif cmode in ("LESS", "FEWER"):
            colname = "Less than " + str(holtalyst.vertex_count)
        else:
            colname = "Vertex Count " + str(holtalyst.vertex_count)

        col = get_collection(colname) if collection_exists(colname) else create_collection(colname)
        select_objects_by_vertex(holtalyst.vertex_count, holtalyst.comparison_mode)
        move_objects_to_collection(so(), col)
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SelectAllIncluding,
    HOLTALYST_OT_FormCollectionString,
    HOLTALYST_OT_SelectAllType,
    HOLTALYST_OT_FormCollectionType,
    HOLTALYST_OT_NameAddPrefix,
    HOLTALYST_OT_NameAddSuffix,
    HOLTALYST_OT_SelectByVertexCount,
    HOLTALYST_OT_FormCollectionVertices,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
