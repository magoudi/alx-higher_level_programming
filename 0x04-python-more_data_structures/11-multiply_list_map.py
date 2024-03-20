#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    y = map(lambda h: h * number, my_list)
    x = list(y)
    return x
