# -*- coding: utf-8 -*-
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

import unittest
from typing import List




            

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
