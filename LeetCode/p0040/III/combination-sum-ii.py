# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: combination-sum-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 12:37:01
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a collection of candidate numbers (`candidates`)
# and a target number (`target`), find all unique combinations in
# `candidates` where the candidate numbers sum to `target`.
#
# Each number in `candidates` may only be used **once** in the combination.
#
# **Note:** The solution set must not contain duplicate combinations.
#
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
# Constraints:
# *   `1 <= candidates.length <= 100`
# *   `1 <= candidates[i] <= 50`
# *   `1 <= target <= 30`
# ********************************************************************************


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        return self.dfs(sorted(candidates), target, 0, [], [])

    def dfs(self, nums, target, idx, combination, combinations):
        if target < 0:
            return combinations[:]

        if target == 0:
            combinations.append(combination)
            return combinations[:]

        res = []
        for i in range(idx, len(nums)):
            if (i > idx and nums[i] == nums[i-1]):
                continue
            res.extend(self.dfs(nums, target-nums[i], i+1, combination+[nums[i]], combinations[:]))

        return res
