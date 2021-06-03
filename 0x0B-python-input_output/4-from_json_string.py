#!/usr/bin/python3
"""JSON function"""
import json


def from_json_string(my_str):
    """function that returns an object represented by JSON string"""

    return json.loads(my_str)
