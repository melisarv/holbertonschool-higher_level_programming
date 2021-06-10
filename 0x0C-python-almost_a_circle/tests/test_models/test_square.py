#!/usr/bin/python3
'''Unittests for Square Class'''
import unittest
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Test class for Square class'''

    def setUp(self):
        '''setup class'''
        Base._Base__nb_objects = 0

    def test30(self):
        '''test30'''
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(5, 3, 4)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 2)
        s3 = Square(9, 8, 7, 2)
        self.assertEqual(s3.size, 9)

    def test31(self):
        '''test31'''
        with self.assertRaises(TypeError) as x:
            s = Square("1")
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, "2")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "3")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, 5, -5)
        self.assertEqual("y must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0)
        self.assertEqual("width must be > 0", str(x.exception))

    def test32(self):
        '''test32'''
        s1 = Square(9, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

    def test33(self):
        '''test33'''
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

    def test34(self):
        '''test34'''
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test35(self):
        '''test35'''
        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(x.exception))
