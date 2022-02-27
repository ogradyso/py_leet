#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:21:28 2022

@author: shauno
"""

import unittest

class Solution:
    def decompress(self, s):
        char_stack = []
        num_stack = []
        n = 0
        rep_str = []
        for char in s:
            if char.isdigit():
                n = n * 10 + int(char)
            elif char.isalpha():
                rep_str.append(char)
            elif char == "[":
                num_stack.append(n)
                char_stack.append(rep_str)
                n = 0
                rep_str = []
            elif char == "]":
                char_stack[-1].extend(rep_str * num_stack.pop())
                rep_str = char_stack.pop()
        return "".join(rep_str)
                            
            
class TestMethods(unittest.TestCase):

    def test_isMatch_ex1(self):
        inputs = "3[a2[abc]]"
        output = "aabcabcaabcabcaabcabc"
        mySolution = Solution()
        self.assertEqual(mySolution.decompress(inputs), output)
    
    def test_isMatch_ex2(self):
        inputs = "3[abc]4[ab]c"
        output = "abcabcabcababababc"
        mySolution = Solution()
        self.assertEqual(mySolution.decompress(inputs), output)
        
    def test_isMatch_ex3(self):
        inputs = "10[a]"
        output = "aaaaaaaaaa"
        mySolution = Solution()
        self.assertEqual(mySolution.decompress(inputs), output)
        
    def test_isMatch_ex4(self):
        inputs = "2[3[a]b]"
        output = "aaabaaab"
        mySolution = Solution()
        self.assertEqual(mySolution.decompress(inputs), output)
        
    def test_isMatch_ex5(self):
        inputs = "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
        output = "xx"
        mySolution = Solution()
        self.assertEqual(mySolution.decompress(inputs), output)
    
    def test_isMatch_ex6(self):
        inputs = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
        output = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
        mySolution = Solution()
        self.assertEqual(mySolution.decompress(inputs), output)

if __name__ == '__main__':
    unittest.main()
    