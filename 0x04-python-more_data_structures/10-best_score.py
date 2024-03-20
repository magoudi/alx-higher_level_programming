#!/usr/bin/python3
def best_score(a_dictionary):
    first_key = next(iter(a_dictionary))
    first_value = a_dictionary[first_key]
    for i in a_dictionary.values():
        if i > first_value:
            first_value = i
    return first_value
