#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """creating a rectangle"""
        
    def __init__(self, width=0, height=0):
        """fjnvjksdfngkjsbdfgbskdhfbv"""
        self.width = width
        self.heigth = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
