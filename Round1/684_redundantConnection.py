# -*- coding: utf-8 -*-
"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
 
"""

import unittest
from typing import List
import collections

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            if source not in visited:
                visited.add(source)
                if source == target: return True
                return any(dfs(child,target) for child in graph[source])
        
        for parent, child in edges:
            visited = set()
            if parent in graph and child in graph and dfs(parent, child):
                return [parent, child]
            graph[parent].add(child)
            graph[child].add(parent)


class TestMethods(unittest.TestCase):

    def test_findRedundantConnection_ex1(self):
        inputs = [[1,2],[1,3],[2,3]]
        output = [2,3]
        mySolution = Solution()
        self.assertEqual(mySolution.findRedundantConnection(inputs), output)
        
    def test_findRedundantConnection_ex2(self):
        inputs = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        output = [1,4]
        mySolution = Solution()
        self.assertEqual(mySolution.findRedundantConnection(inputs), output)
        

if __name__ == '__main__':
    unittest.main()
    