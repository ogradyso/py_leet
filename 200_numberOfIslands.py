# -*- coding: utf-8 -*-
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc, in directions:
                    r,c = row + dr,  col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

            

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