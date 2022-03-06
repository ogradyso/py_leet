# -*- coding: utf-8 -*-
"""
Easy
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
Example 1:
Input:
[[0,30],[5,10],[15,20]]
Output:
 false
Example 2:
Input:
 [[7,10],[2,4]]

Output:
 true

"""
class Interval(object):
    def __init__(self,start, end):
        self.start = start
        self.end = end

import unittest
from typing import List


class Solution:
    def canAttendMeetings(self, intervals:List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end >  i2.start:
                return False
        return True

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