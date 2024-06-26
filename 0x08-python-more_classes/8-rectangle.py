#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """creating a rectangle"""

    number_of_instances = 0
    print_symbol = None
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gbahbfgasvhbdfhv"""
        return self.width * self.height

    def perimeter(self):
        """gfndfgbsifbgvkdgff"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """sdfgbskhdfbvhksdbfhbv"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            for j in range(self.width):
                rect += str(self.print_symbol)
            if i < self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
