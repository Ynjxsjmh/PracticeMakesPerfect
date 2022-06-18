# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-palindromic-substring.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 00:49:54
# Last Updated:
#           By: Ynjxsjmh
# Description:  Given a  string `s`,  return *the  longest palindromic
# substring* in `s`.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
# *   `1 <= s.length <= 1000`
# *   `s` consist of only digits and English letters.
# ********************************************************************************


class Solution(object):
    # Time Limit Exceeded 114/180
    def longestPalindrome(self, s):
        """定义 dp[i][j] 表示区间 [i,j] 是否为回文串
        状态转移方程为：
        dp[i][j] = 1                             if i == j
                 = s[i] == s[j]                  if j = i+1
                 = s[i] == s[j] && dp[i+1][j-1]  if j > i+1
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[False for j in range(l)] for i in range(l)]

        for i in range(l):
            for j in range(i, l):
                dp[i][i] = True
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]

        for j in range(2, l):
            for i in range(0, j-1):
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])

        left = 0
        max_len = 1

        for j in range(l):
            for i in range(0, j+1):
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    left = i

        return s[left:(left+max_len)]

    # Time Limit Exceeded 106/180
    def longestPalindrome(self, s):
        """定义 dp[i][j] 表示区间 [i,j] 是否为回文串
        状态转移方程为：
        dp[i][j] = 1                             if i == j
                 = s[i] == s[j]                  if j = i+1
                 = s[i] == s[j] && dp[i+1][j-1]  if j > i+1
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[False for j in range(l)] for i in range(l)]

        left = 0
        max_len = 1

        for j in range(l):
            dp[j][j] = True
            for i in range(l):
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]
                if j > 1 and i < j-1:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    left = i

        return s[left:(left+max_len)]

    # Time Limit Exceeded 146/180
    def longestPalindrome(self, s):
        """定义 dp[i][j] 表示区间 [i,j] 是否为回文串
        状态转移方程为：
        dp[i][j] = 1                             if i == j
                 = s[i] == s[j]                  if j = i+1
                 = s[i] == s[j] && dp[i+1][j-1]  if j > i+1
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[False for j in range(l)] for i in range(l)]

        left = 0
        max_len = 1

        for j in range(l):
            dp[j][j] = True
            for i in range(j):  # <--- changes here
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]
                if j > 1 and i < j-1:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    left = i

        return s[left:(left+max_len)]

    # Time Limit Exceeded 166/180
    def longestPalindrome(self, s):
        """定义 dp[i][j] 表示区间 [i,j] 是否为回文串
        状态转移方程为：
        dp[i][j] = 1                             if i == j
                 = s[i] == s[j]                  if j = i+1
                 = s[i] == s[j] && dp[i+1][j-1]  if j > i+1
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[False for j in range(l)] for i in range(l)]

        left = 0
        max_len = 1

        for j in range(l):
            dp[j][j] = True
            for i in range(j):
                dp[i][j] = (s[i] == s[j] and (j-i<2 or dp[i+1][j-1]));

                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    left = i

        return s[left:(left+max_len)]

    # Time Limit Exceeded
    def longestPalindrome(self, s):
        """定义 dp[i][j] 表示区间 [i,j] 是否为回文串
        状态转移方程为：
        dp[i][j] = 1                             if i == j
                 = s[i] == s[j]                  if j = i+1
                 = s[i] == s[j] && dp[i+1][j-1]  if j > i+1
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[False for j in range(l)] for i in range(l)]

        left = 0
        max_len = 1

        for j in range(l):
            dp[j][j] = True
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    left = i

        return s[left:(left+max_len)]

