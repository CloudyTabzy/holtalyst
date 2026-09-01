import bpy
from bpy.types import Panel


class HOLTALYST_PT_MeshStats_Panel(Panel):
    bl_idname = "HOLTALYST_PT_MeshStats_Panel"
    bl_label = "Mesh Statistics"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"

    def draw_header(self, context):
        self.layout.label(text="", icon="INFO")

    def draw(self, context):
        pass


class HOLTALYST_PT_MeshStats_Overview(Panel):
    bl_idname = "HOLTALYST_PT_MeshStats_Overview"
    bl_label = "Scene Overview"
    bl_parent_id = "HOLTALYST_PT_MeshStats_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="SCENE_DATA")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column()

        total_verts = 0
        total_faces = 0
        obj_count = 0
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data:
                total_verts += len(obj.data.vertices)
                total_faces += len(obj.data.polygons)
                obj_count += 1

        col.label(text=f"Mesh Objects: {obj_count}")
        col.label(text=f"Total Vertices: {total_verts:,}")
        col.label(text=f"Total Faces: {total_faces:,}")
        col.separator()
        row = col.row(align=True)
        row.operator("holtalyst.mesh_stats_selected", text="Stats (Selected)")
        row.operator("holtalyst.mesh_stats_scene", text="Stats (Scene)")


class HOLTALYST_PT_MeshStats_Tools(Panel):
    bl_idname = "HOLTALYST_PT_MeshStats_Tools"
    bl_label = "Analysis Tools"
    bl_parent_id = "HOLTALYST_PT_MeshStats_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Holtalyst"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon="VIEWZOOM")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator("holtalyst.mesh_stats_per_object", text="Per-Object Stats (Console)")
        row = col.row(align=True)
        row.operator("holtalyst.find_high_poly", text="Find High-Poly Objects")


classes = (
    HOLTALYST_PT_MeshStats_Panel,
    HOLTALYST_PT_MeshStats_Overview,
    HOLTALYST_PT_MeshStats_Tools,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
