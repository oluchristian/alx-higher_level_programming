#!/usr/bin/python3
"""An Square class"""


class Square:
    """a class Square that defines a square by
        - private instance attribute
        - Instantiation with size
        """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Public instance method that returns the current square area"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter to set the size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints # to stdout
        """
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

    @property
    def position(self):
        """A getter to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """A setter to set the position to value"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of positve integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("size must be a positive number")
        self.__size = value
