# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: backspace-string-compare.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-01 08:41:08
# Last Updated:
#           By: Ynjxsjmh
# Description: Given two strings `s` and `t`, return `true` *if they
# are equal when both are typed into empty text editors*. `'#'` means
# a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
# Constraints:
# *   `1 <= s.length, t.length <= 200`
# *   `s` and `t` only contain lowercase letters and `'#'` characters.
# ********************************************************************************


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = len(s) - 1
        j = len(t) - 1
        cnt_s = 0
        cnt_t = 0

        while i >= 0 or j >= 0:
            # 找到第一个可以比较的字符
            while i >= 0:
                if s[i] == '#':
                    cnt_s += 1
                    i -= 1
                elif cnt_s > 0:
                    cnt_s -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    cnt_t += 1
                    j -= 1
                elif cnt_t > 0:
                    cnt_t -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True
