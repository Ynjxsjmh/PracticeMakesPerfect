# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: third-maximum-number.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-09 22:29:19
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums`, return *the **third
# distinct maximum** number in this array. If the third maximum does
# not exist, return the **maximum** number*.
#
# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
#
# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is
# returned instead.
#
# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together
# since they have the same value).
# The third distinct maximum is 1.
#
# Constraints:
# *   `1 <= nums.length <= 104`
# *   `-231 <= nums[i] <= 231 - 1`
# ********************************************************************************



class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        heap = [-num for num in set(nums)]
        heapq.heapify(heap)

        if len(heap) < 3:
            return -heap[0]

        for _ in range(2):
            heapq.heappop(heap)

        return -heap[0]
