# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: peak-index-in-a-mountain-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-11 16:42:36
# Last Updated: 
#           By: Ynjxsjmh
# Description: Let's call an array `arr` a **mountain** if the
# following properties hold:
# `arr.length >= 3`
# There exists some `i` with `0 < i < arr.length - 1` such that:
#     `arr[0] < arr[1] < ... arr[i-1] < arr[i]`
#     `arr[i] > arr[i+1] > ... > arr[arr.length - 1]`
#
# Given an integer array `arr` that is guaranteed to be a mountain,
# return any `i` such that `arr[0] < arr[1] < ... arr[i - 1] < arr[i] >
# arr[i + 1] > ... > arr[arr.length - 1]`.
#
# Example 1:
# Input: arr = [0,1,0]
# Output: 1
#
# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1
#
# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1
#
# Constraints:
#    `3 <= arr.length <= 104`
#    `0 <= arr[i] <= 106`
#    `arr` is guaranteed to be a mountain array.
# ********************************************************************************

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """遍历一遍，用一个变量存当前最大的索引
        :type arr: List[int]
        :rtype: int
        """

        m = 0

        for i, val in enumerate(arr[1:]):
            if val > arr[m]:
                m = i + 1

        return m

    def peakIndexInMountainArray(self, arr):
        """二分查找
        :type arr: List[int]
        :rtype: int
        """

        l = 0
        r = len(arr)

        while l < r:
            m = l + (r - l) / 2

            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m

        return l
