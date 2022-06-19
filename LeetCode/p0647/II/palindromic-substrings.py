# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: palindromic-substrings.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 14:43:45
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s`, return *the number of **palindromic
# substrings** in it*.
#
# A string is a **palindrome** when it reads the same backward as
# forward.
#
# A **substring** is a contiguous sequence of characters within the string.
#
# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Constraints:
# *   `1 <= s.length <= 1000`
# *   `s` consists of lowercase English letters.
# ********************************************************************************


class Solution(object):
    def countSubstrings(self, s):
        """dp[i][j] 用来表示 [i, j] 区间内的子字符串是否为回文串
        状态转移方程为：
        dp[i][j] = 1                             if i == j
                 = s[i] == s[j]                  if j = i+1
                 = s[i] == s[j] && dp[i+1][j-1]  if j > i+1
        :type s: str
        :rtype: int
        """

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        cnt = 0

        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = True
                    cnt += 1
                elif (j - i == 1) and (s[i] == s[j]):
                    dp[i][j] = True
                    cnt += 1
                elif (j - i > 1) and (s[i] == s[j]) and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    cnt += 1

        return cnt
