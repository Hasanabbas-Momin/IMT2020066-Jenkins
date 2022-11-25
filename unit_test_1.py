#!/usr/bin/python3

import unittest
from palindrome import checkPalindrome


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(checkPalindrome("12321"), True)

    def testCase2(self):
        self.assertEqual(checkPalindrome("1212"), False)

    def testCase3(self):
        self.assertEqual(checkPalindrome("9"), True)


if __name__ == '__main__':
    unittest.main()