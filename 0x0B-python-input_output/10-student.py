#!/usr/bin/python3
"""Class Student"""


class Student:
    """"definition class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description of student instance"""
        if attrs is None:
            return self.__dict__

        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value

        return dic
