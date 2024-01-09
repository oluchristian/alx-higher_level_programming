#!/usr/bin/python3
class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """hprints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
