# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: maximum-subarray.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-15 12:41:49
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums`, find the contiguous
# subarray (containing at least one number) which has the largest sum
# and return *its sum*.
#
# A **subarray** is a **contiguous** part of an array.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
# Constraints:
# *   `1 <= nums.length <= 105`
# *   `-104 <= nums[i] <= 104`
# ********************************************************************************


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            dp[i] = max(dp[i-1] + num, num)

        return max(dp)
