#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    new_list[new_list.index(search)] = replace
    return new_list
