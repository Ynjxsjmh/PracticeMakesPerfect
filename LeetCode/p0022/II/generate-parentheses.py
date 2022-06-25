# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: generate-parentheses.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 14:17:09
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given `n` pairs of parentheses, write a function to
# *generate all combinations of well-formed parentheses*.
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#
# Example 2:
# Input: n = 1
# Output: ["()"]
#
# Constraints:
# *   `1 <= n <= 8`
# ********************************************************************************


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        return self.dfs(n, 0, 0, '', [])

    def dfs(self, n, idx, left_cnt, combination, combinations):
        if idx == 2 * n and left_cnt == 0:
            combinations.append(combination)
            return combinations[:]

        if idx == 2 * n and left_cnt != 0:
            return combinations[:]

        left = self.dfs(n, idx+1, left_cnt+1, combination+'(', combinations[:])

        right = []
        if left_cnt > 0:
            right = self.dfs(n, idx+1, left_cnt-1, combination+')', combinations[:])

        return left + right
