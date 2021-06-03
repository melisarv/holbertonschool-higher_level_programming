#!/usr/bin/python3
"""JSON function"""


def class_to_json(obj):
    """function that returns the dictionary description with simple data structure
    for JSON serialization of an object"""

    return vars(obj)
