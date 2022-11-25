#!/usr/bin/python3

import unittest
from palindrome import f


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(f("12321"), True)

    def testCase2(self):
        self.assertEqual(f("1212"), False)

    def testCase3(self):
        self.assertEqual(f("9"), True)


if __name__ == '__main__':
    unittest.main()
