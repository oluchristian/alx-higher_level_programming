#!/usr/bin/python3
"file input and output"


def read_file(filename=""):
    "function to read a file"
    with open(filename, "r", encoding='utf-8') as file:
        readfile = file.read()
        print(readfile, end="")
