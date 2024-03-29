# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-minimum-in-rotated-sorted-array-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-13 00:03:34
# Last Updated: 
#           By: Ynjxsjmh
# Description: Suppose an array of length `n` sorted in ascending
# order is **rotated** between `1` and `n` times. For example, the
# array `nums = [0,1,4,4,5,6,7]` might become:
#
# *   `[4,5,6,7,0,1,4]` if it was rotated `4` times.
# *   `[0,1,4,4,5,6,7]` if it was rotated `7` times.
#
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1
# time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
#
# Given the sorted rotated array `nums` that may contain **duplicates**,
# return *the minimum element of this array*.
#
# You must decrease the overall operation steps as much as possible.
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
#
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
#
# Constraints:
# *   `n == nums.length`
# *   `1 <= n <= 5000`
# *   `-5000 <= nums[i] <= 5000`
# *   `nums` is sorted and rotated between `1` and `n` times.
# ********************************************************************************

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) / 2

            if nums[m] > nums[r]:
                # [l, m] 有序
                l = m + 1
            elif nums[m] < nums[r]:
                # [m, r] 有序
                r = m
            else:
                r -= 1

        return nums[r]

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) / 2

            if nums[m] > nums[r-1]:
                # [l, m] 有序
                l = m
            elif nums[m] < nums[r-1]:
                # [m, r] 有序
                r = m
            else:
                r -= 1

        return nums[l]
