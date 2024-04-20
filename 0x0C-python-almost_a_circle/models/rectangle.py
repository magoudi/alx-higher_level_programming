#!/usr/bin/python3

"""kkugrcazxcvbnmkuytrdcvb"""
from models.base import Base


class Rectangle(Base):
    """gvtesrwzxcvbninyfutrx"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """jfytdftrdfggihiuguyfuf"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """wgrfvsdfgvsedfgsvsedfgvdfsg"""
        return self.__width

    @width.setter
    def width(self, value):
        """dfbvsdghrstfgetfhgsdfgdfg"""
        self.valint(value, "width", True)
        self.__width = value

    @property
    def height(self):
        """wgrfvsdfgvsedfgsvsedfgvdfsg"""
        return self.__height

    @height.setter
    def height(self, value):
        """dfbvsdghrstfgetfhgsdfgdfg"""
        self.valint(value, "height", True)
        self.__height = value

    @property
    def x(self):
        """wgrfvsdfgvsedfgsvsedfgvdfsg"""
        return self.__x

    @x.setter
    def x(self, value):
        """dfbvsdghrstfgetfhgsdfgdfg"""
        self.valint(value, "x", False)
        self.__x = value

    @property
    def y(self):
        """wgrfvsdfgvsedfgsvsedfgvdfsg"""
        return self.__y

    @y.setter
    def y(self, value):
        """dfbvsdghrstfgetfhgsdfgdfg"""
        self.valint(value, "y", False)
        self.__y = value

    def valint(self, value, name, tf):
        """sdfhbsdhbdhfghvfghbfxgb"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if tf:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """wvadvgbradccbrfffrrrabkk"""
        return self.width * self.height

    def display(self):
        """dfgbjdgvnjgnvajfjnlgejrnfkdm"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
