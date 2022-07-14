# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-consecutive-sequence.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-10 15:29:09
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an unsorted array of integers `nums`, return *the
# length of the longest consecutive elements sequence.*
#
# You must write an algorithm that runs in `O(n)` time.
#
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is `[1, 2, 3,
# 4]`. Therefore its length is 4.
#
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
# Constraints:
# *   `0 <= nums.length <= 105`
# *   `-109 <= nums[i] <= 109`
# ********************************************************************************


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s, longest = set(nums), 0

        for num in nums:
            cur_longest = 1

            # 往前找最长连续
            i = 1
            while num - i in s:
                s.remove(num - i)
                i += 1
                cur_longest += 1

            # 往后找最长连续
            j = 1
            while num + j in s:
                s.remove(num + j)
                j += 1
                cur_longest += 1

            longest = max(cur_longest, longest)

        return longest
