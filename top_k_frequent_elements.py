# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is
the array's size.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map_d = {}
        for n in nums:
            str_n = str(n)
            if str_n not in map_d:
                map_d[str_n] = 1
            else:
                map_d[str_n] += 1
        map_d_sort = self.dict_quick_sort(map_d)
        return [int(x[0]) for x in map_d_sort[:k]]

    def dict_quick_sort(self, map_d):
        if not map_d:
            return []
        if not isinstance(map_d, list):
            map_l = map_d.items()
        else:
            map_l = map_d
        m = map_l[0]
        m_elems = [x for x in map_l if x[1] == m[1]]
        r_elems = [x for x in map_l if x[1] < m[1]]
        l_elems = [x for x in map_l if x[1] > m[1]]
        return self.dict_quick_sort(
            l_elems)+m_elems+self.dict_quick_sort(r_elems)


if __name__ == '__main__':
    l = [1, 1, 1, 2, 2, 3, 3, 3]
    k = 2
    s = Solution()
    print s.topKFrequent(l, k)
