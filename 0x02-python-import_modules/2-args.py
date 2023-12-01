import sys
arguements = sys.argv
argc = len(arguements)
count = 1
if __name__ == "__main__":
    if argc == 1:
        print("{} arguments.".format(0))
    elif argc == 2:
        print("{} argument.".format(argc - 1))
        print("{}: {}".format(argc - 1, arguements[1]))
    elif argc > 2:
        print("{} arguments.".format(argc - 1))
        for args in arguements:
            if args != arguements[0]:
                print("{}: {}".format(count, args))
                count += 1 
