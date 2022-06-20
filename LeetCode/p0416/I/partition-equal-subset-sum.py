# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: partition-equal-subset-sum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-21 02:07:00
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a **non-empty** array `nums` containing **only
# positive integers**, find if the array can be partitioned into two
# subsets such that the sum of elements in both subsets is equal.
#
# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
# Constraints:
# *   `1 <= nums.length <= 200`
# *   `1 <= nums[i] <= 100`
# ********************************************************************************

class Solution(object):
    def canPartition(self, nums):
        """原数组所有数字和一定是偶数，否则无法拆成两个和相同的子集合
        算出原数组的数字之和，然后除以 2，就是 target
        问题就转换为能不能找到一个非空子集合，使得其数字之和为 target
        1. 数组和为奇数，不可能
        2. 数组和为偶数
           2.1 数组里最大的数比 target 大，不可能
           2.2 0-1 背包动态规划

        dp[i][j] 表示从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个），
        是否存在一种选取方案使得被选取的正整数的和等于 j（0 <= j <= target）

        边界情况：
        1. 如果不选取任何正整数，则被选取的正整数等于 0。因此对于所有 0≤i<n，都有 dp[i][0]=true。
        2. 当 i==0 时，只有一个正整数 nums[0] 可以被选取，因此 dp[0][nums[0]]=true。

        对于 i>0 且 j>0 的情况，如何确定 dp[i][j] 的值？需要分别考虑以下两种情况：

        1. 如果 j<nums[i]，则在选取的数字的和等于 j 的情况下无法选取当前的数字 nums[i]，
           因此有 dp[i][j] = dp[i−1][j]。
        2. 如果 j ≥ nums[i]，则对于当前的数字 nums[i]，可以选取也可以不选取，
           因此两种情况只要有一个为 true，就有 dp[i][j]=true：
           1. 如果不选取 nums[i]，则 dp[i][j]=dp[i−1][j]；
           2. 如果选取 nums[i]，则 dp[i][j]=dp[i−1][j−nums[i]]。

        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        target = total // 2

        if total % 2:
            return False

        if max(nums) > target:
            return False

        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(1, target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

        return dp[-1][-1]
