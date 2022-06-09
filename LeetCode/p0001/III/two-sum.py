# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: two-sum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-09 22:29:12
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

        d = {}

        for i, num in enumerate(nums):
            val = target - num

            if num in d:
                return [d[num], i]
            else:
                d[val] = i


if __name__ == '__main__':
    solution = Solution()

    print(solution.twoSum([2,7,11,15], 9)) # [0,1]
