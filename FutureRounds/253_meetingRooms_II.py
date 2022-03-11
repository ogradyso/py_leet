# -*- coding: utf-8 -*-
"""
Description
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference 
rooms required.

(0,8),(8,10) is not conflict at 8

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""



class TestMethods(unittest.TestCase):

    def test_minMeetingRooms_ex1(self):
        inputs = [Interval(0,8),Interval(8,10)]
        output = 1
        mySolution = Solution()
        self.assertEqual(mySolution.minMeetingRooms(inputs), output)
        
    def test_minMeetingRooms_ex2(self):
        inputs = [Interval(0,30),Interval(5,10),Interval(15,20)]
        output = 2
        mySolution = Solution()
        self.assertEqual(mySolution.minMeetingRooms(inputs), output)
        
    def test_minMeetingRooms_ex3(self):
        inputs = [Interval(2,7)]
        output = 1
        mySolution = Solution()
        self.assertEqual(mySolution.minMeetingRooms(inputs), output)

if __name__ == '__main__':
    unittest.main()
