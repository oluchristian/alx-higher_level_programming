#!/usr/bin/python3
import sys
args = sys.argv
commands = args[1:]
total = 0
if __name__ != "__main__":
    exit()
for num in commands:
    total += int(num)
print("{:d}".format(num))

