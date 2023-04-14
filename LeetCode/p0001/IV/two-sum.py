# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: two-sum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 16:09:38
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lookup = dict()

        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

        return []
