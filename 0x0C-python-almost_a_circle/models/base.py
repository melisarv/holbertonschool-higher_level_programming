#!/usr/bin/python3
''' Class Base'''
import json
import os
import csv


class Base:
    '''definition Class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs'''
        my_list = []
        if list_objs is not None:
            my_list = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(my_list))
