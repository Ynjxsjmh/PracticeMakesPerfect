# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: partition-to-k-equal-sum-subsets.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-21 19:23:25
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` and an integer `k`,
# return `true` if it is possible to divide this array into `k`
# non-empty subsets whose sums are all equal.
#
# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4),
# (2,3), (2,3) with equal sums.
#
# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false
#
# Constraints:
# *   `1 <= k <= nums.length <= 16`
# *   `1 <= nums[i] <= 104`
# *   The frequency of each element is in the range `[1, 4]`.
# ********************************************************************************


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        以二进制 state 的形式表示数组中每个数字的划分情况，
        - 第 i 位为 1 表示第 i 个数字已被划分；
        - 第 i 位为 0 表示第 i 个数字未被划分。
        注：二进制的位数是从右往左算的
        比如对 nums=[1,2,3,4] 来说，二进制 state=0011 表示选取划分数字 [1,2]
        因此，state=0 时，表示任何一个数字均未被划分；而 state=2^{n}-1 时，表示所有数字均已被划分。
        由于题意说明 1 <= nums.length <= 16，因此 state 的最大值在 2^{16}-1 范围内，可以用整数表示。

        记 dp[state] 表示数组划分状态为 state 时已被划分的数字总和，
        初始时 dp[state] = -1，值为 -1 表示当前 state 不是由之前的 state 变化而来；
        dp[0] 表示任何一个数字均未被划分，因此初始化为 1；
        若最终状态 dp[2^{n}-1] % target = 0，说明可将数组划分为 k 个等和子集。

        假设当前 state = 01010，对当前 state 进行转移有三个方法：
        1. 将第 i 位置 1：state | (1<<i)。假如 i = 0
           (1<<i) = 00001
           01010 | 00001 = 01011
        2. 将第 i 位置 0：state & !(1<<i)。假如 i = 1
           (1<<i) = 00010
           !(1<<i) = 11101
           01010 & 11101 = 01000
        3. 检查第 i 位是否为 1：state & (1<<i)
           如果当前位是 1，结果为非 0 正数。假如 i = 3
           (1<<i) = 01000
           01010 & 01000 = 01000

        我们可以从空集合开始，一个一个的往符合题意的集合里添加元素，每一次只尝试添加一个数。

        如果当前集合里所有元素的和，模target 加上当前考虑的一个数 num 以后的和小于等于每个划分的平均数 target，
        那么加上当前考虑的数的子集有可能是满足题意的一个或者多个划分，否则就一定不是满足题意的一个或者多个划分。

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        total = sum(nums)
        target = total // k

        # total 不是 k 的倍数
        if total % k != 0:
            return False

        # 若最大数字超过 target
        if max(nums) > target:
            return False

        dp = [-1] * pow(2, len(nums))
        dp[0] = 0

        for state in range(0, pow(2, len(nums))):
            if dp[state] == -1:
                continue
            for i in range(len(nums)):
                # 当前没有选中第 i 位
                if((state & (1 << i)) == 0):
                    if((dp[state] % target + nums[i]) <= target):
                        # 将第 i 位置 1
                        dp[state | 1<<i] = dp[state] + nums[i];

        return dp[-1] == total
