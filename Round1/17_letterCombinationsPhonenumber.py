# -*- coding: utf-8 -*-
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Ex
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
 
"""

import unittest

#Other possible solutions:
# Depth first search: use a stack or recursive
# Breadth first search: use a queue or recursive

# list comprehension (nested loops):
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        output_lists = ['']	
        num_dict = {"2":["a","b","c"],"3":["d","e","f"],
        "4":["g","h","i"],"5":["j","k","l"],
        "6":["m","n","o"],"7":["p","q","r","s"],
        "8":["t","u","v"],"9":["w","x","y","z"]}
        for digit in digits:
            output_lists = [prev + num_char for prev in output_lists for num_char in num_dict[digit]]
        return output_lists


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
    