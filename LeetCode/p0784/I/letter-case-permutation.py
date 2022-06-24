# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: letter-case-permutation.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 00:22:34
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string `s`, you can transform every letter
# individually to be lowercase or uppercase to create another string.
#
# Return *a list of all possible strings we could create*. Return the
# output in **any order**.
#
# Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#
# Example 2:
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
#
# Constraints:
# *   `1 <= s.length <= 12`
# *   `s` consists of lowercase English letters, uppercase English letters, and digits.
# ********************************************************************************



class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        return self.dfs(s, 0, '', [])

    def dfs(self, s, idx, permutation, permutations):
        if idx == len(s):
            permutations.append(permutation)
            return permutations[:]

        if not s[idx].isalpha():
            return self.dfs(s, idx+1, permutation+s[idx], permutations[:])

        lower = self.dfs(s, idx+1, permutation+s[idx].lower(), permutations[:])
        upper = self.dfs(s, idx+1, permutation+s[idx].upper(), permutations[:])

        return lower + upper
