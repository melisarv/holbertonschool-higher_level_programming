#!/usr/bin/python3
"""Class Student"""


class Student:
    """"definition class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description of student instance"""
        return vars(self)
