# -*- coding: utf-8 -*-
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

import unittest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1
                    

            

class TestMethods(unittest.TestCase):

    def test_search_ex1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        output = 4
        mySolution = Solution()
        self.assertEqual(mySolution.search(nums, target), output)
        
    def test_search_ex2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        output = -1
        mySolution = Solution()
        self.assertEqual(mySolution.search(nums, target), output)

if __name__ == '__main__':
    unittest.main()
