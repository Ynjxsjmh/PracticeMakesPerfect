# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: longest-substring-without-repeating-character.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-02 15:33:32
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s`, find the length of the **longest
# substring** without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# *   `0 <= s.length <= 5 * 104`
# *   `s` consists of English letters, digits, symbols and spaces.
# ********************************************************************************



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """用两个指针维护一个滑动窗口，并记录窗口内的字符
        :type s: str
        :rtype: int
        """

        record = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            if s[r] not in record:
                record.add(s[r])
                max_len = max(max_len, len(record))
                r += 1
            else:
                record.remove(s[l])
                l += 1

        return max_len
