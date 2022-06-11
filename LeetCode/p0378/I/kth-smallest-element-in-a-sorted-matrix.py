# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: kth-smallest-element-in-a-sorted-matrix.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-11 20:46:13
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an `n x n` `matrix` where each of the rows and
# columns is sorted in ascending order, return *the* `kth` *smallest
# element in the matrix*.
#
# Note that it is the `kth` smallest element **in the sorted order**,
# not the `kth` **distinct** element.
#
# You must find a solution with a memory complexity better than
# `O(n2)`.
#
# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are
# [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5
#
# Constraints:
#    `n == matrix.length == matrix[i].length`
#    `1 <= n <= 300`
#    `-109 <= matrix[i][j] <= 109`
#    All the rows and columns of `matrix` are guaranteed to be sorted in non-decreasing order.
#    `1 <= k <= n2`
# ********************************************************************************

import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """使用最大堆来实现
        但是 Python 的 heapq 其实是个最小堆
        堆里面只会保存较小的数
        我们将所有数去相反后，最小也就成了最大
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        nrow, ncol = len(matrix), len(matrix[0])
        maxHeap = []

        for row in range(nrow):
            for col in range(ncol):
                heapq.heappush(maxHeap, -matrix[row][col])

                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        return -heapq.heappop(maxHeap)
