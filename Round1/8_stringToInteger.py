# -*- coding: utf-8 -*-
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change 
the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

"""

import unittest
 

class Solution(object):
    def myAtoi(self, s: str) -> int:
        polarity = 1
        target_integer = 0
        char_cursor = 0
        while char_cursor < len(s) and s[char_cursor] == " ":
            char_cursor += 1
        if char_cursor < len(s) and s[char_cursor] == "+":
            polarity = 1
            char_cursor += 1
        elif char_cursor < len(s) and s[char_cursor] == "-":
            polarity = -1
            char_cursor += 1
        while char_cursor < len(s) and s[char_cursor].isdigit():
            digit = int(s[char_cursor])
            if ((target_integer > (2**31)-1) or (target_integer < (-2**31))):
                return (2**31)-1 if polarity == 1 else (-2**31)
            target_integer = 10 * target_integer + digit
            char_cursor += 1
        if ((target_integer > (2**31)-1) or (target_integer < (-2**31))):
            return (2**31)-1 if polarity == 1 else (-2**31)
        return polarity * target_integer
        
class TestStringMethods(unittest.TestCase):

    def test_myAtoi_ex1(self):
        input_string = "42"
        output = 42
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
    
    def test_myAtoi_ex2(self):
       input_string = "-42"
       output = -42
       mySolution = Solution()
       self.assertEqual(mySolution.myAtoi(input_string), output)
       
    def test_myAtoi_ex3(self):
        input_string = "4193 with words"
        output = 4193
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
        
    def test_myAtoi_middle(self):
        input_string = "this -4193 with words"
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
    
    def test_myAtoi_end(self):
        input_string = "this is my +4193"
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
                         
    def test_myAtoi_separated(self):
        input_string = "this 12.174 is my"
        output = 0
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
                         
    def test_myAtoi_leading(self):
        input_string = "     12.174 is my"
        output =12
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
                         
    def test_myAtoi_maxBefore(self):
        input_string = "  2147483648 is my"
        output = 2147483647
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
                         
    def test_myAtoi_min(self):
        input_string = "  -2147483649 is my"
        output = -2147483648
        mySolution = Solution()
        self.assertEqual(mySolution.myAtoi(input_string), output)
                         
    def test_myAtoi_empty(self):
       input_string = ""
       output = 0
       mySolution = Solution()
       self.assertEqual(mySolution.myAtoi(input_string), output)
       
    def test_myAtoi_noNum(self):
       input_string = "this is my string, there are many like it but this one is mine"
       output = 0
       mySolution = Solution()
       self.assertEqual(mySolution.myAtoi(input_string), output)
    
    def test_myAtoi_afterString(self):
       input_string = "words and 987"
       output = 0
       mySolution = Solution()
       self.assertEqual(mySolution.myAtoi(input_string), output)
       
    def test_myAtoi_period(self):
       input_string = ".1"
       output = 0
       mySolution = Solution()
       self.assertEqual(mySolution.myAtoi(input_string), output)
       
    def test_myAtoi_plusMinus(self):
       input_string = "+-12"
       output = 0
       mySolution = Solution()
       self.assertEqual(mySolution.myAtoi(input_string), output)

if __name__ == '__main__':
    unittest.main()
    