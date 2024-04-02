#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as request:
        info = request.info().get("X-Request-Id")
        print(info)
