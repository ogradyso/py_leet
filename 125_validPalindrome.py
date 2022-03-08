# -*- coding: utf-8 -*-
"""
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all 
on-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false 
otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing 
non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is 
a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

import unittest
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord("A") <= ord(c) <= ord("Z") or
                   ord("0") <= ord(c) <= ord("9") or
                   ord("a") <= ord(c) <= ord("z"))
        
        left, right = 0, len(s) -1
        while left < right:
            while left < right and not alphaNum(s[left]):
                left += 1
            while right > left and not alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
        

class TestMethods(unittest.TestCase):

    def test_canAttendMeetings_ex1(self):
        
        inputs = [Interval(0,30),Interval(5,10),Interval(15,20)]
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)
        
    def test_canAttendMeetings_ex2(self):
        inputs = [Interval(7,10),Interval(2,4)]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)
        
    def test_canAttendMeetings_ex3(self):
        inputs = [Interval(1,2),Interval(2,4)]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)

if __name__ == '__main__':
    unittest.main()