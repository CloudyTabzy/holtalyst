import bpy
from .common import is_string


def create_texture(name="Texture", type='CLOUDS'):
    if type is not None:
        return bpy.data.textures.new(name, type.upper())
    return None


def get_texture(ref):
    if is_string(ref):
        if ref in bpy.data.textures:
            return bpy.data.textures[ref]
    return ref


def get_all_textures():
    return bpy.data.textures


def get_list_of_textures():
    return get_all_textures()


def rename_texture(ref, name):
    texref = get_texture(ref)
    if name is not None:
        texref.name = name


def delete_texture(ref):
    if is_string(ref):
        bpy.data.textures.remove(get_texture(ref))
    else:
        bpy.data.textures.remove(ref)


def create_image(name='Image', width=1024, height=1024):
    return bpy.data.images.new(name=name, width=width, height=height)


def get_image(ref):
    if is_string(ref):
        if ref in bpy.data.images:
            return bpy.data.images[ref]
    return ref


def get_all_images():
    return bpy.data.images


def get_list_of_images():
    return get_all_images()


def rename_image(ref, name):
    imgref = get_image(ref)
    if name is not None:
        imgref.name = name


def delete_image(ref):
    if is_string(ref):
        bpy.data.images.remove(get_image(ref))
    else:
        bpy.data.images.remove(ref)
