#!/usr/bin/python3
"json serialization"
import json


def to_json_string(my_obj):
    " returns the JSON representation of a string"
    return json.dumps(my_obj)
