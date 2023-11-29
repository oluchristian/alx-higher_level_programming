#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    if (n < 0) or (n >= len(str)):
        return str
    for i in str:
        if i == str[n]:
            continue
        new += i
    return new
