# -*- coding: utf-8 -*-
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

import unittest
from typing import List
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         unique_val_dict = {}
#         for num_iterator in range(len(nums)):
#             difference = target - nums[num_iterator]
#             if nums[num_iterator] in unique_val_dict:
#                 return [unique_val_dict[nums[num_iterator]], num_iterator]
#             else:
#                 unique_val_dict[difference] = num_iterator
            
#         return []
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for index,num in enumerate(nums):
            difference = target-num
            if difference in diff_dict:
                return [diff_dict[difference],index]
            else:
                diff_dict[difference] = index
        return []
            

class TestMethods(unittest.TestCase):

    def test_twoSum_ex1(self):
        nums = [2,7,11,15]
        target = 9
        output = [0,1]
        mySolution = Solution()
        self.assertEqual(mySolution.twoSum(nums, target), output)
        
    def test_twoSum_ex2(self):
        nums = [3,2,4]
        target = 6
        output = [1,2]
        mySolution = Solution()
        self.assertEqual(mySolution.twoSum(nums, target), output)
        
    def test_twoSum_ex3(self):
        nums = [3,3]
        target = 6
        output = [0,1]
        mySolution = Solution()
        self.assertEqual(mySolution.twoSum(nums, target), output)

    def test_twoSum_emptyArray(self):
        nums = []
        target = 6
        output = []
        mySolution = Solution()
        self.assertEqual(mySolution.twoSum(nums, target), output)

    def test_twoSum_unsortedArray(self):
        nums = [9, 6, 109, 3, 1]
        target = 10
        output = [0,4]
        mySolution = Solution()
        self.assertEqual(mySolution.twoSum(nums, target), output)

    def test_twoSum_tgtNotFound(self):
        nums = [9, 6, 109, 3, 8]
        target = 10
        output = []
        mySolution = Solution()
        self.assertEqual(mySolution.twoSum(nums, target), output)
        
    

if __name__ == '__main__':
    unittest.main()