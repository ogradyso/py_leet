# -*- coding: utf-8 -*-
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Example 3: 
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
 
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
    
