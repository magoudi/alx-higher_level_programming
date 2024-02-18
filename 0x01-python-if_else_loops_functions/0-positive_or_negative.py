#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{0}is positive", number)
elif number == 0:
    print(f"{0}is zero", number)
else:
    print(f"{0}is negative", number)
