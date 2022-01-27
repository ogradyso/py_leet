# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
Accepted
2,456,077
Submissions
6,515,933

"""
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None and l2 == None):
            return None
        
        target_node = l1
        num1_str = ''
        num2_str = ''
        while target_node != None:
            num1_str = str(target_node.val) + num1_str 
            target_node = target_node.next
        
        if (num1_str == ''):
            num1_str = '0'
            
        target_node = l2
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next

        if (num2_str == ''):
            num2_str = '0'
            
        sum_val = int(num1_str) + int(num2_str)
        str_val = str(sum_val)
        prev_node = None
        for num_char in str_val:
            current_node = ListNode(int(num_char),prev_node)
            prev_node = current_node
            
            
        return prev_node
        


class TestStringMethods(unittest.TestCase):

    def test_addTwoNumbers_ex1(self):
        L1_c = ListNode(3)
        L1_b = ListNode(4, L1_c)
        L1_a = ListNode(2, L1_b)
        
        L2_c = ListNode(4)
        L2_b = ListNode(6, L2_c)
        L2_a = ListNode(5, L2_b)
        
        num2_str = ''
        mySolution = Solution()
        target_node = mySolution.addTwoNumbers(L1_a,L2_a)
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next
        
        self.assertEqual(num2_str, '807')
        
    def test_addTwoNumbers_ex2(self):
        L1_a = ListNode(0)
        
        L2_a = ListNode(0)
        
        num2_str = ''
        mySolution = Solution()
        target_node = mySolution.addTwoNumbers(L1_a,L2_a)
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next
        
        self.assertEqual(num2_str, '0')
        
    def test_addTwoNumbers_ex3(self):
        L1_g = ListNode(9)
        L1_f = ListNode(9, L1_g)
        L1_e = ListNode(9, L1_f)
        L1_d = ListNode(9, L1_e)
        L1_c = ListNode(9, L1_d)
        L1_b = ListNode(9, L1_c)
        L1_a = ListNode(9, L1_b)
        
        L2_d = ListNode(9)
        L2_c = ListNode(9, L2_d)
        L2_b = ListNode(9, L2_c)
        L2_a = ListNode(9, L2_b)
        
        num2_str = ''
        mySolution = Solution()
        target_node = mySolution.addTwoNumbers(L1_a,L2_a)
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next
        
        self.assertEqual(num2_str, '10009998')
        
    def test_addTwoNumbers_ex4(self):
        L1_c = ListNode(9)
        L1_b = ListNode(4, L1_c)
        L1_a = ListNode(2, L1_b)
        
        L2_d = ListNode(9)
        L2_c = ListNode(4, L2_d)
        L2_b = ListNode(6, L2_c)
        L2_a = ListNode(5, L2_b)
        
        num2_str = ''
        mySolution = Solution()
        target_node = mySolution.addTwoNumbers(L1_a,L2_a)
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next
        
        self.assertEqual(num2_str, '10407')
        
    def test_addTwoNumbers_bothEmpty(self):
        L1_a = None
        
        L2_a = None
        
        output = None
        
        mySolution = Solution()
        self.assertEqual(mySolution.addTwoNumbers(L1_a,L2_a), output)
        
    def test_addTwoNumbers_l1Empty(self):
        L1_a = None
        
        L2_a = ListNode(5)
        
        num2_str = ''
        mySolution = Solution()
        target_node = mySolution.addTwoNumbers(L1_a,L2_a)
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next
        
        self.assertEqual(num2_str, '5')
        
    def test_addTwoNumbers_l2Empty(self):
        L1_a = ListNode(5)
        
        L2_a = None
        
        num2_str = ''
        mySolution = Solution()
        target_node = mySolution.addTwoNumbers(L1_a,L2_a)
        while target_node != None:
            num2_str = str(target_node.val) + num2_str 
            target_node = target_node.next
        
        self.assertEqual(num2_str, '5')
    

if __name__ == '__main__':
    unittest.main()