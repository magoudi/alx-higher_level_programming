#!/usr/bin/python3

"""Module for BaseGeometry class."""


class BaseGeometry:
    """A BaseGeometry class."""

    def area(self):
        """Method to compute this area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating the value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
