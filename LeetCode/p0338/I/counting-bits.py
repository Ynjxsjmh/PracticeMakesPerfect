# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: counting-bits.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-16 10:39:07
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer `n`, return *an array* `ans` *of
# length* `n + 1` *such that for each* `i` (`0 <= i <= n`)*,* `ans[i]`
# *is the **number of*** `1`***'s** in the binary representation of*
# `i`.
#
# Example 1:
# Input: n = 2
# Output: \[0,1,1\]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# Example 2:
# Input: n = 5
# Output: \[0,1,1,2,1,2\]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
# Constraints:
# *   `0 <= n <= 105`
# ********************************************************************************


class Solution(object):
    def countBits(self, n):
        """从 1 开始
        遇到偶数时，其 1 的个数等于该偶数除以 2 得到的数字的 1 的个数
        遇到奇数时，其 1 的个数等于该奇数除以 2 得到的数字的 1 的个数再加 1
        :type n: int
        :rtype: List[int]
        """

        ans = [0] * (n+1)

        for i in range(1, n+1):
            if i % 2:
                ans[i] = ans[i//2] + 1
            else:
                ans[i] = ans[i//2]

        return ans
