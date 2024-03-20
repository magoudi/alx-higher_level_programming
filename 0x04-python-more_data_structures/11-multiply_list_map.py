#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    x = list(my_list)
    for i in range(len(my_list)):
        x[i] *= number
    return x
