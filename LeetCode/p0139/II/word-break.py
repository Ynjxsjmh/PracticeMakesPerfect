# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: word-break.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-19 10:20:17
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s` and a dictionary of strings
# `wordDict`, return `true` if `s` can be segmented into a
# space-separated sequence of one or more dictionary words.
#
# **Note** that the same word in the dictionary may be reused multiple
#   times in the segmentation.
#
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
# Constraints:
# *   `1 <= s.length <= 300`
# *   `1 <= wordDict.length <= 1000`
# *   `1 <= wordDict[i].length <= 20`
# *   `s` and `wordDict[i]` consist of only lowercase English letters.
# *   All the strings of `wordDict` are **unique**.
# ********************************************************************************


class Solution(object):
    def wordBreak(self, s, wordDict):
        """定义 dp[i] 表示字符串 s 区间 [0, i) 内的字符是否能被空格拆分成若干个字典中出现的单词
        状态转移方程：
        [0,i) 为 True 的条件是任意一个 [0,j) 以及 [j,i) 都在 wordDict 中
        dp[i]=dp[j] && check(s[j..i−1])  0 <= j <i
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]