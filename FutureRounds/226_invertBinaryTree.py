# -*- coding: utf-8 -*-
"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
"""

import unittest



class TestMethods(unittest.TestCase):

    def test_isMatch_ex1(self):
        inputs = 3
        output = "III"
        mySolution = Solution()
        self.assertEqual(mySolution.intToRoman(inputs), output)
        
    def test_isMatch_ex2(self):
        inputs = 58
        output = "LVIII"
        mySolution = Solution()
        self.assertEqual(mySolution.intToRoman(inputs), output)
        
    def test_isMatch_ex3(self):
        inputs = 1994
        output = "MCMXCIV"
        mySolution = Solution()
        self.assertEqual(mySolution.intToRoman(inputs), output)

if __name__ == '__main__':
    unittest.main()
    
