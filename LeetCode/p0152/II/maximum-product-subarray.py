# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: maximum-product-subarray.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 00:06:34
# Last Updated:
#           By: Ynjxsjmh
# Description: Given an integer array `nums`, find a contiguous
# non-empty subarray within the array that has the largest product,
# and return *the product*.
#
# The test cases are generated so that the answer will fit in a
# **32-bit** integer.
#
# A **subarray** is a contiguous subsequence of the array.
#
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
# Constraints:
# *  `1 <= nums.length <= 2 * 104`
# *  `-10 <= nums[i] <= 10`
# * The product of any prefix or suffix of `nums` is **guaranteed** to
#     fit in a **32-bit** integer.
# ********************************************************************************



class Solution(object):
    def maxProduct(self, nums):
        """
        dp_max[i] 表示以第 i 个元素*结尾*的乘积最大子数组的乘积
        :type nums: List[int]
        :rtype: int
        """

        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])

        print(dp_max)
        return max(dp_max)
