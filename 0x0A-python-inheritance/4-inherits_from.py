#!/usr/bin/python3
"""inherited instance of a class"""


def inherits_from(obj, a_class):
    """returns true or flase if instance inherits a class"""
    obj_type = type(obj)
    return issubclass(obj_type, a_class) and obj_type != a_class
