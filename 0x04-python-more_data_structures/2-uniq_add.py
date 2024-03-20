#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    else:
        x = my_list[0]
    for i in range(1, len(my_list)):
        f = 1
        for j in range(i):
            if my_list[i] == my_list[j]:
                f = 0
        if f == 1:
            x += my_list[i]
    return x
