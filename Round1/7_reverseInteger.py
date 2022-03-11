# -*- coding: utf-8 -*-
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

import unittest
 

class Solution(object):
    def reverse(self, x: int) -> int:
        if (x == None): 
            return None
        elif (x == 0 or x < -2**31 or x > (2**31)):
            return 0
        else:
            polarity = x > 0 
            if polarity:
                numFrom = str(x)
                new_x = int(numFrom[::-1])
                if (new_x > (2**31)-1):
                    return 0
                else:
                    return int(numFrom[::-1])
            else:
                numFrom = str(x)[1:]
                new_x = int(numFrom[::-1]) * -1
                if (new_x < (-2**31)):
                    return 0
                else:
                    return int(numFrom[::-1]) * -1
            

        
class TestStringMethods(unittest.TestCase):

    def test_reverse_ex1(self):
        x = 321
        output = 123
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
        
    def test_reverse_ex2(self):
        x = -321
        output = -123
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
        
    def test_reverse_ex3(self):
        x = 120
        output = 21
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
        
    def test_reverse_empty(self):
        x = 0
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
        
    def test_reverse_empty2(self):
        x = None
        output = None
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
        
    def test_reverse_same(self):
        x = 1111
        output = 1111
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
    
    def test_reverse_pattern(self):
        x = 202020
        output = 20202
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)
        
    def test_reverse_overflow(self):
        x = (2**31) + 1
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)   
        
    def test_reverse_overflow2(self):
        x = (-2**31) -1
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)  
        
    def test_reverse_overflow3(self):
        x = 1534236469
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.reverse(x), output)  

if __name__ == '__main__':
    unittest.main()
    