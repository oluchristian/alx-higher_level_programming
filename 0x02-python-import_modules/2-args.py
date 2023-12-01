import sys
arguements = sys.argv[1:]
argc = len(arguements)
string = "{:d} argument"
count = 1
if __name__ != "__main__":
    exit()
if argc == 0:
    string += 's.'
elif argc == 1:
    string += ':'
elif argc > 1:
    string += 's:'
print(string.format(argc))
for args in arguements:
    print("{:d}: {:s}".format(count, args))
    count += 1
