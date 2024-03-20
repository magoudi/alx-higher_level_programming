#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    x = map(lambda y: y * number, my_list)
    x= list(x)
    return x
