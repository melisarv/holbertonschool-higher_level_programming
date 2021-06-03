#!/usr/bin/python3
"""JSON save function"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as f:
        written = json.dump(my_obj, f)
    return written
