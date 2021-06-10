#!/usr/bin/python3
'''Class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''definition Class Square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''instance initialization method'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return string format'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update attributes'''
        index = 0
        if args is not None and len(args) != 0:
            for a in args:
                index += 1
                if index == 1:
                    self.integer_validator("id", a)
                    self.id = a
                elif index == 2:
                    self.size = a
                elif index == 3:
                    self.x = a
                elif index == 4:
                    self.y = a
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        my_dic = {'id': self.id, 'x': self.x, 'size': self.size,
                  'y': self.y}
        return my_dic
