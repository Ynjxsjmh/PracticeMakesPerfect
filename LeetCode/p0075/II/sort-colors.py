# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: sort-colors.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-29 13:45:44
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array `nums` with `n` objects colored red,
# white, or blue, sort them
# **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so
# that objects of the same color are adjacent, with the colors in the
# order red, white, and blue.
#
# We will use the integers `0`, `1`, and `2` to represent the color red,
# white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
# Constraints:
# *   `n == nums.length`
# *   `1 <= n <= 300`
# *   `nums[i]` is either `0`, `1`, or `2`.
# ********************************************************************************


class Solution(object):
    def sortColors(self, nums):
        """因为只有三个数，头尾各一个指针，再用一个指针从头开始遍历：
        - 当前指针遇到 2
          1. 和尾指针的数交换，尾指针向前；
          2. 当前指针保持不变，下一轮判断换过来的值是什么；
        - 当前指针遇到 0
          1. 和头指针的数交换，头指针向后；
          2. 当前指针向后（不太理解为什么）
        - 当前指针遇到 1
          1. 当前指针继续向后
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        cur = 0
        l = 0
        r = len(nums) -1

        while cur <= r:
            if nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            elif nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                cur += 1
            else:
                cur += 1
