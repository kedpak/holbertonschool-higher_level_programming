#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def setUP(self):
        pass
    def tearDown(self):
        pass
    def testOne(self):
        max_integer([1, 2, 3, 4])
    def testTwo(self):
        self.assertTrue(max_intger
        max_integer([a, 1, 2, 4])
        with self.assertRaises(TypeError):
            print("type")
    def testThree(self):
        max_integer([4, 4.4, 4.8])




if __name__ == '__main__':
    unittest.main()
