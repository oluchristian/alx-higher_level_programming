import sys

arguments = sys.argv[1:]
argc = len(arguments)

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(argc))

for idx, arg in enumerate(arguments, start=1):
    print("{:d}: {:s}".format(idx, arg))

