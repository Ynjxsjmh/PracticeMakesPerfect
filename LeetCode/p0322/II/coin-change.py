# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: coin-change.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-18 14:35:41
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an integer array `coins` representing
# coins of different denominations and an integer `amount`
# representing a total amount of money.
#
# Return *the fewest number of coins that you need to make up that
# amount*. If that amount of money cannot be made up by any combination
# of the coins, return `-1`.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
#
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
#
# Constraints:
# *   `1 <= coins.length <= 12`
# *   `1 <= coins[i] <= 231 - 1`
# *   `0 <= amount <= 104`
# ********************************************************************************

class Solution(object):
    def coinChange(self, coins, amount):
        """
        dp[i] 定义为 amount 为 i 时需要的最小硬币数
        观察得到：
        amount == i 可以由 amount == i-1 加一个硬币 1 得来
        amount == i 可以由 amount == i-2 加一个硬币 2 得来
        由此推出
        amount == i 可以由 amount == i-coin 加一个硬币 coin 得来
        状态转移方程：
        dp[i] = min(dp[i-coin])+1  coin in coins
        如果 coin 均比 amount == i 大，说明没有硬币组合，用特殊状态表示
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [0] * (amount+1)

        for i in range(1, amount+1):
            dp[i] = min([dp[i-coin] if i-coin >= 0 else float('inf') for coin in coins]) + 1

        return -1 if dp[amount] == float('inf') else dp[amount]
