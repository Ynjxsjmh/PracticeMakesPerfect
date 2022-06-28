# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: best-time-to-buy-and-sell-stock-iii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-28 18:48:34
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an array `prices` where `prices[i]` is
# the price of a given stock on the `ith` day.
#
# Find the maximum profit you can achieve. You may complete **at most
# two transactions**.
#
# **Note:** You may not engage in multiple transactions simultaneously
# **(i.e., you must sell the stock before you buy again).
#
# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
# profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later,
# as you are engaging multiple transactions at the same time. You must
# sell before buying again.
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
# Constraints:
# *   `1 <= prices.length <= 105`
# *   `0 <= prices[i] <= 105`
# ********************************************************************************


class Solution(object):
    def maxProfit(self, prices):
        """
        定义状态为第 i 天结束时，是否持股以及卖出的次数时的最大利润
        dp[天数][当前是否持股][卖出的次数]

        - 第 i 天结束时，不持有股票，一次都没有卖出。dp[i][0][0]
          1. 因为一次都没有买入卖出，所以利润为 0

        - 第 i 天结束时，不持有股票，卖出过 1 次。dp[i][0][1]
          1. 第 i-1 天结束时，有股票；第 i 天卖出了股票。dp[i-1][1][0]+prices[i]
          2. 第 i-1 天结束时，没有股票，卖出过 1 次；第 i 天什么都没做。dp[i-1][0][1]

        - 第 i 天结束时，不持有股票，卖出过 2 次。dp[i][0][2]
          1. 第 i-1 天结束时，有股票；第 i 天卖出了股票。dp[i-1][1][1]+prices[i]
          2. 第 i-1 天结束时，没有股票，卖出过 2 次；第 i 天什么都没做。dp[i-1][0][2]

        - 第 i 天结束时，持有股票，一次都没有卖出。dp[i][1][0]
          1. 第 i-1 天结束时，没有股票；第 i 天买了一支股票。dp[i-1][0][0]-prices[i]
          2. 第 i-1 天结束时，有股票；第 i 天什么都没做。dp[i-1][1][0]

        - 第 i 天结束时，持有股票，卖出过一次。dp[i][1][1]
          1. 第 i-1 天结束时，没有股票；第 i 天买了一支股票。dp[i-1][0][1]-prices[i]
          2. 第 i-1 天结束时，有股票；第 i 天什么都没做。dp[i-1][1][1]

        - 第 i 天结束时，持有股票，卖出过两次。dp[i][1][2]
          1. 不可能存在，因为最多交易两次。如果卖两次还持有的话，就买了三次了。
        :type prices: List[int]
        :rtype: int
        """

        dp = [[[0 for _ in range(3)] for _ in [0, 1]] for _ in range(len(prices))]

        dp[0][0][0] = 0             # 第 0 天结束时，不持有股票，一次都没有卖出
        dp[0][1][0] = -prices[0]    # 第 0 天结束时，持有股票，一次都没有卖出
        dp[0][0][1] = -float('inf') # 第 0 天结束时，不持有股票，卖出过一次（不允许当天买，当天卖）
        dp[0][1][1] = -float('inf') # 第 0 天结束时，持有股票，卖出过一次
        dp[0][0][2] = -float('inf') # 第 0 天结束时，不持有股票，卖出过两次
        dp[0][1][2] = -float('inf') # 第 0 天结束时，持有股票，卖出过两次

        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = max(dp[i-1][1][0]+prices[i], dp[i-1][0][1])
            dp[i][0][2] = max(dp[i-1][1][1]+prices[i], dp[i-1][0][2])
            dp[i][1][0] = max(dp[i-1][0][0]-prices[i], dp[i-1][1][0])
            dp[i][1][1] = max(dp[i-1][0][1]-prices[i], dp[i-1][1][1])
            dp[i][1][2] = -float('inf')

        return max(dp[-1][0]+[0])
