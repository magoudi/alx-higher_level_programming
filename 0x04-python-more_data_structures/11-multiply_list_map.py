#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    x = list(my_list)
    map(lambda y: y * number, x)
    return x
