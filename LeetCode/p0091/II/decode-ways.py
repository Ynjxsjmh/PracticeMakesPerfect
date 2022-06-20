# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: decode-ways.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-20 14:29:07
# Last Updated: 
#           By: Ynjxsjmh
# Description: A message containing letters from `A-Z` can be
# **encoded** into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
# To **decode** an encoded message, all the digits must be grouped then
# mapped back into letters using the reverse of the mapping above (there
# may be multiple ways). For example, `"11106"` can be mapped into:
#
# *   `"AAJF"` with the grouping `(1 1 10 6)`
# *   `"KJF"` with the grouping `(11 10 6)`
#
# Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be
# mapped into `'F'` since `"6"` is different from `"06"`.
#
# Given a string `s` containing only digits, return *the **number** of
# ways to **decode** it*.
#
# The test cases are generated so that the answer fits in a **32-bit**
# integer.
#
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
#
# Constraints:
# *   `1 <= s.length <= 100`
# *   `s` contains only digits and may contain leading zero(s).
# ********************************************************************************

class Solution(object):
    def numDecodings(self, s):
        """dp[i] 表示 [0,i] 个数字一共有多少种解码方式
        dp[0] 表示空字符串有多少种解码方式，
        因为空字符串可以解码成空字符串，初始化成 1 种
        dp[1] 表示第一个数字有多少种解码方式
        如果第一个数字是 0，就是 0 种，如果是 1 就是 1 种
        dp[i] 表示第 i 个数字有多少种解码方式
        第 i 个数字有两种解码方式：
        1. 第 i 个数字单独解码
        2. 第 i 个数字和第 i-1 个数字一起解码
        :type s: str
        :rtype: int
        """

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):
            # 判断第 i 个字符是否可以单独解码
            if s[i-1] != '0':
                # 第 i 个字符单独解码
                dp[i] = dp[i-1]

            # 判断第 i 个字符能否和第 i-1 个字符一起解码
            if (s[i-2] == '1') or (s[i-2] == '2' and s[i-1] <= '6'):
                dp[i] += dp[i-2]

        return dp[-1]
