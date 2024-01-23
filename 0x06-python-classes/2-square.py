#!/usr/bin/python3

"""define a square"""


class Square:
    """represent a square"""
    
    __size = 0
    def __init__(self, size)
        """initialize a square
        
        Args:
            size(int):asdfasdfsdsd
        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
