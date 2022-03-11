# -*- coding: utf-8 -*-
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""


import unittest
from typing import List



class TestMethods(unittest.TestCase):

    def test_canAttendMeetings_ex1(self):
        
        inputs = [Interval(0,30),Interval(5,10),Interval(15,20)]
        output = False
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)
        
    def test_canAttendMeetings_ex2(self):
        inputs = [Interval(7,10),Interval(2,4)]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)
        
    def test_canAttendMeetings_ex3(self):
        inputs = [Interval(1,2),Interval(2,4)]
        output = True
        mySolution = Solution()
        self.assertEqual(mySolution.canAttendMeetings(inputs), output)

if __name__ == '__main__':
    unittest.main()
