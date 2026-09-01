import bpy
from .common import is_string, get_object


def set_material_use_nodes(matref, value):
    matref.use_nodes = value


def set_material_to_use_nodes(matref=None, value=None):
    set_material_use_nodes(matref, value)


def get_material_nodes(ref):
    from .materials import get_material
    mat = get_material(ref)
    return mat.node_tree.nodes


def get_node(nodes, ref):
    if is_string(ref):
        for n in nodes:
            if n.name == ref:
                return n
    return ref


def get_nodes(mat):
    node_tree = mat.node_tree
    if node_tree:
        return node_tree.nodes
    return None


def get_node_tree(matref, make_tree=True):
    matref.use_nodes = make_tree
    return matref.node_tree


def get_node_group(name):
    if name in bpy.data.node_groups:
        return bpy.data.node_groups[name]
    return None


def get_all_node_groups():
    return bpy.data.node_groups


def create_node(nodes, nodetype):
    return nodes.new(type=nodetype)


def delete_node(nodes, ref):
    noderef = get_node(nodes, ref)
    if noderef is not None:
        nodes.remove(noderef)


def get_node_links(matref):
    return matref.node_tree.links


def create_node_link(point1, point2):
    links = point1.id_data.links
    return links.new(point1, point2)


def create_link(point1=None, point2=None):
    return create_node_link(point1, point2)


def get_index_of_output(node, name):
    for i in range(len(node.outputs)):
        if node.outputs[i].name == name:
            return i
    return None


def get_index_of_input(node, name):
    for i in range(len(node.inputs)):
        if node.inputs[i].name == name:
            return i
    return None


def get_world_nodes(index=None):
    if index is not None:
        return bpy.data.worlds[index].node_tree.nodes
    return bpy.data.worlds[0].node_tree.nodes


def replace_duplicate_nodes(nodes):
    for node in nodes:
        if node.type == 'GROUP':
            if '.' in node.name:
                sname = node.node_tree.name.split('.')
                if sname[0] in bpy.data.node_groups:
                    node.node_tree = bpy.data.node_groups[sname[0]]


def fix_node_duplicates():
    for m in bpy.data.materials:
        matnodes = get_nodes(m)
        if matnodes:
            replace_duplicate_nodes(matnodes)
    for ng in bpy.data.node_groups:
        ngnodes = ng.nodes
        replace_duplicate_nodes(ngnodes)


def fix_duplicate_nodes():
    fix_node_duplicates()
