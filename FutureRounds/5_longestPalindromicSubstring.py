# -*- coding: utf-8 -*-
"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

import unittest
 



        
class TestStringMethods(unittest.TestCase):

    def test_longestPalindrome_ex1(self):
        s = "babad"
        output = "bab"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_ex2(self):
        s = "racecar"
        output = "racecar"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_ex3(self):
        s = "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"
        output = "jtdtj"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_longestSingleWord(self):
        s = "saippuakivikauppias"
        output = "saippuakivikauppias"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_middleUneven(self):
        s = "saippu11111111111111111111ikauppias"
        output = "11111111111111111111"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_middleLeft(self):
        s = "sai11111111111111111111fjkldskjenfldskjfldikauppias"
        output = "11111111111111111111"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_middleRight(self):
        s = "fjkldskjenfldskjfldikaupp11111111111111111111sai"
        output = "11111111111111111111"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_single(self):
        s = "1"
        output = "1"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_end(self):
        s = "1bigassracecar"
        output = "racecar"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_beginning(self):
        s = "racecarsgofast"
        output = "racecar"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)
        
    def test_longestPalindrome_multi(self):
        s = "racecarsracecarsracecars"
        output = "racecarsracecarsracecar"
        mySolution = Solution()
        self.assertEqual(mySolution.longestPalindrome(s), output)

if __name__ == '__main__':
    unittest.main()
