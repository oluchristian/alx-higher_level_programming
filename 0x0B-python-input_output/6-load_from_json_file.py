#!/usr/bin/python3
"Object from a json file"
import json


def load_from_json_file(filename):
    "function that creates an Object from a JSON file"
    with open(filename, "r", encoding="UTF-8") as file:
        return json.load(file)
