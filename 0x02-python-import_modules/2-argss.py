#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
argc = len(arguments)

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(argc))

count = 1
for arg in arguments:
    print("{:d}: {:s}".format(count, arg))
    count += 1
