# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-first-and-last-position-of-element-in-sorted-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 14:54:42
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array of integers `nums` sorted in
# non-decreasing order, find the starting and ending position of a
# given `target` value.
#
# If `target` is not found in the array, return `[-1, -1]`.
#
# You must write an algorithm with `O(log n)` runtime complexity.
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
# Constraints:
# *   `0 <= nums.length <= 105`
# *   `-109 <= nums[i] <= 109`
# *   `nums` is a non-decreasing array.
# *   `-109 <= target <= 109`
# ********************************************************************************

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(nums)
        res = []

        while l < r:
            m = l + (r - l) / 2

            if nums[m] == target:
                res.append(m)
                while m-1 >= 0:
                    if nums[m-1] == target:
                        res = [m-1] + res
                    m -= 1
                while m+1 < len(nums):
                    if nums[m+1] == target:
                        res.append(m+1)
                    m += 1
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        if len(res):
            return [res[0], res[-1]]
        else:
            return [-1, -1]
