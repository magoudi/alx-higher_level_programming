#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
        return x
    except Exception:
        print()
        return count
