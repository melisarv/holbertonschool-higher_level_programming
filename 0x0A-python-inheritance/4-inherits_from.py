#!/usr/bin/python3
'''function inherits_from'''


def inherits_from(obj, a_class):
    ''''returns True if the object is an instance of the specified class'''

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
