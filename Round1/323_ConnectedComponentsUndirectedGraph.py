# -*- coding: utf-8 -*-
"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to find the number of 
connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all 
edges are undirected, [0, 1] is the same as [1, 0] and thus will not 
appear together in edges.
"""

import unittest
from typing import List

# DFS solution:
# class Solution:
#     def connectedComponents(self, n: int, edges: List[List[int]]) -> int:
#         adj = {i:[] for i in range(n)}
#         for i,j in edges:
#             adj[i].append(j)
#             adj[j].append(i)
            
#         visited = set()
#         cmp_count = 0
        
#         def dfs(node):
#             if node in visited:
#                 return
#             visited.add(node)
#             for nei in adj[node]:
#                 dfs(nei)

#         for i in range(n):
#             if i not in visited:
#                 cmp_count += 1
#                 dfs(i)
#         return cmp_count

# Union Find solution:
class Solution:
    def connectedComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)] 
        rank = [1] * n
    	
        def find(n1):
            res = n1
            while res != par[res]: 
                par[res] = par[par[res]] 
                res = par[res]
            return res
    	
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:  
                return 0
            if rank[p2] > rank[p1]:
                par[p1]=p2
                rank[p2] += rank[p1]
            else:
                par[p2]=p1
                rank[p1] += rank[p2]
            return 1
    	
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

            

class TestMethods(unittest.TestCase):

    def test_connectedComponents_ex1(self):
        inputs = [[0, 1], [1, 2], [3, 4]]
        num = 5
        output = 2
        mySolution = Solution()
        self.assertEqual(mySolution.connectedComponents(num, inputs), output)
        
    def test_connectedComponents_ex2(self):
        inputs = [[0, 1], [1, 2], [2, 3], [3, 4]]
        num = 5
        output = 1
        mySolution = Solution()
        self.assertEqual(mySolution.connectedComponents(num, inputs), output)
        
    

if __name__ == '__main__':
    unittest.main()