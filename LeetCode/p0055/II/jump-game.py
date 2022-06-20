# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: jump-game.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-20 10:15:49
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an integer array `nums`. You are
# initially positioned at the array's **first index**, and each
# element in the array represents your maximum jump length at that
# position.
#
# Return `true` *if you can reach the last index, or* `false`
# *otherwise*.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum jump length is 0, which makes it impossible to reach the last
# index.
#
# Constraints:
# *   `1 <= nums.length <= 104`
# *   `0 <= nums[i] <= 105`
# ********************************************************************************


class Solution(object):
    # Time Limit Exceeded
    def canJump(self, nums):
        """dp[i] 表示是否能从 [0,i) 跳到 i
        能跳到 i 的条件是存在一个从 [0,i) 的某处+当时的最大跳力比 i 大
        dp[i] = any(j+nums[j]>=i)   0 <= j < i
        :type nums: List[int]
        :rtype: bool
        """

        dp = [False] * len(nums)
        dp[0] = True

        for i in range(1, len(nums)):
            dp[i] = any([j+nums[j] >= i if dp[j] else False for j in range(i)])

        return dp[-1]

    def canJump(self, nums):
        """dp[i] 表示达到 i 位置时剩余的跳力
        当前位置的剩余跳力（dp 值）和当前位置新的跳力中较大的决定了当前能到的最远距离
        下一个位置的剩余跳力（dp 值）就等于当前的这个较大值减去 1，因为需要花一个跳力到达下一个位置
        状态转移方程：
        dp[i] = max(dp[i-1], nums[i-1]) - 1
        :type nums: List[int]
        :rtype: bool
        """

        dp = [0] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if (dp[i] < 0): return False

        return True

    def canJump(self, nums):
        """dp[i] 表示在下标 i 处能够跳跃的最大值
        状态转移方程：
        dp[i] = max(dp[i-1]-1, nums[i])
        :type nums: List[int]
        :rtype: bool
        """

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] == 0: return False
            dp[i] = max(dp[i-1]-1, nums[i])

        return True
