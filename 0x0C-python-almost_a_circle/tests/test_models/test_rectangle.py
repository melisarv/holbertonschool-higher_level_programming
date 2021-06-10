#!/usr/bin/python3
'''Unittests for Rectangle Class'''
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    '''Test class for Rectangle class'''

    def setUp(self):
        '''setup class'''
        Base._Base__nb_objects = 0

    def test10(self):
        '''test10'''
        rec1 = Rectangle(1, 2)
        self.assertEqual(rec1.id, 1)
        rec2 = Rectangle(3, 4)
        self.assertEqual(rec2.id, 2)
        rec3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rec3.id, 12)
        rec4 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(rec4.id, -5)

    def test11(self):
        '''test11'''
        r1 = Rectangle(10, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 4, 5, 6, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 6)

    def test12(self):
        '''test12'''
        r1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test13(self):
        '''test13'''
        with self.assertRaises(TypeError) as x:
            r = Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "Fun")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 2, "Hi")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(-1, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, -1)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 5, 5, -6)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test14(self):
        '''test14'''
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(75, 2)
        self.assertEqual(r2.area(), 150)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test15(self):
        '''test15'''
        f = io.StringIO()
        r1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test16(self):
        '''test16'''
        f = io.StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)

    def test17(self):
        '''test17'''
        f = io.StringIO()
        r1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test18(self):
        '''test18'''
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

    def test19(self):
        '''test19'''
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 1)
        self.assertEqual(r1.width, 1)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 1)
        self.assertEqual(r1.y, 1)

    def test20(self):
        '''test20'''
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89)
        self.assertEqual(r1.id, 89)
        r1.update(id=90, width=4)
        self.assertEqual(r1.width, 4)
        r1.update(id=89, width=4, height=2)
        self.assertEqual(r1.height, 2)
        r1.update(id=70, width=44, height=22, x=3)
        self.assertEqual(r1.x, 3)
        r1.update(id=70, width=44, height=22, x=3, y=4)
        self.assertEqual(r1.id, 70)
        self.assertEqual(r1.width, 44)
        self.assertEqual(r1.height, 22)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
