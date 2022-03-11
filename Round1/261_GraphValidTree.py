# -*- coding: utf-8 -*-
"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
"""

import unittest
from typing import List


class Solution:
    def graphValidTree(self, n: int, edges: List[List[int]]) -> bool:
    	if not n:
    		return True
    	adj = {i:[] for i in range(n)}
    	for (parent, child) in edges:
    		adj[parent].append(child)
    		adj[child].append(parent)
    	
    	visit = set()
    	def dfs(i, prev):
    		if i in visit:
    			return False
    		visit.add(i)
    		for nei in adj[i]:
    			if nei == prev:
    				continue
    			if not dfs(nei,i):
    				return False
    		return True
    	return dfs(0,-1) and n == len(visit)


            

class TestMethods(unittest.TestCase):

    def test_graphValidTree_ex1(self):
        num = 5
        inputs = [[0,1], [0,2], [0,3], [1,4]]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.graphValidTree(num, inputs), output)
        
    def test_graphValidTree_ex2(self):
        num = 5
        inputs = [[0,1], [1,2], [2,3], [1,3], [1,4]]
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.graphValidTree(num, inputs), output)

    

if __name__ == '__main__':
    unittest.main()