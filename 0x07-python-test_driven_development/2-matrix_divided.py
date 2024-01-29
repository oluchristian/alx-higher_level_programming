#!/usr/bin/python3
"""
This is the matrix_divided module which has a function
that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    """
    size = len(matrix[0])
    new_list = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for lst in matrix:
        if len(lst) != size:
            raise TypeError("Each row of the matrix must have the same size")
        small_list = []
        for item in lst:
            if not isinstance(item, (int, float)):
                raise TypeError(message)
            value = round(item / div, 2)
            small_list.append(value)
        new_list.append(small_list)
    return new_list
