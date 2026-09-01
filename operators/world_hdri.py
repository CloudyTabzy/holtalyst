import bpy
from bpy.types import Operator
from bpy.props import EnumProperty


class HOLTALYST_OT_SwitchWorld(Operator):
    bl_idname = "holtalyst.switch_world"
    bl_label = "Switch World"
    bl_description = "Switch to a different world environment"
    bl_options = {'REGISTER', 'UNDO'}

    world_name: EnumProperty(
        name="World",
        items=lambda self, context: [
            (w.name, w.name, "") for w in bpy.data.worlds
        ],
    )

    def execute(self, context):
        if self.world_name in bpy.data.worlds:
            context.scene.world = bpy.data.worlds[self.world_name]
            self.report({'INFO'}, f"Switched to world: {self.world_name}")
        else:
            self.report({'ERROR'}, f"World not found: {self.world_name}")
        return {'FINISHED'}


class HOLTALYST_OT_CycleWorldNext(Operator):
    bl_idname = "holtalyst.cycle_world_next"
    bl_label = "Next World"
    bl_description = "Cycle to the next world in the list"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        worlds = list(bpy.data.worlds)
        if not worlds:
            self.report({'INFO'}, "No worlds in scene")
            return {'CANCELLED'}
        current = context.scene.world
        if current is None:
            context.scene.world = worlds[0]
        else:
            idx = worlds.index(current) if current in worlds else -1
            next_idx = (idx + 1) % len(worlds)
            context.scene.world = worlds[next_idx]
        self.report({'INFO'}, f"World: {context.scene.world.name}")
        return {'FINISHED'}


class HOLTALYST_OT_CycleWorldPrev(Operator):
    bl_idname = "holtalyst.cycle_world_prev"
    bl_label = "Previous World"
    bl_description = "Cycle to the previous world in the list"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        worlds = list(bpy.data.worlds)
        if not worlds:
            self.report({'INFO'}, "No worlds in scene")
            return {'CANCELLED'}
        current = context.scene.world
        if current is None:
            context.scene.world = worlds[-1]
        else:
            idx = worlds.index(current) if current in worlds else 0
            prev_idx = (idx - 1) % len(worlds)
            context.scene.world = worlds[prev_idx]
        self.report({'INFO'}, f"World: {context.scene.world.name}")
        return {'FINISHED'}


class HOLTALYST_OT_SetWorldColor(Operator):
    bl_idname = "holtalyst.set_world_color"
    bl_label = "Set World Color"
    bl_description = "Set the world background color"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        world = context.scene.world
        if world is None:
            self.report({'ERROR'}, "No world in scene")
            return {'CANCELLED'}
        if world.use_nodes:
            for node in world.node_tree.nodes:
                if node.type == 'BACKGROUND':
                    node.inputs[0].default_value = (0.05, 0.05, 0.05, 1.0)
        else:
            world.color = (0.05, 0.05, 0.05)
        self.report({'INFO'}, "World color reset to default")
        return {'FINISHED'}


class HOLTALYST_OT_ListWorlds(Operator):
    bl_idname = "holtalyst.list_worlds"
    bl_label = "List Worlds"
    bl_description = "List all worlds in the scene"
    bl_options = {'REGISTER'}

    def execute(self, context):
        worlds = list(bpy.data.worlds)
        if not worlds:
            self.report({'INFO'}, "No worlds in scene")
        else:
            names = ", ".join(w.name for w in worlds)
            self.report({'INFO'}, f"Worlds: {names}")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_SwitchWorld,
    HOLTALYST_OT_CycleWorldNext,
    HOLTALYST_OT_CycleWorldPrev,
    HOLTALYST_OT_SetWorldColor,
    HOLTALYST_OT_ListWorlds,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
