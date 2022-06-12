# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: sqrtx.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 15:25:44
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a non-negative integer `x`, compute and return
# *the square root of* `x`.

# Since the return type is an integer, the decimal digits are
# **truncated**, and only **the integer part** of the result is
# returned.
#
# **Note: **You are not allowed to use any built-in exponent function or
#   operator, such as `pow(x, 0.5)` or `x ** 0.5`.
#
# Example 1:
# Input: x = 4
# Output: 2
#
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
# Constraints:
# *   `0 <= x <= 231 - 1`
# ********************************************************************************

class Solution(object):
    def mySqrt(self, x):
        """找第一个平方比 x 大的
           找最后一个平方比 x 小的
        :type x: int
        :rtype: int
        """

        if x <= 1:
            return x

        l = 0
        r = x

        while l < r:
            m = l + (r - l) / 2

            if m * m <= x:
                l = m + 1
            else:
                r = m

        return l - 1
