#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tve_last = number % 10
if number < 0:
    last_digit = abs(number) % 10
    neg_last_digit = -last_digit
    print(f"Last digit of {number:d} is {neg_last_digit:d} and is less than 6 and not 0")
elif number > 5:
    print(f"Last digit of {number:d} is {tve_last:d} and is greater than 5")
elif (number < 6) and (number != 0):
    print(f"Last digit of {number:d} is {tve_last:d} and is less than 6 and not 0")
elif number  == 0:
    print(f"Last digit of {number:d} is {tve_last:d} and is 0")