# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: house-robber-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-17 13:49:32
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are a professional robber planning to rob houses
# along a street. Each house has a certain amount of money
# stashed. All houses at this place are **arranged in a circle.** That
# means the first house is the neighbor of the last one. Meanwhile,
# adjacent houses have a security system connected, and **it will
# automatically contact the police if two adjacent houses were broken
# into on the same night**.
#
# Given an integer array `nums` representing the amount of money of each
# house, return *the maximum amount of money you can rob tonight
# **without alerting the police***.
#
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3
# (money = 2), because they are adjacent houses.
#
# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 3:
# Input: nums = [1,2,3]
# Output: 3
#
# Constraints:
# *   `1 <= nums.length <= 100`
# *   `0 <= nums[i] <= 1000`
# ********************************************************************************

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n <= 2:
            return max(nums)

        robEven = [0] * n  # [0, n-2]
        robOdd  = [0] * n  # [1, n-1]

        robEven[0] = nums[0]
        robOdd[1]  = nums[1]

        for i in range(n-1):
            robEven[i] = max(robEven[i-1], robEven[i-2]+nums[i])

        for i in range(1, n):
            robOdd[i] = max(robOdd[i-1], robOdd[i-2]+nums[i])

        return max(robEven[n-2], robOdd[n-1])
