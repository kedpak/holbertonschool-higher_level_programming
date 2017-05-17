#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def testOne(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def testTwo(self):
        self.assertEqual(max_integer([2]), 2)

    @unittest.expectedFailure
    def test_char(self):
        self.assertTrue(max_integer([a, 1, 2, 4]), broken)

    @unittest.expectedFailure
    def test_empty(self):
        self.assertNone(max_integer(), broken)

    @unittest.expectedFailure
    def one_neg(self):
        self.assertEqual(max_integer([1, 5, -4, 9]), broken)

    @unittest.expectedFailure
    def all_neg(self):
        self.assertEqual(max_integer([-4, -5, -2, -10]), broken)

if __name__ == '__main__':
    unittest.main()
