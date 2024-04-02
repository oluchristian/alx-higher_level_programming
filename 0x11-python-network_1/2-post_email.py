#!/usr/bin/python3
"""Python script that sends a POST request to the passed URL"""
import urllib.request
import sys
if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(sys.argv[1], encoded_data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
