# -*- coding: utf-8 -*-
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

import unittest
from typing import List

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0],height[1]) * 1
        left_pointer = 0
        right_pointer = len(height)-1
        min_height = min(height[left_pointer], height[right_pointer])
        max_area = min_height * (right_pointer - left_pointer)
        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
            min_height = min(height[left_pointer], height[right_pointer])
            max_area = max(max_area, min_height * (right_pointer - left_pointer))
        return max_area

        
class TestStringMethods(unittest.TestCase):

    def test_isMatch_ex1(self):
        inputs = [1,8,6,2,5,4,8,3,7]
        output = 49
        mySolution = Solution()
        self.assertEqual(mySolution.maxArea(inputs), output)
        
    def test_isMatch_ex2(self):
        inputs = [1,1]
        output = 1
        mySolution = Solution()
        self.assertEqual(mySolution.maxArea(inputs), output)
        
    def test_isMatch_ex3(self):
        inputs = [1,104,1,1,1]
        output = 4
        mySolution = Solution()
        self.assertEqual(mySolution.maxArea(inputs), output)
        
    def test_isMatch_ex4(self):
         inputs = [1,2]
         output = 1
         mySolution = Solution()
         self.assertEqual(mySolution.maxArea(inputs), output)
    

if __name__ == '__main__':
    unittest.main()
    