#!/usr/bin/python3
"file input and out put. Writing to file"


def write_file(filename="", text=""):
    "write to a file and return the number of characters"
    with open(filename, "w", encoding="UTF8") as file:
        writefile = file.write(text)
        return file.tell()
