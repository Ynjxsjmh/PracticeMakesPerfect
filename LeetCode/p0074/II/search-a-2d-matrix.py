# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: search-a-2d-matrix.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-12 14:11:23
# Last Updated: 
#           By: Ynjxsjmh
# Description: Write an efficient algorithm that searches for a value
# `target` in an `m x n` integer matrix `matrix`. This matrix has the
# following properties:
#
# *   Integers in each row are sorted from left to right.
# *   The first integer of each row is greater than the last
#     integer of the previous row.
#
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
# Constraints:
# *   `m == matrix.length`
# *   `n == matrix[i].length`
# *   `1 <= m, n <= 100`
# *   `-104 <= matrix[i][j], target <= 104`
# ********************************************************************************

class Solution(object):
    def searchMatrix(self, matrix, target):
        """二分查找，因为都是按行递增，且每行最后一个比
        下一行第一个小，因此可以看作一个一维的
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m, n = len(matrix), len(matrix[0])

        l = 0
        r = m * n

        while l < r:
            mid = l + (r - l) / 2

            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                l = mid + 1
            else:
                r = mid

        return False