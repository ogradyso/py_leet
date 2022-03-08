# -*- coding: utf-8 -*-
"""
You are given a string s and an integer k. You can choose any character of 
the string and change it to any other uppercase English character. You can 
perform this operation at most k times.

Return the length of the longest substring containing the same letter you 
can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 
Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

import unittest
from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_count = {}
        res = 0
        
        for right in range(len(s)):
            char_count[s[right]] = 1 + char_count.get(s[right],0)
            while (right - left + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1
            res =max(res, right - left + 1)
        return res

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