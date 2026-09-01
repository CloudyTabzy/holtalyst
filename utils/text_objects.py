import bpy


def create_text_file(textname):
    return bpy.data.texts.new(textname)


def delete_text_file(textname):
    if isinstance(textname, str):
        t = bpy.data.texts[textname]
        bpy.data.texts.remove(t)
    else:
        bpy.data.texts.remove(textname)


def get_lines_in_text_object(textname):
    return bpy.data.texts[textname].lines
