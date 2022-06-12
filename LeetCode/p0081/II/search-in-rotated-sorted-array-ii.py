# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: search-in-rotated-sorted-array-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 13:00:01
# Last Updated: 
#           By: Ynjxsjmh
# Description: There is an integer array `nums` sorted in
# non-decreasing order (not necessarily with **distinct** values).
#
# Before being passed to your function, `nums` is **rotated** at an
# unknown pivot index `k` (`0 <= k < nums.length`) such that the
# resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0],
# nums[1], ..., nums[k-1]]` (**0-indexed**). For example,
# `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and
# become `[4,5,6,6,7,0,1,2,4,4]`.
#
# Given the array `nums` **after** the rotation and an integer
# `target`, return `true` *if* `target` *is in* `nums`*, or* `false`
# *if it is not in* `nums`*.*
#
# You must decrease the overall operation steps as much as possible.
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Constraints:
# *   `1 <= nums.length <= 5000`
# *   `-104 <= nums[i] <= 104`
# *   `nums` is guaranteed to be rotated at some pivot.
# *   `-104 <= target <= 104`
# ********************************************************************************


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) / 2

            if target == nums[m]:
            #Judging more makes faster
            #if target in [nums[m], nums[l], nums[r-1]]:
                return True
            elif nums[m] > nums[r-1]:
                # [l, m] 有序
                if nums[l] <= target & target < nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r-1]:
                # [m, r] 有序
                if nums[m] < target & target <= nums[r-1]:
                    l = m + 1
                else:
                    r = m
            else:
                r = r - 1

        return False
