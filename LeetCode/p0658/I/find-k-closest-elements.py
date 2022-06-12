# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-k-closest-elements.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 13:39:24
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a **sorted** integer array `arr`, two integers
# `k` and `x`, return the `k` closest integers to `x` in the
# array. The result should also be sorted in ascending order.
#
# An integer `a` is closer to `x` than an integer `b` if:
# *   `|a - x| < |b - x|`, or
# *   `|a - x| == |b - x|` and `a < b`
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
#
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
# Constraints:
# *   `1 <= k <= arr.length`
# *   `1 <= arr.length <= 104`
# *   `arr` is sorted in **ascending** order.
# *   `-104 <= arr[i], x <= 104`
# ********************************************************************************

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """双指针
        相当于在长度为 n 的数组中去掉 n-k 个数字，
        且去掉的顺序肯定是从两头开始去，因为距离 x 最远的数字肯定在首尾出现
        每次比较首尾两个数字跟 x 的距离，将距离大的那个数字删除，
        直到剩余的数组长度为 k 为止
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        res = [abs(val-x) for val in arr]

        l = 0
        r = len(res)

        while r - l > k:
            if res[l] > res[r-1]:
                l += 1
            else:
                r -= 1

        return arr[l:r]
