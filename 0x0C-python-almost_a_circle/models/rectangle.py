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
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                    print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """rgdhfgbdgfhbfgbvrsfgvrgfhbvgbvgfv"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Sdfbsdfbvsdfgvdfgvdsfzcgdfcgvdfcgv"""
        listt = [None, None, None, None, None]
        klist = {"id" : None, "x" : None, "y" : None, "width" : None, "height" : None}
        i = 0
        for arg in args:
            listt[i] = arg
            i += 1
        for key, value in kwargs.items():
            klist[key] = value
        if i > 0:
            self.id = listt[0]
        if i > 1:
            self.width = listt[1]
        if i > 2:
            self.height = listt[2]
        if i > 3:
            self.x = listt[3]
        if i > 4:
            self.y = listt[4]
        if i == 0:
            if klist["id"] != None:
                self.id = klist["id"]
            if klist["x"] != None:
                self.x = klist["x"]
            if klist["y"] != None:
                self.y = klist["y"]
            if klist["height"] != None:
                self.height = klist["height"]
            if klist["width"] != None:
                self.width = klist["width"]

    def to_dictionary(self):
        """srgsdfgsdfzgvdfzgvdszfgvdzfgxv"""
        return {'x' : self.x, 'y' : self.y, 'id' : self.id, 'height' : self.height, 'width' : self.width}
