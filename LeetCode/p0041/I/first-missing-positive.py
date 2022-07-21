# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: first-missing-positive.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-22 00:22:14
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an unsorted integer array `nums`, return the
# smallest missing positive integer.
#
# You must implement an algorithm that runs in `O(n)` time and uses
# constant extra space.
#
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
#
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
#
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
#
# Constraints:
# *   `1 <= nums.length <= 5 * 105`
# *   `-231 <= nums[i] <= 231 - 1`
# ********************************************************************************


class Solution(object):
    def firstMissingPositive(self, nums):
        """遍历一次数组把大于等于 1 的并且小于数组大小的值放到原数组对应位置
        然后再遍历一次数组查当前下标是否和值对应：
        1. 如果不对应那这个下标就是答案
        2. 否则遍历完都没出现那么答案就是数组长度加 1。
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                # 下面这样交换不行
                #nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                # 下面这样可以
                #nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp

                # # 下面这样不行
                # temp = nums[i]
                # nums[i] = nums[nums[i]-1]
                # # 下面的 nums[i] 和 temp 时的不一样了
                # nums[nums[i]-1] = temp

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
