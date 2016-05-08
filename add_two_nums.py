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
        aliquo_num = 0
        lr = ListNode(l1.val+l2.val)
        if lr.val >= carry_num:
            aliquo_num = lr.val // carry_num
            lr.val = lr.val % carry_num
        if l1.next and l2.next:
            l1.next.val += aliquo_num
            lr.next = self.addTwoNumbers(l1.next, l2.next)
        elif l1.next:
            l2.next = ListNode(aliquo_num)
            lr.next = self.addTwoNumbers(l1.next, l2.next)
        elif l2.next:
            l1.next = ListNode(aliquo_num)
            lr.next = self.addTwoNumbers(l1.next, l2.next)
        elif aliquo_num:
            nt = ListNode(0)
            ny = ListNode(aliquo_num)
            lr.next = self.addTwoNumbers(nt, ny)
        return lr

if __name__ == '__main__':
    l1 = [3, 7]
    l2 = [9, 2]

    def turn_to_n(l):
        node = None
        while(l):
            if not node:
                n = l.pop(0)
                node = ListNode(n)
                l.append(node)
            if l and isinstance(l[0], int):
                node_t = l.pop()
                n1 = l.pop(0)
                if isinstance(node_t, ListNode):
                    node_t.next = ListNode(n1)
                    l.append(node_t.next)
            else:
                l.pop()
        if node:
            return node
        print "Error!"

    ln1 = turn_to_n(l1)
    ln2 = turn_to_n(l2)
    s = Solution()
    print s.addTwoNumbers(ln1, ln2).val
