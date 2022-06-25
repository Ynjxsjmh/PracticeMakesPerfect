# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: letter-combinations-of-a-phone-number.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 16:06:36
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a string containing digits from `2-9` inclusive,
# return all possible letter combinations that the number could
# represent. Return the answer in **any order**.
#
# A mapping of digits to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
# *   `0 <= digits.length <= 4`
# *   `digits[i]` is a digit in the range `['2', '9']`.
# ********************************************************************************


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        lookup = {
            '2': 'abc',  '3': 'def',
            '4': 'ghi',  '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if len(digits) == 0:
            return []

        return self.dfs(digits, lookup, 0, '', [])

    def dfs(self, digits, lookup, idx, combination, combinations):
        if len(combination) == len(digits):
            combinations.append(combination)
            return combinations[:]

        res = []
        for i in range(idx, len(digits)):
            for char in lookup[digits[i]]:
                res.extend(self.dfs(digits, lookup, i+1, combination+char, combinations[:]))

        return res
