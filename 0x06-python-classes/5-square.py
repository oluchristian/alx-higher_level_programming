#!/usr/bin/python3
"""An Square class"""


class Square:
    """a class Square that defines a square by
        - private instance attribute
        - Instantiation with size
        """

    def __init__(self, size=0):
        """Initializes a Square instance."""
        self.__size = size

    @property
    def size(self):
        """Public instance method that returns the current square area"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter to set the size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
