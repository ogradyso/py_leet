# -*- coding: utf-8 -*-
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

import unittest
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # get each value from the top row:
            for i in range(left, right):
                res.append(matix[top][i])
            top += 1
            # get each value from the right col:
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1
            #handles case: matrix is a sinle column or single row:
            if not (left < right and top < bottom):
                break
            # get each value from the bottom row:
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            # get each value in the left col:
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

class TestMethods(unittest.TestCase):

    def test_canAttendMeetings_ex1(self):
        
        inputs = [Interval(0,30),Interval(5,10),Interval(15,20)]
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)
        
    def test_canAttendMeetings_ex2(self):
        inputs = [Interval(7,10),Interval(2,4)]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)
        
    def test_canAttendMeetings_ex3(self):
        inputs = [Interval(1,2),Interval(2,4)]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)

if __name__ == '__main__':
    unittest.main()