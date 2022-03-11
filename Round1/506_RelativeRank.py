# -*- coding: utf-8 -*-
"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

 

Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
"""

import unittest
from typing import List


# from heapq import heapify, heappush, heappop

# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         place_names = ['Bronze Medal', 'Silver Medal','Gold Medal']
#         place_val = 4
#         heap = []
#         index_dict = {}
#         heapify(heap)
#         # O(n)
#         for score_i,score_val in enumerate(score):
#             heappush(heap, -1 * score_val)
#             index_dict[score_val] = score_i

#         # O(n)
#         while heap:
#             max_val = -1 * heappop(heap)
#             if not place_names:
#                 score[index_dict[max_val]] = str(place_val)
#                 place_val += 1
#             else:
#                 score[index_dict[max_val]] = place_names.pop()

#         return score


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def heappush(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify((self.size-1)//2,True)
        
    def swap(self, parent_i, child_i):
        self.heap[parent_i], self.heap[child_i] = (self.heap[child_i], self.heap[parent_i])
        
    def heapify(self, index, direction):
        if self.size > (2* index)+1:
            if self.heap[index] < self.heap[(2* index)+1]:
                self.swap(index,(2*index)+1)
                if not direction: 
                    self.heapify((2*index)+1,False)
        if self.size > (2* index)+2:
            if self.heap[index] < self.heap[(2* index)+2]:
                self.swap(index,(2*index)+2)
                if not direction: 
                    self.heapify((2*index)+2,False)
        if direction:
            if index == 0:
                return
            self.heapify(index//2,True)
        else:
            return
        
        
    def heappop(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0,False)
        return popped


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        place_names = ["Bronze Medal", "Silver Medal", "Gold Medal"]
        place_val = 4
        heap_scores = MaxHeap()
        score_i_dict = {}
        for score_i,score_val in enumerate(score):
            heap_scores.heappush(score_val)
            score_i_dict[score_val] = score_i
        for i in range(len(score)):
            next_max = heap_scores.heappop()
            max_i = score_i_dict[next_max]
            if place_names:
                score[max_i] = place_names.pop()
            else:
                score[max_i] = str(place_val)
                place_val += 1
        return score

        

        
class TestMethods(unittest.TestCase):

    def test_findRelativeRanks_ex1(self):
        inputs = [5,4,3,2,1]
        output = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        mySolution = Solution()
        self.assertEqual(mySolution.findRelativeRanks(inputs), output)
        
    def test_findRelativeRanks_ex2(self):
        inputs = [10,3,8,9,4]
        output = ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
        mySolution = Solution()
        self.assertEqual(mySolution.findRelativeRanks(inputs), output)

        

if __name__ == '__main__':
    unittest.main()
    