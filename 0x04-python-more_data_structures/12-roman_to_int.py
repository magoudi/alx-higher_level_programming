#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        x, prev = 0, roman_string[0]
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            if dic[i] > dic[prev]:
                x = x + dic[i] - 2 * dic[prev]
            else:
                x += dic[i]
            prev = i
        return x
    return 0
