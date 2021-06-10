#!/usr/bin/python3
'''Unittests for Base Class'''
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Test class for Base class'''

    def setUp(self):
        '''setup class'''
        Base._Base__nb_objects = 0

    def test01(self):
        '''test01: instances'''
        bs1 = Base()
        self.assertEqual(bs1.id, 1)
        bs2 = Base()
        self.assertEqual(bs2.id, 2)
        bs3 = Base(14)
        self.assertEqual(bs3.id, 14)
        bs4 = Base(899)
        self.assertEqual(bs4.id, 899)
        bs5 = Base(0)
        self.assertEqual(bs5.id, 0)
        bs6 = Base(-1)
        self.assertEqual(bs6.id, -1)

    def test02(self):
        '''test02: method to_json_string'''
        dic = {'x': 5, 'width': 10, 'id': 1, 'height': 8, 'y': 6}
        j_dic = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(j_dic, str))
        j_dic1 = Base.to_json_string([])
        self.assertEqual(j_dic1, "[]")
        j_dic2 = Base.to_json_string(None)
        self.assertEqual(j_dic2, "[]")

    def test03(self):
        '''test03: method from_json_string'''
        ls = [{'id': 10, 'width': 7, 'height': 4},
              {'id': 90, 'width': 10, 'height': 8}]
        j_ls = Base.to_json_string(ls)
        j_f_ls = Base.from_json_string(j_ls)
        self.assertTrue(isinstance(j_f_ls, list))

        j_f_ls1 = Base.from_json_string('')
        self.assertEqual(j_f_ls1, [])
        j_f_ls2 = Base.from_json_string(None)
        self.assertEqual(j_f_ls2, [])

    def test04(self):
        '''test04: method create'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test05(self):
        '''test05: method load_from_file'''

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        list_rect = Rectangle.load_from_file()
        self.assertEqual(list_rect, [])
        list_square = Square.load_from_file()
        self.assertEqual(list_square, [])

    def test06(self):
        '''test06: method save_to_file'''
        r0 = Rectangle(20, 10, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r0, r1])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 20, "height": 10},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

        s0 = Square(19, 5, 1, 12)
        s1 = Square(6, 7)
        Square.save_to_file([s0, s1])
        res = ('[{"id": 12, "size": 19, "x": 5, "y": 1},' +
               ' {"id": 3, "size": 6, "x": 7, "y": 0}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
