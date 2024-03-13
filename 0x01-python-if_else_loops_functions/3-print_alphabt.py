#!/usr/bin/python3
for i in range(26):
    if i == ord('q') - 97 or i == ord('e') - 97:
        continue
    else:
        print("{}".format(chr(97+i)), end="")
