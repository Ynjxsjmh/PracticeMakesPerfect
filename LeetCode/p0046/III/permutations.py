# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: permutations.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 01:34:30
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array `nums` of distinct integers, return *all
# the possible permutations*. You can return the answer in **any
# order**.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
# Constraints:
# *   `1 <= nums.length <= 6`
# *   `-10 <= nums[i] <= 10`
# *   All the integers of `nums` are **unique**.
# ********************************************************************************


class Solution(object):
    def permute(self, nums):
        """这个问题可以看作有 n 个排列成一行的空格，需要从左往右依此填
        入题目给定的 n 个数，每个数只能使用一次。

        那么很直接的可以想到一种穷举的算法，即从左往右每一个位置都依此
        尝试填入一个数，看能不能填完这 n 个空格，在程序中我们可以用
        「回溯法」来模拟这个过程。

        定义递归函数 backtrack(idx, permutation) 表示从左往右填到第
        idx 个位置，当前排列为 permutation。 那么整个递归函数分为两个情况：

        - 如果 idx=n，说明已经填完了 n 个位置（注意下标从 0 开始），
          找到了一个可行的解，我们将 permutation 放入答案数组中，递归
          结束。

        - 如果 idx<n，我们要考虑这第 idx 个位置我们要填哪个数。根据题
          目要求我们肯定不能填已经填过的数，因此很容易想到的一个处理手
          段是我们定义一个标记数组 vis 来标记已经填过的数。在填第 idx
          个数的时候我们遍历题目给定的 n 个数，如果这个数没有被标记过，
          我们就填入，并将其标记，继续填下一个位置，即调用函数
          backtrack(idx+1,permutation)。回溯的时候要撤销这一个位置填的
          数以及标记，并继续尝试其他没被标记过的数。

        :type nums: List[int]
        :rtype: List[List[int]]

        """
        visited = [False]*len(nums)
        return self.dfs(nums, 0, visited, [], [])

    def dfs(self, nums, idx, visited, permutation, permutations):
        if idx == len(nums):
            permutations.append(permutation)
            return permutations[:]

        res = []
        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i] = True
            res.extend(self.dfs(nums, idx+1, visited, permutation+[nums[i]], permutations[:]))
            visited[i] = False

        return res
