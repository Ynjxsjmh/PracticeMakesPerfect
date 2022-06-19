# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-continuous-increasing-subsequence.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 19:06:27
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an unsorted array of integers `nums`, return *the
# length of the longest **continuous increasing subsequence**
# (i.e. subarray)*. The subsequence must be **strictly** increasing.
#
# A **continuous increasing subsequence** is defined by two indices `l`
# and `r` (`l < r`) such that it is `[nums[l], nums[l + 1], ..., nums[r
# - 1], nums[r]]` and for each `l <= i < r`, `nums[i] < nums[i + 1]`.
#
# Example 1:
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5]
# with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not
# continuous as elements 5 and 7 are separated by element 4.
#
# Example 2:
# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with
# length 1. Note that it must be strictly increasing.
#
# Constraints:
# *   `1 <= nums.length <= 104`
# *   `-109 <= nums[i] <= 109`
# ********************************************************************************

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """dp[i] 定义为 [0,i] 间以 nums[i] 结尾的最长连续上升子序列的长度
        状态转移方程：
        dp[i] = dp[i-1] + 1   if nums[i] > nums[i-1]
              = 1             if nums[i] <= nums[i-1]
        当 nums[i] > nums[i-1] 时，说明 nums[i] 与之前的数构成一个连续上升子序列，
        因此长度加一
        当 nums[i] <= nums[i-1] 时，之前的连续上升子序列被破坏，
        之后的连续上升子序列从 nums[i] 开始计算，当前长度置 1
        :type nums: List[int]
        :rtype: int
        """

        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            dp[i] = dp[i-1]+1 if nums[i] > nums[i-1] else 1

        return max(dp)