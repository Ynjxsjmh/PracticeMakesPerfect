# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: valid-parentheses.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-18 16:07:46
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s` containing just the characters
# `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input
# string is valid.
#
# An input string is valid if:
# 1.  Open brackets must be closed by the same type of brackets.
# 2.  Open brackets must be closed in the correct order.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Constraints:
# *   `1 <= s.length <= 104`
# *   `s` consists of parentheses only `'()[]{}'`.
# ********************************************************************************


class Solution(object):
    # 思路不对，写成把 "([)]" 当作合法的了
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        m = {
            '(': [],
            '[': [],
            '{': [],
        }

        b = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for ch in s:
            if ch in m:
                m[ch].append(ch)
            else:
                if len(m[b[ch]]) <= 0:
                    return False
                else:
                    m[b[ch]].pop()

        for k in m:
            if len(m[k]) != 0:
                return False

        return True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        m = []

        b = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for ch in s:
            if ch in b.values():
                m.append(ch)
            else:
                if len(m) <= 0:
                    return False
                else:
                    v = m.pop()
                    if v != b[ch]:
                        return False

        return len(m) == 0
