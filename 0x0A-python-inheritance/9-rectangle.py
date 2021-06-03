#!/usr/bin/python3
'''Class Rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''definition class Rectangle'''

    def __init__(self, width, height):
        '''initialization class Rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''calculate area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''return string format'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
