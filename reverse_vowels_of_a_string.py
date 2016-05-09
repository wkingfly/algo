# -*- coding: utf-8 -*-
"""
Write a function that takes a string as input and
reverse only the vowels of a string.

Example 1:
    Given s = "hello", return "holle".

Example 2:
    Given s = "leetcode", return "leotcede".

..note:: vowels are five word: a e i o u
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = list('aeiou')
        if not s:
            return

        n_heap = []
        v_i_stack = []
        v_w_stack = []
        sl = list(s)
        for i in sl:
            if i in vowels:
                v_w_stack.append(i)
                v_i_stack.append(sl.index(i))
        for si in sl:
            if sl.index(si) in v_i_stack:
                n_heap.append(v_w_stack.pop())
            else:
                n_heap.append(si)
        return ''.join(n_heap)


if __name__ == '__main__':
    s = 'hello'
    ss = Solution()
    print ss.reverseVowels(s)
