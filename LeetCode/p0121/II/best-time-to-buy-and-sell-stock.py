# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: best-time-to-buy-and-sell-stock.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-28 18:00:38
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an array `prices` where `prices[i]` is
# the price of a given stock on the `ith` day.
#
# You want to maximize your profit by choosing a **single day** to buy
# one stock and choosing a **different day in the future** to sell that
# stock.
#
# Return *the maximum profit you can achieve from this transaction*. If
# you cannot achieve any profit, return `0`.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Constraints:
# *   `1 <= prices.length <= 105`
# *   `0 <= prices[i] <= 104`
# ********************************************************************************


class Solution(object):
    def maxProfit(self, prices):
        """假设当前在第 i 天，需要判断当天前卖出的最大利润
        那么需要记录 [0, i) 间的最小值
        :type prices: List[int]
        :rtype: int
        """

        cur_min = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > cur_min:
                max_profit = max(max_profit, prices[i]-cur_min)
            else:
                cur_min = prices[i]

        return max_profit
