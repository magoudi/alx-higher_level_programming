#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = dict(a_dictionary)
    for i in a_dict.keys():
        a_dict[i] *= 2
    return a_dict
