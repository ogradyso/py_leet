# -*- coding: utf-8 -*-
"""

"""

import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren_char in s:
            if len(stack) == 0:
                if paren_char in ['(','[','{']:
                    stack.append(paren_char)
                else:
                    return False
            else:
                last_char = stack.pop()
                if last_char == '(':
                    if paren_char not in [')','(','{','[']:
                         return False
                    elif paren_char in ['[','{','(']:
                        stack.append(last_char)
                        stack.append(paren_char)
                elif last_char == '[':
                     if paren_char not in [']','[','{','(']:
                        return False
                     elif paren_char in ['[','{','(']:
                        stack.append(last_char)
                        stack.append(paren_char)
                elif last_char == '{' :
                     if paren_char not in ['}','{','[','(']:
                        return False
                     elif paren_char in ['[','{','(']:
                        stack.append(last_char)
                        stack.append(paren_char)
        if len(stack) != 0:
            return False
        else:
            return True

        
        

        
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
    