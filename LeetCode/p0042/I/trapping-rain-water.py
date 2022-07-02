# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: trapping-rain-water.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-02 15:14:57
# Last Updated:
#           By: Ynjxsjmh
# Description: Given `n` non-negative integers representing an
# elevation map where the width of each bar is `1`, compute how much
# water it can trap after raining.
#
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented
# by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain
# water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
# Constraints:
# *   `n == height.length`
# *   `1 <= n <= 2 * 104`
# *   `0 <= height[i] <= 105`
# ********************************************************************************


class Solution(object):
    def trap(self, height):
        """找 peak 值
        - 如果当前值是 peak 值
          不能存水
        - 如果当前值不是 peak 值
          当前值能存的最大水量是左右最小 peak 与当前值的差

        状态：
        - max_left[i]：[0, i] 中最大的值
        - max_right[i]：[i, n] 中最大的值

        状态转移方程：
        [0, i] 中最大的值为 [0, i-1] 的最大值和 i 值大的那个
        :type height: List[int]
        :rtype: int
        """

        n = len(height)

        max_left  = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        max_right = [0] * n
        max_right[n-1] = height[n-1];
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        water = 0
        for i in range(1, n-1):
            water += min(max_left[i], max_right[i]) - height[i]

        return water
