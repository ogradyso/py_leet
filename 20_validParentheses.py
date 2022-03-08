# -*- coding: utf-8 -*-
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

import unittest

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for paren_char in s:
#             if len(stack) == 0:
#                 if paren_char in ['(','[','{']:
#                     stack.append(paren_char)
#                 else:
#                     return False
#             else:
#                 last_char = stack.pop()
#                 if last_char == '(':
#                     if paren_char not in [')','(','{','[']:
#                          return False
#                     elif paren_char in ['[','{','(']:
#                         stack.append(last_char)
#                         stack.append(paren_char)
#                 elif last_char == '[':
#                      if paren_char not in [']','[','{','(']:
#                         return False
#                      elif paren_char in ['[','{','(']:
#                         stack.append(last_char)
#                         stack.append(paren_char)
#                 elif last_char == '{' :
#                      if paren_char not in ['}','{','[','(']:
#                         return False
#                      elif paren_char in ['[','{','(']:
#                         stack.append(last_char)
#                         stack.append(paren_char)
#         if len(stack) != 0:
#             return False
#         else:
#             return True

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                    stack.append(c)
        return True if not stack else False
        
class TestStringMethods(unittest.TestCase):

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
    