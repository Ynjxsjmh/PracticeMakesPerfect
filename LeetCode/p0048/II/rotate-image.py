# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: rotate-image.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-12 19:19:24
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an `n x n` 2D `matrix` representing an
# image, rotate the image by **90** degrees (clockwise).
#
# You have to rotate the image
# [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm),
# which means you have to modify the input 2D matrix directly. **DO
# NOT** allocate another 2D matrix and do the rotation.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
# Constraints:
# *   `n == matrix.length == matrix[i].length`
# *   `1 <= n <= 20`
# *   `-1000 <= matrix[i][j] <= 1000`
# ********************************************************************************


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # 观察旋转规律可以发现
        # (i, j)    --->  (j, n-1-i)
        #  ^                 |
        #  |                 |
        #  |                 v
        # (n-1-j, i) <--  (n-1-i, n-1-j)

        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
