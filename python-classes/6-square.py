#!/usr/bin/python3
"""
This script defines a class called Square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize the size and position
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple\
 of 2 positive integers")
        for t in position:

            if t < 0 or len(position) != 2 or type(t) is not int:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple\
 of 2 positive integers")
        for t in value:
            if t < 0 or len(value) != 2 or type(t) is not int:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size is 0:
            print()
        for a in range(self.__position[1]):
            print()
        for b in range(self.__size):
            print(" " * self.position[0] + "#" * self.__size)
