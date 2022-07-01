# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: squares-of-a-sorted-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-01 08:26:44
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` sorted in
# **non-decreasing** order, return *an array of **the squares of each
# number** sorted in non-decreasing order*.
#
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
# Constraints:
# *   `1 <= nums.length <= 104`
# *   `-104 <= nums[i] <= 104`
# *   `nums` is sorted in **non-decreasing** order.
# ********************************************************************************


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l, r = 0, len(nums) - 1
        squares = [0] * len(nums)
        i = r

        while l <= r and i >= 0:
            if abs(nums[l]) >= abs(nums[r]):
                squares[i] = nums[l] ** 2
                l += 1
            else:
                squares[i] = nums[r] ** 2
                r -= 1
            i -= 1

        return squares
