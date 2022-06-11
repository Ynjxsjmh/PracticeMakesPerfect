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
        每当堆大小超过 k 时，我们就移除最大的那一个，
        这样的话，最后我们就可以剩下 k 个最小的了。
        由于根是最大的，根就是第 k 个最小的。
        Python heapq 实现的是最小堆，取相反数模拟
        最大堆。
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
