#!/usr/bin/python3
"""
This script defines a class called Square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        initialize the size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
