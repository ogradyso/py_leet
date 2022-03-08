# -*- coding: utf-8 -*-
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 
Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

import unittest
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
            
        have, need = 0, len(countT)
        result, resLen = [-1,-1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c,0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:
                # update our result
                if (right - left + 1) < resLen:
                    result = [left, right]
                    resLen = (right - left + 1)
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left,right = result
        return s[left:right+1] if resLen != float("infinity") else ""

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