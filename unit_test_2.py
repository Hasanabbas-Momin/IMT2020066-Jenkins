#!/usr/bin/python3
# Failing Test case for factorial

import unittest
from factorial import my_factorial


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(my_factorial(-1), 1)

    def testCase2(self):
        self.assertEqual(my_factorial(2.5), 2)


if __name__ == '__main__':
    unittest.main()
