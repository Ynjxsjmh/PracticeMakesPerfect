# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: sudoku-solver.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-25 22:24:11
# Last Updated: 
#           By: Ynjxsjmh
# Description: Write a program to solve a Sudoku puzzle by filling the
# empty cells.
#
# A sudoku solution must satisfy **all of the following rules**:
#
# 1.  Each of the digits `1-9` must occur exactly once in each row.
# 2.  Each of the digits `1-9` must occur exactly once in each column.
# 3.  Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.
#
# The `'.'` character indicates empty cells.
#
# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."]
# ["6",".",".","1","9","5",".",".","."]
# [".","9","8",".",".",".",".","6","."]
# ["8",".",".",".","6",".",".",".","3"]
# ["4",".",".","8",".","3",".",".","1"]
# ["7",".",".",".","2",".",".",".","6"]
# [".","6",".",".",".",".","2","8","."]
# [".",".",".","4","1","9",".",".","5"]
# [".",".",".",".","8",".",".","7","9"]]

# Output: [["5","3","4","6","7","8","9","1","2"]
# ["6","7","2","1","9","5","3","4","8"]
# ["1","9","8","3","4","2","5","6","7"]
# ["8","5","9","7","6","1","4","2","3"]
# ["4","2","6","8","5","3","7","9","1"]
# ["7","1","3","9","2","4","8","5","6"]
# ["9","6","1","5","3","7","2","8","4"]
# ["2","8","7","4","1","9","6","3","5"]
# ["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
# Constraints:
# *   `board.length == 9`
# *   `board[i].length == 9`
# *   `board[i][j]` is a digit or `'.'`.
# *   It is **guaranteed** that the input board has only one solution.
# ********************************************************************************


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.dfs(board, 0, 0)

    def dfs(self, board, i, j):
        if i == 9:
            return True

        # 换到下一行第一列
        if j >= 9:
            return self.dfs(board, i+1, 0)

        if board[i][j] == '.':
            for num in range(1, 10):
                if not self.is_valid(board, str(num), i, j):
                    continue

                board[i][j] = str(num)
                res = self.dfs(board, i, j+1)
                if res:
                    return True
            board[i][j] = '.'
            return False
        else:
            # 当前 (i, j) 为数字，换到下一列
            return self.dfs(board, i, j+1)

    def is_valid(self, board, num, i, j):
        if num in board[i][:]:
            return False

        # board[:][j] 返回的是第 j 行？
        if num in [board[r][j] for r in range(9)]:
            return False

        box = [board[r][c]
               for r in range((i//3)*3, (i//3)*3+3)
               for c in range((j//3)*3, (j//3)*3+3)]
        if num in box:
            return False

        return True
