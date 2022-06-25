# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: palindrome-partitioning.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 14:31:24
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s`, partition `s` such that every
# substring of the partition is a **palindrome**. Return all possible
# palindrome partitioning of `s`.
#
# A **palindrome** string is a string that reads the same backward as
# forward.
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
# Constraints:
# *   `1 <= s.length <= 16`
# *   `s` contains only lowercase English letters.
# ********************************************************************************


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        return self.dfs(s, 0, [], [])

    def dfs(self, s, left, partition, partitions):
        if left == len(s):
            partitions.append(partition)
            return partitions[:]

        res = []
        for right in range(left, len(s)):
            if self.is_palindrome(s, left, right):
                res.extend(self.dfs(s, right+1, partition+[s[left:right+1]], partitions[:]))

        return res

    def is_palindrome(self, s, left, right):
        if left >= right:
            return True
        return self.is_palindrome(s, left + 1, right - 1) if s[left] == s[right] else False
