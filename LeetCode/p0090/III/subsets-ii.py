# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: subsets-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 00:56:39
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` that may contain
# duplicates, return *all possible subsets (the power set)*.
#
# The solution set **must not** contain duplicate subsets. Return the
# solution in **any order**.
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
# *   `1 <= nums.length <= 10`
# *   `-10 <= nums[i] <= 10`
# ********************************************************************************


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return self.dfs(sorted(nums), 0, False, [], [])

    def dfs(self, nums, idx, choose_pre, subset, subsets):
        if idx == len(nums):
            subsets.append(subset)
            return subsets[:]

        # 选择不添加当前数
        not_add = self.dfs(nums, idx+1, False, subset, subsets[:])

        # 选择添加当前数
        # 如果没有选择添加上一个数，并且上一个数和当前数相同
        if ((not choose_pre) and ((idx > 0) and (nums[idx-1] == nums[idx]))):
            # 跳过当前数的选择，因为如果选了当前数，
            # 此时情况是“没有选择添加上一个数，选择当前数”
            # 会和“选择添加上一个数，没有选当前数”产生重复
            return self.dfs(nums, idx+1, False, subset, subsets[:])

        add = self.dfs(nums, idx+1, True, subset+[nums[idx]], subsets[:])

        return not_add + add
