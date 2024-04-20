#!/usr/bin/python3

"""asfgjvnifbvibrgbhbfdgcbnksrnib"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """wfivbwgfheirhguthbwrgibegb"""

    def __init__(self, size, x=0, y=0, id=None):
        """sdfgvgcbwjehsdvusdbfguyfeiurhguybkgufbuy"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """adgfaeahsrthfgvsrgdhfhgv"""
        return self.width

    @size.setter
    def size(self, value):
        """fgvjfgbugnijsjibvjnfxfc"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):


    def __str__(self):
        """wdfjogjfoiwngiodmseghuoasdfbiub"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
