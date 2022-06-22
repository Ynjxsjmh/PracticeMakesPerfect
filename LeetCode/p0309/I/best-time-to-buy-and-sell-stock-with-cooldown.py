# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: best-time-to-buy-and-sell-stock-with-cooldown.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-23 02:07:27
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an array `prices` where `prices[i]` is
# the price of a given stock on the `ith` day.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the
# stock multiple times) with the following restrictions:
#
# *   After you sell your stock, you cannot buy stock on the next day
#     (i.e., cooldown one day).
#
# **Note:** You may not engage in multiple transactions simultaneously
# i.e., you must sell the stock before you buy again).
#
# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
# Example 2:
# Input: prices = [1]
# Output: 0
#
# Constraints:
# *   `1 <= prices.length <= 5000`
# *   `0 <= prices[i] <= 1000`
# ********************************************************************************


class Solution(object):
    def maxProfit(self, prices):
        """定义三个状态：
        buy[i] 表示在第 i 天结束后持有一支股票，在第 i 天的最大收益。
        sell[i] 表示在第 i 天结束后不持有股票，且处于冷冻期，在第 i 天的最大收益。
        rest[i] 表示在第 i 天结束后不持有股票，不处于冷冻期，在第 i 天的最大收益。
        “第 i 天结束后”意味着在第 i 天已经发生了买、卖和冷却这三个操作之一。
        「处于冷冻期」指的是在第 i 天结束之后的状态。即如果第 i 天结束之后处于冷冻期，那么第 i+1 天无法买入股票。

        状态转移方程：
        buy[i] 表示在第 i 天结束后持有一支股票，因此有两种可能：
        1. 买可能是在第 i 天进行的，此时需要在第 i-1 天进行了冷却，收益用 rest[i-1]-prices[i] 表示
        2. 买可能是在第 i 天开始之前进行的，即第 i-1 天结束后最后一个操作是买，收益用 buy[i-1] 表示

        sell[i] 表示在第 i 天结束后不持有股票，且处于冷冻期。说明需要在第 i 天当天卖掉股票，
        卖掉的条件是第 i-1 天结束后持有一支股票，收益用 buy[i-1]+prices[i] 表示

        rest[i] 表示在第 i 天结束后不持有股票，不处于冷冻期。说明第 i-1 天结束后就不持有股票了，可能
        1. 第 i-1 天当天处于冷冻期，第 i-1 天结束后退出冷冻期，第 i 天当天没有进行任何操作，收益用 rest[i-1] 表示
        2. 第 i-1 天当天卖掉股票，第 i 天进入冷冻期，第 i 天结束后退出冷冻期。收益用 sell[i-1] 表示
        3. 第 i-1 天当天不进行任何操作，第 i-1 天结束后不处于冷冻期，收益用 rest[i-1] 表示
        :type prices: List[int]
        :rtype: int
        """

        buy = [0] * len(prices)
        sell = [0] * len(prices)
        rest = [0] * len(prices)

        # 初始状态:
        ## 1: 第 0 天结束后持有一支股票，只有可能是买入
        buy[0] = -prices[0]

        ## 2. 第 0 天结束后不持有股票，且处于冷冻期。不存在此种情况。
        sell[0] = 0

        ## 3. 相当于没买入，收益自然为0
        rest[0] = 0

        for i in range(1, len(prices)):
            buy[i] = max(rest[i-1]-prices[i], buy[i-1])
            sell[i] = buy[i-1] + prices[i]
            rest[i] = max(rest[i-1], sell[i-1])

        return max(sell[-1], rest[-1])