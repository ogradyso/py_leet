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
 

# class Solution(object):
#     def longestPalindrome(self, s):
#         T = '#'.join('^{}$'.format(s))
#         P = [0] * len(T)
#         C = 0
#         R = 0
#         for i in range(1,len(T)-1):
#             P[i] = (R>i) and min(R -i, P[2*C - i])
#             while (T[i+1+P[i]] == T[i-1-P[i]]):
#                 P[i]+=1
            
#             if(i+P[i] > R):
#                 C=i
#                 R=i+P[i]
        
#         mid_index = (P.index(max(P))//2) -1
#         if max(P) % 2 == 0:
#             start_index = mid_index - (max(P)//2) + 1
#         else:
#             start_index = mid_index - (max(P)//2)
#         stop_index = mid_index + (max(P)//2) + 1
#         return s[start_index:stop_index]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    result = s[left:right+1]
                    resLen = right - left +1
                left -= 1
                right += 1
                
            #even length
            left,right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right -left + 1) > resLen:
                    result = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
                
        return result

        
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