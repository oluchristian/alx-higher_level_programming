#!/usr/bin/python3
import requests
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(r.text))
print("\t- content:", r.text)
