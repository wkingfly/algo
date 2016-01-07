"""
Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2. Please
note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_num = None
        second_num = None
        nums_level2 = nums
        for num_level1 in nums:
            for num_level2 in nums_level2:
                if not first_num:
                    first_num = num_level1
                    continue
                if not second_num:
                    second_num = num_level2
                    continue
                if second_num == first_num:
                    second_num = num_level2
                    continue
                result = first_num + second_num
                if result != target:
                    second_num = num_level2
                    continue
                if result == target:
                    return [nums.index(first_num)+1,
                            nums.index(second_num)+1]
            first_num = num_level1
            nums_level2 = nums[nums.index(first_num)+1:]
        return None
