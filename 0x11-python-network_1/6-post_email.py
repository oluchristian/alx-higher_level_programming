#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.get(url, params=payload)
    print(r.text)
