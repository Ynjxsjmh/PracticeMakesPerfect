# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: set-matrix-zeroes.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-11 10:48:17
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an `m x n` integer matrix `matrix`, if an element
# is `0`, set its entire row and column to `0`'s.
#
# You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).
#
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
# Constraints:
# *   `m == matrix.length`
# *   `n == matrix[0].length`
# *   `1 <= m, n <= 200`
# *   `-231 <= matrix[i][j] <= 231 - 1`
# ********************************************************************************


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        # 记录当前行，当前列是否有 0
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # 把行，列分别置 0
                    row[i] = True
                    col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        return matrix
