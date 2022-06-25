# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: combination-sum-iv.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 12:53:37
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array of **distinct** integers `nums` and a
# target integer `target`, return *the number of possible combinations
# that add up to* `target`.
#
# The test cases are generated so that the answer can fit in a
# **32-bit** integer.
#
# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#
# Example 2:
# Input: nums = [9], target = 3
# Output: 0
#
# Constraints:
# *   `1 <= nums.length <= 200`
# *   `1 <= nums[i] <= 1000`
# *   All the elements of `nums` are **unique**.
# *   `1 <= target <= 1000`
# ********************************************************************************


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 用 [None] * (target + 1) 回超时
        mem = {}
        return self.dfs(nums, target, mem)

    def dfs(self, nums, target, mem):
        if target < 0:
            return 0

        if target == 0:
            return 1

        if target in mem:
            return mem[target]

        res = 0
        for i in range(0, len(nums)):
            res += (self.dfs(nums, target-nums[i], mem))
        mem[target] = res

        return res
