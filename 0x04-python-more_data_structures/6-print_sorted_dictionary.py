#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary)
    for i in sorted_k:
        print("{}: {}".format(i, a_dictionary[i]))
