#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sdict = sorted(a_dictionary.keys())
    for i in sdict:
        print("{}: {}".format(i, a_dictionary[i]))
