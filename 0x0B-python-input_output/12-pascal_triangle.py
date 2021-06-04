#!/usr/bin/python3
"""Pascal Triangle function"""


def pascal_triangle(n):
    """returns a list of integers representing the Pascal's Triangle"""
    my_list = [[1]]

    if n <= 0:
        return []

    for i in range(n - 1):
        list1 = []
        list1.append(1)
        for j in range(i):
            list1.append(my_list[i][j] + my_list[i][j+1])
        if n != 0:
            list1.append(1)

        my_list.append(list1)

    return my_list
