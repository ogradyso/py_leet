# -*- coding: utf-8 -*-
"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
import unittest



        


class TestStringMethods(unittest.TestCase):

    def test_lengthOfLongestSubstring_ex1(self):
        input_string = "abcabcbb"
        output_num = 3
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_ex2(self):
        input_string = "bbbbb"
        output_num = 1
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_ex3(self):
        input_string = "pwwkew"
        output_num = 3
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
    
    def test_lengthOfLongestSubstring_ex4(self):
        input_string = "dvdf"
        output_num = 3
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_ex5(self):
        input_string = "dvdfed"
        output_num = 4
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_ex6(self):
        input_string = "dvdfedjk"
        output_num = 5
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_end(self):
        input_string = "pssste"
        output_num = 3
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_full(self):
        input_string = "01_32!"
        output_num = 6
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_empty(self):
        input_string = ""
        output_num = 0
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_long(self):
        input_string = "5555555555555555555555555855555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
        output_num = 2
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_single(self):
        input_string = "1"
        output_num = 1
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_doubleOne(self):
        input_string = "11"
        output_num = 1
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_wholeStringShort(self):
        input_string = "101"
        output_num = 2
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
        
    def test_lengthOfLongestSubstring_wholeStringLong(self):
        input_string = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
        output_num = 46
        mySolution = Solution()
        self.assertEqual(mySolution.lengthOfLongestSubstring(input_string), output_num)
    

if __name__ == '__main__':
    unittest.main()
