# -*- coding: utf-8 -*-
"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

import unittest
from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        unique_words = {}
        for word in words:
            if word in unique_words:
                unique_words[word] += 1
            else:
                unique_words[word] = 0
        heap = []
        for word in unique_words:
            heapq.heappush(heap, (-1 * unique_words[word], word))
            heapq.heapify(heap)
        kth_words = []
        for _ in range(k):
            curr_word = heapq.heappop(heap)
            kth_words.append(curr_word[1])
        return kth_words

        
class TestMethods(unittest.TestCase):

    def test_findRelativeRanks_ex1(self):
        inputs = ["i","love","leetcode","i","love","coding"]
        output = ["i","love"]
        mySolution = Solution()
        self.assertEqual(mySolution.topKFrequent(inputs, 2), output)
        
    def test_findRelativeRanks_ex2(self):
       inputs = ["the","day","is","sunny","the","the","the","sunny","is","is"]
       output = ["the","is","sunny","day"]
       mySolution = Solution()
       self.assertEqual(mySolution.topKFrequent(inputs, 4), output)
        

if __name__ == '__main__':
    unittest.main()
    