#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

'''Class Rectangle'''


class Rectangle(BaseGeometry):
    '''definition class Rectangle'''

    def __init__(self, width, height):
        '''initialization class Rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
