# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: container-with-most-water.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-08 23:03:11
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an integer array `height` of length
# `n`. There are `n` vertical lines drawn such that the two endpoints
# of the `ith` line are `(i, 0)` and `(i, height[i])`.
#
# Find two lines that together with the x-axis form a container, such
# that the container contains the most water.
#
# Return *the maximum amount of water a container can store*.
#
# **Notice** that you may not slant the container.
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue
# section) the container can contain is 49.
#
# Example 2:
# Input: height = [1,1]
# Output: 1
#
# Constraints:
# *   `n == height.length`
# *   `2 <= n <= 105`
# *   `0 <= height[i] <= 104`
# ********************************************************************************


class Solution(object):
    def maxArea(self, height):
        """双指针
        指针移动依据是移动高度低的那一个（记为 a），
        如果移动高的那一个（记为 b）的话，可能会有两种情况：
        1. 新的 b' 满足 b' < a < b，因为距离减小，且面积取决于低的那个，面积必定减小
        2. 新的 b' 满足 a < b' < b，因为距离减小，且面积取决于低的那个，面积必定减小
        3. 新的 b' 满足 a < b < b'，因为距离减小，且面积取决于低的那个，面积必定减小
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height)-1
        max_area = -float('inf')

        while l < r:
            max_area = max(max_area, (r-l)*min(height[l], height[r]))

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area
