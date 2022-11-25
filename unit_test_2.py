#!/usr/bin/python3
import unittest
from palindrome import f


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(f("-1"), True)

    def testCase2(self):
        self.assertEqual(f("2.5"), True)


if __name__ == '__main__':
    unittest.main()
