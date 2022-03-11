# -*- coding: utf-8 -*-
"""
Given an m x n board of characters and a list of strings words, 
return all words on the board.

Each word must be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used 
more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],
                ["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
 
"""

import unittest

class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS = len(board)
        COLS = len(board[0])
        res= []
        
        def dfs(r,c, node, word):
            if (r < 0 or c < 0 or c== COLS or r == ROWS or board[r][c] not in node.children):
                return
            
            
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.append(word)
                node.word = None
                
            placeHolder = board[r][c]
            board[r][c] = 0
            dfs(r-1,c, node, word)
            dfs(r+1,c, node, word)
            dfs(r,c-1, node, word)
            dfs(r,c+1, node, word)
            board[r][c] = placeHolder

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
                
        return list(res)


class TestMethods(unittest.TestCase):

    def test_isMatch_ex1(self):
        inputs = 3
        output = "III"
        mySolution = Solution()
        self.assertEqual(mySolution.intToRoman(inputs), output)
        
    def test_isMatch_ex2(self):
        inputs = 58
        output = "LVIII"
        mySolution = Solution()
        self.assertEqual(mySolution.intToRoman(inputs), output)
        
    def test_isMatch_ex3(self):
        inputs = 1994
        output = "MCMXCIV"
        mySolution = Solution()
        self.assertEqual(mySolution.intToRoman(inputs), output)

if __name__ == '__main__':
    unittest.main()
    