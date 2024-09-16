#!/usr/bin/python3
"""
This script defines a class called Rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def witdh(self, value):
        if type(value) is not int or value < 0:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int or value < 0:
            raise TypeError("height must be an integer")
        self.__height = value
