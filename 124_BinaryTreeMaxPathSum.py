# -*- coding: utf-8 -*-
"""
A path in a binary tree is a sequence of nodes where each 
pair of adjacent nodes in the sequence has an edge 
connecting them. A node can only appear in the sequence 
at most once. Note that the path does not need to pass 
through the root.

The path sum of a path is the sum of the node's values in 
the path.

Given the root of a binary tree, return the maximum path 
sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path 
sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path 
sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range 
[1, 3 * 104].
-1000 <= Node.val <= 1000
 
"""

import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #placing the root val into a list helps make it easier to modify from the recursive function
        res = [root.val]
        
        #basecase
        def dfs(root):
            if not root:
                    return 0
            leftMax= dfs(root.left)
            rightMax = dfs(root.right)
            # set to 0 in the case of negatives:
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute max path sum with a split:
            res[0] = max(res[0],root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
        


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
    