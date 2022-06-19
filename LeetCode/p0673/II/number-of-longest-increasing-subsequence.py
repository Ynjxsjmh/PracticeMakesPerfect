# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: number-of-longest-increasing-subsequence.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 16:06:44
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums`, return *the number of
# longest increasing subsequences.*
#
# **Notice** that the sequence has to be **strictly** increasing.
#
# Example 1:
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4,
# 7] and [1, 3, 5, 7].
#
# Example 2:
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1,
# and there are 5 increasing subsequences of length 1, so output 5.
#
# Constraints:
# *   `1 <= nums.length <= 2000`
# *   `-106 <= nums[i] <= 106`
# ********************************************************************************


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        状态定义：
        dp[i]  表示以 nums[i] 结尾的最长上升子序列的长度
        cnt[i] 表示以 nums[i] 结尾的最长上升子序列的个数
        状态转移方程：
        dp[i] = max(dp[j])+1, 其中 0≤j<i 且 num[j]<num[i]
        max(dp[j]) 用以寻找在 [0,i) 间的最长上升子序列
        cnt[i] = 所有满足 dp[j]+1=dp[i] 的 cnt[j] 之和
        :type nums: List[int]
        :rtype: int
        """

        dp = [1] * len(nums)
        cnt = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 最长递增子序列的长度增加了
                    if dp[j] + 1 > dp[i]:
                        # 长度增加，数量不变
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    # 最长递增子序列的长度没有增加，但出现了长度一样的情况
                    elif dp[j] + 1 == dp[i]:
                        # 数量增加
                        cnt[i] += cnt[j]

        return sum([cnt[i] for i, length in enumerate(dp) if length == max(dp)])
