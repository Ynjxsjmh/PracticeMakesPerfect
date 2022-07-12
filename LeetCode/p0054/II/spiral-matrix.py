# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: spiral-matrix.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-12 16:15:39
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an `m x n` `matrix`, return *all elements of the*
# `matrix` *in spiral order*.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# Constraints:
# *   `m == matrix.length`
# *   `n == matrix[i].length`
# *   `1 <= m, n <= 10`
# *   `-100 <= matrix[i][j] <= 100`
# ********************************************************************************


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []

        while len(res) != m * n:
            # 从左往右
            while j < n and matrix[i][j] != '-':
                res.append(matrix[i][j])
                matrix[i][j] = '-'
                j += 1
            # 校准到下一个合法位置
            j -= 1
            i += 1

            # 从上往下
            while i < m and matrix[i][j] != '-':
                res.append(matrix[i][j])
                matrix[i][j] = '-'
                i += 1
            i -= 1
            j -= 1

            # 从右往左
            while j > -1 and matrix[i][j] != '-':
                res.append(matrix[i][j])
                matrix[i][j] = '-'
                j -= 1
            j += 1
            i -= 1

            # 从下往上
            while i > -1 and matrix[i][j] != '-':
                res.append(matrix[i][j])
                matrix[i][j] = '-'
                i -= 1
            i += 1
            j += 1

        return res
