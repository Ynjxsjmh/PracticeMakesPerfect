# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: product-of-array-except-self.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-10 14:36:21
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums`, return *an array*
# `answer` *such that* `answer[i]` *is equal to the product of all the
# elements of* `nums` *except* `nums[i]`.
#
# The product of any prefix or suffix of `nums` is **guaranteed** to
# fit in a **32-bit** integer.
#
# You must write an algorithm that runs in `O(n)` time and without
# using the division operation.
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
# Constraints:
# *   `2 <= nums.length <= 105`
# *   `-30 <= nums[i] <= 30`
# *   The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.
# ********************************************************************************


class Solution(object):
    # 题目要求 without using the division operation
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zero_cnt = 0
        none_zero_mul = 1

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                none_zero_mul *= num

        res = []
        for num in nums:
            if zero_cnt == 0:
                res.append(none_zero_mul / num)
            elif zero_cnt == 1 and num == 0:
                res.append(none_zero_mul)
            elif zero_cnt == 1 and num != 0:
                res.append(0)
            elif zero_cnt > 1:
                res.append(0)

        return res

    def productExceptSelf(self, nums):
        """
        原数组：       [1       2       3       4]
        左部分的乘积：   1       1      1*2    1*2*3
        右部分的乘积： 2*3*4    3*4      4      1
        结果：        1*2*3*4  1*3*4   1*2*4  1*2*3*1
        :type nums: List[int]
        :rtype: List[int]
        """

        res, left_mul, right_mul = [1], 1, 1

        for i in range(1, len(nums)):
            left_mul *= nums[i-1]
            res.append(left_mul)

        for i in range(len(nums)-1, -1, -1):
            res[i] *= right_mul
            right_mul *= nums[i]

        return res
