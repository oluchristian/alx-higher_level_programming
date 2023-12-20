#!/usr/bin/python3
"""An Square class"""


class Square():
    """
    Class that defines properties of square by: (based on 0-square.py).
    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size):
        """
        Initializes a Square instance.
        
        Args:
            size: size of the square.
        """
        self.__size = size
