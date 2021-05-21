#!/usr/bin/python3
"""
Function add_integer
add_integer: adds 2 integers and return result
"""


def add_integer(a, b=98):
    """
    Return result of adds 2 integers, validation type integer or float
    Args: a is int/float and b is int/float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
