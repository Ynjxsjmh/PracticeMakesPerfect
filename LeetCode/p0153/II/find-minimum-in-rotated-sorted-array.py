# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-minimum-in-rotated-sorted-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 00:46:53
# Last Updated: 
#           By: Ynjxsjmh
# Description: Suppose an array of length `n` sorted in ascending
# order is **rotated** between `1` and `n` times. For example, the
# array `nums = [0,1,2,4,5,6,7]` might become:
#
# *   `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# *   `[0,1,2,4,5,6,7]` if it was rotated `7` times.
#
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]`
# 1 time results in the array `[a[n-1], a[0], a[1], a[2], ...,
# a[n-2]]`.
#
# Given the sorted rotated array `nums` of **unique** elements, return
# *the minimum element of this array*.
#
# You must write an algorithm that runs in `O(log n) time.`
#
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#
# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
#
# Constraints:
#    `n == nums.length`
#    `1 <= n <= 5000`
#    `-5000 <= nums[i] <= 5000`
#    All the integers of `nums` are unique.
#    `nums` is sorted and rotated between `1` and `n` times.
# ********************************************************************************


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums)
        nums.append(float('inf'))

        while l < r:
            m = l + (r - l) / 2

            if nums[m-1] >= nums[m] & nums[m] <= nums[m+1]:
                l = m
                break
            elif nums[m] > nums[r-1]:
                # [l, m] 有序
                # // Case 1) Left side sorted, right side has pivot (minval), go right to find it
                l = m + 1
            else:
                # [m, r] 有序
                # // Case 1) Right side sorted, left side has pivot (minval), go left to find it
                # // Case 2) Both sides sorted, go left to find the pivot (minval) (m 点右边是 minval)
                r = m

        return nums[l]
