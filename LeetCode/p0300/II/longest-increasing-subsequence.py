# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-increasing-subsequence.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 09:59:09
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums`, return the length of the
# longest strictly increasing subsequence.
#
# A **subsequence** is a sequence that can be derived from an array by
# deleting some or no elements without changing the order of the
# remaining elements. For example, `[3,6,2,7]` is a subsequence of the
# array `[0,3,1,6,2,2,7]`.
#
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101],
# therefore the length is 4.
#
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
# Constraints:
# *   `1 <= nums.length <= 2500`
# *   `-104 <= nums[i] <= 104`
# ********************************************************************************


class Solution(object):
    def lengthOfLIS(self, nums):
        """定义 dp[i] 为考虑前 ii 个元素，以第 i 个数字结尾的最长上升子序列的长度
        注意 nums[i] 必须被选取
        状态转移方程：
        dp[i]=max(dp[j])+1, 其中 0≤j<i 且 num[j]<num[i]
        :type nums: List[int]
        :rtype: int
        """

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = max([dp[j]+1 if nums[i] > nums[j] else 1 for j in range(0, i)])

        return max(dp)
