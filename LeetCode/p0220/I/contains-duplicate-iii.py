# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: contains-duplicate-iii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-11 01:10:02
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` and two integers `k` and
# `t`, return `true` if there are **two distinct indices** `i` and `j`
# in the array such that `abs(nums[i] - nums[j]) <= t` and `abs(i - j) <= k`.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
#
# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
#
# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#
# Constraints:
#    `1 <= nums.length <= 2  104`
#    `-231 <= nums[i] <= 231 - 1`
#    `0 <= k <= 104`
#    `0 <= t <= 231 - 1`
# ********************************************************************************

class Solution(object):
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        # Time Limit Exceeded
        """用字典记录 value:index，每次 loop 字典比较 value
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        d = {}

        for i, num in enumerate(nums):
            for val, j in d.items():
                if abs(num-val) <= t and abs(i-j) <= k:
                    return True

            d[num] = i

        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """桶排序，同样用字典记录 value:index
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        bucket = {}
        w = t + 1

        for i, num in enumerate(nums):
            bucket_id = num / w

            if bucket_id in bucket:
                return True
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) < w:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) < w:
                return True

            bucket[bucket_id] = num

            if i >= k: del bucket[nums[i - k] / w]

        return False
