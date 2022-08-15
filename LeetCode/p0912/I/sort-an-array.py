# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: sort-an-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-10 14:31:52
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array of integers `nums`, sort the array in
# ascending order.
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
#
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
# Constraints:
# *   `1 <= nums.length <= 5 * 104`
# *   `-5 * 104 <= nums[i] <= 5 * 104`
# ********************************************************************************



class Solution(object):
    def sortArray(self, nums):
        """基础排序
        :type nums: List[int]
        :rtype: List[int]
        """

        self.quick_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, nums, beg, end):
        if beg >= end: # = doesn't matter
            return

        l, m, r = beg, (end - beg) // 2 + beg, end
        pivot = nums[m]

        while l <= r:
            # 找到左边第一个比 pivot 大的数
            while l <= r and nums[l] < pivot:
                l += 1

            # 找到右边第一个比 pivot 小的数
            while l <= r and nums[r] > pivot:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        self.quick_sort(nums, beg, r)
        self.quick_sort(nums, l, end)
