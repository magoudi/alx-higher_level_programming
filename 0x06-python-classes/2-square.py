#!/usr/bin/python3
"""wergargaawsgdgae"""


class Square:
    """qergwergwergerwgggw"""

    def __init__(self, size=0):
        """ asfgdfgadghadhdhadf

        Args:
            size (int): wfgfgargasrdgadgadg
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
