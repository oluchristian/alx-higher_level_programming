#!/usr/bin/python3
"""0x11. Python - Network #1"""
import urllib.request
if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type:", type(the_page))
        print("\t- content:", the_page)
        print("\t- utf8 content:", the_page.decode('utf-8'))
