#!/usr/bin/python3
'''Class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''definition Class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''instance initialization method'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter method'''
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''height getter method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter method'''
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''x getter method'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter method'''
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''y getter method'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter method'''
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        '''check if value is an integer'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        '''returns the area value of the Rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints the Rectangle instance with the character #'''
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        '''returns string format'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''update attributes'''
        index = 0
        if args is not None and len(args) != 0:
            for a in args:
                index += 1
                if index == 1:
                    self.id = a
                elif index == 2:
                    self.__width = a
                elif index == 3:
                    self.__height = a
                elif index == 4:
                    self.__x = a
                elif index == 5:
                    self.__y = a
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        my_dic = {'x': self.__x, 'y': self.__y, 'id': self.id,
                  'height': self.__height, 'width': self.__width}
        return my_dic
