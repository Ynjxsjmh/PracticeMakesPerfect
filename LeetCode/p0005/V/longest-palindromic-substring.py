# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-palindromic-substring.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-19 01:31:05
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s`, return *the longest palindromic
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
    def longestPalindrome(self, s):
        """中心扩散法：
        1. 往左扩散寻找与当前位置相同的字符，直到遇到不相等为止。
        2. 往右扩散寻找与当前位置相同的字符，直到遇到不相等为止。
        3. 左右双向扩散，直到左和右不相等
        :type s: str
        :rtype: str
        """

        l, r = 0, 0
        cur_len, max_len, max_l = 1, 0, 0

        for i in range(len(s)):
            l, r = i-1, i+1

            while l >= 0 and s[l] == s[i]:
                cur_len += 1
                l -= 1

            while r < len(s) and s[r] == s[i]:
                cur_len += 1
                r += 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len += 2
                l -= 1
                r += 1

            if cur_len > max_len:
                max_len = cur_len
                max_l = l

            cur_len = 1

        # 因为 l 是在原满足基础上继续 -1 才不满足条件，
        # 因此这里需要把不满足的 -1 加回来
        return s[max_l+1:max_l+max_len+1]
