# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: permutations-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 01:55:50
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a collection of numbers, `nums`, that might
# contain duplicates, return *all possible unique permutations **in
# any order**.*
#
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Constraints:
# *   `1 <= nums.length <= 8`
# ********************************************************************************


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        visited = [False]*len(nums)
        return self.dfs(sorted(nums), visited, [], [])

    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(permutation)
            return permutations[:]

        res = []
        for i in range(len(nums)):
            # 当前数字访问过
            if visited[i]:
                continue

            # 当前数没有访问过，并且上一个数和当前数相同
            if ((i > 0 and nums[i] == nums[i-1]) and (not visited[i-1])):
                # 当上一个数没选择过时，跳过当前数的选择，因为如果选了当前数，
                # 此时情况是“没有选择添加上一个数，选择当前数”
                # 会和“选择添加上一个数，没有选当前数”产生重复
                # “选择添加上一个数，没有选当前数”这一个选项是“选择添加上一个数”
                # 时“选择下一个数”以及“不选择下一个数”的一种子情况
                continue

            visited[i] = True
            res.extend(self.dfs(nums, visited, permutation+[nums[i]], permutations[:]))
            visited[i] = False

        return res
