# -*- coding: utf-8 -*-
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

0     6      12
1   5 7   11 13
2 4   8 10
3     9

0   8       16
1  79     15
2 6 10  14
35  1113
4   12

0    10        20        30
1   911      1921      29
2  8 12    18  22    28
3 7  13  17    23  27
46   1416      2426
5    15        25

n*(2*targ)                 n*(2*targ)   n*(2*targ)
n+(n-1)     n+(n-1)  
n-(n-2) n+(n-2)
n-(n-n)

Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

import unittest
 


        
class TestStringMethods(unittest.TestCase):

    def test_convert_ex1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        output = "PAHNAPLSIIGYIR"
        mySolution = Solution()
        self.assertEqual(mySolution.convert(s, num_rows), output)
        
    def test_convert_ex2(self):
        s = "PAYPALISHIRING"
        num_rows = 4
        output = "PINALSIGYAHRPI"
        mySolution = Solution()
        self.assertEqual(mySolution.convert(s, num_rows), output)
        
    def test_convert_ex3(self):
        s = "A"
        num_rows = 1
        output = "A"
        mySolution = Solution()
        self.assertEqual(mySolution.convert(s, num_rows), output)
        
    def test_convert_maxRows(self):
        s = "PAYPALISHIRING"
        num_rows = 1000
        output = "PAYPALISHIRING"
        mySolution = Solution()
        self.assertEqual(mySolution.convert(s, num_rows), output)
        
    def test_convert_manyRowsLongString(self):
        s = "Threedifferentearlyversionsoftheplayareextant"
        num_rows = 5
        output = "Tfropxhfealineletrireysshaeaedetvrotyrnenefat"
        mySolution = Solution()
        self.assertEqual(mySolution.convert(s, num_rows), output)

if __name__ == '__main__':
    unittest.main()
    
