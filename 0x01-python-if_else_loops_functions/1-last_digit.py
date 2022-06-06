#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[len(str(number)) - 1]
l = int(last_digit)
if number < 0:
    l *= -1
if l > 5:
    print(f"Last digit of {number} is {l} and is greater than 5")
elif l < 6 and l != 0:
    print(f"Last digit of {number} is {l} and is less than 6 and not 0")
elif l == 0:
    print(f"Last digit of {number} is {l} and is 0")
else:
    pass
