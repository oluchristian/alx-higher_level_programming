#!/usr/bin/python3
"""An Square class"""


class Square:
    """a class Square that defines a square by
        - private instance attribute
        - Instantiation with size
        """
    def __init__(self, size=0):
        """Initializes a Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
