#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:21:28 2022

@author: shauno
"""

import unittest


                            
            
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
    
