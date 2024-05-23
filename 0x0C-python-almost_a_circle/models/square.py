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
        """Sdfbsdfbvsdfgvdfgvdsfzcgdfcgvdfcgv"""
        listt = [None, None, None, None]
        klist = {"id" : None, "x" : None, "y" : None, "size" : None}
        i = 0
        for arg in args:
            listt[i] = arg
            i += 1
        for key, value in kwargs.items():
            klist[key] = value
        if i > 0:
            self.id = listt[0]
        if i > 1:
            self.size = listt[1]
        if i > 2:
            self.x = listt[2]
        if i > 3:
            self.y = listt[3]
        if i == 0:
            if klist["id"] != None:
                self.id = klist["id"]
            if klist["x"] != None:
                self.x = klist["x"]
            if klist["y"] != None:
                self.y = klist["y"]
            if klist["size"] != None:
                self.size = klist["size"]

    def __str__(self):
        """wdfjogjfoiwngiodmseghuoasdfbiub"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """sdfgsdfgsdfbbgdsgbdgzbdzfbzdbxvx"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
