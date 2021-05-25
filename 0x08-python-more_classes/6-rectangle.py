#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """definition class rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes rectangle with width, height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter value width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter value width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter value height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter value height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """return string for the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result[:-1]

    def __repr__(self):
        """return string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """print the message when is delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
