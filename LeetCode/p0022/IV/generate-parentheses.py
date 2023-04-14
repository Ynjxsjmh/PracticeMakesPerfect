# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: generate-parentheses.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 16:36:36
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = self.generate(0, 0, n, '')

        return res

    def generate(self, n_left, n_right, n, mid_res):
        # 用了几个左括号，用了几个右括号

        # 左括号一定比右括号多，否则不合法
        if n_right > n_left:
            return

        if n_left == n and n_right == n:
            # 双重判断，防止不合法
            return [mid_res]

        res = []

        if n_left < n:
            res1 = self.generate(n_left+1, n_right, n, mid_res+'(')
            if res1:
                res.extend(res1)

        if n_right < n:
            res2 = self.generate(n_left, n_right+1, n, mid_res+')')
            if res2:
                res.extend(res2)

        return res
