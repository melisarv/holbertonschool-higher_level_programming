#!/usr/bin/python3
"""Class Square"""


class Square:
    """definition class square"""

    def __init__(self, size=0):
        """Initializes square with size"""
        self.size = size

    @property
    def size(self):
        """Getter value size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter value size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area and return value"""
        return self.__size ** 2

    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
