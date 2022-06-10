# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: 3sum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-10 10:12:45
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 3:
# Input: nums = [0]
# Output: []
# ********************************************************************************

class Solution(object):
    def threeSum(self, nums):
        """排序好，固定一个数，变成 twoSum 双指针
        利用 set() 保持结果唯一
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = list(sorted(nums))
        res = set()

        for i in range(len(nums)-2):
            lo = i + 1
            hi = len(nums) - 1
            while (lo < hi):
                lst = (nums[i], nums[lo], nums[hi])
                target = sum(lst)

                if target == 0:
                    res.add(lst)
                    lo += 1
                    hi -= 1
                elif target > 0:
                    hi -= 1
                else:
                    lo += 1

        return list(res)
