#!/usr/bin/python3
"""
Function say_my_name
say_my_name: prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints strings My name is first_name last_name
    Args: first_name is a string and last_name is a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
