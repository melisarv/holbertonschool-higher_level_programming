#!/usr/bin/python3
'''Class Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''definition class Square'''

    def __init__(self, size):
        '''initialization class Square'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''return string format'''
        return "[Square] {}/{}".format(self.__size, self.__size)
