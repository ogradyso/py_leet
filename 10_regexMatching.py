# -*- coding: utf-8 -*-
"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

import unittest
 

class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        mem_store = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        mem_store[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    mem_store[i][j] = mem_store[i][j+2] or first_match and mem_store[i+1][j]
                else:
                    mem_store[i][j] = first_match and mem_store[i+1][j+1]

        return mem_store[0][0]
        
class TestStringMethods(unittest.TestCase):

    def test_isMatch_ex1(self):
        inputString = "aa"
        inputPattern = "a"
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
        
    def test_isMatch_ex2(self):
        inputString = "aa"
        inputPattern = "a*"
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
        
    def test_isMatch_ex3(self):
        inputString = "ab"
        inputPattern = ".*"
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
        
    def test_isMatch_multiple(self):
        inputString = "aaabbbc"
        inputPattern = "a*b*c"
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
        
    def test_isMatch_middle(self):
        inputString = "abc"
        inputPattern = "a.c"
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
        
    def test_isMatch_middleMatch(self):
        inputString = "abc"
        inputPattern = ".b."
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
        
    def test_isMatch_multiStar(self):
        inputString = "aaa"
        inputPattern = "a**"
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
    
    def test_isMatch_multiStarFalse(self):
        inputString = "abc"
        inputPattern = "a**"
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.isMatch(inputString,inputPattern), output)
    

if __name__ == '__main__':
    unittest.main()
    