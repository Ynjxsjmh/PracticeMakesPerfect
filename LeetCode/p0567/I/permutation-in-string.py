# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: permutation-in-string.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-27 10:00:13
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given two strings `s1` and `s2`, return `true` *if*
# `s2` *contains a permutation of* `s1`*, or* `false` *otherwise*.
#
# In other words, return `true` if one of `s1`'s permutations is the
# substring of `s2`.
#
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
# Constraints:
# *   `1 <= s1.length, s2.length <= 104`
# *   `s1` and `s2` consist of lowercase English letters.
# ********************************************************************************


class Solution(object):
    def checkInclusion(self, s1, s2):
        """s1 的某个排列组合是 s2 的子串
        特点是 s1 的长度固定，词频不变
        因此用字典记录 s1 中词频与 s2 中 len(s1) 长度中词频的差异
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        l1 = len(s1)
        l2 = len(s2)
        diff = defaultdict(lambda: 0)

        if l1 > l2:
            return False

        for i in range(l1):
            diff[s1[i]] -= 1
            diff[s2[i]] += 1

        for i in range(l1, l2):
            if self.is_match(diff):
                return True

            diff[s2[i]] += 1
            diff[s2[i-l1]] -= 1

        return self.is_match(diff)

    def is_match(self, diff):
        for k, v in diff.items():
            if v != 0:
                return False

        return True
