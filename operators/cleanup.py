import bpy
from bpy.types import Operator


class HOLTALYST_OT_OrganizeOutliner(Operator):
    bl_idname = "outliner.organize_outliner"
    bl_label = "Organize Outliner"
    bl_description = "Organizes the outliner into categories"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import organize_outliner
        organize_outliner()
        return {'FINISHED'}


class HOLTALYST_OT_ConvertSuffixes(Operator):
    bl_idname = "object.convert_suffixes"
    bl_label = "Convert Suffixes"
    bl_description = "Convert .001 suffixes to _1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import convert_suffixes
        convert_suffixes()
        return {'FINISHED'}


class HOLTALYST_OT_PurgeUnwantedData(Operator):
    bl_idname = "object.purge_unwanted_data"
    bl_label = "Purge Unwanted Data"
    bl_description = "Remove all data that isn't being used"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import clear_unwanted_data
        clear_unwanted_data()
        return {'FINISHED'}


class HOLTALYST_OT_DeepClean(Operator):
    bl_idname = "outliner.deep_clean"
    bl_label = "Deep Clean"
    bl_description = "Just clean the blend file me, will ya?"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import organize_outliner, convert_suffixes
        organize_outliner()
        convert_suffixes()
        return {'FINISHED'}


class HOLTALYST_OT_SetAutoSmooth(Operator):
    bl_idname = "object.set_auto_smooth"
    bl_label = "Set Auto Smooth"
    bl_description = "Sets auto smooth true and gives angle"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import so, set_smooth_angle
        holtalyst = context.scene.holtalyst
        for o in so():
            set_smooth_angle(o, holtalyst.autosmooth_angle)
        return {'FINISHED'}


class HOLTALYST_OT_SyncMeshName(Operator):
    bl_idname = "object.sync_mesh_name"
    bl_label = "Sync Mesh Name"
    bl_description = "Sets mesh data names to match object names"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import so
        for o in so():
            if o.data.name != o.name:
                o.data.name = o.name
        return {'FINISHED'}


class HOLTALYST_OT_ShiftToWorldOrigin(Operator):
    bl_idname = "object.shift_to_world_origin"
    bl_label = "Shift to World Origin"
    bl_description = "Takes the selected point and uses this to shift the object to the world origin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import ao, object_mode, set_origin_to_cursor, location
        bpy.ops.view3d.snap_cursor_to_selected()
        object_mode(ao())
        set_origin_to_cursor(ao())
        location(ao(), [0, 0, 0])
        return {'FINISHED'}


class HOLTALYST_OT_RemoveUnusedSlots(Operator):
    bl_idname = "object.remove_unused_slots"
    bl_label = "Remove Unused Slots"
    bl_description = "Removes unused material slots from selected object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import remove_unused_material_slots
        remove_unused_material_slots()
        return {'FINISHED'}


class HOLTALYST_OT_FixDuplicateNodeGroups(Operator):
    bl_idname = "object.fix_duplicate_node_groups"
    bl_label = "Fix Duplicate Node Groups"
    bl_description = "Removes duplicate node groups and replaced with original"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..utils import fix_duplicate_nodes
        fix_duplicate_nodes()
        return {'FINISHED'}


class HOLTALYST_OT_SetNodeGroupDefaults(Operator):
    bl_idname = "object.set_node_group_defaults"
    bl_label = "Set Defaults"
    bl_description = "Sets the current values to be the default values for selected node groups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for m in bpy.data.materials:
            matnodes = m.node_tree.nodes
            for node in matnodes:
                if node.select and node.type == 'GROUP':
                    node_group = node.node_tree
                    for j in range(len(node.inputs)):
                        for item in node_group.interface.items_tree:
                            if item.in_out == 'INPUT' and item.name == node.inputs[j].name:
                                item.default_value = node.inputs[j].default_value

        for w in bpy.data.worlds:
            worldnodes = w.node_tree.nodes
            for node in worldnodes:
                if node.select and node.type == 'GROUP':
                    node_group = node.node_tree
                    for j in range(len(node.inputs)):
                        for item in node_group.interface.items_tree:
                            if item.in_out == 'INPUT' and item.name == node.inputs[j].name:
                                item.default_value = node.inputs[j].default_value

        for n in bpy.data.node_groups:
            geonodes = n.nodes
            for node in geonodes:
                if node.select and node.type == 'GROUP':
                    node_group = node.node_tree
                    for j in range(len(node.inputs)):
                        for item in node_group.interface.items_tree:
                            if item.in_out == 'INPUT' and item.name == node.inputs[j].name:
                                item.default_value = node.inputs[j].default_value

        return {'FINISHED'}


class HOLTALYST_OT_GetNodeGroupDefaults(Operator):
    bl_idname = "object.get_node_group_defaults"
    bl_label = "Get Defaults"
    bl_description = "Gets the current values to be the default values for selected node groups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for m in bpy.data.materials:
            matnodes = m.node_tree.nodes
            for node in matnodes:
                if node.select and node.type == 'GROUP':
                    node_group = node.node_tree
                    for j in range(len(node.inputs)):
                        for item in node_group.interface.items_tree:
                            if item.in_out == 'INPUT' and item.name == node.inputs[j].name:
                                node.inputs[j].default_value = item.default_value

        for w in bpy.data.worlds:
            worldnodes = w.node_tree.nodes
            for node in worldnodes:
                if node.select and node.type == 'GROUP':
                    node_group = node.node_tree
                    for j in range(len(node.inputs)):
                        for item in node_group.interface.items_tree:
                            if item.in_out == 'INPUT' and item.name == node.inputs[j].name:
                                node.inputs[j].default_value = item.default_value

        for n in bpy.data.node_groups:
            geonodes = n.nodes
            for node in geonodes:
                if node.select and node.type == 'GROUP':
                    node_group = node.node_tree
                    for j in range(len(node.inputs)):
                        for item in node_group.interface.items_tree:
                            if item.in_out == 'INPUT' and item.name == node.inputs[j].name:
                                node.inputs[j].default_value = item.default_value

        return {'FINISHED'}


classes = (
    HOLTALYST_OT_OrganizeOutliner,
    HOLTALYST_OT_ConvertSuffixes,
    HOLTALYST_OT_PurgeUnwantedData,
    HOLTALYST_OT_DeepClean,
    HOLTALYST_OT_SetAutoSmooth,
    HOLTALYST_OT_SyncMeshName,
    HOLTALYST_OT_ShiftToWorldOrigin,
    HOLTALYST_OT_RemoveUnusedSlots,
    HOLTALYST_OT_FixDuplicateNodeGroups,
    HOLTALYST_OT_SetNodeGroupDefaults,
    HOLTALYST_OT_GetNodeGroupDefaults,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
