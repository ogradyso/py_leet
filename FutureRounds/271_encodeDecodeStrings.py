# -*- coding: utf-8 -*-
"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""

import unittest
from typing import List




class TestMethods(unittest.TestCase):

    def test_encode_ex1(self):
        inputs = ["lint","code","love","you"]
        output = ["lint","code","love","you"]
        mySolution = Solution()
        self.assertEqual(mySolution.decode(mySolution.encode(inputs)), output)
    
    def test_encode_ex2(self):
        inputs = ["we", "say", ":", "yes"]
        output = ["we", "say", ":", "yes"]
        mySolution = Solution()
        self.assertEqual(mySolution.decode(mySolution.encode(inputs)), output)
    
    
if __name__ == '__main__':
    unittest.main()
