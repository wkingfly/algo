"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a
single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_num = 10
        if l1.val and l2.val:
            lr = ListNode(l1.val+l2.val)
            if lr.val >= carry_num:
                lr.val = lr.val % carry_num
                aliquo_num = lr.val // carry_num
        if not (l1.next and l2.next) is None:
            l1.next.val += aliquo_num
            lr.next = self.addTwoNumbers(l1.next, l2.next)
        return lr
