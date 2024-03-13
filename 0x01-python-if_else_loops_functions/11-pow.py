#!/usr/bin/python3
def pow(a, b):
    x = a
    for i in range(b):
        a = a * x
    return a
