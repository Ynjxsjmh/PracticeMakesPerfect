# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: number-of-islands.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-02 13:07:33
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an `m x n` 2D binary grid `grid` which represents
# a map of `'1'`s (land) and `'0'`s (water), return *the number of
# islands*.
#
# An **island** is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four
# edges of the grid are all surrounded by water.
#
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# *   `m == grid.length`
# *   `n == grid[i].length`
# *   `1 <= m, n <= 300`
# *   `grid[i][j]` is `'0'` or `'1'`.
# ********************************************************************************


class Solution(object):
    def numIslands(self, grid):
        """并查集
        把二维数组一维化，刚开始每个岛屿在它自己本身的集合里。
        因为要求出为 1 的岛屿集合数量，刚开始数量就为为 1 的岛屿数。

        在遍历各个岛屿的过程中，将右下或左上为 1 的岛屿合并到
        当前岛屿所在的集合里，
        如果右下或左上的岛屿不在集合里，初始化的为 1 岛屿数量减一

        https://oi-wiki.org/ds/dsu/
        https://hackmd.io/@CLKO/rkRVS_o-4
        :type grid: List[List[str]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])

        self.parent = [i for i in range(m * n)]
        self.count = sum([grid[i][j]=='1' for i in range(m) for j in range(n)])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                index = i * n + j

                # (i, j) 右边和下边是不是 1
                if j < n-1 and grid[i][j+1] == '1':
                    self.union(index, index+1)
                if i < m-1 and grid[i+1][j] == '1':
                    self.union(index, index+n)

                # # (i, j) 左边和上边是不是 1
                # # 没右边和下边快
                # if j > 0 and grid[i][j-1] == '1':
                #     self.union(index, index-1)
                # if i > 0 and grid[i-1][j] == '1':
                #     self.union(index, index-n)

        return self.count

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_x] = root_y
        if root_x == root_y:
            return
        self.count -= 1

    def find(self, x):
        # 如果 x 不是祖先，就一直往上一辈找
        while x != self.parent[x]:
            x = self.parent[x]

        return x
