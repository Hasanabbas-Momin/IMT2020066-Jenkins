#!/usr/bin/python3
# Passing Test case for checking factorial of numbers

import unittest
from factorial import my_factorial


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(my_factorial(0), 1)

    def testCase2(self):
        self.assertEqual(my_factorial(1), 1)

    def testCase3(self):
        self.assertEqual(my_factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
