import bpy
from bpy.types import Operator


class HOLTALYST_OT_MeshStatsSelected(Operator):
    bl_idname = "holtalyst.mesh_stats_selected"
    bl_label = "Mesh Stats (Selected)"
    bl_description = "Show mesh statistics for selected objects"
    bl_options = {'REGISTER'}

    def execute(self, context):
        total_verts = 0
        total_faces = 0
        total_edges = 0
        obj_count = 0
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.data:
                verts = len(obj.data.vertices)
                faces = len(obj.data.polygons)
                edges = len(obj.data.edges)
                total_verts += verts
                total_faces += faces
                total_edges += edges
                obj_count += 1
        if obj_count == 0:
            self.report({'INFO'}, "No mesh objects selected")
        else:
            self.report({'INFO'}, f"{obj_count} meshes: {total_verts:,} verts, {total_faces:,} faces, {total_edges:,} edges")
        return {'FINISHED'}


class HOLTALYST_OT_MeshStatsScene(Operator):
    bl_idname = "holtalyst.mesh_stats_scene"
    bl_label = "Mesh Stats (Scene)"
    bl_description = "Show mesh statistics for all objects in the scene"
    bl_options = {'REGISTER'}

    def execute(self, context):
        total_verts = 0
        total_faces = 0
        total_edges = 0
        obj_count = 0
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data:
                verts = len(obj.data.vertices)
                faces = len(obj.data.polygons)
                edges = len(obj.data.edges)
                total_verts += verts
                total_faces += faces
                total_edges += edges
                obj_count += 1
        if obj_count == 0:
            self.report({'INFO'}, "No mesh objects in scene")
        else:
            self.report({'INFO'}, f"{obj_count} meshes: {total_verts:,} verts, {total_faces:,} faces, {total_edges:,} edges")
        return {'FINISHED'}


class HOLTALYST_OT_MeshStatsPerObject(Operator):
    bl_idname = "holtalyst.mesh_stats_per_object"
    bl_label = "Mesh Stats (Per Object)"
    bl_description = "Show per-object mesh statistics in the console"
    bl_options = {'REGISTER'}

    def execute(self, context):
        print("\n=== Mesh Statistics ===")
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.data:
                verts = len(obj.data.vertices)
                faces = len(obj.data.polygons)
                edges = len(obj.data.edges)
                tris = sum(len(p.vertices) - 2 for p in obj.data.polygons)
                print(f"  {obj.name}: {verts:,} verts, {faces:,} faces, {edges:,} edges, ~{tris:,} tris")
        print("=======================\n")
        self.report({'INFO'}, "Stats printed to console (Window > Toggle System Console)")
        return {'FINISHED'}


class HOLTALYST_OT_FindHighPolyObjects(Operator):
    bl_idname = "holtalyst.find_high_poly"
    bl_label = "Find High-Poly Objects"
    bl_description = "Find objects with vertex count above a threshold"
    bl_options = {'REGISTER'}

    def execute(self, context):
        threshold = 100000
        found = []
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data:
                if len(obj.data.vertices) > threshold:
                    found.append((obj.name, len(obj.data.vertices)))
        if found:
            found.sort(key=lambda x: x[1], reverse=True)
            names = ", ".join(f"{n} ({v:,})" for n, v in found[:5])
            self.report({'WARNING'}, f"High-poly: {names}")
        else:
            self.report({'INFO'}, f"No objects above {threshold:,} vertices")
        return {'FINISHED'}


classes = (
    HOLTALYST_OT_MeshStatsSelected,
    HOLTALYST_OT_MeshStatsScene,
    HOLTALYST_OT_MeshStatsPerObject,
    HOLTALYST_OT_FindHighPolyObjects,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
