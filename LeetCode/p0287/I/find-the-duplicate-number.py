# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-the-duplicate-number.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-11 12:19:41
# Last Updated:
#           By: Ynjxsjmh
# Description: Given an array of integers `nums` containing `n + 1`
# integers where each integer is in the range `[1, n]` inclusive.
#
# There is only one repeated number in `nums`, return
# this repeated number.
#
# You must solve the problem without modifying
# the array `nums` and uses only constant extra space.
#
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
#
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
#
# Constraints:
#    `1 <= n <= 105`
#    `nums.length == n + 1`
#    `1 <= nums[i] <= n`
#    All the integers in `nums` appear only once except for precisely one
# integer which appears two or more times.
# ********************************************************************************

class Solution(object):
    # 此题只让用 constant extra space，这个方法不行
    def findDuplicate(self, nums):
        """用集合记录出现过的数字，set 比 list 快
        :type nums: List[int]
        :rtype: int
        """

        s = set()

        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)

        return None

    def findDuplicate(self, nums):
        """基于值的二分法：
        因为数都在 [1,n] 之间，二分搜索，
        统计列表中和 mid 相比的数量。
        :type nums: List[int]
        :rtype: int
        """

        lo = 1
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi - lo) / 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt <= mid:
                lo = mid + 1
            else:
                hi = mid

        return hi
