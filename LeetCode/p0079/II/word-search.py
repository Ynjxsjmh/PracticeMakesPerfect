# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: word-search.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-24 23:55:43
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an `m x n` grid of characters `board` and a
# string `word`, return `true` *if* `word` *exists in the grid*.
#
# The word can be constructed from letters of sequentially adjacent
# cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once.
#
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
# Constraints:
# *   `m == board.length`
# *   `n = board[i].length`
# *   `1 <= m, n <= 6`
# *   `1 <= word.length <= 15`
# *   `board` and `word` consists of only lowercase and uppercase English letters.
# ********************************************************************************


class Solution(object):
    def exist(self, board, word):
        """
        遍历 board 矩阵中的每个字符，以该字符为中心，上下左右深搜是否和 word 匹配。
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.search(board, word, i, j, 0):
                    return True

        return False

    # Time Limit Exceeded
    def search(self, board, word, i, j, idx):
        if idx == len(word):
            return True

        m = len(board)
        n = len(board[0])

        res = False
        if board[i][j] == word[idx]:
            char = board[i][j]
            board[i][j] = '#'  # 标记是否访问过
            res = self.search(board, word, (i+1 if i+1 < m else m-1), j, idx+1) or \
                self.search(board, word, i, (j+1 if j+1 < n else n-1), idx+1) or \
                self.search(board, word, (i-1 if i-1 >= 0 else 0), j, idx+1) or \
                self.search(board, word, i, (j-1 if j-1 >= 0 else 0), idx+1)
            board[i][j] = char

        return res

    def search(self, board, word, i, j, idx):
        if idx == len(word):
            return True

        m = len(board)
        n = len(board[0])

        if (i >= m) or (j >= n) or (i < 0) or (j < 0):
            return False

        if board[i][j] != word[idx]:
            return False

        char = board[i][j]
        board[i][j] = '#'  # 标记是否访问过
        res = self.search(board, word, i+1, j, idx+1) or \
            self.search(board, word, i, j+1, idx+1) or \
            self.search(board, word, i-1, j, idx+1) or \
            self.search(board, word, i, j-1, idx+1)
        board[i][j] = char

        return res
