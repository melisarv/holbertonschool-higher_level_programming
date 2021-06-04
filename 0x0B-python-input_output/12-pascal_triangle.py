#!/usr/bin/python3
"""Pascal Triangle function"""


def pascal_triangle(n):
    """returns a list of integers representing the Pascal's Triangle"""
    my_list = []

    if n <= 0:
        return my_list

    for i in range(n):
        my_list.append([])
        my_list[i].append(1)
        for j in range(1, i):
            my_list[i].append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        if n != 0:
            my_list[i].append(1)

    return my_list
