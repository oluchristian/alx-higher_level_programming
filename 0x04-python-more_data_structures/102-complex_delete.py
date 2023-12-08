#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_del = []
    for key, values in a_dictionary.items():
        if values == value:
            key_del.append(key)
    for key in key_del:
        del a_dictionary[key]
    return a_dictionary
