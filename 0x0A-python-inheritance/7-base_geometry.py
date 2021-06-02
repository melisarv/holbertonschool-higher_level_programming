#!/usr/bin/python3
'''Class BaseGeometry'''


class BaseGeometry:
    '''definition class BaseGeometry'''

    def area(self):
        """the raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
