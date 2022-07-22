# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: majority-element.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-22 15:22:18
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array `nums` of size `n`, return *the majority
# element*.
#
# The majority element is the element that appears more than `⌊n / 2⌋`
# times. You may assume that the majority element always exists in the
# array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# *  `n == nums.length`
# *  `1 <= n <= 5  104`
# *  `-109 <= nums[i] <= 109`
#
# **Follow-up:** Could you solve the problem in linear time and in `O(1)` space?
# ********************************************************************************


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = None
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                res = None

            if res == None:
                res = nums[i]
                cnt = 1
            elif res != nums[i]:
                cnt -= 1
            elif res == nums[i]:
                cnt += 1

        return res
