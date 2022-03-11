# -*- coding: utf-8 -*-
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

import unittest
from typing import List
 

class TestStringMethods(unittest.TestCase):

    def test_fourSum_ex1(self):
        nums = [1,0,-1,0,-2,2]
        target=0
        output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        mySolution = Solution()
        self.assertEqual(mySolution.fourSum(nums, target), output)
    
    def test_fourSum_ex2(self):
        nums = [2,2,2,2,2]
        target=8
        output = [[2,2,2,2]]
        mySolution = Solution()
        self.assertEqual(mySolution.fourSum(nums, target), output)
        

if __name__ == '__main__':
    
    unittest.main()
    
