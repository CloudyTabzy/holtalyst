from .common import get_object, so


def get_light(ref):
    obj = get_object(ref)
    return obj.data


def light_power(val=0, ref=None):
    objlist = [ref] if ref is not None else so()
    for o in objlist:
        o.data.energy = val


def light_intensity(val=0, ref=None):
    light_power(val, ref)


def light_power_add(val=0, ref=None):
    objlist = [ref] if ref is not None else so()
    for o in objlist:
        o.data.energy += val


def light_intensity_add(val=0, ref=None):
    light_power_add(val, ref)


def light_power_multiply(val=0, ref=None):
    objlist = [ref] if ref is not None else so()
    for o in objlist:
        o.data.energy *= val


def light_intensity_multiply(val=0, ref=None):
    light_power_multiply(val, ref)
