# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: minimum-size-subarray-sum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-02 19:38:08
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array of positive integers `nums` and a
# positive integer `target`, return the minimal length of a
# **contiguous subarray** `[numsl, numsl+1, ..., numsr-1, numsr]` of
# which the sum is greater than or equal to `target`. If there is no
# such subarray, return `0` instead.
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
# Constraints:
# *   `1 <= target <= 109`
# *   `1 <= nums.length <= 105`
# *   `1 <= nums[i] <= 104`
#
# **Follow up:** If you have figured out the `O(n)` solution, try
# **coding another solution of which the time complexity is `O(n
# **log(n))`.
# ********************************************************************************



class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, 0
        min_len = float('inf')
        cur_sum = 0

        while r < len(nums):
            cur_sum += nums[r]
            r += 1

            while cur_sum >= target:
                min_len = min(min_len, r-l)
                cur_sum -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len
