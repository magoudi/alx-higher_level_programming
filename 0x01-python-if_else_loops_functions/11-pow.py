#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / float(a)
        print(a)
        b = abs(b)
    x = a
    for i in range(b - 1):
        x = x * a
    return x
