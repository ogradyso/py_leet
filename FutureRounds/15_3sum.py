# -*- coding: utf-8 -*-
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

import unittest
from typing import List
 


        
class TestMethods(unittest.TestCase):

    def test_3Sum_ex1(self):
        nums = [1,0,-1,0,-2,2]
        target=0
        output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        mySolution = Solution()
        self.assertEqual(mySolution.fourSum(nums, target), output)
    
    def test_3Sum_ex2(self):
        nums = [2,2,2,2,2]
        target=0
        output = [[2,2,2,2]]
        mySolution = Solution()
        self.assertEqual(mySolution.fourSum(nums, target), output)
        

if __name__ == '__main__':
    
    unittest.main()
    
