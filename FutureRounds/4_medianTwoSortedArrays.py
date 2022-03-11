# -*- coding: utf-8 -*-
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

import unittest



class TestStringMethods(unittest.TestCase):

    def test_twoSum_ex1(self):
        nums1 = [1,3]
        nums2 = [2]
        output = 2.00000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
        
    def test_twoSum_ex2(self):
        nums1 = [1,2]
        nums2 = [3,4]
        output = 2.50000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
        
    def test_twoSum_empty1(self):
        nums1 = []
        nums2 = [3,4]
        output = 3.5
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
        
    def test_twoSum_empty2(self):
        nums1 = [1,3]
        nums2 = []
        output = 2.00000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
    
    def test_twoSum_emptyBoth(self):
        nums1 = []
        nums2 = []
        output = None
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)

    def test_twoSum_interleaved(self):
        nums1 = [1,3,5,7]
        nums2 = [2,4,6]
        output = 4.00000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
        
    def test_twoSum_nums1nums2(self):
        nums1 = [1,2,3,4]
        nums2 = [5,6,7]
        output = 4.00000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
        
    def test_twoSum_nums2nums1(self):
        nums1 = [5,6,7]
        nums2 = [1,2,3,4]
        output = 4.00000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)
        
    def test_twoSum_multiples(self):
        nums1 = [5,6,7]
        nums2 = [1,2,2,4]
        output = 4.00000
        mySolution = Solution()
        self.assertEqual(mySolution.findMedianSortedArrays(nums1, nums2), output)

if __name__ == '__main__':
    unittest.main()
