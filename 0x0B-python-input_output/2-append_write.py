#!/usr/bin/python3
"writing to a file by appending"


def append_write(filename="", text=""):
    "appends a string at the end of a text file"
    with open(filename, "a", encoding="UTF8") as file:
        appendfile = file.write(text)
        return file.tell()
