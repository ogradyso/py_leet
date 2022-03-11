# -*- coding: utf-8 -*-
"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""

import unittest
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]

            

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