# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: minimum-size-subarray-sum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 17:56:46
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
# ********************************************************************************

class Solution(object):
    # Time Limit Exceeded
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = 0
        length = float('inf')

        while l < len(nums) and r < len(nums) and l <= r:
            if sum(nums[l:r+1]) >= target:
                if r+1-l < length:
                    length = r - l + 1
                l = l + 1
            else:
                r = r + 1

        return 0 if length == float('inf') else length

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = 0
        n = len(nums)
        length = float('inf')
        cur_sum = nums[0]
        nums.append(0)

        while l < n and r < n and l <= r:
            if cur_sum >= target:
                if r+1-l < length:
                    length = r - l + 1
                # 把当前 l 移除窗口
                cur_sum -= nums[l]
                l = l + 1
            else:
                # 把下一个 r+1 加入窗口
                r = r + 1
                cur_sum += nums[r]

        return 0 if length == float('inf') else length

