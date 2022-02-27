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
 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []
            # base case:
            if not nums:
                return result
            #return current results if min and max of list
            # are greater/less than avg_val:
            avg_val = target // k
            if avg_val < nums[0] or nums[-1] < avg_val:
                return result
            if k == 2:
                return twoSum(nums, target)
            
            for num_iterator in range(len(nums)):
                if num_iterator == 0 or nums[num_iterator-1] != nums[num_iterator]:
                    for subset in kSum(nums[num_iterator+1:], target - nums[num_iterator], k-1):
                        result.append([nums[num_iterator]]+subset)
                        
            return result
        
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            s = set()
            for num_iterator in range(len(nums)):
                if len(result) == 0 or result[-1][1] != nums[num_iterator]:
                    if target - nums[num_iterator] in s:
                        result.append([target - nums[num_iterator], nums[num_iterator]])
                s.add(nums[num_iterator])
                
            return result
        
        nums.sort()
        return kSum(nums, 0, 3)
        
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
    