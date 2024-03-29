# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-all-duplicates-in-an-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-25 14:33:03
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` of length `n` where all
# the integers of `nums` are in the range `[1, n]` and each integer
# appears **once** or **twice**, return *an array of all the integers
# that appears **twice***.
#
# You must write an algorithm that runs in `O(n) `time and uses only constant extra space.
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
#
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
#
# Example 3:
# Input: nums = [1]
# Output: []
#
# Constraints:
# *   `n == nums.length`
# *   `1 <= n <= 105`
# *   `1 <= nums[i] <= n`
# *   Each element in `nums` appears **once** or **twice**.
# ********************************************************************************



class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        ans = []

        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(nums[i])

        return ans
