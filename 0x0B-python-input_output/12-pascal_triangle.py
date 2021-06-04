#!/usr/bin/python3
"""Pascal Triangle function"""


def pascal_triangle(n):
    """returns a list of integers representing the Pascal's Triangle"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        number = 11**i
        lis = [int(n) for n in str(number)]
        my_list.append(lis)
    return my_list
