#!/usr/bin/python3
"""Module to test function max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to test function max_integer"""

    def test_max_integer(self):
        """ test function max_integer"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([100, 25, 3, 99]), 100)
        self.assertEqual(max_integer([-8, 5, 20, 12]), 20)
        self.assertEqual(max_integer([-8, -10, -33, 22]), 22)
        self.assertEqual(max_integer([-1, -10, -2, -20]), -1)
        self.assertEqual(max_integer([0.8, 5.5, 1.1, 2.2]), 5.5)
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
