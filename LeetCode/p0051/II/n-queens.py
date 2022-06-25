# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: n-queens.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 09:48:34
# Last Updated: 
#           By: Ynjxsjmh
# Description: The **n-queens** puzzle is the problem of placing `n`
# queens on an `n x n` chessboard such that no two queens attack each
# other.
#
# Given an integer `n`, return *all distinct solutions to the
# **n-queens puzzle***. You may return the answer in **any order**.
#
# Each solution contains a distinct board configuration of the
# n-queens' placement, where `'Q'` and `'.'` both indicate a queen and
# an empty space, respectively.
#
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
#
# Example 2:
# Input: n = 1
# Output: [["Q"]]
#
# Constraints:
# *   `1 <= n <= 9`
# ********************************************************************************


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        possible = [[True for _ in range(n)] for _ in range(n)]
        return self.dfs(n, 0, possible, [], [])

    def dfs(self, n, idx, possible, nqueen, nqueens):
        if len(nqueen) == n:
            nqueens.append(nqueen)
            return nqueens[:]

        res = []
        for i in range(idx, n):
            row = ['.'] * n
            for j in range(n):
                if possible[i][j]:                 # 如果 (i, j) 可以放置
                    row[j] = 'Q'                   # 尝试在 (i, j) 放置皇后
                    possible_ = [lst[:] for lst in possible]

                    ncol = j
                    for nrow in range(i, n):
                        possible[nrow][j] = False  # 和 (i, j) 同一列的不行
                        if ncol+nrow-i < n:        # 和 (i, j) 在同一主对角线的不行
                            possible[nrow][ncol+nrow-i] = False
                        if ncol-(nrow-i) >= 0:     # 和 (i, j) 在同一副主对角线的不行
                            possible[nrow][ncol-(nrow-i)] = False

                    res.extend(self.dfs(n, i+1, possible, nqueen+[''.join(row)], nqueens[:]))

                    possible = [lst[:] for lst in possible_]
                    row[j] = '.'
        return res
