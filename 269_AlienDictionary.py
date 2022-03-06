# -*- coding: utf-8 -*-
"""
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:  

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: "cab"

Input words = ["wrt", "wrf", "er", "ett", "rftt"]
output "wertf"

"""

import unittest
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
    	adj = {c:set() for w in words for c in w}
    	
    	for i in range(len(words) -1):
    		w1, w2 = words[i], words[i+1]
    		minLen = min(len(w1), len(w2))
    		if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
    			return ""
    		for j in range(minLen):
    			if w1[j] != w2[j]:
    				adj[w1[j]].add(w2[j])
    				break
    
    	visit = {}  # false = visited, True =current path
    	res = []
    
    	def dfs(c):
    		if c in visit:
    			return visit[c]
    		visit[c] = True
    		
    		for nei in adj[c]:
    			if dfs(nei):
    				return True
    
    		visit[c] = False
    		res.append(c)
    
    	for c in adj:
    		if dfs(c):
    			return ""
    	res.reverse()
    	return "".join(res)
            

class TestMethods(unittest.TestCase):

    def test_alienOrder_ex1(self):
        inputs = ["wrt", "wrf", "er", "ett", "rftt"]
        output = "wertf"
        mySolution = Solution()
        self.assertEqual(mySolution.alienOrder(inputs), output)
        
    def test_alienOrder_ex2(self):
        inputs = ["wrt", "wrf", "wr", "ett", "rftt"]
        output = ""
        mySolution = Solution()
        self.assertEqual(mySolution.alienOrder(inputs), output)
        

if __name__ == '__main__':
    unittest.main()