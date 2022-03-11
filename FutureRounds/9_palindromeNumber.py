# -*- coding: utf-8 -*-
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
Accepted
1,851,900
Submissions
3,552,483
"""

import unittest
 


        
class TestStringMethods(unittest.TestCase):

    def test_isPalindrome_ex1(self):
        inputVal = 121
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_ex2(self):
        inputVal = -121
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_ex3(self):
        inputVal = 10
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_sameNumber(self):
        inputVal = 1111
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_samePattern(self):
        inputVal = 202020
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_oddNumber(self):
        inputVal = 32123
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)

    def test_isPalindrome_evenNumber(self):
        inputVal = 321123
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_evenNumber2(self):
        inputVal = 320023
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_underflow(self):
        inputVal = (-2**31) -1
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)
    
    def test_isPalindrome_overflow(self):
        inputVal = (2**31) -1
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isPalindrome(inputVal), output)

if __name__ == '__main__':
    unittest.main()
    
