#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
argc = len(sys.argv[1:])
if argc != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
args = sys.argv[1:]
a = int(args[0])
b = int(args[2])
c = args[1]
operator = ['+', '-', '*', '/']
if args[1] not in operator:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    if c == operator[0]:
        result = add(a, b)
    elif c == operator[1]:
        result = sub(a, b)
    elif c == operator[2]:
        result = mul(a, b)
    elif c == operator[3]:
        result = div(a, b)
print("{:d} {} {:d} = {:d}".format(a, c, b, result))
