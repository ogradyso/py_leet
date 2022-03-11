# -*- coding: utf-8 -*-
"""
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:  

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: "cab"

Input words = ["wrt", "wrf", "er", "ett", "rftt"]
output "wertf"

"""

import unittest
from typing import List



class TestMethods(unittest.TestCase):

    def test_alienOrder_ex1(self):
        inputs = ["wrt", "wrf", "er", "ett", "rftt"]
        output = "wertf"
        mySolution = Solution()
        self.assertEqual(mySolution.alienOrder(inputs), output)
        
    def test_alienOrder_ex2(self):
        inputs = ["wrt", "wrf", "wr", "ett", "rftt"]
        output = ""
        mySolution = Solution()
        self.assertEqual(mySolution.alienOrder(inputs), output)
        

if __name__ == '__main__':
    unittest.main()
