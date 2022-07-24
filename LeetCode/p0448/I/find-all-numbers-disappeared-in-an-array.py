# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-all-numbers-disappeared-in-an-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-24 10:51:25
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array `nums` of `n` integers where `nums[i]`
# is in the range `[1, n]`, return *an array of all the integers in
# the range* `[1, n]` *that do not appear in* `nums`.
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
# Constraints:
# *   `n == nums.length`
# *   `1 <= n <= 105`
# *   `1 <= nums[i] <= n`
#
# **Follow up:** Could you do it without extra space and in `O(n)`
# **runtime? You may assume the returned list does not count as extra
# **space.
# ********************************************************************************



class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # 将数组元素值对应的索引位置加 n
        for i in range(n):
            idx = (nums[i] - 1) % n
            nums[idx] += n

        res = []
        # 若数组元素值小于等于 n，则说明数组下标值不存在，即消失的数字
        for i in range(n):
            if nums[i] <= n:
                res.append(i+1)

        return res
