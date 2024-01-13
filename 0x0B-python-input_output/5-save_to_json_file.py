#!/usr/bin/python3
"Save Object to a file"
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF-8") as file:
        if isinstance(my_obj, set):
            my_obj = list(my_obj)
        return json.dump(my_obj, file)
