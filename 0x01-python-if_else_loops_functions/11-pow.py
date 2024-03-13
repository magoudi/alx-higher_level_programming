#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
        b = abs(b)
    x = a
    for i in range(b - 1):
        if a >= 1:
            a = a * x
        else:
            a = float(a * x)
    return a
