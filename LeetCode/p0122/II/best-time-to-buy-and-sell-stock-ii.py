# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: best-time-to-buy-and-sell-stock-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-28 18:13:23
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an integer array `prices` where
# `prices[i]` is the price of a given stock on the `ith` day.
#
# On each day, you may decide to buy and/or sell the stock. You can
# only hold **at most one** share of the stock at any time. However,
# you can buy it then immediately sell it on the **same day**.
#
# Find and return *the **maximum** profit you can achieve*.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never
# buy the stock to achieve the maximum profit of 0.
#
# Constraints:
# *   `1 <= prices.length <= 3 * 104`
# *   `0 <= prices[i] <= 104`
# ********************************************************************************


class Solution(object):
    def maxProfit(self, prices):
        """记录两个状态：
        1. 第 i 天交易结束后，有一支股票的最大利润
        2. 第 i 天交易结束后，没有股票的最大利润

        那么状态转移方程的分析过程如下：
        - 如果第 i 天交易结束后，有一支股票
          1. 第 i-1 天交易结束后，没有股票；在第 i 天买的股票
          2. 第 i-1 天交易结束后，有股票；第 i 天什么都没做

        - 如果第 i 天交易结束后，没有股票
          1. 第 i-1 天交易结束后，有一支股票；在第 i 天卖了该股票
          2. 第 i-1 天交易结束后，没有股票；在第 i 天什么都没做
        :type prices: List[int]
        :rtype: int
        """

        buy  = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0]  = -prices[0]
        sell[0] = 0

        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], sell[i-1]-prices[i])
            sell[i] = max(buy[i-1]+prices[i], sell[i-1])

        return max(buy[-1], sell[-1])
