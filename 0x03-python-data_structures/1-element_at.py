#!/usr/bin/python3
def element_at(my_list, idx):
    element_at = len(my_list) - 1
    if idx < 0 or idx > element_at:
        return None
    return my_list[idx]
