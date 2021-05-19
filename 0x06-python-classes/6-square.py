#!/usr/bin/python3
"""Class Square"""


class Square:
    """definition class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square with size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter value position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter value position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area and return value"""
        return self.__size ** 2

    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for s in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for x in range(self.__size):
                    print("#", end='')
                print()
