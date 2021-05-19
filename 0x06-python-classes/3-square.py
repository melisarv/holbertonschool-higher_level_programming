#!/usr/bin/python3
"""Class Square"""


class Square:
    """definition class square"""

    def __init__(self, size=0):
        """Initializes square with size and validate that integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate area and return value"""
        area = self.__size ** 2
        return area
