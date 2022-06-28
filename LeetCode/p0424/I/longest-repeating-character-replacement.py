# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-repeating-character-replacement.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-28 13:36:20
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given a string `s` and an integer `k`. You can
# choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most
# `k` times.
#
# Return *the length of the longest substring containing the same
# letter you can get after performing the above operations*.
#
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
# Constraints:
# *   `1 <= s.length <= 105`
# *   `s` consists of only uppercase English letters.
# *   `0 <= k <= s.length`
# ********************************************************************************


class Solution(object):
    def characterReplacement(self, s, k):
        """用字典记录滑动窗口内各字符的频数
        滑动窗口 [l, r] 保证窗口内经过 k 次替换能变成单一字符
        每次窗口右侧右移时，将新字符加进字典中，
        1. 新字符和原来频数最大的字符相同
           最长重复字符长度增加
        2. 新字符和原来频数最大的字符不同
           比较当前窗口长度，窗口内最大频数和可替换次数
           2.1 如果可替换次数不足，窗口左侧右移，更新字典
           2.2 如果可替换次数足够，窗口右侧继续右移
        :type s: str
        :type k: int
        :rtype: int
        """

        if (len(s) <= 1) :
            return len(s)

        l, r= 0, 0
        max_len, max_freq = 0, 0
        freq = defaultdict(lambda: 0)

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            if (r - l + 1) <= (max_freq + k):
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                freq[s[l]] -= 1
                # freq[s[r]] 应该不更新，但是下次循环却更新了；
                # 因此这里先减去 1
                freq[s[r]] -= 1
                l += 1

        return max_len
