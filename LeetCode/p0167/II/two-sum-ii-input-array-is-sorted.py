# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: two-sum-ii-input-array-is-sorted.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-09 23:41:25
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************

class Solution(object):
    def twoSum(self, numbers, target):
        """双指针
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        while (i < j):
            val = numbers[i] + numbers[j]

            if val == target:
                return [i+1, j+1]
            elif val < target:
                i = i + 1
            else:
                j = j - 1
