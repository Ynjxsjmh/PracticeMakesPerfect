# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: search-a-2d-matrix-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 14:34:08
# Last Updated: 
#           By: Ynjxsjmh
# Description: Write an efficient algorithm that searches for a value
# `target` in an `m x n` integer matrix `matrix`. This matrix has the
# following properties:
#
# *   Integers in each row are sorted in ascending from left to right.
# *   Integers in each column are sorted in ascending from top to bottom.
#
# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
#
# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
#
# Constraints:
# *   `m == matrix.length`
# *   `n == matrix[i].length`
# *   `1 <= n, m <= 300`
# *   `-109 <= matrix[i][j] <= 109`
# *   All the integers in each row are **sorted** in ascending order.
# *   All the integers in each column are **sorted** in ascending order.
# *   `-109 <= target <= 109`
# ********************************************************************************

class Solution(object):
    def searchMatrix(self, matrix, target):
        """利用矩阵中左下右上数的特殊性来搜索
        左下角的数往上变小，往右变大
        右上角的数往下变大，往左变小
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nrow, ncol = len(matrix), len(matrix[0])

        x = 0
        y = ncol - 1

        while (x < nrow) and (y >= 0):
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1

        return False
