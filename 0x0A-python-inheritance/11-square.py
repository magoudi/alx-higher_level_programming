#!/usr/bin/python3

"""hgfyrdtrdtyfghioiluursred"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """fdtfubybtddhtgkujrdryf"""

    def __init__(self, size):
        """tfytftfuguygiyhiygi"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """jgfytfygdhrdfhjgtsfedfhgjh"""
        return self.__size ** 2

    def __str__(self):
        """hgdfrdeafjyfyrdjygc"""
        return "[Square] {}/{}".format(self.__size, self.__size)
