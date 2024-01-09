#!/usr/bin/python3
"""func to return list of attributes and methods of an object"""


def lookup(obj):
    """returns a list of atributes and methods of an obj"""
    return dir(obj)
