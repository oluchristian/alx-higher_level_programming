#!/usr/bin/python3
"""Python script that sends a POST request"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
