# -*- coding: utf-8 -*-
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

import unittest
from typing import List



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
