#!/usr/bin/python3
import unittest
from palindrome import checkPalindrome


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(checkPalindrome("-1"), True)

    def testCase2(self):
        self.assertEqual(checkPalindrome("2.5"), True)


if __name__ == '__main__':
    unittest.main()