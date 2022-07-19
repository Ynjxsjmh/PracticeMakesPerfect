# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: add-to-array-form-of-integer.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-19 22:59:40
# Last Updated: 
#           By: Ynjxsjmh
# Description: The **array-form** of an integer `num` is an array
# representing its digits in left to right order.
#
# *   For example, for `num = 1321`, the array form is `[1,3,2,1]`.
#
# Given `num`, the **array-form** of an integer, and an integer `k`,
# return *the **array-form** of the integer* `num + k`.
#
# Example 1:
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
# Example 2:
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
#
# Example 3:
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
# Constraints:
# *   `1 <= num.length <= 104`
# *   `0 <= num[i] <= 9`
# *   `num` does not contain any leading zeros except for the zero itself.
# *   `1 <= k <= 104`
# ********************************************************************************


class Solution(object):
    # Time Limit Exceeded
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        num = sum([n * pow(10, len(num)-i-1) for i, n in enumerate(num)]) + k
        res = []

        while num:
            res = [num % 10] + res
            num = num // 10

        return res

    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        i = len(num) - 1
        carry = 0

        while k or i >= 0 or carry:
            n1 = num[i] if i >= 0 else 0
            n2 = k % 10 if k else 0

            n = n1 + n2 + carry
            res = [n % 10] + res
            carry = n // 10

            i -= 1
            k = k // 10

        return res
