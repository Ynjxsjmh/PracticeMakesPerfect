# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: multiply-strings.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-17 02:35:09
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given two non-negative integers `num1` and `num2`
# represented as strings, return the product of `num1` and `num2`,
# also represented as a string.
#
# **Note:** You must not use any built-in BigInteger library or
# **convert the inputs to integer directly.
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
# Constraints:
# *   `1 <= num1.length, num2.length <= 200`
# *   `num1` and `num2` consist of digits only.
# *   Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.
# ********************************************************************************


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'

        res = '0'

        for i in range(len(num1)-1, -1, -1):
            carry = 0
            ir = ''.join(['0' for _ in range(len(num1)-1-i)])

            j = len(num2) - 1
            while j >= 0 or carry:
                value1 = int(num1[i])
                value2 = int(num2[j]) if j >= 0 else 0
                value = value1 * value2 + carry
                carry = value // 10
                ir = str(value % 10) + ir
                j -= 1

            res = self.add(res, ir)

        return res

    def add(self, num1, num2):
        nums1 = list(num1)
        nums2 = list(num2)
        carry = 0
        res = ''

        while nums1 or nums2 or carry:
            value1 = int(nums1.pop()) if nums1 else 0
            value2 = int(nums2.pop()) if nums2 else 0

            value = value1 + value2 + carry

            res = str(value % 10) + res
            carry = value // 10

        return res
