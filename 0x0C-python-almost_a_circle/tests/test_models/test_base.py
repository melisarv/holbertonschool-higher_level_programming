#!/usr/bin/python3
'''Unittests for Base Class'''

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


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

if __name__ == '__main__':
    unittest.main()
