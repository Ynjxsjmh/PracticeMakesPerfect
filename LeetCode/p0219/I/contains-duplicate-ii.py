# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: contains-duplicate-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-11 01:01:12
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
# Constraints:
#    `1 <= nums.length <= 105`
#    `-109 <= nums[i] <= 109`
#    `0 <= k <= 105`
# ********************************************************************************

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """用字典保存 value:index
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d = {}

        for i, num in enumerate(nums):
            if num in d and abs(d[num]-i) <= k:
                return True
            else:
                d[num] = i

        return False
