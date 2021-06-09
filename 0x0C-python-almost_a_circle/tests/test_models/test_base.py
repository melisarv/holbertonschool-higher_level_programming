#!/usr/bin/python3
'''Unittests for Base Class'''

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest, sys, json

class TestBase(unittest.TestCase):
    '''Test class for Base class'''

    def setUp(self):
        Base._Base__nb_objects = 0



