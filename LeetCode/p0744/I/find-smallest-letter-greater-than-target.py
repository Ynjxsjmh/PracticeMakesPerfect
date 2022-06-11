# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: find-smallest-letter-greater-than-target.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-11 15:23:19
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a characters array `letters` that is sorted in
# **non-decreasing** order and a character `target`, return *the
# smallest character in the array that is larger than* `target`.
#
# Note that the letters wrap around.
#   For example, if `target == 'z'` and `letters == ['a', 'b']`, the answer is `'a'`.
#
# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#
# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#
# Example 3:
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#
# Constraints:
#    `2 <= letters.length <= 104`
#    `letters[i]` is a lowercase English letter.
#    `letters` is sorted in non-decreasing order.
#    `letters` contains at least two different characters.
#    `target` is a lowercase English letter.
# ********************************************************************************


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """从头搜到尾
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        for letter in letters:
            if letter > target:
                return letter

        return letters[0]

    def nextGreatestLetter(self, letters, target):
        """二分查找
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        lo = 0
        hi = len(letters)

        while lo < hi:
            mid = lo + (hi - lo) / 2

            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid

        return letters[lo % len(letters)]
