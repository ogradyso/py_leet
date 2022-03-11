# -*- coding: utf-8 -*-
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

import unittest
from typing import List
#solution optimized for time and space: runtime: O(n) space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        current = 1
        for i in range(1,len(nums)):
            current *= nums[i-1]
            output[i] = current
        current = 1
        for j in range(len(nums) -2, -1, -1):
            current *= nums[j+1]
            output[j] *= current
        return output

# Brute force: runtime: O(n) space: O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left = [0] * len(nums)
#         right = [0] * len(nums)
#         prod = [0] * len(nums)
#         left[0] = 1
#         right[len(nums)-1] = 1
#         for i in range(1,len(nums)):
#             left[i] = nums[i-1] * left[i-1]
#         for j in range(len(nums)-2, -1, -1):
#             right[j] = nums[j + 1] * right[j+1]
#         for i in range(len(nums)):
#             prod[i] = left[i] * right[i]
#         return prod

            

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