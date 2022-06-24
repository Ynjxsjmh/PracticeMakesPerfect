# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: subsets.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 00:50:58
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` of **unique** elements,
# return *all possible subsets (the power set)*.
#
# The solution set **must not** contain duplicate subsets. Return the
# solution in **any order**.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
# *   `1 <= nums.length <= 10`
# *   `-10 <= nums[i] <= 10`
# *   All the numbers of `nums` are unique.
# ********************************************************************************


class Solution(object):
    def subsets(self, nums):
        """对当前每个数有加或不加两种选择
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return self.dfs(nums, 0, [], [])

    def dfs(self, nums, idx, subset, subsets):
        if idx == len(nums):
            subsets.append(subset)
            return subsets[:]

        add = self.dfs(nums, idx+1, subset+[nums[idx]], subsets[:])
        not_add = self.dfs(nums, idx+1, subset+[], subsets[:])

        return add + not_add